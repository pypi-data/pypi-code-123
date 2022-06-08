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

__all__ = ['VirtualNetworkResourceArgs', 'VirtualNetworkResource']

@pulumi.input_type
class VirtualNetworkResourceArgs:
    def __init__(__self__, *,
                 lab_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 allowed_subnets: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_provider_resource_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 subnet_overrides: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetOverrideArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualNetworkResource resource.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]] allowed_subnets: The allowed subnets of the virtual network.
        :param pulumi.Input[str] description: The description of the virtual network.
        :param pulumi.Input[str] external_provider_resource_id: The Microsoft.Network resource identifier of the virtual network.
        :param pulumi.Input[str] id: The identifier of the resource.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[Sequence[pulumi.Input['SubnetOverrideArgs']]] subnet_overrides: The subnet overrides of the virtual network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] type: The type of the resource.
        """
        pulumi.set(__self__, "lab_name", lab_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if allowed_subnets is not None:
            pulumi.set(__self__, "allowed_subnets", allowed_subnets)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if external_provider_resource_id is not None:
            pulumi.set(__self__, "external_provider_resource_id", external_provider_resource_id)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if subnet_overrides is not None:
            pulumi.set(__self__, "subnet_overrides", subnet_overrides)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[str]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_name", value)

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
    @pulumi.getter(name="allowedSubnets")
    def allowed_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]]:
        """
        The allowed subnets of the virtual network.
        """
        return pulumi.get(self, "allowed_subnets")

    @allowed_subnets.setter
    def allowed_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]]):
        pulumi.set(self, "allowed_subnets", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the virtual network.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="externalProviderResourceId")
    def external_provider_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Microsoft.Network resource identifier of the virtual network.
        """
        return pulumi.get(self, "external_provider_resource_id")

    @external_provider_resource_id.setter
    def external_provider_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_provider_resource_id", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="subnetOverrides")
    def subnet_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetOverrideArgs']]]]:
        """
        The subnet overrides of the virtual network.
        """
        return pulumi.get(self, "subnet_overrides")

    @subnet_overrides.setter
    def subnet_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetOverrideArgs']]]]):
        pulumi.set(self, "subnet_overrides", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


warnings.warn("""Version v20150521preview will be removed in the next major version of the provider. Upgrade to version v20180915 or later.""", DeprecationWarning)


class VirtualNetworkResource(pulumi.CustomResource):
    warnings.warn("""Version v20150521preview will be removed in the next major version of the provider. Upgrade to version v20180915 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_provider_resource_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetOverrideArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A virtual network.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]] allowed_subnets: The allowed subnets of the virtual network.
        :param pulumi.Input[str] description: The description of the virtual network.
        :param pulumi.Input[str] external_provider_resource_id: The Microsoft.Network resource identifier of the virtual network.
        :param pulumi.Input[str] id: The identifier of the resource.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetOverrideArgs']]]] subnet_overrides: The subnet overrides of the virtual network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] type: The type of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualNetworkResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A virtual network.

        :param str resource_name: The name of the resource.
        :param VirtualNetworkResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualNetworkResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_provider_resource_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetOverrideArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""VirtualNetworkResource is deprecated: Version v20150521preview will be removed in the next major version of the provider. Upgrade to version v20180915 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualNetworkResourceArgs.__new__(VirtualNetworkResourceArgs)

            __props__.__dict__["allowed_subnets"] = allowed_subnets
            __props__.__dict__["description"] = description
            __props__.__dict__["external_provider_resource_id"] = external_provider_resource_id
            __props__.__dict__["id"] = id
            if lab_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_name'")
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subnet_overrides"] = subnet_overrides
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devtestlab:VirtualNetworkResource"), pulumi.Alias(type_="azure-native:devtestlab/v20160515:VirtualNetworkResource"), pulumi.Alias(type_="azure-native:devtestlab/v20180915:VirtualNetworkResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualNetworkResource, __self__).__init__(
            'azure-native:devtestlab/v20150521preview:VirtualNetworkResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualNetworkResource':
        """
        Get an existing VirtualNetworkResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualNetworkResourceArgs.__new__(VirtualNetworkResourceArgs)

        __props__.__dict__["allowed_subnets"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["external_provider_resource_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["subnet_overrides"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return VirtualNetworkResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedSubnets")
    def allowed_subnets(self) -> pulumi.Output[Optional[Sequence['outputs.SubnetResponse']]]:
        """
        The allowed subnets of the virtual network.
        """
        return pulumi.get(self, "allowed_subnets")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the virtual network.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="externalProviderResourceId")
    def external_provider_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Microsoft.Network resource identifier of the virtual network.
        """
        return pulumi.get(self, "external_provider_resource_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="subnetOverrides")
    def subnet_overrides(self) -> pulumi.Output[Optional[Sequence['outputs.SubnetOverrideResponse']]]:
        """
        The subnet overrides of the virtual network.
        """
        return pulumi.get(self, "subnet_overrides")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

