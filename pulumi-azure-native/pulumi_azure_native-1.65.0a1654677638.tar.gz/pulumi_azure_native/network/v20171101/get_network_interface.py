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
    'GetNetworkInterfaceResult',
    'AwaitableGetNetworkInterfaceResult',
    'get_network_interface',
    'get_network_interface_output',
]

warnings.warn("""Version v20171101 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""", DeprecationWarning)

@pulumi.output_type
class GetNetworkInterfaceResult:
    """
    A network interface in a resource group.
    """
    def __init__(__self__, dns_settings=None, enable_accelerated_networking=None, enable_ip_forwarding=None, etag=None, id=None, ip_configurations=None, location=None, mac_address=None, name=None, network_security_group=None, primary=None, provisioning_state=None, resource_guid=None, tags=None, type=None, virtual_machine=None):
        if dns_settings and not isinstance(dns_settings, dict):
            raise TypeError("Expected argument 'dns_settings' to be a dict")
        pulumi.set(__self__, "dns_settings", dns_settings)
        if enable_accelerated_networking and not isinstance(enable_accelerated_networking, bool):
            raise TypeError("Expected argument 'enable_accelerated_networking' to be a bool")
        pulumi.set(__self__, "enable_accelerated_networking", enable_accelerated_networking)
        if enable_ip_forwarding and not isinstance(enable_ip_forwarding, bool):
            raise TypeError("Expected argument 'enable_ip_forwarding' to be a bool")
        pulumi.set(__self__, "enable_ip_forwarding", enable_ip_forwarding)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_configurations and not isinstance(ip_configurations, list):
            raise TypeError("Expected argument 'ip_configurations' to be a list")
        pulumi.set(__self__, "ip_configurations", ip_configurations)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mac_address and not isinstance(mac_address, str):
            raise TypeError("Expected argument 'mac_address' to be a str")
        pulumi.set(__self__, "mac_address", mac_address)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_security_group and not isinstance(network_security_group, dict):
            raise TypeError("Expected argument 'network_security_group' to be a dict")
        pulumi.set(__self__, "network_security_group", network_security_group)
        if primary and not isinstance(primary, bool):
            raise TypeError("Expected argument 'primary' to be a bool")
        pulumi.set(__self__, "primary", primary)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machine and not isinstance(virtual_machine, dict):
            raise TypeError("Expected argument 'virtual_machine' to be a dict")
        pulumi.set(__self__, "virtual_machine", virtual_machine)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional['outputs.NetworkInterfaceDnsSettingsResponse']:
        """
        The DNS settings in network interface.
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[bool]:
        """
        If the network interface is accelerated networking enabled.
        """
        return pulumi.get(self, "enable_accelerated_networking")

    @property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[bool]:
        """
        Indicates whether IP forwarding is enabled on this network interface.
        """
        return pulumi.get(self, "enable_ip_forwarding")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
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
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[Sequence['outputs.NetworkInterfaceIPConfigurationResponse']]:
        """
        A list of IPConfigurations of the network interface.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[str]:
        """
        The MAC address of the network interface.
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional['outputs.NetworkSecurityGroupResponse']:
        """
        The reference of the NetworkSecurityGroup resource.
        """
        return pulumi.get(self, "network_security_group")

    @property
    @pulumi.getter
    def primary(self) -> Optional[bool]:
        """
        Gets whether this is a primary network interface on a virtual machine.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[str]:
        """
        The resource GUID property of the network interface resource.
        """
        return pulumi.get(self, "resource_guid")

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
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional['outputs.SubResourceResponse']:
        """
        The reference of a virtual machine.
        """
        return pulumi.get(self, "virtual_machine")


class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInterfaceResult(
            dns_settings=self.dns_settings,
            enable_accelerated_networking=self.enable_accelerated_networking,
            enable_ip_forwarding=self.enable_ip_forwarding,
            etag=self.etag,
            id=self.id,
            ip_configurations=self.ip_configurations,
            location=self.location,
            mac_address=self.mac_address,
            name=self.name,
            network_security_group=self.network_security_group,
            primary=self.primary,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            tags=self.tags,
            type=self.type,
            virtual_machine=self.virtual_machine)


def get_network_interface(expand: Optional[str] = None,
                          network_interface_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInterfaceResult:
    """
    A network interface in a resource group.


    :param str expand: Expands referenced resources.
    :param str network_interface_name: The name of the network interface.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_network_interface is deprecated: Version v20171101 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""")
    __args__ = dict()
    __args__['expand'] = expand
    __args__['networkInterfaceName'] = network_interface_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20171101:getNetworkInterface', __args__, opts=opts, typ=GetNetworkInterfaceResult).value

    return AwaitableGetNetworkInterfaceResult(
        dns_settings=__ret__.dns_settings,
        enable_accelerated_networking=__ret__.enable_accelerated_networking,
        enable_ip_forwarding=__ret__.enable_ip_forwarding,
        etag=__ret__.etag,
        id=__ret__.id,
        ip_configurations=__ret__.ip_configurations,
        location=__ret__.location,
        mac_address=__ret__.mac_address,
        name=__ret__.name,
        network_security_group=__ret__.network_security_group,
        primary=__ret__.primary,
        provisioning_state=__ret__.provisioning_state,
        resource_guid=__ret__.resource_guid,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_machine=__ret__.virtual_machine)


@_utilities.lift_output_func(get_network_interface)
def get_network_interface_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                 network_interface_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkInterfaceResult]:
    """
    A network interface in a resource group.


    :param str expand: Expands referenced resources.
    :param str network_interface_name: The name of the network interface.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_network_interface is deprecated: Version v20171101 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""")
    ...
