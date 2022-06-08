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

__all__ = ['LocalUserArgs', 'LocalUser']

@pulumi.input_type
class LocalUserArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 has_shared_key: Optional[pulumi.Input[bool]] = None,
                 has_ssh_key: Optional[pulumi.Input[bool]] = None,
                 has_ssh_password: Optional[pulumi.Input[bool]] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionScopeArgs']]]] = None,
                 ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input['SshPublicKeyArgs']]]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LocalUser resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[bool] has_shared_key: Indicates whether shared key exists. Set it to false to remove existing shared key.
        :param pulumi.Input[bool] has_ssh_key: Indicates whether ssh key exists. Set it to false to remove existing SSH key.
        :param pulumi.Input[bool] has_ssh_password: Indicates whether ssh password exists. Set it to false to remove existing SSH password.
        :param pulumi.Input[str] home_directory: Optional, local user home directory.
        :param pulumi.Input[Sequence[pulumi.Input['PermissionScopeArgs']]] permission_scopes: The permission scopes of the local user.
        :param pulumi.Input[Sequence[pulumi.Input['SshPublicKeyArgs']]] ssh_authorized_keys: Optional, local user ssh authorized keys for SFTP.
        :param pulumi.Input[str] username: The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if has_shared_key is not None:
            pulumi.set(__self__, "has_shared_key", has_shared_key)
        if has_ssh_key is not None:
            pulumi.set(__self__, "has_ssh_key", has_ssh_key)
        if has_ssh_password is not None:
            pulumi.set(__self__, "has_ssh_password", has_ssh_password)
        if home_directory is not None:
            pulumi.set(__self__, "home_directory", home_directory)
        if permission_scopes is not None:
            pulumi.set(__self__, "permission_scopes", permission_scopes)
        if ssh_authorized_keys is not None:
            pulumi.set(__self__, "ssh_authorized_keys", ssh_authorized_keys)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="hasSharedKey")
    def has_shared_key(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether shared key exists. Set it to false to remove existing shared key.
        """
        return pulumi.get(self, "has_shared_key")

    @has_shared_key.setter
    def has_shared_key(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_shared_key", value)

    @property
    @pulumi.getter(name="hasSshKey")
    def has_ssh_key(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether ssh key exists. Set it to false to remove existing SSH key.
        """
        return pulumi.get(self, "has_ssh_key")

    @has_ssh_key.setter
    def has_ssh_key(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_ssh_key", value)

    @property
    @pulumi.getter(name="hasSshPassword")
    def has_ssh_password(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether ssh password exists. Set it to false to remove existing SSH password.
        """
        return pulumi.get(self, "has_ssh_password")

    @has_ssh_password.setter
    def has_ssh_password(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_ssh_password", value)

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[str]]:
        """
        Optional, local user home directory.
        """
        return pulumi.get(self, "home_directory")

    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory", value)

    @property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PermissionScopeArgs']]]]:
        """
        The permission scopes of the local user.
        """
        return pulumi.get(self, "permission_scopes")

    @permission_scopes.setter
    def permission_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionScopeArgs']]]]):
        pulumi.set(self, "permission_scopes", value)

    @property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SshPublicKeyArgs']]]]:
        """
        Optional, local user ssh authorized keys for SFTP.
        """
        return pulumi.get(self, "ssh_authorized_keys")

    @ssh_authorized_keys.setter
    def ssh_authorized_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SshPublicKeyArgs']]]]):
        pulumi.set(self, "ssh_authorized_keys", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class LocalUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 has_shared_key: Optional[pulumi.Input[bool]] = None,
                 has_ssh_key: Optional[pulumi.Input[bool]] = None,
                 has_ssh_password: Optional[pulumi.Input[bool]] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionScopeArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SshPublicKeyArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The local user associated with the storage accounts.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[bool] has_shared_key: Indicates whether shared key exists. Set it to false to remove existing shared key.
        :param pulumi.Input[bool] has_ssh_key: Indicates whether ssh key exists. Set it to false to remove existing SSH key.
        :param pulumi.Input[bool] has_ssh_password: Indicates whether ssh password exists. Set it to false to remove existing SSH password.
        :param pulumi.Input[str] home_directory: Optional, local user home directory.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionScopeArgs']]]] permission_scopes: The permission scopes of the local user.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SshPublicKeyArgs']]]] ssh_authorized_keys: Optional, local user ssh authorized keys for SFTP.
        :param pulumi.Input[str] username: The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The local user associated with the storage accounts.

        :param str resource_name: The name of the resource.
        :param LocalUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 has_shared_key: Optional[pulumi.Input[bool]] = None,
                 has_ssh_key: Optional[pulumi.Input[bool]] = None,
                 has_ssh_password: Optional[pulumi.Input[bool]] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 permission_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionScopeArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssh_authorized_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SshPublicKeyArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
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
            __props__ = LocalUserArgs.__new__(LocalUserArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["has_shared_key"] = has_shared_key
            __props__.__dict__["has_ssh_key"] = has_ssh_key
            __props__.__dict__["has_ssh_password"] = has_ssh_password
            __props__.__dict__["home_directory"] = home_directory
            __props__.__dict__["permission_scopes"] = permission_scopes
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["ssh_authorized_keys"] = ssh_authorized_keys
            __props__.__dict__["username"] = username
            __props__.__dict__["name"] = None
            __props__.__dict__["sid"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:LocalUser"), pulumi.Alias(type_="azure-native:storage/v20210801:LocalUser")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LocalUser, __self__).__init__(
            'azure-native:storage/v20210901:LocalUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocalUser':
        """
        Get an existing LocalUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocalUserArgs.__new__(LocalUserArgs)

        __props__.__dict__["has_shared_key"] = None
        __props__.__dict__["has_ssh_key"] = None
        __props__.__dict__["has_ssh_password"] = None
        __props__.__dict__["home_directory"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["permission_scopes"] = None
        __props__.__dict__["sid"] = None
        __props__.__dict__["ssh_authorized_keys"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return LocalUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hasSharedKey")
    def has_shared_key(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether shared key exists. Set it to false to remove existing shared key.
        """
        return pulumi.get(self, "has_shared_key")

    @property
    @pulumi.getter(name="hasSshKey")
    def has_ssh_key(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether ssh key exists. Set it to false to remove existing SSH key.
        """
        return pulumi.get(self, "has_ssh_key")

    @property
    @pulumi.getter(name="hasSshPassword")
    def has_ssh_password(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether ssh password exists. Set it to false to remove existing SSH password.
        """
        return pulumi.get(self, "has_ssh_password")

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[str]]:
        """
        Optional, local user home directory.
        """
        return pulumi.get(self, "home_directory")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(self) -> pulumi.Output[Optional[Sequence['outputs.PermissionScopeResponse']]]:
        """
        The permission scopes of the local user.
        """
        return pulumi.get(self, "permission_scopes")

    @property
    @pulumi.getter
    def sid(self) -> pulumi.Output[str]:
        """
        A unique Security Identifier that is generated by the server.
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(self) -> pulumi.Output[Optional[Sequence['outputs.SshPublicKeyResponse']]]:
        """
        Optional, local user ssh authorized keys for SFTP.
        """
        return pulumi.get(self, "ssh_authorized_keys")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

