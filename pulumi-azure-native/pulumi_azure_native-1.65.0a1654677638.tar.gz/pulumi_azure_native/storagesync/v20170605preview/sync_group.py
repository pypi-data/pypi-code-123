# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['SyncGroupArgs', 'SyncGroup']

@pulumi.input_type
class SyncGroupArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 storage_sync_service_name: pulumi.Input[str],
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 unique_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SyncGroup resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] storage_sync_service_name: Name of Storage Sync Service resource.
        :param pulumi.Input[str] sync_group_name: Name of Sync Group resource.
        :param pulumi.Input[str] unique_id: Unique Id
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_sync_service_name", storage_sync_service_name)
        if sync_group_name is not None:
            pulumi.set(__self__, "sync_group_name", sync_group_name)
        if unique_id is not None:
            pulumi.set(__self__, "unique_id", unique_id)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageSyncServiceName")
    def storage_sync_service_name(self) -> pulumi.Input[str]:
        """
        Name of Storage Sync Service resource.
        """
        return pulumi.get(self, "storage_sync_service_name")

    @storage_sync_service_name.setter
    def storage_sync_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_sync_service_name", value)

    @property
    @pulumi.getter(name="syncGroupName")
    def sync_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Sync Group resource.
        """
        return pulumi.get(self, "sync_group_name")

    @sync_group_name.setter
    def sync_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_group_name", value)

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique Id
        """
        return pulumi.get(self, "unique_id")

    @unique_id.setter
    def unique_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unique_id", value)


warnings.warn("""Version v20170605preview will be removed in the next major version of the provider. Upgrade to version v20200301 or later.""", DeprecationWarning)


class SyncGroup(pulumi.CustomResource):
    warnings.warn("""Version v20170605preview will be removed in the next major version of the provider. Upgrade to version v20200301 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_sync_service_name: Optional[pulumi.Input[str]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 unique_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Sync Group object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] storage_sync_service_name: Name of Storage Sync Service resource.
        :param pulumi.Input[str] sync_group_name: Name of Sync Group resource.
        :param pulumi.Input[str] unique_id: Unique Id
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SyncGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Sync Group object.

        :param str resource_name: The name of the resource.
        :param SyncGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SyncGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_sync_service_name: Optional[pulumi.Input[str]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 unique_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SyncGroup is deprecated: Version v20170605preview will be removed in the next major version of the provider. Upgrade to version v20200301 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SyncGroupArgs.__new__(SyncGroupArgs)

            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_sync_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_sync_service_name'")
            __props__.__dict__["storage_sync_service_name"] = storage_sync_service_name
            __props__.__dict__["sync_group_name"] = sync_group_name
            __props__.__dict__["unique_id"] = unique_id
            __props__.__dict__["name"] = None
            __props__.__dict__["sync_group_status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storagesync:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20180402:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20180701:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20181001:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20190201:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20190301:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20190601:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20191001:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20200301:SyncGroup"), pulumi.Alias(type_="azure-native:storagesync/v20200901:SyncGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SyncGroup, __self__).__init__(
            'azure-native:storagesync/v20170605preview:SyncGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SyncGroup':
        """
        Get an existing SyncGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SyncGroupArgs.__new__(SyncGroupArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["sync_group_status"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unique_id"] = None
        return SyncGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="syncGroupStatus")
    def sync_group_status(self) -> pulumi.Output[str]:
        """
        Sync group status
        """
        return pulumi.get(self, "sync_group_status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[Optional[str]]:
        """
        Unique Id
        """
        return pulumi.get(self, "unique_id")

