# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetVirtualWANResult',
    'AwaitableGetVirtualWANResult',
    'get_virtual_wan',
    'get_virtual_wan_output',
]

warnings.warn("""Version v20180401 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""", DeprecationWarning)

@pulumi.output_type
class GetVirtualWANResult:
    """
    VirtualWAN Resource.
    """
    def __init__(__self__, disable_vpn_encryption=None, etag=None, id=None, location=None, name=None, provisioning_state=None, tags=None, type=None, virtual_hubs=None, vpn_sites=None):
        if disable_vpn_encryption and not isinstance(disable_vpn_encryption, bool):
            raise TypeError("Expected argument 'disable_vpn_encryption' to be a bool")
        pulumi.set(__self__, "disable_vpn_encryption", disable_vpn_encryption)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_hubs and not isinstance(virtual_hubs, list):
            raise TypeError("Expected argument 'virtual_hubs' to be a list")
        pulumi.set(__self__, "virtual_hubs", virtual_hubs)
        if vpn_sites and not isinstance(vpn_sites, list):
            raise TypeError("Expected argument 'vpn_sites' to be a list")
        pulumi.set(__self__, "vpn_sites", vpn_sites)

    @property
    @pulumi.getter(name="disableVpnEncryption")
    def disable_vpn_encryption(self) -> Optional[bool]:
        """
        Vpn encryption to be disabled or not.
        """
        return pulumi.get(self, "disable_vpn_encryption")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHubs")
    def virtual_hubs(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of VirtualHubs in the VirtualWAN.
        """
        return pulumi.get(self, "virtual_hubs")

    @property
    @pulumi.getter(name="vpnSites")
    def vpn_sites(self) -> Sequence['outputs.SubResourceResponse']:
        return pulumi.get(self, "vpn_sites")


class AwaitableGetVirtualWANResult(GetVirtualWANResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualWANResult(
            disable_vpn_encryption=self.disable_vpn_encryption,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type,
            virtual_hubs=self.virtual_hubs,
            vpn_sites=self.vpn_sites)


def get_virtual_wan(resource_group_name: Optional[str] = None,
                    virtual_wan_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualWANResult:
    """
    VirtualWAN Resource.


    :param str resource_group_name: The resource group name of the VirtualWan.
    :param str virtual_wan_name: The name of the VirtualWAN being retrieved.
    """
    pulumi.log.warn("""get_virtual_wan is deprecated: Version v20180401 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualWANName'] = virtual_wan_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20180401:getVirtualWAN', __args__, opts=opts, typ=GetVirtualWANResult).value

    return AwaitableGetVirtualWANResult(
        disable_vpn_encryption=__ret__.disable_vpn_encryption,
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_hubs=__ret__.virtual_hubs,
        vpn_sites=__ret__.vpn_sites)


@_utilities.lift_output_func(get_virtual_wan)
def get_virtual_wan_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                           virtual_wan_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualWANResult]:
    """
    VirtualWAN Resource.


    :param str resource_group_name: The resource group name of the VirtualWan.
    :param str virtual_wan_name: The name of the VirtualWAN being retrieved.
    """
    pulumi.log.warn("""get_virtual_wan is deprecated: Version v20180401 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""")
    ...
