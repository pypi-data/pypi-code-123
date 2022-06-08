# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetSshPublicKeyResult',
    'AwaitableGetSshPublicKeyResult',
    'get_ssh_public_key',
    'get_ssh_public_key_output',
]

warnings.warn("""Version v20200601 will be removed in the next major version of the provider. Upgrade to version v20200930 or later.""", DeprecationWarning)

@pulumi.output_type
class GetSshPublicKeyResult:
    """
    Specifies information about the SSH public key.
    """
    def __init__(__self__, id=None, location=None, name=None, public_key=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[str]:
        """
        SSH public key used to authenticate to a virtual machine through ssh. If this property is not initially provided when the resource is created, the publicKey property will be populated when generateKeyPair is called. If the public key is provided upon resource creation, the provided public key needs to be at least 2048-bit and in ssh-rsa format.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetSshPublicKeyResult(GetSshPublicKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshPublicKeyResult(
            id=self.id,
            location=self.location,
            name=self.name,
            public_key=self.public_key,
            tags=self.tags,
            type=self.type)


def get_ssh_public_key(resource_group_name: Optional[str] = None,
                       ssh_public_key_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSshPublicKeyResult:
    """
    Specifies information about the SSH public key.


    :param str resource_group_name: The name of the resource group.
    :param str ssh_public_key_name: The name of the SSH public key.
    """
    pulumi.log.warn("""get_ssh_public_key is deprecated: Version v20200601 will be removed in the next major version of the provider. Upgrade to version v20200930 or later.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sshPublicKeyName'] = ssh_public_key_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20200601:getSshPublicKey', __args__, opts=opts, typ=GetSshPublicKeyResult).value

    return AwaitableGetSshPublicKeyResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        public_key=__ret__.public_key,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_ssh_public_key)
def get_ssh_public_key_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                              ssh_public_key_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSshPublicKeyResult]:
    """
    Specifies information about the SSH public key.


    :param str resource_group_name: The name of the resource group.
    :param str ssh_public_key_name: The name of the SSH public key.
    """
    pulumi.log.warn("""get_ssh_public_key is deprecated: Version v20200601 will be removed in the next major version of the provider. Upgrade to version v20200930 or later.""")
    ...
