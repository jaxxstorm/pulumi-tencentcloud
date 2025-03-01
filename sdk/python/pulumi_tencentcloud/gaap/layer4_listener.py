# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['Layer4ListenerArgs', 'Layer4Listener']

@pulumi.input_type
class Layer4ListenerArgs:
    def __init__(__self__, *,
                 port: pulumi.Input[int],
                 protocol: pulumi.Input[str],
                 proxy_id: pulumi.Input[str],
                 realserver_type: pulumi.Input[str],
                 client_ip_method: Optional[pulumi.Input[int]] = None,
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 health_check: Optional[pulumi.Input[bool]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 realserver_bind_sets: Optional[pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Layer4Listener resource.
        :param pulumi.Input[int] port: Port of the layer4 listener.
        :param pulumi.Input[str] protocol: Protocol of the layer4 listener. Valid value: `TCP` and `UDP`.
        :param pulumi.Input[str] proxy_id: ID of the GAAP proxy.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.
        :param pulumi.Input[int] client_ip_method: The way the listener gets the client IP, 0 for TOA, 1 for Proxy Protocol, default value is 0. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[str] name: Name of the layer4 listener, the maximum length is 30.
        :param pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]] realserver_bind_sets: An information list of GAAP realserver.
        :param pulumi.Input[str] scheduler: Scheduling policy of the layer4 listener, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "proxy_id", proxy_id)
        pulumi.set(__self__, "realserver_type", realserver_type)
        if client_ip_method is not None:
            pulumi.set(__self__, "client_ip_method", client_ip_method)
        if connect_timeout is not None:
            pulumi.set(__self__, "connect_timeout", connect_timeout)
        if health_check is not None:
            pulumi.set(__self__, "health_check", health_check)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if realserver_bind_sets is not None:
            pulumi.set(__self__, "realserver_bind_sets", realserver_bind_sets)
        if scheduler is not None:
            pulumi.set(__self__, "scheduler", scheduler)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        Port of the layer4 listener.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        Protocol of the layer4 listener. Valid value: `TCP` and `UDP`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> pulumi.Input[str]:
        """
        ID of the GAAP proxy.
        """
        return pulumi.get(self, "proxy_id")

    @proxy_id.setter
    def proxy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "proxy_id", value)

    @property
    @pulumi.getter(name="realserverType")
    def realserver_type(self) -> pulumi.Input[str]:
        """
        Type of the realserver. Valid value: `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.
        """
        return pulumi.get(self, "realserver_type")

    @realserver_type.setter
    def realserver_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "realserver_type", value)

    @property
    @pulumi.getter(name="clientIpMethod")
    def client_ip_method(self) -> Optional[pulumi.Input[int]]:
        """
        The way the listener gets the client IP, 0 for TOA, 1 for Proxy Protocol, default value is 0. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "client_ip_method")

    @client_ip_method.setter
    def client_ip_method(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "client_ip_method", value)

    @property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.
        """
        return pulumi.get(self, "connect_timeout")

    @connect_timeout.setter
    def connect_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "connect_timeout", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the layer4 listener, the maximum length is 30.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="realserverBindSets")
    def realserver_bind_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]]]:
        """
        An information list of GAAP realserver.
        """
        return pulumi.get(self, "realserver_bind_sets")

    @realserver_bind_sets.setter
    def realserver_bind_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]]]):
        pulumi.set(self, "realserver_bind_sets", value)

    @property
    @pulumi.getter
    def scheduler(self) -> Optional[pulumi.Input[str]]:
        """
        Scheduling policy of the layer4 listener, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        return pulumi.get(self, "scheduler")

    @scheduler.setter
    def scheduler(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduler", value)


@pulumi.input_type
class _Layer4ListenerState:
    def __init__(__self__, *,
                 client_ip_method: Optional[pulumi.Input[int]] = None,
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input[bool]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxy_id: Optional[pulumi.Input[str]] = None,
                 realserver_bind_sets: Optional[pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]]] = None,
                 realserver_type: Optional[pulumi.Input[str]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Layer4Listener resources.
        :param pulumi.Input[int] client_ip_method: The way the listener gets the client IP, 0 for TOA, 1 for Proxy Protocol, default value is 0. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.
        :param pulumi.Input[str] create_time: Creation time of the layer4 listener.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[str] name: Name of the layer4 listener, the maximum length is 30.
        :param pulumi.Input[int] port: Port of the layer4 listener.
        :param pulumi.Input[str] protocol: Protocol of the layer4 listener. Valid value: `TCP` and `UDP`.
        :param pulumi.Input[str] proxy_id: ID of the GAAP proxy.
        :param pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]] realserver_bind_sets: An information list of GAAP realserver.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.
        :param pulumi.Input[str] scheduler: Scheduling policy of the layer4 listener, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        :param pulumi.Input[int] status: Status of the layer4 listener.
        """
        if client_ip_method is not None:
            pulumi.set(__self__, "client_ip_method", client_ip_method)
        if connect_timeout is not None:
            pulumi.set(__self__, "connect_timeout", connect_timeout)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if health_check is not None:
            pulumi.set(__self__, "health_check", health_check)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if proxy_id is not None:
            pulumi.set(__self__, "proxy_id", proxy_id)
        if realserver_bind_sets is not None:
            pulumi.set(__self__, "realserver_bind_sets", realserver_bind_sets)
        if realserver_type is not None:
            pulumi.set(__self__, "realserver_type", realserver_type)
        if scheduler is not None:
            pulumi.set(__self__, "scheduler", scheduler)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="clientIpMethod")
    def client_ip_method(self) -> Optional[pulumi.Input[int]]:
        """
        The way the listener gets the client IP, 0 for TOA, 1 for Proxy Protocol, default value is 0. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "client_ip_method")

    @client_ip_method.setter
    def client_ip_method(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "client_ip_method", value)

    @property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.
        """
        return pulumi.get(self, "connect_timeout")

    @connect_timeout.setter
    def connect_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "connect_timeout", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of the layer4 listener.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the layer4 listener, the maximum length is 30.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port of the layer4 listener.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Protocol of the layer4 listener. Valid value: `TCP` and `UDP`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the GAAP proxy.
        """
        return pulumi.get(self, "proxy_id")

    @proxy_id.setter
    def proxy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_id", value)

    @property
    @pulumi.getter(name="realserverBindSets")
    def realserver_bind_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]]]:
        """
        An information list of GAAP realserver.
        """
        return pulumi.get(self, "realserver_bind_sets")

    @realserver_bind_sets.setter
    def realserver_bind_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['Layer4ListenerRealserverBindSetArgs']]]]):
        pulumi.set(self, "realserver_bind_sets", value)

    @property
    @pulumi.getter(name="realserverType")
    def realserver_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the realserver. Valid value: `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.
        """
        return pulumi.get(self, "realserver_type")

    @realserver_type.setter
    def realserver_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realserver_type", value)

    @property
    @pulumi.getter
    def scheduler(self) -> Optional[pulumi.Input[str]]:
        """
        Scheduling policy of the layer4 listener, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        return pulumi.get(self, "scheduler")

    @scheduler.setter
    def scheduler(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduler", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[int]]:
        """
        Status of the layer4 listener.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "status", value)


class Layer4Listener(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_ip_method: Optional[pulumi.Input[int]] = None,
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 health_check: Optional[pulumi.Input[bool]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxy_id: Optional[pulumi.Input[str]] = None,
                 realserver_bind_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Layer4ListenerRealserverBindSetArgs']]]]] = None,
                 realserver_type: Optional[pulumi.Input[str]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to create a layer4 listener of GAAP.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo_proxy = tencentcloud.gaap.Proxy("fooProxy",
            bandwidth=10,
            concurrent=2,
            access_region="SouthChina",
            realserver_region="NorthChina")
        foo_realserver = tencentcloud.gaap.Realserver("fooRealserver", ip="1.1.1.1")
        bar = tencentcloud.gaap.Realserver("bar", ip="119.29.29.29")
        foo_layer4_listener = tencentcloud.gaap.Layer4Listener("fooLayer4Listener",
            protocol="TCP",
            port=80,
            realserver_type="IP",
            proxy_id=foo_proxy.id,
            health_check=True,
            realserver_bind_sets=[
                tencentcloud.gaap.Layer4ListenerRealserverBindSetArgs(
                    id=foo_realserver.id,
                    ip=foo_realserver.ip,
                    port=80,
                ),
                tencentcloud.gaap.Layer4ListenerRealserverBindSetArgs(
                    id=bar.id,
                    ip=bar.ip,
                    port=80,
                ),
            ])
        ```

        ## Import

        GAAP layer4 listener can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Gaap/layer4Listener:Layer4Listener tencentcloud_gaap_layer4_listener.foo listener-11112222
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] client_ip_method: The way the listener gets the client IP, 0 for TOA, 1 for Proxy Protocol, default value is 0. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[str] name: Name of the layer4 listener, the maximum length is 30.
        :param pulumi.Input[int] port: Port of the layer4 listener.
        :param pulumi.Input[str] protocol: Protocol of the layer4 listener. Valid value: `TCP` and `UDP`.
        :param pulumi.Input[str] proxy_id: ID of the GAAP proxy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Layer4ListenerRealserverBindSetArgs']]]] realserver_bind_sets: An information list of GAAP realserver.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.
        :param pulumi.Input[str] scheduler: Scheduling policy of the layer4 listener, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Layer4ListenerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a layer4 listener of GAAP.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo_proxy = tencentcloud.gaap.Proxy("fooProxy",
            bandwidth=10,
            concurrent=2,
            access_region="SouthChina",
            realserver_region="NorthChina")
        foo_realserver = tencentcloud.gaap.Realserver("fooRealserver", ip="1.1.1.1")
        bar = tencentcloud.gaap.Realserver("bar", ip="119.29.29.29")
        foo_layer4_listener = tencentcloud.gaap.Layer4Listener("fooLayer4Listener",
            protocol="TCP",
            port=80,
            realserver_type="IP",
            proxy_id=foo_proxy.id,
            health_check=True,
            realserver_bind_sets=[
                tencentcloud.gaap.Layer4ListenerRealserverBindSetArgs(
                    id=foo_realserver.id,
                    ip=foo_realserver.ip,
                    port=80,
                ),
                tencentcloud.gaap.Layer4ListenerRealserverBindSetArgs(
                    id=bar.id,
                    ip=bar.ip,
                    port=80,
                ),
            ])
        ```

        ## Import

        GAAP layer4 listener can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Gaap/layer4Listener:Layer4Listener tencentcloud_gaap_layer4_listener.foo listener-11112222
        ```

        :param str resource_name: The name of the resource.
        :param Layer4ListenerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Layer4ListenerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_ip_method: Optional[pulumi.Input[int]] = None,
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 health_check: Optional[pulumi.Input[bool]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxy_id: Optional[pulumi.Input[str]] = None,
                 realserver_bind_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Layer4ListenerRealserverBindSetArgs']]]]] = None,
                 realserver_type: Optional[pulumi.Input[str]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None,
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
            __props__ = Layer4ListenerArgs.__new__(Layer4ListenerArgs)

            __props__.__dict__["client_ip_method"] = client_ip_method
            __props__.__dict__["connect_timeout"] = connect_timeout
            __props__.__dict__["health_check"] = health_check
            __props__.__dict__["interval"] = interval
            __props__.__dict__["name"] = name
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if proxy_id is None and not opts.urn:
                raise TypeError("Missing required property 'proxy_id'")
            __props__.__dict__["proxy_id"] = proxy_id
            __props__.__dict__["realserver_bind_sets"] = realserver_bind_sets
            if realserver_type is None and not opts.urn:
                raise TypeError("Missing required property 'realserver_type'")
            __props__.__dict__["realserver_type"] = realserver_type
            __props__.__dict__["scheduler"] = scheduler
            __props__.__dict__["create_time"] = None
            __props__.__dict__["status"] = None
        super(Layer4Listener, __self__).__init__(
            'tencentcloud:Gaap/layer4Listener:Layer4Listener',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_ip_method: Optional[pulumi.Input[int]] = None,
            connect_timeout: Optional[pulumi.Input[int]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            health_check: Optional[pulumi.Input[bool]] = None,
            interval: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            proxy_id: Optional[pulumi.Input[str]] = None,
            realserver_bind_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Layer4ListenerRealserverBindSetArgs']]]]] = None,
            realserver_type: Optional[pulumi.Input[str]] = None,
            scheduler: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[int]] = None) -> 'Layer4Listener':
        """
        Get an existing Layer4Listener resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] client_ip_method: The way the listener gets the client IP, 0 for TOA, 1 for Proxy Protocol, default value is 0. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.
        :param pulumi.Input[str] create_time: Creation time of the layer4 listener.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.
        :param pulumi.Input[str] name: Name of the layer4 listener, the maximum length is 30.
        :param pulumi.Input[int] port: Port of the layer4 listener.
        :param pulumi.Input[str] protocol: Protocol of the layer4 listener. Valid value: `TCP` and `UDP`.
        :param pulumi.Input[str] proxy_id: ID of the GAAP proxy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Layer4ListenerRealserverBindSetArgs']]]] realserver_bind_sets: An information list of GAAP realserver.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.
        :param pulumi.Input[str] scheduler: Scheduling policy of the layer4 listener, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        :param pulumi.Input[int] status: Status of the layer4 listener.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _Layer4ListenerState.__new__(_Layer4ListenerState)

        __props__.__dict__["client_ip_method"] = client_ip_method
        __props__.__dict__["connect_timeout"] = connect_timeout
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["health_check"] = health_check
        __props__.__dict__["interval"] = interval
        __props__.__dict__["name"] = name
        __props__.__dict__["port"] = port
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["proxy_id"] = proxy_id
        __props__.__dict__["realserver_bind_sets"] = realserver_bind_sets
        __props__.__dict__["realserver_type"] = realserver_type
        __props__.__dict__["scheduler"] = scheduler
        __props__.__dict__["status"] = status
        return Layer4Listener(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientIpMethod")
    def client_ip_method(self) -> pulumi.Output[Optional[int]]:
        """
        The way the listener gets the client IP, 0 for TOA, 1 for Proxy Protocol, default value is 0. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "client_ip_method")

    @property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> pulumi.Output[Optional[int]]:
        """
        Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.
        """
        return pulumi.get(self, "connect_timeout")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of the layer4 listener.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[int]]:
        """
        Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the layer4 listener, the maximum length is 30.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Port of the layer4 listener.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Protocol of the layer4 listener. Valid value: `TCP` and `UDP`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> pulumi.Output[str]:
        """
        ID of the GAAP proxy.
        """
        return pulumi.get(self, "proxy_id")

    @property
    @pulumi.getter(name="realserverBindSets")
    def realserver_bind_sets(self) -> pulumi.Output[Optional[Sequence['outputs.Layer4ListenerRealserverBindSet']]]:
        """
        An information list of GAAP realserver.
        """
        return pulumi.get(self, "realserver_bind_sets")

    @property
    @pulumi.getter(name="realserverType")
    def realserver_type(self) -> pulumi.Output[str]:
        """
        Type of the realserver. Valid value: `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.
        """
        return pulumi.get(self, "realserver_type")

    @property
    @pulumi.getter
    def scheduler(self) -> pulumi.Output[Optional[str]]:
        """
        Scheduling policy of the layer4 listener, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        return pulumi.get(self, "scheduler")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[int]:
        """
        Status of the layer4 listener.
        """
        return pulumi.get(self, "status")

