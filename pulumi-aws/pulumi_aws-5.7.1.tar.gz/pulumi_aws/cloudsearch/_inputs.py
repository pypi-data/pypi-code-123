# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DomainEndpointOptionsArgs',
    'DomainIndexFieldArgs',
    'DomainScalingParametersArgs',
]

@pulumi.input_type
class DomainEndpointOptionsArgs:
    def __init__(__self__, *,
                 enforce_https: Optional[pulumi.Input[bool]] = None,
                 tls_security_policy: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enforce_https: Enables or disables the requirement that all requests to the domain arrive over HTTPS.
        :param pulumi.Input[str] tls_security_policy: The minimum required TLS version. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainEndpointOptions.html) for valid values.
        """
        if enforce_https is not None:
            pulumi.set(__self__, "enforce_https", enforce_https)
        if tls_security_policy is not None:
            pulumi.set(__self__, "tls_security_policy", tls_security_policy)

    @property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables or disables the requirement that all requests to the domain arrive over HTTPS.
        """
        return pulumi.get(self, "enforce_https")

    @enforce_https.setter
    def enforce_https(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enforce_https", value)

    @property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The minimum required TLS version. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainEndpointOptions.html) for valid values.
        """
        return pulumi.get(self, "tls_security_policy")

    @tls_security_policy.setter
    def tls_security_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_security_policy", value)


@pulumi.input_type
class DomainIndexFieldArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 analysis_scheme: Optional[pulumi.Input[str]] = None,
                 default_value: Optional[pulumi.Input[str]] = None,
                 facet: Optional[pulumi.Input[bool]] = None,
                 highlight: Optional[pulumi.Input[bool]] = None,
                 return_: Optional[pulumi.Input[bool]] = None,
                 search: Optional[pulumi.Input[bool]] = None,
                 sort: Optional[pulumi.Input[bool]] = None,
                 source_fields: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: A unique name for the field. Field names must begin with a letter and be at least 3 and no more than 64 characters long. The allowed characters are: `a`-`z` (lower-case letters), `0`-`9`, and `_` (underscore). The name `score` is reserved and cannot be used as a field name.
        :param pulumi.Input[str] type: The field type. Valid values: `date`, `date-array`, `double`, `double-array`, `int`, `int-array`, `literal`, `literal-array`, `text`, `text-array`.
        :param pulumi.Input[str] analysis_scheme: The analysis scheme you want to use for a `text` field. The analysis scheme specifies the language-specific text processing options that are used during indexing.
        :param pulumi.Input[str] default_value: The default value for the field. This value is used when no value is specified for the field in the document data.
        :param pulumi.Input[bool] facet: You can get facet information by enabling this.
        :param pulumi.Input[bool] highlight: You can highlight information.
        :param pulumi.Input[bool] return_: You can enable returning the value of all searchable fields.
        :param pulumi.Input[bool] search: You can set whether this index should be searchable or not.
        :param pulumi.Input[bool] sort: You can enable the property to be sortable.
        :param pulumi.Input[str] source_fields: A comma-separated list of source fields to map to the field. Specifying a source field copies data from one field to another, enabling you to use the same source data in different ways by configuring different options for the fields.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if analysis_scheme is not None:
            pulumi.set(__self__, "analysis_scheme", analysis_scheme)
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if facet is not None:
            pulumi.set(__self__, "facet", facet)
        if highlight is not None:
            pulumi.set(__self__, "highlight", highlight)
        if return_ is not None:
            pulumi.set(__self__, "return_", return_)
        if search is not None:
            pulumi.set(__self__, "search", search)
        if sort is not None:
            pulumi.set(__self__, "sort", sort)
        if source_fields is not None:
            pulumi.set(__self__, "source_fields", source_fields)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        A unique name for the field. Field names must begin with a letter and be at least 3 and no more than 64 characters long. The allowed characters are: `a`-`z` (lower-case letters), `0`-`9`, and `_` (underscore). The name `score` is reserved and cannot be used as a field name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The field type. Valid values: `date`, `date-array`, `double`, `double-array`, `int`, `int-array`, `literal`, `literal-array`, `text`, `text-array`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="analysisScheme")
    def analysis_scheme(self) -> Optional[pulumi.Input[str]]:
        """
        The analysis scheme you want to use for a `text` field. The analysis scheme specifies the language-specific text processing options that are used during indexing.
        """
        return pulumi.get(self, "analysis_scheme")

    @analysis_scheme.setter
    def analysis_scheme(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "analysis_scheme", value)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[str]]:
        """
        The default value for the field. This value is used when no value is specified for the field in the document data.
        """
        return pulumi.get(self, "default_value")

    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_value", value)

    @property
    @pulumi.getter
    def facet(self) -> Optional[pulumi.Input[bool]]:
        """
        You can get facet information by enabling this.
        """
        return pulumi.get(self, "facet")

    @facet.setter
    def facet(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "facet", value)

    @property
    @pulumi.getter
    def highlight(self) -> Optional[pulumi.Input[bool]]:
        """
        You can highlight information.
        """
        return pulumi.get(self, "highlight")

    @highlight.setter
    def highlight(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "highlight", value)

    @property
    @pulumi.getter(name="return")
    def return_(self) -> Optional[pulumi.Input[bool]]:
        """
        You can enable returning the value of all searchable fields.
        """
        return pulumi.get(self, "return_")

    @return_.setter
    def return_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "return_", value)

    @property
    @pulumi.getter
    def search(self) -> Optional[pulumi.Input[bool]]:
        """
        You can set whether this index should be searchable or not.
        """
        return pulumi.get(self, "search")

    @search.setter
    def search(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "search", value)

    @property
    @pulumi.getter
    def sort(self) -> Optional[pulumi.Input[bool]]:
        """
        You can enable the property to be sortable.
        """
        return pulumi.get(self, "sort")

    @sort.setter
    def sort(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sort", value)

    @property
    @pulumi.getter(name="sourceFields")
    def source_fields(self) -> Optional[pulumi.Input[str]]:
        """
        A comma-separated list of source fields to map to the field. Specifying a source field copies data from one field to another, enabling you to use the same source data in different ways by configuring different options for the fields.
        """
        return pulumi.get(self, "source_fields")

    @source_fields.setter
    def source_fields(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_fields", value)


@pulumi.input_type
class DomainScalingParametersArgs:
    def __init__(__self__, *,
                 desired_instance_type: Optional[pulumi.Input[str]] = None,
                 desired_partition_count: Optional[pulumi.Input[int]] = None,
                 desired_replication_count: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] desired_instance_type: The instance type that you want to preconfigure for your domain. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParameters.html) for valid values.
        :param pulumi.Input[int] desired_partition_count: The number of partitions you want to preconfigure for your domain. Only valid when you select `search.2xlarge` as the instance type.
        :param pulumi.Input[int] desired_replication_count: The number of replicas you want to preconfigure for each index partition.
        """
        if desired_instance_type is not None:
            pulumi.set(__self__, "desired_instance_type", desired_instance_type)
        if desired_partition_count is not None:
            pulumi.set(__self__, "desired_partition_count", desired_partition_count)
        if desired_replication_count is not None:
            pulumi.set(__self__, "desired_replication_count", desired_replication_count)

    @property
    @pulumi.getter(name="desiredInstanceType")
    def desired_instance_type(self) -> Optional[pulumi.Input[str]]:
        """
        The instance type that you want to preconfigure for your domain. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParameters.html) for valid values.
        """
        return pulumi.get(self, "desired_instance_type")

    @desired_instance_type.setter
    def desired_instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "desired_instance_type", value)

    @property
    @pulumi.getter(name="desiredPartitionCount")
    def desired_partition_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of partitions you want to preconfigure for your domain. Only valid when you select `search.2xlarge` as the instance type.
        """
        return pulumi.get(self, "desired_partition_count")

    @desired_partition_count.setter
    def desired_partition_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "desired_partition_count", value)

    @property
    @pulumi.getter(name="desiredReplicationCount")
    def desired_replication_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of replicas you want to preconfigure for each index partition.
        """
        return pulumi.get(self, "desired_replication_count")

    @desired_replication_count.setter
    def desired_replication_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "desired_replication_count", value)


