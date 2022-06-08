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

__all__ = ['ConnectAttachmentArgs', 'ConnectAttachment']

@pulumi.input_type
class ConnectAttachmentArgs:
    def __init__(__self__, *,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 edge_location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input['ConnectAttachmentOptionsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]]] = None,
                 transport_attachment_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConnectAttachment resource.
        :param pulumi.Input[str] core_network_id: ID of the CoreNetwork that the attachment will be attached to.
        :param pulumi.Input[str] edge_location: Edge location of the attachment.
        :param pulumi.Input['ConnectAttachmentOptionsArgs'] options: Protocol options for connect attachment
        :param pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]] tags: Tags for the attachment.
        :param pulumi.Input[str] transport_attachment_id: Id of transport attachment
        """
        if core_network_id is not None:
            pulumi.set(__self__, "core_network_id", core_network_id)
        if edge_location is not None:
            pulumi.set(__self__, "edge_location", edge_location)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if transport_attachment_id is not None:
            pulumi.set(__self__, "transport_attachment_id", transport_attachment_id)

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the CoreNetwork that the attachment will be attached to.
        """
        return pulumi.get(self, "core_network_id")

    @core_network_id.setter
    def core_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "core_network_id", value)

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[pulumi.Input[str]]:
        """
        Edge location of the attachment.
        """
        return pulumi.get(self, "edge_location")

    @edge_location.setter
    def edge_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edge_location", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['ConnectAttachmentOptionsArgs']]:
        """
        Protocol options for connect attachment
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['ConnectAttachmentOptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]]]:
        """
        Tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectAttachmentTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of transport attachment
        """
        return pulumi.get(self, "transport_attachment_id")

    @transport_attachment_id.setter
    def transport_attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transport_attachment_id", value)


warnings.warn("""ConnectAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ConnectAttachment(pulumi.CustomResource):
    warnings.warn("""ConnectAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 edge_location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['ConnectAttachmentOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectAttachmentTagArgs']]]]] = None,
                 transport_attachment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        AWS::NetworkManager::ConnectAttachment Resource Type Definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] core_network_id: ID of the CoreNetwork that the attachment will be attached to.
        :param pulumi.Input[str] edge_location: Edge location of the attachment.
        :param pulumi.Input[pulumi.InputType['ConnectAttachmentOptionsArgs']] options: Protocol options for connect attachment
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectAttachmentTagArgs']]]] tags: Tags for the attachment.
        :param pulumi.Input[str] transport_attachment_id: Id of transport attachment
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConnectAttachmentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::NetworkManager::ConnectAttachment Resource Type Definition

        :param str resource_name: The name of the resource.
        :param ConnectAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 edge_location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['ConnectAttachmentOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectAttachmentTagArgs']]]]] = None,
                 transport_attachment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ConnectAttachment is deprecated: ConnectAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectAttachmentArgs.__new__(ConnectAttachmentArgs)

            __props__.__dict__["core_network_id"] = core_network_id
            __props__.__dict__["edge_location"] = edge_location
            __props__.__dict__["options"] = options
            __props__.__dict__["tags"] = tags
            __props__.__dict__["transport_attachment_id"] = transport_attachment_id
            __props__.__dict__["attachment_id"] = None
            __props__.__dict__["attachment_policy_rule_number"] = None
            __props__.__dict__["attachment_type"] = None
            __props__.__dict__["core_network_arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["owner_account_id"] = None
            __props__.__dict__["proposed_segment_change"] = None
            __props__.__dict__["resource_arn"] = None
            __props__.__dict__["segment_name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated_at"] = None
        super(ConnectAttachment, __self__).__init__(
            'aws-native:networkmanager:ConnectAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectAttachment':
        """
        Get an existing ConnectAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectAttachmentArgs.__new__(ConnectAttachmentArgs)

        __props__.__dict__["attachment_id"] = None
        __props__.__dict__["attachment_policy_rule_number"] = None
        __props__.__dict__["attachment_type"] = None
        __props__.__dict__["core_network_arn"] = None
        __props__.__dict__["core_network_id"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["edge_location"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["owner_account_id"] = None
        __props__.__dict__["proposed_segment_change"] = None
        __props__.__dict__["resource_arn"] = None
        __props__.__dict__["segment_name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["transport_attachment_id"] = None
        __props__.__dict__["updated_at"] = None
        return ConnectAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Output[str]:
        """
        The ID of the attachment.
        """
        return pulumi.get(self, "attachment_id")

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> pulumi.Output[int]:
        """
        The policy rule number associated with the attachment.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Output[str]:
        """
        The type of attachment.
        """
        return pulumi.get(self, "attachment_type")

    @property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> pulumi.Output[str]:
        """
        The ARN of a core network for the VPC attachment.
        """
        return pulumi.get(self, "core_network_arn")

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the CoreNetwork that the attachment will be attached to.
        """
        return pulumi.get(self, "core_network_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation time of the attachment.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[Optional[str]]:
        """
        Edge location of the attachment.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional['outputs.ConnectAttachmentOptions']]:
        """
        Protocol options for connect attachment
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[str]:
        """
        The ID of the attachment account owner.
        """
        return pulumi.get(self, "owner_account_id")

    @property
    @pulumi.getter(name="proposedSegmentChange")
    def proposed_segment_change(self) -> pulumi.Output['outputs.ConnectAttachmentProposedSegmentChange']:
        """
        The attachment to move from one segment to another.
        """
        return pulumi.get(self, "proposed_segment_change")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        The attachment resource ARN.
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> pulumi.Output[str]:
        """
        The name of the segment attachment.
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectAttachmentTag']]]:
        """
        Tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> pulumi.Output[Optional[str]]:
        """
        Id of transport attachment
        """
        return pulumi.get(self, "transport_attachment_id")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Last update time of the attachment.
        """
        return pulumi.get(self, "updated_at")

