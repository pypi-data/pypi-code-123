# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['BucketOwnershipControlsArgs', 'BucketOwnershipControls']

@pulumi.input_type
class BucketOwnershipControlsArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 rule: pulumi.Input['BucketOwnershipControlsRuleArgs']):
        """
        The set of arguments for constructing a BucketOwnershipControls resource.
        :param pulumi.Input[str] bucket: The name of the bucket that you want to associate this access point with.
        :param pulumi.Input['BucketOwnershipControlsRuleArgs'] rule: Configuration block(s) with Ownership Controls rules. Detailed below.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "rule", rule)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket that you want to associate this access point with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def rule(self) -> pulumi.Input['BucketOwnershipControlsRuleArgs']:
        """
        Configuration block(s) with Ownership Controls rules. Detailed below.
        """
        return pulumi.get(self, "rule")

    @rule.setter
    def rule(self, value: pulumi.Input['BucketOwnershipControlsRuleArgs']):
        pulumi.set(self, "rule", value)


@pulumi.input_type
class _BucketOwnershipControlsState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 rule: Optional[pulumi.Input['BucketOwnershipControlsRuleArgs']] = None):
        """
        Input properties used for looking up and filtering BucketOwnershipControls resources.
        :param pulumi.Input[str] bucket: The name of the bucket that you want to associate this access point with.
        :param pulumi.Input['BucketOwnershipControlsRuleArgs'] rule: Configuration block(s) with Ownership Controls rules. Detailed below.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if rule is not None:
            pulumi.set(__self__, "rule", rule)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket that you want to associate this access point with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input['BucketOwnershipControlsRuleArgs']]:
        """
        Configuration block(s) with Ownership Controls rules. Detailed below.
        """
        return pulumi.get(self, "rule")

    @rule.setter
    def rule(self, value: Optional[pulumi.Input['BucketOwnershipControlsRuleArgs']]):
        pulumi.set(self, "rule", value)


class BucketOwnershipControls(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 rule: Optional[pulumi.Input[pulumi.InputType['BucketOwnershipControlsRuleArgs']]] = None,
                 __props__=None):
        """
        Provides a resource to manage S3 Bucket Ownership Controls. For more information, see the [S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2")
        example_bucket_ownership_controls = aws.s3.BucketOwnershipControls("exampleBucketOwnershipControls",
            bucket=example_bucket_v2.id,
            rule=aws.s3.BucketOwnershipControlsRuleArgs(
                object_ownership="BucketOwnerPreferred",
            ))
        ```

        ## Import

        S3 Bucket Ownership Controls can be imported using S3 Bucket name, e.g.,

        ```sh
         $ pulumi import aws:s3/bucketOwnershipControls:BucketOwnershipControls example my-bucket
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket that you want to associate this access point with.
        :param pulumi.Input[pulumi.InputType['BucketOwnershipControlsRuleArgs']] rule: Configuration block(s) with Ownership Controls rules. Detailed below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketOwnershipControlsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage S3 Bucket Ownership Controls. For more information, see the [S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2")
        example_bucket_ownership_controls = aws.s3.BucketOwnershipControls("exampleBucketOwnershipControls",
            bucket=example_bucket_v2.id,
            rule=aws.s3.BucketOwnershipControlsRuleArgs(
                object_ownership="BucketOwnerPreferred",
            ))
        ```

        ## Import

        S3 Bucket Ownership Controls can be imported using S3 Bucket name, e.g.,

        ```sh
         $ pulumi import aws:s3/bucketOwnershipControls:BucketOwnershipControls example my-bucket
        ```

        :param str resource_name: The name of the resource.
        :param BucketOwnershipControlsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketOwnershipControlsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 rule: Optional[pulumi.Input[pulumi.InputType['BucketOwnershipControlsRuleArgs']]] = None,
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
            __props__ = BucketOwnershipControlsArgs.__new__(BucketOwnershipControlsArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            if rule is None and not opts.urn:
                raise TypeError("Missing required property 'rule'")
            __props__.__dict__["rule"] = rule
        super(BucketOwnershipControls, __self__).__init__(
            'aws:s3/bucketOwnershipControls:BucketOwnershipControls',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            rule: Optional[pulumi.Input[pulumi.InputType['BucketOwnershipControlsRuleArgs']]] = None) -> 'BucketOwnershipControls':
        """
        Get an existing BucketOwnershipControls resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket that you want to associate this access point with.
        :param pulumi.Input[pulumi.InputType['BucketOwnershipControlsRuleArgs']] rule: Configuration block(s) with Ownership Controls rules. Detailed below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BucketOwnershipControlsState.__new__(_BucketOwnershipControlsState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["rule"] = rule
        return BucketOwnershipControls(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket that you want to associate this access point with.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def rule(self) -> pulumi.Output['outputs.BucketOwnershipControlsRule']:
        """
        Configuration block(s) with Ownership Controls rules. Detailed below.
        """
        return pulumi.get(self, "rule")

