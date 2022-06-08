# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetAlertRuleResult',
    'AwaitableGetAlertRuleResult',
    'get_alert_rule',
    'get_alert_rule_output',
]

warnings.warn("""Please use one of the variants: FusionAlertRule, MicrosoftSecurityIncidentCreationAlertRule, ScheduledAlertRule.""", DeprecationWarning)

@pulumi.output_type
class GetAlertRuleResult:
    """
    Alert rule.
    """
    def __init__(__self__, etag=None, id=None, kind=None, name=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The alert rule kind
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetAlertRuleResult(GetAlertRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAlertRuleResult(
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            name=self.name,
            type=self.type)


def get_alert_rule(resource_group_name: Optional[str] = None,
                   rule_id: Optional[str] = None,
                   workspace_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAlertRuleResult:
    """
    Alert rule.
    API Version: 2020-01-01.


    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str rule_id: Alert rule ID
    :param str workspace_name: The name of the workspace.
    """
    pulumi.log.warn("""get_alert_rule is deprecated: Please use one of the variants: FusionAlertRule, MicrosoftSecurityIncidentCreationAlertRule, ScheduledAlertRule.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleId'] = rule_id
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights:getAlertRule', __args__, opts=opts, typ=GetAlertRuleResult).value

    return AwaitableGetAlertRuleResult(
        etag=__ret__.etag,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_alert_rule)
def get_alert_rule_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                          rule_id: Optional[pulumi.Input[str]] = None,
                          workspace_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAlertRuleResult]:
    """
    Alert rule.
    API Version: 2020-01-01.


    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str rule_id: Alert rule ID
    :param str workspace_name: The name of the workspace.
    """
    pulumi.log.warn("""get_alert_rule is deprecated: Please use one of the variants: FusionAlertRule, MicrosoftSecurityIncidentCreationAlertRule, ScheduledAlertRule.""")
    ...
