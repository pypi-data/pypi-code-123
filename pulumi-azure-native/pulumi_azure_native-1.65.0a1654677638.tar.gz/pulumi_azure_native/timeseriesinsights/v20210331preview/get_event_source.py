# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetEventSourceResult',
    'AwaitableGetEventSourceResult',
    'get_event_source',
    'get_event_source_output',
]

warnings.warn("""Please use one of the variants: EventHubEventSource, IoTHubEventSource.""", DeprecationWarning)

@pulumi.output_type
class GetEventSourceResult:
    """
    An environment receives data from one or more event sources. Each event source has associated connection info that allows the Time Series Insights ingress pipeline to connect to and pull data from the event source
    """
    def __init__(__self__, id=None, kind=None, location=None, name=None, tags=None, type=None):
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
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the event source.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetEventSourceResult(GetEventSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventSourceResult(
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            tags=self.tags,
            type=self.type)


def get_event_source(environment_name: Optional[str] = None,
                     event_source_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventSourceResult:
    """
    An environment receives data from one or more event sources. Each event source has associated connection info that allows the Time Series Insights ingress pipeline to connect to and pull data from the event source


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    pulumi.log.warn("""get_event_source is deprecated: Please use one of the variants: EventHubEventSource, IoTHubEventSource.""")
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['eventSourceName'] = event_source_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:timeseriesinsights/v20210331preview:getEventSource', __args__, opts=opts, typ=GetEventSourceResult).value

    return AwaitableGetEventSourceResult(
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_event_source)
def get_event_source_output(environment_name: Optional[pulumi.Input[str]] = None,
                            event_source_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventSourceResult]:
    """
    An environment receives data from one or more event sources. Each event source has associated connection info that allows the Time Series Insights ingress pipeline to connect to and pull data from the event source


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    pulumi.log.warn("""get_event_source is deprecated: Please use one of the variants: EventHubEventSource, IoTHubEventSource.""")
    ...
