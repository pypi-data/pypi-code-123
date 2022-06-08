import re
from collections import OrderedDict
from typing import Callable, Optional, Tuple, Type

import sqlalchemy
from graphene import Field
from graphene.relay import Connection, Node
from graphene.types.objecttype import ObjectType, ObjectTypeOptions
from graphene.types.utils import yank_fields_from_attrs
from graphene.utils.orderedtype import OrderedType
from graphql import GraphQLResolveInfo
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import (
    ColumnProperty,
    CompositeProperty,
    DeclarativeMeta,
    RelationshipProperty,
)

from .converter import (
    convert_sqlalchemy_column,
    convert_sqlalchemy_composite,
    convert_sqlalchemy_fk,
    convert_sqlalchemy_fk_reverse,
    convert_sqlalchemy_hybrid_method,
    convert_sqlalchemy_relationship,
)
from .enums import (
    enum_for_field,
    sort_argument_for_object_type,
    sort_enum_for_object_type,
)
from .node import AsyncNode
from .registry import Registry, get_global_registry
from .resolvers import get_attr_resolver, get_custom_resolver
from .utils import get_query, is_mapped_class, is_mapped_instance


class ORMField(OrderedType):
    def __init__(
        self,
        model_attr: str = None,
        type_=None,
        required: bool = None,
        description: str = None,
        deprecation_reason: str = None,
        batching: bool = None,
        _creation_counter: int = None,
        **field_kwargs,
    ):
        """
        Use this to override fields automatically generated by SQLAlchemyObjectType.
        Unless specified, options will default to SQLAlchemyObjectType usual behavior
        for the given SQLAlchemy model property.

        Usage:
            class MyModel(Base):
                id = Column(Integer(), primary_key=True)
                name = Column(String)

            class MyType(SQLAlchemyObjectType):
                class Meta:
                    model = MyModel

                id = ORMField(type=graphene.Int)
                name = ORMField(required=True)

        -> MyType.id will be of type Int (vs ID).
        -> MyType.name will be of type NonNull(String) (vs String).

        :param str model_attr:
            Name of the SQLAlchemy model attribute used to resolve this field.
            Default to the name of the attribute referencing the ORMField.
        :param type_:
            Default to the type mapping in converter.py.
        :param str description:
            Default to the `doc` attribute of the SQLAlchemy column property.
        :param bool required:
            Default to the opposite of the `nullable` attribute of the SQLAlchemy column property.
        :param str description:
            Same behavior as in graphene.Field. Defaults to None.
        :param str deprecation_reason:
            Same behavior as in graphene.Field. Defaults to None.
        :param bool batching:
            Toggle SQL batching. Defaults to None, that is `SQLAlchemyObjectType.meta.batching`.
        :param int _creation_counter:
            Same behavior as in graphene.Field.
        """
        super().__init__(_creation_counter=_creation_counter)
        # The is only useful for documentation and auto-completion
        common_kwargs = {
            "model_attr": model_attr,
            "type_": type_,
            "required": required,
            "description": description,
            "deprecation_reason": deprecation_reason,
            "batching": batching,
        }
        common_kwargs = {
            kwarg: value for kwarg, value in common_kwargs.items() if value is not None
        }
        self.kwargs = field_kwargs
        self.kwargs.update(common_kwargs)


def construct_fields(
    obj_type: Type["SQLAlchemyObjectType"],
    model: DeclarativeMeta,
    registry: Registry,
    only_fields: Tuple[str, ...],
    exclude_fields: Tuple[str, ...],
    connection_field_factory: Optional[Callable],
) -> OrderedDict[str, Field]:
    """
    Construct all the fields for a SQLAlchemyObjectType.
    The main steps are:
      - Gather all the relevant attributes from the SQLAlchemy model
      - Gather all the ORM fields defined on the type
      - Merge in overrides and build up all the fields
    """
    inspected_model = sqlalchemy.inspect(model)
    # Gather all the relevant attributes from the SQLAlchemy model in order
    all_model_attrs = OrderedDict(
        inspected_model.column_attrs.items()
        + inspected_model.composites.items()
        + [
            (name, item)
            for name, item in inspected_model.all_orm_descriptors.items()
            if isinstance(item, hybrid_property)
        ]
        + inspected_model.relationships.items()
    )

    # Filter out excluded fields
    auto_orm_field_names = []
    for attr_name, attr in all_model_attrs.items():
        if (only_fields and attr_name not in only_fields) or (
            attr_name in exclude_fields
        ):
            continue
        auto_orm_field_names.append(attr_name)

    # Gather all the ORM fields defined on the type
    custom_orm_fields_items = [
        (attn_name, attr)
        for base in reversed(obj_type.__mro__)
        for attn_name, attr in base.__dict__.items()
        if isinstance(attr, ORMField)
    ]
    custom_orm_fields_items = sorted(custom_orm_fields_items, key=lambda item: item[1])

    # Set the model_attr if not set
    for orm_field_name, orm_field in custom_orm_fields_items:
        attr_name = orm_field.kwargs.get("model_attr", orm_field_name)
        if attr_name not in all_model_attrs:
            raise ValueError(
                (
                    f"Cannot map ORMField to a model attribute.\n"
                    f"Field: '{obj_type.__name__}.{orm_field_name}'"
                )
            )
        orm_field.kwargs["model_attr"] = attr_name

    # Merge automatic fields with custom ORM fields
    orm_fields = OrderedDict(custom_orm_fields_items)
    for orm_field_name in auto_orm_field_names:
        if orm_field_name in orm_fields:
            continue
        orm_fields[orm_field_name] = ORMField(model_attr=orm_field_name)

    # Build all the field dictionary
    auto_fields = OrderedDict()
    for mapper in inspected_model.registry.mappers:
        for fk in mapper.local_table.foreign_keys:
            if inspected_model.selectable == fk.column.table:
                orm_field_name = str(fk.parent.table.fullname)
                if (only_fields and orm_field_name not in only_fields) or (
                    orm_field_name in exclude_fields
                ):
                    continue
                auto_fields[orm_field_name] = convert_sqlalchemy_fk_reverse(
                    fk, obj_type
                )

    for fk in inspected_model.mapped_table.foreign_keys:
        orm_field_name = re.sub(r"_(?:id|pk)$", "", fk.parent.key)
        if (only_fields and orm_field_name not in only_fields) or (
            orm_field_name in exclude_fields
        ):
            continue
        auto_fields[orm_field_name] = convert_sqlalchemy_fk(
            fk,
            obj_type,
            orm_field_name,
        )

    fields = OrderedDict()
    for orm_field_name, orm_field in orm_fields.items():
        attr_name = orm_field.kwargs.pop("model_attr")
        attr = all_model_attrs[attr_name]
        resolver = get_custom_resolver(obj_type, orm_field_name) or get_attr_resolver(
            attr_name
        )

        if isinstance(attr, ColumnProperty):
            field = convert_sqlalchemy_column(
                attr, registry, resolver, **orm_field.kwargs
            )
        elif isinstance(attr, RelationshipProperty):
            field = convert_sqlalchemy_relationship(
                attr,
                obj_type,
                connection_field_factory,
                orm_field_name,
                **orm_field.kwargs,
            )
        elif isinstance(attr, CompositeProperty):
            if attr_name != orm_field_name or orm_field.kwargs:
                # TODO Add a way to override composite property fields
                raise ValueError(
                    "ORMField kwargs for composite fields must be empty. "
                    f"Field: {obj_type.__name__}.{orm_field_name}"
                )
            field = convert_sqlalchemy_composite(attr, registry, resolver)
        elif isinstance(attr, hybrid_property):
            field = convert_sqlalchemy_hybrid_method(attr, resolver, **orm_field.kwargs)
        else:
            raise Exception("Property type is not supported")  # Should never happen

        registry.register_orm_field(obj_type, orm_field_name, attr)
        fields[orm_field_name] = field

    return OrderedDict(auto_fields | fields)


class SQLAlchemyObjectTypeOptions(ObjectTypeOptions):
    model: Type[DeclarativeMeta] = None
    registry: Registry = None
    connection: Type[Connection] = None
    id: str = None


class SQLAlchemyObjectType(ObjectType):
    _meta: SQLAlchemyObjectTypeOptions

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        model: DeclarativeMeta = None,
        registry: Registry = None,
        skip_registry=False,
        only_fields=(),
        exclude_fields=(),
        connection=None,
        connection_class=None,
        use_connection=None,
        interfaces=(),
        id=None,
        connection_field_factory=None,
        _meta=None,
        **options,
    ):
        assert is_mapped_class(model), (
            "You need to pass a valid SQLAlchemy Model in "
            f'{cls.__name__}.Meta, received "{model}".'
        )

        if not registry:
            registry = get_global_registry()

        assert isinstance(registry, Registry), (
            f"The attribute registry in {cls.__name__} needs to be an instance of "
            f'Registry, received "{registry}".'
        )

        if only_fields and exclude_fields:
            raise ValueError(
                "The options 'only_fields' and 'exclude_fields' cannot be both set on the same type."
            )

        sqla_fields = yank_fields_from_attrs(
            construct_fields(
                obj_type=cls,
                model=model,
                registry=registry,
                only_fields=only_fields,
                exclude_fields=exclude_fields,
                connection_field_factory=connection_field_factory,
            ),
            _as=Field,
            sort=False,
        )

        if use_connection is None and interfaces:
            use_connection = any(
                issubclass(interface, (Node, AsyncNode)) for interface in interfaces
            )

        if use_connection and not connection:
            # We create the connection automatically
            if not connection_class:
                connection_class = Connection

            connection = connection_class.create_type(
                f"{cls.__name__}Connection", node=cls
            )

        if connection is not None:
            assert issubclass(
                connection, Connection
            ), f"The connection must be a Connection. Received {connection.__name__}"

        if not _meta:
            _meta = SQLAlchemyObjectTypeOptions(cls)

        _meta.model = model
        _meta.registry = registry

        if _meta.fields:
            _meta.fields.update(sqla_fields)
        else:
            _meta.fields = sqla_fields

        _meta.connection = connection
        _meta.id = id or "id"

        if options.get("filter_fields"):
            _meta.filter_fields = options["filter_fields"]

        cls.connection = connection  # Public way to get the connection

        super().__init_subclass_with_meta__(
            _meta=_meta, interfaces=interfaces, **options
        )

        if not skip_registry:
            registry.register(cls)

    @classmethod
    def is_type_of(cls, root, info: GraphQLResolveInfo):
        if isinstance(root, cls):
            return True
        if not is_mapped_instance(root):
            raise Exception(f'Received incompatible instance "{root}".')
        return isinstance(root, cls._meta.model)

    @classmethod
    async def get_query(cls, info: GraphQLResolveInfo):
        return get_query(cls._meta.model, info, cls.__name__)

    @classmethod
    async def get_node(cls, info: GraphQLResolveInfo, id):
        session = info.context.session

        pk = sqlalchemy.inspect(cls._meta.model).primary_key[0]
        q = (await cls.get_query(info)).where(pk == id)
        obj = (await session.execute(q)).first()
        if obj:
            result = cls(**obj)
            return result

    async def resolve_id(self, info: GraphQLResolveInfo):
        key = "id"
        if isinstance(self, SQLAlchemyObjectType):
            model = self._meta.model
            key = model.__mapper__.primary_key[0].key
        return getattr(self, key, None)

    @classmethod
    def enum_for_field(cls, field_name):
        return enum_for_field(cls, field_name)

    @classmethod
    async def _resolve_reference_bulk(cls, model_instance, info):
        for field in info.parent_type.fields.values():
            if hasattr(field.type, "name"):
                field_type_name = field.type.name
                if (
                    field_type_name.endswith("Connection")
                    and field_type_name[:-10] == info.context.representation
                ):
                    return await field.resolve(model_instance, info)

    sort_enum = classmethod(sort_enum_for_object_type)

    sort_argument = classmethod(sort_argument_for_object_type)
