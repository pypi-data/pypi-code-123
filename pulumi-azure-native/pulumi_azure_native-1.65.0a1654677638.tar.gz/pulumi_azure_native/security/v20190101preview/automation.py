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

__all__ = ['AutomationArgs', 'Automation']

@pulumi.input_type
class AutomationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AutomationActionEventHubArgs', 'AutomationActionLogicAppArgs', 'AutomationActionWorkspaceArgs']]]]] = None,
                 automation_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationScopeArgs']]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationSourceArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Automation resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[Union['AutomationActionEventHubArgs', 'AutomationActionLogicAppArgs', 'AutomationActionWorkspaceArgs']]]] actions: A collection of the actions which are triggered if all the configured rules evaluations, within at least one rule set, are true.
        :param pulumi.Input[str] automation_name: The security automation name.
        :param pulumi.Input[str] description: The security automation description.
        :param pulumi.Input[bool] is_enabled: Indicates whether the security automation is enabled.
        :param pulumi.Input[str] kind: Kind of the resource
        :param pulumi.Input[str] location: Location where the resource is stored
        :param pulumi.Input[Sequence[pulumi.Input['AutomationScopeArgs']]] scopes: A collection of scopes on which the security automations logic is applied. Supported scopes are the subscription itself or a resource group under that subscription. The automation will only apply on defined scopes.
        :param pulumi.Input[Sequence[pulumi.Input['AutomationSourceArgs']]] sources: A collection of the source event types which evaluate the security automation set of rules.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A list of key value pairs that describe the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if automation_name is not None:
            pulumi.set(__self__, "automation_name", automation_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['AutomationActionEventHubArgs', 'AutomationActionLogicAppArgs', 'AutomationActionWorkspaceArgs']]]]]:
        """
        A collection of the actions which are triggered if all the configured rules evaluations, within at least one rule set, are true.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AutomationActionEventHubArgs', 'AutomationActionLogicAppArgs', 'AutomationActionWorkspaceArgs']]]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter(name="automationName")
    def automation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The security automation name.
        """
        return pulumi.get(self, "automation_name")

    @automation_name.setter
    def automation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "automation_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The security automation description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the security automation is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AutomationScopeArgs']]]]:
        """
        A collection of scopes on which the security automations logic is applied. Supported scopes are the subscription itself or a resource group under that subscription. The automation will only apply on defined scopes.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationScopeArgs']]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AutomationSourceArgs']]]]:
        """
        A collection of the source event types which evaluate the security automation set of rules.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationSourceArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A list of key value pairs that describe the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Automation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AutomationActionEventHubArgs'], pulumi.InputType['AutomationActionLogicAppArgs'], pulumi.InputType['AutomationActionWorkspaceArgs']]]]]] = None,
                 automation_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutomationScopeArgs']]]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutomationSourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The security automation resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AutomationActionEventHubArgs'], pulumi.InputType['AutomationActionLogicAppArgs'], pulumi.InputType['AutomationActionWorkspaceArgs']]]]] actions: A collection of the actions which are triggered if all the configured rules evaluations, within at least one rule set, are true.
        :param pulumi.Input[str] automation_name: The security automation name.
        :param pulumi.Input[str] description: The security automation description.
        :param pulumi.Input[bool] is_enabled: Indicates whether the security automation is enabled.
        :param pulumi.Input[str] kind: Kind of the resource
        :param pulumi.Input[str] location: Location where the resource is stored
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutomationScopeArgs']]]] scopes: A collection of scopes on which the security automations logic is applied. Supported scopes are the subscription itself or a resource group under that subscription. The automation will only apply on defined scopes.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutomationSourceArgs']]]] sources: A collection of the source event types which evaluate the security automation set of rules.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A list of key value pairs that describe the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutomationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The security automation resource.

        :param str resource_name: The name of the resource.
        :param AutomationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutomationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AutomationActionEventHubArgs'], pulumi.InputType['AutomationActionLogicAppArgs'], pulumi.InputType['AutomationActionWorkspaceArgs']]]]]] = None,
                 automation_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutomationScopeArgs']]]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AutomationSourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = AutomationArgs.__new__(AutomationArgs)

            __props__.__dict__["actions"] = actions
            __props__.__dict__["automation_name"] = automation_name
            __props__.__dict__["description"] = description
            __props__.__dict__["is_enabled"] = is_enabled
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["sources"] = sources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:Automation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Automation, __self__).__init__(
            'azure-native:security/v20190101preview:Automation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Automation':
        """
        Get an existing Automation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AutomationArgs.__new__(AutomationArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["sources"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Automation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        A collection of the actions which are triggered if all the configured rules evaluations, within at least one rule set, are true.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The security automation description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Entity tag is used for comparing two or more entities from the same requested resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the security automation is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence['outputs.AutomationScopeResponse']]]:
        """
        A collection of scopes on which the security automations logic is applied. Supported scopes are the subscription itself or a resource group under that subscription. The automation will only apply on defined scopes.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence['outputs.AutomationSourceResponse']]]:
        """
        A collection of the source event types which evaluate the security automation set of rules.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A list of key value pairs that describe the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

