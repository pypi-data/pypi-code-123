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

__all__ = ['BatchAccountArgs', 'BatchAccount']

@pulumi.input_type
class BatchAccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 auto_storage: Optional[pulumi.Input['AutoStorageBasePropertiesArgs']] = None,
                 key_vault_reference: Optional[pulumi.Input['KeyVaultReferenceArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_allocation_mode: Optional[pulumi.Input['PoolAllocationMode']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a BatchAccount resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the Batch account.
        :param pulumi.Input[str] account_name: A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.
        :param pulumi.Input['AutoStorageBasePropertiesArgs'] auto_storage: The properties related to the auto-storage account.
        :param pulumi.Input['KeyVaultReferenceArgs'] key_vault_reference: A reference to the Azure key vault associated with the Batch account.
        :param pulumi.Input[str] location: The region in which to create the account.
        :param pulumi.Input['PoolAllocationMode'] pool_allocation_mode: The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The user-specified tags associated with the account.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if auto_storage is not None:
            pulumi.set(__self__, "auto_storage", auto_storage)
        if key_vault_reference is not None:
            pulumi.set(__self__, "key_vault_reference", key_vault_reference)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if pool_allocation_mode is not None:
            pulumi.set(__self__, "pool_allocation_mode", pool_allocation_mode)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the Batch account.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="autoStorage")
    def auto_storage(self) -> Optional[pulumi.Input['AutoStorageBasePropertiesArgs']]:
        """
        The properties related to the auto-storage account.
        """
        return pulumi.get(self, "auto_storage")

    @auto_storage.setter
    def auto_storage(self, value: Optional[pulumi.Input['AutoStorageBasePropertiesArgs']]):
        pulumi.set(self, "auto_storage", value)

    @property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(self) -> Optional[pulumi.Input['KeyVaultReferenceArgs']]:
        """
        A reference to the Azure key vault associated with the Batch account.
        """
        return pulumi.get(self, "key_vault_reference")

    @key_vault_reference.setter
    def key_vault_reference(self, value: Optional[pulumi.Input['KeyVaultReferenceArgs']]):
        pulumi.set(self, "key_vault_reference", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to create the account.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="poolAllocationMode")
    def pool_allocation_mode(self) -> Optional[pulumi.Input['PoolAllocationMode']]:
        """
        The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.
        """
        return pulumi.get(self, "pool_allocation_mode")

    @pool_allocation_mode.setter
    def pool_allocation_mode(self, value: Optional[pulumi.Input['PoolAllocationMode']]):
        pulumi.set(self, "pool_allocation_mode", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The user-specified tags associated with the account.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version v20190801 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""", DeprecationWarning)


class BatchAccount(pulumi.CustomResource):
    warnings.warn("""Version v20190801 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 auto_storage: Optional[pulumi.Input[pulumi.InputType['AutoStorageBasePropertiesArgs']]] = None,
                 key_vault_reference: Optional[pulumi.Input[pulumi.InputType['KeyVaultReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_allocation_mode: Optional[pulumi.Input['PoolAllocationMode']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Contains information about an Azure Batch account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.
        :param pulumi.Input[pulumi.InputType['AutoStorageBasePropertiesArgs']] auto_storage: The properties related to the auto-storage account.
        :param pulumi.Input[pulumi.InputType['KeyVaultReferenceArgs']] key_vault_reference: A reference to the Azure key vault associated with the Batch account.
        :param pulumi.Input[str] location: The region in which to create the account.
        :param pulumi.Input['PoolAllocationMode'] pool_allocation_mode: The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the Batch account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The user-specified tags associated with the account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BatchAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contains information about an Azure Batch account.

        :param str resource_name: The name of the resource.
        :param BatchAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BatchAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 auto_storage: Optional[pulumi.Input[pulumi.InputType['AutoStorageBasePropertiesArgs']]] = None,
                 key_vault_reference: Optional[pulumi.Input[pulumi.InputType['KeyVaultReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_allocation_mode: Optional[pulumi.Input['PoolAllocationMode']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""BatchAccount is deprecated: Version v20190801 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BatchAccountArgs.__new__(BatchAccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["auto_storage"] = auto_storage
            __props__.__dict__["key_vault_reference"] = key_vault_reference
            __props__.__dict__["location"] = location
            __props__.__dict__["pool_allocation_mode"] = pool_allocation_mode
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["account_endpoint"] = None
            __props__.__dict__["active_job_and_job_schedule_quota"] = None
            __props__.__dict__["dedicated_core_quota"] = None
            __props__.__dict__["dedicated_core_quota_per_vm_family"] = None
            __props__.__dict__["dedicated_core_quota_per_vm_family_enforced"] = None
            __props__.__dict__["low_priority_core_quota"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["pool_quota"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:batch:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20151201:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20170101:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20170501:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20170901:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20181201:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20190401:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20200301:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20200501:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20200901:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20210101:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20210601:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20220101:BatchAccount"), pulumi.Alias(type_="azure-native:batch/v20220601:BatchAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BatchAccount, __self__).__init__(
            'azure-native:batch/v20190801:BatchAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BatchAccount':
        """
        Get an existing BatchAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BatchAccountArgs.__new__(BatchAccountArgs)

        __props__.__dict__["account_endpoint"] = None
        __props__.__dict__["active_job_and_job_schedule_quota"] = None
        __props__.__dict__["auto_storage"] = None
        __props__.__dict__["dedicated_core_quota"] = None
        __props__.__dict__["dedicated_core_quota_per_vm_family"] = None
        __props__.__dict__["dedicated_core_quota_per_vm_family_enforced"] = None
        __props__.__dict__["key_vault_reference"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["low_priority_core_quota"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pool_allocation_mode"] = None
        __props__.__dict__["pool_quota"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return BatchAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountEndpoint")
    def account_endpoint(self) -> pulumi.Output[str]:
        """
        The account endpoint used to interact with the Batch service.
        """
        return pulumi.get(self, "account_endpoint")

    @property
    @pulumi.getter(name="activeJobAndJobScheduleQuota")
    def active_job_and_job_schedule_quota(self) -> pulumi.Output[int]:
        return pulumi.get(self, "active_job_and_job_schedule_quota")

    @property
    @pulumi.getter(name="autoStorage")
    def auto_storage(self) -> pulumi.Output['outputs.AutoStoragePropertiesResponse']:
        """
        Contains information about the auto-storage account associated with a Batch account.
        """
        return pulumi.get(self, "auto_storage")

    @property
    @pulumi.getter(name="dedicatedCoreQuota")
    def dedicated_core_quota(self) -> pulumi.Output[int]:
        """
        For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned.
        """
        return pulumi.get(self, "dedicated_core_quota")

    @property
    @pulumi.getter(name="dedicatedCoreQuotaPerVMFamily")
    def dedicated_core_quota_per_vm_family(self) -> pulumi.Output[Sequence['outputs.VirtualMachineFamilyCoreQuotaResponse']]:
        """
        A list of the dedicated core quota per Virtual Machine family for the Batch account. For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned.
        """
        return pulumi.get(self, "dedicated_core_quota_per_vm_family")

    @property
    @pulumi.getter(name="dedicatedCoreQuotaPerVMFamilyEnforced")
    def dedicated_core_quota_per_vm_family_enforced(self) -> pulumi.Output[bool]:
        """
        Batch is transitioning its core quota system for dedicated cores to be enforced per Virtual Machine family. During this transitional phase, the dedicated core quota per Virtual Machine family may not yet be enforced. If this flag is false, dedicated core quota is enforced via the old dedicatedCoreQuota property on the account and does not consider Virtual Machine family. If this flag is true, dedicated core quota is enforced via the dedicatedCoreQuotaPerVMFamily property on the account, and the old dedicatedCoreQuota does not apply.
        """
        return pulumi.get(self, "dedicated_core_quota_per_vm_family_enforced")

    @property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(self) -> pulumi.Output['outputs.KeyVaultReferenceResponse']:
        """
        Identifies the Azure key vault associated with a Batch account.
        """
        return pulumi.get(self, "key_vault_reference")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="lowPriorityCoreQuota")
    def low_priority_core_quota(self) -> pulumi.Output[int]:
        """
        For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned.
        """
        return pulumi.get(self, "low_priority_core_quota")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="poolAllocationMode")
    def pool_allocation_mode(self) -> pulumi.Output[str]:
        """
        The allocation mode for creating pools in the Batch account.
        """
        return pulumi.get(self, "pool_allocation_mode")

    @property
    @pulumi.getter(name="poolQuota")
    def pool_quota(self) -> pulumi.Output[int]:
        return pulumi.get(self, "pool_quota")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

