# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ScalingConfigDataDiskArgs',
    'ScalingConfigInstanceNameSettingsArgs',
    'ScalingGroupForwardBalancerIdArgs',
    'ScalingGroupForwardBalancerIdTargetAttributeArgs',
]

@pulumi.input_type
class ScalingConfigDataDiskArgs:
    def __init__(__self__, *,
                 delete_with_instance: Optional[pulumi.Input[bool]] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 disk_type: Optional[pulumi.Input[str]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None):
        if delete_with_instance is not None:
            pulumi.set(__self__, "delete_with_instance", delete_with_instance)
        if disk_size is not None:
            pulumi.set(__self__, "disk_size", disk_size)
        if disk_type is not None:
            pulumi.set(__self__, "disk_type", disk_type)
        if snapshot_id is not None:
            pulumi.set(__self__, "snapshot_id", snapshot_id)

    @property
    @pulumi.getter(name="deleteWithInstance")
    def delete_with_instance(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_with_instance")

    @delete_with_instance.setter
    def delete_with_instance(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_with_instance", value)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "disk_size")

    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_size", value)

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "disk_type")

    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_type", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_id", value)


@pulumi.input_type
class ScalingConfigInstanceNameSettingsArgs:
    def __init__(__self__, *,
                 instance_name: pulumi.Input[str],
                 instance_name_style: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "instance_name", instance_name)
        if instance_name_style is not None:
            pulumi.set(__self__, "instance_name_style", instance_name_style)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="instanceNameStyle")
    def instance_name_style(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_name_style")

    @instance_name_style.setter
    def instance_name_style(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name_style", value)


@pulumi.input_type
class ScalingGroupForwardBalancerIdArgs:
    def __init__(__self__, *,
                 listener_id: pulumi.Input[str],
                 load_balancer_id: pulumi.Input[str],
                 target_attributes: pulumi.Input[Sequence[pulumi.Input['ScalingGroupForwardBalancerIdTargetAttributeArgs']]],
                 rule_id: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "listener_id", listener_id)
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        pulumi.set(__self__, "target_attributes", target_attributes)
        if rule_id is not None:
            pulumi.set(__self__, "rule_id", rule_id)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "load_balancer_id")

    @load_balancer_id.setter
    def load_balancer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "load_balancer_id", value)

    @property
    @pulumi.getter(name="targetAttributes")
    def target_attributes(self) -> pulumi.Input[Sequence[pulumi.Input['ScalingGroupForwardBalancerIdTargetAttributeArgs']]]:
        return pulumi.get(self, "target_attributes")

    @target_attributes.setter
    def target_attributes(self, value: pulumi.Input[Sequence[pulumi.Input['ScalingGroupForwardBalancerIdTargetAttributeArgs']]]):
        pulumi.set(self, "target_attributes", value)

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rule_id")

    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_id", value)


@pulumi.input_type
class ScalingGroupForwardBalancerIdTargetAttributeArgs:
    def __init__(__self__, *,
                 port: pulumi.Input[int],
                 weight: pulumi.Input[int]):
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Input[int]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: pulumi.Input[int]):
        pulumi.set(self, "weight", value)


