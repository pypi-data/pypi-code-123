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
    'GetWebPubSubSharedPrivateLinkResourceResult',
    'AwaitableGetWebPubSubSharedPrivateLinkResourceResult',
    'get_web_pub_sub_shared_private_link_resource',
    'get_web_pub_sub_shared_private_link_resource_output',
]

@pulumi.output_type
class GetWebPubSubSharedPrivateLinkResourceResult:
    """
    Describes a Shared Private Link Resource
    """
    def __init__(__self__, group_id=None, id=None, name=None, private_link_resource_id=None, provisioning_state=None, request_message=None, status=None, system_data=None, type=None):
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_link_resource_id and not isinstance(private_link_resource_id, str):
            raise TypeError("Expected argument 'private_link_resource_id' to be a str")
        pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if request_message and not isinstance(request_message, str):
            raise TypeError("Expected argument 'request_message' to be a str")
        pulumi.set(__self__, "request_message", request_message)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> str:
        """
        The group id from the provider of resource the shared private link resource is for
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> str:
        """
        The resource id of the resource the shared private link resource is for
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the shared private link resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[str]:
        """
        The request message for requesting approval of the shared private link resource
        """
        return pulumi.get(self, "request_message")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the shared private link resource
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource - e.g. "Microsoft.SignalRService/SignalR"
        """
        return pulumi.get(self, "type")


class AwaitableGetWebPubSubSharedPrivateLinkResourceResult(GetWebPubSubSharedPrivateLinkResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebPubSubSharedPrivateLinkResourceResult(
            group_id=self.group_id,
            id=self.id,
            name=self.name,
            private_link_resource_id=self.private_link_resource_id,
            provisioning_state=self.provisioning_state,
            request_message=self.request_message,
            status=self.status,
            system_data=self.system_data,
            type=self.type)


def get_web_pub_sub_shared_private_link_resource(resource_group_name: Optional[str] = None,
                                                 resource_name: Optional[str] = None,
                                                 shared_private_link_resource_name: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebPubSubSharedPrivateLinkResourceResult:
    """
    Describes a Shared Private Link Resource


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str resource_name: The name of the resource.
    :param str shared_private_link_resource_name: The name of the shared private link resource
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    __args__['sharedPrivateLinkResourceName'] = shared_private_link_resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:webpubsub/v20210901preview:getWebPubSubSharedPrivateLinkResource', __args__, opts=opts, typ=GetWebPubSubSharedPrivateLinkResourceResult).value

    return AwaitableGetWebPubSubSharedPrivateLinkResourceResult(
        group_id=__ret__.group_id,
        id=__ret__.id,
        name=__ret__.name,
        private_link_resource_id=__ret__.private_link_resource_id,
        provisioning_state=__ret__.provisioning_state,
        request_message=__ret__.request_message,
        status=__ret__.status,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_web_pub_sub_shared_private_link_resource)
def get_web_pub_sub_shared_private_link_resource_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                        resource_name: Optional[pulumi.Input[str]] = None,
                                                        shared_private_link_resource_name: Optional[pulumi.Input[str]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebPubSubSharedPrivateLinkResourceResult]:
    """
    Describes a Shared Private Link Resource


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str resource_name: The name of the resource.
    :param str shared_private_link_resource_name: The name of the shared private link resource
    """
    ...
