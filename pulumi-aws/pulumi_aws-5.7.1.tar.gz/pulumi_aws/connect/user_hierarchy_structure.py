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

__all__ = ['UserHierarchyStructureArgs', 'UserHierarchyStructure']

@pulumi.input_type
class UserHierarchyStructureArgs:
    def __init__(__self__, *,
                 hierarchy_structure: pulumi.Input['UserHierarchyStructureHierarchyStructureArgs'],
                 instance_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a UserHierarchyStructure resource.
        :param pulumi.Input['UserHierarchyStructureHierarchyStructureArgs'] hierarchy_structure: A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented below.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        """
        pulumi.set(__self__, "hierarchy_structure", hierarchy_structure)
        pulumi.set(__self__, "instance_id", instance_id)

    @property
    @pulumi.getter(name="hierarchyStructure")
    def hierarchy_structure(self) -> pulumi.Input['UserHierarchyStructureHierarchyStructureArgs']:
        """
        A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented below.
        """
        return pulumi.get(self, "hierarchy_structure")

    @hierarchy_structure.setter
    def hierarchy_structure(self, value: pulumi.Input['UserHierarchyStructureHierarchyStructureArgs']):
        pulumi.set(self, "hierarchy_structure", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        Specifies the identifier of the hosting Amazon Connect Instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)


@pulumi.input_type
class _UserHierarchyStructureState:
    def __init__(__self__, *,
                 hierarchy_structure: Optional[pulumi.Input['UserHierarchyStructureHierarchyStructureArgs']] = None,
                 instance_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserHierarchyStructure resources.
        :param pulumi.Input['UserHierarchyStructureHierarchyStructureArgs'] hierarchy_structure: A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented below.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        """
        if hierarchy_structure is not None:
            pulumi.set(__self__, "hierarchy_structure", hierarchy_structure)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)

    @property
    @pulumi.getter(name="hierarchyStructure")
    def hierarchy_structure(self) -> Optional[pulumi.Input['UserHierarchyStructureHierarchyStructureArgs']]:
        """
        A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented below.
        """
        return pulumi.get(self, "hierarchy_structure")

    @hierarchy_structure.setter
    def hierarchy_structure(self, value: Optional[pulumi.Input['UserHierarchyStructureHierarchyStructureArgs']]):
        pulumi.set(self, "hierarchy_structure", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the identifier of the hosting Amazon Connect Instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)


class UserHierarchyStructure(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hierarchy_structure: Optional[pulumi.Input[pulumi.InputType['UserHierarchyStructureHierarchyStructureArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Amazon Connect User Hierarchy Structure resource. For more information see
        [Amazon Connect: Getting Started](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-get-started.html)

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.connect.UserHierarchyStructure("example",
            hierarchy_structure=aws.connect.UserHierarchyStructureHierarchyStructureArgs(
                level_one=aws.connect.UserHierarchyStructureHierarchyStructureLevelOneArgs(
                    name="levelone",
                ),
            ),
            instance_id="aaaaaaaa-bbbb-cccc-dddd-111111111111")
        ```
        ### With Five Levels

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.connect.UserHierarchyStructure("example",
            hierarchy_structure=aws.connect.UserHierarchyStructureHierarchyStructureArgs(
                level_five=aws.connect.UserHierarchyStructureHierarchyStructureLevelFiveArgs(
                    name="levelfive",
                ),
                level_four=aws.connect.UserHierarchyStructureHierarchyStructureLevelFourArgs(
                    name="levelfour",
                ),
                level_one=aws.connect.UserHierarchyStructureHierarchyStructureLevelOneArgs(
                    name="levelone",
                ),
                level_three=aws.connect.UserHierarchyStructureHierarchyStructureLevelThreeArgs(
                    name="levelthree",
                ),
                level_two=aws.connect.UserHierarchyStructureHierarchyStructureLevelTwoArgs(
                    name="leveltwo",
                ),
            ),
            instance_id="aaaaaaaa-bbbb-cccc-dddd-111111111111")
        ```

        ## Import

        Amazon Connect User Hierarchy Structures can be imported using the `instance_id`, e.g.,

        ```sh
         $ pulumi import aws:connect/userHierarchyStructure:UserHierarchyStructure example f1288a1f-6193-445a-b47e-af739b2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['UserHierarchyStructureHierarchyStructureArgs']] hierarchy_structure: A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented below.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserHierarchyStructureArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Amazon Connect User Hierarchy Structure resource. For more information see
        [Amazon Connect: Getting Started](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-get-started.html)

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.connect.UserHierarchyStructure("example",
            hierarchy_structure=aws.connect.UserHierarchyStructureHierarchyStructureArgs(
                level_one=aws.connect.UserHierarchyStructureHierarchyStructureLevelOneArgs(
                    name="levelone",
                ),
            ),
            instance_id="aaaaaaaa-bbbb-cccc-dddd-111111111111")
        ```
        ### With Five Levels

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.connect.UserHierarchyStructure("example",
            hierarchy_structure=aws.connect.UserHierarchyStructureHierarchyStructureArgs(
                level_five=aws.connect.UserHierarchyStructureHierarchyStructureLevelFiveArgs(
                    name="levelfive",
                ),
                level_four=aws.connect.UserHierarchyStructureHierarchyStructureLevelFourArgs(
                    name="levelfour",
                ),
                level_one=aws.connect.UserHierarchyStructureHierarchyStructureLevelOneArgs(
                    name="levelone",
                ),
                level_three=aws.connect.UserHierarchyStructureHierarchyStructureLevelThreeArgs(
                    name="levelthree",
                ),
                level_two=aws.connect.UserHierarchyStructureHierarchyStructureLevelTwoArgs(
                    name="leveltwo",
                ),
            ),
            instance_id="aaaaaaaa-bbbb-cccc-dddd-111111111111")
        ```

        ## Import

        Amazon Connect User Hierarchy Structures can be imported using the `instance_id`, e.g.,

        ```sh
         $ pulumi import aws:connect/userHierarchyStructure:UserHierarchyStructure example f1288a1f-6193-445a-b47e-af739b2
        ```

        :param str resource_name: The name of the resource.
        :param UserHierarchyStructureArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserHierarchyStructureArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hierarchy_structure: Optional[pulumi.Input[pulumi.InputType['UserHierarchyStructureHierarchyStructureArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = UserHierarchyStructureArgs.__new__(UserHierarchyStructureArgs)

            if hierarchy_structure is None and not opts.urn:
                raise TypeError("Missing required property 'hierarchy_structure'")
            __props__.__dict__["hierarchy_structure"] = hierarchy_structure
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
        super(UserHierarchyStructure, __self__).__init__(
            'aws:connect/userHierarchyStructure:UserHierarchyStructure',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            hierarchy_structure: Optional[pulumi.Input[pulumi.InputType['UserHierarchyStructureHierarchyStructureArgs']]] = None,
            instance_id: Optional[pulumi.Input[str]] = None) -> 'UserHierarchyStructure':
        """
        Get an existing UserHierarchyStructure resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['UserHierarchyStructureHierarchyStructureArgs']] hierarchy_structure: A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented below.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserHierarchyStructureState.__new__(_UserHierarchyStructureState)

        __props__.__dict__["hierarchy_structure"] = hierarchy_structure
        __props__.__dict__["instance_id"] = instance_id
        return UserHierarchyStructure(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hierarchyStructure")
    def hierarchy_structure(self) -> pulumi.Output['outputs.UserHierarchyStructureHierarchyStructure']:
        """
        A block that defines the hierarchy structure's levels. The `hierarchy_structure` block is documented below.
        """
        return pulumi.get(self, "hierarchy_structure")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        Specifies the identifier of the hosting Amazon Connect Instance.
        """
        return pulumi.get(self, "instance_id")

