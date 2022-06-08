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
    'GetEndpointResult',
    'AwaitableGetEndpointResult',
    'get_endpoint',
    'get_endpoint_output',
]

warnings.warn("""Version v20160402 will be removed in the next major version of the provider. Upgrade to version v20200901 or later.""", DeprecationWarning)

@pulumi.output_type
class GetEndpointResult:
    """
    CDN endpoint is the entity within a CDN profile containing configuration information regarding caching behaviors and origins. The CDN endpoint is exposed using the URL format <endpointname>.azureedge.net by default, but custom domains can also be created.
    """
    def __init__(__self__, content_types_to_compress=None, host_name=None, id=None, is_compression_enabled=None, is_http_allowed=None, is_https_allowed=None, location=None, name=None, origin_host_header=None, origin_path=None, origins=None, provisioning_state=None, query_string_caching_behavior=None, resource_state=None, tags=None, type=None):
        if content_types_to_compress and not isinstance(content_types_to_compress, list):
            raise TypeError("Expected argument 'content_types_to_compress' to be a list")
        pulumi.set(__self__, "content_types_to_compress", content_types_to_compress)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_compression_enabled and not isinstance(is_compression_enabled, bool):
            raise TypeError("Expected argument 'is_compression_enabled' to be a bool")
        pulumi.set(__self__, "is_compression_enabled", is_compression_enabled)
        if is_http_allowed and not isinstance(is_http_allowed, bool):
            raise TypeError("Expected argument 'is_http_allowed' to be a bool")
        pulumi.set(__self__, "is_http_allowed", is_http_allowed)
        if is_https_allowed and not isinstance(is_https_allowed, bool):
            raise TypeError("Expected argument 'is_https_allowed' to be a bool")
        pulumi.set(__self__, "is_https_allowed", is_https_allowed)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origin_host_header and not isinstance(origin_host_header, str):
            raise TypeError("Expected argument 'origin_host_header' to be a str")
        pulumi.set(__self__, "origin_host_header", origin_host_header)
        if origin_path and not isinstance(origin_path, str):
            raise TypeError("Expected argument 'origin_path' to be a str")
        pulumi.set(__self__, "origin_path", origin_path)
        if origins and not isinstance(origins, list):
            raise TypeError("Expected argument 'origins' to be a list")
        pulumi.set(__self__, "origins", origins)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if query_string_caching_behavior and not isinstance(query_string_caching_behavior, str):
            raise TypeError("Expected argument 'query_string_caching_behavior' to be a str")
        pulumi.set(__self__, "query_string_caching_behavior", query_string_caching_behavior)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="contentTypesToCompress")
    def content_types_to_compress(self) -> Optional[Sequence[str]]:
        """
        List of content types on which compression will be applied. The value for the elements should be a valid MIME type.
        """
        return pulumi.get(self, "content_types_to_compress")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        The host name of the endpoint {endpointName}.{DNSZone}
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[bool]:
        """
        Indicates whether the compression is enabled. Default value is false. If compression is enabled, the content transferred from cdn endpoint to end user will be compressed. The requested content must be larger than 1 byte and smaller than 1 MB.
        """
        return pulumi.get(self, "is_compression_enabled")

    @property
    @pulumi.getter(name="isHttpAllowed")
    def is_http_allowed(self) -> Optional[bool]:
        """
        Indicates whether HTTP traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed.
        """
        return pulumi.get(self, "is_http_allowed")

    @property
    @pulumi.getter(name="isHttpsAllowed")
    def is_https_allowed(self) -> Optional[bool]:
        """
        Indicates whether https traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed.
        """
        return pulumi.get(self, "is_https_allowed")

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
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[str]:
        """
        The host header the CDN provider will send along with content requests to origins. The default value is the host name of the origin.
        """
        return pulumi.get(self, "origin_host_header")

    @property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[str]:
        """
        The path used for origin requests.
        """
        return pulumi.get(self, "origin_path")

    @property
    @pulumi.getter
    def origins(self) -> Optional[Sequence['outputs.DeepCreatedOriginResponse']]:
        """
        The set of origins for the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options.
        """
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning status of the endpoint.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> Optional[str]:
        """
        Defines the query string caching behavior.
        """
        return pulumi.get(self, "query_string_caching_behavior")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Resource status of the endpoint.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetEndpointResult(GetEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEndpointResult(
            content_types_to_compress=self.content_types_to_compress,
            host_name=self.host_name,
            id=self.id,
            is_compression_enabled=self.is_compression_enabled,
            is_http_allowed=self.is_http_allowed,
            is_https_allowed=self.is_https_allowed,
            location=self.location,
            name=self.name,
            origin_host_header=self.origin_host_header,
            origin_path=self.origin_path,
            origins=self.origins,
            provisioning_state=self.provisioning_state,
            query_string_caching_behavior=self.query_string_caching_behavior,
            resource_state=self.resource_state,
            tags=self.tags,
            type=self.type)


def get_endpoint(endpoint_name: Optional[str] = None,
                 profile_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEndpointResult:
    """
    CDN endpoint is the entity within a CDN profile containing configuration information regarding caching behaviors and origins. The CDN endpoint is exposed using the URL format <endpointname>.azureedge.net by default, but custom domains can also be created.


    :param str endpoint_name: Name of the endpoint within the CDN profile.
    :param str profile_name: Name of the CDN profile within the resource group.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    pulumi.log.warn("""get_endpoint is deprecated: Version v20160402 will be removed in the next major version of the provider. Upgrade to version v20200901 or later.""")
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:cdn/v20160402:getEndpoint', __args__, opts=opts, typ=GetEndpointResult).value

    return AwaitableGetEndpointResult(
        content_types_to_compress=__ret__.content_types_to_compress,
        host_name=__ret__.host_name,
        id=__ret__.id,
        is_compression_enabled=__ret__.is_compression_enabled,
        is_http_allowed=__ret__.is_http_allowed,
        is_https_allowed=__ret__.is_https_allowed,
        location=__ret__.location,
        name=__ret__.name,
        origin_host_header=__ret__.origin_host_header,
        origin_path=__ret__.origin_path,
        origins=__ret__.origins,
        provisioning_state=__ret__.provisioning_state,
        query_string_caching_behavior=__ret__.query_string_caching_behavior,
        resource_state=__ret__.resource_state,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_endpoint)
def get_endpoint_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                        profile_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEndpointResult]:
    """
    CDN endpoint is the entity within a CDN profile containing configuration information regarding caching behaviors and origins. The CDN endpoint is exposed using the URL format <endpointname>.azureedge.net by default, but custom domains can also be created.


    :param str endpoint_name: Name of the endpoint within the CDN profile.
    :param str profile_name: Name of the CDN profile within the resource group.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    pulumi.log.warn("""get_endpoint is deprecated: Version v20160402 will be removed in the next major version of the provider. Upgrade to version v20200901 or later.""")
    ...
