# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['SqlResourceSqlRoleAssignmentArgs', 'SqlResourceSqlRoleAssignment']

@pulumi.input_type
class SqlResourceSqlRoleAssignmentArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 principal_id: Optional[pulumi.Input[str]] = None,
                 role_assignment_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlResourceSqlRoleAssignment resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] principal_id: The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.
        :param pulumi.Input[str] role_assignment_id: The GUID for the Role Assignment.
        :param pulumi.Input[str] role_definition_id: The unique identifier for the associated Role Definition.
        :param pulumi.Input[str] scope: The data plane resource path for which access is being granted through this Role Assignment.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if role_assignment_id is not None:
            pulumi.set(__self__, "role_assignment_id", role_assignment_id)
        if role_definition_id is not None:
            pulumi.set(__self__, "role_definition_id", role_definition_id)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Cosmos DB database account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

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
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="roleAssignmentId")
    def role_assignment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GUID for the Role Assignment.
        """
        return pulumi.get(self, "role_assignment_id")

    @role_assignment_id.setter
    def role_assignment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_assignment_id", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier for the associated Role Definition.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_definition_id", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The data plane resource path for which access is being granted through this Role Assignment.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class SqlResourceSqlRoleAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_assignment_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure Cosmos DB Role Assignment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] principal_id: The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] role_assignment_id: The GUID for the Role Assignment.
        :param pulumi.Input[str] role_definition_id: The unique identifier for the associated Role Definition.
        :param pulumi.Input[str] scope: The data plane resource path for which access is being granted through this Role Assignment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlResourceSqlRoleAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Cosmos DB Role Assignment

        :param str resource_name: The name of the resource.
        :param SqlResourceSqlRoleAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlResourceSqlRoleAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_assignment_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
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
            __props__ = SqlResourceSqlRoleAssignmentArgs.__new__(SqlResourceSqlRoleAssignmentArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["principal_id"] = principal_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["role_assignment_id"] = role_assignment_id
            __props__.__dict__["role_definition_id"] = role_definition_id
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20200601preview:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20210301preview:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20210401preview:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20210515:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20210615:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20210701preview:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20211015:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20211015preview:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20211115preview:SqlResourceSqlRoleAssignment"), pulumi.Alias(type_="azure-native:documentdb/v20220215preview:SqlResourceSqlRoleAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlResourceSqlRoleAssignment, __self__).__init__(
            'azure-native:documentdb/v20210415:SqlResourceSqlRoleAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlResourceSqlRoleAssignment':
        """
        Get an existing SqlResourceSqlRoleAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlResourceSqlRoleAssignmentArgs.__new__(SqlResourceSqlRoleAssignmentArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["principal_id"] = None
        __props__.__dict__["role_definition_id"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["type"] = None
        return SqlResourceSqlRoleAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[Optional[str]]:
        """
        The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[Optional[str]]:
        """
        The unique identifier for the associated Role Definition.
        """
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        The data plane resource path for which access is being granted through this Role Assignment.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

