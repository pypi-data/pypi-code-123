# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetMongoDBResourceMongoUserDefinitionResult',
    'AwaitableGetMongoDBResourceMongoUserDefinitionResult',
    'get_mongo_db_resource_mongo_user_definition',
    'get_mongo_db_resource_mongo_user_definition_output',
]

@pulumi.output_type
class GetMongoDBResourceMongoUserDefinitionResult:
    """
    An Azure Cosmos DB User Definition
    """
    def __init__(__self__, custom_data=None, database_name=None, id=None, mechanisms=None, name=None, password=None, roles=None, type=None, user_name=None):
        if custom_data and not isinstance(custom_data, str):
            raise TypeError("Expected argument 'custom_data' to be a str")
        pulumi.set(__self__, "custom_data", custom_data)
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mechanisms and not isinstance(mechanisms, str):
            raise TypeError("Expected argument 'mechanisms' to be a str")
        pulumi.set(__self__, "mechanisms", mechanisms)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[str]:
        """
        A custom definition for the USer Definition.
        """
        return pulumi.get(self, "custom_data")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[str]:
        """
        The database name for which access is being granted for this User Definition.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique resource identifier of the database account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def mechanisms(self) -> Optional[str]:
        """
        The Mongo Auth mechanism. For now, we only support auth mechanism SCRAM-SHA-256.
        """
        return pulumi.get(self, "mechanisms")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        The password for User Definition. Response does not contain user password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def roles(self) -> Optional[Sequence['outputs.RoleResponse']]:
        """
        The set of roles inherited by the User Definition.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[str]:
        """
        The user name for User Definition.
        """
        return pulumi.get(self, "user_name")


class AwaitableGetMongoDBResourceMongoUserDefinitionResult(GetMongoDBResourceMongoUserDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMongoDBResourceMongoUserDefinitionResult(
            custom_data=self.custom_data,
            database_name=self.database_name,
            id=self.id,
            mechanisms=self.mechanisms,
            name=self.name,
            password=self.password,
            roles=self.roles,
            type=self.type,
            user_name=self.user_name)


def get_mongo_db_resource_mongo_user_definition(account_name: Optional[str] = None,
                                                mongo_user_definition_id: Optional[str] = None,
                                                resource_group_name: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMongoDBResourceMongoUserDefinitionResult:
    """
    An Azure Cosmos DB User Definition


    :param str account_name: Cosmos DB database account name.
    :param str mongo_user_definition_id: The ID for the User Definition {dbName.userName}.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['mongoUserDefinitionId'] = mongo_user_definition_id
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20211115preview:getMongoDBResourceMongoUserDefinition', __args__, opts=opts, typ=GetMongoDBResourceMongoUserDefinitionResult).value

    return AwaitableGetMongoDBResourceMongoUserDefinitionResult(
        custom_data=__ret__.custom_data,
        database_name=__ret__.database_name,
        id=__ret__.id,
        mechanisms=__ret__.mechanisms,
        name=__ret__.name,
        password=__ret__.password,
        roles=__ret__.roles,
        type=__ret__.type,
        user_name=__ret__.user_name)


@_utilities.lift_output_func(get_mongo_db_resource_mongo_user_definition)
def get_mongo_db_resource_mongo_user_definition_output(account_name: Optional[pulumi.Input[str]] = None,
                                                       mongo_user_definition_id: Optional[pulumi.Input[str]] = None,
                                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMongoDBResourceMongoUserDefinitionResult]:
    """
    An Azure Cosmos DB User Definition


    :param str account_name: Cosmos DB database account name.
    :param str mongo_user_definition_id: The ID for the User Definition {dbName.userName}.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
