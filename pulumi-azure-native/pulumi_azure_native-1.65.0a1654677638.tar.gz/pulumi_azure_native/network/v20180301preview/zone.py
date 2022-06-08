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

__all__ = ['ZoneArgs', 'Zone']

@pulumi.input_type
class ZoneArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 registration_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]] = None,
                 resolution_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 zone_type: Optional[pulumi.Input['ZoneType']] = None):
        """
        The set of arguments for constructing a Zone resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]] registration_virtual_networks: A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.
        :param pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]] resolution_virtual_networks: A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] zone_name: The name of the DNS zone (without a terminating dot).
        :param pulumi.Input['ZoneType'] zone_type: The type of this DNS zone (Public or Private).
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if registration_virtual_networks is not None:
            pulumi.set(__self__, "registration_virtual_networks", registration_virtual_networks)
        if resolution_virtual_networks is not None:
            pulumi.set(__self__, "resolution_virtual_networks", resolution_virtual_networks)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone_name is not None:
            pulumi.set(__self__, "zone_name", zone_name)
        if zone_type is None:
            zone_type = 'Public'
        if zone_type is not None:
            pulumi.set(__self__, "zone_type", zone_type)

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
    @pulumi.getter(name="registrationVirtualNetworks")
    def registration_virtual_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]:
        """
        A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.
        """
        return pulumi.get(self, "registration_virtual_networks")

    @registration_virtual_networks.setter
    def registration_virtual_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]):
        pulumi.set(self, "registration_virtual_networks", value)

    @property
    @pulumi.getter(name="resolutionVirtualNetworks")
    def resolution_virtual_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]:
        """
        A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.
        """
        return pulumi.get(self, "resolution_virtual_networks")

    @resolution_virtual_networks.setter
    def resolution_virtual_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]):
        pulumi.set(self, "resolution_virtual_networks", value)

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

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DNS zone (without a terminating dot).
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_name", value)

    @property
    @pulumi.getter(name="zoneType")
    def zone_type(self) -> Optional[pulumi.Input['ZoneType']]:
        """
        The type of this DNS zone (Public or Private).
        """
        return pulumi.get(self, "zone_type")

    @zone_type.setter
    def zone_type(self, value: Optional[pulumi.Input['ZoneType']]):
        pulumi.set(self, "zone_type", value)


warnings.warn("""Version v20180301preview will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""", DeprecationWarning)


class Zone(pulumi.CustomResource):
    warnings.warn("""Version v20180301preview will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 registration_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 resolution_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 zone_type: Optional[pulumi.Input['ZoneType']] = None,
                 __props__=None):
        """
        Describes a DNS zone.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]] registration_virtual_networks: A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]] resolution_virtual_networks: A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] zone_name: The name of the DNS zone (without a terminating dot).
        :param pulumi.Input['ZoneType'] zone_type: The type of this DNS zone (Public or Private).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZoneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a DNS zone.

        :param str resource_name: The name of the resource.
        :param ZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 registration_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 resolution_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 zone_type: Optional[pulumi.Input['ZoneType']] = None,
                 __props__=None):
        pulumi.log.warn("""Zone is deprecated: Version v20180301preview will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneArgs.__new__(ZoneArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["registration_virtual_networks"] = registration_virtual_networks
            __props__.__dict__["resolution_virtual_networks"] = resolution_virtual_networks
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone_name"] = zone_name
            if zone_type is None:
                zone_type = 'Public'
            __props__.__dict__["zone_type"] = zone_type
            __props__.__dict__["etag"] = None
            __props__.__dict__["max_number_of_record_sets"] = None
            __props__.__dict__["max_number_of_records_per_record_set"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["name_servers"] = None
            __props__.__dict__["number_of_record_sets"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:Zone"), pulumi.Alias(type_="azure-native:network/v20150504preview:Zone"), pulumi.Alias(type_="azure-native:network/v20160401:Zone"), pulumi.Alias(type_="azure-native:network/v20170901:Zone"), pulumi.Alias(type_="azure-native:network/v20171001:Zone"), pulumi.Alias(type_="azure-native:network/v20180501:Zone")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Zone, __self__).__init__(
            'azure-native:network/v20180301preview:Zone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Zone':
        """
        Get an existing Zone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ZoneArgs.__new__(ZoneArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_number_of_record_sets"] = None
        __props__.__dict__["max_number_of_records_per_record_set"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["name_servers"] = None
        __props__.__dict__["number_of_record_sets"] = None
        __props__.__dict__["registration_virtual_networks"] = None
        __props__.__dict__["resolution_virtual_networks"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zone_type"] = None
        return Zone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The etag of the zone.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxNumberOfRecordSets")
    def max_number_of_record_sets(self) -> pulumi.Output[float]:
        """
        The maximum number of record sets that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "max_number_of_record_sets")

    @property
    @pulumi.getter(name="maxNumberOfRecordsPerRecordSet")
    def max_number_of_records_per_record_set(self) -> pulumi.Output[float]:
        """
        The maximum number of records per record set that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "max_number_of_records_per_record_set")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Sequence[str]]:
        """
        The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "name_servers")

    @property
    @pulumi.getter(name="numberOfRecordSets")
    def number_of_record_sets(self) -> pulumi.Output[float]:
        """
        The current number of record sets in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "number_of_record_sets")

    @property
    @pulumi.getter(name="registrationVirtualNetworks")
    def registration_virtual_networks(self) -> pulumi.Output[Optional[Sequence['outputs.SubResourceResponse']]]:
        """
        A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.
        """
        return pulumi.get(self, "registration_virtual_networks")

    @property
    @pulumi.getter(name="resolutionVirtualNetworks")
    def resolution_virtual_networks(self) -> pulumi.Output[Optional[Sequence['outputs.SubResourceResponse']]]:
        """
        A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.
        """
        return pulumi.get(self, "resolution_virtual_networks")

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

    @property
    @pulumi.getter(name="zoneType")
    def zone_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of this DNS zone (Public or Private).
        """
        return pulumi.get(self, "zone_type")

