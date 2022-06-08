# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class OrmTag(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'color': 'str',
        'created_dt': 'datetime',
        'edges': 'OrmTagEdges',
        'id': 'int',
        'name': 'str',
        'tag_tag_group': 'int',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'color': 'color',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'name': 'name',
        'tag_tag_group': 'tag_tag_group',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, color=None, created_dt=None, edges=None, id=None, name=None, tag_tag_group=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmTag - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._color = None
        self._created_dt = None
        self._edges = None
        self._id = None
        self._name = None
        self._tag_tag_group = None
        self._updated_dt = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag_tag_group is not None:
            self.tag_tag_group = tag_tag_group
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def color(self):
        """Gets the color of this OrmTag.  # noqa: E501


        :return: The color of this OrmTag.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this OrmTag.


        :param color: The color of this OrmTag.  # noqa: E501
        :type color: str
        """

        self._color = color

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmTag.  # noqa: E501


        :return: The created_dt of this OrmTag.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmTag.


        :param created_dt: The created_dt of this OrmTag.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmTag.  # noqa: E501


        :return: The edges of this OrmTag.  # noqa: E501
        :rtype: OrmTagEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmTag.


        :param edges: The edges of this OrmTag.  # noqa: E501
        :type edges: OrmTagEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmTag.  # noqa: E501


        :return: The id of this OrmTag.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmTag.


        :param id: The id of this OrmTag.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrmTag.  # noqa: E501


        :return: The name of this OrmTag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrmTag.


        :param name: The name of this OrmTag.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def tag_tag_group(self):
        """Gets the tag_tag_group of this OrmTag.  # noqa: E501


        :return: The tag_tag_group of this OrmTag.  # noqa: E501
        :rtype: int
        """
        return self._tag_tag_group

    @tag_tag_group.setter
    def tag_tag_group(self, tag_tag_group):
        """Sets the tag_tag_group of this OrmTag.


        :param tag_tag_group: The tag_tag_group of this OrmTag.  # noqa: E501
        :type tag_tag_group: int
        """

        self._tag_tag_group = tag_tag_group

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmTag.  # noqa: E501


        :return: The updated_dt of this OrmTag.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmTag.


        :param updated_dt: The updated_dt of this OrmTag.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrmTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmTag):
            return True

        return self.to_dict() != other.to_dict()
