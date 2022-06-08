# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['BillingGroupArgs', 'BillingGroup']

@pulumi.input_type
class BillingGroupArgs:
    def __init__(__self__, *,
                 account_grouping: pulumi.Input['BillingGroupAccountGroupingArgs'],
                 computation_preference: pulumi.Input['BillingGroupComputationPreferenceArgs'],
                 primary_account_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['BillingGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a BillingGroup resource.
        :param pulumi.Input[str] primary_account_id: This account will act as a virtual payer account of the billing group
        """
        pulumi.set(__self__, "account_grouping", account_grouping)
        pulumi.set(__self__, "computation_preference", computation_preference)
        pulumi.set(__self__, "primary_account_id", primary_account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountGrouping")
    def account_grouping(self) -> pulumi.Input['BillingGroupAccountGroupingArgs']:
        return pulumi.get(self, "account_grouping")

    @account_grouping.setter
    def account_grouping(self, value: pulumi.Input['BillingGroupAccountGroupingArgs']):
        pulumi.set(self, "account_grouping", value)

    @property
    @pulumi.getter(name="computationPreference")
    def computation_preference(self) -> pulumi.Input['BillingGroupComputationPreferenceArgs']:
        return pulumi.get(self, "computation_preference")

    @computation_preference.setter
    def computation_preference(self, value: pulumi.Input['BillingGroupComputationPreferenceArgs']):
        pulumi.set(self, "computation_preference", value)

    @property
    @pulumi.getter(name="primaryAccountId")
    def primary_account_id(self) -> pulumi.Input[str]:
        """
        This account will act as a virtual payer account of the billing group
        """
        return pulumi.get(self, "primary_account_id")

    @primary_account_id.setter
    def primary_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary_account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BillingGroupTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BillingGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""BillingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class BillingGroup(pulumi.CustomResource):
    warnings.warn("""BillingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_grouping: Optional[pulumi.Input[pulumi.InputType['BillingGroupAccountGroupingArgs']]] = None,
                 computation_preference: Optional[pulumi.Input[pulumi.InputType['BillingGroupComputationPreferenceArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BillingGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        A billing group is a set of linked account which belong to the same end customer. It can be seen as a virtual consolidated billing family.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] primary_account_id: This account will act as a virtual payer account of the billing group
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BillingGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A billing group is a set of linked account which belong to the same end customer. It can be seen as a virtual consolidated billing family.

        :param str resource_name: The name of the resource.
        :param BillingGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BillingGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_grouping: Optional[pulumi.Input[pulumi.InputType['BillingGroupAccountGroupingArgs']]] = None,
                 computation_preference: Optional[pulumi.Input[pulumi.InputType['BillingGroupComputationPreferenceArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BillingGroupTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""BillingGroup is deprecated: BillingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BillingGroupArgs.__new__(BillingGroupArgs)

            if account_grouping is None and not opts.urn:
                raise TypeError("Missing required property 'account_grouping'")
            __props__.__dict__["account_grouping"] = account_grouping
            if computation_preference is None and not opts.urn:
                raise TypeError("Missing required property 'computation_preference'")
            __props__.__dict__["computation_preference"] = computation_preference
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if primary_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'primary_account_id'")
            __props__.__dict__["primary_account_id"] = primary_account_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["size"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_reason"] = None
        super(BillingGroup, __self__).__init__(
            'aws-native:billingconductor:BillingGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BillingGroup':
        """
        Get an existing BillingGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BillingGroupArgs.__new__(BillingGroupArgs)

        __props__.__dict__["account_grouping"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["computation_preference"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["primary_account_id"] = None
        __props__.__dict__["size"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_reason"] = None
        __props__.__dict__["tags"] = None
        return BillingGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountGrouping")
    def account_grouping(self) -> pulumi.Output['outputs.BillingGroupAccountGrouping']:
        return pulumi.get(self, "account_grouping")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Billing Group ARN
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="computationPreference")
    def computation_preference(self) -> pulumi.Output['outputs.BillingGroupComputationPreference']:
        return pulumi.get(self, "computation_preference")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        Creation timestamp in UNIX epoch time format
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[int]:
        """
        Latest modified timestamp in UNIX epoch time format
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryAccountId")
    def primary_account_id(self) -> pulumi.Output[str]:
        """
        This account will act as a virtual payer account of the billing group
        """
        return pulumi.get(self, "primary_account_id")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        Number of accounts in the billing group
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['BillingGroupStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status_reason")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.BillingGroupTag']]]:
        return pulumi.get(self, "tags")

