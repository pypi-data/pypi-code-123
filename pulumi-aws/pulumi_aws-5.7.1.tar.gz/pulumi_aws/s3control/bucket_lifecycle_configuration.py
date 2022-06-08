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

__all__ = ['BucketLifecycleConfigurationArgs', 'BucketLifecycleConfiguration']

@pulumi.input_type
class BucketLifecycleConfigurationArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 rules: pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]]):
        """
        The set of arguments for constructing a BucketLifecycleConfiguration resource.
        :param pulumi.Input[str] bucket: Amazon Resource Name (ARN) of the bucket.
        :param pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]] rules: Configuration block(s) containing lifecycle rules for the bucket.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        Amazon Resource Name (ARN) of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]]:
        """
        Configuration block(s) containing lifecycle rules for the bucket.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class _BucketLifecycleConfigurationState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering BucketLifecycleConfiguration resources.
        :param pulumi.Input[str] bucket: Amazon Resource Name (ARN) of the bucket.
        :param pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]] rules: Configuration block(s) containing lifecycle rules for the bucket.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]]]:
        """
        Configuration block(s) containing lifecycle rules for the bucket.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleConfigurationRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class BucketLifecycleConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationRuleArgs']]]]] = None,
                 __props__=None):
        """
        Provides a resource to manage an S3 Control Bucket Lifecycle Configuration.

        > **NOTE:** Each S3 Control Bucket can only have one Lifecycle Configuration. Using multiple of this resource against the same S3 Control Bucket will result in perpetual differences each provider run.

        > This functionality is for managing [S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3onOutposts.html). To manage S3 Bucket Lifecycle Configurations in an AWS Partition, see the `s3.BucketV2` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3control.BucketLifecycleConfiguration("example",
            bucket=aws_s3control_bucket["example"]["arn"],
            rules=[
                aws.s3control.BucketLifecycleConfigurationRuleArgs(
                    expiration=aws.s3control.BucketLifecycleConfigurationRuleExpirationArgs(
                        days=365,
                    ),
                    filter=aws.s3control.BucketLifecycleConfigurationRuleFilterArgs(
                        prefix="logs/",
                    ),
                    id="logs",
                ),
                aws.s3control.BucketLifecycleConfigurationRuleArgs(
                    expiration=aws.s3control.BucketLifecycleConfigurationRuleExpirationArgs(
                        days=7,
                    ),
                    filter=aws.s3control.BucketLifecycleConfigurationRuleFilterArgs(
                        prefix="temp/",
                    ),
                    id="temp",
                ),
            ])
        ```

        ## Import

        S3 Control Bucket Lifecycle Configurations can be imported using the Amazon Resource Name (ARN), e.g.,

        ```sh
         $ pulumi import aws:s3control/bucketLifecycleConfiguration:BucketLifecycleConfiguration example arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-12345678/bucket/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Amazon Resource Name (ARN) of the bucket.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationRuleArgs']]]] rules: Configuration block(s) containing lifecycle rules for the bucket.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketLifecycleConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage an S3 Control Bucket Lifecycle Configuration.

        > **NOTE:** Each S3 Control Bucket can only have one Lifecycle Configuration. Using multiple of this resource against the same S3 Control Bucket will result in perpetual differences each provider run.

        > This functionality is for managing [S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3onOutposts.html). To manage S3 Bucket Lifecycle Configurations in an AWS Partition, see the `s3.BucketV2` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3control.BucketLifecycleConfiguration("example",
            bucket=aws_s3control_bucket["example"]["arn"],
            rules=[
                aws.s3control.BucketLifecycleConfigurationRuleArgs(
                    expiration=aws.s3control.BucketLifecycleConfigurationRuleExpirationArgs(
                        days=365,
                    ),
                    filter=aws.s3control.BucketLifecycleConfigurationRuleFilterArgs(
                        prefix="logs/",
                    ),
                    id="logs",
                ),
                aws.s3control.BucketLifecycleConfigurationRuleArgs(
                    expiration=aws.s3control.BucketLifecycleConfigurationRuleExpirationArgs(
                        days=7,
                    ),
                    filter=aws.s3control.BucketLifecycleConfigurationRuleFilterArgs(
                        prefix="temp/",
                    ),
                    id="temp",
                ),
            ])
        ```

        ## Import

        S3 Control Bucket Lifecycle Configurations can be imported using the Amazon Resource Name (ARN), e.g.,

        ```sh
         $ pulumi import aws:s3control/bucketLifecycleConfiguration:BucketLifecycleConfiguration example arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-12345678/bucket/example
        ```

        :param str resource_name: The name of the resource.
        :param BucketLifecycleConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketLifecycleConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationRuleArgs']]]]] = None,
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
            __props__ = BucketLifecycleConfigurationArgs.__new__(BucketLifecycleConfigurationArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
        super(BucketLifecycleConfiguration, __self__).__init__(
            'aws:s3control/bucketLifecycleConfiguration:BucketLifecycleConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationRuleArgs']]]]] = None) -> 'BucketLifecycleConfiguration':
        """
        Get an existing BucketLifecycleConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Amazon Resource Name (ARN) of the bucket.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BucketLifecycleConfigurationRuleArgs']]]] rules: Configuration block(s) containing lifecycle rules for the bucket.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BucketLifecycleConfigurationState.__new__(_BucketLifecycleConfigurationState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["rules"] = rules
        return BucketLifecycleConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.BucketLifecycleConfigurationRule']]:
        """
        Configuration block(s) containing lifecycle rules for the bucket.
        """
        return pulumi.get(self, "rules")

