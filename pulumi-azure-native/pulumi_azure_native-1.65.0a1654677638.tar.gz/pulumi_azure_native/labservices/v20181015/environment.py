# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 environment_setting_name: pulumi.Input[str],
                 lab_account_name: pulumi.Input[str],
                 lab_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 environment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_sets: Optional[pulumi.Input['ResourceSetArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[str] environment_setting_name: The name of the environment Setting.
        :param pulumi.Input[str] lab_account_name: The name of the lab Account.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] environment_name: The name of the environment.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input['ResourceSetArgs'] resource_sets: The set of a VM and the setting id it was created for
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] unique_identifier: The unique immutable identifier of a resource (Guid).
        """
        pulumi.set(__self__, "environment_setting_name", environment_setting_name)
        pulumi.set(__self__, "lab_account_name", lab_account_name)
        pulumi.set(__self__, "lab_name", lab_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if environment_name is not None:
            pulumi.set(__self__, "environment_name", environment_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_sets is not None:
            pulumi.set(__self__, "resource_sets", resource_sets)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if unique_identifier is not None:
            pulumi.set(__self__, "unique_identifier", unique_identifier)

    @property
    @pulumi.getter(name="environmentSettingName")
    def environment_setting_name(self) -> pulumi.Input[str]:
        """
        The name of the environment Setting.
        """
        return pulumi.get(self, "environment_setting_name")

    @environment_setting_name.setter
    def environment_setting_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_setting_name", value)

    @property
    @pulumi.getter(name="labAccountName")
    def lab_account_name(self) -> pulumi.Input[str]:
        """
        The name of the lab Account.
        """
        return pulumi.get(self, "lab_account_name")

    @lab_account_name.setter
    def lab_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_account_name", value)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[str]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_name", value)

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
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="resourceSets")
    def resource_sets(self) -> Optional[pulumi.Input['ResourceSetArgs']]:
        """
        The set of a VM and the setting id it was created for
        """
        return pulumi.get(self, "resource_sets")

    @resource_sets.setter
    def resource_sets(self, value: Optional[pulumi.Input['ResourceSetArgs']]):
        pulumi.set(self, "resource_sets", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @unique_identifier.setter
    def unique_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unique_identifier", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 environment_setting_name: Optional[pulumi.Input[str]] = None,
                 lab_account_name: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_sets: Optional[pulumi.Input[pulumi.InputType['ResourceSetArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents an environment instance

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] environment_name: The name of the environment.
        :param pulumi.Input[str] environment_setting_name: The name of the environment Setting.
        :param pulumi.Input[str] lab_account_name: The name of the lab Account.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['ResourceSetArgs']] resource_sets: The set of a VM and the setting id it was created for
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] unique_identifier: The unique immutable identifier of a resource (Guid).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an environment instance

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 environment_setting_name: Optional[pulumi.Input[str]] = None,
                 lab_account_name: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_sets: Optional[pulumi.Input[pulumi.InputType['ResourceSetArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            __props__.__dict__["environment_name"] = environment_name
            if environment_setting_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_setting_name'")
            __props__.__dict__["environment_setting_name"] = environment_setting_name
            if lab_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_account_name'")
            __props__.__dict__["lab_account_name"] = lab_account_name
            if lab_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_name'")
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["location"] = location
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_sets"] = resource_sets
            __props__.__dict__["tags"] = tags
            __props__.__dict__["unique_identifier"] = unique_identifier
            __props__.__dict__["claimed_by_user_name"] = None
            __props__.__dict__["claimed_by_user_object_id"] = None
            __props__.__dict__["claimed_by_user_principal_id"] = None
            __props__.__dict__["is_claimed"] = None
            __props__.__dict__["last_known_power_state"] = None
            __props__.__dict__["latest_operation_result"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["network_interface"] = None
            __props__.__dict__["password_last_reset"] = None
            __props__.__dict__["total_usage"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:labservices:Environment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Environment, __self__).__init__(
            'azure-native:labservices/v20181015:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

        __props__.__dict__["claimed_by_user_name"] = None
        __props__.__dict__["claimed_by_user_object_id"] = None
        __props__.__dict__["claimed_by_user_principal_id"] = None
        __props__.__dict__["is_claimed"] = None
        __props__.__dict__["last_known_power_state"] = None
        __props__.__dict__["latest_operation_result"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_interface"] = None
        __props__.__dict__["password_last_reset"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_sets"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["total_usage"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unique_identifier"] = None
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="claimedByUserName")
    def claimed_by_user_name(self) -> pulumi.Output[str]:
        """
        The name or email address of the user who has claimed the environment
        """
        return pulumi.get(self, "claimed_by_user_name")

    @property
    @pulumi.getter(name="claimedByUserObjectId")
    def claimed_by_user_object_id(self) -> pulumi.Output[str]:
        """
        The AAD object Id of the user who has claimed the environment
        """
        return pulumi.get(self, "claimed_by_user_object_id")

    @property
    @pulumi.getter(name="claimedByUserPrincipalId")
    def claimed_by_user_principal_id(self) -> pulumi.Output[str]:
        """
        The user principal Id of the user who has claimed the environment
        """
        return pulumi.get(self, "claimed_by_user_principal_id")

    @property
    @pulumi.getter(name="isClaimed")
    def is_claimed(self) -> pulumi.Output[bool]:
        """
        Is the environment claimed or not
        """
        return pulumi.get(self, "is_claimed")

    @property
    @pulumi.getter(name="lastKnownPowerState")
    def last_known_power_state(self) -> pulumi.Output[str]:
        """
        Last known power state of the environment
        """
        return pulumi.get(self, "last_known_power_state")

    @property
    @pulumi.getter(name="latestOperationResult")
    def latest_operation_result(self) -> pulumi.Output['outputs.LatestOperationResultResponse']:
        """
        The details of the latest operation. ex: status, error
        """
        return pulumi.get(self, "latest_operation_result")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> pulumi.Output['outputs.NetworkInterfaceResponse']:
        """
        Network details of the environment
        """
        return pulumi.get(self, "network_interface")

    @property
    @pulumi.getter(name="passwordLastReset")
    def password_last_reset(self) -> pulumi.Output[str]:
        """
        When the password was last reset on the environment.
        """
        return pulumi.get(self, "password_last_reset")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceSets")
    def resource_sets(self) -> pulumi.Output[Optional['outputs.ResourceSetResponse']]:
        """
        The set of a VM and the setting id it was created for
        """
        return pulumi.get(self, "resource_sets")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="totalUsage")
    def total_usage(self) -> pulumi.Output[str]:
        """
        How long the environment has been used by a lab user
        """
        return pulumi.get(self, "total_usage")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

