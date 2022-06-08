# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetUserPoolDomainResult',
    'AwaitableGetUserPoolDomainResult',
    'get_user_pool_domain',
    'get_user_pool_domain_output',
]

@pulumi.output_type
class GetUserPoolDomainResult:
    def __init__(__self__, custom_domain_config=None, id=None):
        if custom_domain_config and not isinstance(custom_domain_config, dict):
            raise TypeError("Expected argument 'custom_domain_config' to be a dict")
        pulumi.set(__self__, "custom_domain_config", custom_domain_config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="customDomainConfig")
    def custom_domain_config(self) -> Optional['outputs.UserPoolDomainCustomDomainConfigType']:
        return pulumi.get(self, "custom_domain_config")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetUserPoolDomainResult(GetUserPoolDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolDomainResult(
            custom_domain_config=self.custom_domain_config,
            id=self.id)


def get_user_pool_domain(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPoolDomainResult:
    """
    Resource Type definition for AWS::Cognito::UserPoolDomain
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:cognito:getUserPoolDomain', __args__, opts=opts, typ=GetUserPoolDomainResult).value

    return AwaitableGetUserPoolDomainResult(
        custom_domain_config=__ret__.custom_domain_config,
        id=__ret__.id)


@_utilities.lift_output_func(get_user_pool_domain)
def get_user_pool_domain_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPoolDomainResult]:
    """
    Resource Type definition for AWS::Cognito::UserPoolDomain
    """
    ...
