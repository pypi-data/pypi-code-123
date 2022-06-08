# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetLifecyclePolicyResult',
    'AwaitableGetLifecyclePolicyResult',
    'get_lifecycle_policy',
    'get_lifecycle_policy_output',
]

@pulumi.output_type
class GetLifecyclePolicyResult:
    def __init__(__self__, arn=None, description=None, execution_role_arn=None, id=None, policy_details=None, state=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if execution_role_arn and not isinstance(execution_role_arn, str):
            raise TypeError("Expected argument 'execution_role_arn' to be a str")
        pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_details and not isinstance(policy_details, dict):
            raise TypeError("Expected argument 'policy_details' to be a dict")
        pulumi.set(__self__, "policy_details", policy_details)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[str]:
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyDetails")
    def policy_details(self) -> Optional['outputs.LifecyclePolicyPolicyDetails']:
        return pulumi.get(self, "policy_details")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LifecyclePolicyTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetLifecyclePolicyResult(GetLifecyclePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLifecyclePolicyResult(
            arn=self.arn,
            description=self.description,
            execution_role_arn=self.execution_role_arn,
            id=self.id,
            policy_details=self.policy_details,
            state=self.state,
            tags=self.tags)


def get_lifecycle_policy(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLifecyclePolicyResult:
    """
    Resource Type definition for AWS::DLM::LifecyclePolicy
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:dlm:getLifecyclePolicy', __args__, opts=opts, typ=GetLifecyclePolicyResult).value

    return AwaitableGetLifecyclePolicyResult(
        arn=__ret__.arn,
        description=__ret__.description,
        execution_role_arn=__ret__.execution_role_arn,
        id=__ret__.id,
        policy_details=__ret__.policy_details,
        state=__ret__.state,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_lifecycle_policy)
def get_lifecycle_policy_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLifecyclePolicyResult]:
    """
    Resource Type definition for AWS::DLM::LifecyclePolicy
    """
    ...
