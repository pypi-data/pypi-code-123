# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['JobCredentialArgs', 'JobCredential']

@pulumi.input_type
class JobCredentialArgs:
    def __init__(__self__, *,
                 job_agent_name: pulumi.Input[str],
                 password: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 username: pulumi.Input[str],
                 credential_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a JobCredential resource.
        :param pulumi.Input[str] job_agent_name: The name of the job agent.
        :param pulumi.Input[str] password: The credential password.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] username: The credential user name.
        :param pulumi.Input[str] credential_name: The name of the credential.
        """
        pulumi.set(__self__, "job_agent_name", job_agent_name)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        pulumi.set(__self__, "username", username)
        if credential_name is not None:
            pulumi.set(__self__, "credential_name", credential_name)

    @property
    @pulumi.getter(name="jobAgentName")
    def job_agent_name(self) -> pulumi.Input[str]:
        """
        The name of the job agent.
        """
        return pulumi.get(self, "job_agent_name")

    @job_agent_name.setter
    def job_agent_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_agent_name", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The credential password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The credential user name.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the credential.
        """
        return pulumi.get(self, "credential_name")

    @credential_name.setter
    def credential_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_name", value)


class JobCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 job_agent_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A stored credential that can be used by a job to connect to target databases.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] credential_name: The name of the credential.
        :param pulumi.Input[str] job_agent_name: The name of the job agent.
        :param pulumi.Input[str] password: The credential password.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] username: The credential user name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobCredentialArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A stored credential that can be used by a job to connect to target databases.

        :param str resource_name: The name of the resource.
        :param JobCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 job_agent_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobCredentialArgs.__new__(JobCredentialArgs)

            __props__.__dict__["credential_name"] = credential_name
            if job_agent_name is None and not opts.urn:
                raise TypeError("Missing required property 'job_agent_name'")
            __props__.__dict__["job_agent_name"] = job_agent_name
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = password
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:JobCredential"), pulumi.Alias(type_="azure-native:sql/v20170301preview:JobCredential"), pulumi.Alias(type_="azure-native:sql/v20200202preview:JobCredential"), pulumi.Alias(type_="azure-native:sql/v20200801preview:JobCredential"), pulumi.Alias(type_="azure-native:sql/v20201101preview:JobCredential"), pulumi.Alias(type_="azure-native:sql/v20210201preview:JobCredential"), pulumi.Alias(type_="azure-native:sql/v20210501preview:JobCredential"), pulumi.Alias(type_="azure-native:sql/v20210801preview:JobCredential")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(JobCredential, __self__).__init__(
            'azure-native:sql/v20211101preview:JobCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobCredential':
        """
        Get an existing JobCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobCredentialArgs.__new__(JobCredentialArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["username"] = None
        return JobCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The credential user name.
        """
        return pulumi.get(self, "username")

