# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetStackResult',
    'AwaitableGetStackResult',
    'get_stack',
    'get_stack_output',
]

@pulumi.output_type
class GetStackResult:
    def __init__(__self__, agent_version=None, attributes=None, chef_configuration=None, configuration_manager=None, custom_cookbooks_source=None, custom_json=None, default_availability_zone=None, default_instance_profile_arn=None, default_os=None, default_root_device_type=None, default_ssh_key_name=None, default_subnet_id=None, ecs_cluster_arn=None, elastic_ips=None, hostname_theme=None, id=None, name=None, rds_db_instances=None, tags=None, use_custom_cookbooks=None, use_opsworks_security_groups=None):
        if agent_version and not isinstance(agent_version, str):
            raise TypeError("Expected argument 'agent_version' to be a str")
        pulumi.set(__self__, "agent_version", agent_version)
        if attributes and not isinstance(attributes, dict):
            raise TypeError("Expected argument 'attributes' to be a dict")
        pulumi.set(__self__, "attributes", attributes)
        if chef_configuration and not isinstance(chef_configuration, dict):
            raise TypeError("Expected argument 'chef_configuration' to be a dict")
        pulumi.set(__self__, "chef_configuration", chef_configuration)
        if configuration_manager and not isinstance(configuration_manager, dict):
            raise TypeError("Expected argument 'configuration_manager' to be a dict")
        pulumi.set(__self__, "configuration_manager", configuration_manager)
        if custom_cookbooks_source and not isinstance(custom_cookbooks_source, dict):
            raise TypeError("Expected argument 'custom_cookbooks_source' to be a dict")
        pulumi.set(__self__, "custom_cookbooks_source", custom_cookbooks_source)
        if custom_json and not isinstance(custom_json, dict):
            raise TypeError("Expected argument 'custom_json' to be a dict")
        pulumi.set(__self__, "custom_json", custom_json)
        if default_availability_zone and not isinstance(default_availability_zone, str):
            raise TypeError("Expected argument 'default_availability_zone' to be a str")
        pulumi.set(__self__, "default_availability_zone", default_availability_zone)
        if default_instance_profile_arn and not isinstance(default_instance_profile_arn, str):
            raise TypeError("Expected argument 'default_instance_profile_arn' to be a str")
        pulumi.set(__self__, "default_instance_profile_arn", default_instance_profile_arn)
        if default_os and not isinstance(default_os, str):
            raise TypeError("Expected argument 'default_os' to be a str")
        pulumi.set(__self__, "default_os", default_os)
        if default_root_device_type and not isinstance(default_root_device_type, str):
            raise TypeError("Expected argument 'default_root_device_type' to be a str")
        pulumi.set(__self__, "default_root_device_type", default_root_device_type)
        if default_ssh_key_name and not isinstance(default_ssh_key_name, str):
            raise TypeError("Expected argument 'default_ssh_key_name' to be a str")
        pulumi.set(__self__, "default_ssh_key_name", default_ssh_key_name)
        if default_subnet_id and not isinstance(default_subnet_id, str):
            raise TypeError("Expected argument 'default_subnet_id' to be a str")
        pulumi.set(__self__, "default_subnet_id", default_subnet_id)
        if ecs_cluster_arn and not isinstance(ecs_cluster_arn, str):
            raise TypeError("Expected argument 'ecs_cluster_arn' to be a str")
        pulumi.set(__self__, "ecs_cluster_arn", ecs_cluster_arn)
        if elastic_ips and not isinstance(elastic_ips, list):
            raise TypeError("Expected argument 'elastic_ips' to be a list")
        pulumi.set(__self__, "elastic_ips", elastic_ips)
        if hostname_theme and not isinstance(hostname_theme, str):
            raise TypeError("Expected argument 'hostname_theme' to be a str")
        pulumi.set(__self__, "hostname_theme", hostname_theme)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rds_db_instances and not isinstance(rds_db_instances, list):
            raise TypeError("Expected argument 'rds_db_instances' to be a list")
        pulumi.set(__self__, "rds_db_instances", rds_db_instances)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if use_custom_cookbooks and not isinstance(use_custom_cookbooks, bool):
            raise TypeError("Expected argument 'use_custom_cookbooks' to be a bool")
        pulumi.set(__self__, "use_custom_cookbooks", use_custom_cookbooks)
        if use_opsworks_security_groups and not isinstance(use_opsworks_security_groups, bool):
            raise TypeError("Expected argument 'use_opsworks_security_groups' to be a bool")
        pulumi.set(__self__, "use_opsworks_security_groups", use_opsworks_security_groups)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[str]:
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="chefConfiguration")
    def chef_configuration(self) -> Optional['outputs.StackChefConfiguration']:
        return pulumi.get(self, "chef_configuration")

    @property
    @pulumi.getter(name="configurationManager")
    def configuration_manager(self) -> Optional['outputs.StackConfigurationManager']:
        return pulumi.get(self, "configuration_manager")

    @property
    @pulumi.getter(name="customCookbooksSource")
    def custom_cookbooks_source(self) -> Optional['outputs.StackSource']:
        return pulumi.get(self, "custom_cookbooks_source")

    @property
    @pulumi.getter(name="customJson")
    def custom_json(self) -> Optional[Any]:
        return pulumi.get(self, "custom_json")

    @property
    @pulumi.getter(name="defaultAvailabilityZone")
    def default_availability_zone(self) -> Optional[str]:
        return pulumi.get(self, "default_availability_zone")

    @property
    @pulumi.getter(name="defaultInstanceProfileArn")
    def default_instance_profile_arn(self) -> Optional[str]:
        return pulumi.get(self, "default_instance_profile_arn")

    @property
    @pulumi.getter(name="defaultOs")
    def default_os(self) -> Optional[str]:
        return pulumi.get(self, "default_os")

    @property
    @pulumi.getter(name="defaultRootDeviceType")
    def default_root_device_type(self) -> Optional[str]:
        return pulumi.get(self, "default_root_device_type")

    @property
    @pulumi.getter(name="defaultSshKeyName")
    def default_ssh_key_name(self) -> Optional[str]:
        return pulumi.get(self, "default_ssh_key_name")

    @property
    @pulumi.getter(name="defaultSubnetId")
    def default_subnet_id(self) -> Optional[str]:
        return pulumi.get(self, "default_subnet_id")

    @property
    @pulumi.getter(name="ecsClusterArn")
    def ecs_cluster_arn(self) -> Optional[str]:
        return pulumi.get(self, "ecs_cluster_arn")

    @property
    @pulumi.getter(name="elasticIps")
    def elastic_ips(self) -> Optional[Sequence['outputs.StackElasticIp']]:
        return pulumi.get(self, "elastic_ips")

    @property
    @pulumi.getter(name="hostnameTheme")
    def hostname_theme(self) -> Optional[str]:
        return pulumi.get(self, "hostname_theme")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rdsDbInstances")
    def rds_db_instances(self) -> Optional[Sequence['outputs.StackRdsDbInstance']]:
        return pulumi.get(self, "rds_db_instances")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.StackTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useCustomCookbooks")
    def use_custom_cookbooks(self) -> Optional[bool]:
        return pulumi.get(self, "use_custom_cookbooks")

    @property
    @pulumi.getter(name="useOpsworksSecurityGroups")
    def use_opsworks_security_groups(self) -> Optional[bool]:
        return pulumi.get(self, "use_opsworks_security_groups")


class AwaitableGetStackResult(GetStackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStackResult(
            agent_version=self.agent_version,
            attributes=self.attributes,
            chef_configuration=self.chef_configuration,
            configuration_manager=self.configuration_manager,
            custom_cookbooks_source=self.custom_cookbooks_source,
            custom_json=self.custom_json,
            default_availability_zone=self.default_availability_zone,
            default_instance_profile_arn=self.default_instance_profile_arn,
            default_os=self.default_os,
            default_root_device_type=self.default_root_device_type,
            default_ssh_key_name=self.default_ssh_key_name,
            default_subnet_id=self.default_subnet_id,
            ecs_cluster_arn=self.ecs_cluster_arn,
            elastic_ips=self.elastic_ips,
            hostname_theme=self.hostname_theme,
            id=self.id,
            name=self.name,
            rds_db_instances=self.rds_db_instances,
            tags=self.tags,
            use_custom_cookbooks=self.use_custom_cookbooks,
            use_opsworks_security_groups=self.use_opsworks_security_groups)


def get_stack(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStackResult:
    """
    Resource Type definition for AWS::OpsWorks::Stack
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:opsworks:getStack', __args__, opts=opts, typ=GetStackResult).value

    return AwaitableGetStackResult(
        agent_version=__ret__.agent_version,
        attributes=__ret__.attributes,
        chef_configuration=__ret__.chef_configuration,
        configuration_manager=__ret__.configuration_manager,
        custom_cookbooks_source=__ret__.custom_cookbooks_source,
        custom_json=__ret__.custom_json,
        default_availability_zone=__ret__.default_availability_zone,
        default_instance_profile_arn=__ret__.default_instance_profile_arn,
        default_os=__ret__.default_os,
        default_root_device_type=__ret__.default_root_device_type,
        default_ssh_key_name=__ret__.default_ssh_key_name,
        default_subnet_id=__ret__.default_subnet_id,
        ecs_cluster_arn=__ret__.ecs_cluster_arn,
        elastic_ips=__ret__.elastic_ips,
        hostname_theme=__ret__.hostname_theme,
        id=__ret__.id,
        name=__ret__.name,
        rds_db_instances=__ret__.rds_db_instances,
        tags=__ret__.tags,
        use_custom_cookbooks=__ret__.use_custom_cookbooks,
        use_opsworks_security_groups=__ret__.use_opsworks_security_groups)


@_utilities.lift_output_func(get_stack)
def get_stack_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStackResult]:
    """
    Resource Type definition for AWS::OpsWorks::Stack
    """
    ...
