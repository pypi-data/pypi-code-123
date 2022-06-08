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
    'GetManagedEnvironmentsStorageResult',
    'AwaitableGetManagedEnvironmentsStorageResult',
    'get_managed_environments_storage',
    'get_managed_environments_storage_output',
]

@pulumi.output_type
class GetManagedEnvironmentsStorageResult:
    """
    Storage resource for managedEnvironment.
    """
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
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
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ManagedEnvironmentStorageResponseProperties':
        """
        Storage properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedEnvironmentsStorageResult(GetManagedEnvironmentsStorageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedEnvironmentsStorageResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_managed_environments_storage(environment_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     storage_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedEnvironmentsStorageResult:
    """
    Storage resource for managedEnvironment.
    API Version: 2022-03-01.


    :param str environment_name: Name of the Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_name: Name of the storage.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageName'] = storage_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:app:getManagedEnvironmentsStorage', __args__, opts=opts, typ=GetManagedEnvironmentsStorageResult).value

    return AwaitableGetManagedEnvironmentsStorageResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_managed_environments_storage)
def get_managed_environments_storage_output(environment_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            storage_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedEnvironmentsStorageResult]:
    """
    Storage resource for managedEnvironment.
    API Version: 2022-03-01.


    :param str environment_name: Name of the Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_name: Name of the storage.
    """
    ...
