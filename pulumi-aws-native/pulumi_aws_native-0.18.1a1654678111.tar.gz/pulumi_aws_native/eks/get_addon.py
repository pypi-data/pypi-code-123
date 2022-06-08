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
    'GetAddonResult',
    'AwaitableGetAddonResult',
    'get_addon',
    'get_addon_output',
]

@pulumi.output_type
class GetAddonResult:
    def __init__(__self__, addon_version=None, arn=None, service_account_role_arn=None, tags=None):
        if addon_version and not isinstance(addon_version, str):
            raise TypeError("Expected argument 'addon_version' to be a str")
        pulumi.set(__self__, "addon_version", addon_version)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if service_account_role_arn and not isinstance(service_account_role_arn, str):
            raise TypeError("Expected argument 'service_account_role_arn' to be a str")
        pulumi.set(__self__, "service_account_role_arn", service_account_role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> Optional[str]:
        """
        Version of Addon
        """
        return pulumi.get(self, "addon_version")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the add-on
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> Optional[str]:
        """
        IAM role to bind to the add-on's service account
        """
        return pulumi.get(self, "service_account_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.AddonTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetAddonResult(GetAddonResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddonResult(
            addon_version=self.addon_version,
            arn=self.arn,
            service_account_role_arn=self.service_account_role_arn,
            tags=self.tags)


def get_addon(addon_name: Optional[str] = None,
              cluster_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddonResult:
    """
    Resource Schema for AWS::EKS::Addon


    :param str addon_name: Name of Addon
    :param str cluster_name: Name of Cluster
    """
    __args__ = dict()
    __args__['addonName'] = addon_name
    __args__['clusterName'] = cluster_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:eks:getAddon', __args__, opts=opts, typ=GetAddonResult).value

    return AwaitableGetAddonResult(
        addon_version=__ret__.addon_version,
        arn=__ret__.arn,
        service_account_role_arn=__ret__.service_account_role_arn,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_addon)
def get_addon_output(addon_name: Optional[pulumi.Input[str]] = None,
                     cluster_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddonResult]:
    """
    Resource Schema for AWS::EKS::Addon


    :param str addon_name: Name of Addon
    :param str cluster_name: Name of Cluster
    """
    ...
