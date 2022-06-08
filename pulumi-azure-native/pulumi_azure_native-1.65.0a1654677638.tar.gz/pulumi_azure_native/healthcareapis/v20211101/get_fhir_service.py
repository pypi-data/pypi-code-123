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
    'GetFhirServiceResult',
    'AwaitableGetFhirServiceResult',
    'get_fhir_service',
    'get_fhir_service_output',
]

warnings.warn("""Version v20211101 will be removed in the next major version of the provider. Upgrade to version v20220515 or later.""", DeprecationWarning)

@pulumi.output_type
class GetFhirServiceResult:
    """
    The description of Fhir Service
    """
    def __init__(__self__, access_policies=None, acr_configuration=None, authentication_configuration=None, cors_configuration=None, etag=None, event_state=None, export_configuration=None, id=None, identity=None, kind=None, location=None, name=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, resource_version_policy_configuration=None, system_data=None, tags=None, type=None):
        if access_policies and not isinstance(access_policies, list):
            raise TypeError("Expected argument 'access_policies' to be a list")
        pulumi.set(__self__, "access_policies", access_policies)
        if acr_configuration and not isinstance(acr_configuration, dict):
            raise TypeError("Expected argument 'acr_configuration' to be a dict")
        pulumi.set(__self__, "acr_configuration", acr_configuration)
        if authentication_configuration and not isinstance(authentication_configuration, dict):
            raise TypeError("Expected argument 'authentication_configuration' to be a dict")
        pulumi.set(__self__, "authentication_configuration", authentication_configuration)
        if cors_configuration and not isinstance(cors_configuration, dict):
            raise TypeError("Expected argument 'cors_configuration' to be a dict")
        pulumi.set(__self__, "cors_configuration", cors_configuration)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if event_state and not isinstance(event_state, str):
            raise TypeError("Expected argument 'event_state' to be a str")
        pulumi.set(__self__, "event_state", event_state)
        if export_configuration and not isinstance(export_configuration, dict):
            raise TypeError("Expected argument 'export_configuration' to be a dict")
        pulumi.set(__self__, "export_configuration", export_configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if resource_version_policy_configuration and not isinstance(resource_version_policy_configuration, dict):
            raise TypeError("Expected argument 'resource_version_policy_configuration' to be a dict")
        pulumi.set(__self__, "resource_version_policy_configuration", resource_version_policy_configuration)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Sequence['outputs.FhirServiceAccessPolicyEntryResponse']]:
        """
        Fhir Service access policies.
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(self) -> Optional['outputs.FhirServiceAcrConfigurationResponse']:
        """
        Fhir Service Azure container registry configuration.
        """
        return pulumi.get(self, "acr_configuration")

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional['outputs.FhirServiceAuthenticationConfigurationResponse']:
        """
        Fhir Service authentication configuration.
        """
        return pulumi.get(self, "authentication_configuration")

    @property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional['outputs.FhirServiceCorsConfigurationResponse']:
        """
        Fhir Service Cors configuration.
        """
        return pulumi.get(self, "cors_configuration")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        An etag associated with the resource, used for optimistic concurrency when editing it.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="eventState")
    def event_state(self) -> str:
        """
        Fhir Service event support status.
        """
        return pulumi.get(self, "event_state")

    @property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(self) -> Optional['outputs.FhirServiceExportConfigurationResponse']:
        """
        Fhir Service export configuration.
        """
        return pulumi.get(self, "export_configuration")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ServiceManagedIdentityResponseIdentity']:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The kind of the service.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        The list of private endpoint connections that are set up for this resource.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> str:
        """
        Control permission for data plane traffic coming from public networks while private endpoint is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="resourceVersionPolicyConfiguration")
    def resource_version_policy_configuration(self) -> Optional['outputs.ResourceVersionPolicyConfigurationResponse']:
        """
        Determines tracking of history for resources.
        """
        return pulumi.get(self, "resource_version_policy_configuration")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetFhirServiceResult(GetFhirServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFhirServiceResult(
            access_policies=self.access_policies,
            acr_configuration=self.acr_configuration,
            authentication_configuration=self.authentication_configuration,
            cors_configuration=self.cors_configuration,
            etag=self.etag,
            event_state=self.event_state,
            export_configuration=self.export_configuration,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            resource_version_policy_configuration=self.resource_version_policy_configuration,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_fhir_service(fhir_service_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     workspace_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFhirServiceResult:
    """
    The description of Fhir Service


    :param str fhir_service_name: The name of FHIR Service resource.
    :param str resource_group_name: The name of the resource group that contains the service instance.
    :param str workspace_name: The name of workspace resource.
    """
    pulumi.log.warn("""get_fhir_service is deprecated: Version v20211101 will be removed in the next major version of the provider. Upgrade to version v20220515 or later.""")
    __args__ = dict()
    __args__['fhirServiceName'] = fhir_service_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:healthcareapis/v20211101:getFhirService', __args__, opts=opts, typ=GetFhirServiceResult).value

    return AwaitableGetFhirServiceResult(
        access_policies=__ret__.access_policies,
        acr_configuration=__ret__.acr_configuration,
        authentication_configuration=__ret__.authentication_configuration,
        cors_configuration=__ret__.cors_configuration,
        etag=__ret__.etag,
        event_state=__ret__.event_state,
        export_configuration=__ret__.export_configuration,
        id=__ret__.id,
        identity=__ret__.identity,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        private_endpoint_connections=__ret__.private_endpoint_connections,
        provisioning_state=__ret__.provisioning_state,
        public_network_access=__ret__.public_network_access,
        resource_version_policy_configuration=__ret__.resource_version_policy_configuration,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_fhir_service)
def get_fhir_service_output(fhir_service_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            workspace_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFhirServiceResult]:
    """
    The description of Fhir Service


    :param str fhir_service_name: The name of FHIR Service resource.
    :param str resource_group_name: The name of the resource group that contains the service instance.
    :param str workspace_name: The name of workspace resource.
    """
    pulumi.log.warn("""get_fhir_service is deprecated: Version v20211101 will be removed in the next major version of the provider. Upgrade to version v20220515 or later.""")
    ...
