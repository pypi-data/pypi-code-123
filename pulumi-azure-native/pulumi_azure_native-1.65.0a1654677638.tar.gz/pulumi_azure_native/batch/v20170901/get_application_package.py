# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetApplicationPackageResult',
    'AwaitableGetApplicationPackageResult',
    'get_application_package',
    'get_application_package_output',
]

warnings.warn("""Version v20170901 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""", DeprecationWarning)

@pulumi.output_type
class GetApplicationPackageResult:
    """
    An application package which represents a particular version of an application.
    """
    def __init__(__self__, format=None, id=None, last_activation_time=None, state=None, storage_url=None, storage_url_expiry=None, version=None):
        if format and not isinstance(format, str):
            raise TypeError("Expected argument 'format' to be a str")
        pulumi.set(__self__, "format", format)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_activation_time and not isinstance(last_activation_time, str):
            raise TypeError("Expected argument 'last_activation_time' to be a str")
        pulumi.set(__self__, "last_activation_time", last_activation_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_url and not isinstance(storage_url, str):
            raise TypeError("Expected argument 'storage_url' to be a str")
        pulumi.set(__self__, "storage_url", storage_url)
        if storage_url_expiry and not isinstance(storage_url_expiry, str):
            raise TypeError("Expected argument 'storage_url_expiry' to be a str")
        pulumi.set(__self__, "storage_url_expiry", storage_url_expiry)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def format(self) -> str:
        """
        The format of the application package, if the package is active.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the application.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastActivationTime")
    def last_activation_time(self) -> str:
        """
        The time at which the package was last activated, if the package is active.
        """
        return pulumi.get(self, "last_activation_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the application package.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageUrl")
    def storage_url(self) -> str:
        """
        The URL for the application package in Azure Storage.
        """
        return pulumi.get(self, "storage_url")

    @property
    @pulumi.getter(name="storageUrlExpiry")
    def storage_url_expiry(self) -> str:
        """
        The UTC time at which the Azure Storage URL will expire.
        """
        return pulumi.get(self, "storage_url_expiry")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the application package.
        """
        return pulumi.get(self, "version")


class AwaitableGetApplicationPackageResult(GetApplicationPackageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationPackageResult(
            format=self.format,
            id=self.id,
            last_activation_time=self.last_activation_time,
            state=self.state,
            storage_url=self.storage_url,
            storage_url_expiry=self.storage_url_expiry,
            version=self.version)


def get_application_package(account_name: Optional[str] = None,
                            application_id: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            version: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationPackageResult:
    """
    An application package which represents a particular version of an application.


    :param str account_name: The name of the Batch account.
    :param str application_id: The ID of the application.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    :param str version: The version of the application.
    """
    pulumi.log.warn("""get_application_package is deprecated: Version v20170901 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['applicationId'] = application_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['version'] = version
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:batch/v20170901:getApplicationPackage', __args__, opts=opts, typ=GetApplicationPackageResult).value

    return AwaitableGetApplicationPackageResult(
        format=__ret__.format,
        id=__ret__.id,
        last_activation_time=__ret__.last_activation_time,
        state=__ret__.state,
        storage_url=__ret__.storage_url,
        storage_url_expiry=__ret__.storage_url_expiry,
        version=__ret__.version)


@_utilities.lift_output_func(get_application_package)
def get_application_package_output(account_name: Optional[pulumi.Input[str]] = None,
                                   application_id: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   version: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationPackageResult]:
    """
    An application package which represents a particular version of an application.


    :param str account_name: The name of the Batch account.
    :param str application_id: The ID of the application.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    :param str version: The version of the application.
    """
    pulumi.log.warn("""get_application_package is deprecated: Version v20170901 will be removed in the next major version of the provider. Upgrade to version v20210101 or later.""")
    ...
