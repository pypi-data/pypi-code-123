# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['PublisherArgs', 'Publisher']

@pulumi.input_type
class PublisherArgs:
    def __init__(__self__, *,
                 accept_terms_and_conditions: pulumi.Input[bool],
                 connection_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Publisher resource.
        :param pulumi.Input[bool] accept_terms_and_conditions: Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf
        :param pulumi.Input[str] connection_arn: If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.
        """
        pulumi.set(__self__, "accept_terms_and_conditions", accept_terms_and_conditions)
        if connection_arn is not None:
            pulumi.set(__self__, "connection_arn", connection_arn)

    @property
    @pulumi.getter(name="acceptTermsAndConditions")
    def accept_terms_and_conditions(self) -> pulumi.Input[bool]:
        """
        Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf
        """
        return pulumi.get(self, "accept_terms_and_conditions")

    @accept_terms_and_conditions.setter
    def accept_terms_and_conditions(self, value: pulumi.Input[bool]):
        pulumi.set(self, "accept_terms_and_conditions", value)

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> Optional[pulumi.Input[str]]:
        """
        If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.
        """
        return pulumi.get(self, "connection_arn")

    @connection_arn.setter
    def connection_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_arn", value)


class Publisher(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_terms_and_conditions: Optional[pulumi.Input[bool]] = None,
                 connection_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Register as a publisher in the CloudFormation Registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accept_terms_and_conditions: Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf
        :param pulumi.Input[str] connection_arn: If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PublisherArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Register as a publisher in the CloudFormation Registry.

        :param str resource_name: The name of the resource.
        :param PublisherArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublisherArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_terms_and_conditions: Optional[pulumi.Input[bool]] = None,
                 connection_arn: Optional[pulumi.Input[str]] = None,
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
            __props__ = PublisherArgs.__new__(PublisherArgs)

            if accept_terms_and_conditions is None and not opts.urn:
                raise TypeError("Missing required property 'accept_terms_and_conditions'")
            __props__.__dict__["accept_terms_and_conditions"] = accept_terms_and_conditions
            __props__.__dict__["connection_arn"] = connection_arn
            __props__.__dict__["identity_provider"] = None
            __props__.__dict__["publisher_id"] = None
            __props__.__dict__["publisher_profile"] = None
            __props__.__dict__["publisher_status"] = None
        super(Publisher, __self__).__init__(
            'aws-native:cloudformation:Publisher',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Publisher':
        """
        Get an existing Publisher resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PublisherArgs.__new__(PublisherArgs)

        __props__.__dict__["accept_terms_and_conditions"] = None
        __props__.__dict__["connection_arn"] = None
        __props__.__dict__["identity_provider"] = None
        __props__.__dict__["publisher_id"] = None
        __props__.__dict__["publisher_profile"] = None
        __props__.__dict__["publisher_status"] = None
        return Publisher(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptTermsAndConditions")
    def accept_terms_and_conditions(self) -> pulumi.Output[bool]:
        """
        Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf
        """
        return pulumi.get(self, "accept_terms_and_conditions")

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Output[Optional[str]]:
        """
        If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.
        """
        return pulumi.get(self, "connection_arn")

    @property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> pulumi.Output['PublisherIdentityProvider']:
        """
        The type of account used as the identity provider when registering this publisher with CloudFormation.
        """
        return pulumi.get(self, "identity_provider")

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> pulumi.Output[str]:
        """
        The publisher id assigned by CloudFormation for publishing in this region.
        """
        return pulumi.get(self, "publisher_id")

    @property
    @pulumi.getter(name="publisherProfile")
    def publisher_profile(self) -> pulumi.Output[str]:
        """
        The URL to the publisher's profile with the identity provider.
        """
        return pulumi.get(self, "publisher_profile")

    @property
    @pulumi.getter(name="publisherStatus")
    def publisher_status(self) -> pulumi.Output['PublisherStatus']:
        """
        Whether the publisher is verified.
        """
        return pulumi.get(self, "publisher_status")

