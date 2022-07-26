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

__all__ = ['HttpRuleArgs', 'HttpRule']

@pulumi.input_type
class HttpRuleArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 health_check: pulumi.Input[bool],
                 listener_id: pulumi.Input[str],
                 path: pulumi.Input[str],
                 realserver_type: pulumi.Input[str],
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 forward_host: Optional[pulumi.Input[str]] = None,
                 health_check_method: Optional[pulumi.Input[str]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 health_check_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 realservers: Optional[pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None,
                 sni: Optional[pulumi.Input[str]] = None,
                 sni_switch: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HttpRule resource.
        :param pulumi.Input[str] domain: Forward domain of the forward rule.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[str] path: Path of the forward rule. Maximum length is 80.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, default value is 2s.
        :param pulumi.Input[str] forward_host: The default value of requested host which is forwarded to the realserver by the listener is `default`.
        :param pulumi.Input[str] health_check_method: Method of the health check. Valid value: `GET` and `HEAD`.
        :param pulumi.Input[str] health_check_path: Path of health check. Maximum length is 80.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] health_check_status_codes: Return code of confirmed normal. Valid value: `100`, `200`, `300`, `400` and `500`.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s.
        :param pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]] realservers: An information list of GAAP realserver.
        :param pulumi.Input[str] scheduler: Scheduling policy of the forward rule, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        :param pulumi.Input[str] sni: ServerNameIndication (SNI) is required when the SNI switch is turned on.
        :param pulumi.Input[str] sni_switch: ServerNameIndication (SNI) switch. ON means on and OFF means off.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "health_check", health_check)
        pulumi.set(__self__, "listener_id", listener_id)
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "realserver_type", realserver_type)
        if connect_timeout is not None:
            pulumi.set(__self__, "connect_timeout", connect_timeout)
        if forward_host is not None:
            pulumi.set(__self__, "forward_host", forward_host)
        if health_check_method is not None:
            pulumi.set(__self__, "health_check_method", health_check_method)
        if health_check_path is not None:
            pulumi.set(__self__, "health_check_path", health_check_path)
        if health_check_status_codes is not None:
            pulumi.set(__self__, "health_check_status_codes", health_check_status_codes)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if realservers is not None:
            pulumi.set(__self__, "realservers", realservers)
        if scheduler is not None:
            pulumi.set(__self__, "scheduler", scheduler)
        if sni is not None:
            pulumi.set(__self__, "sni", sni)
        if sni_switch is not None:
            pulumi.set(__self__, "sni_switch", sni_switch)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        Forward domain of the forward rule.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Input[bool]:
        """
        Indicates whether health check is enable.
        """
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: pulumi.Input[bool]):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        """
        ID of the layer7 listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        Path of the forward rule. Maximum length is 80.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="realserverType")
    def realserver_type(self) -> pulumi.Input[str]:
        """
        Type of the realserver. Valid value: `IP` and `DOMAIN`.
        """
        return pulumi.get(self, "realserver_type")

    @realserver_type.setter
    def realserver_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "realserver_type", value)

    @property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout of the health check response, default value is 2s.
        """
        return pulumi.get(self, "connect_timeout")

    @connect_timeout.setter
    def connect_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "connect_timeout", value)

    @property
    @pulumi.getter(name="forwardHost")
    def forward_host(self) -> Optional[pulumi.Input[str]]:
        """
        The default value of requested host which is forwarded to the realserver by the listener is `default`.
        """
        return pulumi.get(self, "forward_host")

    @forward_host.setter
    def forward_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forward_host", value)

    @property
    @pulumi.getter(name="healthCheckMethod")
    def health_check_method(self) -> Optional[pulumi.Input[str]]:
        """
        Method of the health check. Valid value: `GET` and `HEAD`.
        """
        return pulumi.get(self, "health_check_method")

    @health_check_method.setter
    def health_check_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_method", value)

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[str]]:
        """
        Path of health check. Maximum length is 80.
        """
        return pulumi.get(self, "health_check_path")

    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_path", value)

    @property
    @pulumi.getter(name="healthCheckStatusCodes")
    def health_check_status_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Return code of confirmed normal. Valid value: `100`, `200`, `300`, `400` and `500`.
        """
        return pulumi.get(self, "health_check_status_codes")

    @health_check_status_codes.setter
    def health_check_status_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "health_check_status_codes", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Interval of the health check, default value is 5s.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter
    def realservers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]]]:
        """
        An information list of GAAP realserver.
        """
        return pulumi.get(self, "realservers")

    @realservers.setter
    def realservers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]]]):
        pulumi.set(self, "realservers", value)

    @property
    @pulumi.getter
    def scheduler(self) -> Optional[pulumi.Input[str]]:
        """
        Scheduling policy of the forward rule, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        return pulumi.get(self, "scheduler")

    @scheduler.setter
    def scheduler(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduler", value)

    @property
    @pulumi.getter
    def sni(self) -> Optional[pulumi.Input[str]]:
        """
        ServerNameIndication (SNI) is required when the SNI switch is turned on.
        """
        return pulumi.get(self, "sni")

    @sni.setter
    def sni(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sni", value)

    @property
    @pulumi.getter(name="sniSwitch")
    def sni_switch(self) -> Optional[pulumi.Input[str]]:
        """
        ServerNameIndication (SNI) switch. ON means on and OFF means off.
        """
        return pulumi.get(self, "sni_switch")

    @sni_switch.setter
    def sni_switch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sni_switch", value)


@pulumi.input_type
class _HttpRuleState:
    def __init__(__self__, *,
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 forward_host: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input[bool]] = None,
                 health_check_method: Optional[pulumi.Input[str]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 health_check_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 realserver_type: Optional[pulumi.Input[str]] = None,
                 realservers: Optional[pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None,
                 sni: Optional[pulumi.Input[str]] = None,
                 sni_switch: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HttpRule resources.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, default value is 2s.
        :param pulumi.Input[str] domain: Forward domain of the forward rule.
        :param pulumi.Input[str] forward_host: The default value of requested host which is forwarded to the realserver by the listener is `default`.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable.
        :param pulumi.Input[str] health_check_method: Method of the health check. Valid value: `GET` and `HEAD`.
        :param pulumi.Input[str] health_check_path: Path of health check. Maximum length is 80.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] health_check_status_codes: Return code of confirmed normal. Valid value: `100`, `200`, `300`, `400` and `500`.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[str] path: Path of the forward rule. Maximum length is 80.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`.
        :param pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]] realservers: An information list of GAAP realserver.
        :param pulumi.Input[str] scheduler: Scheduling policy of the forward rule, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        :param pulumi.Input[str] sni: ServerNameIndication (SNI) is required when the SNI switch is turned on.
        :param pulumi.Input[str] sni_switch: ServerNameIndication (SNI) switch. ON means on and OFF means off.
        """
        if connect_timeout is not None:
            pulumi.set(__self__, "connect_timeout", connect_timeout)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if forward_host is not None:
            pulumi.set(__self__, "forward_host", forward_host)
        if health_check is not None:
            pulumi.set(__self__, "health_check", health_check)
        if health_check_method is not None:
            pulumi.set(__self__, "health_check_method", health_check_method)
        if health_check_path is not None:
            pulumi.set(__self__, "health_check_path", health_check_path)
        if health_check_status_codes is not None:
            pulumi.set(__self__, "health_check_status_codes", health_check_status_codes)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if listener_id is not None:
            pulumi.set(__self__, "listener_id", listener_id)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if realserver_type is not None:
            pulumi.set(__self__, "realserver_type", realserver_type)
        if realservers is not None:
            pulumi.set(__self__, "realservers", realservers)
        if scheduler is not None:
            pulumi.set(__self__, "scheduler", scheduler)
        if sni is not None:
            pulumi.set(__self__, "sni", sni)
        if sni_switch is not None:
            pulumi.set(__self__, "sni_switch", sni_switch)

    @property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout of the health check response, default value is 2s.
        """
        return pulumi.get(self, "connect_timeout")

    @connect_timeout.setter
    def connect_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "connect_timeout", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Forward domain of the forward rule.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="forwardHost")
    def forward_host(self) -> Optional[pulumi.Input[str]]:
        """
        The default value of requested host which is forwarded to the realserver by the listener is `default`.
        """
        return pulumi.get(self, "forward_host")

    @forward_host.setter
    def forward_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forward_host", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether health check is enable.
        """
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter(name="healthCheckMethod")
    def health_check_method(self) -> Optional[pulumi.Input[str]]:
        """
        Method of the health check. Valid value: `GET` and `HEAD`.
        """
        return pulumi.get(self, "health_check_method")

    @health_check_method.setter
    def health_check_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_method", value)

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[str]]:
        """
        Path of health check. Maximum length is 80.
        """
        return pulumi.get(self, "health_check_path")

    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_path", value)

    @property
    @pulumi.getter(name="healthCheckStatusCodes")
    def health_check_status_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Return code of confirmed normal. Valid value: `100`, `200`, `300`, `400` and `500`.
        """
        return pulumi.get(self, "health_check_status_codes")

    @health_check_status_codes.setter
    def health_check_status_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "health_check_status_codes", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Interval of the health check, default value is 5s.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the layer7 listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Path of the forward rule. Maximum length is 80.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="realserverType")
    def realserver_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the realserver. Valid value: `IP` and `DOMAIN`.
        """
        return pulumi.get(self, "realserver_type")

    @realserver_type.setter
    def realserver_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realserver_type", value)

    @property
    @pulumi.getter
    def realservers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]]]:
        """
        An information list of GAAP realserver.
        """
        return pulumi.get(self, "realservers")

    @realservers.setter
    def realservers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HttpRuleRealserverArgs']]]]):
        pulumi.set(self, "realservers", value)

    @property
    @pulumi.getter
    def scheduler(self) -> Optional[pulumi.Input[str]]:
        """
        Scheduling policy of the forward rule, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        return pulumi.get(self, "scheduler")

    @scheduler.setter
    def scheduler(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduler", value)

    @property
    @pulumi.getter
    def sni(self) -> Optional[pulumi.Input[str]]:
        """
        ServerNameIndication (SNI) is required when the SNI switch is turned on.
        """
        return pulumi.get(self, "sni")

    @sni.setter
    def sni(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sni", value)

    @property
    @pulumi.getter(name="sniSwitch")
    def sni_switch(self) -> Optional[pulumi.Input[str]]:
        """
        ServerNameIndication (SNI) switch. ON means on and OFF means off.
        """
        return pulumi.get(self, "sni_switch")

    @sni_switch.setter
    def sni_switch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sni_switch", value)


class HttpRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 forward_host: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input[bool]] = None,
                 health_check_method: Optional[pulumi.Input[str]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 health_check_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 realserver_type: Optional[pulumi.Input[str]] = None,
                 realservers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HttpRuleRealserverArgs']]]]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None,
                 sni: Optional[pulumi.Input[str]] = None,
                 sni_switch: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a HttpRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, default value is 2s.
        :param pulumi.Input[str] domain: Forward domain of the forward rule.
        :param pulumi.Input[str] forward_host: The default value of requested host which is forwarded to the realserver by the listener is `default`.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable.
        :param pulumi.Input[str] health_check_method: Method of the health check. Valid value: `GET` and `HEAD`.
        :param pulumi.Input[str] health_check_path: Path of health check. Maximum length is 80.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] health_check_status_codes: Return code of confirmed normal. Valid value: `100`, `200`, `300`, `400` and `500`.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[str] path: Path of the forward rule. Maximum length is 80.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HttpRuleRealserverArgs']]]] realservers: An information list of GAAP realserver.
        :param pulumi.Input[str] scheduler: Scheduling policy of the forward rule, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        :param pulumi.Input[str] sni: ServerNameIndication (SNI) is required when the SNI switch is turned on.
        :param pulumi.Input[str] sni_switch: ServerNameIndication (SNI) switch. ON means on and OFF means off.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HttpRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a HttpRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param HttpRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HttpRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connect_timeout: Optional[pulumi.Input[int]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 forward_host: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input[bool]] = None,
                 health_check_method: Optional[pulumi.Input[str]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 health_check_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 realserver_type: Optional[pulumi.Input[str]] = None,
                 realservers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HttpRuleRealserverArgs']]]]] = None,
                 scheduler: Optional[pulumi.Input[str]] = None,
                 sni: Optional[pulumi.Input[str]] = None,
                 sni_switch: Optional[pulumi.Input[str]] = None,
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
            __props__ = HttpRuleArgs.__new__(HttpRuleArgs)

            __props__.__dict__["connect_timeout"] = connect_timeout
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["forward_host"] = forward_host
            if health_check is None and not opts.urn:
                raise TypeError("Missing required property 'health_check'")
            __props__.__dict__["health_check"] = health_check
            __props__.__dict__["health_check_method"] = health_check_method
            __props__.__dict__["health_check_path"] = health_check_path
            __props__.__dict__["health_check_status_codes"] = health_check_status_codes
            __props__.__dict__["interval"] = interval
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            if realserver_type is None and not opts.urn:
                raise TypeError("Missing required property 'realserver_type'")
            __props__.__dict__["realserver_type"] = realserver_type
            __props__.__dict__["realservers"] = realservers
            __props__.__dict__["scheduler"] = scheduler
            __props__.__dict__["sni"] = sni
            __props__.__dict__["sni_switch"] = sni_switch
        super(HttpRule, __self__).__init__(
            'tencentcloud:Gaap/httpRule:HttpRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connect_timeout: Optional[pulumi.Input[int]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            forward_host: Optional[pulumi.Input[str]] = None,
            health_check: Optional[pulumi.Input[bool]] = None,
            health_check_method: Optional[pulumi.Input[str]] = None,
            health_check_path: Optional[pulumi.Input[str]] = None,
            health_check_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            interval: Optional[pulumi.Input[int]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            realserver_type: Optional[pulumi.Input[str]] = None,
            realservers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HttpRuleRealserverArgs']]]]] = None,
            scheduler: Optional[pulumi.Input[str]] = None,
            sni: Optional[pulumi.Input[str]] = None,
            sni_switch: Optional[pulumi.Input[str]] = None) -> 'HttpRule':
        """
        Get an existing HttpRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] connect_timeout: Timeout of the health check response, default value is 2s.
        :param pulumi.Input[str] domain: Forward domain of the forward rule.
        :param pulumi.Input[str] forward_host: The default value of requested host which is forwarded to the realserver by the listener is `default`.
        :param pulumi.Input[bool] health_check: Indicates whether health check is enable.
        :param pulumi.Input[str] health_check_method: Method of the health check. Valid value: `GET` and `HEAD`.
        :param pulumi.Input[str] health_check_path: Path of health check. Maximum length is 80.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] health_check_status_codes: Return code of confirmed normal. Valid value: `100`, `200`, `300`, `400` and `500`.
        :param pulumi.Input[int] interval: Interval of the health check, default value is 5s.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[str] path: Path of the forward rule. Maximum length is 80.
        :param pulumi.Input[str] realserver_type: Type of the realserver. Valid value: `IP` and `DOMAIN`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HttpRuleRealserverArgs']]]] realservers: An information list of GAAP realserver.
        :param pulumi.Input[str] scheduler: Scheduling policy of the forward rule, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        :param pulumi.Input[str] sni: ServerNameIndication (SNI) is required when the SNI switch is turned on.
        :param pulumi.Input[str] sni_switch: ServerNameIndication (SNI) switch. ON means on and OFF means off.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HttpRuleState.__new__(_HttpRuleState)

        __props__.__dict__["connect_timeout"] = connect_timeout
        __props__.__dict__["domain"] = domain
        __props__.__dict__["forward_host"] = forward_host
        __props__.__dict__["health_check"] = health_check
        __props__.__dict__["health_check_method"] = health_check_method
        __props__.__dict__["health_check_path"] = health_check_path
        __props__.__dict__["health_check_status_codes"] = health_check_status_codes
        __props__.__dict__["interval"] = interval
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["path"] = path
        __props__.__dict__["realserver_type"] = realserver_type
        __props__.__dict__["realservers"] = realservers
        __props__.__dict__["scheduler"] = scheduler
        __props__.__dict__["sni"] = sni
        __props__.__dict__["sni_switch"] = sni_switch
        return HttpRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> pulumi.Output[Optional[int]]:
        """
        Timeout of the health check response, default value is 2s.
        """
        return pulumi.get(self, "connect_timeout")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        Forward domain of the forward rule.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="forwardHost")
    def forward_host(self) -> pulumi.Output[Optional[str]]:
        """
        The default value of requested host which is forwarded to the realserver by the listener is `default`.
        """
        return pulumi.get(self, "forward_host")

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output[bool]:
        """
        Indicates whether health check is enable.
        """
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter(name="healthCheckMethod")
    def health_check_method(self) -> pulumi.Output[Optional[str]]:
        """
        Method of the health check. Valid value: `GET` and `HEAD`.
        """
        return pulumi.get(self, "health_check_method")

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> pulumi.Output[Optional[str]]:
        """
        Path of health check. Maximum length is 80.
        """
        return pulumi.get(self, "health_check_path")

    @property
    @pulumi.getter(name="healthCheckStatusCodes")
    def health_check_status_codes(self) -> pulumi.Output[Sequence[int]]:
        """
        Return code of confirmed normal. Valid value: `100`, `200`, `300`, `400` and `500`.
        """
        return pulumi.get(self, "health_check_status_codes")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[int]]:
        """
        Interval of the health check, default value is 5s.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        ID of the layer7 listener.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Path of the forward rule. Maximum length is 80.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="realserverType")
    def realserver_type(self) -> pulumi.Output[str]:
        """
        Type of the realserver. Valid value: `IP` and `DOMAIN`.
        """
        return pulumi.get(self, "realserver_type")

    @property
    @pulumi.getter
    def realservers(self) -> pulumi.Output[Optional[Sequence['outputs.HttpRuleRealserver']]]:
        """
        An information list of GAAP realserver.
        """
        return pulumi.get(self, "realservers")

    @property
    @pulumi.getter
    def scheduler(self) -> pulumi.Output[Optional[str]]:
        """
        Scheduling policy of the forward rule, default value is `rr`. Valid value: `rr`, `wrr` and `lc`.
        """
        return pulumi.get(self, "scheduler")

    @property
    @pulumi.getter
    def sni(self) -> pulumi.Output[str]:
        """
        ServerNameIndication (SNI) is required when the SNI switch is turned on.
        """
        return pulumi.get(self, "sni")

    @property
    @pulumi.getter(name="sniSwitch")
    def sni_switch(self) -> pulumi.Output[str]:
        """
        ServerNameIndication (SNI) switch. ON means on and OFF means off.
        """
        return pulumi.get(self, "sni_switch")

