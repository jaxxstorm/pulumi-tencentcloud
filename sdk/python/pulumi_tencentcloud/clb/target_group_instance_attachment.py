# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TargetGroupInstanceAttachmentArgs', 'TargetGroupInstanceAttachment']

@pulumi.input_type
class TargetGroupInstanceAttachmentArgs:
    def __init__(__self__, *,
                 bind_ip: pulumi.Input[str],
                 port: pulumi.Input[int],
                 target_group_id: pulumi.Input[str],
                 weight: pulumi.Input[int]):
        """
        The set of arguments for constructing a TargetGroupInstanceAttachment resource.
        :param pulumi.Input[str] bind_ip: The Intranet IP of the target group instance.
        :param pulumi.Input[int] port: Port of the target group instance.
        :param pulumi.Input[str] target_group_id: Target group ID.
        :param pulumi.Input[int] weight: The weight of the target group instance.
        """
        pulumi.set(__self__, "bind_ip", bind_ip)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "target_group_id", target_group_id)
        pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="bindIp")
    def bind_ip(self) -> pulumi.Input[str]:
        """
        The Intranet IP of the target group instance.
        """
        return pulumi.get(self, "bind_ip")

    @bind_ip.setter
    def bind_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "bind_ip", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        Port of the target group instance.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="targetGroupId")
    def target_group_id(self) -> pulumi.Input[str]:
        """
        Target group ID.
        """
        return pulumi.get(self, "target_group_id")

    @target_group_id.setter
    def target_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_group_id", value)

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Input[int]:
        """
        The weight of the target group instance.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: pulumi.Input[int]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class _TargetGroupInstanceAttachmentState:
    def __init__(__self__, *,
                 bind_ip: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 target_group_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering TargetGroupInstanceAttachment resources.
        :param pulumi.Input[str] bind_ip: The Intranet IP of the target group instance.
        :param pulumi.Input[int] port: Port of the target group instance.
        :param pulumi.Input[str] target_group_id: Target group ID.
        :param pulumi.Input[int] weight: The weight of the target group instance.
        """
        if bind_ip is not None:
            pulumi.set(__self__, "bind_ip", bind_ip)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if target_group_id is not None:
            pulumi.set(__self__, "target_group_id", target_group_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="bindIp")
    def bind_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The Intranet IP of the target group instance.
        """
        return pulumi.get(self, "bind_ip")

    @bind_ip.setter
    def bind_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bind_ip", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port of the target group instance.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="targetGroupId")
    def target_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Target group ID.
        """
        return pulumi.get(self, "target_group_id")

    @target_group_id.setter
    def target_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_group_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        The weight of the target group instance.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class TargetGroupInstanceAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bind_ip: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 target_group_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a resource to create a CLB target group instance attachment.

        ## Import

        CLB target group instance attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Clb/targetGroupInstanceAttachment:TargetGroupInstanceAttachment test lbtg-3k3io0i0#172.16.48.18#222
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bind_ip: The Intranet IP of the target group instance.
        :param pulumi.Input[int] port: Port of the target group instance.
        :param pulumi.Input[str] target_group_id: Target group ID.
        :param pulumi.Input[int] weight: The weight of the target group instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TargetGroupInstanceAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a CLB target group instance attachment.

        ## Import

        CLB target group instance attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Clb/targetGroupInstanceAttachment:TargetGroupInstanceAttachment test lbtg-3k3io0i0#172.16.48.18#222
        ```

        :param str resource_name: The name of the resource.
        :param TargetGroupInstanceAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TargetGroupInstanceAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bind_ip: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 target_group_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
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
            __props__ = TargetGroupInstanceAttachmentArgs.__new__(TargetGroupInstanceAttachmentArgs)

            if bind_ip is None and not opts.urn:
                raise TypeError("Missing required property 'bind_ip'")
            __props__.__dict__["bind_ip"] = bind_ip
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            if target_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_group_id'")
            __props__.__dict__["target_group_id"] = target_group_id
            if weight is None and not opts.urn:
                raise TypeError("Missing required property 'weight'")
            __props__.__dict__["weight"] = weight
        super(TargetGroupInstanceAttachment, __self__).__init__(
            'tencentcloud:Clb/targetGroupInstanceAttachment:TargetGroupInstanceAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bind_ip: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            target_group_id: Optional[pulumi.Input[str]] = None,
            weight: Optional[pulumi.Input[int]] = None) -> 'TargetGroupInstanceAttachment':
        """
        Get an existing TargetGroupInstanceAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bind_ip: The Intranet IP of the target group instance.
        :param pulumi.Input[int] port: Port of the target group instance.
        :param pulumi.Input[str] target_group_id: Target group ID.
        :param pulumi.Input[int] weight: The weight of the target group instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TargetGroupInstanceAttachmentState.__new__(_TargetGroupInstanceAttachmentState)

        __props__.__dict__["bind_ip"] = bind_ip
        __props__.__dict__["port"] = port
        __props__.__dict__["target_group_id"] = target_group_id
        __props__.__dict__["weight"] = weight
        return TargetGroupInstanceAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bindIp")
    def bind_ip(self) -> pulumi.Output[str]:
        """
        The Intranet IP of the target group instance.
        """
        return pulumi.get(self, "bind_ip")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Port of the target group instance.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="targetGroupId")
    def target_group_id(self) -> pulumi.Output[str]:
        """
        Target group ID.
        """
        return pulumi.get(self, "target_group_id")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[int]:
        """
        The weight of the target group instance.
        """
        return pulumi.get(self, "weight")

