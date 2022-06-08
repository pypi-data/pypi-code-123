# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['InstanceDetailsArgs', 'InstanceDetails']

@pulumi.input_type
class InstanceDetailsArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 administration: Optional[pulumi.Input['DFPInstanceAdministratorsArgs']] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InstanceDetails resource.
        :param pulumi.Input[str] resource_group_name: The name of the Azure Resource group of which a given DFP instance is part. This name must be at least 1 character in length, and no more than 90.
        :param pulumi.Input['DFPInstanceAdministratorsArgs'] administration: A collection of DFP instance administrators
        :param pulumi.Input[str] instance_name: The name of the DFP instances. It must be a minimum of 3 characters, and a maximum of 63.
        :param pulumi.Input[str] location: Location of the DFP resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional resource provisioning properties.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if administration is not None:
            pulumi.set(__self__, "administration", administration)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure Resource group of which a given DFP instance is part. This name must be at least 1 character in length, and no more than 90.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def administration(self) -> Optional[pulumi.Input['DFPInstanceAdministratorsArgs']]:
        """
        A collection of DFP instance administrators
        """
        return pulumi.get(self, "administration")

    @administration.setter
    def administration(self, value: Optional[pulumi.Input['DFPInstanceAdministratorsArgs']]):
        pulumi.set(self, "administration", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DFP instances. It must be a minimum of 3 characters, and a maximum of 63.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the DFP resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class InstanceDetails(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administration: Optional[pulumi.Input[pulumi.InputType['DFPInstanceAdministratorsArgs']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents an instance of a DFP instance resource.
        API Version: 2021-02-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DFPInstanceAdministratorsArgs']] administration: A collection of DFP instance administrators
        :param pulumi.Input[str] instance_name: The name of the DFP instances. It must be a minimum of 3 characters, and a maximum of 63.
        :param pulumi.Input[str] location: Location of the DFP resource.
        :param pulumi.Input[str] resource_group_name: The name of the Azure Resource group of which a given DFP instance is part. This name must be at least 1 character in length, and no more than 90.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional resource provisioning properties.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceDetailsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an instance of a DFP instance resource.
        API Version: 2021-02-01-preview.

        :param str resource_name: The name of the resource.
        :param InstanceDetailsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceDetailsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administration: Optional[pulumi.Input[pulumi.InputType['DFPInstanceAdministratorsArgs']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = InstanceDetailsArgs.__new__(InstanceDetailsArgs)

            __props__.__dict__["administration"] = administration
            __props__.__dict__["instance_name"] = instance_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dynamics365fraudprotection/v20210201preview:InstanceDetails")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InstanceDetails, __self__).__init__(
            'azure-native:dynamics365fraudprotection:InstanceDetails',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstanceDetails':
        """
        Get an existing InstanceDetails resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceDetailsArgs.__new__(InstanceDetailsArgs)

        __props__.__dict__["administration"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return InstanceDetails(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def administration(self) -> pulumi.Output[Optional['outputs.DFPInstanceAdministratorsResponse']]:
        """
        A collection of DFP instance administrators
        """
        return pulumi.get(self, "administration")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the DFP resource.
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment state of DFP resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

