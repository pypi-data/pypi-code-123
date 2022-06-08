# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GatewayCertificateAuthorityArgs', 'GatewayCertificateAuthority']

@pulumi.input_type
class GatewayCertificateAuthorityArgs:
    def __init__(__self__, *,
                 gateway_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 is_trusted: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GatewayCertificateAuthority resource.
        :param pulumi.Input[str] gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
        :param pulumi.Input[bool] is_trusted: Determines whether certificate authority is trusted.
        """
        pulumi.set(__self__, "gateway_id", gateway_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if is_trusted is not None:
            pulumi.set(__self__, "is_trusted", is_trusted)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Input[str]:
        """
        Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the certificate entity. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter(name="isTrusted")
    def is_trusted(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether certificate authority is trusted.
        """
        return pulumi.get(self, "is_trusted")

    @is_trusted.setter
    def is_trusted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_trusted", value)


class GatewayCertificateAuthority(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 is_trusted: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Gateway certificate authority details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
        :param pulumi.Input[bool] is_trusted: Determines whether certificate authority is trusted.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayCertificateAuthorityArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Gateway certificate authority details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param GatewayCertificateAuthorityArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayCertificateAuthorityArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 is_trusted: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = GatewayCertificateAuthorityArgs.__new__(GatewayCertificateAuthorityArgs)

            __props__.__dict__["certificate_id"] = certificate_id
            if gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_id'")
            __props__.__dict__["gateway_id"] = gateway_id
            __props__.__dict__["is_trusted"] = is_trusted
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:GatewayCertificateAuthority"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:GatewayCertificateAuthority"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:GatewayCertificateAuthority"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:GatewayCertificateAuthority"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:GatewayCertificateAuthority"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:GatewayCertificateAuthority")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GatewayCertificateAuthority, __self__).__init__(
            'azure-native:apimanagement:GatewayCertificateAuthority',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GatewayCertificateAuthority':
        """
        Get an existing GatewayCertificateAuthority resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayCertificateAuthorityArgs.__new__(GatewayCertificateAuthorityArgs)

        __props__.__dict__["is_trusted"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return GatewayCertificateAuthority(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="isTrusted")
    def is_trusted(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines whether certificate authority is trusted.
        """
        return pulumi.get(self, "is_trusted")

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
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

