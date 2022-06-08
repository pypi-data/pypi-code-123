# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['LinkArgs', 'Link']

@pulumi.input_type
class LinkArgs:
    def __init__(__self__, *,
                 hub_name: pulumi.Input[str],
                 participant_property_references: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]],
                 resource_group_name: pulumi.Input[str],
                 source_interaction_type: pulumi.Input[str],
                 target_profile_type: pulumi.Input[str],
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 link_name: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]]] = None,
                 operation_type: Optional[pulumi.Input['InstanceOperationType']] = None,
                 reference_only: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Link resource.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]] participant_property_references: The properties that represent the participating profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] source_interaction_type: Name of the source Interaction Type.
        :param pulumi.Input[str] target_profile_type: Name of the target Profile Type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the Link.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display name for the Link.
        :param pulumi.Input[str] link_name: The name of the link.
        :param pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]] mappings: The set of properties mappings between the source and target Types.
        :param pulumi.Input['InstanceOperationType'] operation_type: Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        :param pulumi.Input[bool] reference_only: Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        """
        pulumi.set(__self__, "hub_name", hub_name)
        pulumi.set(__self__, "participant_property_references", participant_property_references)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_interaction_type", source_interaction_type)
        pulumi.set(__self__, "target_profile_type", target_profile_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if link_name is not None:
            pulumi.set(__self__, "link_name", link_name)
        if mappings is not None:
            pulumi.set(__self__, "mappings", mappings)
        if operation_type is not None:
            pulumi.set(__self__, "operation_type", operation_type)
        if reference_only is not None:
            pulumi.set(__self__, "reference_only", reference_only)

    @property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[str]:
        """
        The name of the hub.
        """
        return pulumi.get(self, "hub_name")

    @hub_name.setter
    def hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "hub_name", value)

    @property
    @pulumi.getter(name="participantPropertyReferences")
    def participant_property_references(self) -> pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]:
        """
        The properties that represent the participating profile.
        """
        return pulumi.get(self, "participant_property_references")

    @participant_property_references.setter
    def participant_property_references(self, value: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]):
        pulumi.set(self, "participant_property_references", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sourceInteractionType")
    def source_interaction_type(self) -> pulumi.Input[str]:
        """
        Name of the source Interaction Type.
        """
        return pulumi.get(self, "source_interaction_type")

    @source_interaction_type.setter
    def source_interaction_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_interaction_type", value)

    @property
    @pulumi.getter(name="targetProfileType")
    def target_profile_type(self) -> pulumi.Input[str]:
        """
        Name of the target Profile Type.
        """
        return pulumi.get(self, "target_profile_type")

    @target_profile_type.setter
    def target_profile_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_profile_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized descriptions for the Link.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized display name for the Link.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="linkName")
    def link_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the link.
        """
        return pulumi.get(self, "link_name")

    @link_name.setter
    def link_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "link_name", value)

    @property
    @pulumi.getter
    def mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]]]:
        """
        The set of properties mappings between the source and target Types.
        """
        return pulumi.get(self, "mappings")

    @mappings.setter
    def mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]]]):
        pulumi.set(self, "mappings", value)

    @property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[pulumi.Input['InstanceOperationType']]:
        """
        Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        """
        return pulumi.get(self, "operation_type")

    @operation_type.setter
    def operation_type(self, value: Optional[pulumi.Input['InstanceOperationType']]):
        pulumi.set(self, "operation_type", value)

    @property
    @pulumi.getter(name="referenceOnly")
    def reference_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        """
        return pulumi.get(self, "reference_only")

    @reference_only.setter
    def reference_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reference_only", value)


warnings.warn("""Version v20170101 will be removed in the next major version of the provider. Upgrade to version v20170426 or later.""", DeprecationWarning)


class Link(pulumi.CustomResource):
    warnings.warn("""Version v20170101 will be removed in the next major version of the provider. Upgrade to version v20170426 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 link_name: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TypePropertiesMappingArgs']]]]] = None,
                 operation_type: Optional[pulumi.Input['InstanceOperationType']] = None,
                 participant_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]]] = None,
                 reference_only: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_interaction_type: Optional[pulumi.Input[str]] = None,
                 target_profile_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The link resource format.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the Link.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display name for the Link.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[str] link_name: The name of the link.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TypePropertiesMappingArgs']]]] mappings: The set of properties mappings between the source and target Types.
        :param pulumi.Input['InstanceOperationType'] operation_type: Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]] participant_property_references: The properties that represent the participating profile.
        :param pulumi.Input[bool] reference_only: Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] source_interaction_type: Name of the source Interaction Type.
        :param pulumi.Input[str] target_profile_type: Name of the target Profile Type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The link resource format.

        :param str resource_name: The name of the resource.
        :param LinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 link_name: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TypePropertiesMappingArgs']]]]] = None,
                 operation_type: Optional[pulumi.Input['InstanceOperationType']] = None,
                 participant_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]]] = None,
                 reference_only: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_interaction_type: Optional[pulumi.Input[str]] = None,
                 target_profile_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Link is deprecated: Version v20170101 will be removed in the next major version of the provider. Upgrade to version v20170426 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkArgs.__new__(LinkArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'hub_name'")
            __props__.__dict__["hub_name"] = hub_name
            __props__.__dict__["link_name"] = link_name
            __props__.__dict__["mappings"] = mappings
            __props__.__dict__["operation_type"] = operation_type
            if participant_property_references is None and not opts.urn:
                raise TypeError("Missing required property 'participant_property_references'")
            __props__.__dict__["participant_property_references"] = participant_property_references
            __props__.__dict__["reference_only"] = reference_only
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source_interaction_type is None and not opts.urn:
                raise TypeError("Missing required property 'source_interaction_type'")
            __props__.__dict__["source_interaction_type"] = source_interaction_type
            if target_profile_type is None and not opts.urn:
                raise TypeError("Missing required property 'target_profile_type'")
            __props__.__dict__["target_profile_type"] = target_profile_type
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:customerinsights:Link"), pulumi.Alias(type_="azure-native:customerinsights/v20170426:Link")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Link, __self__).__init__(
            'azure-native:customerinsights/v20170101:Link',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Link':
        """
        Get an existing Link resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LinkArgs.__new__(LinkArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["link_name"] = None
        __props__.__dict__["mappings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation_type"] = None
        __props__.__dict__["participant_property_references"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["reference_only"] = None
        __props__.__dict__["source_interaction_type"] = None
        __props__.__dict__["target_profile_type"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return Link(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized descriptions for the Link.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized display name for the Link.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="linkName")
    def link_name(self) -> pulumi.Output[str]:
        """
        The link name.
        """
        return pulumi.get(self, "link_name")

    @property
    @pulumi.getter
    def mappings(self) -> pulumi.Output[Optional[Sequence['outputs.TypePropertiesMappingResponse']]]:
        """
        The set of properties mappings between the source and target Types.
        """
        return pulumi.get(self, "mappings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> pulumi.Output[Optional[str]]:
        """
        Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        """
        return pulumi.get(self, "operation_type")

    @property
    @pulumi.getter(name="participantPropertyReferences")
    def participant_property_references(self) -> pulumi.Output[Sequence['outputs.ParticipantPropertyReferenceResponse']]:
        """
        The properties that represent the participating profile.
        """
        return pulumi.get(self, "participant_property_references")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="referenceOnly")
    def reference_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        """
        return pulumi.get(self, "reference_only")

    @property
    @pulumi.getter(name="sourceInteractionType")
    def source_interaction_type(self) -> pulumi.Output[str]:
        """
        Name of the source Interaction Type.
        """
        return pulumi.get(self, "source_interaction_type")

    @property
    @pulumi.getter(name="targetProfileType")
    def target_profile_type(self) -> pulumi.Output[str]:
        """
        Name of the target Profile Type.
        """
        return pulumi.get(self, "target_profile_type")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

