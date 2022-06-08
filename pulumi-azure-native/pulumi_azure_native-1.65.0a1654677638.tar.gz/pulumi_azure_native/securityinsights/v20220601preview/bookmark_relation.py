# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['BookmarkRelationArgs', 'BookmarkRelation']

@pulumi.input_type
class BookmarkRelationArgs:
    def __init__(__self__, *,
                 bookmark_id: pulumi.Input[str],
                 related_resource_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 relation_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BookmarkRelation resource.
        :param pulumi.Input[str] bookmark_id: Bookmark ID
        :param pulumi.Input[str] related_resource_id: The resource ID of the related resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] relation_name: Relation Name
        """
        pulumi.set(__self__, "bookmark_id", bookmark_id)
        pulumi.set(__self__, "related_resource_id", related_resource_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if relation_name is not None:
            pulumi.set(__self__, "relation_name", relation_name)

    @property
    @pulumi.getter(name="bookmarkId")
    def bookmark_id(self) -> pulumi.Input[str]:
        """
        Bookmark ID
        """
        return pulumi.get(self, "bookmark_id")

    @bookmark_id.setter
    def bookmark_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bookmark_id", value)

    @property
    @pulumi.getter(name="relatedResourceId")
    def related_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the related resource
        """
        return pulumi.get(self, "related_resource_id")

    @related_resource_id.setter
    def related_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "related_resource_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="relationName")
    def relation_name(self) -> Optional[pulumi.Input[str]]:
        """
        Relation Name
        """
        return pulumi.get(self, "relation_name")

    @relation_name.setter
    def relation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relation_name", value)


class BookmarkRelation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bookmark_id: Optional[pulumi.Input[str]] = None,
                 related_resource_id: Optional[pulumi.Input[str]] = None,
                 relation_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a relation between two resources

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bookmark_id: Bookmark ID
        :param pulumi.Input[str] related_resource_id: The resource ID of the related resource
        :param pulumi.Input[str] relation_name: Relation Name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BookmarkRelationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a relation between two resources

        :param str resource_name: The name of the resource.
        :param BookmarkRelationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BookmarkRelationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bookmark_id: Optional[pulumi.Input[str]] = None,
                 related_resource_id: Optional[pulumi.Input[str]] = None,
                 relation_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = BookmarkRelationArgs.__new__(BookmarkRelationArgs)

            if bookmark_id is None and not opts.urn:
                raise TypeError("Missing required property 'bookmark_id'")
            __props__.__dict__["bookmark_id"] = bookmark_id
            if related_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'related_resource_id'")
            __props__.__dict__["related_resource_id"] = related_resource_id
            __props__.__dict__["relation_name"] = relation_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["related_resource_kind"] = None
            __props__.__dict__["related_resource_name"] = None
            __props__.__dict__["related_resource_type"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:BookmarkRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:BookmarkRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:BookmarkRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:BookmarkRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:BookmarkRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:BookmarkRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:BookmarkRelation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BookmarkRelation, __self__).__init__(
            'azure-native:securityinsights/v20220601preview:BookmarkRelation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BookmarkRelation':
        """
        Get an existing BookmarkRelation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BookmarkRelationArgs.__new__(BookmarkRelationArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["related_resource_id"] = None
        __props__.__dict__["related_resource_kind"] = None
        __props__.__dict__["related_resource_name"] = None
        __props__.__dict__["related_resource_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return BookmarkRelation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="relatedResourceId")
    def related_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the related resource
        """
        return pulumi.get(self, "related_resource_id")

    @property
    @pulumi.getter(name="relatedResourceKind")
    def related_resource_kind(self) -> pulumi.Output[str]:
        """
        The resource kind of the related resource
        """
        return pulumi.get(self, "related_resource_kind")

    @property
    @pulumi.getter(name="relatedResourceName")
    def related_resource_name(self) -> pulumi.Output[str]:
        """
        The name of the related resource
        """
        return pulumi.get(self, "related_resource_name")

    @property
    @pulumi.getter(name="relatedResourceType")
    def related_resource_type(self) -> pulumi.Output[str]:
        """
        The resource type of the related resource
        """
        return pulumi.get(self, "related_resource_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

