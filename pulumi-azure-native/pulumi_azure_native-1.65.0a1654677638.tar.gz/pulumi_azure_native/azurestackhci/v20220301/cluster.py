# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 aad_application_object_id: Optional[pulumi.Input[str]] = None,
                 aad_client_id: Optional[pulumi.Input[str]] = None,
                 aad_service_principal_object_id: Optional[pulumi.Input[str]] = None,
                 aad_tenant_id: Optional[pulumi.Input[str]] = None,
                 cloud_management_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 desired_properties: Optional[pulumi.Input['ClusterDesiredPropertiesArgs']] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] aad_application_object_id: Object id of cluster AAD identity.
        :param pulumi.Input[str] aad_client_id: App id of cluster AAD identity.
        :param pulumi.Input[str] aad_service_principal_object_id: Id of cluster identity service principal.
        :param pulumi.Input[str] aad_tenant_id: Tenant id of cluster AAD identity.
        :param pulumi.Input[str] cloud_management_endpoint: Endpoint configured for management from the Azure portal.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input['ClusterDesiredPropertiesArgs'] desired_properties: Desired properties of the cluster.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if aad_application_object_id is not None:
            pulumi.set(__self__, "aad_application_object_id", aad_application_object_id)
        if aad_client_id is not None:
            pulumi.set(__self__, "aad_client_id", aad_client_id)
        if aad_service_principal_object_id is not None:
            pulumi.set(__self__, "aad_service_principal_object_id", aad_service_principal_object_id)
        if aad_tenant_id is not None:
            pulumi.set(__self__, "aad_tenant_id", aad_tenant_id)
        if cloud_management_endpoint is not None:
            pulumi.set(__self__, "cloud_management_endpoint", cloud_management_endpoint)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if desired_properties is not None:
            pulumi.set(__self__, "desired_properties", desired_properties)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="aadApplicationObjectId")
    def aad_application_object_id(self) -> Optional[pulumi.Input[str]]:
        """
        Object id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_application_object_id")

    @aad_application_object_id.setter
    def aad_application_object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aad_application_object_id", value)

    @property
    @pulumi.getter(name="aadClientId")
    def aad_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        App id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_client_id")

    @aad_client_id.setter
    def aad_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aad_client_id", value)

    @property
    @pulumi.getter(name="aadServicePrincipalObjectId")
    def aad_service_principal_object_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of cluster identity service principal.
        """
        return pulumi.get(self, "aad_service_principal_object_id")

    @aad_service_principal_object_id.setter
    def aad_service_principal_object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aad_service_principal_object_id", value)

    @property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tenant id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_tenant_id")

    @aad_tenant_id.setter
    def aad_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aad_tenant_id", value)

    @property
    @pulumi.getter(name="cloudManagementEndpoint")
    def cloud_management_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint configured for management from the Azure portal.
        """
        return pulumi.get(self, "cloud_management_endpoint")

    @cloud_management_endpoint.setter
    def cloud_management_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_management_endpoint", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @created_by_type.setter
    def created_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "created_by_type", value)

    @property
    @pulumi.getter(name="desiredProperties")
    def desired_properties(self) -> Optional[pulumi.Input['ClusterDesiredPropertiesArgs']]:
        """
        Desired properties of the cluster.
        """
        return pulumi.get(self, "desired_properties")

    @desired_properties.setter
    def desired_properties(self, value: Optional[pulumi.Input['ClusterDesiredPropertiesArgs']]):
        pulumi.set(self, "desired_properties", value)

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_at", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_by", value)

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @last_modified_by_type.setter
    def last_modified_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "last_modified_by_type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_application_object_id: Optional[pulumi.Input[str]] = None,
                 aad_client_id: Optional[pulumi.Input[str]] = None,
                 aad_service_principal_object_id: Optional[pulumi.Input[str]] = None,
                 aad_tenant_id: Optional[pulumi.Input[str]] = None,
                 cloud_management_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 desired_properties: Optional[pulumi.Input[pulumi.InputType['ClusterDesiredPropertiesArgs']]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Cluster details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aad_application_object_id: Object id of cluster AAD identity.
        :param pulumi.Input[str] aad_client_id: App id of cluster AAD identity.
        :param pulumi.Input[str] aad_service_principal_object_id: Id of cluster identity service principal.
        :param pulumi.Input[str] aad_tenant_id: Tenant id of cluster AAD identity.
        :param pulumi.Input[str] cloud_management_endpoint: Endpoint configured for management from the Azure portal.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[pulumi.InputType['ClusterDesiredPropertiesArgs']] desired_properties: Desired properties of the cluster.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Cluster details.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_application_object_id: Optional[pulumi.Input[str]] = None,
                 aad_client_id: Optional[pulumi.Input[str]] = None,
                 aad_service_principal_object_id: Optional[pulumi.Input[str]] = None,
                 aad_tenant_id: Optional[pulumi.Input[str]] = None,
                 cloud_management_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 desired_properties: Optional[pulumi.Input[pulumi.InputType['ClusterDesiredPropertiesArgs']]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
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
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["aad_application_object_id"] = aad_application_object_id
            __props__.__dict__["aad_client_id"] = aad_client_id
            __props__.__dict__["aad_service_principal_object_id"] = aad_service_principal_object_id
            __props__.__dict__["aad_tenant_id"] = aad_tenant_id
            __props__.__dict__["cloud_management_endpoint"] = cloud_management_endpoint
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["created_by_type"] = created_by_type
            __props__.__dict__["desired_properties"] = desired_properties
            __props__.__dict__["last_modified_at"] = last_modified_at
            __props__.__dict__["last_modified_by"] = last_modified_by
            __props__.__dict__["last_modified_by_type"] = last_modified_by_type
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["billing_model"] = None
            __props__.__dict__["cloud_id"] = None
            __props__.__dict__["last_billing_timestamp"] = None
            __props__.__dict__["last_sync_timestamp"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["registration_timestamp"] = None
            __props__.__dict__["reported_properties"] = None
            __props__.__dict__["service_endpoint"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["trial_days_remaining"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:Cluster"), pulumi.Alias(type_="azure-native:azurestackhci/v20200301preview:Cluster"), pulumi.Alias(type_="azure-native:azurestackhci/v20201001:Cluster"), pulumi.Alias(type_="azure-native:azurestackhci/v20210101preview:Cluster"), pulumi.Alias(type_="azure-native:azurestackhci/v20210901:Cluster"), pulumi.Alias(type_="azure-native:azurestackhci/v20220101:Cluster"), pulumi.Alias(type_="azure-native:azurestackhci/v20220501:Cluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cluster, __self__).__init__(
            'azure-native:azurestackhci/v20220301:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["aad_application_object_id"] = None
        __props__.__dict__["aad_client_id"] = None
        __props__.__dict__["aad_service_principal_object_id"] = None
        __props__.__dict__["aad_tenant_id"] = None
        __props__.__dict__["billing_model"] = None
        __props__.__dict__["cloud_id"] = None
        __props__.__dict__["cloud_management_endpoint"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_by_type"] = None
        __props__.__dict__["desired_properties"] = None
        __props__.__dict__["last_billing_timestamp"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_by_type"] = None
        __props__.__dict__["last_sync_timestamp"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["registration_timestamp"] = None
        __props__.__dict__["reported_properties"] = None
        __props__.__dict__["service_endpoint"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trial_days_remaining"] = None
        __props__.__dict__["type"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aadApplicationObjectId")
    def aad_application_object_id(self) -> pulumi.Output[Optional[str]]:
        """
        Object id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_application_object_id")

    @property
    @pulumi.getter(name="aadClientId")
    def aad_client_id(self) -> pulumi.Output[Optional[str]]:
        """
        App id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_client_id")

    @property
    @pulumi.getter(name="aadServicePrincipalObjectId")
    def aad_service_principal_object_id(self) -> pulumi.Output[Optional[str]]:
        """
        Id of cluster identity service principal.
        """
        return pulumi.get(self, "aad_service_principal_object_id")

    @property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        Tenant id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_tenant_id")

    @property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> pulumi.Output[str]:
        """
        Type of billing applied to the resource.
        """
        return pulumi.get(self, "billing_model")

    @property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> pulumi.Output[str]:
        """
        Unique, immutable resource id.
        """
        return pulumi.get(self, "cloud_id")

    @property
    @pulumi.getter(name="cloudManagementEndpoint")
    def cloud_management_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        Endpoint configured for management from the Azure portal.
        """
        return pulumi.get(self, "cloud_management_endpoint")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="desiredProperties")
    def desired_properties(self) -> pulumi.Output[Optional['outputs.ClusterDesiredPropertiesResponse']]:
        """
        Desired properties of the cluster.
        """
        return pulumi.get(self, "desired_properties")

    @property
    @pulumi.getter(name="lastBillingTimestamp")
    def last_billing_timestamp(self) -> pulumi.Output[str]:
        """
        Most recent billing meter timestamp.
        """
        return pulumi.get(self, "last_billing_timestamp")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @property
    @pulumi.getter(name="lastSyncTimestamp")
    def last_sync_timestamp(self) -> pulumi.Output[str]:
        """
        Most recent cluster sync timestamp.
        """
        return pulumi.get(self, "last_sync_timestamp")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="registrationTimestamp")
    def registration_timestamp(self) -> pulumi.Output[str]:
        """
        First cluster sync timestamp.
        """
        return pulumi.get(self, "registration_timestamp")

    @property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> pulumi.Output['outputs.ClusterReportedPropertiesResponse']:
        """
        Properties reported by cluster agent.
        """
        return pulumi.get(self, "reported_properties")

    @property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> pulumi.Output[str]:
        """
        Region specific DataPath Endpoint of the cluster.
        """
        return pulumi.get(self, "service_endpoint")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the cluster agent.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trialDaysRemaining")
    def trial_days_remaining(self) -> pulumi.Output[float]:
        """
        Number of days remaining in the trial period.
        """
        return pulumi.get(self, "trial_days_remaining")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

