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

__all__ = ['BlobContainerArgs', 'BlobContainer']

@pulumi.input_type
class BlobContainerArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 container_name: Optional[pulumi.Input[str]] = None,
                 default_encryption_scope: Optional[pulumi.Input[str]] = None,
                 deny_encryption_scope_override: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 public_access: Optional[pulumi.Input['PublicAccess']] = None):
        """
        The set of arguments for constructing a BlobContainer resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        :param pulumi.Input[str] default_encryption_scope: Default the container to use specified encryption scope for all writes.
        :param pulumi.Input[bool] deny_encryption_scope_override: Block override of encryption scope from the container default.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A name-value pair to associate with the container as metadata.
        :param pulumi.Input['PublicAccess'] public_access: Specifies whether data in the container may be accessed publicly and the level of access.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if container_name is not None:
            pulumi.set(__self__, "container_name", container_name)
        if default_encryption_scope is not None:
            pulumi.set(__self__, "default_encryption_scope", default_encryption_scope)
        if deny_encryption_scope_override is not None:
            pulumi.set(__self__, "deny_encryption_scope_override", deny_encryption_scope_override)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if public_access is not None:
            pulumi.set(__self__, "public_access", public_access)

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
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="defaultEncryptionScope")
    def default_encryption_scope(self) -> Optional[pulumi.Input[str]]:
        """
        Default the container to use specified encryption scope for all writes.
        """
        return pulumi.get(self, "default_encryption_scope")

    @default_encryption_scope.setter
    def default_encryption_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_encryption_scope", value)

    @property
    @pulumi.getter(name="denyEncryptionScopeOverride")
    def deny_encryption_scope_override(self) -> Optional[pulumi.Input[bool]]:
        """
        Block override of encryption scope from the container default.
        """
        return pulumi.get(self, "deny_encryption_scope_override")

    @deny_encryption_scope_override.setter
    def deny_encryption_scope_override(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deny_encryption_scope_override", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A name-value pair to associate with the container as metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> Optional[pulumi.Input['PublicAccess']]:
        """
        Specifies whether data in the container may be accessed publicly and the level of access.
        """
        return pulumi.get(self, "public_access")

    @public_access.setter
    def public_access(self, value: Optional[pulumi.Input['PublicAccess']]):
        pulumi.set(self, "public_access", value)


warnings.warn("""Version v20190601 will be removed in the next major version of the provider. Upgrade to version v20210201 or later.""", DeprecationWarning)


class BlobContainer(pulumi.CustomResource):
    warnings.warn("""Version v20190601 will be removed in the next major version of the provider. Upgrade to version v20210201 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 default_encryption_scope: Optional[pulumi.Input[str]] = None,
                 deny_encryption_scope_override: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 public_access: Optional[pulumi.Input['PublicAccess']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Properties of the blob container, including Id, resource name, resource type, Etag.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        :param pulumi.Input[str] default_encryption_scope: Default the container to use specified encryption scope for all writes.
        :param pulumi.Input[bool] deny_encryption_scope_override: Block override of encryption scope from the container default.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A name-value pair to associate with the container as metadata.
        :param pulumi.Input['PublicAccess'] public_access: Specifies whether data in the container may be accessed publicly and the level of access.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BlobContainerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Properties of the blob container, including Id, resource name, resource type, Etag.

        :param str resource_name: The name of the resource.
        :param BlobContainerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BlobContainerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 default_encryption_scope: Optional[pulumi.Input[str]] = None,
                 deny_encryption_scope_override: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 public_access: Optional[pulumi.Input['PublicAccess']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""BlobContainer is deprecated: Version v20190601 will be removed in the next major version of the provider. Upgrade to version v20210201 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BlobContainerArgs.__new__(BlobContainerArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["container_name"] = container_name
            __props__.__dict__["default_encryption_scope"] = default_encryption_scope
            __props__.__dict__["deny_encryption_scope_override"] = deny_encryption_scope_override
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["public_access"] = public_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["deleted"] = None
            __props__.__dict__["deleted_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["has_immutability_policy"] = None
            __props__.__dict__["has_legal_hold"] = None
            __props__.__dict__["immutability_policy"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["lease_duration"] = None
            __props__.__dict__["lease_state"] = None
            __props__.__dict__["lease_status"] = None
            __props__.__dict__["legal_hold"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["remaining_retention_days"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20180201:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20180301preview:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20180701:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20181101:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20190401:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20200801preview:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20210101:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20210201:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20210401:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20210601:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20210801:BlobContainer"), pulumi.Alias(type_="azure-native:storage/v20210901:BlobContainer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BlobContainer, __self__).__init__(
            'azure-native:storage/v20190601:BlobContainer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BlobContainer':
        """
        Get an existing BlobContainer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BlobContainerArgs.__new__(BlobContainerArgs)

        __props__.__dict__["default_encryption_scope"] = None
        __props__.__dict__["deleted"] = None
        __props__.__dict__["deleted_time"] = None
        __props__.__dict__["deny_encryption_scope_override"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["has_immutability_policy"] = None
        __props__.__dict__["has_legal_hold"] = None
        __props__.__dict__["immutability_policy"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["lease_duration"] = None
        __props__.__dict__["lease_state"] = None
        __props__.__dict__["lease_status"] = None
        __props__.__dict__["legal_hold"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["public_access"] = None
        __props__.__dict__["remaining_retention_days"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return BlobContainer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultEncryptionScope")
    def default_encryption_scope(self) -> pulumi.Output[Optional[str]]:
        """
        Default the container to use specified encryption scope for all writes.
        """
        return pulumi.get(self, "default_encryption_scope")

    @property
    @pulumi.getter
    def deleted(self) -> pulumi.Output[bool]:
        """
        Indicates whether the blob container was deleted.
        """
        return pulumi.get(self, "deleted")

    @property
    @pulumi.getter(name="deletedTime")
    def deleted_time(self) -> pulumi.Output[str]:
        """
        Blob container deletion time.
        """
        return pulumi.get(self, "deleted_time")

    @property
    @pulumi.getter(name="denyEncryptionScopeOverride")
    def deny_encryption_scope_override(self) -> pulumi.Output[Optional[bool]]:
        """
        Block override of encryption scope from the container default.
        """
        return pulumi.get(self, "deny_encryption_scope_override")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hasImmutabilityPolicy")
    def has_immutability_policy(self) -> pulumi.Output[bool]:
        """
        The hasImmutabilityPolicy public property is set to true by SRP if ImmutabilityPolicy has been created for this container. The hasImmutabilityPolicy public property is set to false by SRP if ImmutabilityPolicy has not been created for this container.
        """
        return pulumi.get(self, "has_immutability_policy")

    @property
    @pulumi.getter(name="hasLegalHold")
    def has_legal_hold(self) -> pulumi.Output[bool]:
        """
        The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold=true for a given account.
        """
        return pulumi.get(self, "has_legal_hold")

    @property
    @pulumi.getter(name="immutabilityPolicy")
    def immutability_policy(self) -> pulumi.Output['outputs.ImmutabilityPolicyPropertiesResponse']:
        """
        The ImmutabilityPolicy property of the container.
        """
        return pulumi.get(self, "immutability_policy")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        Returns the date and time the container was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="leaseDuration")
    def lease_duration(self) -> pulumi.Output[str]:
        """
        Specifies whether the lease on a container is of infinite or fixed duration, only when the container is leased.
        """
        return pulumi.get(self, "lease_duration")

    @property
    @pulumi.getter(name="leaseState")
    def lease_state(self) -> pulumi.Output[str]:
        """
        Lease state of the container.
        """
        return pulumi.get(self, "lease_state")

    @property
    @pulumi.getter(name="leaseStatus")
    def lease_status(self) -> pulumi.Output[str]:
        """
        The lease status of the container.
        """
        return pulumi.get(self, "lease_status")

    @property
    @pulumi.getter(name="legalHold")
    def legal_hold(self) -> pulumi.Output['outputs.LegalHoldPropertiesResponse']:
        """
        The LegalHold property of the container.
        """
        return pulumi.get(self, "legal_hold")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A name-value pair to associate with the container as metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether data in the container may be accessed publicly and the level of access.
        """
        return pulumi.get(self, "public_access")

    @property
    @pulumi.getter(name="remainingRetentionDays")
    def remaining_retention_days(self) -> pulumi.Output[int]:
        """
        Remaining retention days for soft deleted blob container.
        """
        return pulumi.get(self, "remaining_retention_days")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the deleted blob container.
        """
        return pulumi.get(self, "version")

