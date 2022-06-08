# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ManagedInstanceAzureADOnlyAuthenticationArgs', 'ManagedInstanceAzureADOnlyAuthentication']

@pulumi.input_type
class ManagedInstanceAzureADOnlyAuthenticationArgs:
    def __init__(__self__, *,
                 azure_ad_only_authentication: pulumi.Input[bool],
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 authentication_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagedInstanceAzureADOnlyAuthentication resource.
        :param pulumi.Input[bool] azure_ad_only_authentication: Azure Active Directory only Authentication enabled.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] authentication_name: The name of server azure active directory only authentication.
        """
        pulumi.set(__self__, "azure_ad_only_authentication", azure_ad_only_authentication)
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authentication_name is not None:
            pulumi.set(__self__, "authentication_name", authentication_name)

    @property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> pulumi.Input[bool]:
        """
        Azure Active Directory only Authentication enabled.
        """
        return pulumi.get(self, "azure_ad_only_authentication")

    @azure_ad_only_authentication.setter
    def azure_ad_only_authentication(self, value: pulumi.Input[bool]):
        pulumi.set(self, "azure_ad_only_authentication", value)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

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
    @pulumi.getter(name="authenticationName")
    def authentication_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of server azure active directory only authentication.
        """
        return pulumi.get(self, "authentication_name")

    @authentication_name.setter
    def authentication_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_name", value)


class ManagedInstanceAzureADOnlyAuthentication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_name: Optional[pulumi.Input[str]] = None,
                 azure_ad_only_authentication: Optional[pulumi.Input[bool]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure Active Directory only authentication.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_name: The name of server azure active directory only authentication.
        :param pulumi.Input[bool] azure_ad_only_authentication: Azure Active Directory only Authentication enabled.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedInstanceAzureADOnlyAuthenticationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure Active Directory only authentication.

        :param str resource_name: The name of the resource.
        :param ManagedInstanceAzureADOnlyAuthenticationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedInstanceAzureADOnlyAuthenticationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_name: Optional[pulumi.Input[str]] = None,
                 azure_ad_only_authentication: Optional[pulumi.Input[bool]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ManagedInstanceAzureADOnlyAuthenticationArgs.__new__(ManagedInstanceAzureADOnlyAuthenticationArgs)

            __props__.__dict__["authentication_name"] = authentication_name
            if azure_ad_only_authentication is None and not opts.urn:
                raise TypeError("Missing required property 'azure_ad_only_authentication'")
            __props__.__dict__["azure_ad_only_authentication"] = azure_ad_only_authentication
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ManagedInstanceAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ManagedInstanceAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20200801preview:ManagedInstanceAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ManagedInstanceAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ManagedInstanceAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ManagedInstanceAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20210801preview:ManagedInstanceAzureADOnlyAuthentication")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedInstanceAzureADOnlyAuthentication, __self__).__init__(
            'azure-native:sql/v20211101preview:ManagedInstanceAzureADOnlyAuthentication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedInstanceAzureADOnlyAuthentication':
        """
        Get an existing ManagedInstanceAzureADOnlyAuthentication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedInstanceAzureADOnlyAuthenticationArgs.__new__(ManagedInstanceAzureADOnlyAuthenticationArgs)

        __props__.__dict__["azure_ad_only_authentication"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return ManagedInstanceAzureADOnlyAuthentication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> pulumi.Output[bool]:
        """
        Azure Active Directory only Authentication enabled.
        """
        return pulumi.get(self, "azure_ad_only_authentication")

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

