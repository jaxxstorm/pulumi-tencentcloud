# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TemplateArgs', 'Template']

@pulumi.input_type
class TemplateArgs:
    def __init__(__self__, *,
                 protocols: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Template resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocols: Protocol list. Valid protocols are `tcp`, `udp`, `icmp`, `gre`. Single port(tcp:80), multi-port(tcp:80,443), port
               range(tcp:3306-20000), all(tcp:all) format are support. Protocol `icmp` and `gre` cannot specify port.
        :param pulumi.Input[str] name: Name of the protocol template.
        """
        pulumi.set(__self__, "protocols", protocols)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def protocols(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Protocol list. Valid protocols are `tcp`, `udp`, `icmp`, `gre`. Single port(tcp:80), multi-port(tcp:80,443), port
        range(tcp:3306-20000), all(tcp:all) format are support. Protocol `icmp` and `gre` cannot specify port.
        """
        return pulumi.get(self, "protocols")

    @protocols.setter
    def protocols(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "protocols", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the protocol template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TemplateState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 protocols: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Template resources.
        :param pulumi.Input[str] name: Name of the protocol template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocols: Protocol list. Valid protocols are `tcp`, `udp`, `icmp`, `gre`. Single port(tcp:80), multi-port(tcp:80,443), port
               range(tcp:3306-20000), all(tcp:all) format are support. Protocol `icmp` and `gre` cannot specify port.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protocols is not None:
            pulumi.set(__self__, "protocols", protocols)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the protocol template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Protocol list. Valid protocols are `tcp`, `udp`, `icmp`, `gre`. Single port(tcp:80), multi-port(tcp:80,443), port
        range(tcp:3306-20000), all(tcp:all) format are support. Protocol `icmp` and `gre` cannot specify port.
        """
        return pulumi.get(self, "protocols")

    @protocols.setter
    def protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "protocols", value)


class Template(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocols: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Template resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the protocol template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocols: Protocol list. Valid protocols are `tcp`, `udp`, `icmp`, `gre`. Single port(tcp:80), multi-port(tcp:80,443), port
               range(tcp:3306-20000), all(tcp:all) format are support. Protocol `icmp` and `gre` cannot specify port.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Template resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protocols: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = TemplateArgs.__new__(TemplateArgs)

            __props__.__dict__["name"] = name
            if protocols is None and not opts.urn:
                raise TypeError("Missing required property 'protocols'")
            __props__.__dict__["protocols"] = protocols
        super(Template, __self__).__init__(
            'tencentcloud:Protocol/template:Template',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            protocols: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Template':
        """
        Get an existing Template resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the protocol template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocols: Protocol list. Valid protocols are `tcp`, `udp`, `icmp`, `gre`. Single port(tcp:80), multi-port(tcp:80,443), port
               range(tcp:3306-20000), all(tcp:all) format are support. Protocol `icmp` and `gre` cannot specify port.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TemplateState.__new__(_TemplateState)

        __props__.__dict__["name"] = name
        __props__.__dict__["protocols"] = protocols
        return Template(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the protocol template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Sequence[str]]:
        """
        Protocol list. Valid protocols are `tcp`, `udp`, `icmp`, `gre`. Single port(tcp:80), multi-port(tcp:80,443), port
        range(tcp:3306-20000), all(tcp:all) format are support. Protocol `icmp` and `gre` cannot specify port.
        """
        return pulumi.get(self, "protocols")

