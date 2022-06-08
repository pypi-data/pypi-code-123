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

__all__ = ['SqlPoolsV3Args', 'SqlPoolsV3']

@pulumi.input_type
class SqlPoolsV3Args:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 auto_pause_timer: Optional[pulumi.Input[int]] = None,
                 auto_resume: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_service_objective_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuV3Args']] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SqlPoolsV3 resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[int] auto_pause_timer: The period of inactivity in minutes before automatically pausing the sql pool.
        :param pulumi.Input[bool] auto_resume: Indicates whether the sql pool can automatically resume when connection attempts are made.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] max_service_objective_name: The max service level objective name of the sql pool.
        :param pulumi.Input['SkuV3Args'] sku: The sql pool SKU. The list of SKUs may vary by region and support offer.
        :param pulumi.Input[str] sql_pool_name: The name of the sql pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if auto_pause_timer is not None:
            pulumi.set(__self__, "auto_pause_timer", auto_pause_timer)
        if auto_resume is not None:
            pulumi.set(__self__, "auto_resume", auto_resume)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if max_service_objective_name is not None:
            pulumi.set(__self__, "max_service_objective_name", max_service_objective_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if sql_pool_name is not None:
            pulumi.set(__self__, "sql_pool_name", sql_pool_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="autoPauseTimer")
    def auto_pause_timer(self) -> Optional[pulumi.Input[int]]:
        """
        The period of inactivity in minutes before automatically pausing the sql pool.
        """
        return pulumi.get(self, "auto_pause_timer")

    @auto_pause_timer.setter
    def auto_pause_timer(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "auto_pause_timer", value)

    @property
    @pulumi.getter(name="autoResume")
    def auto_resume(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the sql pool can automatically resume when connection attempts are made.
        """
        return pulumi.get(self, "auto_resume")

    @auto_resume.setter
    def auto_resume(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_resume", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maxServiceObjectiveName")
    def max_service_objective_name(self) -> Optional[pulumi.Input[str]]:
        """
        The max service level objective name of the sql pool.
        """
        return pulumi.get(self, "max_service_objective_name")

    @max_service_objective_name.setter
    def max_service_objective_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "max_service_objective_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuV3Args']]:
        """
        The sql pool SKU. The list of SKUs may vary by region and support offer.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuV3Args']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="sqlPoolName")
    def sql_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the sql pool.
        """
        return pulumi.get(self, "sql_pool_name")

    @sql_pool_name.setter
    def sql_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_pool_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version v20200401preview will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""", DeprecationWarning)


class SqlPoolsV3(pulumi.CustomResource):
    warnings.warn("""Version v20200401preview will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_pause_timer: Optional[pulumi.Input[int]] = None,
                 auto_resume: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_service_objective_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuV3Args']]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A sql pool resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] auto_pause_timer: The period of inactivity in minutes before automatically pausing the sql pool.
        :param pulumi.Input[bool] auto_resume: Indicates whether the sql pool can automatically resume when connection attempts are made.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] max_service_objective_name: The max service level objective name of the sql pool.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuV3Args']] sku: The sql pool SKU. The list of SKUs may vary by region and support offer.
        :param pulumi.Input[str] sql_pool_name: The name of the sql pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlPoolsV3Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A sql pool resource.

        :param str resource_name: The name of the resource.
        :param SqlPoolsV3Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlPoolsV3Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_pause_timer: Optional[pulumi.Input[int]] = None,
                 auto_resume: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_service_objective_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuV3Args']]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SqlPoolsV3 is deprecated: Version v20200401preview will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlPoolsV3Args.__new__(SqlPoolsV3Args)

            __props__.__dict__["auto_pause_timer"] = auto_pause_timer
            __props__.__dict__["auto_resume"] = auto_resume
            __props__.__dict__["location"] = location
            __props__.__dict__["max_service_objective_name"] = max_service_objective_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["sql_pool_name"] = sql_pool_name
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["current_service_objective_name"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["requested_service_objective_name"] = None
            __props__.__dict__["sql_pool_guid"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse:SqlPoolsV3"), pulumi.Alias(type_="azure-native:synapse/v20190601preview:SqlPoolsV3"), pulumi.Alias(type_="azure-native:synapse/v20201201:SqlPoolsV3"), pulumi.Alias(type_="azure-native:synapse/v20210301:SqlPoolsV3"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:SqlPoolsV3"), pulumi.Alias(type_="azure-native:synapse/v20210501:SqlPoolsV3"), pulumi.Alias(type_="azure-native:synapse/v20210601:SqlPoolsV3"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:SqlPoolsV3")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlPoolsV3, __self__).__init__(
            'azure-native:synapse/v20200401preview:SqlPoolsV3',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlPoolsV3':
        """
        Get an existing SqlPoolsV3 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlPoolsV3Args.__new__(SqlPoolsV3Args)

        __props__.__dict__["auto_pause_timer"] = None
        __props__.__dict__["auto_resume"] = None
        __props__.__dict__["current_service_objective_name"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_service_objective_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["requested_service_objective_name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["sql_pool_guid"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SqlPoolsV3(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoPauseTimer")
    def auto_pause_timer(self) -> pulumi.Output[Optional[int]]:
        """
        The period of inactivity in minutes before automatically pausing the sql pool.
        """
        return pulumi.get(self, "auto_pause_timer")

    @property
    @pulumi.getter(name="autoResume")
    def auto_resume(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the sql pool can automatically resume when connection attempts are made.
        """
        return pulumi.get(self, "auto_resume")

    @property
    @pulumi.getter(name="currentServiceObjectiveName")
    def current_service_objective_name(self) -> pulumi.Output[str]:
        """
        The current service level objective name of the sql pool.
        """
        return pulumi.get(self, "current_service_objective_name")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of SqlPool.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxServiceObjectiveName")
    def max_service_objective_name(self) -> pulumi.Output[Optional[str]]:
        """
        The max service level objective name of the sql pool.
        """
        return pulumi.get(self, "max_service_objective_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requestedServiceObjectiveName")
    def requested_service_objective_name(self) -> pulumi.Output[str]:
        """
        The requested service level objective name of the sql pool.
        """
        return pulumi.get(self, "requested_service_objective_name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuV3Response']]:
        """
        The sql pool SKU. The list of SKUs may vary by region and support offer.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sqlPoolGuid")
    def sql_pool_guid(self) -> pulumi.Output[str]:
        """
        The Guid of the sql pool.
        """
        return pulumi.get(self, "sql_pool_guid")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the sql pool.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        SystemData of SqlPool.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

