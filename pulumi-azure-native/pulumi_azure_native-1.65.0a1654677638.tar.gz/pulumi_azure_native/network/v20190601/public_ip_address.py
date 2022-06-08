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

__all__ = ['PublicIPAddressInitArgs', 'PublicIPAddress']

@pulumi.input_type
class PublicIPAddressInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 ddos_settings: Optional[pulumi.Input['DdosSettingsArgs']] = None,
                 dns_settings: Optional[pulumi.Input['PublicIPAddressDnsSettingsArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input['IpTagArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 public_ip_address_version: Optional[pulumi.Input[Union[str, 'IPVersion']]] = None,
                 public_ip_allocation_method: Optional[pulumi.Input[Union[str, 'IPAllocationMethod']]] = None,
                 public_ip_prefix: Optional[pulumi.Input['SubResourceArgs']] = None,
                 public_ip_address_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['PublicIPAddressSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PublicIPAddress resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['DdosSettingsArgs'] ddos_settings: The DDoS protection custom policy associated with the public IP address.
        :param pulumi.Input['PublicIPAddressDnsSettingsArgs'] dns_settings: The FQDN of the DNS record associated with the public IP address.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] idle_timeout_in_minutes: The idle timeout of the public IP address.
        :param pulumi.Input[str] ip_address: The IP address associated with the public IP address resource.
        :param pulumi.Input[Sequence[pulumi.Input['IpTagArgs']]] ip_tags: The list of tags associated with the public IP address.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[Union[str, 'IPVersion']] public_ip_address_version: The public IP address version.
        :param pulumi.Input[Union[str, 'IPAllocationMethod']] public_ip_allocation_method: The public IP address allocation method.
        :param pulumi.Input['SubResourceArgs'] public_ip_prefix: The Public IP Prefix this Public IP Address should be allocated from.
        :param pulumi.Input[str] public_ip_address_name: The name of the public IP address.
        :param pulumi.Input[str] resource_guid: The resource GUID property of the public IP resource.
        :param pulumi.Input['PublicIPAddressSkuArgs'] sku: The public IP address SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if ddos_settings is not None:
            pulumi.set(__self__, "ddos_settings", ddos_settings)
        if dns_settings is not None:
            pulumi.set(__self__, "dns_settings", dns_settings)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if idle_timeout_in_minutes is not None:
            pulumi.set(__self__, "idle_timeout_in_minutes", idle_timeout_in_minutes)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if ip_tags is not None:
            pulumi.set(__self__, "ip_tags", ip_tags)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_ip_address_version is not None:
            pulumi.set(__self__, "public_ip_address_version", public_ip_address_version)
        if public_ip_allocation_method is not None:
            pulumi.set(__self__, "public_ip_allocation_method", public_ip_allocation_method)
        if public_ip_prefix is not None:
            pulumi.set(__self__, "public_ip_prefix", public_ip_prefix)
        if public_ip_address_name is not None:
            pulumi.set(__self__, "public_ip_address_name", public_ip_address_name)
        if resource_guid is not None:
            pulumi.set(__self__, "resource_guid", resource_guid)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

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
    @pulumi.getter(name="ddosSettings")
    def ddos_settings(self) -> Optional[pulumi.Input['DdosSettingsArgs']]:
        """
        The DDoS protection custom policy associated with the public IP address.
        """
        return pulumi.get(self, "ddos_settings")

    @ddos_settings.setter
    def ddos_settings(self, value: Optional[pulumi.Input['DdosSettingsArgs']]):
        pulumi.set(self, "ddos_settings", value)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input['PublicIPAddressDnsSettingsArgs']]:
        """
        The FQDN of the DNS record associated with the public IP address.
        """
        return pulumi.get(self, "dns_settings")

    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input['PublicIPAddressDnsSettingsArgs']]):
        pulumi.set(self, "dns_settings", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The idle timeout of the public IP address.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_timeout_in_minutes", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address associated with the public IP address resource.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpTagArgs']]]]:
        """
        The list of tags associated with the public IP address.
        """
        return pulumi.get(self, "ip_tags")

    @ip_tags.setter
    def ip_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpTagArgs']]]]):
        pulumi.set(self, "ip_tags", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> Optional[pulumi.Input[Union[str, 'IPVersion']]]:
        """
        The public IP address version.
        """
        return pulumi.get(self, "public_ip_address_version")

    @public_ip_address_version.setter
    def public_ip_address_version(self, value: Optional[pulumi.Input[Union[str, 'IPVersion']]]):
        pulumi.set(self, "public_ip_address_version", value)

    @property
    @pulumi.getter(name="publicIPAllocationMethod")
    def public_ip_allocation_method(self) -> Optional[pulumi.Input[Union[str, 'IPAllocationMethod']]]:
        """
        The public IP address allocation method.
        """
        return pulumi.get(self, "public_ip_allocation_method")

    @public_ip_allocation_method.setter
    def public_ip_allocation_method(self, value: Optional[pulumi.Input[Union[str, 'IPAllocationMethod']]]):
        pulumi.set(self, "public_ip_allocation_method", value)

    @property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The Public IP Prefix this Public IP Address should be allocated from.
        """
        return pulumi.get(self, "public_ip_prefix")

    @public_ip_prefix.setter
    def public_ip_prefix(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "public_ip_prefix", value)

    @property
    @pulumi.getter(name="publicIpAddressName")
    def public_ip_address_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the public IP address.
        """
        return pulumi.get(self, "public_ip_address_name")

    @public_ip_address_name.setter
    def public_ip_address_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip_address_name", value)

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[pulumi.Input[str]]:
        """
        The resource GUID property of the public IP resource.
        """
        return pulumi.get(self, "resource_guid")

    @resource_guid.setter
    def resource_guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_guid", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['PublicIPAddressSkuArgs']]:
        """
        The public IP address SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['PublicIPAddressSkuArgs']]):
        pulumi.set(self, "sku", value)

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
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class PublicIPAddress(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ddos_settings: Optional[pulumi.Input[pulumi.InputType['DdosSettingsArgs']]] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['PublicIPAddressDnsSettingsArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpTagArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 public_ip_address_version: Optional[pulumi.Input[Union[str, 'IPVersion']]] = None,
                 public_ip_allocation_method: Optional[pulumi.Input[Union[str, 'IPAllocationMethod']]] = None,
                 public_ip_prefix: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 public_ip_address_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['PublicIPAddressSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Public IP address resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DdosSettingsArgs']] ddos_settings: The DDoS protection custom policy associated with the public IP address.
        :param pulumi.Input[pulumi.InputType['PublicIPAddressDnsSettingsArgs']] dns_settings: The FQDN of the DNS record associated with the public IP address.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] idle_timeout_in_minutes: The idle timeout of the public IP address.
        :param pulumi.Input[str] ip_address: The IP address associated with the public IP address resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpTagArgs']]]] ip_tags: The list of tags associated with the public IP address.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[Union[str, 'IPVersion']] public_ip_address_version: The public IP address version.
        :param pulumi.Input[Union[str, 'IPAllocationMethod']] public_ip_allocation_method: The public IP address allocation method.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] public_ip_prefix: The Public IP Prefix this Public IP Address should be allocated from.
        :param pulumi.Input[str] public_ip_address_name: The name of the public IP address.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_guid: The resource GUID property of the public IP resource.
        :param pulumi.Input[pulumi.InputType['PublicIPAddressSkuArgs']] sku: The public IP address SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PublicIPAddressInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Public IP address resource.

        :param str resource_name: The name of the resource.
        :param PublicIPAddressInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublicIPAddressInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ddos_settings: Optional[pulumi.Input[pulumi.InputType['DdosSettingsArgs']]] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['PublicIPAddressDnsSettingsArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpTagArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 public_ip_address_version: Optional[pulumi.Input[Union[str, 'IPVersion']]] = None,
                 public_ip_allocation_method: Optional[pulumi.Input[Union[str, 'IPAllocationMethod']]] = None,
                 public_ip_prefix: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 public_ip_address_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['PublicIPAddressSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = PublicIPAddressInitArgs.__new__(PublicIPAddressInitArgs)

            __props__.__dict__["ddos_settings"] = ddos_settings
            __props__.__dict__["dns_settings"] = dns_settings
            __props__.__dict__["id"] = id
            __props__.__dict__["idle_timeout_in_minutes"] = idle_timeout_in_minutes
            __props__.__dict__["ip_address"] = ip_address
            __props__.__dict__["ip_tags"] = ip_tags
            __props__.__dict__["location"] = location
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["public_ip_address_version"] = public_ip_address_version
            __props__.__dict__["public_ip_allocation_method"] = public_ip_allocation_method
            __props__.__dict__["public_ip_prefix"] = public_ip_prefix
            __props__.__dict__["public_ip_address_name"] = public_ip_address_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_guid"] = resource_guid
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zones"] = zones
            __props__.__dict__["etag"] = None
            __props__.__dict__["ip_configuration"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20150501preview:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20150615:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20160330:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20160601:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20160901:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20161201:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20170301:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20170601:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20170801:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20170901:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20171001:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20171101:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20180101:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20180201:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20180401:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20180601:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20180701:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20180801:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20181001:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20181101:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20181201:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20190201:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20190401:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20190701:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20190801:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20190901:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20191101:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20191201:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20200301:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20200401:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20200501:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20200601:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20200701:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20200801:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20201101:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20210201:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20210301:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20210501:PublicIPAddress"), pulumi.Alias(type_="azure-native:network/v20210801:PublicIPAddress")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PublicIPAddress, __self__).__init__(
            'azure-native:network/v20190601:PublicIPAddress',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PublicIPAddress':
        """
        Get an existing PublicIPAddress resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PublicIPAddressInitArgs.__new__(PublicIPAddressInitArgs)

        __props__.__dict__["ddos_settings"] = None
        __props__.__dict__["dns_settings"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["idle_timeout_in_minutes"] = None
        __props__.__dict__["ip_address"] = None
        __props__.__dict__["ip_configuration"] = None
        __props__.__dict__["ip_tags"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_ip_address_version"] = None
        __props__.__dict__["public_ip_allocation_method"] = None
        __props__.__dict__["public_ip_prefix"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zones"] = None
        return PublicIPAddress(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ddosSettings")
    def ddos_settings(self) -> pulumi.Output[Optional['outputs.DdosSettingsResponse']]:
        """
        The DDoS protection custom policy associated with the public IP address.
        """
        return pulumi.get(self, "ddos_settings")

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[Optional['outputs.PublicIPAddressDnsSettingsResponse']]:
        """
        The FQDN of the DNS record associated with the public IP address.
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        The idle timeout of the public IP address.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[Optional[str]]:
        """
        The IP address associated with the public IP address resource.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> pulumi.Output['outputs.IPConfigurationResponse']:
        """
        The IP configuration associated with the public IP address.
        """
        return pulumi.get(self, "ip_configuration")

    @property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> pulumi.Output[Optional[Sequence['outputs.IpTagResponse']]]:
        """
        The list of tags associated with the public IP address.
        """
        return pulumi.get(self, "ip_tags")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> pulumi.Output[Optional[str]]:
        """
        The public IP address version.
        """
        return pulumi.get(self, "public_ip_address_version")

    @property
    @pulumi.getter(name="publicIPAllocationMethod")
    def public_ip_allocation_method(self) -> pulumi.Output[Optional[str]]:
        """
        The public IP address allocation method.
        """
        return pulumi.get(self, "public_ip_allocation_method")

    @property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The Public IP Prefix this Public IP Address should be allocated from.
        """
        return pulumi.get(self, "public_ip_prefix")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[Optional[str]]:
        """
        The resource GUID property of the public IP resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.PublicIPAddressSkuResponse']]:
        """
        The public IP address SKU.
        """
        return pulumi.get(self, "sku")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        return pulumi.get(self, "zones")

