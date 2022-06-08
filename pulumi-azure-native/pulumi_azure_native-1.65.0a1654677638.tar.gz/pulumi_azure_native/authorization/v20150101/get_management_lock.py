# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetManagementLockResult',
    'AwaitableGetManagementLockResult',
    'get_management_lock',
    'get_management_lock_output',
]

warnings.warn("""Version v20150101 will be removed in the next major version of the provider. Upgrade to version v20170401 or later.""", DeprecationWarning)

@pulumi.output_type
class GetManagementLockResult:
    """
    Management lock information.
    """
    def __init__(__self__, id=None, level=None, name=None, notes=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if level and not isinstance(level, str):
            raise TypeError("Expected argument 'level' to be a str")
        pulumi.set(__self__, "level", level)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Id of the lock.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def level(self) -> Optional[str]:
        """
        The lock level of the management lock.
        """
        return pulumi.get(self, "level")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the lock.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        The notes of the management lock.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the lock.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagementLockResult(GetManagementLockResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementLockResult(
            id=self.id,
            level=self.level,
            name=self.name,
            notes=self.notes,
            type=self.type)


def get_management_lock(lock_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementLockResult:
    """
    Management lock information.


    :param str lock_name: Name of the management lock.
    """
    pulumi.log.warn("""get_management_lock is deprecated: Version v20150101 will be removed in the next major version of the provider. Upgrade to version v20170401 or later.""")
    __args__ = dict()
    __args__['lockName'] = lock_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20150101:getManagementLock', __args__, opts=opts, typ=GetManagementLockResult).value

    return AwaitableGetManagementLockResult(
        id=__ret__.id,
        level=__ret__.level,
        name=__ret__.name,
        notes=__ret__.notes,
        type=__ret__.type)


@_utilities.lift_output_func(get_management_lock)
def get_management_lock_output(lock_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagementLockResult]:
    """
    Management lock information.


    :param str lock_name: Name of the management lock.
    """
    pulumi.log.warn("""get_management_lock is deprecated: Version v20150101 will be removed in the next major version of the provider. Upgrade to version v20170401 or later.""")
    ...
