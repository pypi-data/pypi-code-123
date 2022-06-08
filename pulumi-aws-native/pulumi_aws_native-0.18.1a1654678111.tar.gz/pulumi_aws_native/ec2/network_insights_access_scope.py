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

__all__ = ['NetworkInsightsAccessScopeArgs', 'NetworkInsightsAccessScope']

@pulumi.input_type
class NetworkInsightsAccessScopeArgs:
    def __init__(__self__, *,
                 exclude_paths: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]] = None,
                 match_paths: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeTagArgs']]]] = None):
        """
        The set of arguments for constructing a NetworkInsightsAccessScope resource.
        """
        if exclude_paths is not None:
            pulumi.set(__self__, "exclude_paths", exclude_paths)
        if match_paths is not None:
            pulumi.set(__self__, "match_paths", match_paths)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="excludePaths")
    def exclude_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]:
        return pulumi.get(self, "exclude_paths")

    @exclude_paths.setter
    def exclude_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]):
        pulumi.set(self, "exclude_paths", value)

    @property
    @pulumi.getter(name="matchPaths")
    def match_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]:
        return pulumi.get(self, "match_paths")

    @match_paths.setter
    def match_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]):
        pulumi.set(self, "match_paths", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAccessScopeTagArgs']]]]):
        pulumi.set(self, "tags", value)


class NetworkInsightsAccessScope(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exclude_paths: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]] = None,
                 match_paths: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::EC2::NetworkInsightsAccessScope

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[NetworkInsightsAccessScopeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::EC2::NetworkInsightsAccessScope

        :param str resource_name: The name of the resource.
        :param NetworkInsightsAccessScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInsightsAccessScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exclude_paths: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]] = None,
                 match_paths: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeAccessScopePathRequestArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAccessScopeTagArgs']]]]] = None,
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
            __props__ = NetworkInsightsAccessScopeArgs.__new__(NetworkInsightsAccessScopeArgs)

            __props__.__dict__["exclude_paths"] = exclude_paths
            __props__.__dict__["match_paths"] = match_paths
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_date"] = None
            __props__.__dict__["network_insights_access_scope_arn"] = None
            __props__.__dict__["network_insights_access_scope_id"] = None
            __props__.__dict__["updated_date"] = None
        super(NetworkInsightsAccessScope, __self__).__init__(
            'aws-native:ec2:NetworkInsightsAccessScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInsightsAccessScope':
        """
        Get an existing NetworkInsightsAccessScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInsightsAccessScopeArgs.__new__(NetworkInsightsAccessScopeArgs)

        __props__.__dict__["created_date"] = None
        __props__.__dict__["exclude_paths"] = None
        __props__.__dict__["match_paths"] = None
        __props__.__dict__["network_insights_access_scope_arn"] = None
        __props__.__dict__["network_insights_access_scope_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["updated_date"] = None
        return NetworkInsightsAccessScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="excludePaths")
    def exclude_paths(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInsightsAccessScopeAccessScopePathRequest']]]:
        return pulumi.get(self, "exclude_paths")

    @property
    @pulumi.getter(name="matchPaths")
    def match_paths(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInsightsAccessScopeAccessScopePathRequest']]]:
        return pulumi.get(self, "match_paths")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeArn")
    def network_insights_access_scope_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_access_scope_arn")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeId")
    def network_insights_access_scope_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_access_scope_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInsightsAccessScopeTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedDate")
    def updated_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "updated_date")

