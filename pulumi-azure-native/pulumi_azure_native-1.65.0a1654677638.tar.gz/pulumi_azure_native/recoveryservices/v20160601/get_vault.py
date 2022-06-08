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
    'GetVaultResult',
    'AwaitableGetVaultResult',
    'get_vault',
    'get_vault_output',
]

warnings.warn("""Version v20160601 will be removed in the next major version of the provider. Upgrade to version v20180710 or later.""", DeprecationWarning)

@pulumi.output_type
class GetVaultResult:
    """
    Resource information, as returned by the resource provider.
    """
    def __init__(__self__, e_tag=None, id=None, identity=None, location=None, name=None, properties=None, sku=None, tags=None, type=None):
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        Optional ETag.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id represents the complete path to the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityDataResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name associated with the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.VaultPropertiesResponse':
        """
        Properties of the vault.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        Identifies the unique system identifier for each Azure resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/...
        """
        return pulumi.get(self, "type")


class AwaitableGetVaultResult(GetVaultResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVaultResult(
            e_tag=self.e_tag,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            properties=self.properties,
            sku=self.sku,
            tags=self.tags,
            type=self.type)


def get_vault(resource_group_name: Optional[str] = None,
              vault_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVaultResult:
    """
    Resource information, as returned by the resource provider.


    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param str vault_name: The name of the recovery services vault.
    """
    pulumi.log.warn("""get_vault is deprecated: Version v20160601 will be removed in the next major version of the provider. Upgrade to version v20180710 or later.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['vaultName'] = vault_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:recoveryservices/v20160601:getVault', __args__, opts=opts, typ=GetVaultResult).value

    return AwaitableGetVaultResult(
        e_tag=__ret__.e_tag,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        properties=__ret__.properties,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_vault)
def get_vault_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                     vault_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVaultResult]:
    """
    Resource information, as returned by the resource provider.


    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param str vault_name: The name of the recovery services vault.
    """
    pulumi.log.warn("""get_vault is deprecated: Version v20160601 will be removed in the next major version of the provider. Upgrade to version v20180710 or later.""")
    ...
