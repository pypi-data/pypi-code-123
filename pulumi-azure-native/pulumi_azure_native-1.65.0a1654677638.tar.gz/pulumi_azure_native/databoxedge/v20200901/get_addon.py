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
    'GetAddonResult',
    'AwaitableGetAddonResult',
    'get_addon',
    'get_addon_output',
]

warnings.warn("""Version v20200901 will be removed in the next major version of the provider. Upgrade to version v20201201 or later.""", DeprecationWarning)

@pulumi.output_type
class GetAddonResult:
    """
    Role Addon
    """
    def __init__(__self__, id=None, kind=None, name=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Addon type.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Addon type
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetAddonResult(GetAddonResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddonResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_addon(addon_name: Optional[str] = None,
              device_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              role_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddonResult:
    """
    Role Addon


    :param str addon_name: The addon name.
    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str role_name: The role name.
    """
    pulumi.log.warn("""get_addon is deprecated: Version v20200901 will be removed in the next major version of the provider. Upgrade to version v20201201 or later.""")
    __args__ = dict()
    __args__['addonName'] = addon_name
    __args__['deviceName'] = device_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['roleName'] = role_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20200901:getAddon', __args__, opts=opts, typ=GetAddonResult).value

    return AwaitableGetAddonResult(
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_addon)
def get_addon_output(addon_name: Optional[pulumi.Input[str]] = None,
                     device_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     role_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddonResult]:
    """
    Role Addon


    :param str addon_name: The addon name.
    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str role_name: The role name.
    """
    pulumi.log.warn("""get_addon is deprecated: Version v20200901 will be removed in the next major version of the provider. Upgrade to version v20201201 or later.""")
    ...
