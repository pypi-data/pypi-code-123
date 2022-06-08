# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['LinkedServerArgs', 'LinkedServer']

@pulumi.input_type
class LinkedServerArgs:
    def __init__(__self__, *,
                 linked_redis_cache_id: pulumi.Input[str],
                 linked_redis_cache_location: pulumi.Input[str],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_role: pulumi.Input['ReplicationRole'],
                 linked_server_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LinkedServer resource.
        :param pulumi.Input[str] linked_redis_cache_id: Fully qualified resourceId of the linked redis cache.
        :param pulumi.Input[str] linked_redis_cache_location: Location of the linked redis cache.
        :param pulumi.Input[str] name: The name of the Redis cache.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['ReplicationRole'] server_role: Role of the linked server.
        :param pulumi.Input[str] linked_server_name: The name of the linked server that is being added to the Redis cache.
        """
        pulumi.set(__self__, "linked_redis_cache_id", linked_redis_cache_id)
        pulumi.set(__self__, "linked_redis_cache_location", linked_redis_cache_location)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_role", server_role)
        if linked_server_name is not None:
            pulumi.set(__self__, "linked_server_name", linked_server_name)

    @property
    @pulumi.getter(name="linkedRedisCacheId")
    def linked_redis_cache_id(self) -> pulumi.Input[str]:
        """
        Fully qualified resourceId of the linked redis cache.
        """
        return pulumi.get(self, "linked_redis_cache_id")

    @linked_redis_cache_id.setter
    def linked_redis_cache_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "linked_redis_cache_id", value)

    @property
    @pulumi.getter(name="linkedRedisCacheLocation")
    def linked_redis_cache_location(self) -> pulumi.Input[str]:
        """
        Location of the linked redis cache.
        """
        return pulumi.get(self, "linked_redis_cache_location")

    @linked_redis_cache_location.setter
    def linked_redis_cache_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "linked_redis_cache_location", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the Redis cache.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="serverRole")
    def server_role(self) -> pulumi.Input['ReplicationRole']:
        """
        Role of the linked server.
        """
        return pulumi.get(self, "server_role")

    @server_role.setter
    def server_role(self, value: pulumi.Input['ReplicationRole']):
        pulumi.set(self, "server_role", value)

    @property
    @pulumi.getter(name="linkedServerName")
    def linked_server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the linked server that is being added to the Redis cache.
        """
        return pulumi.get(self, "linked_server_name")

    @linked_server_name.setter
    def linked_server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_server_name", value)


warnings.warn("""Version v20190701 will be removed in the next major version of the provider. Upgrade to version v20200601 or later.""", DeprecationWarning)


class LinkedServer(pulumi.CustomResource):
    warnings.warn("""Version v20190701 will be removed in the next major version of the provider. Upgrade to version v20200601 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_redis_cache_id: Optional[pulumi.Input[str]] = None,
                 linked_redis_cache_location: Optional[pulumi.Input[str]] = None,
                 linked_server_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_role: Optional[pulumi.Input['ReplicationRole']] = None,
                 __props__=None):
        """
        Response to put/get linked server (with properties) for Redis cache.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] linked_redis_cache_id: Fully qualified resourceId of the linked redis cache.
        :param pulumi.Input[str] linked_redis_cache_location: Location of the linked redis cache.
        :param pulumi.Input[str] linked_server_name: The name of the linked server that is being added to the Redis cache.
        :param pulumi.Input[str] name: The name of the Redis cache.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['ReplicationRole'] server_role: Role of the linked server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkedServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response to put/get linked server (with properties) for Redis cache.

        :param str resource_name: The name of the resource.
        :param LinkedServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkedServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_redis_cache_id: Optional[pulumi.Input[str]] = None,
                 linked_redis_cache_location: Optional[pulumi.Input[str]] = None,
                 linked_server_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_role: Optional[pulumi.Input['ReplicationRole']] = None,
                 __props__=None):
        pulumi.log.warn("""LinkedServer is deprecated: Version v20190701 will be removed in the next major version of the provider. Upgrade to version v20200601 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkedServerArgs.__new__(LinkedServerArgs)

            if linked_redis_cache_id is None and not opts.urn:
                raise TypeError("Missing required property 'linked_redis_cache_id'")
            __props__.__dict__["linked_redis_cache_id"] = linked_redis_cache_id
            if linked_redis_cache_location is None and not opts.urn:
                raise TypeError("Missing required property 'linked_redis_cache_location'")
            __props__.__dict__["linked_redis_cache_location"] = linked_redis_cache_location
            __props__.__dict__["linked_server_name"] = linked_server_name
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_role is None and not opts.urn:
                raise TypeError("Missing required property 'server_role'")
            __props__.__dict__["server_role"] = server_role
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cache:LinkedServer"), pulumi.Alias(type_="azure-native:cache/v20170201:LinkedServer"), pulumi.Alias(type_="azure-native:cache/v20171001:LinkedServer"), pulumi.Alias(type_="azure-native:cache/v20180301:LinkedServer"), pulumi.Alias(type_="azure-native:cache/v20200601:LinkedServer"), pulumi.Alias(type_="azure-native:cache/v20201201:LinkedServer"), pulumi.Alias(type_="azure-native:cache/v20210601:LinkedServer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LinkedServer, __self__).__init__(
            'azure-native:cache/v20190701:LinkedServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LinkedServer':
        """
        Get an existing LinkedServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LinkedServerArgs.__new__(LinkedServerArgs)

        __props__.__dict__["linked_redis_cache_id"] = None
        __props__.__dict__["linked_redis_cache_location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["server_role"] = None
        __props__.__dict__["type"] = None
        return LinkedServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="linkedRedisCacheId")
    def linked_redis_cache_id(self) -> pulumi.Output[str]:
        """
        Fully qualified resourceId of the linked redis cache.
        """
        return pulumi.get(self, "linked_redis_cache_id")

    @property
    @pulumi.getter(name="linkedRedisCacheLocation")
    def linked_redis_cache_location(self) -> pulumi.Output[str]:
        """
        Location of the linked redis cache.
        """
        return pulumi.get(self, "linked_redis_cache_location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Terminal state of the link between primary and secondary redis cache.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverRole")
    def server_role(self) -> pulumi.Output[str]:
        """
        Role of the linked server.
        """
        return pulumi.get(self, "server_role")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

