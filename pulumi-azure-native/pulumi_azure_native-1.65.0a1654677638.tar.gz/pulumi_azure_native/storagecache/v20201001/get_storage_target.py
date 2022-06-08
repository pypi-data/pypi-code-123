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
    'GetStorageTargetResult',
    'AwaitableGetStorageTargetResult',
    'get_storage_target',
    'get_storage_target_output',
]

warnings.warn("""Version v20201001 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""", DeprecationWarning)

@pulumi.output_type
class GetStorageTargetResult:
    """
    Type of the Storage Target.
    """
    def __init__(__self__, clfs=None, id=None, junctions=None, location=None, name=None, nfs3=None, provisioning_state=None, system_data=None, target_type=None, type=None, unknown=None):
        if clfs and not isinstance(clfs, dict):
            raise TypeError("Expected argument 'clfs' to be a dict")
        pulumi.set(__self__, "clfs", clfs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if junctions and not isinstance(junctions, list):
            raise TypeError("Expected argument 'junctions' to be a list")
        pulumi.set(__self__, "junctions", junctions)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nfs3 and not isinstance(nfs3, dict):
            raise TypeError("Expected argument 'nfs3' to be a dict")
        pulumi.set(__self__, "nfs3", nfs3)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if target_type and not isinstance(target_type, str):
            raise TypeError("Expected argument 'target_type' to be a str")
        pulumi.set(__self__, "target_type", target_type)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unknown and not isinstance(unknown, dict):
            raise TypeError("Expected argument 'unknown' to be a dict")
        pulumi.set(__self__, "unknown", unknown)

    @property
    @pulumi.getter
    def clfs(self) -> Optional['outputs.ClfsTargetResponse']:
        """
        Properties when targetType is clfs.
        """
        return pulumi.get(self, "clfs")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID of the Storage Target.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def junctions(self) -> Optional[Sequence['outputs.NamespaceJunctionResponse']]:
        """
        List of Cache namespace junctions to target for namespace associations.
        """
        return pulumi.get(self, "junctions")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Region name string.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Storage Target.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nfs3(self) -> Optional['outputs.Nfs3TargetResponse']:
        """
        Properties when targetType is nfs3.
        """
        return pulumi.get(self, "nfs3")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> str:
        """
        Type of the Storage Target.
        """
        return pulumi.get(self, "target_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the Storage Target; Microsoft.StorageCache/Cache/StorageTarget
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def unknown(self) -> Optional['outputs.UnknownTargetResponse']:
        """
        Properties when targetType is unknown.
        """
        return pulumi.get(self, "unknown")


class AwaitableGetStorageTargetResult(GetStorageTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageTargetResult(
            clfs=self.clfs,
            id=self.id,
            junctions=self.junctions,
            location=self.location,
            name=self.name,
            nfs3=self.nfs3,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            target_type=self.target_type,
            type=self.type,
            unknown=self.unknown)


def get_storage_target(cache_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       storage_target_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageTargetResult:
    """
    Type of the Storage Target.


    :param str cache_name: Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.
    :param str resource_group_name: Target resource group.
    :param str storage_target_name: Name of the Storage Target. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.
    """
    pulumi.log.warn("""get_storage_target is deprecated: Version v20201001 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""")
    __args__ = dict()
    __args__['cacheName'] = cache_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageTargetName'] = storage_target_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storagecache/v20201001:getStorageTarget', __args__, opts=opts, typ=GetStorageTargetResult).value

    return AwaitableGetStorageTargetResult(
        clfs=__ret__.clfs,
        id=__ret__.id,
        junctions=__ret__.junctions,
        location=__ret__.location,
        name=__ret__.name,
        nfs3=__ret__.nfs3,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        target_type=__ret__.target_type,
        type=__ret__.type,
        unknown=__ret__.unknown)


@_utilities.lift_output_func(get_storage_target)
def get_storage_target_output(cache_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              storage_target_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageTargetResult]:
    """
    Type of the Storage Target.


    :param str cache_name: Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.
    :param str resource_group_name: Target resource group.
    :param str storage_target_name: Name of the Storage Target. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.
    """
    pulumi.log.warn("""get_storage_target is deprecated: Version v20201001 will be removed in the next major version of the provider. Upgrade to version v20210301 or later.""")
    ...
