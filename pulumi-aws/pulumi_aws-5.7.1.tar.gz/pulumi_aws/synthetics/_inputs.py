# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'CanaryArtifactConfigArgs',
    'CanaryArtifactConfigS3EncryptionArgs',
    'CanaryRunConfigArgs',
    'CanaryScheduleArgs',
    'CanaryTimelineArgs',
    'CanaryVpcConfigArgs',
]

@pulumi.input_type
class CanaryArtifactConfigArgs:
    def __init__(__self__, *,
                 s3_encryption: Optional[pulumi.Input['CanaryArtifactConfigS3EncryptionArgs']] = None):
        """
        :param pulumi.Input['CanaryArtifactConfigS3EncryptionArgs'] s3_encryption: Configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3. See S3 Encryption.
        """
        if s3_encryption is not None:
            pulumi.set(__self__, "s3_encryption", s3_encryption)

    @property
    @pulumi.getter(name="s3Encryption")
    def s3_encryption(self) -> Optional[pulumi.Input['CanaryArtifactConfigS3EncryptionArgs']]:
        """
        Configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3. See S3 Encryption.
        """
        return pulumi.get(self, "s3_encryption")

    @s3_encryption.setter
    def s3_encryption(self, value: Optional[pulumi.Input['CanaryArtifactConfigS3EncryptionArgs']]):
        pulumi.set(self, "s3_encryption", value)


@pulumi.input_type
class CanaryArtifactConfigS3EncryptionArgs:
    def __init__(__self__, *,
                 encryption_mode: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] encryption_mode: The encryption method to use for artifacts created by this canary. Valid values are: `SSE_S3` and `SSE_KMS`.
        :param pulumi.Input[str] kms_key_arn: The ARN of the customer-managed KMS key to use, if you specify `SSE_KMS` for `encryption_mode`.
        """
        if encryption_mode is not None:
            pulumi.set(__self__, "encryption_mode", encryption_mode)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)

    @property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The encryption method to use for artifacts created by this canary. Valid values are: `SSE_S3` and `SSE_KMS`.
        """
        return pulumi.get(self, "encryption_mode")

    @encryption_mode.setter
    def encryption_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_mode", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the customer-managed KMS key to use, if you specify `SSE_KMS` for `encryption_mode`.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)


@pulumi.input_type
class CanaryRunConfigArgs:
    def __init__(__self__, *,
                 active_tracing: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 memory_in_mb: Optional[pulumi.Input[int]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[bool] active_tracing: Whether this canary is to use active AWS X-Ray tracing when it runs. You can enable active tracing only for canaries that use version syn-nodejs-2.0 or later for their canary runtime.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment_variables: Map of environment variables that are accessible from the canary during execution. Please see [AWS Docs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime) for variables reserved for Lambda.
        :param pulumi.Input[int] memory_in_mb: Maximum amount of memory available to the canary while it is running, in MB. The value you specify must be a multiple of 64.
        :param pulumi.Input[int] timeout_in_seconds: Number of seconds the canary is allowed to run before it must stop. If you omit this field, the frequency of the canary is used, up to a maximum of 840 (14 minutes).
        """
        if active_tracing is not None:
            pulumi.set(__self__, "active_tracing", active_tracing)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if memory_in_mb is not None:
            pulumi.set(__self__, "memory_in_mb", memory_in_mb)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)

    @property
    @pulumi.getter(name="activeTracing")
    def active_tracing(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this canary is to use active AWS X-Ray tracing when it runs. You can enable active tracing only for canaries that use version syn-nodejs-2.0 or later for their canary runtime.
        """
        return pulumi.get(self, "active_tracing")

    @active_tracing.setter
    def active_tracing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active_tracing", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of environment variables that are accessible from the canary during execution. Please see [AWS Docs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime) for variables reserved for Lambda.
        """
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter(name="memoryInMb")
    def memory_in_mb(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum amount of memory available to the canary while it is running, in MB. The value you specify must be a multiple of 64.
        """
        return pulumi.get(self, "memory_in_mb")

    @memory_in_mb.setter
    def memory_in_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memory_in_mb", value)

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Number of seconds the canary is allowed to run before it must stop. If you omit this field, the frequency of the canary is used, up to a maximum of 840 (14 minutes).
        """
        return pulumi.get(self, "timeout_in_seconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_seconds", value)


@pulumi.input_type
class CanaryScheduleArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 duration_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] expression: Rate expression or cron expression that defines how often the canary is to run. For rate expression, the syntax is `rate(number unit)`. _unit_ can be `minute`, `minutes`, or `hour`. For cron expression, the syntax is `cron(expression)`. For more information about the syntax for cron expressions, see [Scheduling canary runs using cron](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html).
        :param pulumi.Input[int] duration_in_seconds: Duration in seconds, for the canary to continue making regular runs according to the schedule in the Expression value.
        """
        pulumi.set(__self__, "expression", expression)
        if duration_in_seconds is not None:
            pulumi.set(__self__, "duration_in_seconds", duration_in_seconds)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        """
        Rate expression or cron expression that defines how often the canary is to run. For rate expression, the syntax is `rate(number unit)`. _unit_ can be `minute`, `minutes`, or `hour`. For cron expression, the syntax is `cron(expression)`. For more information about the syntax for cron expressions, see [Scheduling canary runs using cron](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html).
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter(name="durationInSeconds")
    def duration_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Duration in seconds, for the canary to continue making regular runs according to the schedule in the Expression value.
        """
        return pulumi.get(self, "duration_in_seconds")

    @duration_in_seconds.setter
    def duration_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "duration_in_seconds", value)


@pulumi.input_type
class CanaryTimelineArgs:
    def __init__(__self__, *,
                 created: Optional[pulumi.Input[str]] = None,
                 last_modified: Optional[pulumi.Input[str]] = None,
                 last_started: Optional[pulumi.Input[str]] = None,
                 last_stopped: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] created: Date and time the canary was created.
        :param pulumi.Input[str] last_modified: Date and time the canary was most recently modified.
        :param pulumi.Input[str] last_started: Date and time that the canary's most recent run started.
        :param pulumi.Input[str] last_stopped: Date and time that the canary's most recent run ended.
        """
        if created is not None:
            pulumi.set(__self__, "created", created)
        if last_modified is not None:
            pulumi.set(__self__, "last_modified", last_modified)
        if last_started is not None:
            pulumi.set(__self__, "last_started", last_started)
        if last_stopped is not None:
            pulumi.set(__self__, "last_stopped", last_stopped)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time the canary was created.
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time the canary was most recently modified.
        """
        return pulumi.get(self, "last_modified")

    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified", value)

    @property
    @pulumi.getter(name="lastStarted")
    def last_started(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time that the canary's most recent run started.
        """
        return pulumi.get(self, "last_started")

    @last_started.setter
    def last_started(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_started", value)

    @property
    @pulumi.getter(name="lastStopped")
    def last_stopped(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time that the canary's most recent run ended.
        """
        return pulumi.get(self, "last_stopped")

    @last_stopped.setter
    def last_stopped(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_stopped", value)


@pulumi.input_type
class CanaryVpcConfigArgs:
    def __init__(__self__, *,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: IDs of the security groups for this canary.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: IDs of the subnets where this canary is to run.
        :param pulumi.Input[str] vpc_id: ID of the VPC where this canary is to run.
        """
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        IDs of the security groups for this canary.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        IDs of the subnets where this canary is to run.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the VPC where this canary is to run.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


