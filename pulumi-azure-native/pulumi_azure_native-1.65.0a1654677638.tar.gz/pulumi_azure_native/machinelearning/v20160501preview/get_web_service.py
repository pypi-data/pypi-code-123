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
    'GetWebServiceResult',
    'AwaitableGetWebServiceResult',
    'get_web_service',
    'get_web_service_output',
]

@pulumi.output_type
class GetWebServiceResult:
    """
    Instance of an Azure ML web service resource.
    """
    def __init__(__self__, id=None, location=None, name=None, properties=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Specifies the resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.WebServicePropertiesForGraphResponse':
        """
        Contains the property payload that describes the web service.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetWebServiceResult(GetWebServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebServiceResult(
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            tags=self.tags,
            type=self.type)


def get_web_service(resource_group_name: Optional[str] = None,
                    web_service_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebServiceResult:
    """
    Instance of an Azure ML web service resource.


    :param str resource_group_name: Name of the resource group in which the web service is located.
    :param str web_service_name: The name of the web service.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['webServiceName'] = web_service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearning/v20160501preview:getWebService', __args__, opts=opts, typ=GetWebServiceResult).value

    return AwaitableGetWebServiceResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        properties=__ret__.properties,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_web_service)
def get_web_service_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                           web_service_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebServiceResult]:
    """
    Instance of an Azure ML web service resource.


    :param str resource_group_name: Name of the resource group in which the web service is located.
    :param str web_service_name: The name of the web service.
    """
    ...
