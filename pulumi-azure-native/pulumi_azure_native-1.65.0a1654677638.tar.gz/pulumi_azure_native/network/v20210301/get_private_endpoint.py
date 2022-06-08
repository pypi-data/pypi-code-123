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
    'GetPrivateEndpointResult',
    'AwaitableGetPrivateEndpointResult',
    'get_private_endpoint',
    'get_private_endpoint_output',
]

@pulumi.output_type
class GetPrivateEndpointResult:
    """
    Private endpoint resource.
    """
    def __init__(__self__, application_security_groups=None, custom_dns_configs=None, custom_network_interface_name=None, etag=None, extended_location=None, id=None, ip_configurations=None, location=None, manual_private_link_service_connections=None, name=None, network_interfaces=None, private_link_service_connections=None, provisioning_state=None, subnet=None, tags=None, type=None):
        if application_security_groups and not isinstance(application_security_groups, list):
            raise TypeError("Expected argument 'application_security_groups' to be a list")
        pulumi.set(__self__, "application_security_groups", application_security_groups)
        if custom_dns_configs and not isinstance(custom_dns_configs, list):
            raise TypeError("Expected argument 'custom_dns_configs' to be a list")
        pulumi.set(__self__, "custom_dns_configs", custom_dns_configs)
        if custom_network_interface_name and not isinstance(custom_network_interface_name, str):
            raise TypeError("Expected argument 'custom_network_interface_name' to be a str")
        pulumi.set(__self__, "custom_network_interface_name", custom_network_interface_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_configurations and not isinstance(ip_configurations, list):
            raise TypeError("Expected argument 'ip_configurations' to be a list")
        pulumi.set(__self__, "ip_configurations", ip_configurations)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if manual_private_link_service_connections and not isinstance(manual_private_link_service_connections, list):
            raise TypeError("Expected argument 'manual_private_link_service_connections' to be a list")
        pulumi.set(__self__, "manual_private_link_service_connections", manual_private_link_service_connections)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_interfaces and not isinstance(network_interfaces, list):
            raise TypeError("Expected argument 'network_interfaces' to be a list")
        pulumi.set(__self__, "network_interfaces", network_interfaces)
        if private_link_service_connections and not isinstance(private_link_service_connections, list):
            raise TypeError("Expected argument 'private_link_service_connections' to be a list")
        pulumi.set(__self__, "private_link_service_connections", private_link_service_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if subnet and not isinstance(subnet, dict):
            raise TypeError("Expected argument 'subnet' to be a dict")
        pulumi.set(__self__, "subnet", subnet)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(self) -> Optional[Sequence['outputs.ApplicationSecurityGroupResponse']]:
        """
        Application security groups in which the private endpoint IP configuration is included.
        """
        return pulumi.get(self, "application_security_groups")

    @property
    @pulumi.getter(name="customDnsConfigs")
    def custom_dns_configs(self) -> Optional[Sequence['outputs.CustomDnsConfigPropertiesFormatResponse']]:
        """
        An array of custom dns configurations.
        """
        return pulumi.get(self, "custom_dns_configs")

    @property
    @pulumi.getter(name="customNetworkInterfaceName")
    def custom_network_interface_name(self) -> Optional[str]:
        """
        The custom name of the network interface attached to the private endpoint.
        """
        return pulumi.get(self, "custom_network_interface_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location of the load balancer.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[Sequence['outputs.PrivateEndpointIPConfigurationResponse']]:
        """
        A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints.
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
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> Optional[Sequence['outputs.PrivateLinkServiceConnectionResponse']]:
        """
        A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.
        """
        return pulumi.get(self, "manual_private_link_service_connections")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence['outputs.NetworkInterfaceResponse']:
        """
        An array of references to the network interfaces created for this private endpoint.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(self) -> Optional[Sequence['outputs.PrivateLinkServiceConnectionResponse']]:
        """
        A grouping of information about the connection to the remote resource.
        """
        return pulumi.get(self, "private_link_service_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def subnet(self) -> Optional['outputs.SubnetResponse']:
        """
        The ID of the subnet from which the private IP will be allocated.
        """
        return pulumi.get(self, "subnet")

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


class AwaitableGetPrivateEndpointResult(GetPrivateEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointResult(
            application_security_groups=self.application_security_groups,
            custom_dns_configs=self.custom_dns_configs,
            custom_network_interface_name=self.custom_network_interface_name,
            etag=self.etag,
            extended_location=self.extended_location,
            id=self.id,
            ip_configurations=self.ip_configurations,
            location=self.location,
            manual_private_link_service_connections=self.manual_private_link_service_connections,
            name=self.name,
            network_interfaces=self.network_interfaces,
            private_link_service_connections=self.private_link_service_connections,
            provisioning_state=self.provisioning_state,
            subnet=self.subnet,
            tags=self.tags,
            type=self.type)


def get_private_endpoint(expand: Optional[str] = None,
                         private_endpoint_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointResult:
    """
    Private endpoint resource.


    :param str expand: Expands referenced resources.
    :param str private_endpoint_name: The name of the private endpoint.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['privateEndpointName'] = private_endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20210301:getPrivateEndpoint', __args__, opts=opts, typ=GetPrivateEndpointResult).value

    return AwaitableGetPrivateEndpointResult(
        application_security_groups=__ret__.application_security_groups,
        custom_dns_configs=__ret__.custom_dns_configs,
        custom_network_interface_name=__ret__.custom_network_interface_name,
        etag=__ret__.etag,
        extended_location=__ret__.extended_location,
        id=__ret__.id,
        ip_configurations=__ret__.ip_configurations,
        location=__ret__.location,
        manual_private_link_service_connections=__ret__.manual_private_link_service_connections,
        name=__ret__.name,
        network_interfaces=__ret__.network_interfaces,
        private_link_service_connections=__ret__.private_link_service_connections,
        provisioning_state=__ret__.provisioning_state,
        subnet=__ret__.subnet,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_private_endpoint)
def get_private_endpoint_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                private_endpoint_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateEndpointResult]:
    """
    Private endpoint resource.


    :param str expand: Expands referenced resources.
    :param str private_endpoint_name: The name of the private endpoint.
    :param str resource_group_name: The name of the resource group.
    """
    ...
