# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    """
    Certificate details.
    """
    def __init__(__self__, expiration_date=None, id=None, name=None, subject=None, thumbprint=None, type=None):
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        pulumi.set(__self__, "expiration_date", expiration_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if subject and not isinstance(subject, str):
            raise TypeError("Expected argument 'subject' to be a str")
        pulumi.set(__self__, "subject", subject)
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        pulumi.set(__self__, "thumbprint", thumbprint)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> str:
        """
        Expiration date of the certificate. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def subject(self) -> str:
        """
        Subject attribute of the certificate.
        """
        return pulumi.get(self, "subject")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        Thumbprint of the certificate.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            expiration_date=self.expiration_date,
            id=self.id,
            name=self.name,
            subject=self.subject,
            thumbprint=self.thumbprint,
            type=self.type)


def get_certificate(certificate_id: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    service_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Certificate details.


    :param str certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['certificateId'] = certificate_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20191201preview:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        expiration_date=__ret__.expiration_date,
        id=__ret__.id,
        name=__ret__.name,
        subject=__ret__.subject,
        thumbprint=__ret__.thumbprint,
        type=__ret__.type)


@_utilities.lift_output_func(get_certificate)
def get_certificate_output(certificate_id: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           service_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateResult]:
    """
    Certificate details.


    :param str certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
