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
    'GetBatchAccountResult',
    'AwaitableGetBatchAccountResult',
    'get_batch_account',
    'get_batch_account_output',
]

warnings.warn("""Version v20151201 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""", DeprecationWarning)

@pulumi.output_type
class GetBatchAccountResult:
    """
    Contains information about an Azure Batch account.
    """
    def __init__(__self__, account_endpoint=None, active_job_and_job_schedule_quota=None, auto_storage=None, core_quota=None, id=None, location=None, name=None, pool_quota=None, provisioning_state=None, tags=None, type=None):
        if account_endpoint and not isinstance(account_endpoint, str):
            raise TypeError("Expected argument 'account_endpoint' to be a str")
        pulumi.set(__self__, "account_endpoint", account_endpoint)
        if active_job_and_job_schedule_quota and not isinstance(active_job_and_job_schedule_quota, int):
            raise TypeError("Expected argument 'active_job_and_job_schedule_quota' to be a int")
        pulumi.set(__self__, "active_job_and_job_schedule_quota", active_job_and_job_schedule_quota)
        if auto_storage and not isinstance(auto_storage, dict):
            raise TypeError("Expected argument 'auto_storage' to be a dict")
        pulumi.set(__self__, "auto_storage", auto_storage)
        if core_quota and not isinstance(core_quota, int):
            raise TypeError("Expected argument 'core_quota' to be a int")
        pulumi.set(__self__, "core_quota", core_quota)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pool_quota and not isinstance(pool_quota, int):
            raise TypeError("Expected argument 'pool_quota' to be a int")
        pulumi.set(__self__, "pool_quota", pool_quota)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountEndpoint")
    def account_endpoint(self) -> str:
        """
        The endpoint used by this account to interact with the Batch services.
        """
        return pulumi.get(self, "account_endpoint")

    @property
    @pulumi.getter(name="activeJobAndJobScheduleQuota")
    def active_job_and_job_schedule_quota(self) -> int:
        """
        The active job and job schedule quota for this Batch account.
        """
        return pulumi.get(self, "active_job_and_job_schedule_quota")

    @property
    @pulumi.getter(name="autoStorage")
    def auto_storage(self) -> Optional['outputs.AutoStoragePropertiesResponse']:
        """
        The properties and status of any auto storage account associated with the account.
        """
        return pulumi.get(self, "auto_storage")

    @property
    @pulumi.getter(name="coreQuota")
    def core_quota(self) -> int:
        """
        The core quota for this Batch account.
        """
        return pulumi.get(self, "core_quota")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="poolQuota")
    def pool_quota(self) -> int:
        """
        The pool quota for this Batch account.
        """
        return pulumi.get(self, "pool_quota")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioned state of the resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource
        """
        return pulumi.get(self, "type")


class AwaitableGetBatchAccountResult(GetBatchAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBatchAccountResult(
            account_endpoint=self.account_endpoint,
            active_job_and_job_schedule_quota=self.active_job_and_job_schedule_quota,
            auto_storage=self.auto_storage,
            core_quota=self.core_quota,
            id=self.id,
            location=self.location,
            name=self.name,
            pool_quota=self.pool_quota,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type)


def get_batch_account(account_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBatchAccountResult:
    """
    Contains information about an Azure Batch account.


    :param str account_name: The name of the account.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    """
    pulumi.log.warn("""get_batch_account is deprecated: Version v20151201 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:batch/v20151201:getBatchAccount', __args__, opts=opts, typ=GetBatchAccountResult).value

    return AwaitableGetBatchAccountResult(
        account_endpoint=__ret__.account_endpoint,
        active_job_and_job_schedule_quota=__ret__.active_job_and_job_schedule_quota,
        auto_storage=__ret__.auto_storage,
        core_quota=__ret__.core_quota,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        pool_quota=__ret__.pool_quota,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_batch_account)
def get_batch_account_output(account_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBatchAccountResult]:
    """
    Contains information about an Azure Batch account.


    :param str account_name: The name of the account.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    """
    pulumi.log.warn("""get_batch_account is deprecated: Version v20151201 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""")
    ...
