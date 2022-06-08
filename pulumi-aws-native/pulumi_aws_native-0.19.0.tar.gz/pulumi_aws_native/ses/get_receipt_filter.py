# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetReceiptFilterResult',
    'AwaitableGetReceiptFilterResult',
    'get_receipt_filter',
    'get_receipt_filter_output',
]

@pulumi.output_type
class GetReceiptFilterResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetReceiptFilterResult(GetReceiptFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReceiptFilterResult(
            id=self.id)


def get_receipt_filter(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReceiptFilterResult:
    """
    Resource Type definition for AWS::SES::ReceiptFilter
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ses:getReceiptFilter', __args__, opts=opts, typ=GetReceiptFilterResult).value

    return AwaitableGetReceiptFilterResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_receipt_filter)
def get_receipt_filter_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReceiptFilterResult]:
    """
    Resource Type definition for AWS::SES::ReceiptFilter
    """
    ...
