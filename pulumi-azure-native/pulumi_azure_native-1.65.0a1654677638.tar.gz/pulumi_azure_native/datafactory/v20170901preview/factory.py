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

__all__ = ['FactoryArgs', 'Factory']

@pulumi.input_type
class FactoryArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 factory_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['FactoryIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vsts_configuration: Optional[pulumi.Input['FactoryVSTSConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Factory resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input['FactoryIdentityArgs'] identity: Managed service identity of the factory.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input['FactoryVSTSConfigurationArgs'] vsts_configuration: VSTS repo information of the factory.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if factory_name is not None:
            pulumi.set(__self__, "factory_name", factory_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vsts_configuration is not None:
            pulumi.set(__self__, "vsts_configuration", vsts_configuration)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> Optional[pulumi.Input[str]]:
        """
        The factory name.
        """
        return pulumi.get(self, "factory_name")

    @factory_name.setter
    def factory_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "factory_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['FactoryIdentityArgs']]:
        """
        Managed service identity of the factory.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['FactoryIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vstsConfiguration")
    def vsts_configuration(self) -> Optional[pulumi.Input['FactoryVSTSConfigurationArgs']]:
        """
        VSTS repo information of the factory.
        """
        return pulumi.get(self, "vsts_configuration")

    @vsts_configuration.setter
    def vsts_configuration(self, value: Optional[pulumi.Input['FactoryVSTSConfigurationArgs']]):
        pulumi.set(self, "vsts_configuration", value)


warnings.warn("""Version v20170901preview will be removed in the next major version of the provider. Upgrade to version v20180601 or later.""", DeprecationWarning)


class Factory(pulumi.CustomResource):
    warnings.warn("""Version v20170901preview will be removed in the next major version of the provider. Upgrade to version v20180601 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['FactoryIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vsts_configuration: Optional[pulumi.Input[pulumi.InputType['FactoryVSTSConfigurationArgs']]] = None,
                 __props__=None):
        """
        Factory resource type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[pulumi.InputType['FactoryIdentityArgs']] identity: Managed service identity of the factory.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[pulumi.InputType['FactoryVSTSConfigurationArgs']] vsts_configuration: VSTS repo information of the factory.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FactoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Factory resource type.

        :param str resource_name: The name of the resource.
        :param FactoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FactoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['FactoryIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vsts_configuration: Optional[pulumi.Input[pulumi.InputType['FactoryVSTSConfigurationArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Factory is deprecated: Version v20170901preview will be removed in the next major version of the provider. Upgrade to version v20180601 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FactoryArgs.__new__(FactoryArgs)

            __props__.__dict__["factory_name"] = factory_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vsts_configuration"] = vsts_configuration
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datafactory:Factory"), pulumi.Alias(type_="azure-native:datafactory/v20180601:Factory")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Factory, __self__).__init__(
            'azure-native:datafactory/v20170901preview:Factory',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Factory':
        """
        Get an existing Factory resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FactoryArgs.__new__(FactoryArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        __props__.__dict__["vsts_configuration"] = None
        return Factory(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time the factory was created in ISO8601 format.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.FactoryIdentityResponse']]:
        """
        Managed service identity of the factory.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Factory provisioning state, example Succeeded.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of the factory.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="vstsConfiguration")
    def vsts_configuration(self) -> pulumi.Output[Optional['outputs.FactoryVSTSConfigurationResponse']]:
        """
        VSTS repo information of the factory.
        """
        return pulumi.get(self, "vsts_configuration")

