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
    'GetIntegrationAccountCertificateResult',
    'AwaitableGetIntegrationAccountCertificateResult',
    'get_integration_account_certificate',
    'get_integration_account_certificate_output',
]

@pulumi.output_type
class GetIntegrationAccountCertificateResult:
    """
    The integration account certificate.
    """
    def __init__(__self__, changed_time=None, created_time=None, id=None, key=None, location=None, metadata=None, name=None, public_certificate=None, tags=None, type=None):
        if changed_time and not isinstance(changed_time, str):
            raise TypeError("Expected argument 'changed_time' to be a str")
        pulumi.set(__self__, "changed_time", changed_time)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key and not isinstance(key, dict):
            raise TypeError("Expected argument 'key' to be a dict")
        pulumi.set(__self__, "key", key)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_certificate and not isinstance(public_certificate, str):
            raise TypeError("Expected argument 'public_certificate' to be a str")
        pulumi.set(__self__, "public_certificate", public_certificate)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> str:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def key(self) -> Optional['outputs.KeyVaultKeyReferenceResponse']:
        """
        The key details in the key vault.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicCertificate")
    def public_certificate(self) -> Optional[str]:
        """
        The public certificate.
        """
        return pulumi.get(self, "public_certificate")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIntegrationAccountCertificateResult(GetIntegrationAccountCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationAccountCertificateResult(
            changed_time=self.changed_time,
            created_time=self.created_time,
            id=self.id,
            key=self.key,
            location=self.location,
            metadata=self.metadata,
            name=self.name,
            public_certificate=self.public_certificate,
            tags=self.tags,
            type=self.type)


def get_integration_account_certificate(certificate_name: Optional[str] = None,
                                        integration_account_name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationAccountCertificateResult:
    """
    The integration account certificate.


    :param str certificate_name: The integration account certificate name.
    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['certificateName'] = certificate_name
    __args__['integrationAccountName'] = integration_account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:logic/v20180701preview:getIntegrationAccountCertificate', __args__, opts=opts, typ=GetIntegrationAccountCertificateResult).value

    return AwaitableGetIntegrationAccountCertificateResult(
        changed_time=__ret__.changed_time,
        created_time=__ret__.created_time,
        id=__ret__.id,
        key=__ret__.key,
        location=__ret__.location,
        metadata=__ret__.metadata,
        name=__ret__.name,
        public_certificate=__ret__.public_certificate,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_integration_account_certificate)
def get_integration_account_certificate_output(certificate_name: Optional[pulumi.Input[str]] = None,
                                               integration_account_name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationAccountCertificateResult]:
    """
    The integration account certificate.


    :param str certificate_name: The integration account certificate name.
    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    """
    ...
