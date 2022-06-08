# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetLinksResult',
    'AwaitableGetLinksResult',
    'get_links',
    'get_links_output',
]

@pulumi.output_type
class GetLinksResult:
    """
    A collection of values returned by getLinks.
    """
    def __init__(__self__, global_network_id=None, id=None, ids=None, provider_name=None, site_id=None, tags=None, type=None):
        if global_network_id and not isinstance(global_network_id, str):
            raise TypeError("Expected argument 'global_network_id' to be a str")
        pulumi.set(__self__, "global_network_id", global_network_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)
        if site_id and not isinstance(site_id, str):
            raise TypeError("Expected argument 'site_id' to be a str")
        pulumi.set(__self__, "site_id", site_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> str:
        return pulumi.get(self, "global_network_id")

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
        The IDs of the links.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[str]:
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[str]:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


class AwaitableGetLinksResult(GetLinksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLinksResult(
            global_network_id=self.global_network_id,
            id=self.id,
            ids=self.ids,
            provider_name=self.provider_name,
            site_id=self.site_id,
            tags=self.tags,
            type=self.type)


def get_links(global_network_id: Optional[str] = None,
              provider_name: Optional[str] = None,
              site_id: Optional[str] = None,
              tags: Optional[Mapping[str, str]] = None,
              type: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLinksResult:
    """
    Retrieve information about link.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.networkmanager.get_links(global_network_id=var["global_network_id"],
        tags={
            "Env": "test",
        })
    ```


    :param str global_network_id: The ID of the Global Network of the links to retrieve.
    :param str provider_name: The link provider to retrieve.
    :param str site_id: The ID of the site of the links to retrieve.
    :param Mapping[str, str] tags: Restricts the list to the links with these tags.
    :param str type: The link type to retrieve.
    """
    __args__ = dict()
    __args__['globalNetworkId'] = global_network_id
    __args__['providerName'] = provider_name
    __args__['siteId'] = site_id
    __args__['tags'] = tags
    __args__['type'] = type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:networkmanager/getLinks:getLinks', __args__, opts=opts, typ=GetLinksResult).value

    return AwaitableGetLinksResult(
        global_network_id=__ret__.global_network_id,
        id=__ret__.id,
        ids=__ret__.ids,
        provider_name=__ret__.provider_name,
        site_id=__ret__.site_id,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_links)
def get_links_output(global_network_id: Optional[pulumi.Input[str]] = None,
                     provider_name: Optional[pulumi.Input[Optional[str]]] = None,
                     site_id: Optional[pulumi.Input[Optional[str]]] = None,
                     tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                     type: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLinksResult]:
    """
    Retrieve information about link.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.networkmanager.get_links(global_network_id=var["global_network_id"],
        tags={
            "Env": "test",
        })
    ```


    :param str global_network_id: The ID of the Global Network of the links to retrieve.
    :param str provider_name: The link provider to retrieve.
    :param str site_id: The ID of the site of the links to retrieve.
    :param Mapping[str, str] tags: Restricts the list to the links with these tags.
    :param str type: The link type to retrieve.
    """
    ...
