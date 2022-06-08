# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 lab_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 additional_usage_quota: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] email: Email address of the user.
        :param pulumi.Input[str] lab_name: The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] additional_usage_quota: The amount of usage quota time the user gets in addition to the lab usage quota.
        :param pulumi.Input[str] user_name: The name of the user that uniquely identifies it within containing lab. Used in resource URIs.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "lab_name", lab_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if additional_usage_quota is not None:
            pulumi.set(__self__, "additional_usage_quota", additional_usage_quota)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        Email address of the user.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[str]:
        """
        The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="additionalUsageQuota")
    def additional_usage_quota(self) -> Optional[pulumi.Input[str]]:
        """
        The amount of usage quota time the user gets in addition to the lab usage quota.
        """
        return pulumi.get(self, "additional_usage_quota")

    @additional_usage_quota.setter
    def additional_usage_quota(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "additional_usage_quota", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user that uniquely identifies it within containing lab. Used in resource URIs.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_usage_quota: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        User of a lab that can register for and use virtual machines within the lab.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] additional_usage_quota: The amount of usage quota time the user gets in addition to the lab usage quota.
        :param pulumi.Input[str] email: Email address of the user.
        :param pulumi.Input[str] lab_name: The name of the lab that uniquely identifies it within containing lab account. Used in resource URIs.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] user_name: The name of the user that uniquely identifies it within containing lab. Used in resource URIs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        User of a lab that can register for and use virtual machines within the lab.

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_usage_quota: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["additional_usage_quota"] = additional_usage_quota
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if lab_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_name'")
            __props__.__dict__["lab_name"] = lab_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["display_name"] = None
            __props__.__dict__["invitation_sent"] = None
            __props__.__dict__["invitation_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["registration_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["total_usage"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:labservices/v20211001preview:User")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(User, __self__).__init__(
            'azure-native:labservices/v20211115preview:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserArgs.__new__(UserArgs)

        __props__.__dict__["additional_usage_quota"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["email"] = None
        __props__.__dict__["invitation_sent"] = None
        __props__.__dict__["invitation_state"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["registration_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["total_usage"] = None
        __props__.__dict__["type"] = None
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalUsageQuota")
    def additional_usage_quota(self) -> pulumi.Output[Optional[str]]:
        """
        The amount of usage quota time the user gets in addition to the lab usage quota.
        """
        return pulumi.get(self, "additional_usage_quota")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Display name of the user, for example user's full name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Email address of the user.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="invitationSent")
    def invitation_sent(self) -> pulumi.Output[str]:
        """
        Date and time when the invitation message was sent to the user.
        """
        return pulumi.get(self, "invitation_sent")

    @property
    @pulumi.getter(name="invitationState")
    def invitation_state(self) -> pulumi.Output[str]:
        """
        State of the invitation message for the user.
        """
        return pulumi.get(self, "invitation_state")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Current provisioning state of the user resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="registrationState")
    def registration_state(self) -> pulumi.Output[str]:
        """
        State of the user's registration within the lab.
        """
        return pulumi.get(self, "registration_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the user resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="totalUsage")
    def total_usage(self) -> pulumi.Output[str]:
        """
        How long the user has used their virtual machines in this lab.
        """
        return pulumi.get(self, "total_usage")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

