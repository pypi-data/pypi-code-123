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
    'GetHostPoolResult',
    'AwaitableGetHostPoolResult',
    'get_host_pool',
    'get_host_pool_output',
]

warnings.warn("""Version v20200921preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""", DeprecationWarning)

@pulumi.output_type
class GetHostPoolResult:
    """
    Represents a HostPool definition.
    """
    def __init__(__self__, application_group_references=None, custom_rdp_property=None, description=None, friendly_name=None, host_pool_type=None, id=None, load_balancer_type=None, location=None, max_session_limit=None, name=None, personal_desktop_assignment_type=None, preferred_app_group_type=None, registration_info=None, ring=None, sso_context=None, tags=None, type=None, validation_environment=None, vm_template=None):
        if application_group_references and not isinstance(application_group_references, list):
            raise TypeError("Expected argument 'application_group_references' to be a list")
        pulumi.set(__self__, "application_group_references", application_group_references)
        if custom_rdp_property and not isinstance(custom_rdp_property, str):
            raise TypeError("Expected argument 'custom_rdp_property' to be a str")
        pulumi.set(__self__, "custom_rdp_property", custom_rdp_property)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if host_pool_type and not isinstance(host_pool_type, str):
            raise TypeError("Expected argument 'host_pool_type' to be a str")
        pulumi.set(__self__, "host_pool_type", host_pool_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if load_balancer_type and not isinstance(load_balancer_type, str):
            raise TypeError("Expected argument 'load_balancer_type' to be a str")
        pulumi.set(__self__, "load_balancer_type", load_balancer_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_session_limit and not isinstance(max_session_limit, int):
            raise TypeError("Expected argument 'max_session_limit' to be a int")
        pulumi.set(__self__, "max_session_limit", max_session_limit)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if personal_desktop_assignment_type and not isinstance(personal_desktop_assignment_type, str):
            raise TypeError("Expected argument 'personal_desktop_assignment_type' to be a str")
        pulumi.set(__self__, "personal_desktop_assignment_type", personal_desktop_assignment_type)
        if preferred_app_group_type and not isinstance(preferred_app_group_type, str):
            raise TypeError("Expected argument 'preferred_app_group_type' to be a str")
        pulumi.set(__self__, "preferred_app_group_type", preferred_app_group_type)
        if registration_info and not isinstance(registration_info, dict):
            raise TypeError("Expected argument 'registration_info' to be a dict")
        pulumi.set(__self__, "registration_info", registration_info)
        if ring and not isinstance(ring, int):
            raise TypeError("Expected argument 'ring' to be a int")
        pulumi.set(__self__, "ring", ring)
        if sso_context and not isinstance(sso_context, str):
            raise TypeError("Expected argument 'sso_context' to be a str")
        pulumi.set(__self__, "sso_context", sso_context)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if validation_environment and not isinstance(validation_environment, bool):
            raise TypeError("Expected argument 'validation_environment' to be a bool")
        pulumi.set(__self__, "validation_environment", validation_environment)
        if vm_template and not isinstance(vm_template, str):
            raise TypeError("Expected argument 'vm_template' to be a str")
        pulumi.set(__self__, "vm_template", vm_template)

    @property
    @pulumi.getter(name="applicationGroupReferences")
    def application_group_references(self) -> Sequence[str]:
        """
        List of applicationGroup links.
        """
        return pulumi.get(self, "application_group_references")

    @property
    @pulumi.getter(name="customRdpProperty")
    def custom_rdp_property(self) -> Optional[str]:
        """
        Custom rdp property of HostPool.
        """
        return pulumi.get(self, "custom_rdp_property")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of HostPool.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Friendly name of HostPool.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPoolType")
    def host_pool_type(self) -> str:
        """
        HostPool type for desktop.
        """
        return pulumi.get(self, "host_pool_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> str:
        """
        The type of the load balancer.
        """
        return pulumi.get(self, "load_balancer_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxSessionLimit")
    def max_session_limit(self) -> Optional[int]:
        """
        The max session limit of HostPool.
        """
        return pulumi.get(self, "max_session_limit")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="personalDesktopAssignmentType")
    def personal_desktop_assignment_type(self) -> Optional[str]:
        """
        PersonalDesktopAssignment type for HostPool.
        """
        return pulumi.get(self, "personal_desktop_assignment_type")

    @property
    @pulumi.getter(name="preferredAppGroupType")
    def preferred_app_group_type(self) -> str:
        """
        The type of preferred application group type, default to Desktop Application Group
        """
        return pulumi.get(self, "preferred_app_group_type")

    @property
    @pulumi.getter(name="registrationInfo")
    def registration_info(self) -> Optional['outputs.RegistrationInfoResponse']:
        """
        The registration info of HostPool.
        """
        return pulumi.get(self, "registration_info")

    @property
    @pulumi.getter
    def ring(self) -> Optional[int]:
        """
        The ring number of HostPool.
        """
        return pulumi.get(self, "ring")

    @property
    @pulumi.getter(name="ssoContext")
    def sso_context(self) -> Optional[str]:
        """
        Path to keyvault containing ssoContext secret.
        """
        return pulumi.get(self, "sso_context")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationEnvironment")
    def validation_environment(self) -> Optional[bool]:
        """
        Is validation environment.
        """
        return pulumi.get(self, "validation_environment")

    @property
    @pulumi.getter(name="vmTemplate")
    def vm_template(self) -> Optional[str]:
        """
        VM template for sessionhosts configuration within hostpool.
        """
        return pulumi.get(self, "vm_template")


class AwaitableGetHostPoolResult(GetHostPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHostPoolResult(
            application_group_references=self.application_group_references,
            custom_rdp_property=self.custom_rdp_property,
            description=self.description,
            friendly_name=self.friendly_name,
            host_pool_type=self.host_pool_type,
            id=self.id,
            load_balancer_type=self.load_balancer_type,
            location=self.location,
            max_session_limit=self.max_session_limit,
            name=self.name,
            personal_desktop_assignment_type=self.personal_desktop_assignment_type,
            preferred_app_group_type=self.preferred_app_group_type,
            registration_info=self.registration_info,
            ring=self.ring,
            sso_context=self.sso_context,
            tags=self.tags,
            type=self.type,
            validation_environment=self.validation_environment,
            vm_template=self.vm_template)


def get_host_pool(host_pool_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHostPoolResult:
    """
    Represents a HostPool definition.


    :param str host_pool_name: The name of the host pool within the specified resource group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    pulumi.log.warn("""get_host_pool is deprecated: Version v20200921preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""")
    __args__ = dict()
    __args__['hostPoolName'] = host_pool_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20200921preview:getHostPool', __args__, opts=opts, typ=GetHostPoolResult).value

    return AwaitableGetHostPoolResult(
        application_group_references=__ret__.application_group_references,
        custom_rdp_property=__ret__.custom_rdp_property,
        description=__ret__.description,
        friendly_name=__ret__.friendly_name,
        host_pool_type=__ret__.host_pool_type,
        id=__ret__.id,
        load_balancer_type=__ret__.load_balancer_type,
        location=__ret__.location,
        max_session_limit=__ret__.max_session_limit,
        name=__ret__.name,
        personal_desktop_assignment_type=__ret__.personal_desktop_assignment_type,
        preferred_app_group_type=__ret__.preferred_app_group_type,
        registration_info=__ret__.registration_info,
        ring=__ret__.ring,
        sso_context=__ret__.sso_context,
        tags=__ret__.tags,
        type=__ret__.type,
        validation_environment=__ret__.validation_environment,
        vm_template=__ret__.vm_template)


@_utilities.lift_output_func(get_host_pool)
def get_host_pool_output(host_pool_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHostPoolResult]:
    """
    Represents a HostPool definition.


    :param str host_pool_name: The name of the host pool within the specified resource group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    pulumi.log.warn("""get_host_pool is deprecated: Version v20200921preview will be removed in the next major version of the provider. Upgrade to version v20210201preview or later.""")
    ...
