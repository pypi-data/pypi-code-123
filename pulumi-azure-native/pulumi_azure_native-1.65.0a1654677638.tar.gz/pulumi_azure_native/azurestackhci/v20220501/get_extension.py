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
    'GetExtensionResult',
    'AwaitableGetExtensionResult',
    'get_extension',
    'get_extension_output',
]

@pulumi.output_type
class GetExtensionResult:
    """
    Details of a particular extension in HCI Cluster.
    """
    def __init__(__self__, aggregate_state=None, auto_upgrade_minor_version=None, created_at=None, created_by=None, created_by_type=None, force_update_tag=None, id=None, last_modified_at=None, last_modified_by=None, last_modified_by_type=None, name=None, per_node_extension_details=None, protected_settings=None, provisioning_state=None, publisher=None, settings=None, type=None, type_handler_version=None):
        if aggregate_state and not isinstance(aggregate_state, str):
            raise TypeError("Expected argument 'aggregate_state' to be a str")
        pulumi.set(__self__, "aggregate_state", aggregate_state)
        if auto_upgrade_minor_version and not isinstance(auto_upgrade_minor_version, bool):
            raise TypeError("Expected argument 'auto_upgrade_minor_version' to be a bool")
        pulumi.set(__self__, "auto_upgrade_minor_version", auto_upgrade_minor_version)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if created_by_type and not isinstance(created_by_type, str):
            raise TypeError("Expected argument 'created_by_type' to be a str")
        pulumi.set(__self__, "created_by_type", created_by_type)
        if force_update_tag and not isinstance(force_update_tag, str):
            raise TypeError("Expected argument 'force_update_tag' to be a str")
        pulumi.set(__self__, "force_update_tag", force_update_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_at and not isinstance(last_modified_at, str):
            raise TypeError("Expected argument 'last_modified_at' to be a str")
        pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by and not isinstance(last_modified_by, str):
            raise TypeError("Expected argument 'last_modified_by' to be a str")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type and not isinstance(last_modified_by_type, str):
            raise TypeError("Expected argument 'last_modified_by_type' to be a str")
        pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if per_node_extension_details and not isinstance(per_node_extension_details, list):
            raise TypeError("Expected argument 'per_node_extension_details' to be a list")
        pulumi.set(__self__, "per_node_extension_details", per_node_extension_details)
        if protected_settings and not isinstance(protected_settings, dict):
            raise TypeError("Expected argument 'protected_settings' to be a dict")
        pulumi.set(__self__, "protected_settings", protected_settings)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if publisher and not isinstance(publisher, str):
            raise TypeError("Expected argument 'publisher' to be a str")
        pulumi.set(__self__, "publisher", publisher)
        if settings and not isinstance(settings, dict):
            raise TypeError("Expected argument 'settings' to be a dict")
        pulumi.set(__self__, "settings", settings)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if type_handler_version and not isinstance(type_handler_version, str):
            raise TypeError("Expected argument 'type_handler_version' to be a str")
        pulumi.set(__self__, "type_handler_version", type_handler_version)

    @property
    @pulumi.getter(name="aggregateState")
    def aggregate_state(self) -> str:
        """
        Aggregate state of Arc Extensions across the nodes in this HCI cluster.
        """
        return pulumi.get(self, "aggregate_state")

    @property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[bool]:
        """
        Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[str]:
        """
        How the extension handler should be forced to update even if the extension configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perNodeExtensionDetails")
    def per_node_extension_details(self) -> Sequence['outputs.PerNodeExtensionStateResponse']:
        """
        State of Arc Extension in each of the nodes.
        """
        return pulumi.get(self, "per_node_extension_details")

    @property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        """
        Protected settings (may contain secrets).
        """
        return pulumi.get(self, "protected_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Extension proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def publisher(self) -> Optional[str]:
        """
        The name of the extension handler publisher.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        """
        Json formatted public settings for the extension.
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[str]:
        """
        Specifies the version of the script handler.
        """
        return pulumi.get(self, "type_handler_version")


class AwaitableGetExtensionResult(GetExtensionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExtensionResult(
            aggregate_state=self.aggregate_state,
            auto_upgrade_minor_version=self.auto_upgrade_minor_version,
            created_at=self.created_at,
            created_by=self.created_by,
            created_by_type=self.created_by_type,
            force_update_tag=self.force_update_tag,
            id=self.id,
            last_modified_at=self.last_modified_at,
            last_modified_by=self.last_modified_by,
            last_modified_by_type=self.last_modified_by_type,
            name=self.name,
            per_node_extension_details=self.per_node_extension_details,
            protected_settings=self.protected_settings,
            provisioning_state=self.provisioning_state,
            publisher=self.publisher,
            settings=self.settings,
            type=self.type,
            type_handler_version=self.type_handler_version)


def get_extension(arc_setting_name: Optional[str] = None,
                  cluster_name: Optional[str] = None,
                  extension_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExtensionResult:
    """
    Details of a particular extension in HCI Cluster.


    :param str arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
    :param str cluster_name: The name of the cluster.
    :param str extension_name: The name of the machine extension.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['arcSettingName'] = arc_setting_name
    __args__['clusterName'] = cluster_name
    __args__['extensionName'] = extension_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20220501:getExtension', __args__, opts=opts, typ=GetExtensionResult).value

    return AwaitableGetExtensionResult(
        aggregate_state=__ret__.aggregate_state,
        auto_upgrade_minor_version=__ret__.auto_upgrade_minor_version,
        created_at=__ret__.created_at,
        created_by=__ret__.created_by,
        created_by_type=__ret__.created_by_type,
        force_update_tag=__ret__.force_update_tag,
        id=__ret__.id,
        last_modified_at=__ret__.last_modified_at,
        last_modified_by=__ret__.last_modified_by,
        last_modified_by_type=__ret__.last_modified_by_type,
        name=__ret__.name,
        per_node_extension_details=__ret__.per_node_extension_details,
        protected_settings=__ret__.protected_settings,
        provisioning_state=__ret__.provisioning_state,
        publisher=__ret__.publisher,
        settings=__ret__.settings,
        type=__ret__.type,
        type_handler_version=__ret__.type_handler_version)


@_utilities.lift_output_func(get_extension)
def get_extension_output(arc_setting_name: Optional[pulumi.Input[str]] = None,
                         cluster_name: Optional[pulumi.Input[str]] = None,
                         extension_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExtensionResult]:
    """
    Details of a particular extension in HCI Cluster.


    :param str arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
    :param str cluster_name: The name of the cluster.
    :param str extension_name: The name of the machine extension.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
