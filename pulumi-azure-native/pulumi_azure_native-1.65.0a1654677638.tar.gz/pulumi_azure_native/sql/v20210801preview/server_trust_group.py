# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ServerTrustGroupArgs', 'ServerTrustGroup']

@pulumi.input_type
class ServerTrustGroupArgs:
    def __init__(__self__, *,
                 group_members: pulumi.Input[Sequence[pulumi.Input['ServerInfoArgs']]],
                 location_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 trust_scopes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 server_trust_group_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerTrustGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['ServerInfoArgs']]] group_members: Group members information for the server trust group.
        :param pulumi.Input[str] location_name: The name of the region where the resource is located.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trust_scopes: Trust scope of the server trust group.
        :param pulumi.Input[str] server_trust_group_name: The name of the server trust group.
        """
        pulumi.set(__self__, "group_members", group_members)
        pulumi.set(__self__, "location_name", location_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "trust_scopes", trust_scopes)
        if server_trust_group_name is not None:
            pulumi.set(__self__, "server_trust_group_name", server_trust_group_name)

    @property
    @pulumi.getter(name="groupMembers")
    def group_members(self) -> pulumi.Input[Sequence[pulumi.Input['ServerInfoArgs']]]:
        """
        Group members information for the server trust group.
        """
        return pulumi.get(self, "group_members")

    @group_members.setter
    def group_members(self, value: pulumi.Input[Sequence[pulumi.Input['ServerInfoArgs']]]):
        pulumi.set(self, "group_members", value)

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> pulumi.Input[str]:
        """
        The name of the region where the resource is located.
        """
        return pulumi.get(self, "location_name")

    @location_name.setter
    def location_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "location_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="trustScopes")
    def trust_scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Trust scope of the server trust group.
        """
        return pulumi.get(self, "trust_scopes")

    @trust_scopes.setter
    def trust_scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "trust_scopes", value)

    @property
    @pulumi.getter(name="serverTrustGroupName")
    def server_trust_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server trust group.
        """
        return pulumi.get(self, "server_trust_group_name")

    @server_trust_group_name.setter
    def server_trust_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_trust_group_name", value)


class ServerTrustGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerInfoArgs']]]]] = None,
                 location_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_trust_group_name: Optional[pulumi.Input[str]] = None,
                 trust_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A server trust group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerInfoArgs']]]] group_members: Group members information for the server trust group.
        :param pulumi.Input[str] location_name: The name of the region where the resource is located.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_trust_group_name: The name of the server trust group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trust_scopes: Trust scope of the server trust group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerTrustGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A server trust group.

        :param str resource_name: The name of the resource.
        :param ServerTrustGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerTrustGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerInfoArgs']]]]] = None,
                 location_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_trust_group_name: Optional[pulumi.Input[str]] = None,
                 trust_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = ServerTrustGroupArgs.__new__(ServerTrustGroupArgs)

            if group_members is None and not opts.urn:
                raise TypeError("Missing required property 'group_members'")
            __props__.__dict__["group_members"] = group_members
            if location_name is None and not opts.urn:
                raise TypeError("Missing required property 'location_name'")
            __props__.__dict__["location_name"] = location_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["server_trust_group_name"] = server_trust_group_name
            if trust_scopes is None and not opts.urn:
                raise TypeError("Missing required property 'trust_scopes'")
            __props__.__dict__["trust_scopes"] = trust_scopes
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ServerTrustGroup"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ServerTrustGroup"), pulumi.Alias(type_="azure-native:sql/v20200801preview:ServerTrustGroup"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ServerTrustGroup"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ServerTrustGroup"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ServerTrustGroup"), pulumi.Alias(type_="azure-native:sql/v20211101preview:ServerTrustGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerTrustGroup, __self__).__init__(
            'azure-native:sql/v20210801preview:ServerTrustGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerTrustGroup':
        """
        Get an existing ServerTrustGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerTrustGroupArgs.__new__(ServerTrustGroupArgs)

        __props__.__dict__["group_members"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["trust_scopes"] = None
        __props__.__dict__["type"] = None
        return ServerTrustGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupMembers")
    def group_members(self) -> pulumi.Output[Sequence['outputs.ServerInfoResponse']]:
        """
        Group members information for the server trust group.
        """
        return pulumi.get(self, "group_members")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="trustScopes")
    def trust_scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        Trust scope of the server trust group.
        """
        return pulumi.get(self, "trust_scopes")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

