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
    'GetJitNetworkAccessPolicyResult',
    'AwaitableGetJitNetworkAccessPolicyResult',
    'get_jit_network_access_policy',
    'get_jit_network_access_policy_output',
]

@pulumi.output_type
class GetJitNetworkAccessPolicyResult:
    def __init__(__self__, id=None, kind=None, location=None, name=None, provisioning_state=None, requests=None, type=None, virtual_machines=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if requests and not isinstance(requests, list):
            raise TypeError("Expected argument 'requests' to be a list")
        pulumi.set(__self__, "requests", requests)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machines and not isinstance(virtual_machines, list):
            raise TypeError("Expected argument 'virtual_machines' to be a list")
        pulumi.set(__self__, "virtual_machines", virtual_machines)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the provisioning state of the Just-in-Time policy.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def requests(self) -> Optional[Sequence['outputs.JitNetworkAccessRequestResponse']]:
        return pulumi.get(self, "requests")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(self) -> Sequence['outputs.JitNetworkAccessPolicyVirtualMachineResponse']:
        """
        Configurations for Microsoft.Compute/virtualMachines resource type.
        """
        return pulumi.get(self, "virtual_machines")


class AwaitableGetJitNetworkAccessPolicyResult(GetJitNetworkAccessPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJitNetworkAccessPolicyResult(
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            requests=self.requests,
            type=self.type,
            virtual_machines=self.virtual_machines)


def get_jit_network_access_policy(asc_location: Optional[str] = None,
                                  jit_network_access_policy_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJitNetworkAccessPolicyResult:
    """
    Use this data source to access information about an existing resource.

    :param str asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :param str jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['ascLocation'] = asc_location
    __args__['jitNetworkAccessPolicyName'] = jit_network_access_policy_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20200101:getJitNetworkAccessPolicy', __args__, opts=opts, typ=GetJitNetworkAccessPolicyResult).value

    return AwaitableGetJitNetworkAccessPolicyResult(
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        requests=__ret__.requests,
        type=__ret__.type,
        virtual_machines=__ret__.virtual_machines)


@_utilities.lift_output_func(get_jit_network_access_policy)
def get_jit_network_access_policy_output(asc_location: Optional[pulumi.Input[str]] = None,
                                         jit_network_access_policy_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJitNetworkAccessPolicyResult]:
    """
    Use this data source to access information about an existing resource.

    :param str asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :param str jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
