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

__all__ = ['TaskTemplateArgs', 'TaskTemplate']

@pulumi.input_type
class TaskTemplateArgs:
    def __init__(__self__, *,
                 instance_arn: pulumi.Input[str],
                 client_token: Optional[pulumi.Input[str]] = None,
                 constraints: Optional[pulumi.Input['ConstraintsPropertiesArgs']] = None,
                 contact_flow_arn: Optional[pulumi.Input[str]] = None,
                 defaults: Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateDefaultFieldValueArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateFieldArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['TaskTemplateStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateTagArgs']]]] = None):
        """
        The set of arguments for constructing a TaskTemplate resource.
        :param pulumi.Input[str] instance_arn: The identifier (arn) of the instance.
        :param pulumi.Input['ConstraintsPropertiesArgs'] constraints: The constraints for the task template
        :param pulumi.Input[str] contact_flow_arn: The identifier of the contact flow.
        :param pulumi.Input[str] description: The description of the task template.
        :param pulumi.Input[Sequence[pulumi.Input['TaskTemplateFieldArgs']]] fields: The list of task template's fields
        :param pulumi.Input[str] name: The name of the task template.
        :param pulumi.Input[Sequence[pulumi.Input['TaskTemplateTagArgs']]] tags: One or more tags.
        """
        pulumi.set(__self__, "instance_arn", instance_arn)
        if client_token is not None:
            pulumi.set(__self__, "client_token", client_token)
        if constraints is not None:
            pulumi.set(__self__, "constraints", constraints)
        if contact_flow_arn is not None:
            pulumi.set(__self__, "contact_flow_arn", contact_flow_arn)
        if defaults is not None:
            pulumi.set(__self__, "defaults", defaults)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The identifier (arn) of the instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_token")

    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_token", value)

    @property
    @pulumi.getter
    def constraints(self) -> Optional[pulumi.Input['ConstraintsPropertiesArgs']]:
        """
        The constraints for the task template
        """
        return pulumi.get(self, "constraints")

    @constraints.setter
    def constraints(self, value: Optional[pulumi.Input['ConstraintsPropertiesArgs']]):
        pulumi.set(self, "constraints", value)

    @property
    @pulumi.getter(name="contactFlowArn")
    def contact_flow_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the contact flow.
        """
        return pulumi.get(self, "contact_flow_arn")

    @contact_flow_arn.setter
    def contact_flow_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_flow_arn", value)

    @property
    @pulumi.getter
    def defaults(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateDefaultFieldValueArgs']]]]:
        return pulumi.get(self, "defaults")

    @defaults.setter
    def defaults(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateDefaultFieldValueArgs']]]]):
        pulumi.set(self, "defaults", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the task template.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateFieldArgs']]]]:
        """
        The list of task template's fields
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateFieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the task template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['TaskTemplateStatus']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['TaskTemplateStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateTagArgs']]]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskTemplateTagArgs']]]]):
        pulumi.set(self, "tags", value)


class TaskTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 constraints: Optional[pulumi.Input[pulumi.InputType['ConstraintsPropertiesArgs']]] = None,
                 contact_flow_arn: Optional[pulumi.Input[str]] = None,
                 defaults: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateDefaultFieldValueArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateFieldArgs']]]]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['TaskTemplateStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::TaskTemplate.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConstraintsPropertiesArgs']] constraints: The constraints for the task template
        :param pulumi.Input[str] contact_flow_arn: The identifier of the contact flow.
        :param pulumi.Input[str] description: The description of the task template.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateFieldArgs']]]] fields: The list of task template's fields
        :param pulumi.Input[str] instance_arn: The identifier (arn) of the instance.
        :param pulumi.Input[str] name: The name of the task template.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateTagArgs']]]] tags: One or more tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TaskTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::TaskTemplate.

        :param str resource_name: The name of the resource.
        :param TaskTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TaskTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 constraints: Optional[pulumi.Input[pulumi.InputType['ConstraintsPropertiesArgs']]] = None,
                 contact_flow_arn: Optional[pulumi.Input[str]] = None,
                 defaults: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateDefaultFieldValueArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateFieldArgs']]]]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['TaskTemplateStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskTemplateTagArgs']]]]] = None,
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
            __props__ = TaskTemplateArgs.__new__(TaskTemplateArgs)

            __props__.__dict__["client_token"] = client_token
            __props__.__dict__["constraints"] = constraints
            __props__.__dict__["contact_flow_arn"] = contact_flow_arn
            __props__.__dict__["defaults"] = defaults
            __props__.__dict__["description"] = description
            __props__.__dict__["fields"] = fields
            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(TaskTemplate, __self__).__init__(
            'aws-native:connect:TaskTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TaskTemplate':
        """
        Get an existing TaskTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TaskTemplateArgs.__new__(TaskTemplateArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["client_token"] = None
        __props__.__dict__["constraints"] = None
        __props__.__dict__["contact_flow_arn"] = None
        __props__.__dict__["defaults"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return TaskTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The identifier (arn) of the task template.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "client_token")

    @property
    @pulumi.getter
    def constraints(self) -> pulumi.Output[Optional['outputs.ConstraintsProperties']]:
        """
        The constraints for the task template
        """
        return pulumi.get(self, "constraints")

    @property
    @pulumi.getter(name="contactFlowArn")
    def contact_flow_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the contact flow.
        """
        return pulumi.get(self, "contact_flow_arn")

    @property
    @pulumi.getter
    def defaults(self) -> pulumi.Output[Optional[Sequence['outputs.TaskTemplateDefaultFieldValue']]]:
        return pulumi.get(self, "defaults")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the task template.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Sequence['outputs.TaskTemplateField']]]:
        """
        The list of task template's fields
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The identifier (arn) of the instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the task template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional['TaskTemplateStatus']]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TaskTemplateTag']]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

