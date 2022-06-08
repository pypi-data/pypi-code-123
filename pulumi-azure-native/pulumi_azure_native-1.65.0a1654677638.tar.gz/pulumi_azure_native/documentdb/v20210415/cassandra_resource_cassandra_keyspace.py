# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CassandraResourceCassandraKeyspaceArgs', 'CassandraResourceCassandraKeyspace']

@pulumi.input_type
class CassandraResourceCassandraKeyspaceArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource: pulumi.Input['CassandraKeyspaceResourceArgs'],
                 resource_group_name: pulumi.Input[str],
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input['CreateUpdateOptionsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CassandraResourceCassandraKeyspace resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input['CassandraKeyspaceResourceArgs'] resource: The standard JSON format of a Cassandra keyspace
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] keyspace_name: Cosmos DB keyspace name.
        :param pulumi.Input[str] location: The location of the resource group to which the resource belongs.
        :param pulumi.Input['CreateUpdateOptionsArgs'] options: A key-value pair of options to be applied for the request. This corresponds to the headers sent with the request.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource", resource)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if keyspace_name is not None:
            pulumi.set(__self__, "keyspace_name", keyspace_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter
    def resource(self) -> pulumi.Input['CassandraKeyspaceResourceArgs']:
        """
        The standard JSON format of a Cassandra keyspace
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input['CassandraKeyspaceResourceArgs']):
        pulumi.set(self, "resource", value)

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
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cosmos DB keyspace name.
        """
        return pulumi.get(self, "keyspace_name")

    @keyspace_name.setter
    def keyspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keyspace_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['CreateUpdateOptionsArgs']]:
        """
        A key-value pair of options to be applied for the request. This corresponds to the headers sent with the request.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['CreateUpdateOptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class CassandraResourceCassandraKeyspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['CreateUpdateOptionsArgs']]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['CassandraKeyspaceResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An Azure Cosmos DB Cassandra keyspace.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] keyspace_name: Cosmos DB keyspace name.
        :param pulumi.Input[str] location: The location of the resource group to which the resource belongs.
        :param pulumi.Input[pulumi.InputType['CreateUpdateOptionsArgs']] options: A key-value pair of options to be applied for the request. This corresponds to the headers sent with the request.
        :param pulumi.Input[pulumi.InputType['CassandraKeyspaceResourceArgs']] resource: The standard JSON format of a Cassandra keyspace
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CassandraResourceCassandraKeyspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Cosmos DB Cassandra keyspace.

        :param str resource_name: The name of the resource.
        :param CassandraResourceCassandraKeyspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CassandraResourceCassandraKeyspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['CreateUpdateOptionsArgs']]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['CassandraKeyspaceResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = CassandraResourceCassandraKeyspaceArgs.__new__(CassandraResourceCassandraKeyspaceArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["keyspace_name"] = keyspace_name
            __props__.__dict__["location"] = location
            __props__.__dict__["options"] = options
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__.__dict__["resource"] = resource
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20150401:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20150408:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20151106:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20160319:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20160331:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20190801:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20191212:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200301:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200401:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200601preview:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200901:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210115:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210301preview:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210315:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210401preview:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210515:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210615:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210701preview:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20211015:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20211015preview:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20211115preview:CassandraResourceCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20220215preview:CassandraResourceCassandraKeyspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CassandraResourceCassandraKeyspace, __self__).__init__(
            'azure-native:documentdb/v20210415:CassandraResourceCassandraKeyspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CassandraResourceCassandraKeyspace':
        """
        Get an existing CassandraResourceCassandraKeyspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CassandraResourceCassandraKeyspaceArgs.__new__(CassandraResourceCassandraKeyspaceArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["resource"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return CassandraResourceCassandraKeyspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the ARM resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional['outputs.CassandraKeyspaceGetPropertiesResponseOptions']]:
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output[Optional['outputs.CassandraKeyspaceGetPropertiesResponseResource']]:
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

