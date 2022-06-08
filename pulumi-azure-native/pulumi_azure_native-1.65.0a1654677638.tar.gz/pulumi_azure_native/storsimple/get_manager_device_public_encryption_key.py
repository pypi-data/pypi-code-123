# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetManagerDevicePublicEncryptionKeyResult',
    'AwaitableGetManagerDevicePublicEncryptionKeyResult',
    'get_manager_device_public_encryption_key',
    'get_manager_device_public_encryption_key_output',
]

@pulumi.output_type
class GetManagerDevicePublicEncryptionKeyResult:
    """
    The public key.
    """
    def __init__(__self__, key=None):
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key.
        """
        return pulumi.get(self, "key")


class AwaitableGetManagerDevicePublicEncryptionKeyResult(GetManagerDevicePublicEncryptionKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagerDevicePublicEncryptionKeyResult(
            key=self.key)


def get_manager_device_public_encryption_key(device_name: Optional[str] = None,
                                             manager_name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagerDevicePublicEncryptionKeyResult:
    """
    The public key.
    API Version: 2017-06-01.


    :param str device_name: The device name
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple:getManagerDevicePublicEncryptionKey', __args__, opts=opts, typ=GetManagerDevicePublicEncryptionKeyResult).value

    return AwaitableGetManagerDevicePublicEncryptionKeyResult(
        key=__ret__.key)


@_utilities.lift_output_func(get_manager_device_public_encryption_key)
def get_manager_device_public_encryption_key_output(device_name: Optional[pulumi.Input[str]] = None,
                                                    manager_name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagerDevicePublicEncryptionKeyResult]:
    """
    The public key.
    API Version: 2017-06-01.


    :param str device_name: The device name
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    ...
