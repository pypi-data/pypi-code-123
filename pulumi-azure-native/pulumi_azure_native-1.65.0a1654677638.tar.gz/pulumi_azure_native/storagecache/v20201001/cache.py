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

__all__ = ['CacheArgs', 'Cache']

@pulumi.input_type
class CacheArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 cache_name: Optional[pulumi.Input[str]] = None,
                 cache_size_gb: Optional[pulumi.Input[int]] = None,
                 directory_services_settings: Optional[pulumi.Input['CacheDirectorySettingsArgs']] = None,
                 encryption_settings: Optional[pulumi.Input['CacheEncryptionSettingsArgs']] = None,
                 identity: Optional[pulumi.Input['CacheIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_settings: Optional[pulumi.Input['CacheNetworkSettingsArgs']] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningStateType']]] = None,
                 security_settings: Optional[pulumi.Input['CacheSecuritySettingsArgs']] = None,
                 sku: Optional[pulumi.Input['CacheSkuArgs']] = None,
                 subnet: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a Cache resource.
        :param pulumi.Input[str] resource_group_name: Target resource group.
        :param pulumi.Input[str] cache_name: Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.
        :param pulumi.Input[int] cache_size_gb: The size of this Cache, in GB.
        :param pulumi.Input['CacheDirectorySettingsArgs'] directory_services_settings: Specifies Directory Services settings of the cache.
        :param pulumi.Input['CacheEncryptionSettingsArgs'] encryption_settings: Specifies encryption settings of the cache.
        :param pulumi.Input['CacheIdentityArgs'] identity: The identity of the cache, if configured.
        :param pulumi.Input[str] location: Region name string.
        :param pulumi.Input['CacheNetworkSettingsArgs'] network_settings: Specifies network settings of the cache.
        :param pulumi.Input[Union[str, 'ProvisioningStateType']] provisioning_state: ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
        :param pulumi.Input['CacheSecuritySettingsArgs'] security_settings: Specifies security settings of the cache.
        :param pulumi.Input['CacheSkuArgs'] sku: SKU for the Cache.
        :param pulumi.Input[str] subnet: Subnet used for the Cache.
        :param Any tags: ARM tags as name/value pairs.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cache_name is not None:
            pulumi.set(__self__, "cache_name", cache_name)
        if cache_size_gb is not None:
            pulumi.set(__self__, "cache_size_gb", cache_size_gb)
        if directory_services_settings is not None:
            pulumi.set(__self__, "directory_services_settings", directory_services_settings)
        if encryption_settings is not None:
            pulumi.set(__self__, "encryption_settings", encryption_settings)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_settings is not None:
            pulumi.set(__self__, "network_settings", network_settings)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if security_settings is not None:
            pulumi.set(__self__, "security_settings", security_settings)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Target resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="cacheName")
    def cache_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.
        """
        return pulumi.get(self, "cache_name")

    @cache_name.setter
    def cache_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_name", value)

    @property
    @pulumi.getter(name="cacheSizeGB")
    def cache_size_gb(self) -> Optional[pulumi.Input[int]]:
        """
        The size of this Cache, in GB.
        """
        return pulumi.get(self, "cache_size_gb")

    @cache_size_gb.setter
    def cache_size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cache_size_gb", value)

    @property
    @pulumi.getter(name="directoryServicesSettings")
    def directory_services_settings(self) -> Optional[pulumi.Input['CacheDirectorySettingsArgs']]:
        """
        Specifies Directory Services settings of the cache.
        """
        return pulumi.get(self, "directory_services_settings")

    @directory_services_settings.setter
    def directory_services_settings(self, value: Optional[pulumi.Input['CacheDirectorySettingsArgs']]):
        pulumi.set(self, "directory_services_settings", value)

    @property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[pulumi.Input['CacheEncryptionSettingsArgs']]:
        """
        Specifies encryption settings of the cache.
        """
        return pulumi.get(self, "encryption_settings")

    @encryption_settings.setter
    def encryption_settings(self, value: Optional[pulumi.Input['CacheEncryptionSettingsArgs']]):
        pulumi.set(self, "encryption_settings", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['CacheIdentityArgs']]:
        """
        The identity of the cache, if configured.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['CacheIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Region name string.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> Optional[pulumi.Input['CacheNetworkSettingsArgs']]:
        """
        Specifies network settings of the cache.
        """
        return pulumi.get(self, "network_settings")

    @network_settings.setter
    def network_settings(self, value: Optional[pulumi.Input['CacheNetworkSettingsArgs']]):
        pulumi.set(self, "network_settings", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningStateType']]]:
        """
        ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningStateType']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input['CacheSecuritySettingsArgs']]:
        """
        Specifies security settings of the cache.
        """
        return pulumi.get(self, "security_settings")

    @security_settings.setter
    def security_settings(self, value: Optional[pulumi.Input['CacheSecuritySettingsArgs']]):
        pulumi.set(self, "security_settings", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['CacheSkuArgs']]:
        """
        SKU for the Cache.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['CacheSkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[str]]:
        """
        Subnet used for the Cache.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        ARM tags as name/value pairs.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version v20201001 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""", DeprecationWarning)


class Cache(pulumi.CustomResource):
    warnings.warn("""Version v20201001 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_name: Optional[pulumi.Input[str]] = None,
                 cache_size_gb: Optional[pulumi.Input[int]] = None,
                 directory_services_settings: Optional[pulumi.Input[pulumi.InputType['CacheDirectorySettingsArgs']]] = None,
                 encryption_settings: Optional[pulumi.Input[pulumi.InputType['CacheEncryptionSettingsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['CacheIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_settings: Optional[pulumi.Input[pulumi.InputType['CacheNetworkSettingsArgs']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningStateType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_settings: Optional[pulumi.Input[pulumi.InputType['CacheSecuritySettingsArgs']]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['CacheSkuArgs']]] = None,
                 subnet: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        A Cache instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cache_name: Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.
        :param pulumi.Input[int] cache_size_gb: The size of this Cache, in GB.
        :param pulumi.Input[pulumi.InputType['CacheDirectorySettingsArgs']] directory_services_settings: Specifies Directory Services settings of the cache.
        :param pulumi.Input[pulumi.InputType['CacheEncryptionSettingsArgs']] encryption_settings: Specifies encryption settings of the cache.
        :param pulumi.Input[pulumi.InputType['CacheIdentityArgs']] identity: The identity of the cache, if configured.
        :param pulumi.Input[str] location: Region name string.
        :param pulumi.Input[pulumi.InputType['CacheNetworkSettingsArgs']] network_settings: Specifies network settings of the cache.
        :param pulumi.Input[Union[str, 'ProvisioningStateType']] provisioning_state: ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
        :param pulumi.Input[str] resource_group_name: Target resource group.
        :param pulumi.Input[pulumi.InputType['CacheSecuritySettingsArgs']] security_settings: Specifies security settings of the cache.
        :param pulumi.Input[pulumi.InputType['CacheSkuArgs']] sku: SKU for the Cache.
        :param pulumi.Input[str] subnet: Subnet used for the Cache.
        :param Any tags: ARM tags as name/value pairs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CacheArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Cache instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md

        :param str resource_name: The name of the resource.
        :param CacheArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CacheArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_name: Optional[pulumi.Input[str]] = None,
                 cache_size_gb: Optional[pulumi.Input[int]] = None,
                 directory_services_settings: Optional[pulumi.Input[pulumi.InputType['CacheDirectorySettingsArgs']]] = None,
                 encryption_settings: Optional[pulumi.Input[pulumi.InputType['CacheEncryptionSettingsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['CacheIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_settings: Optional[pulumi.Input[pulumi.InputType['CacheNetworkSettingsArgs']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningStateType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_settings: Optional[pulumi.Input[pulumi.InputType['CacheSecuritySettingsArgs']]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['CacheSkuArgs']]] = None,
                 subnet: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        pulumi.log.warn("""Cache is deprecated: Version v20201001 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CacheArgs.__new__(CacheArgs)

            __props__.__dict__["cache_name"] = cache_name
            __props__.__dict__["cache_size_gb"] = cache_size_gb
            __props__.__dict__["directory_services_settings"] = directory_services_settings
            __props__.__dict__["encryption_settings"] = encryption_settings
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["network_settings"] = network_settings
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["security_settings"] = security_settings
            __props__.__dict__["sku"] = sku
            __props__.__dict__["subnet"] = subnet
            __props__.__dict__["tags"] = tags
            __props__.__dict__["health"] = None
            __props__.__dict__["mount_addresses"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["upgrade_status"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storagecache:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20190801preview:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20191101:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20200301:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20210301:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20210501:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20210901:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20220101:Cache"), pulumi.Alias(type_="azure-native:storagecache/v20220501:Cache")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cache, __self__).__init__(
            'azure-native:storagecache/v20201001:Cache',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cache':
        """
        Get an existing Cache resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CacheArgs.__new__(CacheArgs)

        __props__.__dict__["cache_size_gb"] = None
        __props__.__dict__["directory_services_settings"] = None
        __props__.__dict__["encryption_settings"] = None
        __props__.__dict__["health"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mount_addresses"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_settings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["security_settings"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["subnet"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["upgrade_status"] = None
        return Cache(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cacheSizeGB")
    def cache_size_gb(self) -> pulumi.Output[Optional[int]]:
        """
        The size of this Cache, in GB.
        """
        return pulumi.get(self, "cache_size_gb")

    @property
    @pulumi.getter(name="directoryServicesSettings")
    def directory_services_settings(self) -> pulumi.Output[Optional['outputs.CacheDirectorySettingsResponse']]:
        """
        Specifies Directory Services settings of the cache.
        """
        return pulumi.get(self, "directory_services_settings")

    @property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> pulumi.Output[Optional['outputs.CacheEncryptionSettingsResponse']]:
        """
        Specifies encryption settings of the cache.
        """
        return pulumi.get(self, "encryption_settings")

    @property
    @pulumi.getter
    def health(self) -> pulumi.Output['outputs.CacheHealthResponse']:
        """
        Health of the Cache.
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.CacheIdentityResponse']]:
        """
        The identity of the cache, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Region name string.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mountAddresses")
    def mount_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        Array of IP addresses that can be used by clients mounting this Cache.
        """
        return pulumi.get(self, "mount_addresses")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of Cache.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> pulumi.Output[Optional['outputs.CacheNetworkSettingsResponse']]:
        """
        Specifies network settings of the cache.
        """
        return pulumi.get(self, "network_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Output[Optional['outputs.CacheSecuritySettingsResponse']]:
        """
        Specifies security settings of the cache.
        """
        return pulumi.get(self, "security_settings")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.CacheResponseSku']]:
        """
        SKU for the Cache.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional[str]]:
        """
        Subnet used for the Cache.
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        ARM tags as name/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the Cache; Microsoft.StorageCache/Cache
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> pulumi.Output[Optional['outputs.CacheUpgradeStatusResponse']]:
        """
        Upgrade status of the Cache.
        """
        return pulumi.get(self, "upgrade_status")

