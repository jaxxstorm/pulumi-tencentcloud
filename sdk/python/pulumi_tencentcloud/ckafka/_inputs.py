# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceConfigArgs',
    'InstanceDynamicRetentionConfigArgs',
    'InstanceTagArgs',
    'GetInstancesFilterArgs',
]

@pulumi.input_type
class InstanceConfigArgs:
    def __init__(__self__, *,
                 auto_create_topic_enable: pulumi.Input[bool],
                 default_num_partitions: pulumi.Input[int],
                 default_replication_factor: pulumi.Input[int]):
        """
        :param pulumi.Input[bool] auto_create_topic_enable: Automatic creation. true: enabled, false: not enabled.
        :param pulumi.Input[int] default_num_partitions: If auto.create.topic.enable is set to true and this value is not set, 3 will be used by default.
        :param pulumi.Input[int] default_replication_factor: If auto.create.topic.enable is set to true but this value is not set, 2 will be used by default.
        """
        pulumi.set(__self__, "auto_create_topic_enable", auto_create_topic_enable)
        pulumi.set(__self__, "default_num_partitions", default_num_partitions)
        pulumi.set(__self__, "default_replication_factor", default_replication_factor)

    @property
    @pulumi.getter(name="autoCreateTopicEnable")
    def auto_create_topic_enable(self) -> pulumi.Input[bool]:
        """
        Automatic creation. true: enabled, false: not enabled.
        """
        return pulumi.get(self, "auto_create_topic_enable")

    @auto_create_topic_enable.setter
    def auto_create_topic_enable(self, value: pulumi.Input[bool]):
        pulumi.set(self, "auto_create_topic_enable", value)

    @property
    @pulumi.getter(name="defaultNumPartitions")
    def default_num_partitions(self) -> pulumi.Input[int]:
        """
        If auto.create.topic.enable is set to true and this value is not set, 3 will be used by default.
        """
        return pulumi.get(self, "default_num_partitions")

    @default_num_partitions.setter
    def default_num_partitions(self, value: pulumi.Input[int]):
        pulumi.set(self, "default_num_partitions", value)

    @property
    @pulumi.getter(name="defaultReplicationFactor")
    def default_replication_factor(self) -> pulumi.Input[int]:
        """
        If auto.create.topic.enable is set to true but this value is not set, 2 will be used by default.
        """
        return pulumi.get(self, "default_replication_factor")

    @default_replication_factor.setter
    def default_replication_factor(self, value: pulumi.Input[int]):
        pulumi.set(self, "default_replication_factor", value)


@pulumi.input_type
class InstanceDynamicRetentionConfigArgs:
    def __init__(__self__, *,
                 bottom_retention: Optional[pulumi.Input[int]] = None,
                 disk_quota_percentage: Optional[pulumi.Input[int]] = None,
                 enable: Optional[pulumi.Input[int]] = None,
                 step_forward_percentage: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] bottom_retention: Minimum retention time, in minutes.
        :param pulumi.Input[int] disk_quota_percentage: Disk quota threshold (in percentage) for triggering the message retention time change event.
        :param pulumi.Input[int] enable: Whether the dynamic message retention time configuration is enabled. 0: disabled; 1: enabled.
        :param pulumi.Input[int] step_forward_percentage: Percentage by which the message retention time is shortened each time.
        """
        if bottom_retention is not None:
            pulumi.set(__self__, "bottom_retention", bottom_retention)
        if disk_quota_percentage is not None:
            pulumi.set(__self__, "disk_quota_percentage", disk_quota_percentage)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if step_forward_percentage is not None:
            pulumi.set(__self__, "step_forward_percentage", step_forward_percentage)

    @property
    @pulumi.getter(name="bottomRetention")
    def bottom_retention(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum retention time, in minutes.
        """
        return pulumi.get(self, "bottom_retention")

    @bottom_retention.setter
    def bottom_retention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bottom_retention", value)

    @property
    @pulumi.getter(name="diskQuotaPercentage")
    def disk_quota_percentage(self) -> Optional[pulumi.Input[int]]:
        """
        Disk quota threshold (in percentage) for triggering the message retention time change event.
        """
        return pulumi.get(self, "disk_quota_percentage")

    @disk_quota_percentage.setter
    def disk_quota_percentage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_quota_percentage", value)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[int]]:
        """
        Whether the dynamic message retention time configuration is enabled. 0: disabled; 1: enabled.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter(name="stepForwardPercentage")
    def step_forward_percentage(self) -> Optional[pulumi.Input[int]]:
        """
        Percentage by which the message retention time is shortened each time.
        """
        return pulumi.get(self, "step_forward_percentage")

    @step_forward_percentage.setter
    def step_forward_percentage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "step_forward_percentage", value)


@pulumi.input_type
class InstanceTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] key: Tag key.
        :param pulumi.Input[str] value: Tag value.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Tag key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Tag value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class GetInstancesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: The field that needs to be filtered.
        :param Sequence[str] values: The filtered value of the field.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The field that needs to be filtered.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        The filtered value of the field.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)


