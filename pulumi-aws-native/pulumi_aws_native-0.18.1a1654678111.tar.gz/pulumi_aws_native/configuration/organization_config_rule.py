# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['OrganizationConfigRuleArgs', 'OrganizationConfigRule']

@pulumi.input_type
class OrganizationConfigRuleArgs:
    def __init__(__self__, *,
                 excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 organization_config_rule_name: Optional[pulumi.Input[str]] = None,
                 organization_custom_rule_metadata: Optional[pulumi.Input['OrganizationConfigRuleOrganizationCustomRuleMetadataArgs']] = None,
                 organization_managed_rule_metadata: Optional[pulumi.Input['OrganizationConfigRuleOrganizationManagedRuleMetadataArgs']] = None):
        """
        The set of arguments for constructing a OrganizationConfigRule resource.
        """
        if excluded_accounts is not None:
            pulumi.set(__self__, "excluded_accounts", excluded_accounts)
        if organization_config_rule_name is not None:
            pulumi.set(__self__, "organization_config_rule_name", organization_config_rule_name)
        if organization_custom_rule_metadata is not None:
            pulumi.set(__self__, "organization_custom_rule_metadata", organization_custom_rule_metadata)
        if organization_managed_rule_metadata is not None:
            pulumi.set(__self__, "organization_managed_rule_metadata", organization_managed_rule_metadata)

    @property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "excluded_accounts")

    @excluded_accounts.setter
    def excluded_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_accounts", value)

    @property
    @pulumi.getter(name="organizationConfigRuleName")
    def organization_config_rule_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "organization_config_rule_name")

    @organization_config_rule_name.setter
    def organization_config_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_config_rule_name", value)

    @property
    @pulumi.getter(name="organizationCustomRuleMetadata")
    def organization_custom_rule_metadata(self) -> Optional[pulumi.Input['OrganizationConfigRuleOrganizationCustomRuleMetadataArgs']]:
        return pulumi.get(self, "organization_custom_rule_metadata")

    @organization_custom_rule_metadata.setter
    def organization_custom_rule_metadata(self, value: Optional[pulumi.Input['OrganizationConfigRuleOrganizationCustomRuleMetadataArgs']]):
        pulumi.set(self, "organization_custom_rule_metadata", value)

    @property
    @pulumi.getter(name="organizationManagedRuleMetadata")
    def organization_managed_rule_metadata(self) -> Optional[pulumi.Input['OrganizationConfigRuleOrganizationManagedRuleMetadataArgs']]:
        return pulumi.get(self, "organization_managed_rule_metadata")

    @organization_managed_rule_metadata.setter
    def organization_managed_rule_metadata(self, value: Optional[pulumi.Input['OrganizationConfigRuleOrganizationManagedRuleMetadataArgs']]):
        pulumi.set(self, "organization_managed_rule_metadata", value)


warnings.warn("""OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class OrganizationConfigRule(pulumi.CustomResource):
    warnings.warn("""OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 organization_config_rule_name: Optional[pulumi.Input[str]] = None,
                 organization_custom_rule_metadata: Optional[pulumi.Input[pulumi.InputType['OrganizationConfigRuleOrganizationCustomRuleMetadataArgs']]] = None,
                 organization_managed_rule_metadata: Optional[pulumi.Input[pulumi.InputType['OrganizationConfigRuleOrganizationManagedRuleMetadataArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Config::OrganizationConfigRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[OrganizationConfigRuleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Config::OrganizationConfigRule

        :param str resource_name: The name of the resource.
        :param OrganizationConfigRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationConfigRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 organization_config_rule_name: Optional[pulumi.Input[str]] = None,
                 organization_custom_rule_metadata: Optional[pulumi.Input[pulumi.InputType['OrganizationConfigRuleOrganizationCustomRuleMetadataArgs']]] = None,
                 organization_managed_rule_metadata: Optional[pulumi.Input[pulumi.InputType['OrganizationConfigRuleOrganizationManagedRuleMetadataArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""OrganizationConfigRule is deprecated: OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationConfigRuleArgs.__new__(OrganizationConfigRuleArgs)

            __props__.__dict__["excluded_accounts"] = excluded_accounts
            __props__.__dict__["organization_config_rule_name"] = organization_config_rule_name
            __props__.__dict__["organization_custom_rule_metadata"] = organization_custom_rule_metadata
            __props__.__dict__["organization_managed_rule_metadata"] = organization_managed_rule_metadata
        super(OrganizationConfigRule, __self__).__init__(
            'aws-native:configuration:OrganizationConfigRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationConfigRule':
        """
        Get an existing OrganizationConfigRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationConfigRuleArgs.__new__(OrganizationConfigRuleArgs)

        __props__.__dict__["excluded_accounts"] = None
        __props__.__dict__["organization_config_rule_name"] = None
        __props__.__dict__["organization_custom_rule_metadata"] = None
        __props__.__dict__["organization_managed_rule_metadata"] = None
        return OrganizationConfigRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "excluded_accounts")

    @property
    @pulumi.getter(name="organizationConfigRuleName")
    def organization_config_rule_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "organization_config_rule_name")

    @property
    @pulumi.getter(name="organizationCustomRuleMetadata")
    def organization_custom_rule_metadata(self) -> pulumi.Output[Optional['outputs.OrganizationConfigRuleOrganizationCustomRuleMetadata']]:
        return pulumi.get(self, "organization_custom_rule_metadata")

    @property
    @pulumi.getter(name="organizationManagedRuleMetadata")
    def organization_managed_rule_metadata(self) -> pulumi.Output[Optional['outputs.OrganizationConfigRuleOrganizationManagedRuleMetadata']]:
        return pulumi.get(self, "organization_managed_rule_metadata")

