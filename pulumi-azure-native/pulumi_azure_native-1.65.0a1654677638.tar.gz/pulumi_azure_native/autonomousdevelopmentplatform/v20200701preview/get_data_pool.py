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
    'GetDataPoolResult',
    'AwaitableGetDataPoolResult',
    'get_data_pool',
    'get_data_pool_output',
]

warnings.warn("""Version v20200701preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""", DeprecationWarning)

@pulumi.output_type
class GetDataPoolResult:
    """
    An ADP Data Pool.
    """
    def __init__(__self__, data_pool_id=None, id=None, locations=None, name=None, provisioning_state=None, system_data=None, type=None):
        if data_pool_id and not isinstance(data_pool_id, str):
            raise TypeError("Expected argument 'data_pool_id' to be a str")
        pulumi.set(__self__, "data_pool_id", data_pool_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if locations and not isinstance(locations, list):
            raise TypeError("Expected argument 'locations' to be a list")
        pulumi.set(__self__, "locations", locations)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataPoolId")
    def data_pool_id(self) -> str:
        """
        The Data Pool's data-plane ID
        """
        return pulumi.get(self, "data_pool_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def locations(self) -> Sequence['outputs.DataPoolLocationResponse']:
        """
        Gets or sets the collection of locations where Data Pool resources should be created.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the status of the data pool at the time the operation was called.
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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDataPoolResult(GetDataPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataPoolResult(
            data_pool_id=self.data_pool_id,
            id=self.id,
            locations=self.locations,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_data_pool(account_name: Optional[str] = None,
                  data_pool_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataPoolResult:
    """
    An ADP Data Pool.


    :param str account_name: The name of the ADP account.
    :param str data_pool_name: The name of the Data Pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    pulumi.log.warn("""get_data_pool is deprecated: Version v20200701preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataPoolName'] = data_pool_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:autonomousdevelopmentplatform/v20200701preview:getDataPool', __args__, opts=opts, typ=GetDataPoolResult).value

    return AwaitableGetDataPoolResult(
        data_pool_id=__ret__.data_pool_id,
        id=__ret__.id,
        locations=__ret__.locations,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_data_pool)
def get_data_pool_output(account_name: Optional[pulumi.Input[str]] = None,
                         data_pool_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataPoolResult]:
    """
    An ADP Data Pool.


    :param str account_name: The name of the ADP account.
    :param str data_pool_name: The name of the Data Pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    pulumi.log.warn("""get_data_pool is deprecated: Version v20200701preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""")
    ...
