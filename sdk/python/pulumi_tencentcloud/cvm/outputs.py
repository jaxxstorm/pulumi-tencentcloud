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
    'ImagesImageResult',
    'ImagesImageSnapshotResult',
    'InstanceDataDisk',
    'InstancesTypesFilterResult',
    'InstancesTypesInstanceTypeResult',
    'ReservedInstanceConfigsConfigListResult',
]

@pulumi.output_type
class ImagesImageResult(dict):
    def __init__(__self__, *,
                 architecture: str,
                 created_time: str,
                 image_creator: str,
                 image_description: str,
                 image_id: str,
                 image_name: str,
                 image_size: int,
                 image_source: str,
                 image_state: str,
                 image_type: str,
                 os_name: str,
                 platform: str,
                 snapshots: Sequence['outputs.ImagesImageSnapshotResult'],
                 support_cloud_init: bool,
                 sync_percent: int):
        pulumi.set(__self__, "architecture", architecture)
        pulumi.set(__self__, "created_time", created_time)
        pulumi.set(__self__, "image_creator", image_creator)
        pulumi.set(__self__, "image_description", image_description)
        pulumi.set(__self__, "image_id", image_id)
        pulumi.set(__self__, "image_name", image_name)
        pulumi.set(__self__, "image_size", image_size)
        pulumi.set(__self__, "image_source", image_source)
        pulumi.set(__self__, "image_state", image_state)
        pulumi.set(__self__, "image_type", image_type)
        pulumi.set(__self__, "os_name", os_name)
        pulumi.set(__self__, "platform", platform)
        pulumi.set(__self__, "snapshots", snapshots)
        pulumi.set(__self__, "support_cloud_init", support_cloud_init)
        pulumi.set(__self__, "sync_percent", sync_percent)

    @property
    @pulumi.getter
    def architecture(self) -> str:
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="imageCreator")
    def image_creator(self) -> str:
        return pulumi.get(self, "image_creator")

    @property
    @pulumi.getter(name="imageDescription")
    def image_description(self) -> str:
        return pulumi.get(self, "image_description")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> str:
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="imageSize")
    def image_size(self) -> int:
        return pulumi.get(self, "image_size")

    @property
    @pulumi.getter(name="imageSource")
    def image_source(self) -> str:
        return pulumi.get(self, "image_source")

    @property
    @pulumi.getter(name="imageState")
    def image_state(self) -> str:
        return pulumi.get(self, "image_state")

    @property
    @pulumi.getter(name="imageType")
    def image_type(self) -> str:
        return pulumi.get(self, "image_type")

    @property
    @pulumi.getter(name="osName")
    def os_name(self) -> str:
        return pulumi.get(self, "os_name")

    @property
    @pulumi.getter
    def platform(self) -> str:
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter
    def snapshots(self) -> Sequence['outputs.ImagesImageSnapshotResult']:
        return pulumi.get(self, "snapshots")

    @property
    @pulumi.getter(name="supportCloudInit")
    def support_cloud_init(self) -> bool:
        return pulumi.get(self, "support_cloud_init")

    @property
    @pulumi.getter(name="syncPercent")
    def sync_percent(self) -> int:
        return pulumi.get(self, "sync_percent")


@pulumi.output_type
class ImagesImageSnapshotResult(dict):
    def __init__(__self__, *,
                 disk_size: int,
                 disk_usage: str,
                 snapshot_id: str,
                 snapshot_name: str):
        pulumi.set(__self__, "disk_size", disk_size)
        pulumi.set(__self__, "disk_usage", disk_usage)
        pulumi.set(__self__, "snapshot_id", snapshot_id)
        pulumi.set(__self__, "snapshot_name", snapshot_name)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> int:
        return pulumi.get(self, "disk_size")

    @property
    @pulumi.getter(name="diskUsage")
    def disk_usage(self) -> str:
        return pulumi.get(self, "disk_usage")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> str:
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> str:
        return pulumi.get(self, "snapshot_name")


@pulumi.output_type
class InstanceDataDisk(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataDiskSize":
            suggest = "data_disk_size"
        elif key == "dataDiskType":
            suggest = "data_disk_type"
        elif key == "dataDiskId":
            suggest = "data_disk_id"
        elif key == "dataDiskSnapshotId":
            suggest = "data_disk_snapshot_id"
        elif key == "deleteWithInstance":
            suggest = "delete_with_instance"
        elif key == "throughputPerformance":
            suggest = "throughput_performance"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceDataDisk. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceDataDisk.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceDataDisk.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_disk_size: int,
                 data_disk_type: str,
                 data_disk_id: Optional[str] = None,
                 data_disk_snapshot_id: Optional[str] = None,
                 delete_with_instance: Optional[bool] = None,
                 encrypt: Optional[bool] = None,
                 throughput_performance: Optional[int] = None):
        pulumi.set(__self__, "data_disk_size", data_disk_size)
        pulumi.set(__self__, "data_disk_type", data_disk_type)
        if data_disk_id is not None:
            pulumi.set(__self__, "data_disk_id", data_disk_id)
        if data_disk_snapshot_id is not None:
            pulumi.set(__self__, "data_disk_snapshot_id", data_disk_snapshot_id)
        if delete_with_instance is not None:
            pulumi.set(__self__, "delete_with_instance", delete_with_instance)
        if encrypt is not None:
            pulumi.set(__self__, "encrypt", encrypt)
        if throughput_performance is not None:
            pulumi.set(__self__, "throughput_performance", throughput_performance)

    @property
    @pulumi.getter(name="dataDiskSize")
    def data_disk_size(self) -> int:
        return pulumi.get(self, "data_disk_size")

    @property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> str:
        return pulumi.get(self, "data_disk_type")

    @property
    @pulumi.getter(name="dataDiskId")
    def data_disk_id(self) -> Optional[str]:
        return pulumi.get(self, "data_disk_id")

    @property
    @pulumi.getter(name="dataDiskSnapshotId")
    def data_disk_snapshot_id(self) -> Optional[str]:
        return pulumi.get(self, "data_disk_snapshot_id")

    @property
    @pulumi.getter(name="deleteWithInstance")
    def delete_with_instance(self) -> Optional[bool]:
        return pulumi.get(self, "delete_with_instance")

    @property
    @pulumi.getter
    def encrypt(self) -> Optional[bool]:
        return pulumi.get(self, "encrypt")

    @property
    @pulumi.getter(name="throughputPerformance")
    def throughput_performance(self) -> Optional[int]:
        return pulumi.get(self, "throughput_performance")


@pulumi.output_type
class InstancesTypesFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class InstancesTypesInstanceTypeResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 cpu_core_count: int,
                 family: str,
                 gpu_core_count: int,
                 instance_charge_type: str,
                 instance_type: str,
                 memory_size: int,
                 status: str):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "cpu_core_count", cpu_core_count)
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "gpu_core_count", gpu_core_count)
        pulumi.set(__self__, "instance_charge_type", instance_charge_type)
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "memory_size", memory_size)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> int:
        return pulumi.get(self, "cpu_core_count")

    @property
    @pulumi.getter
    def family(self) -> str:
        return pulumi.get(self, "family")

    @property
    @pulumi.getter(name="gpuCoreCount")
    def gpu_core_count(self) -> int:
        return pulumi.get(self, "gpu_core_count")

    @property
    @pulumi.getter(name="instanceChargeType")
    def instance_charge_type(self) -> str:
        return pulumi.get(self, "instance_charge_type")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> int:
        return pulumi.get(self, "memory_size")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")


@pulumi.output_type
class ReservedInstanceConfigsConfigListResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 config_id: str,
                 currency_code: str,
                 duration: int,
                 instance_type: str,
                 offering_type: str,
                 platform: str,
                 price: float,
                 usage_price: float):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "config_id", config_id)
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "offering_type", offering_type)
        pulumi.set(__self__, "platform", platform)
        pulumi.set(__self__, "price", price)
        pulumi.set(__self__, "usage_price", usage_price)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> str:
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def duration(self) -> int:
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> str:
        return pulumi.get(self, "offering_type")

    @property
    @pulumi.getter
    def platform(self) -> str:
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter
    def price(self) -> float:
        return pulumi.get(self, "price")

    @property
    @pulumi.getter(name="usagePrice")
    def usage_price(self) -> float:
        return pulumi.get(self, "usage_price")


