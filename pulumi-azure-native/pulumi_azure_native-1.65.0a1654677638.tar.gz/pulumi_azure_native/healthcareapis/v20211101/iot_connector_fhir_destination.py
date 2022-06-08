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

__all__ = ['IotConnectorFhirDestinationArgs', 'IotConnectorFhirDestination']

@pulumi.input_type
class IotConnectorFhirDestinationArgs:
    def __init__(__self__, *,
                 fhir_mapping: pulumi.Input['IotMappingPropertiesArgs'],
                 fhir_service_resource_id: pulumi.Input[str],
                 iot_connector_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_identity_resolution_type: pulumi.Input[Union[str, 'IotIdentityResolutionType']],
                 workspace_name: pulumi.Input[str],
                 fhir_destination_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IotConnectorFhirDestination resource.
        :param pulumi.Input['IotMappingPropertiesArgs'] fhir_mapping: FHIR Mappings
        :param pulumi.Input[str] fhir_service_resource_id: Fully qualified resource id of the FHIR service to connect to.
        :param pulumi.Input[str] iot_connector_name: The name of IoT Connector resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input[Union[str, 'IotIdentityResolutionType']] resource_identity_resolution_type: Determines how resource identity is resolved on the destination.
        :param pulumi.Input[str] workspace_name: The name of workspace resource.
        :param pulumi.Input[str] fhir_destination_name: The name of IoT Connector FHIR destination resource.
        :param pulumi.Input[str] location: The resource location.
        """
        pulumi.set(__self__, "fhir_mapping", fhir_mapping)
        pulumi.set(__self__, "fhir_service_resource_id", fhir_service_resource_id)
        pulumi.set(__self__, "iot_connector_name", iot_connector_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_identity_resolution_type", resource_identity_resolution_type)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if fhir_destination_name is not None:
            pulumi.set(__self__, "fhir_destination_name", fhir_destination_name)
        if location is not None:
            pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter(name="fhirMapping")
    def fhir_mapping(self) -> pulumi.Input['IotMappingPropertiesArgs']:
        """
        FHIR Mappings
        """
        return pulumi.get(self, "fhir_mapping")

    @fhir_mapping.setter
    def fhir_mapping(self, value: pulumi.Input['IotMappingPropertiesArgs']):
        pulumi.set(self, "fhir_mapping", value)

    @property
    @pulumi.getter(name="fhirServiceResourceId")
    def fhir_service_resource_id(self) -> pulumi.Input[str]:
        """
        Fully qualified resource id of the FHIR service to connect to.
        """
        return pulumi.get(self, "fhir_service_resource_id")

    @fhir_service_resource_id.setter
    def fhir_service_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "fhir_service_resource_id", value)

    @property
    @pulumi.getter(name="iotConnectorName")
    def iot_connector_name(self) -> pulumi.Input[str]:
        """
        The name of IoT Connector resource.
        """
        return pulumi.get(self, "iot_connector_name")

    @iot_connector_name.setter
    def iot_connector_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "iot_connector_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the service instance.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceIdentityResolutionType")
    def resource_identity_resolution_type(self) -> pulumi.Input[Union[str, 'IotIdentityResolutionType']]:
        """
        Determines how resource identity is resolved on the destination.
        """
        return pulumi.get(self, "resource_identity_resolution_type")

    @resource_identity_resolution_type.setter
    def resource_identity_resolution_type(self, value: pulumi.Input[Union[str, 'IotIdentityResolutionType']]):
        pulumi.set(self, "resource_identity_resolution_type", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of workspace resource.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="fhirDestinationName")
    def fhir_destination_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of IoT Connector FHIR destination resource.
        """
        return pulumi.get(self, "fhir_destination_name")

    @fhir_destination_name.setter
    def fhir_destination_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fhir_destination_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)


warnings.warn("""Version v20211101 will be removed in the next major version of the provider. Upgrade to version v20220515 or later.""", DeprecationWarning)


class IotConnectorFhirDestination(pulumi.CustomResource):
    warnings.warn("""Version v20211101 will be removed in the next major version of the provider. Upgrade to version v20220515 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fhir_destination_name: Optional[pulumi.Input[str]] = None,
                 fhir_mapping: Optional[pulumi.Input[pulumi.InputType['IotMappingPropertiesArgs']]] = None,
                 fhir_service_resource_id: Optional[pulumi.Input[str]] = None,
                 iot_connector_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_identity_resolution_type: Optional[pulumi.Input[Union[str, 'IotIdentityResolutionType']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        IoT Connector FHIR destination definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fhir_destination_name: The name of IoT Connector FHIR destination resource.
        :param pulumi.Input[pulumi.InputType['IotMappingPropertiesArgs']] fhir_mapping: FHIR Mappings
        :param pulumi.Input[str] fhir_service_resource_id: Fully qualified resource id of the FHIR service to connect to.
        :param pulumi.Input[str] iot_connector_name: The name of IoT Connector resource.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input[Union[str, 'IotIdentityResolutionType']] resource_identity_resolution_type: Determines how resource identity is resolved on the destination.
        :param pulumi.Input[str] workspace_name: The name of workspace resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotConnectorFhirDestinationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        IoT Connector FHIR destination definition.

        :param str resource_name: The name of the resource.
        :param IotConnectorFhirDestinationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotConnectorFhirDestinationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fhir_destination_name: Optional[pulumi.Input[str]] = None,
                 fhir_mapping: Optional[pulumi.Input[pulumi.InputType['IotMappingPropertiesArgs']]] = None,
                 fhir_service_resource_id: Optional[pulumi.Input[str]] = None,
                 iot_connector_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_identity_resolution_type: Optional[pulumi.Input[Union[str, 'IotIdentityResolutionType']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""IotConnectorFhirDestination is deprecated: Version v20211101 will be removed in the next major version of the provider. Upgrade to version v20220515 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IotConnectorFhirDestinationArgs.__new__(IotConnectorFhirDestinationArgs)

            __props__.__dict__["fhir_destination_name"] = fhir_destination_name
            if fhir_mapping is None and not opts.urn:
                raise TypeError("Missing required property 'fhir_mapping'")
            __props__.__dict__["fhir_mapping"] = fhir_mapping
            if fhir_service_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'fhir_service_resource_id'")
            __props__.__dict__["fhir_service_resource_id"] = fhir_service_resource_id
            if iot_connector_name is None and not opts.urn:
                raise TypeError("Missing required property 'iot_connector_name'")
            __props__.__dict__["iot_connector_name"] = iot_connector_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_identity_resolution_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_identity_resolution_type'")
            __props__.__dict__["resource_identity_resolution_type"] = resource_identity_resolution_type
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:healthcareapis:IotConnectorFhirDestination"), pulumi.Alias(type_="azure-native:healthcareapis/v20210601preview:IotConnectorFhirDestination"), pulumi.Alias(type_="azure-native:healthcareapis/v20220131preview:IotConnectorFhirDestination"), pulumi.Alias(type_="azure-native:healthcareapis/v20220515:IotConnectorFhirDestination")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotConnectorFhirDestination, __self__).__init__(
            'azure-native:healthcareapis/v20211101:IotConnectorFhirDestination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotConnectorFhirDestination':
        """
        Get an existing IotConnectorFhirDestination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotConnectorFhirDestinationArgs.__new__(IotConnectorFhirDestinationArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["fhir_mapping"] = None
        __props__.__dict__["fhir_service_resource_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_identity_resolution_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return IotConnectorFhirDestination(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        An etag associated with the resource, used for optimistic concurrency when editing it.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="fhirMapping")
    def fhir_mapping(self) -> pulumi.Output['outputs.IotMappingPropertiesResponse']:
        """
        FHIR Mappings
        """
        return pulumi.get(self, "fhir_mapping")

    @property
    @pulumi.getter(name="fhirServiceResourceId")
    def fhir_service_resource_id(self) -> pulumi.Output[str]:
        """
        Fully qualified resource id of the FHIR service to connect to.
        """
        return pulumi.get(self, "fhir_service_resource_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceIdentityResolutionType")
    def resource_identity_resolution_type(self) -> pulumi.Output[str]:
        """
        Determines how resource identity is resolved on the destination.
        """
        return pulumi.get(self, "resource_identity_resolution_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

