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

__all__ = ['ScalingPlanArgs', 'ScalingPlan']

@pulumi.input_type
class ScalingPlanArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 exclusion_tag: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pool_references: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingHostPoolReferenceArgs']]]] = None,
                 host_pool_type: Optional[pulumi.Input[Union[str, 'HostPoolType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 scaling_plan_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingScheduleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScalingPlan resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] description: Description of scaling plan.
        :param pulumi.Input[str] exclusion_tag: Exclusion tag for scaling plan.
        :param pulumi.Input[str] friendly_name: User friendly name of scaling plan.
        :param pulumi.Input[Sequence[pulumi.Input['ScalingHostPoolReferenceArgs']]] host_pool_references: List of ScalingHostPoolReference definitions.
        :param pulumi.Input[Union[str, 'HostPoolType']] host_pool_type: HostPool type for scaling plan.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] scaling_plan_name: The name of the scaling plan.
        :param pulumi.Input[Sequence[pulumi.Input['ScalingScheduleArgs']]] schedules: List of ScalingSchedule definitions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] time_zone: Timezone of the scaling plan.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if exclusion_tag is not None:
            pulumi.set(__self__, "exclusion_tag", exclusion_tag)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if host_pool_references is not None:
            pulumi.set(__self__, "host_pool_references", host_pool_references)
        if host_pool_type is not None:
            pulumi.set(__self__, "host_pool_type", host_pool_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if scaling_plan_name is not None:
            pulumi.set(__self__, "scaling_plan_name", scaling_plan_name)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of scaling plan.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> Optional[pulumi.Input[str]]:
        """
        Exclusion tag for scaling plan.
        """
        return pulumi.get(self, "exclusion_tag")

    @exclusion_tag.setter
    def exclusion_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclusion_tag", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        User friendly name of scaling plan.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="hostPoolReferences")
    def host_pool_references(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingHostPoolReferenceArgs']]]]:
        """
        List of ScalingHostPoolReference definitions.
        """
        return pulumi.get(self, "host_pool_references")

    @host_pool_references.setter
    def host_pool_references(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingHostPoolReferenceArgs']]]]):
        pulumi.set(self, "host_pool_references", value)

    @property
    @pulumi.getter(name="hostPoolType")
    def host_pool_type(self) -> Optional[pulumi.Input[Union[str, 'HostPoolType']]]:
        """
        HostPool type for scaling plan.
        """
        return pulumi.get(self, "host_pool_type")

    @host_pool_type.setter
    def host_pool_type(self, value: Optional[pulumi.Input[Union[str, 'HostPoolType']]]):
        pulumi.set(self, "host_pool_type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="scalingPlanName")
    def scaling_plan_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the scaling plan.
        """
        return pulumi.get(self, "scaling_plan_name")

    @scaling_plan_name.setter
    def scaling_plan_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scaling_plan_name", value)

    @property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingScheduleArgs']]]]:
        """
        List of ScalingSchedule definitions.
        """
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingScheduleArgs']]]]):
        pulumi.set(self, "schedules", value)

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

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Timezone of the scaling plan.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


warnings.warn("""Version v20201110preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""", DeprecationWarning)


class ScalingPlan(pulumi.CustomResource):
    warnings.warn("""Version v20201110preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exclusion_tag: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pool_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingHostPoolReferenceArgs']]]]] = None,
                 host_pool_type: Optional[pulumi.Input[Union[str, 'HostPoolType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scaling_plan_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingScheduleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a scaling plan definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of scaling plan.
        :param pulumi.Input[str] exclusion_tag: Exclusion tag for scaling plan.
        :param pulumi.Input[str] friendly_name: User friendly name of scaling plan.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingHostPoolReferenceArgs']]]] host_pool_references: List of ScalingHostPoolReference definitions.
        :param pulumi.Input[Union[str, 'HostPoolType']] host_pool_type: HostPool type for scaling plan.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] scaling_plan_name: The name of the scaling plan.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingScheduleArgs']]]] schedules: List of ScalingSchedule definitions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] time_zone: Timezone of the scaling plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScalingPlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a scaling plan definition.

        :param str resource_name: The name of the resource.
        :param ScalingPlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScalingPlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exclusion_tag: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pool_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingHostPoolReferenceArgs']]]]] = None,
                 host_pool_type: Optional[pulumi.Input[Union[str, 'HostPoolType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scaling_plan_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingScheduleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ScalingPlan is deprecated: Version v20201110preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScalingPlanArgs.__new__(ScalingPlanArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["exclusion_tag"] = exclusion_tag
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["host_pool_references"] = host_pool_references
            __props__.__dict__["host_pool_type"] = host_pool_type
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scaling_plan_name"] = scaling_plan_name
            __props__.__dict__["schedules"] = schedules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["time_zone"] = time_zone
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:desktopvirtualization:ScalingPlan"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210114preview:ScalingPlan"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210201preview:ScalingPlan"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210309preview:ScalingPlan"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210401preview:ScalingPlan"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210712:ScalingPlan"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210903preview:ScalingPlan"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20220210preview:ScalingPlan")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScalingPlan, __self__).__init__(
            'azure-native:desktopvirtualization/v20201110preview:ScalingPlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScalingPlan':
        """
        Get an existing ScalingPlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScalingPlanArgs.__new__(ScalingPlanArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["exclusion_tag"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["host_pool_references"] = None
        __props__.__dict__["host_pool_type"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schedules"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_zone"] = None
        __props__.__dict__["type"] = None
        return ScalingPlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of scaling plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> pulumi.Output[Optional[str]]:
        """
        Exclusion tag for scaling plan.
        """
        return pulumi.get(self, "exclusion_tag")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        User friendly name of scaling plan.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPoolReferences")
    def host_pool_references(self) -> pulumi.Output[Optional[Sequence['outputs.ScalingHostPoolReferenceResponse']]]:
        """
        List of ScalingHostPoolReference definitions.
        """
        return pulumi.get(self, "host_pool_references")

    @property
    @pulumi.getter(name="hostPoolType")
    def host_pool_type(self) -> pulumi.Output[Optional[str]]:
        """
        HostPool type for scaling plan.
        """
        return pulumi.get(self, "host_pool_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Output[Optional[Sequence['outputs.ScalingScheduleResponse']]]:
        """
        List of ScalingSchedule definitions.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Timezone of the scaling plan.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

