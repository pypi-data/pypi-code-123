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

__all__ = ['SizeConstraintSetArgs', 'SizeConstraintSet']

@pulumi.input_type
class SizeConstraintSetArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]] = None):
        """
        The set of arguments for constructing a SizeConstraintSet resource.
        :param pulumi.Input[str] name: The name or description of the Size Constraint Set.
        :param pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]] size_constraints: Specifies the parts of web requests that you want to inspect the size of.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size_constraints is not None:
            pulumi.set(__self__, "size_constraints", size_constraints)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name or description of the Size Constraint Set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]]:
        """
        Specifies the parts of web requests that you want to inspect the size of.
        """
        return pulumi.get(self, "size_constraints")

    @size_constraints.setter
    def size_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]]):
        pulumi.set(self, "size_constraints", value)


@pulumi.input_type
class _SizeConstraintSetState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]] = None):
        """
        Input properties used for looking up and filtering SizeConstraintSet resources.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN)
        :param pulumi.Input[str] name: The name or description of the Size Constraint Set.
        :param pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]] size_constraints: Specifies the parts of web requests that you want to inspect the size of.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size_constraints is not None:
            pulumi.set(__self__, "size_constraints", size_constraints)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN)
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name or description of the Size Constraint Set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]]:
        """
        Specifies the parts of web requests that you want to inspect the size of.
        """
        return pulumi.get(self, "size_constraints")

    @size_constraints.setter
    def size_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]]):
        pulumi.set(self, "size_constraints", value)


class SizeConstraintSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SizeConstraintSetSizeConstraintArgs']]]]] = None,
                 __props__=None):
        """
        Provides a WAF Size Constraint Set Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        size_constraint_set = aws.waf.SizeConstraintSet("sizeConstraintSet", size_constraints=[aws.waf.SizeConstraintSetSizeConstraintArgs(
            comparison_operator="EQ",
            field_to_match=aws.waf.SizeConstraintSetSizeConstraintFieldToMatchArgs(
                type="BODY",
            ),
            size=4096,
            text_transformation="NONE",
        )])
        ```

        ## Import

        AWS WAF Size Constraint Set can be imported using their ID, e.g.,

        ```sh
         $ pulumi import aws:waf/sizeConstraintSet:SizeConstraintSet example a1b2c3d4-d5f6-7777-8888-9999aaaabbbbcccc
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name or description of the Size Constraint Set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SizeConstraintSetSizeConstraintArgs']]]] size_constraints: Specifies the parts of web requests that you want to inspect the size of.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SizeConstraintSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a WAF Size Constraint Set Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        size_constraint_set = aws.waf.SizeConstraintSet("sizeConstraintSet", size_constraints=[aws.waf.SizeConstraintSetSizeConstraintArgs(
            comparison_operator="EQ",
            field_to_match=aws.waf.SizeConstraintSetSizeConstraintFieldToMatchArgs(
                type="BODY",
            ),
            size=4096,
            text_transformation="NONE",
        )])
        ```

        ## Import

        AWS WAF Size Constraint Set can be imported using their ID, e.g.,

        ```sh
         $ pulumi import aws:waf/sizeConstraintSet:SizeConstraintSet example a1b2c3d4-d5f6-7777-8888-9999aaaabbbbcccc
        ```

        :param str resource_name: The name of the resource.
        :param SizeConstraintSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SizeConstraintSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SizeConstraintSetSizeConstraintArgs']]]]] = None,
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
            __props__ = SizeConstraintSetArgs.__new__(SizeConstraintSetArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["size_constraints"] = size_constraints
            __props__.__dict__["arn"] = None
        super(SizeConstraintSet, __self__).__init__(
            'aws:waf/sizeConstraintSet:SizeConstraintSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SizeConstraintSetSizeConstraintArgs']]]]] = None) -> 'SizeConstraintSet':
        """
        Get an existing SizeConstraintSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN)
        :param pulumi.Input[str] name: The name or description of the Size Constraint Set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SizeConstraintSetSizeConstraintArgs']]]] size_constraints: Specifies the parts of web requests that you want to inspect the size of.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SizeConstraintSetState.__new__(_SizeConstraintSetState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["name"] = name
        __props__.__dict__["size_constraints"] = size_constraints
        return SizeConstraintSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN)
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name or description of the Size Constraint Set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> pulumi.Output[Optional[Sequence['outputs.SizeConstraintSetSizeConstraint']]]:
        """
        Specifies the parts of web requests that you want to inspect the size of.
        """
        return pulumi.get(self, "size_constraints")

