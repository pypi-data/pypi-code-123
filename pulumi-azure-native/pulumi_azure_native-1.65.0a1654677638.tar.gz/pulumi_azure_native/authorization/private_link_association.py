# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['PrivateLinkAssociationArgs', 'PrivateLinkAssociation']

@pulumi.input_type
class PrivateLinkAssociationArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 pla_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['PrivateLinkAssociationPropertiesArgs']] = None):
        """
        The set of arguments for constructing a PrivateLinkAssociation resource.
        :param pulumi.Input[str] group_id: The management group ID.
        :param pulumi.Input[str] pla_id: The ID of the PLA
        :param pulumi.Input['PrivateLinkAssociationPropertiesArgs'] properties: The properties of the PrivateLinkAssociation.
        """
        pulumi.set(__self__, "group_id", group_id)
        if pla_id is not None:
            pulumi.set(__self__, "pla_id", pla_id)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The management group ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="plaId")
    def pla_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the PLA
        """
        return pulumi.get(self, "pla_id")

    @pla_id.setter
    def pla_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pla_id", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['PrivateLinkAssociationPropertiesArgs']]:
        """
        The properties of the PrivateLinkAssociation.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['PrivateLinkAssociationPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class PrivateLinkAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 pla_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['PrivateLinkAssociationPropertiesArgs']]] = None,
                 __props__=None):
        """
        API Version: 2020-05-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The management group ID.
        :param pulumi.Input[str] pla_id: The ID of the PLA
        :param pulumi.Input[pulumi.InputType['PrivateLinkAssociationPropertiesArgs']] properties: The properties of the PrivateLinkAssociation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateLinkAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        API Version: 2020-05-01.

        :param str resource_name: The name of the resource.
        :param PrivateLinkAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateLinkAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 pla_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['PrivateLinkAssociationPropertiesArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateLinkAssociationArgs.__new__(PrivateLinkAssociationArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["pla_id"] = pla_id
            __props__.__dict__["properties"] = properties
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization/v20200501:PrivateLinkAssociation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateLinkAssociation, __self__).__init__(
            'azure-native:authorization:PrivateLinkAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateLinkAssociation':
        """
        Get an existing PrivateLinkAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateLinkAssociationArgs.__new__(PrivateLinkAssociationArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return PrivateLinkAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The pla name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.PrivateLinkAssociationPropertiesExpandedResponse']:
        """
        The private link association properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The operation type.
        """
        return pulumi.get(self, "type")

