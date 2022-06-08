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

__all__ = ['PrivateEndpointInitArgs', 'PrivateEndpoint']

@pulumi.input_type
class PrivateEndpointInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 manual_private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]] = None,
                 private_endpoint_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]] = None,
                 subnet: Optional[pulumi.Input['SubnetArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PrivateEndpoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]] manual_private_link_service_connections: A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.
        :param pulumi.Input[str] private_endpoint_name: The name of the private endpoint.
        :param pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]] private_link_service_connections: A grouping of information about the connection to the remote resource.
        :param pulumi.Input['SubnetArgs'] subnet: The ID of the subnet from which the private IP will be allocated.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if manual_private_link_service_connections is not None:
            pulumi.set(__self__, "manual_private_link_service_connections", manual_private_link_service_connections)
        if private_endpoint_name is not None:
            pulumi.set(__self__, "private_endpoint_name", private_endpoint_name)
        if private_link_service_connections is not None:
            pulumi.set(__self__, "private_link_service_connections", private_link_service_connections)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]:
        """
        A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.
        """
        return pulumi.get(self, "manual_private_link_service_connections")

    @manual_private_link_service_connections.setter
    def manual_private_link_service_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]):
        pulumi.set(self, "manual_private_link_service_connections", value)

    @property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the private endpoint.
        """
        return pulumi.get(self, "private_endpoint_name")

    @private_endpoint_name.setter
    def private_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_name", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]:
        """
        A grouping of information about the connection to the remote resource.
        """
        return pulumi.get(self, "private_link_service_connections")

    @private_link_service_connections.setter
    def private_link_service_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]):
        pulumi.set(self, "private_link_service_connections", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input['SubnetArgs']]:
        """
        The ID of the subnet from which the private IP will be allocated.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input['SubnetArgs']]):
        pulumi.set(self, "subnet", value)

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


class PrivateEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 manual_private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionArgs']]]]] = None,
                 private_endpoint_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['SubnetArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Private endpoint resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionArgs']]]] manual_private_link_service_connections: A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.
        :param pulumi.Input[str] private_endpoint_name: The name of the private endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionArgs']]]] private_link_service_connections: A grouping of information about the connection to the remote resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SubnetArgs']] subnet: The ID of the subnet from which the private IP will be allocated.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateEndpointInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Private endpoint resource.

        :param str resource_name: The name of the resource.
        :param PrivateEndpointInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateEndpointInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 manual_private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionArgs']]]]] = None,
                 private_endpoint_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['SubnetArgs']]] = None,
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
            __props__ = PrivateEndpointInitArgs.__new__(PrivateEndpointInitArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["manual_private_link_service_connections"] = manual_private_link_service_connections
            __props__.__dict__["private_endpoint_name"] = private_endpoint_name
            __props__.__dict__["private_link_service_connections"] = private_link_service_connections
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subnet"] = subnet
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["network_interfaces"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20180801:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20181001:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20181101:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20181201:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20190201:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20190401:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20190601:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20190801:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20190901:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20191101:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20191201:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20200301:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20200401:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20200501:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20200601:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20200701:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20200801:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20201101:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20210201:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20210301:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20210501:PrivateEndpoint"), pulumi.Alias(type_="azure-native:network/v20210801:PrivateEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpoint, __self__).__init__(
            'azure-native:network/v20190701:PrivateEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateEndpoint':
        """
        Get an existing PrivateEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateEndpointInitArgs.__new__(PrivateEndpointInitArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["manual_private_link_service_connections"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_interfaces"] = None
        __props__.__dict__["private_link_service_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["subnet"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateLinkServiceConnectionResponse']]]:
        """
        A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.
        """
        return pulumi.get(self, "manual_private_link_service_connections")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Sequence['outputs.NetworkInterfaceResponse']]:
        """
        An array of references to the network interfaces created for this private endpoint.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateLinkServiceConnectionResponse']]]:
        """
        A grouping of information about the connection to the remote resource.
        """
        return pulumi.get(self, "private_link_service_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the private endpoint resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional['outputs.SubnetResponse']]:
        """
        The ID of the subnet from which the private IP will be allocated.
        """
        return pulumi.get(self, "subnet")

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

