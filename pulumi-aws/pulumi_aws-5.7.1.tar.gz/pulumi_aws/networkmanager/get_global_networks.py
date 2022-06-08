# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGlobalNetworksResult',
    'AwaitableGetGlobalNetworksResult',
    'get_global_networks',
    'get_global_networks_output',
]

@pulumi.output_type
class GetGlobalNetworksResult:
    """
    A collection of values returned by getGlobalNetworks.
    """
    def __init__(__self__, id=None, ids=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        The IDs of the global networks.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")


class AwaitableGetGlobalNetworksResult(GetGlobalNetworksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGlobalNetworksResult(
            id=self.id,
            ids=self.ids,
            tags=self.tags)


def get_global_networks(tags: Optional[Mapping[str, str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGlobalNetworksResult:
    """
    Retrieve information about global networks.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.networkmanager.get_global_networks(tags={
        "Env": "test",
    })
    ```


    :param Mapping[str, str] tags: Restricts the list to the global networks with these tags.
    """
    __args__ = dict()
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:networkmanager/getGlobalNetworks:getGlobalNetworks', __args__, opts=opts, typ=GetGlobalNetworksResult).value

    return AwaitableGetGlobalNetworksResult(
        id=__ret__.id,
        ids=__ret__.ids,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_global_networks)
def get_global_networks_output(tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGlobalNetworksResult]:
    """
    Retrieve information about global networks.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.networkmanager.get_global_networks(tags={
        "Env": "test",
    })
    ```


    :param Mapping[str, str] tags: Restricts the list to the global networks with these tags.
    """
    ...
