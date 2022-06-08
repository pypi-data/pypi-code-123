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

__all__ = ['CollectorPolicyInitArgs', 'CollectorPolicy']

@pulumi.input_type
class CollectorPolicyInitArgs:
    def __init__(__self__, *,
                 azure_traffic_collector_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 collector_policy_name: Optional[pulumi.Input[str]] = None,
                 emission_policies: Optional[pulumi.Input[Sequence[pulumi.Input['EmissionPoliciesPropertiesFormatArgs']]]] = None,
                 ingestion_policy: Optional[pulumi.Input['IngestionPolicyPropertiesFormatArgs']] = None):
        """
        The set of arguments for constructing a CollectorPolicy resource.
        :param pulumi.Input[str] azure_traffic_collector_name: Azure Traffic Collector name
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] collector_policy_name: Collector Policy Name
        :param pulumi.Input[Sequence[pulumi.Input['EmissionPoliciesPropertiesFormatArgs']]] emission_policies: Emission policies.
        :param pulumi.Input['IngestionPolicyPropertiesFormatArgs'] ingestion_policy: Ingestion policies.
        """
        pulumi.set(__self__, "azure_traffic_collector_name", azure_traffic_collector_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if collector_policy_name is not None:
            pulumi.set(__self__, "collector_policy_name", collector_policy_name)
        if emission_policies is not None:
            pulumi.set(__self__, "emission_policies", emission_policies)
        if ingestion_policy is not None:
            pulumi.set(__self__, "ingestion_policy", ingestion_policy)

    @property
    @pulumi.getter(name="azureTrafficCollectorName")
    def azure_traffic_collector_name(self) -> pulumi.Input[str]:
        """
        Azure Traffic Collector name
        """
        return pulumi.get(self, "azure_traffic_collector_name")

    @azure_traffic_collector_name.setter
    def azure_traffic_collector_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "azure_traffic_collector_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="collectorPolicyName")
    def collector_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Collector Policy Name
        """
        return pulumi.get(self, "collector_policy_name")

    @collector_policy_name.setter
    def collector_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collector_policy_name", value)

    @property
    @pulumi.getter(name="emissionPolicies")
    def emission_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EmissionPoliciesPropertiesFormatArgs']]]]:
        """
        Emission policies.
        """
        return pulumi.get(self, "emission_policies")

    @emission_policies.setter
    def emission_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EmissionPoliciesPropertiesFormatArgs']]]]):
        pulumi.set(self, "emission_policies", value)

    @property
    @pulumi.getter(name="ingestionPolicy")
    def ingestion_policy(self) -> Optional[pulumi.Input['IngestionPolicyPropertiesFormatArgs']]:
        """
        Ingestion policies.
        """
        return pulumi.get(self, "ingestion_policy")

    @ingestion_policy.setter
    def ingestion_policy(self, value: Optional[pulumi.Input['IngestionPolicyPropertiesFormatArgs']]):
        pulumi.set(self, "ingestion_policy", value)


warnings.warn("""Version v20210901preview will be removed in the next major version of the provider. Upgrade to version v20220501 or later.""", DeprecationWarning)


class CollectorPolicy(pulumi.CustomResource):
    warnings.warn("""Version v20210901preview will be removed in the next major version of the provider. Upgrade to version v20220501 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_traffic_collector_name: Optional[pulumi.Input[str]] = None,
                 collector_policy_name: Optional[pulumi.Input[str]] = None,
                 emission_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmissionPoliciesPropertiesFormatArgs']]]]] = None,
                 ingestion_policy: Optional[pulumi.Input[pulumi.InputType['IngestionPolicyPropertiesFormatArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Collector policy resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azure_traffic_collector_name: Azure Traffic Collector name
        :param pulumi.Input[str] collector_policy_name: Collector Policy Name
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmissionPoliciesPropertiesFormatArgs']]]] emission_policies: Emission policies.
        :param pulumi.Input[pulumi.InputType['IngestionPolicyPropertiesFormatArgs']] ingestion_policy: Ingestion policies.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CollectorPolicyInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Collector policy resource.

        :param str resource_name: The name of the resource.
        :param CollectorPolicyInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CollectorPolicyInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_traffic_collector_name: Optional[pulumi.Input[str]] = None,
                 collector_policy_name: Optional[pulumi.Input[str]] = None,
                 emission_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmissionPoliciesPropertiesFormatArgs']]]]] = None,
                 ingestion_policy: Optional[pulumi.Input[pulumi.InputType['IngestionPolicyPropertiesFormatArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""CollectorPolicy is deprecated: Version v20210901preview will be removed in the next major version of the provider. Upgrade to version v20220501 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CollectorPolicyInitArgs.__new__(CollectorPolicyInitArgs)

            if azure_traffic_collector_name is None and not opts.urn:
                raise TypeError("Missing required property 'azure_traffic_collector_name'")
            __props__.__dict__["azure_traffic_collector_name"] = azure_traffic_collector_name
            __props__.__dict__["collector_policy_name"] = collector_policy_name
            __props__.__dict__["emission_policies"] = emission_policies
            __props__.__dict__["ingestion_policy"] = ingestion_policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkfunction:CollectorPolicy"), pulumi.Alias(type_="azure-native:networkfunction/v20220501:CollectorPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CollectorPolicy, __self__).__init__(
            'azure-native:networkfunction/v20210901preview:CollectorPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CollectorPolicy':
        """
        Get an existing CollectorPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CollectorPolicyInitArgs.__new__(CollectorPolicyInitArgs)

        __props__.__dict__["emission_policies"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["ingestion_policy"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CollectorPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="emissionPolicies")
    def emission_policies(self) -> pulumi.Output[Optional[Sequence['outputs.EmissionPoliciesPropertiesFormatResponse']]]:
        """
        Emission policies.
        """
        return pulumi.get(self, "emission_policies")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="ingestionPolicy")
    def ingestion_policy(self) -> pulumi.Output[Optional['outputs.IngestionPolicyPropertiesFormatResponse']]:
        """
        Ingestion policies.
        """
        return pulumi.get(self, "ingestion_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.CollectorPolicyResponseSystemData']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

