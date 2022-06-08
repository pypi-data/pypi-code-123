# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetLaunchTemplateConstraintResult',
    'AwaitableGetLaunchTemplateConstraintResult',
    'get_launch_template_constraint',
    'get_launch_template_constraint_output',
]

@pulumi.output_type
class GetLaunchTemplateConstraintResult:
    def __init__(__self__, accept_language=None, description=None, id=None, rules=None):
        if accept_language and not isinstance(accept_language, str):
            raise TypeError("Expected argument 'accept_language' to be a str")
        pulumi.set(__self__, "accept_language", accept_language)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rules and not isinstance(rules, str):
            raise TypeError("Expected argument 'rules' to be a str")
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[str]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def rules(self) -> Optional[str]:
        return pulumi.get(self, "rules")


class AwaitableGetLaunchTemplateConstraintResult(GetLaunchTemplateConstraintResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLaunchTemplateConstraintResult(
            accept_language=self.accept_language,
            description=self.description,
            id=self.id,
            rules=self.rules)


def get_launch_template_constraint(id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLaunchTemplateConstraintResult:
    """
    Resource Type definition for AWS::ServiceCatalog::LaunchTemplateConstraint
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalog:getLaunchTemplateConstraint', __args__, opts=opts, typ=GetLaunchTemplateConstraintResult).value

    return AwaitableGetLaunchTemplateConstraintResult(
        accept_language=__ret__.accept_language,
        description=__ret__.description,
        id=__ret__.id,
        rules=__ret__.rules)


@_utilities.lift_output_func(get_launch_template_constraint)
def get_launch_template_constraint_output(id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLaunchTemplateConstraintResult]:
    """
    Resource Type definition for AWS::ServiceCatalog::LaunchTemplateConstraint
    """
    ...
