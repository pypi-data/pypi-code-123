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
    'GetLoadBalancerResult',
    'AwaitableGetLoadBalancerResult',
    'get_load_balancer',
    'get_load_balancer_output',
]

@pulumi.output_type
class GetLoadBalancerResult:
    def __init__(__self__, attached_instances=None, health_check_path=None, load_balancer_arn=None, session_stickiness_enabled=None, session_stickiness_lb_cookie_duration_seconds=None, tags=None, tls_policy_name=None):
        if attached_instances and not isinstance(attached_instances, list):
            raise TypeError("Expected argument 'attached_instances' to be a list")
        pulumi.set(__self__, "attached_instances", attached_instances)
        if health_check_path and not isinstance(health_check_path, str):
            raise TypeError("Expected argument 'health_check_path' to be a str")
        pulumi.set(__self__, "health_check_path", health_check_path)
        if load_balancer_arn and not isinstance(load_balancer_arn, str):
            raise TypeError("Expected argument 'load_balancer_arn' to be a str")
        pulumi.set(__self__, "load_balancer_arn", load_balancer_arn)
        if session_stickiness_enabled and not isinstance(session_stickiness_enabled, bool):
            raise TypeError("Expected argument 'session_stickiness_enabled' to be a bool")
        pulumi.set(__self__, "session_stickiness_enabled", session_stickiness_enabled)
        if session_stickiness_lb_cookie_duration_seconds and not isinstance(session_stickiness_lb_cookie_duration_seconds, str):
            raise TypeError("Expected argument 'session_stickiness_lb_cookie_duration_seconds' to be a str")
        pulumi.set(__self__, "session_stickiness_lb_cookie_duration_seconds", session_stickiness_lb_cookie_duration_seconds)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tls_policy_name and not isinstance(tls_policy_name, str):
            raise TypeError("Expected argument 'tls_policy_name' to be a str")
        pulumi.set(__self__, "tls_policy_name", tls_policy_name)

    @property
    @pulumi.getter(name="attachedInstances")
    def attached_instances(self) -> Optional[Sequence[str]]:
        """
        The names of the instances attached to the load balancer.
        """
        return pulumi.get(self, "attached_instances")

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[str]:
        """
        The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "/").
        """
        return pulumi.get(self, "health_check_path")

    @property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> Optional[str]:
        return pulumi.get(self, "load_balancer_arn")

    @property
    @pulumi.getter(name="sessionStickinessEnabled")
    def session_stickiness_enabled(self) -> Optional[bool]:
        """
        Configuration option to enable session stickiness.
        """
        return pulumi.get(self, "session_stickiness_enabled")

    @property
    @pulumi.getter(name="sessionStickinessLBCookieDurationSeconds")
    def session_stickiness_lb_cookie_duration_seconds(self) -> Optional[str]:
        """
        Configuration option to adjust session stickiness cookie duration parameter.
        """
        return pulumi.get(self, "session_stickiness_lb_cookie_duration_seconds")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LoadBalancerTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tlsPolicyName")
    def tls_policy_name(self) -> Optional[str]:
        """
        The name of the TLS policy to apply to the load balancer.
        """
        return pulumi.get(self, "tls_policy_name")


class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            attached_instances=self.attached_instances,
            health_check_path=self.health_check_path,
            load_balancer_arn=self.load_balancer_arn,
            session_stickiness_enabled=self.session_stickiness_enabled,
            session_stickiness_lb_cookie_duration_seconds=self.session_stickiness_lb_cookie_duration_seconds,
            tags=self.tags,
            tls_policy_name=self.tls_policy_name)


def get_load_balancer(load_balancer_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerResult:
    """
    Resource Type definition for AWS::Lightsail::LoadBalancer


    :param str load_balancer_name: The name of your load balancer.
    """
    __args__ = dict()
    __args__['loadBalancerName'] = load_balancer_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:lightsail:getLoadBalancer', __args__, opts=opts, typ=GetLoadBalancerResult).value

    return AwaitableGetLoadBalancerResult(
        attached_instances=__ret__.attached_instances,
        health_check_path=__ret__.health_check_path,
        load_balancer_arn=__ret__.load_balancer_arn,
        session_stickiness_enabled=__ret__.session_stickiness_enabled,
        session_stickiness_lb_cookie_duration_seconds=__ret__.session_stickiness_lb_cookie_duration_seconds,
        tags=__ret__.tags,
        tls_policy_name=__ret__.tls_policy_name)


@_utilities.lift_output_func(get_load_balancer)
def get_load_balancer_output(load_balancer_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoadBalancerResult]:
    """
    Resource Type definition for AWS::Lightsail::LoadBalancer


    :param str load_balancer_name: The name of your load balancer.
    """
    ...
