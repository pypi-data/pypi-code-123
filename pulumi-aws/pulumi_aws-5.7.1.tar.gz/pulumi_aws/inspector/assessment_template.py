# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AssessmentTemplateArgs', 'AssessmentTemplate']

@pulumi.input_type
class AssessmentTemplateArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[int],
                 rules_package_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 target_arn: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AssessmentTemplate resource.
        :param pulumi.Input[int] duration: The duration of the inspector run.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rules_package_arns: The rules to be used during the run.
        :param pulumi.Input[str] target_arn: The assessment target ARN to attach the template to.
        :param pulumi.Input[str] name: The name of the assessment template.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the Inspector assessment template. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "rules_package_arns", rules_package_arns)
        pulumi.set(__self__, "target_arn", target_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[int]:
        """
        The duration of the inspector run.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[int]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter(name="rulesPackageArns")
    def rules_package_arns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The rules to be used during the run.
        """
        return pulumi.get(self, "rules_package_arns")

    @rules_package_arns.setter
    def rules_package_arns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "rules_package_arns", value)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[str]:
        """
        The assessment target ARN to attach the template to.
        """
        return pulumi.get(self, "target_arn")

    @target_arn.setter
    def target_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the assessment template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of tags for the Inspector assessment template. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AssessmentTemplateState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules_package_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AssessmentTemplate resources.
        :param pulumi.Input[str] arn: The template assessment ARN.
        :param pulumi.Input[int] duration: The duration of the inspector run.
        :param pulumi.Input[str] name: The name of the assessment template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rules_package_arns: The rules to be used during the run.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the Inspector assessment template. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] target_arn: The assessment target ARN to attach the template to.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if duration is not None:
            pulumi.set(__self__, "duration", duration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules_package_arns is not None:
            pulumi.set(__self__, "rules_package_arns", rules_package_arns)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if target_arn is not None:
            pulumi.set(__self__, "target_arn", target_arn)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The template assessment ARN.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[int]]:
        """
        The duration of the inspector run.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the assessment template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="rulesPackageArns")
    def rules_package_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The rules to be used during the run.
        """
        return pulumi.get(self, "rules_package_arns")

    @rules_package_arns.setter
    def rules_package_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rules_package_arns", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of tags for the Inspector assessment template. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The assessment target ARN to attach the template to.
        """
        return pulumi.get(self, "target_arn")

    @target_arn.setter
    def target_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_arn", value)


class AssessmentTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules_package_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Inspector assessment template

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.inspector.AssessmentTemplate("example",
            target_arn=aws_inspector_assessment_target["example"]["arn"],
            duration=3600,
            rules_package_arns=[
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p",
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-H5hpSawc",
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ",
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-vg5GGHSD",
            ])
        ```

        ## Import

        `aws_inspector_assessment_template` can be imported by using the template assessment ARN, e.g.,

        ```sh
         $ pulumi import aws:inspector/assessmentTemplate:AssessmentTemplate example arn:aws:inspector:us-west-2:123456789012:target/0-9IaAzhGR/template/0-WEcjR8CH
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] duration: The duration of the inspector run.
        :param pulumi.Input[str] name: The name of the assessment template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rules_package_arns: The rules to be used during the run.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the Inspector assessment template. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] target_arn: The assessment target ARN to attach the template to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssessmentTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Inspector assessment template

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.inspector.AssessmentTemplate("example",
            target_arn=aws_inspector_assessment_target["example"]["arn"],
            duration=3600,
            rules_package_arns=[
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p",
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-H5hpSawc",
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ",
                "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-vg5GGHSD",
            ])
        ```

        ## Import

        `aws_inspector_assessment_template` can be imported by using the template assessment ARN, e.g.,

        ```sh
         $ pulumi import aws:inspector/assessmentTemplate:AssessmentTemplate example arn:aws:inspector:us-west-2:123456789012:target/0-9IaAzhGR/template/0-WEcjR8CH
        ```

        :param str resource_name: The name of the resource.
        :param AssessmentTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssessmentTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules_package_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
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
            __props__ = AssessmentTemplateArgs.__new__(AssessmentTemplateArgs)

            if duration is None and not opts.urn:
                raise TypeError("Missing required property 'duration'")
            __props__.__dict__["duration"] = duration
            __props__.__dict__["name"] = name
            if rules_package_arns is None and not opts.urn:
                raise TypeError("Missing required property 'rules_package_arns'")
            __props__.__dict__["rules_package_arns"] = rules_package_arns
            __props__.__dict__["tags"] = tags
            if target_arn is None and not opts.urn:
                raise TypeError("Missing required property 'target_arn'")
            __props__.__dict__["target_arn"] = target_arn
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        super(AssessmentTemplate, __self__).__init__(
            'aws:inspector/assessmentTemplate:AssessmentTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            duration: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rules_package_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            target_arn: Optional[pulumi.Input[str]] = None) -> 'AssessmentTemplate':
        """
        Get an existing AssessmentTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The template assessment ARN.
        :param pulumi.Input[int] duration: The duration of the inspector run.
        :param pulumi.Input[str] name: The name of the assessment template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rules_package_arns: The rules to be used during the run.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the Inspector assessment template. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] target_arn: The assessment target ARN to attach the template to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AssessmentTemplateState.__new__(_AssessmentTemplateState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["duration"] = duration
        __props__.__dict__["name"] = name
        __props__.__dict__["rules_package_arns"] = rules_package_arns
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["target_arn"] = target_arn
        return AssessmentTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The template assessment ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Output[int]:
        """
        The duration of the inspector run.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the assessment template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rulesPackageArns")
    def rules_package_arns(self) -> pulumi.Output[Sequence[str]]:
        """
        The rules to be used during the run.
        """
        return pulumi.get(self, "rules_package_arns")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of tags for the Inspector assessment template. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[str]:
        """
        The assessment target ARN to attach the template to.
        """
        return pulumi.get(self, "target_arn")

