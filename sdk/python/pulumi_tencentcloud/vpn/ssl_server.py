# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SslServerArgs', 'SslServer']

@pulumi.input_type
class SslServerArgs:
    def __init__(__self__, *,
                 local_addresses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 remote_address: pulumi.Input[str],
                 ssl_vpn_server_name: pulumi.Input[str],
                 vpn_gateway_id: pulumi.Input[str],
                 compress: Optional[pulumi.Input[bool]] = None,
                 encrypt_algorithm: Optional[pulumi.Input[str]] = None,
                 integrity_algorithm: Optional[pulumi.Input[str]] = None,
                 ssl_vpn_port: Optional[pulumi.Input[int]] = None,
                 ssl_vpn_protocol: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SslServer resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_addresses: List of local CIDR.
        :param pulumi.Input[str] remote_address: Remote CIDR for client.
        :param pulumi.Input[str] ssl_vpn_server_name: The name of ssl vpn server to be created.
        :param pulumi.Input[str] vpn_gateway_id: VPN gateway ID.
        :param pulumi.Input[bool] compress: need compressed. Default value: False.
        :param pulumi.Input[str] encrypt_algorithm: The encrypt algorithm. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, NONE.Default value: NONE.
        :param pulumi.Input[str] integrity_algorithm: The integrity algorithm. Valid values: SHA1, MD5 and NONE. Default value: NONE.
        :param pulumi.Input[int] ssl_vpn_port: The port of ssl vpn. Default value: 1194.
        :param pulumi.Input[str] ssl_vpn_protocol: The protocol of ssl vpn. Default value: UDP.
        """
        pulumi.set(__self__, "local_addresses", local_addresses)
        pulumi.set(__self__, "remote_address", remote_address)
        pulumi.set(__self__, "ssl_vpn_server_name", ssl_vpn_server_name)
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)
        if compress is not None:
            pulumi.set(__self__, "compress", compress)
        if encrypt_algorithm is not None:
            pulumi.set(__self__, "encrypt_algorithm", encrypt_algorithm)
        if integrity_algorithm is not None:
            pulumi.set(__self__, "integrity_algorithm", integrity_algorithm)
        if ssl_vpn_port is not None:
            pulumi.set(__self__, "ssl_vpn_port", ssl_vpn_port)
        if ssl_vpn_protocol is not None:
            pulumi.set(__self__, "ssl_vpn_protocol", ssl_vpn_protocol)

    @property
    @pulumi.getter(name="localAddresses")
    def local_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of local CIDR.
        """
        return pulumi.get(self, "local_addresses")

    @local_addresses.setter
    def local_addresses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "local_addresses", value)

    @property
    @pulumi.getter(name="remoteAddress")
    def remote_address(self) -> pulumi.Input[str]:
        """
        Remote CIDR for client.
        """
        return pulumi.get(self, "remote_address")

    @remote_address.setter
    def remote_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "remote_address", value)

    @property
    @pulumi.getter(name="sslVpnServerName")
    def ssl_vpn_server_name(self) -> pulumi.Input[str]:
        """
        The name of ssl vpn server to be created.
        """
        return pulumi.get(self, "ssl_vpn_server_name")

    @ssl_vpn_server_name.setter
    def ssl_vpn_server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "ssl_vpn_server_name", value)

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Input[str]:
        """
        VPN gateway ID.
        """
        return pulumi.get(self, "vpn_gateway_id")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpn_gateway_id", value)

    @property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[bool]]:
        """
        need compressed. Default value: False.
        """
        return pulumi.get(self, "compress")

    @compress.setter
    def compress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "compress", value)

    @property
    @pulumi.getter(name="encryptAlgorithm")
    def encrypt_algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        The encrypt algorithm. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, NONE.Default value: NONE.
        """
        return pulumi.get(self, "encrypt_algorithm")

    @encrypt_algorithm.setter
    def encrypt_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypt_algorithm", value)

    @property
    @pulumi.getter(name="integrityAlgorithm")
    def integrity_algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        The integrity algorithm. Valid values: SHA1, MD5 and NONE. Default value: NONE.
        """
        return pulumi.get(self, "integrity_algorithm")

    @integrity_algorithm.setter
    def integrity_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integrity_algorithm", value)

    @property
    @pulumi.getter(name="sslVpnPort")
    def ssl_vpn_port(self) -> Optional[pulumi.Input[int]]:
        """
        The port of ssl vpn. Default value: 1194.
        """
        return pulumi.get(self, "ssl_vpn_port")

    @ssl_vpn_port.setter
    def ssl_vpn_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_vpn_port", value)

    @property
    @pulumi.getter(name="sslVpnProtocol")
    def ssl_vpn_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol of ssl vpn. Default value: UDP.
        """
        return pulumi.get(self, "ssl_vpn_protocol")

    @ssl_vpn_protocol.setter
    def ssl_vpn_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_vpn_protocol", value)


@pulumi.input_type
class _SslServerState:
    def __init__(__self__, *,
                 compress: Optional[pulumi.Input[bool]] = None,
                 encrypt_algorithm: Optional[pulumi.Input[str]] = None,
                 integrity_algorithm: Optional[pulumi.Input[str]] = None,
                 local_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_address: Optional[pulumi.Input[str]] = None,
                 ssl_vpn_port: Optional[pulumi.Input[int]] = None,
                 ssl_vpn_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_vpn_server_name: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SslServer resources.
        :param pulumi.Input[bool] compress: need compressed. Default value: False.
        :param pulumi.Input[str] encrypt_algorithm: The encrypt algorithm. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, NONE.Default value: NONE.
        :param pulumi.Input[str] integrity_algorithm: The integrity algorithm. Valid values: SHA1, MD5 and NONE. Default value: NONE.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_addresses: List of local CIDR.
        :param pulumi.Input[str] remote_address: Remote CIDR for client.
        :param pulumi.Input[int] ssl_vpn_port: The port of ssl vpn. Default value: 1194.
        :param pulumi.Input[str] ssl_vpn_protocol: The protocol of ssl vpn. Default value: UDP.
        :param pulumi.Input[str] ssl_vpn_server_name: The name of ssl vpn server to be created.
        :param pulumi.Input[str] vpn_gateway_id: VPN gateway ID.
        """
        if compress is not None:
            pulumi.set(__self__, "compress", compress)
        if encrypt_algorithm is not None:
            pulumi.set(__self__, "encrypt_algorithm", encrypt_algorithm)
        if integrity_algorithm is not None:
            pulumi.set(__self__, "integrity_algorithm", integrity_algorithm)
        if local_addresses is not None:
            pulumi.set(__self__, "local_addresses", local_addresses)
        if remote_address is not None:
            pulumi.set(__self__, "remote_address", remote_address)
        if ssl_vpn_port is not None:
            pulumi.set(__self__, "ssl_vpn_port", ssl_vpn_port)
        if ssl_vpn_protocol is not None:
            pulumi.set(__self__, "ssl_vpn_protocol", ssl_vpn_protocol)
        if ssl_vpn_server_name is not None:
            pulumi.set(__self__, "ssl_vpn_server_name", ssl_vpn_server_name)
        if vpn_gateway_id is not None:
            pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)

    @property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[bool]]:
        """
        need compressed. Default value: False.
        """
        return pulumi.get(self, "compress")

    @compress.setter
    def compress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "compress", value)

    @property
    @pulumi.getter(name="encryptAlgorithm")
    def encrypt_algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        The encrypt algorithm. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, NONE.Default value: NONE.
        """
        return pulumi.get(self, "encrypt_algorithm")

    @encrypt_algorithm.setter
    def encrypt_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypt_algorithm", value)

    @property
    @pulumi.getter(name="integrityAlgorithm")
    def integrity_algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        The integrity algorithm. Valid values: SHA1, MD5 and NONE. Default value: NONE.
        """
        return pulumi.get(self, "integrity_algorithm")

    @integrity_algorithm.setter
    def integrity_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integrity_algorithm", value)

    @property
    @pulumi.getter(name="localAddresses")
    def local_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of local CIDR.
        """
        return pulumi.get(self, "local_addresses")

    @local_addresses.setter
    def local_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "local_addresses", value)

    @property
    @pulumi.getter(name="remoteAddress")
    def remote_address(self) -> Optional[pulumi.Input[str]]:
        """
        Remote CIDR for client.
        """
        return pulumi.get(self, "remote_address")

    @remote_address.setter
    def remote_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_address", value)

    @property
    @pulumi.getter(name="sslVpnPort")
    def ssl_vpn_port(self) -> Optional[pulumi.Input[int]]:
        """
        The port of ssl vpn. Default value: 1194.
        """
        return pulumi.get(self, "ssl_vpn_port")

    @ssl_vpn_port.setter
    def ssl_vpn_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_vpn_port", value)

    @property
    @pulumi.getter(name="sslVpnProtocol")
    def ssl_vpn_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol of ssl vpn. Default value: UDP.
        """
        return pulumi.get(self, "ssl_vpn_protocol")

    @ssl_vpn_protocol.setter
    def ssl_vpn_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_vpn_protocol", value)

    @property
    @pulumi.getter(name="sslVpnServerName")
    def ssl_vpn_server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of ssl vpn server to be created.
        """
        return pulumi.get(self, "ssl_vpn_server_name")

    @ssl_vpn_server_name.setter
    def ssl_vpn_server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_vpn_server_name", value)

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        VPN gateway ID.
        """
        return pulumi.get(self, "vpn_gateway_id")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpn_gateway_id", value)


class SslServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compress: Optional[pulumi.Input[bool]] = None,
                 encrypt_algorithm: Optional[pulumi.Input[str]] = None,
                 integrity_algorithm: Optional[pulumi.Input[str]] = None,
                 local_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_address: Optional[pulumi.Input[str]] = None,
                 ssl_vpn_port: Optional[pulumi.Input[int]] = None,
                 ssl_vpn_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_vpn_server_name: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a SslServer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] compress: need compressed. Default value: False.
        :param pulumi.Input[str] encrypt_algorithm: The encrypt algorithm. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, NONE.Default value: NONE.
        :param pulumi.Input[str] integrity_algorithm: The integrity algorithm. Valid values: SHA1, MD5 and NONE. Default value: NONE.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_addresses: List of local CIDR.
        :param pulumi.Input[str] remote_address: Remote CIDR for client.
        :param pulumi.Input[int] ssl_vpn_port: The port of ssl vpn. Default value: 1194.
        :param pulumi.Input[str] ssl_vpn_protocol: The protocol of ssl vpn. Default value: UDP.
        :param pulumi.Input[str] ssl_vpn_server_name: The name of ssl vpn server to be created.
        :param pulumi.Input[str] vpn_gateway_id: VPN gateway ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SslServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SslServer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SslServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SslServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compress: Optional[pulumi.Input[bool]] = None,
                 encrypt_algorithm: Optional[pulumi.Input[str]] = None,
                 integrity_algorithm: Optional[pulumi.Input[str]] = None,
                 local_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_address: Optional[pulumi.Input[str]] = None,
                 ssl_vpn_port: Optional[pulumi.Input[int]] = None,
                 ssl_vpn_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_vpn_server_name: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = SslServerArgs.__new__(SslServerArgs)

            __props__.__dict__["compress"] = compress
            __props__.__dict__["encrypt_algorithm"] = encrypt_algorithm
            __props__.__dict__["integrity_algorithm"] = integrity_algorithm
            if local_addresses is None and not opts.urn:
                raise TypeError("Missing required property 'local_addresses'")
            __props__.__dict__["local_addresses"] = local_addresses
            if remote_address is None and not opts.urn:
                raise TypeError("Missing required property 'remote_address'")
            __props__.__dict__["remote_address"] = remote_address
            __props__.__dict__["ssl_vpn_port"] = ssl_vpn_port
            __props__.__dict__["ssl_vpn_protocol"] = ssl_vpn_protocol
            if ssl_vpn_server_name is None and not opts.urn:
                raise TypeError("Missing required property 'ssl_vpn_server_name'")
            __props__.__dict__["ssl_vpn_server_name"] = ssl_vpn_server_name
            if vpn_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpn_gateway_id'")
            __props__.__dict__["vpn_gateway_id"] = vpn_gateway_id
        super(SslServer, __self__).__init__(
            'tencentcloud:Vpn/sslServer:SslServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compress: Optional[pulumi.Input[bool]] = None,
            encrypt_algorithm: Optional[pulumi.Input[str]] = None,
            integrity_algorithm: Optional[pulumi.Input[str]] = None,
            local_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            remote_address: Optional[pulumi.Input[str]] = None,
            ssl_vpn_port: Optional[pulumi.Input[int]] = None,
            ssl_vpn_protocol: Optional[pulumi.Input[str]] = None,
            ssl_vpn_server_name: Optional[pulumi.Input[str]] = None,
            vpn_gateway_id: Optional[pulumi.Input[str]] = None) -> 'SslServer':
        """
        Get an existing SslServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] compress: need compressed. Default value: False.
        :param pulumi.Input[str] encrypt_algorithm: The encrypt algorithm. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, NONE.Default value: NONE.
        :param pulumi.Input[str] integrity_algorithm: The integrity algorithm. Valid values: SHA1, MD5 and NONE. Default value: NONE.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_addresses: List of local CIDR.
        :param pulumi.Input[str] remote_address: Remote CIDR for client.
        :param pulumi.Input[int] ssl_vpn_port: The port of ssl vpn. Default value: 1194.
        :param pulumi.Input[str] ssl_vpn_protocol: The protocol of ssl vpn. Default value: UDP.
        :param pulumi.Input[str] ssl_vpn_server_name: The name of ssl vpn server to be created.
        :param pulumi.Input[str] vpn_gateway_id: VPN gateway ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SslServerState.__new__(_SslServerState)

        __props__.__dict__["compress"] = compress
        __props__.__dict__["encrypt_algorithm"] = encrypt_algorithm
        __props__.__dict__["integrity_algorithm"] = integrity_algorithm
        __props__.__dict__["local_addresses"] = local_addresses
        __props__.__dict__["remote_address"] = remote_address
        __props__.__dict__["ssl_vpn_port"] = ssl_vpn_port
        __props__.__dict__["ssl_vpn_protocol"] = ssl_vpn_protocol
        __props__.__dict__["ssl_vpn_server_name"] = ssl_vpn_server_name
        __props__.__dict__["vpn_gateway_id"] = vpn_gateway_id
        return SslServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def compress(self) -> pulumi.Output[Optional[bool]]:
        """
        need compressed. Default value: False.
        """
        return pulumi.get(self, "compress")

    @property
    @pulumi.getter(name="encryptAlgorithm")
    def encrypt_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        The encrypt algorithm. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, NONE.Default value: NONE.
        """
        return pulumi.get(self, "encrypt_algorithm")

    @property
    @pulumi.getter(name="integrityAlgorithm")
    def integrity_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        The integrity algorithm. Valid values: SHA1, MD5 and NONE. Default value: NONE.
        """
        return pulumi.get(self, "integrity_algorithm")

    @property
    @pulumi.getter(name="localAddresses")
    def local_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        List of local CIDR.
        """
        return pulumi.get(self, "local_addresses")

    @property
    @pulumi.getter(name="remoteAddress")
    def remote_address(self) -> pulumi.Output[str]:
        """
        Remote CIDR for client.
        """
        return pulumi.get(self, "remote_address")

    @property
    @pulumi.getter(name="sslVpnPort")
    def ssl_vpn_port(self) -> pulumi.Output[Optional[int]]:
        """
        The port of ssl vpn. Default value: 1194.
        """
        return pulumi.get(self, "ssl_vpn_port")

    @property
    @pulumi.getter(name="sslVpnProtocol")
    def ssl_vpn_protocol(self) -> pulumi.Output[Optional[str]]:
        """
        The protocol of ssl vpn. Default value: UDP.
        """
        return pulumi.get(self, "ssl_vpn_protocol")

    @property
    @pulumi.getter(name="sslVpnServerName")
    def ssl_vpn_server_name(self) -> pulumi.Output[str]:
        """
        The name of ssl vpn server to be created.
        """
        return pulumi.get(self, "ssl_vpn_server_name")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Output[str]:
        """
        VPN gateway ID.
        """
        return pulumi.get(self, "vpn_gateway_id")

