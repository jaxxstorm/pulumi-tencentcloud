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

__all__ = ['DdosPolicyArgs', 'DdosPolicy']

@pulumi.input_type
class DdosPolicyArgs:
    def __init__(__self__, *,
                 drop_options: pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]],
                 resource_type: pulumi.Input[str],
                 black_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 packet_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]]] = None,
                 port_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]]] = None,
                 watermark_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]]] = None,
                 white_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DdosPolicy resource.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]] drop_options: Option list of abnormal check of the DDos policy, should set at least one policy.
        :param pulumi.Input[str] resource_type: Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] black_ips: Black IP list.
        :param pulumi.Input[str] name: Name of the DDoS policy. Length should between 1 and 32.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]] packet_filters: Message filter options list.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]] port_filters: Port limits of abnormal check of the DDos policy.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]] watermark_filters: Watermark policy options, and only support one watermark policy at most.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] white_ips: White IP list.
        """
        pulumi.set(__self__, "drop_options", drop_options)
        pulumi.set(__self__, "resource_type", resource_type)
        if black_ips is not None:
            pulumi.set(__self__, "black_ips", black_ips)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if packet_filters is not None:
            pulumi.set(__self__, "packet_filters", packet_filters)
        if port_filters is not None:
            pulumi.set(__self__, "port_filters", port_filters)
        if watermark_filters is not None:
            pulumi.set(__self__, "watermark_filters", watermark_filters)
        if white_ips is not None:
            pulumi.set(__self__, "white_ips", white_ips)

    @property
    @pulumi.getter(name="dropOptions")
    def drop_options(self) -> pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]]:
        """
        Option list of abnormal check of the DDos policy, should set at least one policy.
        """
        return pulumi.get(self, "drop_options")

    @drop_options.setter
    def drop_options(self, value: pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]]):
        pulumi.set(self, "drop_options", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="blackIps")
    def black_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Black IP list.
        """
        return pulumi.get(self, "black_ips")

    @black_ips.setter
    def black_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "black_ips", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the DDoS policy. Length should between 1 and 32.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="packetFilters")
    def packet_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]]]:
        """
        Message filter options list.
        """
        return pulumi.get(self, "packet_filters")

    @packet_filters.setter
    def packet_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]]]):
        pulumi.set(self, "packet_filters", value)

    @property
    @pulumi.getter(name="portFilters")
    def port_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]]]:
        """
        Port limits of abnormal check of the DDos policy.
        """
        return pulumi.get(self, "port_filters")

    @port_filters.setter
    def port_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]]]):
        pulumi.set(self, "port_filters", value)

    @property
    @pulumi.getter(name="watermarkFilters")
    def watermark_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]]]:
        """
        Watermark policy options, and only support one watermark policy at most.
        """
        return pulumi.get(self, "watermark_filters")

    @watermark_filters.setter
    def watermark_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]]]):
        pulumi.set(self, "watermark_filters", value)

    @property
    @pulumi.getter(name="whiteIps")
    def white_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        White IP list.
        """
        return pulumi.get(self, "white_ips")

    @white_ips.setter
    def white_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "white_ips", value)


@pulumi.input_type
class _DdosPolicyState:
    def __init__(__self__, *,
                 black_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 drop_options: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 packet_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 port_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 scene_id: Optional[pulumi.Input[str]] = None,
                 watermark_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]]] = None,
                 watermark_keys: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkKeyArgs']]]] = None,
                 white_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering DdosPolicy resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] black_ips: Black IP list.
        :param pulumi.Input[str] create_time: Create time of the DDoS policy.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]] drop_options: Option list of abnormal check of the DDos policy, should set at least one policy.
        :param pulumi.Input[str] name: Name of the DDoS policy. Length should between 1 and 32.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]] packet_filters: Message filter options list.
        :param pulumi.Input[str] policy_id: Id of policy.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]] port_filters: Port limits of abnormal check of the DDos policy.
        :param pulumi.Input[str] resource_type: Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.
        :param pulumi.Input[str] scene_id: Id of policy case that the DDoS policy works for.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]] watermark_filters: Watermark policy options, and only support one watermark policy at most.
        :param pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkKeyArgs']]] watermark_keys: Watermark content.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] white_ips: White IP list.
        """
        if black_ips is not None:
            pulumi.set(__self__, "black_ips", black_ips)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if drop_options is not None:
            pulumi.set(__self__, "drop_options", drop_options)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if packet_filters is not None:
            pulumi.set(__self__, "packet_filters", packet_filters)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if port_filters is not None:
            pulumi.set(__self__, "port_filters", port_filters)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if scene_id is not None:
            pulumi.set(__self__, "scene_id", scene_id)
        if watermark_filters is not None:
            pulumi.set(__self__, "watermark_filters", watermark_filters)
        if watermark_keys is not None:
            pulumi.set(__self__, "watermark_keys", watermark_keys)
        if white_ips is not None:
            pulumi.set(__self__, "white_ips", white_ips)

    @property
    @pulumi.getter(name="blackIps")
    def black_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Black IP list.
        """
        return pulumi.get(self, "black_ips")

    @black_ips.setter
    def black_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "black_ips", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Create time of the DDoS policy.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="dropOptions")
    def drop_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]]]:
        """
        Option list of abnormal check of the DDos policy, should set at least one policy.
        """
        return pulumi.get(self, "drop_options")

    @drop_options.setter
    def drop_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyDropOptionArgs']]]]):
        pulumi.set(self, "drop_options", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the DDoS policy. Length should between 1 and 32.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="packetFilters")
    def packet_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]]]:
        """
        Message filter options list.
        """
        return pulumi.get(self, "packet_filters")

    @packet_filters.setter
    def packet_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPacketFilterArgs']]]]):
        pulumi.set(self, "packet_filters", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="portFilters")
    def port_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]]]:
        """
        Port limits of abnormal check of the DDos policy.
        """
        return pulumi.get(self, "port_filters")

    @port_filters.setter
    def port_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyPortFilterArgs']]]]):
        pulumi.set(self, "port_filters", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="sceneId")
    def scene_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of policy case that the DDoS policy works for.
        """
        return pulumi.get(self, "scene_id")

    @scene_id.setter
    def scene_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scene_id", value)

    @property
    @pulumi.getter(name="watermarkFilters")
    def watermark_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]]]:
        """
        Watermark policy options, and only support one watermark policy at most.
        """
        return pulumi.get(self, "watermark_filters")

    @watermark_filters.setter
    def watermark_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkFilterArgs']]]]):
        pulumi.set(self, "watermark_filters", value)

    @property
    @pulumi.getter(name="watermarkKeys")
    def watermark_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkKeyArgs']]]]:
        """
        Watermark content.
        """
        return pulumi.get(self, "watermark_keys")

    @watermark_keys.setter
    def watermark_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DdosPolicyWatermarkKeyArgs']]]]):
        pulumi.set(self, "watermark_keys", value)

    @property
    @pulumi.getter(name="whiteIps")
    def white_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        White IP list.
        """
        return pulumi.get(self, "white_ips")

    @white_ips.setter
    def white_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "white_ips", value)


class DdosPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 black_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 drop_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyDropOptionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 packet_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPacketFilterArgs']]]]] = None,
                 port_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPortFilterArgs']]]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 watermark_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyWatermarkFilterArgs']]]]] = None,
                 white_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a DdosPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] black_ips: Black IP list.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyDropOptionArgs']]]] drop_options: Option list of abnormal check of the DDos policy, should set at least one policy.
        :param pulumi.Input[str] name: Name of the DDoS policy. Length should between 1 and 32.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPacketFilterArgs']]]] packet_filters: Message filter options list.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPortFilterArgs']]]] port_filters: Port limits of abnormal check of the DDos policy.
        :param pulumi.Input[str] resource_type: Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyWatermarkFilterArgs']]]] watermark_filters: Watermark policy options, and only support one watermark policy at most.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] white_ips: White IP list.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DdosPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DdosPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DdosPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DdosPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 black_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 drop_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyDropOptionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 packet_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPacketFilterArgs']]]]] = None,
                 port_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPortFilterArgs']]]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 watermark_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyWatermarkFilterArgs']]]]] = None,
                 white_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = DdosPolicyArgs.__new__(DdosPolicyArgs)

            __props__.__dict__["black_ips"] = black_ips
            if drop_options is None and not opts.urn:
                raise TypeError("Missing required property 'drop_options'")
            __props__.__dict__["drop_options"] = drop_options
            __props__.__dict__["name"] = name
            __props__.__dict__["packet_filters"] = packet_filters
            __props__.__dict__["port_filters"] = port_filters
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["watermark_filters"] = watermark_filters
            __props__.__dict__["white_ips"] = white_ips
            __props__.__dict__["create_time"] = None
            __props__.__dict__["policy_id"] = None
            __props__.__dict__["scene_id"] = None
            __props__.__dict__["watermark_keys"] = None
        super(DdosPolicy, __self__).__init__(
            'tencentcloud:Dayu/ddosPolicy:DdosPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            black_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            drop_options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyDropOptionArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            packet_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPacketFilterArgs']]]]] = None,
            policy_id: Optional[pulumi.Input[str]] = None,
            port_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPortFilterArgs']]]]] = None,
            resource_type: Optional[pulumi.Input[str]] = None,
            scene_id: Optional[pulumi.Input[str]] = None,
            watermark_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyWatermarkFilterArgs']]]]] = None,
            watermark_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyWatermarkKeyArgs']]]]] = None,
            white_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'DdosPolicy':
        """
        Get an existing DdosPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] black_ips: Black IP list.
        :param pulumi.Input[str] create_time: Create time of the DDoS policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyDropOptionArgs']]]] drop_options: Option list of abnormal check of the DDos policy, should set at least one policy.
        :param pulumi.Input[str] name: Name of the DDoS policy. Length should between 1 and 32.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPacketFilterArgs']]]] packet_filters: Message filter options list.
        :param pulumi.Input[str] policy_id: Id of policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyPortFilterArgs']]]] port_filters: Port limits of abnormal check of the DDos policy.
        :param pulumi.Input[str] resource_type: Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.
        :param pulumi.Input[str] scene_id: Id of policy case that the DDoS policy works for.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyWatermarkFilterArgs']]]] watermark_filters: Watermark policy options, and only support one watermark policy at most.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DdosPolicyWatermarkKeyArgs']]]] watermark_keys: Watermark content.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] white_ips: White IP list.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DdosPolicyState.__new__(_DdosPolicyState)

        __props__.__dict__["black_ips"] = black_ips
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["drop_options"] = drop_options
        __props__.__dict__["name"] = name
        __props__.__dict__["packet_filters"] = packet_filters
        __props__.__dict__["policy_id"] = policy_id
        __props__.__dict__["port_filters"] = port_filters
        __props__.__dict__["resource_type"] = resource_type
        __props__.__dict__["scene_id"] = scene_id
        __props__.__dict__["watermark_filters"] = watermark_filters
        __props__.__dict__["watermark_keys"] = watermark_keys
        __props__.__dict__["white_ips"] = white_ips
        return DdosPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blackIps")
    def black_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Black IP list.
        """
        return pulumi.get(self, "black_ips")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time of the DDoS policy.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dropOptions")
    def drop_options(self) -> pulumi.Output[Sequence['outputs.DdosPolicyDropOption']]:
        """
        Option list of abnormal check of the DDos policy, should set at least one policy.
        """
        return pulumi.get(self, "drop_options")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the DDoS policy. Length should between 1 and 32.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packetFilters")
    def packet_filters(self) -> pulumi.Output[Optional[Sequence['outputs.DdosPolicyPacketFilter']]]:
        """
        Message filter options list.
        """
        return pulumi.get(self, "packet_filters")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        Id of policy.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="portFilters")
    def port_filters(self) -> pulumi.Output[Optional[Sequence['outputs.DdosPolicyPortFilter']]]:
        """
        Port limits of abnormal check of the DDos policy.
        """
        return pulumi.get(self, "port_filters")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="sceneId")
    def scene_id(self) -> pulumi.Output[str]:
        """
        Id of policy case that the DDoS policy works for.
        """
        return pulumi.get(self, "scene_id")

    @property
    @pulumi.getter(name="watermarkFilters")
    def watermark_filters(self) -> pulumi.Output[Optional[Sequence['outputs.DdosPolicyWatermarkFilter']]]:
        """
        Watermark policy options, and only support one watermark policy at most.
        """
        return pulumi.get(self, "watermark_filters")

    @property
    @pulumi.getter(name="watermarkKeys")
    def watermark_keys(self) -> pulumi.Output[Sequence['outputs.DdosPolicyWatermarkKey']]:
        """
        Watermark content.
        """
        return pulumi.get(self, "watermark_keys")

    @property
    @pulumi.getter(name="whiteIps")
    def white_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        White IP list.
        """
        return pulumi.get(self, "white_ips")

