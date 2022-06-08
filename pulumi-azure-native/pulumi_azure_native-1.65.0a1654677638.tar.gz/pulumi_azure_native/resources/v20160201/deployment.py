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

__all__ = ['DeploymentArgs', 'Deployment']

@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['DeploymentPropertiesArgs']] = None):
        """
        The set of arguments for constructing a Deployment resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] deployment_name: The name of the deployment.
        :param pulumi.Input['DeploymentPropertiesArgs'] properties: The deployment properties.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if deployment_name is not None:
            pulumi.set(__self__, "deployment_name", deployment_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

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
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the deployment.
        """
        return pulumi.get(self, "deployment_name")

    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['DeploymentPropertiesArgs']]:
        """
        The deployment properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['DeploymentPropertiesArgs']]):
        pulumi.set(self, "properties", value)


warnings.warn("""Version v20160201 will be removed in the next major version of the provider. Upgrade to version v20190501 or later.""", DeprecationWarning)


class Deployment(pulumi.CustomResource):
    warnings.warn("""Version v20160201 will be removed in the next major version of the provider. Upgrade to version v20190501 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['DeploymentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Deployment information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_name: The name of the deployment.
        :param pulumi.Input[pulumi.InputType['DeploymentPropertiesArgs']] properties: The deployment properties.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Deployment information.

        :param str resource_name: The name of the resource.
        :param DeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['DeploymentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Deployment is deprecated: Version v20160201 will be removed in the next major version of the provider. Upgrade to version v20190501 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentArgs.__new__(DeploymentArgs)

            __props__.__dict__["deployment_name"] = deployment_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:resources:Deployment"), pulumi.Alias(type_="azure-native:resources/v20151101:Deployment"), pulumi.Alias(type_="azure-native:resources/v20160701:Deployment"), pulumi.Alias(type_="azure-native:resources/v20160901:Deployment"), pulumi.Alias(type_="azure-native:resources/v20170510:Deployment"), pulumi.Alias(type_="azure-native:resources/v20180201:Deployment"), pulumi.Alias(type_="azure-native:resources/v20180501:Deployment"), pulumi.Alias(type_="azure-native:resources/v20190301:Deployment"), pulumi.Alias(type_="azure-native:resources/v20190501:Deployment"), pulumi.Alias(type_="azure-native:resources/v20190510:Deployment"), pulumi.Alias(type_="azure-native:resources/v20190701:Deployment"), pulumi.Alias(type_="azure-native:resources/v20190801:Deployment"), pulumi.Alias(type_="azure-native:resources/v20191001:Deployment"), pulumi.Alias(type_="azure-native:resources/v20200601:Deployment"), pulumi.Alias(type_="azure-native:resources/v20200801:Deployment"), pulumi.Alias(type_="azure-native:resources/v20201001:Deployment"), pulumi.Alias(type_="azure-native:resources/v20210101:Deployment"), pulumi.Alias(type_="azure-native:resources/v20210401:Deployment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Deployment, __self__).__init__(
            'azure-native:resources/v20160201:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentArgs.__new__(DeploymentArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the deployment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.DeploymentPropertiesExtendedResponse']:
        """
        Deployment properties.
        """
        return pulumi.get(self, "properties")

