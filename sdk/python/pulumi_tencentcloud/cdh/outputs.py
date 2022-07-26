# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'InstanceHostResource',
    'InstancesCdhInstanceListResult',
    'InstancesCdhInstanceListHostResourceResult',
]

@pulumi.output_type
class InstanceHostResource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cpuAvailableNum":
            suggest = "cpu_available_num"
        elif key == "cpuTotalNum":
            suggest = "cpu_total_num"
        elif key == "diskAvailableSize":
            suggest = "disk_available_size"
        elif key == "diskTotalSize":
            suggest = "disk_total_size"
        elif key == "diskType":
            suggest = "disk_type"
        elif key == "memoryAvailableSize":
            suggest = "memory_available_size"
        elif key == "memoryTotalSize":
            suggest = "memory_total_size"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceHostResource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceHostResource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceHostResource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cpu_available_num: Optional[int] = None,
                 cpu_total_num: Optional[int] = None,
                 disk_available_size: Optional[int] = None,
                 disk_total_size: Optional[int] = None,
                 disk_type: Optional[str] = None,
                 memory_available_size: Optional[float] = None,
                 memory_total_size: Optional[float] = None):
        if cpu_available_num is not None:
            pulumi.set(__self__, "cpu_available_num", cpu_available_num)
        if cpu_total_num is not None:
            pulumi.set(__self__, "cpu_total_num", cpu_total_num)
        if disk_available_size is not None:
            pulumi.set(__self__, "disk_available_size", disk_available_size)
        if disk_total_size is not None:
            pulumi.set(__self__, "disk_total_size", disk_total_size)
        if disk_type is not None:
            pulumi.set(__self__, "disk_type", disk_type)
        if memory_available_size is not None:
            pulumi.set(__self__, "memory_available_size", memory_available_size)
        if memory_total_size is not None:
            pulumi.set(__self__, "memory_total_size", memory_total_size)

    @property
    @pulumi.getter(name="cpuAvailableNum")
    def cpu_available_num(self) -> Optional[int]:
        return pulumi.get(self, "cpu_available_num")

    @property
    @pulumi.getter(name="cpuTotalNum")
    def cpu_total_num(self) -> Optional[int]:
        return pulumi.get(self, "cpu_total_num")

    @property
    @pulumi.getter(name="diskAvailableSize")
    def disk_available_size(self) -> Optional[int]:
        return pulumi.get(self, "disk_available_size")

    @property
    @pulumi.getter(name="diskTotalSize")
    def disk_total_size(self) -> Optional[int]:
        return pulumi.get(self, "disk_total_size")

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[str]:
        return pulumi.get(self, "disk_type")

    @property
    @pulumi.getter(name="memoryAvailableSize")
    def memory_available_size(self) -> Optional[float]:
        return pulumi.get(self, "memory_available_size")

    @property
    @pulumi.getter(name="memoryTotalSize")
    def memory_total_size(self) -> Optional[float]:
        return pulumi.get(self, "memory_total_size")


@pulumi.output_type
class InstancesCdhInstanceListResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 cage_id: str,
                 charge_type: str,
                 create_time: str,
                 cvm_instance_ids: Sequence[str],
                 expired_time: str,
                 host_id: str,
                 host_name: str,
                 host_resources: Sequence['outputs.InstancesCdhInstanceListHostResourceResult'],
                 host_state: str,
                 host_type: str,
                 prepaid_renew_flag: str,
                 project_id: int):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "cage_id", cage_id)
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "cvm_instance_ids", cvm_instance_ids)
        pulumi.set(__self__, "expired_time", expired_time)
        pulumi.set(__self__, "host_id", host_id)
        pulumi.set(__self__, "host_name", host_name)
        pulumi.set(__self__, "host_resources", host_resources)
        pulumi.set(__self__, "host_state", host_state)
        pulumi.set(__self__, "host_type", host_type)
        pulumi.set(__self__, "prepaid_renew_flag", prepaid_renew_flag)
        pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="cageId")
    def cage_id(self) -> str:
        return pulumi.get(self, "cage_id")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="cvmInstanceIds")
    def cvm_instance_ids(self) -> Sequence[str]:
        return pulumi.get(self, "cvm_instance_ids")

    @property
    @pulumi.getter(name="expiredTime")
    def expired_time(self) -> str:
        return pulumi.get(self, "expired_time")

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> str:
        return pulumi.get(self, "host_id")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="hostResources")
    def host_resources(self) -> Sequence['outputs.InstancesCdhInstanceListHostResourceResult']:
        return pulumi.get(self, "host_resources")

    @property
    @pulumi.getter(name="hostState")
    def host_state(self) -> str:
        return pulumi.get(self, "host_state")

    @property
    @pulumi.getter(name="hostType")
    def host_type(self) -> str:
        return pulumi.get(self, "host_type")

    @property
    @pulumi.getter(name="prepaidRenewFlag")
    def prepaid_renew_flag(self) -> str:
        return pulumi.get(self, "prepaid_renew_flag")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> int:
        return pulumi.get(self, "project_id")


@pulumi.output_type
class InstancesCdhInstanceListHostResourceResult(dict):
    def __init__(__self__, *,
                 cpu_available_num: int,
                 cpu_total_num: int,
                 disk_available_size: int,
                 disk_total_size: int,
                 disk_type: str,
                 memory_available_size: float,
                 memory_total_size: float):
        pulumi.set(__self__, "cpu_available_num", cpu_available_num)
        pulumi.set(__self__, "cpu_total_num", cpu_total_num)
        pulumi.set(__self__, "disk_available_size", disk_available_size)
        pulumi.set(__self__, "disk_total_size", disk_total_size)
        pulumi.set(__self__, "disk_type", disk_type)
        pulumi.set(__self__, "memory_available_size", memory_available_size)
        pulumi.set(__self__, "memory_total_size", memory_total_size)

    @property
    @pulumi.getter(name="cpuAvailableNum")
    def cpu_available_num(self) -> int:
        return pulumi.get(self, "cpu_available_num")

    @property
    @pulumi.getter(name="cpuTotalNum")
    def cpu_total_num(self) -> int:
        return pulumi.get(self, "cpu_total_num")

    @property
    @pulumi.getter(name="diskAvailableSize")
    def disk_available_size(self) -> int:
        return pulumi.get(self, "disk_available_size")

    @property
    @pulumi.getter(name="diskTotalSize")
    def disk_total_size(self) -> int:
        return pulumi.get(self, "disk_total_size")

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> str:
        return pulumi.get(self, "disk_type")

    @property
    @pulumi.getter(name="memoryAvailableSize")
    def memory_available_size(self) -> float:
        return pulumi.get(self, "memory_available_size")

    @property
    @pulumi.getter(name="memoryTotalSize")
    def memory_total_size(self) -> float:
        return pulumi.get(self, "memory_total_size")


