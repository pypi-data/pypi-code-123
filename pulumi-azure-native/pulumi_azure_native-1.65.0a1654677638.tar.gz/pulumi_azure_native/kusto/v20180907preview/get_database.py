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
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    Class representing a Kusto database.
    """
    def __init__(__self__, etag=None, hot_cache_period_in_days=None, id=None, location=None, name=None, provisioning_state=None, soft_delete_period_in_days=None, statistics=None, tags=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if hot_cache_period_in_days and not isinstance(hot_cache_period_in_days, int):
            raise TypeError("Expected argument 'hot_cache_period_in_days' to be a int")
        pulumi.set(__self__, "hot_cache_period_in_days", hot_cache_period_in_days)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if soft_delete_period_in_days and not isinstance(soft_delete_period_in_days, int):
            raise TypeError("Expected argument 'soft_delete_period_in_days' to be a int")
        pulumi.set(__self__, "soft_delete_period_in_days", soft_delete_period_in_days)
        if statistics and not isinstance(statistics, dict):
            raise TypeError("Expected argument 'statistics' to be a dict")
        pulumi.set(__self__, "statistics", statistics)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        An ETag of the resource created.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hotCachePeriodInDays")
    def hot_cache_period_in_days(self) -> Optional[int]:
        """
        The number of days of data that should be kept in cache for fast queries.
        """
        return pulumi.get(self, "hot_cache_period_in_days")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="softDeletePeriodInDays")
    def soft_delete_period_in_days(self) -> int:
        """
        The number of days data should be kept before it stops being accessible to queries.
        """
        return pulumi.get(self, "soft_delete_period_in_days")

    @property
    @pulumi.getter
    def statistics(self) -> 'outputs.DatabaseStatisticsResponse':
        """
        The statistics of the database.
        """
        return pulumi.get(self, "statistics")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            etag=self.etag,
            hot_cache_period_in_days=self.hot_cache_period_in_days,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            soft_delete_period_in_days=self.soft_delete_period_in_days,
            statistics=self.statistics,
            tags=self.tags,
            type=self.type)


def get_database(cluster_name: Optional[str] = None,
                 database_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    Class representing a Kusto database.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20180907preview:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        etag=__ret__.etag,
        hot_cache_period_in_days=__ret__.hot_cache_period_in_days,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        soft_delete_period_in_days=__ret__.soft_delete_period_in_days,
        statistics=__ret__.statistics,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_database)
def get_database_output(cluster_name: Optional[pulumi.Input[str]] = None,
                        database_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    Class representing a Kusto database.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
