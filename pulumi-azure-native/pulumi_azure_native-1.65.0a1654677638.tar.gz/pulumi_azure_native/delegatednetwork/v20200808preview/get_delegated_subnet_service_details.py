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
    'GetDelegatedSubnetServiceDetailsResult',
    'AwaitableGetDelegatedSubnetServiceDetailsResult',
    'get_delegated_subnet_service_details',
    'get_delegated_subnet_service_details_output',
]

warnings.warn("""Version v20200808preview will be removed in the next major version of the provider. Upgrade to version v20210315 or later.""", DeprecationWarning)

@pulumi.output_type
class GetDelegatedSubnetServiceDetailsResult:
    """
    Represents an instance of a orchestrator.
    """
    def __init__(__self__, controller_details=None, id=None, location=None, name=None, provisioning_state=None, resource_guid=None, subnet_details=None, tags=None, type=None):
        if controller_details and not isinstance(controller_details, dict):
            raise TypeError("Expected argument 'controller_details' to be a dict")
        pulumi.set(__self__, "controller_details", controller_details)
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
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if subnet_details and not isinstance(subnet_details, dict):
            raise TypeError("Expected argument 'subnet_details' to be a dict")
        pulumi.set(__self__, "subnet_details", subnet_details)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> Optional['outputs.ControllerDetailsResponse']:
        """
        Properties of the controller.
        """
        return pulumi.get(self, "controller_details")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current state of dnc delegated subnet resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        Resource guid.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="subnetDetails")
    def subnet_details(self) -> Optional['outputs.SubnetDetailsResponse']:
        """
        subnet details
        """
        return pulumi.get(self, "subnet_details")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetDelegatedSubnetServiceDetailsResult(GetDelegatedSubnetServiceDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDelegatedSubnetServiceDetailsResult(
            controller_details=self.controller_details,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            subnet_details=self.subnet_details,
            tags=self.tags,
            type=self.type)


def get_delegated_subnet_service_details(resource_group_name: Optional[str] = None,
                                         resource_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDelegatedSubnetServiceDetailsResult:
    """
    Represents an instance of a orchestrator.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
    """
    pulumi.log.warn("""get_delegated_subnet_service_details is deprecated: Version v20200808preview will be removed in the next major version of the provider. Upgrade to version v20210315 or later.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:delegatednetwork/v20200808preview:getDelegatedSubnetServiceDetails', __args__, opts=opts, typ=GetDelegatedSubnetServiceDetailsResult).value

    return AwaitableGetDelegatedSubnetServiceDetailsResult(
        controller_details=__ret__.controller_details,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        resource_guid=__ret__.resource_guid,
        subnet_details=__ret__.subnet_details,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_delegated_subnet_service_details)
def get_delegated_subnet_service_details_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                resource_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDelegatedSubnetServiceDetailsResult]:
    """
    Represents an instance of a orchestrator.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
    """
    pulumi.log.warn("""get_delegated_subnet_service_details is deprecated: Version v20200808preview will be removed in the next major version of the provider. Upgrade to version v20210315 or later.""")
    ...
