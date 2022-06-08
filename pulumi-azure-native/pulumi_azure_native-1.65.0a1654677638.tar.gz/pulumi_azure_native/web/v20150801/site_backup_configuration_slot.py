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

__all__ = ['SiteBackupConfigurationSlotArgs', 'SiteBackupConfigurationSlot']

@pulumi.input_type
class SiteBackupConfigurationSlotArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 slot: pulumi.Input[str],
                 type: pulumi.Input[str],
                 backup_schedule: Optional[pulumi.Input['BackupScheduleArgs']] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseBackupSettingArgs']]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 storage_account_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SiteBackupConfigurationSlot resource.
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[str] slot: Name of web app slot. If not specified then will default to production slot.
        :param pulumi.Input[str] type: Resource type
        :param pulumi.Input['BackupScheduleArgs'] backup_schedule: Schedule for the backup if it is executed periodically
        :param pulumi.Input[Sequence[pulumi.Input['DatabaseBackupSettingArgs']]] databases: Databases included in the backup
        :param pulumi.Input[bool] enabled: True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] storage_account_url: SAS URL to the container
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "slot", slot)
        pulumi.set(__self__, "type", type)
        if backup_schedule is not None:
            pulumi.set(__self__, "backup_schedule", backup_schedule)
        if databases is not None:
            pulumi.set(__self__, "databases", databases)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if storage_account_url is not None:
            pulumi.set(__self__, "storage_account_url", storage_account_url)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def slot(self) -> pulumi.Input[str]:
        """
        Name of web app slot. If not specified then will default to production slot.
        """
        return pulumi.get(self, "slot")

    @slot.setter
    def slot(self, value: pulumi.Input[str]):
        pulumi.set(self, "slot", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> Optional[pulumi.Input['BackupScheduleArgs']]:
        """
        Schedule for the backup if it is executed periodically
        """
        return pulumi.get(self, "backup_schedule")

    @backup_schedule.setter
    def backup_schedule(self, value: Optional[pulumi.Input['BackupScheduleArgs']]):
        pulumi.set(self, "backup_schedule", value)

    @property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseBackupSettingArgs']]]]:
        """
        Databases included in the backup
        """
        return pulumi.get(self, "databases")

    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseBackupSettingArgs']]]]):
        pulumi.set(self, "databases", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> Optional[pulumi.Input[str]]:
        """
        SAS URL to the container
        """
        return pulumi.get(self, "storage_account_url")

    @storage_account_url.setter
    def storage_account_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_url", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version v20150801 will be removed in the next major version of the provider. Upgrade to version v20150801preview or later.""", DeprecationWarning)


class SiteBackupConfigurationSlot(pulumi.CustomResource):
    warnings.warn("""Version v20150801 will be removed in the next major version of the provider. Upgrade to version v20150801preview or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_schedule: Optional[pulumi.Input[pulumi.InputType['BackupScheduleArgs']]] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseBackupSettingArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
                 storage_account_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Description of a backup which will be performed

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BackupScheduleArgs']] backup_schedule: Schedule for the backup if it is executed periodically
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseBackupSettingArgs']]]] databases: Databases included in the backup
        :param pulumi.Input[bool] enabled: True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[str] slot: Name of web app slot. If not specified then will default to production slot.
        :param pulumi.Input[str] storage_account_url: SAS URL to the container
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SiteBackupConfigurationSlotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of a backup which will be performed

        :param str resource_name: The name of the resource.
        :param SiteBackupConfigurationSlotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SiteBackupConfigurationSlotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_schedule: Optional[pulumi.Input[pulumi.InputType['BackupScheduleArgs']]] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseBackupSettingArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
                 storage_account_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SiteBackupConfigurationSlot is deprecated: Version v20150801 will be removed in the next major version of the provider. Upgrade to version v20150801preview or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SiteBackupConfigurationSlotArgs.__new__(SiteBackupConfigurationSlotArgs)

            __props__.__dict__["backup_schedule"] = backup_schedule
            __props__.__dict__["databases"] = databases
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if slot is None and not opts.urn:
                raise TypeError("Missing required property 'slot'")
            __props__.__dict__["slot"] = slot
            __props__.__dict__["storage_account_url"] = storage_account_url
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20160801:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20180201:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20181101:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20190801:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20200601:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20200901:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20201001:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20201201:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20210101:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20210115:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20210201:SiteBackupConfigurationSlot"), pulumi.Alias(type_="azure-native:web/v20210301:SiteBackupConfigurationSlot")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SiteBackupConfigurationSlot, __self__).__init__(
            'azure-native:web/v20150801:SiteBackupConfigurationSlot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SiteBackupConfigurationSlot':
        """
        Get an existing SiteBackupConfigurationSlot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SiteBackupConfigurationSlotArgs.__new__(SiteBackupConfigurationSlotArgs)

        __props__.__dict__["backup_schedule"] = None
        __props__.__dict__["databases"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["storage_account_url"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SiteBackupConfigurationSlot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> pulumi.Output[Optional['outputs.BackupScheduleResponse']]:
        """
        Schedule for the backup if it is executed periodically
        """
        return pulumi.get(self, "backup_schedule")

    @property
    @pulumi.getter
    def databases(self) -> pulumi.Output[Optional[Sequence['outputs.DatabaseBackupSettingResponse']]]:
        """
        Databases included in the backup
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> pulumi.Output[Optional[str]]:
        """
        SAS URL to the container
        """
        return pulumi.get(self, "storage_account_url")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

