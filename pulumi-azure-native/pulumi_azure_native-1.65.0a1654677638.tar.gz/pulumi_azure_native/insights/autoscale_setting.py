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

__all__ = ['AutoscaleSettingArgs', 'AutoscaleSetting']

@pulumi.input_type
class AutoscaleSettingArgs:
    def __init__(__self__, *,
                 profiles: pulumi.Input[Sequence[pulumi.Input['AutoscaleProfileArgs']]],
                 resource_group_name: pulumi.Input[str],
                 autoscale_setting_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notifications: Optional[pulumi.Input[Sequence[pulumi.Input['AutoscaleNotificationArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_location: Optional[pulumi.Input[str]] = None,
                 target_resource_uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AutoscaleSetting resource.
        :param pulumi.Input[Sequence[pulumi.Input['AutoscaleProfileArgs']]] profiles: the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] autoscale_setting_name: The autoscale setting name.
        :param pulumi.Input[bool] enabled: the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'true'.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: the name of the autoscale setting.
        :param pulumi.Input[Sequence[pulumi.Input['AutoscaleNotificationArgs']]] notifications: the collection of notifications.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] target_resource_location: the location of the resource that the autoscale setting should be added to.
        :param pulumi.Input[str] target_resource_uri: the resource identifier of the resource that the autoscale setting should be added to.
        """
        pulumi.set(__self__, "profiles", profiles)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if autoscale_setting_name is not None:
            pulumi.set(__self__, "autoscale_setting_name", autoscale_setting_name)
        if enabled is None:
            enabled = True
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notifications is not None:
            pulumi.set(__self__, "notifications", notifications)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_resource_location is not None:
            pulumi.set(__self__, "target_resource_location", target_resource_location)
        if target_resource_uri is not None:
            pulumi.set(__self__, "target_resource_uri", target_resource_uri)

    @property
    @pulumi.getter
    def profiles(self) -> pulumi.Input[Sequence[pulumi.Input['AutoscaleProfileArgs']]]:
        """
        the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified.
        """
        return pulumi.get(self, "profiles")

    @profiles.setter
    def profiles(self, value: pulumi.Input[Sequence[pulumi.Input['AutoscaleProfileArgs']]]):
        pulumi.set(self, "profiles", value)

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
    @pulumi.getter(name="autoscaleSettingName")
    def autoscale_setting_name(self) -> Optional[pulumi.Input[str]]:
        """
        The autoscale setting name.
        """
        return pulumi.get(self, "autoscale_setting_name")

    @autoscale_setting_name.setter
    def autoscale_setting_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "autoscale_setting_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'true'.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        the name of the autoscale setting.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AutoscaleNotificationArgs']]]]:
        """
        the collection of notifications.
        """
        return pulumi.get(self, "notifications")

    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AutoscaleNotificationArgs']]]]):
        pulumi.set(self, "notifications", value)

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

    @property
    @pulumi.getter(name="targetResourceLocation")
    def target_resource_location(self) -> Optional[pulumi.Input[str]]:
        """
        the location of the resource that the autoscale setting should be added to.
        """
        return pulumi.get(self, "target_resource_location")

    @target_resource_location.setter
    def target_resource_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_location", value)

    @property
    @pulumi.getter(name="targetResourceUri")
    def target_resource_uri(self) -> Optional[pulumi.Input[str]]:
        """
        the resource identifier of the resource that the autoscale setting should be added to.
        """
        return pulumi.get(self, "target_resource_uri")

    @target_resource_uri.setter
    def target_resource_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_uri", value)


class AutoscaleSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autoscale_setting_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutoscaleNotificationArgs']]]]] = None,
                 profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutoscaleProfileArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_location: Optional[pulumi.Input[str]] = None,
                 target_resource_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The autoscale setting resource.
        API Version: 2015-04-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] autoscale_setting_name: The autoscale setting name.
        :param pulumi.Input[bool] enabled: the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'true'.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: the name of the autoscale setting.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutoscaleNotificationArgs']]]] notifications: the collection of notifications.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutoscaleProfileArgs']]]] profiles: the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] target_resource_location: the location of the resource that the autoscale setting should be added to.
        :param pulumi.Input[str] target_resource_uri: the resource identifier of the resource that the autoscale setting should be added to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutoscaleSettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The autoscale setting resource.
        API Version: 2015-04-01.

        :param str resource_name: The name of the resource.
        :param AutoscaleSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoscaleSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autoscale_setting_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutoscaleNotificationArgs']]]]] = None,
                 profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutoscaleProfileArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_location: Optional[pulumi.Input[str]] = None,
                 target_resource_uri: Optional[pulumi.Input[str]] = None,
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
            __props__ = AutoscaleSettingArgs.__new__(AutoscaleSettingArgs)

            __props__.__dict__["autoscale_setting_name"] = autoscale_setting_name
            if enabled is None:
                enabled = True
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["notifications"] = notifications
            if profiles is None and not opts.urn:
                raise TypeError("Missing required property 'profiles'")
            __props__.__dict__["profiles"] = profiles
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_resource_location"] = target_resource_location
            __props__.__dict__["target_resource_uri"] = target_resource_uri
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights/v20140401:AutoscaleSetting"), pulumi.Alias(type_="azure-native:insights/v20150401:AutoscaleSetting"), pulumi.Alias(type_="azure-native:insights/v20210501preview:AutoscaleSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AutoscaleSetting, __self__).__init__(
            'azure-native:insights:AutoscaleSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AutoscaleSetting':
        """
        Get an existing AutoscaleSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AutoscaleSettingArgs.__new__(AutoscaleSettingArgs)

        __props__.__dict__["enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notifications"] = None
        __props__.__dict__["profiles"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_resource_location"] = None
        __props__.__dict__["target_resource_uri"] = None
        __props__.__dict__["type"] = None
        return AutoscaleSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'true'.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notifications(self) -> pulumi.Output[Optional[Sequence['outputs.AutoscaleNotificationResponse']]]:
        """
        the collection of notifications.
        """
        return pulumi.get(self, "notifications")

    @property
    @pulumi.getter
    def profiles(self) -> pulumi.Output[Sequence['outputs.AutoscaleProfileResponse']]:
        """
        the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified.
        """
        return pulumi.get(self, "profiles")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceLocation")
    def target_resource_location(self) -> pulumi.Output[Optional[str]]:
        """
        the location of the resource that the autoscale setting should be added to.
        """
        return pulumi.get(self, "target_resource_location")

    @property
    @pulumi.getter(name="targetResourceUri")
    def target_resource_uri(self) -> pulumi.Output[Optional[str]]:
        """
        the resource identifier of the resource that the autoscale setting should be added to.
        """
        return pulumi.get(self, "target_resource_uri")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

