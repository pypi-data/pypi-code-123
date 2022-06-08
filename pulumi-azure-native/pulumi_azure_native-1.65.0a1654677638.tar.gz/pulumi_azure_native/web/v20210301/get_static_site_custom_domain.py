# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetStaticSiteCustomDomainResult',
    'AwaitableGetStaticSiteCustomDomainResult',
    'get_static_site_custom_domain',
    'get_static_site_custom_domain_output',
]

@pulumi.output_type
class GetStaticSiteCustomDomainResult:
    """
    Static Site Custom Domain Overview ARM resource.
    """
    def __init__(__self__, created_on=None, domain_name=None, error_message=None, id=None, kind=None, name=None, status=None, type=None, validation_token=None):
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if validation_token and not isinstance(validation_token, str):
            raise TypeError("Expected argument 'validation_token' to be a str")
        pulumi.set(__self__, "validation_token", validation_token)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        """
        The date and time on which the custom domain was created for the static site.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        """
        The domain name for the static site custom domain.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the custom domain
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationToken")
    def validation_token(self) -> str:
        """
        The TXT record validation token
        """
        return pulumi.get(self, "validation_token")


class AwaitableGetStaticSiteCustomDomainResult(GetStaticSiteCustomDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticSiteCustomDomainResult(
            created_on=self.created_on,
            domain_name=self.domain_name,
            error_message=self.error_message,
            id=self.id,
            kind=self.kind,
            name=self.name,
            status=self.status,
            type=self.type,
            validation_token=self.validation_token)


def get_static_site_custom_domain(domain_name: Optional[str] = None,
                                  name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticSiteCustomDomainResult:
    """
    Static Site Custom Domain Overview ARM resource.


    :param str domain_name: The custom domain name.
    :param str name: Name of the static site resource to search in.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20210301:getStaticSiteCustomDomain', __args__, opts=opts, typ=GetStaticSiteCustomDomainResult).value

    return AwaitableGetStaticSiteCustomDomainResult(
        created_on=__ret__.created_on,
        domain_name=__ret__.domain_name,
        error_message=__ret__.error_message,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        status=__ret__.status,
        type=__ret__.type,
        validation_token=__ret__.validation_token)


@_utilities.lift_output_func(get_static_site_custom_domain)
def get_static_site_custom_domain_output(domain_name: Optional[pulumi.Input[str]] = None,
                                         name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStaticSiteCustomDomainResult]:
    """
    Static Site Custom Domain Overview ARM resource.


    :param str domain_name: The custom domain name.
    :param str name: Name of the static site resource to search in.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
