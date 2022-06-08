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

__all__ = ['BigDataPoolArgs', 'BigDataPool']

@pulumi.input_type
class BigDataPoolArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 auto_pause: Optional[pulumi.Input['AutoPausePropertiesArgs']] = None,
                 auto_scale: Optional[pulumi.Input['AutoScalePropertiesArgs']] = None,
                 big_data_pool_name: Optional[pulumi.Input[str]] = None,
                 cache_size: Optional[pulumi.Input[int]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 custom_libraries: Optional[pulumi.Input[Sequence[pulumi.Input['LibraryInfoArgs']]]] = None,
                 default_spark_log_folder: Optional[pulumi.Input[str]] = None,
                 dynamic_executor_allocation: Optional[pulumi.Input['DynamicExecutorAllocationArgs']] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 is_compute_isolation_enabled: Optional[pulumi.Input[bool]] = None,
                 library_requirements: Optional[pulumi.Input['LibraryRequirementsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 node_size: Optional[pulumi.Input[Union[str, 'NodeSize']]] = None,
                 node_size_family: Optional[pulumi.Input[Union[str, 'NodeSizeFamily']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 session_level_packages_enabled: Optional[pulumi.Input[bool]] = None,
                 spark_config_properties: Optional[pulumi.Input['LibraryRequirementsArgs']] = None,
                 spark_events_folder: Optional[pulumi.Input[str]] = None,
                 spark_version: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a BigDataPool resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        :param pulumi.Input['AutoPausePropertiesArgs'] auto_pause: Auto-pausing properties
        :param pulumi.Input['AutoScalePropertiesArgs'] auto_scale: Auto-scaling properties
        :param pulumi.Input[str] big_data_pool_name: Big Data pool name
        :param pulumi.Input[int] cache_size: The cache size
        :param pulumi.Input[str] creation_date: The time when the Big Data pool was created.
        :param pulumi.Input[Sequence[pulumi.Input['LibraryInfoArgs']]] custom_libraries: List of custom libraries/packages associated with the spark pool.
        :param pulumi.Input[str] default_spark_log_folder: The default folder where Spark logs will be written.
        :param pulumi.Input['DynamicExecutorAllocationArgs'] dynamic_executor_allocation: Dynamic Executor Allocation
        :param pulumi.Input[bool] force: Whether to stop any running jobs in the Big Data pool
        :param pulumi.Input[bool] is_compute_isolation_enabled: Whether compute isolation is required or not.
        :param pulumi.Input['LibraryRequirementsArgs'] library_requirements: Library version requirements
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[int] node_count: The number of nodes in the Big Data pool.
        :param pulumi.Input[Union[str, 'NodeSize']] node_size: The level of compute power that each node in the Big Data pool has.
        :param pulumi.Input[Union[str, 'NodeSizeFamily']] node_size_family: The kind of nodes that the Big Data pool provides.
        :param pulumi.Input[str] provisioning_state: The state of the Big Data pool.
        :param pulumi.Input[bool] session_level_packages_enabled: Whether session level packages enabled.
        :param pulumi.Input['LibraryRequirementsArgs'] spark_config_properties: Spark configuration file to specify additional properties
        :param pulumi.Input[str] spark_events_folder: The Spark events folder
        :param pulumi.Input[str] spark_version: The Apache Spark version.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if auto_pause is not None:
            pulumi.set(__self__, "auto_pause", auto_pause)
        if auto_scale is not None:
            pulumi.set(__self__, "auto_scale", auto_scale)
        if big_data_pool_name is not None:
            pulumi.set(__self__, "big_data_pool_name", big_data_pool_name)
        if cache_size is not None:
            pulumi.set(__self__, "cache_size", cache_size)
        if creation_date is not None:
            pulumi.set(__self__, "creation_date", creation_date)
        if custom_libraries is not None:
            pulumi.set(__self__, "custom_libraries", custom_libraries)
        if default_spark_log_folder is not None:
            pulumi.set(__self__, "default_spark_log_folder", default_spark_log_folder)
        if dynamic_executor_allocation is not None:
            pulumi.set(__self__, "dynamic_executor_allocation", dynamic_executor_allocation)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if is_compute_isolation_enabled is not None:
            pulumi.set(__self__, "is_compute_isolation_enabled", is_compute_isolation_enabled)
        if library_requirements is not None:
            pulumi.set(__self__, "library_requirements", library_requirements)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)
        if node_size is not None:
            pulumi.set(__self__, "node_size", node_size)
        if node_size_family is not None:
            pulumi.set(__self__, "node_size_family", node_size_family)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if session_level_packages_enabled is not None:
            pulumi.set(__self__, "session_level_packages_enabled", session_level_packages_enabled)
        if spark_config_properties is not None:
            pulumi.set(__self__, "spark_config_properties", spark_config_properties)
        if spark_events_folder is not None:
            pulumi.set(__self__, "spark_events_folder", spark_events_folder)
        if spark_version is not None:
            pulumi.set(__self__, "spark_version", spark_version)
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
        The name of the workspace
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> Optional[pulumi.Input['AutoPausePropertiesArgs']]:
        """
        Auto-pausing properties
        """
        return pulumi.get(self, "auto_pause")

    @auto_pause.setter
    def auto_pause(self, value: Optional[pulumi.Input['AutoPausePropertiesArgs']]):
        pulumi.set(self, "auto_pause", value)

    @property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> Optional[pulumi.Input['AutoScalePropertiesArgs']]:
        """
        Auto-scaling properties
        """
        return pulumi.get(self, "auto_scale")

    @auto_scale.setter
    def auto_scale(self, value: Optional[pulumi.Input['AutoScalePropertiesArgs']]):
        pulumi.set(self, "auto_scale", value)

    @property
    @pulumi.getter(name="bigDataPoolName")
    def big_data_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        Big Data pool name
        """
        return pulumi.get(self, "big_data_pool_name")

    @big_data_pool_name.setter
    def big_data_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "big_data_pool_name", value)

    @property
    @pulumi.getter(name="cacheSize")
    def cache_size(self) -> Optional[pulumi.Input[int]]:
        """
        The cache size
        """
        return pulumi.get(self, "cache_size")

    @cache_size.setter
    def cache_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cache_size", value)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the Big Data pool was created.
        """
        return pulumi.get(self, "creation_date")

    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_date", value)

    @property
    @pulumi.getter(name="customLibraries")
    def custom_libraries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LibraryInfoArgs']]]]:
        """
        List of custom libraries/packages associated with the spark pool.
        """
        return pulumi.get(self, "custom_libraries")

    @custom_libraries.setter
    def custom_libraries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LibraryInfoArgs']]]]):
        pulumi.set(self, "custom_libraries", value)

    @property
    @pulumi.getter(name="defaultSparkLogFolder")
    def default_spark_log_folder(self) -> Optional[pulumi.Input[str]]:
        """
        The default folder where Spark logs will be written.
        """
        return pulumi.get(self, "default_spark_log_folder")

    @default_spark_log_folder.setter
    def default_spark_log_folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_spark_log_folder", value)

    @property
    @pulumi.getter(name="dynamicExecutorAllocation")
    def dynamic_executor_allocation(self) -> Optional[pulumi.Input['DynamicExecutorAllocationArgs']]:
        """
        Dynamic Executor Allocation
        """
        return pulumi.get(self, "dynamic_executor_allocation")

    @dynamic_executor_allocation.setter
    def dynamic_executor_allocation(self, value: Optional[pulumi.Input['DynamicExecutorAllocationArgs']]):
        pulumi.set(self, "dynamic_executor_allocation", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to stop any running jobs in the Big Data pool
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="isComputeIsolationEnabled")
    def is_compute_isolation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether compute isolation is required or not.
        """
        return pulumi.get(self, "is_compute_isolation_enabled")

    @is_compute_isolation_enabled.setter
    def is_compute_isolation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_compute_isolation_enabled", value)

    @property
    @pulumi.getter(name="libraryRequirements")
    def library_requirements(self) -> Optional[pulumi.Input['LibraryRequirementsArgs']]:
        """
        Library version requirements
        """
        return pulumi.get(self, "library_requirements")

    @library_requirements.setter
    def library_requirements(self, value: Optional[pulumi.Input['LibraryRequirementsArgs']]):
        pulumi.set(self, "library_requirements", value)

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
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes in the Big Data pool.
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> Optional[pulumi.Input[Union[str, 'NodeSize']]]:
        """
        The level of compute power that each node in the Big Data pool has.
        """
        return pulumi.get(self, "node_size")

    @node_size.setter
    def node_size(self, value: Optional[pulumi.Input[Union[str, 'NodeSize']]]):
        pulumi.set(self, "node_size", value)

    @property
    @pulumi.getter(name="nodeSizeFamily")
    def node_size_family(self) -> Optional[pulumi.Input[Union[str, 'NodeSizeFamily']]]:
        """
        The kind of nodes that the Big Data pool provides.
        """
        return pulumi.get(self, "node_size_family")

    @node_size_family.setter
    def node_size_family(self, value: Optional[pulumi.Input[Union[str, 'NodeSizeFamily']]]):
        pulumi.set(self, "node_size_family", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the Big Data pool.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="sessionLevelPackagesEnabled")
    def session_level_packages_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether session level packages enabled.
        """
        return pulumi.get(self, "session_level_packages_enabled")

    @session_level_packages_enabled.setter
    def session_level_packages_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "session_level_packages_enabled", value)

    @property
    @pulumi.getter(name="sparkConfigProperties")
    def spark_config_properties(self) -> Optional[pulumi.Input['LibraryRequirementsArgs']]:
        """
        Spark configuration file to specify additional properties
        """
        return pulumi.get(self, "spark_config_properties")

    @spark_config_properties.setter
    def spark_config_properties(self, value: Optional[pulumi.Input['LibraryRequirementsArgs']]):
        pulumi.set(self, "spark_config_properties", value)

    @property
    @pulumi.getter(name="sparkEventsFolder")
    def spark_events_folder(self) -> Optional[pulumi.Input[str]]:
        """
        The Spark events folder
        """
        return pulumi.get(self, "spark_events_folder")

    @spark_events_folder.setter
    def spark_events_folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spark_events_folder", value)

    @property
    @pulumi.getter(name="sparkVersion")
    def spark_version(self) -> Optional[pulumi.Input[str]]:
        """
        The Apache Spark version.
        """
        return pulumi.get(self, "spark_version")

    @spark_version.setter
    def spark_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spark_version", value)

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


warnings.warn("""Version v20201201 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""", DeprecationWarning)


class BigDataPool(pulumi.CustomResource):
    warnings.warn("""Version v20201201 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_pause: Optional[pulumi.Input[pulumi.InputType['AutoPausePropertiesArgs']]] = None,
                 auto_scale: Optional[pulumi.Input[pulumi.InputType['AutoScalePropertiesArgs']]] = None,
                 big_data_pool_name: Optional[pulumi.Input[str]] = None,
                 cache_size: Optional[pulumi.Input[int]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 custom_libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LibraryInfoArgs']]]]] = None,
                 default_spark_log_folder: Optional[pulumi.Input[str]] = None,
                 dynamic_executor_allocation: Optional[pulumi.Input[pulumi.InputType['DynamicExecutorAllocationArgs']]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 is_compute_isolation_enabled: Optional[pulumi.Input[bool]] = None,
                 library_requirements: Optional[pulumi.Input[pulumi.InputType['LibraryRequirementsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 node_size: Optional[pulumi.Input[Union[str, 'NodeSize']]] = None,
                 node_size_family: Optional[pulumi.Input[Union[str, 'NodeSizeFamily']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 session_level_packages_enabled: Optional[pulumi.Input[bool]] = None,
                 spark_config_properties: Optional[pulumi.Input[pulumi.InputType['LibraryRequirementsArgs']]] = None,
                 spark_events_folder: Optional[pulumi.Input[str]] = None,
                 spark_version: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Big Data pool

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AutoPausePropertiesArgs']] auto_pause: Auto-pausing properties
        :param pulumi.Input[pulumi.InputType['AutoScalePropertiesArgs']] auto_scale: Auto-scaling properties
        :param pulumi.Input[str] big_data_pool_name: Big Data pool name
        :param pulumi.Input[int] cache_size: The cache size
        :param pulumi.Input[str] creation_date: The time when the Big Data pool was created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LibraryInfoArgs']]]] custom_libraries: List of custom libraries/packages associated with the spark pool.
        :param pulumi.Input[str] default_spark_log_folder: The default folder where Spark logs will be written.
        :param pulumi.Input[pulumi.InputType['DynamicExecutorAllocationArgs']] dynamic_executor_allocation: Dynamic Executor Allocation
        :param pulumi.Input[bool] force: Whether to stop any running jobs in the Big Data pool
        :param pulumi.Input[bool] is_compute_isolation_enabled: Whether compute isolation is required or not.
        :param pulumi.Input[pulumi.InputType['LibraryRequirementsArgs']] library_requirements: Library version requirements
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[int] node_count: The number of nodes in the Big Data pool.
        :param pulumi.Input[Union[str, 'NodeSize']] node_size: The level of compute power that each node in the Big Data pool has.
        :param pulumi.Input[Union[str, 'NodeSizeFamily']] node_size_family: The kind of nodes that the Big Data pool provides.
        :param pulumi.Input[str] provisioning_state: The state of the Big Data pool.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[bool] session_level_packages_enabled: Whether session level packages enabled.
        :param pulumi.Input[pulumi.InputType['LibraryRequirementsArgs']] spark_config_properties: Spark configuration file to specify additional properties
        :param pulumi.Input[str] spark_events_folder: The Spark events folder
        :param pulumi.Input[str] spark_version: The Apache Spark version.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BigDataPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Big Data pool

        :param str resource_name: The name of the resource.
        :param BigDataPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BigDataPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_pause: Optional[pulumi.Input[pulumi.InputType['AutoPausePropertiesArgs']]] = None,
                 auto_scale: Optional[pulumi.Input[pulumi.InputType['AutoScalePropertiesArgs']]] = None,
                 big_data_pool_name: Optional[pulumi.Input[str]] = None,
                 cache_size: Optional[pulumi.Input[int]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 custom_libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LibraryInfoArgs']]]]] = None,
                 default_spark_log_folder: Optional[pulumi.Input[str]] = None,
                 dynamic_executor_allocation: Optional[pulumi.Input[pulumi.InputType['DynamicExecutorAllocationArgs']]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 is_compute_isolation_enabled: Optional[pulumi.Input[bool]] = None,
                 library_requirements: Optional[pulumi.Input[pulumi.InputType['LibraryRequirementsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 node_size: Optional[pulumi.Input[Union[str, 'NodeSize']]] = None,
                 node_size_family: Optional[pulumi.Input[Union[str, 'NodeSizeFamily']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 session_level_packages_enabled: Optional[pulumi.Input[bool]] = None,
                 spark_config_properties: Optional[pulumi.Input[pulumi.InputType['LibraryRequirementsArgs']]] = None,
                 spark_events_folder: Optional[pulumi.Input[str]] = None,
                 spark_version: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""BigDataPool is deprecated: Version v20201201 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BigDataPoolArgs.__new__(BigDataPoolArgs)

            __props__.__dict__["auto_pause"] = auto_pause
            __props__.__dict__["auto_scale"] = auto_scale
            __props__.__dict__["big_data_pool_name"] = big_data_pool_name
            __props__.__dict__["cache_size"] = cache_size
            __props__.__dict__["creation_date"] = creation_date
            __props__.__dict__["custom_libraries"] = custom_libraries
            __props__.__dict__["default_spark_log_folder"] = default_spark_log_folder
            __props__.__dict__["dynamic_executor_allocation"] = dynamic_executor_allocation
            __props__.__dict__["force"] = force
            __props__.__dict__["is_compute_isolation_enabled"] = is_compute_isolation_enabled
            __props__.__dict__["library_requirements"] = library_requirements
            __props__.__dict__["location"] = location
            __props__.__dict__["node_count"] = node_count
            __props__.__dict__["node_size"] = node_size
            __props__.__dict__["node_size_family"] = node_size_family
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["session_level_packages_enabled"] = session_level_packages_enabled
            __props__.__dict__["spark_config_properties"] = spark_config_properties
            __props__.__dict__["spark_events_folder"] = spark_events_folder
            __props__.__dict__["spark_version"] = spark_version
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["last_succeeded_timestamp"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse:BigDataPool"), pulumi.Alias(type_="azure-native:synapse/v20190601preview:BigDataPool"), pulumi.Alias(type_="azure-native:synapse/v20210301:BigDataPool"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:BigDataPool"), pulumi.Alias(type_="azure-native:synapse/v20210501:BigDataPool"), pulumi.Alias(type_="azure-native:synapse/v20210601:BigDataPool"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:BigDataPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BigDataPool, __self__).__init__(
            'azure-native:synapse/v20201201:BigDataPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BigDataPool':
        """
        Get an existing BigDataPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BigDataPoolArgs.__new__(BigDataPoolArgs)

        __props__.__dict__["auto_pause"] = None
        __props__.__dict__["auto_scale"] = None
        __props__.__dict__["cache_size"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["custom_libraries"] = None
        __props__.__dict__["default_spark_log_folder"] = None
        __props__.__dict__["dynamic_executor_allocation"] = None
        __props__.__dict__["is_compute_isolation_enabled"] = None
        __props__.__dict__["last_succeeded_timestamp"] = None
        __props__.__dict__["library_requirements"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_count"] = None
        __props__.__dict__["node_size"] = None
        __props__.__dict__["node_size_family"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["session_level_packages_enabled"] = None
        __props__.__dict__["spark_config_properties"] = None
        __props__.__dict__["spark_events_folder"] = None
        __props__.__dict__["spark_version"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return BigDataPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> pulumi.Output[Optional['outputs.AutoPausePropertiesResponse']]:
        """
        Auto-pausing properties
        """
        return pulumi.get(self, "auto_pause")

    @property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> pulumi.Output[Optional['outputs.AutoScalePropertiesResponse']]:
        """
        Auto-scaling properties
        """
        return pulumi.get(self, "auto_scale")

    @property
    @pulumi.getter(name="cacheSize")
    def cache_size(self) -> pulumi.Output[Optional[int]]:
        """
        The cache size
        """
        return pulumi.get(self, "cache_size")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[Optional[str]]:
        """
        The time when the Big Data pool was created.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="customLibraries")
    def custom_libraries(self) -> pulumi.Output[Optional[Sequence['outputs.LibraryInfoResponse']]]:
        """
        List of custom libraries/packages associated with the spark pool.
        """
        return pulumi.get(self, "custom_libraries")

    @property
    @pulumi.getter(name="defaultSparkLogFolder")
    def default_spark_log_folder(self) -> pulumi.Output[Optional[str]]:
        """
        The default folder where Spark logs will be written.
        """
        return pulumi.get(self, "default_spark_log_folder")

    @property
    @pulumi.getter(name="dynamicExecutorAllocation")
    def dynamic_executor_allocation(self) -> pulumi.Output[Optional['outputs.DynamicExecutorAllocationResponse']]:
        """
        Dynamic Executor Allocation
        """
        return pulumi.get(self, "dynamic_executor_allocation")

    @property
    @pulumi.getter(name="isComputeIsolationEnabled")
    def is_compute_isolation_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether compute isolation is required or not.
        """
        return pulumi.get(self, "is_compute_isolation_enabled")

    @property
    @pulumi.getter(name="lastSucceededTimestamp")
    def last_succeeded_timestamp(self) -> pulumi.Output[str]:
        """
        The time when the Big Data pool was updated successfully.
        """
        return pulumi.get(self, "last_succeeded_timestamp")

    @property
    @pulumi.getter(name="libraryRequirements")
    def library_requirements(self) -> pulumi.Output[Optional['outputs.LibraryRequirementsResponse']]:
        """
        Library version requirements
        """
        return pulumi.get(self, "library_requirements")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[Optional[int]]:
        """
        The number of nodes in the Big Data pool.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> pulumi.Output[Optional[str]]:
        """
        The level of compute power that each node in the Big Data pool has.
        """
        return pulumi.get(self, "node_size")

    @property
    @pulumi.getter(name="nodeSizeFamily")
    def node_size_family(self) -> pulumi.Output[Optional[str]]:
        """
        The kind of nodes that the Big Data pool provides.
        """
        return pulumi.get(self, "node_size_family")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The state of the Big Data pool.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sessionLevelPackagesEnabled")
    def session_level_packages_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether session level packages enabled.
        """
        return pulumi.get(self, "session_level_packages_enabled")

    @property
    @pulumi.getter(name="sparkConfigProperties")
    def spark_config_properties(self) -> pulumi.Output[Optional['outputs.LibraryRequirementsResponse']]:
        """
        Spark configuration file to specify additional properties
        """
        return pulumi.get(self, "spark_config_properties")

    @property
    @pulumi.getter(name="sparkEventsFolder")
    def spark_events_folder(self) -> pulumi.Output[Optional[str]]:
        """
        The Spark events folder
        """
        return pulumi.get(self, "spark_events_folder")

    @property
    @pulumi.getter(name="sparkVersion")
    def spark_version(self) -> pulumi.Output[Optional[str]]:
        """
        The Apache Spark version.
        """
        return pulumi.get(self, "spark_version")

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

