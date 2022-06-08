# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['PolicyArgs', 'Policy']

@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 custom_rules: Optional[pulumi.Input['CustomRuleListArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_rules: Optional[pulumi.Input['ManagedRuleSetListArgs']] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_settings: Optional[pulumi.Input['PolicySettingsArgs']] = None,
                 rate_limit_rules: Optional[pulumi.Input['RateLimitRuleListArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Policy resource.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['SkuArgs'] sku: The pricing tier (defines a CDN provider, feature list and rate) of the CdnWebApplicationFirewallPolicy.
        :param pulumi.Input['CustomRuleListArgs'] custom_rules: Describes custom rules inside the policy.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['ManagedRuleSetListArgs'] managed_rules: Describes managed rules inside the policy.
        :param pulumi.Input[str] policy_name: The name of the CdnWebApplicationFirewallPolicy.
        :param pulumi.Input['PolicySettingsArgs'] policy_settings: Describes  policySettings for policy
        :param pulumi.Input['RateLimitRuleListArgs'] rate_limit_rules: Describes rate limit rules inside the policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if custom_rules is not None:
            pulumi.set(__self__, "custom_rules", custom_rules)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_rules is not None:
            pulumi.set(__self__, "managed_rules", managed_rules)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if policy_settings is not None:
            pulumi.set(__self__, "policy_settings", policy_settings)
        if rate_limit_rules is not None:
            pulumi.set(__self__, "rate_limit_rules", rate_limit_rules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        The pricing tier (defines a CDN provider, feature list and rate) of the CdnWebApplicationFirewallPolicy.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[pulumi.Input['CustomRuleListArgs']]:
        """
        Describes custom rules inside the policy.
        """
        return pulumi.get(self, "custom_rules")

    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input['CustomRuleListArgs']]):
        pulumi.set(self, "custom_rules", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> Optional[pulumi.Input['ManagedRuleSetListArgs']]:
        """
        Describes managed rules inside the policy.
        """
        return pulumi.get(self, "managed_rules")

    @managed_rules.setter
    def managed_rules(self, value: Optional[pulumi.Input['ManagedRuleSetListArgs']]):
        pulumi.set(self, "managed_rules", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the CdnWebApplicationFirewallPolicy.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> Optional[pulumi.Input['PolicySettingsArgs']]:
        """
        Describes  policySettings for policy
        """
        return pulumi.get(self, "policy_settings")

    @policy_settings.setter
    def policy_settings(self, value: Optional[pulumi.Input['PolicySettingsArgs']]):
        pulumi.set(self, "policy_settings", value)

    @property
    @pulumi.getter(name="rateLimitRules")
    def rate_limit_rules(self) -> Optional[pulumi.Input['RateLimitRuleListArgs']]:
        """
        Describes rate limit rules inside the policy.
        """
        return pulumi.get(self, "rate_limit_rules")

    @rate_limit_rules.setter
    def rate_limit_rules(self, value: Optional[pulumi.Input['RateLimitRuleListArgs']]):
        pulumi.set(self, "rate_limit_rules", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version v20190615preview will be removed in the next major version of the provider. Upgrade to version v20200901 or later.""", DeprecationWarning)


class Policy(pulumi.CustomResource):
    warnings.warn("""Version v20190615preview will be removed in the next major version of the provider. Upgrade to version v20200901 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_rules: Optional[pulumi.Input[pulumi.InputType['CustomRuleListArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_rules: Optional[pulumi.Input[pulumi.InputType['ManagedRuleSetListArgs']]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_settings: Optional[pulumi.Input[pulumi.InputType['PolicySettingsArgs']]] = None,
                 rate_limit_rules: Optional[pulumi.Input[pulumi.InputType['RateLimitRuleListArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Defines web application firewall policy for Azure CDN.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CustomRuleListArgs']] custom_rules: Describes custom rules inside the policy.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[pulumi.InputType['ManagedRuleSetListArgs']] managed_rules: Describes managed rules inside the policy.
        :param pulumi.Input[str] policy_name: The name of the CdnWebApplicationFirewallPolicy.
        :param pulumi.Input[pulumi.InputType['PolicySettingsArgs']] policy_settings: Describes  policySettings for policy
        :param pulumi.Input[pulumi.InputType['RateLimitRuleListArgs']] rate_limit_rules: Describes rate limit rules inside the policy.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The pricing tier (defines a CDN provider, feature list and rate) of the CdnWebApplicationFirewallPolicy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines web application firewall policy for Azure CDN.

        :param str resource_name: The name of the resource.
        :param PolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_rules: Optional[pulumi.Input[pulumi.InputType['CustomRuleListArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_rules: Optional[pulumi.Input[pulumi.InputType['ManagedRuleSetListArgs']]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_settings: Optional[pulumi.Input[pulumi.InputType['PolicySettingsArgs']]] = None,
                 rate_limit_rules: Optional[pulumi.Input[pulumi.InputType['RateLimitRuleListArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Policy is deprecated: Version v20190615preview will be removed in the next major version of the provider. Upgrade to version v20200901 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyArgs.__new__(PolicyArgs)

            __props__.__dict__["custom_rules"] = custom_rules
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_rules"] = managed_rules
            __props__.__dict__["policy_name"] = policy_name
            __props__.__dict__["policy_settings"] = policy_settings
            __props__.__dict__["rate_limit_rules"] = rate_limit_rules
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["endpoint_links"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn:Policy"), pulumi.Alias(type_="azure-native:cdn/v20190615:Policy"), pulumi.Alias(type_="azure-native:cdn/v20200331:Policy"), pulumi.Alias(type_="azure-native:cdn/v20200415:Policy"), pulumi.Alias(type_="azure-native:cdn/v20200901:Policy"), pulumi.Alias(type_="azure-native:cdn/v20210601:Policy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Policy, __self__).__init__(
            'azure-native:cdn/v20190615preview:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyArgs.__new__(PolicyArgs)

        __props__.__dict__["custom_rules"] = None
        __props__.__dict__["endpoint_links"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_rules"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy_settings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rate_limit_rules"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> pulumi.Output[Optional['outputs.CustomRuleListResponse']]:
        """
        Describes custom rules inside the policy.
        """
        return pulumi.get(self, "custom_rules")

    @property
    @pulumi.getter(name="endpointLinks")
    def endpoint_links(self) -> pulumi.Output[Sequence['outputs.CdnEndpointResponse']]:
        """
        Describes Azure CDN endpoints associated with this Web Application Firewall policy.
        """
        return pulumi.get(self, "endpoint_links")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> pulumi.Output[Optional['outputs.ManagedRuleSetListResponse']]:
        """
        Describes managed rules inside the policy.
        """
        return pulumi.get(self, "managed_rules")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> pulumi.Output[Optional['outputs.PolicySettingsResponse']]:
        """
        Describes  policySettings for policy
        """
        return pulumi.get(self, "policy_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the WebApplicationFirewallPolicy.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rateLimitRules")
    def rate_limit_rules(self) -> pulumi.Output[Optional['outputs.RateLimitRuleListResponse']]:
        """
        Describes rate limit rules inside the policy.
        """
        return pulumi.get(self, "rate_limit_rules")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        The pricing tier (defines a CDN provider, feature list and rate) of the CdnWebApplicationFirewallPolicy.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

