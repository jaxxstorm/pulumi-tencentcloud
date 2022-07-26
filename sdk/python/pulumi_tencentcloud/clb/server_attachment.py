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

__all__ = ['ServerAttachmentArgs', 'ServerAttachment']

@pulumi.input_type
class ServerAttachmentArgs:
    def __init__(__self__, *,
                 clb_id: pulumi.Input[str],
                 listener_id: pulumi.Input[str],
                 targets: pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]],
                 rule_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerAttachment resource.
        :param pulumi.Input[str] clb_id: ID of the CLB.
        :param pulumi.Input[str] listener_id: ID of the CLB listener.
        :param pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]] targets: Information of the backends to be attached.
        :param pulumi.Input[str] rule_id: ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
        """
        pulumi.set(__self__, "clb_id", clb_id)
        pulumi.set(__self__, "listener_id", listener_id)
        pulumi.set(__self__, "targets", targets)
        if rule_id is not None:
            pulumi.set(__self__, "rule_id", rule_id)

    @property
    @pulumi.getter(name="clbId")
    def clb_id(self) -> pulumi.Input[str]:
        """
        ID of the CLB.
        """
        return pulumi.get(self, "clb_id")

    @clb_id.setter
    def clb_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "clb_id", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        """
        ID of the CLB listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]]:
        """
        Information of the backends to be attached.
        """
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]]):
        pulumi.set(self, "targets", value)

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
        """
        return pulumi.get(self, "rule_id")

    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_id", value)


@pulumi.input_type
class _ServerAttachmentState:
    def __init__(__self__, *,
                 clb_id: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 protocol_type: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]]] = None):
        """
        Input properties used for looking up and filtering ServerAttachment resources.
        :param pulumi.Input[str] clb_id: ID of the CLB.
        :param pulumi.Input[str] listener_id: ID of the CLB listener.
        :param pulumi.Input[str] protocol_type: Type of protocol within the listener.
        :param pulumi.Input[str] rule_id: ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
        :param pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]] targets: Information of the backends to be attached.
        """
        if clb_id is not None:
            pulumi.set(__self__, "clb_id", clb_id)
        if listener_id is not None:
            pulumi.set(__self__, "listener_id", listener_id)
        if protocol_type is not None:
            pulumi.set(__self__, "protocol_type", protocol_type)
        if rule_id is not None:
            pulumi.set(__self__, "rule_id", rule_id)
        if targets is not None:
            pulumi.set(__self__, "targets", targets)

    @property
    @pulumi.getter(name="clbId")
    def clb_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the CLB.
        """
        return pulumi.get(self, "clb_id")

    @clb_id.setter
    def clb_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "clb_id", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the CLB listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of protocol within the listener.
        """
        return pulumi.get(self, "protocol_type")

    @protocol_type.setter
    def protocol_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol_type", value)

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
        """
        return pulumi.get(self, "rule_id")

    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_id", value)

    @property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]]]:
        """
        Information of the backends to be attached.
        """
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerAttachmentTargetArgs']]]]):
        pulumi.set(self, "targets", value)


class ServerAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clb_id: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerAttachmentTargetArgs']]]]] = None,
                 __props__=None):
        """
        Create a ServerAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] clb_id: ID of the CLB.
        :param pulumi.Input[str] listener_id: ID of the CLB listener.
        :param pulumi.Input[str] rule_id: ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerAttachmentTargetArgs']]]] targets: Information of the backends to be attached.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ServerAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ServerAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clb_id: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerAttachmentTargetArgs']]]]] = None,
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
            __props__ = ServerAttachmentArgs.__new__(ServerAttachmentArgs)

            if clb_id is None and not opts.urn:
                raise TypeError("Missing required property 'clb_id'")
            __props__.__dict__["clb_id"] = clb_id
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            __props__.__dict__["rule_id"] = rule_id
            if targets is None and not opts.urn:
                raise TypeError("Missing required property 'targets'")
            __props__.__dict__["targets"] = targets
            __props__.__dict__["protocol_type"] = None
        super(ServerAttachment, __self__).__init__(
            'tencentcloud:Clb/serverAttachment:ServerAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            clb_id: Optional[pulumi.Input[str]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            protocol_type: Optional[pulumi.Input[str]] = None,
            rule_id: Optional[pulumi.Input[str]] = None,
            targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerAttachmentTargetArgs']]]]] = None) -> 'ServerAttachment':
        """
        Get an existing ServerAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] clb_id: ID of the CLB.
        :param pulumi.Input[str] listener_id: ID of the CLB listener.
        :param pulumi.Input[str] protocol_type: Type of protocol within the listener.
        :param pulumi.Input[str] rule_id: ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerAttachmentTargetArgs']]]] targets: Information of the backends to be attached.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServerAttachmentState.__new__(_ServerAttachmentState)

        __props__.__dict__["clb_id"] = clb_id
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["protocol_type"] = protocol_type
        __props__.__dict__["rule_id"] = rule_id
        __props__.__dict__["targets"] = targets
        return ServerAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clbId")
    def clb_id(self) -> pulumi.Output[str]:
        """
        ID of the CLB.
        """
        return pulumi.get(self, "clb_id")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        ID of the CLB listener.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Output[str]:
        """
        Type of protocol within the listener.
        """
        return pulumi.get(self, "protocol_type")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
        """
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Output[Sequence['outputs.ServerAttachmentTarget']]:
        """
        Information of the backends to be attached.
        """
        return pulumi.get(self, "targets")

