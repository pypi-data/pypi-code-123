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
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    def __init__(__self__, domain_id=None, tags=None):
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[str]:
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DomainTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            domain_id=self.domain_id,
            tags=self.tags)


def get_domain(domain_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    The AWS::VoiceID::Domain resource specifies an Amazon VoiceID Domain.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:voiceid:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        domain_id=__ret__.domain_id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_domain)
def get_domain_output(domain_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    The AWS::VoiceID::Domain resource specifies an Amazon VoiceID Domain.
    """
    ...
