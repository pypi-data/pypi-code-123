# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ApplicationReferenceDataSourceArgs', 'ApplicationReferenceDataSource']

@pulumi.input_type
class ApplicationReferenceDataSourceArgs:
    def __init__(__self__, *,
                 application_name: pulumi.Input[str],
                 reference_data_source: pulumi.Input['ApplicationReferenceDataSourceReferenceDataSourceArgs']):
        """
        The set of arguments for constructing a ApplicationReferenceDataSource resource.
        """
        pulumi.set(__self__, "application_name", application_name)
        pulumi.set(__self__, "reference_data_source", reference_data_source)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_name", value)

    @property
    @pulumi.getter(name="referenceDataSource")
    def reference_data_source(self) -> pulumi.Input['ApplicationReferenceDataSourceReferenceDataSourceArgs']:
        return pulumi.get(self, "reference_data_source")

    @reference_data_source.setter
    def reference_data_source(self, value: pulumi.Input['ApplicationReferenceDataSourceReferenceDataSourceArgs']):
        pulumi.set(self, "reference_data_source", value)


warnings.warn("""ApplicationReferenceDataSource is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ApplicationReferenceDataSource(pulumi.CustomResource):
    warnings.warn("""ApplicationReferenceDataSource is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 reference_data_source: Optional[pulumi.Input[pulumi.InputType['ApplicationReferenceDataSourceReferenceDataSourceArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationReferenceDataSourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource

        :param str resource_name: The name of the resource.
        :param ApplicationReferenceDataSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationReferenceDataSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 reference_data_source: Optional[pulumi.Input[pulumi.InputType['ApplicationReferenceDataSourceReferenceDataSourceArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ApplicationReferenceDataSource is deprecated: ApplicationReferenceDataSource is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationReferenceDataSourceArgs.__new__(ApplicationReferenceDataSourceArgs)

            if application_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_name'")
            __props__.__dict__["application_name"] = application_name
            if reference_data_source is None and not opts.urn:
                raise TypeError("Missing required property 'reference_data_source'")
            __props__.__dict__["reference_data_source"] = reference_data_source
        super(ApplicationReferenceDataSource, __self__).__init__(
            'aws-native:kinesisanalyticsv2:ApplicationReferenceDataSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationReferenceDataSource':
        """
        Get an existing ApplicationReferenceDataSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationReferenceDataSourceArgs.__new__(ApplicationReferenceDataSourceArgs)

        __props__.__dict__["application_name"] = None
        __props__.__dict__["reference_data_source"] = None
        return ApplicationReferenceDataSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter(name="referenceDataSource")
    def reference_data_source(self) -> pulumi.Output['outputs.ApplicationReferenceDataSourceReferenceDataSource']:
        return pulumi.get(self, "reference_data_source")

