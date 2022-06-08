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
    'GetOrganizationResult',
    'AwaitableGetOrganizationResult',
    'get_organization',
    'get_organization_output',
]

@pulumi.output_type
class GetOrganizationResult:
    """
    Organization resource.
    """
    def __init__(__self__, created_time=None, id=None, location=None, name=None, offer_detail=None, organization_id=None, provisioning_state=None, sso_url=None, system_data=None, tags=None, type=None, user_detail=None):
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if offer_detail and not isinstance(offer_detail, dict):
            raise TypeError("Expected argument 'offer_detail' to be a dict")
        pulumi.set(__self__, "offer_detail", offer_detail)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sso_url and not isinstance(sso_url, str):
            raise TypeError("Expected argument 'sso_url' to be a str")
        pulumi.set(__self__, "sso_url", sso_url)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_detail and not isinstance(user_detail, dict):
            raise TypeError("Expected argument 'user_detail' to be a dict")
        pulumi.set(__self__, "user_detail", user_detail)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        The creation time of the resource.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM id of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location of Organization resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offerDetail")
    def offer_detail(self) -> 'outputs.OfferDetailResponse':
        """
        Confluent offer detail
        """
        return pulumi.get(self, "offer_detail")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        Id of the Confluent organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provision states for confluent RP
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ssoUrl")
    def sso_url(self) -> str:
        """
        SSO url for the Confluent organization.
        """
        return pulumi.get(self, "sso_url")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Organization resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userDetail")
    def user_detail(self) -> 'outputs.UserDetailResponse':
        """
        Subscriber detail
        """
        return pulumi.get(self, "user_detail")


class AwaitableGetOrganizationResult(GetOrganizationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationResult(
            created_time=self.created_time,
            id=self.id,
            location=self.location,
            name=self.name,
            offer_detail=self.offer_detail,
            organization_id=self.organization_id,
            provisioning_state=self.provisioning_state,
            sso_url=self.sso_url,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            user_detail=self.user_detail)


def get_organization(organization_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationResult:
    """
    Organization resource.


    :param str organization_name: Organization resource name
    :param str resource_group_name: Resource group name
    """
    __args__ = dict()
    __args__['organizationName'] = organization_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:confluent/v20211201:getOrganization', __args__, opts=opts, typ=GetOrganizationResult).value

    return AwaitableGetOrganizationResult(
        created_time=__ret__.created_time,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        offer_detail=__ret__.offer_detail,
        organization_id=__ret__.organization_id,
        provisioning_state=__ret__.provisioning_state,
        sso_url=__ret__.sso_url,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        user_detail=__ret__.user_detail)


@_utilities.lift_output_func(get_organization)
def get_organization_output(organization_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationResult]:
    """
    Organization resource.


    :param str organization_name: Organization resource name
    :param str resource_group_name: Resource group name
    """
    ...
