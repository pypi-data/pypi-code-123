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
    'GetFileServicePropertiesResult',
    'AwaitableGetFileServicePropertiesResult',
    'get_file_service_properties',
    'get_file_service_properties_output',
]

warnings.warn("""Version v20190401 will be removed in the next major version of the provider. Upgrade to version v20210201 or later.""", DeprecationWarning)

@pulumi.output_type
class GetFileServicePropertiesResult:
    """
    The properties of File services in storage account.
    """
    def __init__(__self__, cors=None, id=None, name=None, type=None):
        if cors and not isinstance(cors, dict):
            raise TypeError("Expected argument 'cors' to be a dict")
        pulumi.set(__self__, "cors", cors)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cors(self) -> Optional['outputs.CorsRulesResponse']:
        """
        Specifies CORS rules for the File service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the File service.
        """
        return pulumi.get(self, "cors")

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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetFileServicePropertiesResult(GetFileServicePropertiesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileServicePropertiesResult(
            cors=self.cors,
            id=self.id,
            name=self.name,
            type=self.type)


def get_file_service_properties(account_name: Optional[str] = None,
                                file_services_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileServicePropertiesResult:
    """
    The properties of File services in storage account.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str file_services_name: The name of the file Service within the specified storage account. File Service Name must be "default"
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    pulumi.log.warn("""get_file_service_properties is deprecated: Version v20190401 will be removed in the next major version of the provider. Upgrade to version v20210201 or later.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['fileServicesName'] = file_services_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storage/v20190401:getFileServiceProperties', __args__, opts=opts, typ=GetFileServicePropertiesResult).value

    return AwaitableGetFileServicePropertiesResult(
        cors=__ret__.cors,
        id=__ret__.id,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_file_service_properties)
def get_file_service_properties_output(account_name: Optional[pulumi.Input[str]] = None,
                                       file_services_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFileServicePropertiesResult]:
    """
    The properties of File services in storage account.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str file_services_name: The name of the file Service within the specified storage account. File Service Name must be "default"
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    pulumi.log.warn("""get_file_service_properties is deprecated: Version v20190401 will be removed in the next major version of the provider. Upgrade to version v20210201 or later.""")
    ...
