# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['InboundNatRuleInitArgs', 'InboundNatRule']

@pulumi.input_type
class InboundNatRuleInitArgs:
    def __init__(__self__, *,
                 load_balancer_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 backend_address_pool: Optional[pulumi.Input['SubResourceArgs']] = None,
                 backend_port: Optional[pulumi.Input[int]] = None,
                 enable_floating_ip: Optional[pulumi.Input[bool]] = None,
                 enable_tcp_reset: Optional[pulumi.Input[bool]] = None,
                 frontend_ip_configuration: Optional[pulumi.Input['SubResourceArgs']] = None,
                 frontend_port: Optional[pulumi.Input[int]] = None,
                 frontend_port_range_end: Optional[pulumi.Input[int]] = None,
                 frontend_port_range_start: Optional[pulumi.Input[int]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 inbound_nat_rule_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'TransportProtocol']]] = None):
        """
        The set of arguments for constructing a InboundNatRule resource.
        :param pulumi.Input[str] load_balancer_name: The name of the load balancer.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['SubResourceArgs'] backend_address_pool: A reference to backendAddressPool resource.
        :param pulumi.Input[int] backend_port: The port used for the internal endpoint. Acceptable values range from 1 to 65535.
        :param pulumi.Input[bool] enable_floating_ip: Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.
        :param pulumi.Input[bool] enable_tcp_reset: Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.
        :param pulumi.Input['SubResourceArgs'] frontend_ip_configuration: A reference to frontend IP addresses.
        :param pulumi.Input[int] frontend_port: The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.
        :param pulumi.Input[int] frontend_port_range_end: The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        :param pulumi.Input[int] frontend_port_range_start: The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] idle_timeout_in_minutes: The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.
        :param pulumi.Input[str] inbound_nat_rule_name: The name of the inbound NAT rule.
        :param pulumi.Input[str] name: The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource.
        :param pulumi.Input[Union[str, 'TransportProtocol']] protocol: The reference to the transport protocol used by the load balancing rule.
        """
        pulumi.set(__self__, "load_balancer_name", load_balancer_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if backend_address_pool is not None:
            pulumi.set(__self__, "backend_address_pool", backend_address_pool)
        if backend_port is not None:
            pulumi.set(__self__, "backend_port", backend_port)
        if enable_floating_ip is not None:
            pulumi.set(__self__, "enable_floating_ip", enable_floating_ip)
        if enable_tcp_reset is not None:
            pulumi.set(__self__, "enable_tcp_reset", enable_tcp_reset)
        if frontend_ip_configuration is not None:
            pulumi.set(__self__, "frontend_ip_configuration", frontend_ip_configuration)
        if frontend_port is not None:
            pulumi.set(__self__, "frontend_port", frontend_port)
        if frontend_port_range_end is not None:
            pulumi.set(__self__, "frontend_port_range_end", frontend_port_range_end)
        if frontend_port_range_start is not None:
            pulumi.set(__self__, "frontend_port_range_start", frontend_port_range_start)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if idle_timeout_in_minutes is not None:
            pulumi.set(__self__, "idle_timeout_in_minutes", idle_timeout_in_minutes)
        if inbound_nat_rule_name is not None:
            pulumi.set(__self__, "inbound_nat_rule_name", inbound_nat_rule_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> pulumi.Input[str]:
        """
        The name of the load balancer.
        """
        return pulumi.get(self, "load_balancer_name")

    @load_balancer_name.setter
    def load_balancer_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "load_balancer_name", value)

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
    @pulumi.getter(name="backendAddressPool")
    def backend_address_pool(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        A reference to backendAddressPool resource.
        """
        return pulumi.get(self, "backend_address_pool")

    @backend_address_pool.setter
    def backend_address_pool(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "backend_address_pool", value)

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[int]]:
        """
        The port used for the internal endpoint. Acceptable values range from 1 to 65535.
        """
        return pulumi.get(self, "backend_port")

    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backend_port", value)

    @property
    @pulumi.getter(name="enableFloatingIP")
    def enable_floating_ip(self) -> Optional[pulumi.Input[bool]]:
        """
        Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.
        """
        return pulumi.get(self, "enable_floating_ip")

    @enable_floating_ip.setter
    def enable_floating_ip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_floating_ip", value)

    @property
    @pulumi.getter(name="enableTcpReset")
    def enable_tcp_reset(self) -> Optional[pulumi.Input[bool]]:
        """
        Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.
        """
        return pulumi.get(self, "enable_tcp_reset")

    @enable_tcp_reset.setter
    def enable_tcp_reset(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_tcp_reset", value)

    @property
    @pulumi.getter(name="frontendIPConfiguration")
    def frontend_ip_configuration(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        A reference to frontend IP addresses.
        """
        return pulumi.get(self, "frontend_ip_configuration")

    @frontend_ip_configuration.setter
    def frontend_ip_configuration(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "frontend_ip_configuration", value)

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[pulumi.Input[int]]:
        """
        The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.
        """
        return pulumi.get(self, "frontend_port")

    @frontend_port.setter
    def frontend_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_port", value)

    @property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> Optional[pulumi.Input[int]]:
        """
        The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        """
        return pulumi.get(self, "frontend_port_range_end")

    @frontend_port_range_end.setter
    def frontend_port_range_end(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_port_range_end", value)

    @property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> Optional[pulumi.Input[int]]:
        """
        The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        """
        return pulumi.get(self, "frontend_port_range_start")

    @frontend_port_range_start.setter
    def frontend_port_range_start(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_port_range_start", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_timeout_in_minutes", value)

    @property
    @pulumi.getter(name="inboundNatRuleName")
    def inbound_nat_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the inbound NAT rule.
        """
        return pulumi.get(self, "inbound_nat_rule_name")

    @inbound_nat_rule_name.setter
    def inbound_nat_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inbound_nat_rule_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[Union[str, 'TransportProtocol']]]:
        """
        The reference to the transport protocol used by the load balancing rule.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[Union[str, 'TransportProtocol']]]):
        pulumi.set(self, "protocol", value)


class InboundNatRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_address_pool: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 backend_port: Optional[pulumi.Input[int]] = None,
                 enable_floating_ip: Optional[pulumi.Input[bool]] = None,
                 enable_tcp_reset: Optional[pulumi.Input[bool]] = None,
                 frontend_ip_configuration: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 frontend_port: Optional[pulumi.Input[int]] = None,
                 frontend_port_range_end: Optional[pulumi.Input[int]] = None,
                 frontend_port_range_start: Optional[pulumi.Input[int]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 inbound_nat_rule_name: Optional[pulumi.Input[str]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'TransportProtocol']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Inbound NAT rule of the load balancer.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] backend_address_pool: A reference to backendAddressPool resource.
        :param pulumi.Input[int] backend_port: The port used for the internal endpoint. Acceptable values range from 1 to 65535.
        :param pulumi.Input[bool] enable_floating_ip: Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.
        :param pulumi.Input[bool] enable_tcp_reset: Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] frontend_ip_configuration: A reference to frontend IP addresses.
        :param pulumi.Input[int] frontend_port: The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.
        :param pulumi.Input[int] frontend_port_range_end: The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        :param pulumi.Input[int] frontend_port_range_start: The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] idle_timeout_in_minutes: The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.
        :param pulumi.Input[str] inbound_nat_rule_name: The name of the inbound NAT rule.
        :param pulumi.Input[str] load_balancer_name: The name of the load balancer.
        :param pulumi.Input[str] name: The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource.
        :param pulumi.Input[Union[str, 'TransportProtocol']] protocol: The reference to the transport protocol used by the load balancing rule.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InboundNatRuleInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Inbound NAT rule of the load balancer.

        :param str resource_name: The name of the resource.
        :param InboundNatRuleInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InboundNatRuleInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_address_pool: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 backend_port: Optional[pulumi.Input[int]] = None,
                 enable_floating_ip: Optional[pulumi.Input[bool]] = None,
                 enable_tcp_reset: Optional[pulumi.Input[bool]] = None,
                 frontend_ip_configuration: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 frontend_port: Optional[pulumi.Input[int]] = None,
                 frontend_port_range_end: Optional[pulumi.Input[int]] = None,
                 frontend_port_range_start: Optional[pulumi.Input[int]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 inbound_nat_rule_name: Optional[pulumi.Input[str]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'TransportProtocol']]] = None,
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
            __props__ = InboundNatRuleInitArgs.__new__(InboundNatRuleInitArgs)

            __props__.__dict__["backend_address_pool"] = backend_address_pool
            __props__.__dict__["backend_port"] = backend_port
            __props__.__dict__["enable_floating_ip"] = enable_floating_ip
            __props__.__dict__["enable_tcp_reset"] = enable_tcp_reset
            __props__.__dict__["frontend_ip_configuration"] = frontend_ip_configuration
            __props__.__dict__["frontend_port"] = frontend_port
            __props__.__dict__["frontend_port_range_end"] = frontend_port_range_end
            __props__.__dict__["frontend_port_range_start"] = frontend_port_range_start
            __props__.__dict__["id"] = id
            __props__.__dict__["idle_timeout_in_minutes"] = idle_timeout_in_minutes
            __props__.__dict__["inbound_nat_rule_name"] = inbound_nat_rule_name
            if load_balancer_name is None and not opts.urn:
                raise TypeError("Missing required property 'load_balancer_name'")
            __props__.__dict__["load_balancer_name"] = load_balancer_name
            __props__.__dict__["name"] = name
            __props__.__dict__["protocol"] = protocol
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["backend_ip_configuration"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20170601:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20170801:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20170901:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20171001:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20171101:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20180101:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20180201:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20180401:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20180601:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20180701:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20180801:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20181001:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20181101:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20181201:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20190201:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20190401:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20190601:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20190701:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20190801:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20190901:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20191101:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20191201:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20200301:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20200401:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20200501:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20200601:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20200701:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20200801:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20201101:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20210201:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20210301:InboundNatRule"), pulumi.Alias(type_="azure-native:network/v20210801:InboundNatRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InboundNatRule, __self__).__init__(
            'azure-native:network/v20210501:InboundNatRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InboundNatRule':
        """
        Get an existing InboundNatRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InboundNatRuleInitArgs.__new__(InboundNatRuleInitArgs)

        __props__.__dict__["backend_address_pool"] = None
        __props__.__dict__["backend_ip_configuration"] = None
        __props__.__dict__["backend_port"] = None
        __props__.__dict__["enable_floating_ip"] = None
        __props__.__dict__["enable_tcp_reset"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["frontend_ip_configuration"] = None
        __props__.__dict__["frontend_port"] = None
        __props__.__dict__["frontend_port_range_end"] = None
        __props__.__dict__["frontend_port_range_start"] = None
        __props__.__dict__["idle_timeout_in_minutes"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return InboundNatRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendAddressPool")
    def backend_address_pool(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        A reference to backendAddressPool resource.
        """
        return pulumi.get(self, "backend_address_pool")

    @property
    @pulumi.getter(name="backendIPConfiguration")
    def backend_ip_configuration(self) -> pulumi.Output['outputs.NetworkInterfaceIPConfigurationResponse']:
        """
        A reference to a private IP address defined on a network interface of a VM. Traffic sent to the frontend port of each of the frontend IP configurations is forwarded to the backend IP.
        """
        return pulumi.get(self, "backend_ip_configuration")

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> pulumi.Output[Optional[int]]:
        """
        The port used for the internal endpoint. Acceptable values range from 1 to 65535.
        """
        return pulumi.get(self, "backend_port")

    @property
    @pulumi.getter(name="enableFloatingIP")
    def enable_floating_ip(self) -> pulumi.Output[Optional[bool]]:
        """
        Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.
        """
        return pulumi.get(self, "enable_floating_ip")

    @property
    @pulumi.getter(name="enableTcpReset")
    def enable_tcp_reset(self) -> pulumi.Output[Optional[bool]]:
        """
        Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.
        """
        return pulumi.get(self, "enable_tcp_reset")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="frontendIPConfiguration")
    def frontend_ip_configuration(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        A reference to frontend IP addresses.
        """
        return pulumi.get(self, "frontend_ip_configuration")

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> pulumi.Output[Optional[int]]:
        """
        The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.
        """
        return pulumi.get(self, "frontend_port")

    @property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> pulumi.Output[Optional[int]]:
        """
        The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        """
        return pulumi.get(self, "frontend_port_range_end")

    @property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> pulumi.Output[Optional[int]]:
        """
        The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.
        """
        return pulumi.get(self, "frontend_port_range_start")

    @property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[str]]:
        """
        The reference to the transport protocol used by the load balancing rule.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the inbound NAT rule resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

