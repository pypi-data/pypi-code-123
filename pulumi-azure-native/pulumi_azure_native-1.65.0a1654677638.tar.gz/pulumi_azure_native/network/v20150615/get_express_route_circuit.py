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
    'GetExpressRouteCircuitResult',
    'AwaitableGetExpressRouteCircuitResult',
    'get_express_route_circuit',
    'get_express_route_circuit_output',
]

warnings.warn("""Version v20150615 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""", DeprecationWarning)

@pulumi.output_type
class GetExpressRouteCircuitResult:
    """
    ExpressRouteCircuit resource
    """
    def __init__(__self__, authorizations=None, circuit_provisioning_state=None, etag=None, id=None, location=None, name=None, peerings=None, provisioning_state=None, service_key=None, service_provider_notes=None, service_provider_properties=None, service_provider_provisioning_state=None, sku=None, tags=None, type=None):
        if authorizations and not isinstance(authorizations, list):
            raise TypeError("Expected argument 'authorizations' to be a list")
        pulumi.set(__self__, "authorizations", authorizations)
        if circuit_provisioning_state and not isinstance(circuit_provisioning_state, str):
            raise TypeError("Expected argument 'circuit_provisioning_state' to be a str")
        pulumi.set(__self__, "circuit_provisioning_state", circuit_provisioning_state)
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
        if peerings and not isinstance(peerings, list):
            raise TypeError("Expected argument 'peerings' to be a list")
        pulumi.set(__self__, "peerings", peerings)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_key and not isinstance(service_key, str):
            raise TypeError("Expected argument 'service_key' to be a str")
        pulumi.set(__self__, "service_key", service_key)
        if service_provider_notes and not isinstance(service_provider_notes, str):
            raise TypeError("Expected argument 'service_provider_notes' to be a str")
        pulumi.set(__self__, "service_provider_notes", service_provider_notes)
        if service_provider_properties and not isinstance(service_provider_properties, dict):
            raise TypeError("Expected argument 'service_provider_properties' to be a dict")
        pulumi.set(__self__, "service_provider_properties", service_provider_properties)
        if service_provider_provisioning_state and not isinstance(service_provider_provisioning_state, str):
            raise TypeError("Expected argument 'service_provider_provisioning_state' to be a str")
        pulumi.set(__self__, "service_provider_provisioning_state", service_provider_provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def authorizations(self) -> Optional[Sequence['outputs.ExpressRouteCircuitAuthorizationResponse']]:
        """
        The list of authorizations.
        """
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter(name="circuitProvisioningState")
    def circuit_provisioning_state(self) -> Optional[str]:
        """
        The CircuitProvisioningState state of the resource.
        """
        return pulumi.get(self, "circuit_provisioning_state")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource Identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
    @pulumi.getter
    def peerings(self) -> Optional[Sequence['outputs.ExpressRouteCircuitPeeringResponse']]:
        """
        The list of peerings.
        """
        return pulumi.get(self, "peerings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[str]:
        """
        The ServiceKey.
        """
        return pulumi.get(self, "service_key")

    @property
    @pulumi.getter(name="serviceProviderNotes")
    def service_provider_notes(self) -> Optional[str]:
        """
        The ServiceProviderNotes.
        """
        return pulumi.get(self, "service_provider_notes")

    @property
    @pulumi.getter(name="serviceProviderProperties")
    def service_provider_properties(self) -> Optional['outputs.ExpressRouteCircuitServiceProviderPropertiesResponse']:
        """
        The ServiceProviderProperties.
        """
        return pulumi.get(self, "service_provider_properties")

    @property
    @pulumi.getter(name="serviceProviderProvisioningState")
    def service_provider_provisioning_state(self) -> Optional[str]:
        """
        The ServiceProviderProvisioningState state of the resource. Possible values are 'NotProvisioned', 'Provisioning', 'Provisioned', and 'Deprovisioning'.
        """
        return pulumi.get(self, "service_provider_provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ExpressRouteCircuitSkuResponse']:
        """
        The SKU.
        """
        return pulumi.get(self, "sku")

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


class AwaitableGetExpressRouteCircuitResult(GetExpressRouteCircuitResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExpressRouteCircuitResult(
            authorizations=self.authorizations,
            circuit_provisioning_state=self.circuit_provisioning_state,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            peerings=self.peerings,
            provisioning_state=self.provisioning_state,
            service_key=self.service_key,
            service_provider_notes=self.service_provider_notes,
            service_provider_properties=self.service_provider_properties,
            service_provider_provisioning_state=self.service_provider_provisioning_state,
            sku=self.sku,
            tags=self.tags,
            type=self.type)


def get_express_route_circuit(circuit_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExpressRouteCircuitResult:
    """
    ExpressRouteCircuit resource


    :param str circuit_name: The name of express route circuit.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_express_route_circuit is deprecated: Version v20150615 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""")
    __args__ = dict()
    __args__['circuitName'] = circuit_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20150615:getExpressRouteCircuit', __args__, opts=opts, typ=GetExpressRouteCircuitResult).value

    return AwaitableGetExpressRouteCircuitResult(
        authorizations=__ret__.authorizations,
        circuit_provisioning_state=__ret__.circuit_provisioning_state,
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        peerings=__ret__.peerings,
        provisioning_state=__ret__.provisioning_state,
        service_key=__ret__.service_key,
        service_provider_notes=__ret__.service_provider_notes,
        service_provider_properties=__ret__.service_provider_properties,
        service_provider_provisioning_state=__ret__.service_provider_provisioning_state,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_express_route_circuit)
def get_express_route_circuit_output(circuit_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExpressRouteCircuitResult]:
    """
    ExpressRouteCircuit resource


    :param str circuit_name: The name of express route circuit.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_express_route_circuit is deprecated: Version v20150615 will be removed in the next major version of the provider. Upgrade to version v20180501 or later.""")
    ...
