# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstancesReservedInstanceListResult',
]

@pulumi.output_type
class InstancesReservedInstanceListResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 end_time: str,
                 instance_count: int,
                 instance_type: str,
                 reserved_instance_id: str,
                 start_time: str,
                 status: str):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "instance_count", instance_count)
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "reserved_instance_id", reserved_instance_id)
        pulumi.set(__self__, "start_time", start_time)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> int:
        return pulumi.get(self, "instance_count")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="reservedInstanceId")
    def reserved_instance_id(self) -> str:
        return pulumi.get(self, "reserved_instance_id")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")


