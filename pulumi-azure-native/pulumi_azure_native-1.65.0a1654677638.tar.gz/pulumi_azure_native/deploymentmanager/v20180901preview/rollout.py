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

__all__ = ['RolloutArgs', 'Rollout']

@pulumi.input_type
class RolloutArgs:
    def __init__(__self__, *,
                 build_version: pulumi.Input[str],
                 identity: pulumi.Input['IdentityArgs'],
                 resource_group_name: pulumi.Input[str],
                 step_groups: pulumi.Input[Sequence[pulumi.Input['StepArgs']]],
                 target_service_topology_id: pulumi.Input[str],
                 artifact_source_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 rollout_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Rollout resource.
        :param pulumi.Input[str] build_version: The version of the build being deployed.
        :param pulumi.Input['IdentityArgs'] identity: Identity for the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['StepArgs']]] step_groups: The list of step groups that define the orchestration.
        :param pulumi.Input[str] target_service_topology_id: The resource Id of the service topology from which service units are being referenced in step groups to be deployed.
        :param pulumi.Input[str] artifact_source_id: The reference to the artifact source resource Id where the payload is located.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] rollout_name: The rollout name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "build_version", build_version)
        pulumi.set(__self__, "identity", identity)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "step_groups", step_groups)
        pulumi.set(__self__, "target_service_topology_id", target_service_topology_id)
        if artifact_source_id is not None:
            pulumi.set(__self__, "artifact_source_id", artifact_source_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if rollout_name is not None:
            pulumi.set(__self__, "rollout_name", rollout_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="buildVersion")
    def build_version(self) -> pulumi.Input[str]:
        """
        The version of the build being deployed.
        """
        return pulumi.get(self, "build_version")

    @build_version.setter
    def build_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "build_version", value)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Input['IdentityArgs']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: pulumi.Input['IdentityArgs']):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter(name="stepGroups")
    def step_groups(self) -> pulumi.Input[Sequence[pulumi.Input['StepArgs']]]:
        """
        The list of step groups that define the orchestration.
        """
        return pulumi.get(self, "step_groups")

    @step_groups.setter
    def step_groups(self, value: pulumi.Input[Sequence[pulumi.Input['StepArgs']]]):
        pulumi.set(self, "step_groups", value)

    @property
    @pulumi.getter(name="targetServiceTopologyId")
    def target_service_topology_id(self) -> pulumi.Input[str]:
        """
        The resource Id of the service topology from which service units are being referenced in step groups to be deployed.
        """
        return pulumi.get(self, "target_service_topology_id")

    @target_service_topology_id.setter
    def target_service_topology_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_service_topology_id", value)

    @property
    @pulumi.getter(name="artifactSourceId")
    def artifact_source_id(self) -> Optional[pulumi.Input[str]]:
        """
        The reference to the artifact source resource Id where the payload is located.
        """
        return pulumi.get(self, "artifact_source_id")

    @artifact_source_id.setter
    def artifact_source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "artifact_source_id", value)

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
    @pulumi.getter(name="rolloutName")
    def rollout_name(self) -> Optional[pulumi.Input[str]]:
        """
        The rollout name.
        """
        return pulumi.get(self, "rollout_name")

    @rollout_name.setter
    def rollout_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rollout_name", value)

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


warnings.warn("""Version v20180901preview will be removed in the next major version of the provider. Upgrade to version v20191101preview or later.""", DeprecationWarning)


class Rollout(pulumi.CustomResource):
    warnings.warn("""Version v20180901preview will be removed in the next major version of the provider. Upgrade to version v20191101preview or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_source_id: Optional[pulumi.Input[str]] = None,
                 build_version: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rollout_name: Optional[pulumi.Input[str]] = None,
                 step_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StepArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_service_topology_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the PUT rollout request body.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] artifact_source_id: The reference to the artifact source resource Id where the payload is located.
        :param pulumi.Input[str] build_version: The version of the build being deployed.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: Identity for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] rollout_name: The rollout name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StepArgs']]]] step_groups: The list of step groups that define the orchestration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] target_service_topology_id: The resource Id of the service topology from which service units are being referenced in step groups to be deployed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RolloutArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the PUT rollout request body.

        :param str resource_name: The name of the resource.
        :param RolloutArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RolloutArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_source_id: Optional[pulumi.Input[str]] = None,
                 build_version: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rollout_name: Optional[pulumi.Input[str]] = None,
                 step_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StepArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_service_topology_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Rollout is deprecated: Version v20180901preview will be removed in the next major version of the provider. Upgrade to version v20191101preview or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RolloutArgs.__new__(RolloutArgs)

            __props__.__dict__["artifact_source_id"] = artifact_source_id
            if build_version is None and not opts.urn:
                raise TypeError("Missing required property 'build_version'")
            __props__.__dict__["build_version"] = build_version
            if identity is None and not opts.urn:
                raise TypeError("Missing required property 'identity'")
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rollout_name"] = rollout_name
            if step_groups is None and not opts.urn:
                raise TypeError("Missing required property 'step_groups'")
            __props__.__dict__["step_groups"] = step_groups
            __props__.__dict__["tags"] = tags
            if target_service_topology_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_service_topology_id'")
            __props__.__dict__["target_service_topology_id"] = target_service_topology_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:deploymentmanager:Rollout"), pulumi.Alias(type_="azure-native:deploymentmanager/v20191101preview:Rollout")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Rollout, __self__).__init__(
            'azure-native:deploymentmanager/v20180901preview:Rollout',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Rollout':
        """
        Get an existing Rollout resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RolloutArgs.__new__(RolloutArgs)

        __props__.__dict__["artifact_source_id"] = None
        __props__.__dict__["build_version"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["step_groups"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_service_topology_id"] = None
        __props__.__dict__["type"] = None
        return Rollout(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="artifactSourceId")
    def artifact_source_id(self) -> pulumi.Output[Optional[str]]:
        """
        The reference to the artifact source resource Id where the payload is located.
        """
        return pulumi.get(self, "artifact_source_id")

    @property
    @pulumi.getter(name="buildVersion")
    def build_version(self) -> pulumi.Output[str]:
        """
        The version of the build being deployed.
        """
        return pulumi.get(self, "build_version")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.IdentityResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

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
    @pulumi.getter(name="stepGroups")
    def step_groups(self) -> pulumi.Output[Sequence['outputs.StepResponse']]:
        """
        The list of step groups that define the orchestration.
        """
        return pulumi.get(self, "step_groups")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetServiceTopologyId")
    def target_service_topology_id(self) -> pulumi.Output[str]:
        """
        The resource Id of the service topology from which service units are being referenced in step groups to be deployed.
        """
        return pulumi.get(self, "target_service_topology_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

