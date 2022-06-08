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

__all__ = ['RoutingProfileArgs', 'RoutingProfile']

@pulumi.input_type
class RoutingProfileArgs:
    def __init__(__self__, *,
                 default_outbound_queue_id: pulumi.Input[str],
                 description: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 media_concurrencies: pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]],
                 name: Optional[pulumi.Input[str]] = None,
                 queue_configs: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RoutingProfile resource.
        :param pulumi.Input[str] default_outbound_queue_id: Specifies the default outbound queue for the Routing Profile.
        :param pulumi.Input[str] description: Specifies the description of the Routing Profile.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        :param pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]] media_concurrencies: One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented below.
        :param pulumi.Input[str] name: Specifies the name of the Routing Profile.
        :param pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]] queue_configs: One or more `queue_configs` blocks that specify the inbound queues associated with the routing profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to apply to the Routing Profile. If configured with a provider
               [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        pulumi.set(__self__, "default_outbound_queue_id", default_outbound_queue_id)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "media_concurrencies", media_concurrencies)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if queue_configs is not None:
            pulumi.set(__self__, "queue_configs", queue_configs)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="defaultOutboundQueueId")
    def default_outbound_queue_id(self) -> pulumi.Input[str]:
        """
        Specifies the default outbound queue for the Routing Profile.
        """
        return pulumi.get(self, "default_outbound_queue_id")

    @default_outbound_queue_id.setter
    def default_outbound_queue_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_outbound_queue_id", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Specifies the description of the Routing Profile.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

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

    @property
    @pulumi.getter(name="mediaConcurrencies")
    def media_concurrencies(self) -> pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]]:
        """
        One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented below.
        """
        return pulumi.get(self, "media_concurrencies")

    @media_concurrencies.setter
    def media_concurrencies(self, value: pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]]):
        pulumi.set(self, "media_concurrencies", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Routing Profile.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]]]:
        """
        One or more `queue_configs` blocks that specify the inbound queues associated with the routing profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is documented below.
        """
        return pulumi.get(self, "queue_configs")

    @queue_configs.setter
    def queue_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]]]):
        pulumi.set(self, "queue_configs", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags to apply to the Routing Profile. If configured with a provider
        [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _RoutingProfileState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 default_outbound_queue_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 media_concurrencies: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue_configs: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]]] = None,
                 queue_configs_associateds: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigsAssociatedArgs']]]] = None,
                 routing_profile_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering RoutingProfile resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the Routing Profile.
        :param pulumi.Input[str] default_outbound_queue_id: Specifies the default outbound queue for the Routing Profile.
        :param pulumi.Input[str] description: Specifies the description of the Routing Profile.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        :param pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]] media_concurrencies: One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented below.
        :param pulumi.Input[str] name: Specifies the name of the Routing Profile.
        :param pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]] queue_configs: One or more `queue_configs` blocks that specify the inbound queues associated with the routing profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is documented below.
        :param pulumi.Input[str] routing_profile_id: The identifier for the Routing Profile.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to apply to the Routing Profile. If configured with a provider
               [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if default_outbound_queue_id is not None:
            pulumi.set(__self__, "default_outbound_queue_id", default_outbound_queue_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if media_concurrencies is not None:
            pulumi.set(__self__, "media_concurrencies", media_concurrencies)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if queue_configs is not None:
            pulumi.set(__self__, "queue_configs", queue_configs)
        if queue_configs_associateds is not None:
            pulumi.set(__self__, "queue_configs_associateds", queue_configs_associateds)
        if routing_profile_id is not None:
            pulumi.set(__self__, "routing_profile_id", routing_profile_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the Routing Profile.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="defaultOutboundQueueId")
    def default_outbound_queue_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the default outbound queue for the Routing Profile.
        """
        return pulumi.get(self, "default_outbound_queue_id")

    @default_outbound_queue_id.setter
    def default_outbound_queue_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_outbound_queue_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the description of the Routing Profile.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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

    @property
    @pulumi.getter(name="mediaConcurrencies")
    def media_concurrencies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]]]:
        """
        One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented below.
        """
        return pulumi.get(self, "media_concurrencies")

    @media_concurrencies.setter
    def media_concurrencies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileMediaConcurrencyArgs']]]]):
        pulumi.set(self, "media_concurrencies", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Routing Profile.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]]]:
        """
        One or more `queue_configs` blocks that specify the inbound queues associated with the routing profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is documented below.
        """
        return pulumi.get(self, "queue_configs")

    @queue_configs.setter
    def queue_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigArgs']]]]):
        pulumi.set(self, "queue_configs", value)

    @property
    @pulumi.getter(name="queueConfigsAssociateds")
    def queue_configs_associateds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigsAssociatedArgs']]]]:
        return pulumi.get(self, "queue_configs_associateds")

    @queue_configs_associateds.setter
    def queue_configs_associateds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingProfileQueueConfigsAssociatedArgs']]]]):
        pulumi.set(self, "queue_configs_associateds", value)

    @property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the Routing Profile.
        """
        return pulumi.get(self, "routing_profile_id")

    @routing_profile_id.setter
    def routing_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_profile_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags to apply to the Routing Profile. If configured with a provider
        [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class RoutingProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_outbound_queue_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 media_concurrencies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileMediaConcurrencyArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileQueueConfigArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an Amazon Connect Routing Profile resource. For more information see
        [Amazon Connect: Getting Started](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-get-started.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.connect.RoutingProfile("example",
            default_outbound_queue_id="12345678-1234-1234-1234-123456789012",
            description="example description",
            instance_id="aaaaaaaa-bbbb-cccc-dddd-111111111111",
            media_concurrencies=[aws.connect.RoutingProfileMediaConcurrencyArgs(
                channel="VOICE",
                concurrency=1,
            )],
            queue_configs=[aws.connect.RoutingProfileQueueConfigArgs(
                channel="VOICE",
                delay=2,
                priority=1,
                queue_id="12345678-1234-1234-1234-123456789012",
            )],
            tags={
                "Name": "Example Routing Profile",
            })
        ```

        ## Import

        Amazon Connect Routing Profiles can be imported using the `instance_id` and `routing_profile_id` separated by a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:connect/routingProfile:RoutingProfile example f1288a1f-6193-445a-b47e-af739b2:c1d4e5f6-1b3c-1b3c-1b3c-c1d4e5f6c1d4e5
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_outbound_queue_id: Specifies the default outbound queue for the Routing Profile.
        :param pulumi.Input[str] description: Specifies the description of the Routing Profile.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileMediaConcurrencyArgs']]]] media_concurrencies: One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented below.
        :param pulumi.Input[str] name: Specifies the name of the Routing Profile.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileQueueConfigArgs']]]] queue_configs: One or more `queue_configs` blocks that specify the inbound queues associated with the routing profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to apply to the Routing Profile. If configured with a provider
               [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoutingProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Amazon Connect Routing Profile resource. For more information see
        [Amazon Connect: Getting Started](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-get-started.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.connect.RoutingProfile("example",
            default_outbound_queue_id="12345678-1234-1234-1234-123456789012",
            description="example description",
            instance_id="aaaaaaaa-bbbb-cccc-dddd-111111111111",
            media_concurrencies=[aws.connect.RoutingProfileMediaConcurrencyArgs(
                channel="VOICE",
                concurrency=1,
            )],
            queue_configs=[aws.connect.RoutingProfileQueueConfigArgs(
                channel="VOICE",
                delay=2,
                priority=1,
                queue_id="12345678-1234-1234-1234-123456789012",
            )],
            tags={
                "Name": "Example Routing Profile",
            })
        ```

        ## Import

        Amazon Connect Routing Profiles can be imported using the `instance_id` and `routing_profile_id` separated by a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:connect/routingProfile:RoutingProfile example f1288a1f-6193-445a-b47e-af739b2:c1d4e5f6-1b3c-1b3c-1b3c-c1d4e5f6c1d4e5
        ```

        :param str resource_name: The name of the resource.
        :param RoutingProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoutingProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_outbound_queue_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 media_concurrencies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileMediaConcurrencyArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileQueueConfigArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = RoutingProfileArgs.__new__(RoutingProfileArgs)

            if default_outbound_queue_id is None and not opts.urn:
                raise TypeError("Missing required property 'default_outbound_queue_id'")
            __props__.__dict__["default_outbound_queue_id"] = default_outbound_queue_id
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if media_concurrencies is None and not opts.urn:
                raise TypeError("Missing required property 'media_concurrencies'")
            __props__.__dict__["media_concurrencies"] = media_concurrencies
            __props__.__dict__["name"] = name
            __props__.__dict__["queue_configs"] = queue_configs
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
            __props__.__dict__["queue_configs_associateds"] = None
            __props__.__dict__["routing_profile_id"] = None
        super(RoutingProfile, __self__).__init__(
            'aws:connect/routingProfile:RoutingProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            default_outbound_queue_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            media_concurrencies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileMediaConcurrencyArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            queue_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileQueueConfigArgs']]]]] = None,
            queue_configs_associateds: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileQueueConfigsAssociatedArgs']]]]] = None,
            routing_profile_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'RoutingProfile':
        """
        Get an existing RoutingProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the Routing Profile.
        :param pulumi.Input[str] default_outbound_queue_id: Specifies the default outbound queue for the Routing Profile.
        :param pulumi.Input[str] description: Specifies the description of the Routing Profile.
        :param pulumi.Input[str] instance_id: Specifies the identifier of the hosting Amazon Connect Instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileMediaConcurrencyArgs']]]] media_concurrencies: One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented below.
        :param pulumi.Input[str] name: Specifies the name of the Routing Profile.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingProfileQueueConfigArgs']]]] queue_configs: One or more `queue_configs` blocks that specify the inbound queues associated with the routing profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is documented below.
        :param pulumi.Input[str] routing_profile_id: The identifier for the Routing Profile.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to apply to the Routing Profile. If configured with a provider
               [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoutingProfileState.__new__(_RoutingProfileState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["default_outbound_queue_id"] = default_outbound_queue_id
        __props__.__dict__["description"] = description
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["media_concurrencies"] = media_concurrencies
        __props__.__dict__["name"] = name
        __props__.__dict__["queue_configs"] = queue_configs
        __props__.__dict__["queue_configs_associateds"] = queue_configs_associateds
        __props__.__dict__["routing_profile_id"] = routing_profile_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return RoutingProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Routing Profile.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultOutboundQueueId")
    def default_outbound_queue_id(self) -> pulumi.Output[str]:
        """
        Specifies the default outbound queue for the Routing Profile.
        """
        return pulumi.get(self, "default_outbound_queue_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Specifies the description of the Routing Profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        Specifies the identifier of the hosting Amazon Connect Instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="mediaConcurrencies")
    def media_concurrencies(self) -> pulumi.Output[Sequence['outputs.RoutingProfileMediaConcurrency']]:
        """
        One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented below.
        """
        return pulumi.get(self, "media_concurrencies")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Routing Profile.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(self) -> pulumi.Output[Optional[Sequence['outputs.RoutingProfileQueueConfig']]]:
        """
        One or more `queue_configs` blocks that specify the inbound queues associated with the routing profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is documented below.
        """
        return pulumi.get(self, "queue_configs")

    @property
    @pulumi.getter(name="queueConfigsAssociateds")
    def queue_configs_associateds(self) -> pulumi.Output[Sequence['outputs.RoutingProfileQueueConfigsAssociated']]:
        return pulumi.get(self, "queue_configs_associateds")

    @property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> pulumi.Output[str]:
        """
        The identifier for the Routing Profile.
        """
        return pulumi.get(self, "routing_profile_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags to apply to the Routing Profile. If configured with a provider
        [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

