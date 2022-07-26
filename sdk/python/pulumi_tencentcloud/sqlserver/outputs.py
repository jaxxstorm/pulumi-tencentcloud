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
    'AccountDBAttachmentsListResult',
    'AccountsListResult',
    'BackupsListResult',
    'BasicInstancesInstanceListResult',
    'DBsDbListResult',
    'InstancesInstanceListResult',
    'PublishSubscribeDatabaseTuple',
    'PublishSubscribesPublishSubscribeListResult',
    'PublishSubscribesPublishSubscribeListDatabaseTupleResult',
    'ReadonlyGroupsListResult',
    'ZoneConfigZoneListResult',
    'ZoneConfigZoneListSpecinfoListResult',
]

@pulumi.output_type
class AccountDBAttachmentsListResult(dict):
    def __init__(__self__, *,
                 account_name: str,
                 db_name: str,
                 instance_id: str,
                 privilege: str):
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "db_name", db_name)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "privilege", privilege)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> str:
        return pulumi.get(self, "db_name")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def privilege(self) -> str:
        return pulumi.get(self, "privilege")


@pulumi.output_type
class AccountsListResult(dict):
    def __init__(__self__, *,
                 create_time: str,
                 instance_id: str,
                 name: str,
                 remark: str,
                 status: int,
                 update_time: str):
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "remark", remark)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def remark(self) -> str:
        return pulumi.get(self, "remark")

    @property
    @pulumi.getter
    def status(self) -> int:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        return pulumi.get(self, "update_time")


@pulumi.output_type
class BackupsListResult(dict):
    def __init__(__self__, *,
                 db_lists: Sequence[str],
                 end_time: str,
                 file_name: str,
                 id: str,
                 instance_id: str,
                 internet_url: str,
                 intranet_url: str,
                 size: int,
                 start_time: str,
                 status: int,
                 strategy: int,
                 trigger_model: int):
        pulumi.set(__self__, "db_lists", db_lists)
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "file_name", file_name)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "internet_url", internet_url)
        pulumi.set(__self__, "intranet_url", intranet_url)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "start_time", start_time)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "strategy", strategy)
        pulumi.set(__self__, "trigger_model", trigger_model)

    @property
    @pulumi.getter(name="dbLists")
    def db_lists(self) -> Sequence[str]:
        return pulumi.get(self, "db_lists")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> str:
        return pulumi.get(self, "file_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="internetUrl")
    def internet_url(self) -> str:
        return pulumi.get(self, "internet_url")

    @property
    @pulumi.getter(name="intranetUrl")
    def intranet_url(self) -> str:
        return pulumi.get(self, "intranet_url")

    @property
    @pulumi.getter
    def size(self) -> int:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def status(self) -> int:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def strategy(self) -> int:
        return pulumi.get(self, "strategy")

    @property
    @pulumi.getter(name="triggerModel")
    def trigger_model(self) -> int:
        return pulumi.get(self, "trigger_model")


@pulumi.output_type
class BasicInstancesInstanceListResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 charge_type: str,
                 cpu: int,
                 create_time: str,
                 engine_version: str,
                 id: str,
                 memory: int,
                 name: str,
                 project_id: int,
                 status: int,
                 storage: int,
                 subnet_id: str,
                 tags: Mapping[str, Any],
                 used_storage: int,
                 vip: str,
                 vpc_id: str,
                 vport: int):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "engine_version", engine_version)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "memory", memory)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "storage", storage)
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "used_storage", used_storage)
        pulumi.set(__self__, "vip", vip)
        pulumi.set(__self__, "vpc_id", vpc_id)
        pulumi.set(__self__, "vport", vport)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter
    def cpu(self) -> int:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def memory(self) -> int:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> int:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def status(self) -> int:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def storage(self) -> int:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="usedStorage")
    def used_storage(self) -> int:
        return pulumi.get(self, "used_storage")

    @property
    @pulumi.getter
    def vip(self) -> str:
        return pulumi.get(self, "vip")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter
    def vport(self) -> int:
        return pulumi.get(self, "vport")


@pulumi.output_type
class DBsDbListResult(dict):
    def __init__(__self__, *,
                 charset: str,
                 create_time: str,
                 instance_id: str,
                 name: str,
                 remark: str,
                 status: str):
        pulumi.set(__self__, "charset", charset)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "remark", remark)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def charset(self) -> str:
        return pulumi.get(self, "charset")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def remark(self) -> str:
        return pulumi.get(self, "remark")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")


@pulumi.output_type
class InstancesInstanceListResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 charge_type: str,
                 create_time: str,
                 engine_version: str,
                 ha_type: str,
                 id: str,
                 memory: int,
                 name: str,
                 project_id: int,
                 ro_flag: str,
                 status: int,
                 storage: int,
                 subnet_id: str,
                 tags: Mapping[str, Any],
                 used_storage: int,
                 vip: str,
                 vpc_id: str,
                 vport: int):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "engine_version", engine_version)
        pulumi.set(__self__, "ha_type", ha_type)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "memory", memory)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "ro_flag", ro_flag)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "storage", storage)
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "used_storage", used_storage)
        pulumi.set(__self__, "vip", vip)
        pulumi.set(__self__, "vpc_id", vpc_id)
        pulumi.set(__self__, "vport", vport)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="haType")
    def ha_type(self) -> str:
        return pulumi.get(self, "ha_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def memory(self) -> int:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> int:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="roFlag")
    def ro_flag(self) -> str:
        return pulumi.get(self, "ro_flag")

    @property
    @pulumi.getter
    def status(self) -> int:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def storage(self) -> int:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="usedStorage")
    def used_storage(self) -> int:
        return pulumi.get(self, "used_storage")

    @property
    @pulumi.getter
    def vip(self) -> str:
        return pulumi.get(self, "vip")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter
    def vport(self) -> int:
        return pulumi.get(self, "vport")


@pulumi.output_type
class PublishSubscribeDatabaseTuple(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "publishDatabase":
            suggest = "publish_database"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PublishSubscribeDatabaseTuple. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PublishSubscribeDatabaseTuple.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PublishSubscribeDatabaseTuple.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 publish_database: str):
        pulumi.set(__self__, "publish_database", publish_database)

    @property
    @pulumi.getter(name="publishDatabase")
    def publish_database(self) -> str:
        return pulumi.get(self, "publish_database")


@pulumi.output_type
class PublishSubscribesPublishSubscribeListResult(dict):
    def __init__(__self__, *,
                 database_tuples: Sequence['outputs.PublishSubscribesPublishSubscribeListDatabaseTupleResult'],
                 publish_instance_id: str,
                 publish_instance_ip: str,
                 publish_instance_name: str,
                 publish_subscribe_id: int,
                 publish_subscribe_name: str,
                 subscribe_instance_id: str,
                 subscribe_instance_ip: str,
                 subscribe_instance_name: str):
        pulumi.set(__self__, "database_tuples", database_tuples)
        pulumi.set(__self__, "publish_instance_id", publish_instance_id)
        pulumi.set(__self__, "publish_instance_ip", publish_instance_ip)
        pulumi.set(__self__, "publish_instance_name", publish_instance_name)
        pulumi.set(__self__, "publish_subscribe_id", publish_subscribe_id)
        pulumi.set(__self__, "publish_subscribe_name", publish_subscribe_name)
        pulumi.set(__self__, "subscribe_instance_id", subscribe_instance_id)
        pulumi.set(__self__, "subscribe_instance_ip", subscribe_instance_ip)
        pulumi.set(__self__, "subscribe_instance_name", subscribe_instance_name)

    @property
    @pulumi.getter(name="databaseTuples")
    def database_tuples(self) -> Sequence['outputs.PublishSubscribesPublishSubscribeListDatabaseTupleResult']:
        return pulumi.get(self, "database_tuples")

    @property
    @pulumi.getter(name="publishInstanceId")
    def publish_instance_id(self) -> str:
        return pulumi.get(self, "publish_instance_id")

    @property
    @pulumi.getter(name="publishInstanceIp")
    def publish_instance_ip(self) -> str:
        return pulumi.get(self, "publish_instance_ip")

    @property
    @pulumi.getter(name="publishInstanceName")
    def publish_instance_name(self) -> str:
        return pulumi.get(self, "publish_instance_name")

    @property
    @pulumi.getter(name="publishSubscribeId")
    def publish_subscribe_id(self) -> int:
        return pulumi.get(self, "publish_subscribe_id")

    @property
    @pulumi.getter(name="publishSubscribeName")
    def publish_subscribe_name(self) -> str:
        return pulumi.get(self, "publish_subscribe_name")

    @property
    @pulumi.getter(name="subscribeInstanceId")
    def subscribe_instance_id(self) -> str:
        return pulumi.get(self, "subscribe_instance_id")

    @property
    @pulumi.getter(name="subscribeInstanceIp")
    def subscribe_instance_ip(self) -> str:
        return pulumi.get(self, "subscribe_instance_ip")

    @property
    @pulumi.getter(name="subscribeInstanceName")
    def subscribe_instance_name(self) -> str:
        return pulumi.get(self, "subscribe_instance_name")


@pulumi.output_type
class PublishSubscribesPublishSubscribeListDatabaseTupleResult(dict):
    def __init__(__self__, *,
                 last_sync_time: str,
                 publish_database: str,
                 status: str,
                 subscribe_database: str):
        pulumi.set(__self__, "last_sync_time", last_sync_time)
        pulumi.set(__self__, "publish_database", publish_database)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "subscribe_database", subscribe_database)

    @property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> str:
        return pulumi.get(self, "last_sync_time")

    @property
    @pulumi.getter(name="publishDatabase")
    def publish_database(self) -> str:
        return pulumi.get(self, "publish_database")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscribeDatabase")
    def subscribe_database(self) -> str:
        return pulumi.get(self, "subscribe_database")


@pulumi.output_type
class ReadonlyGroupsListResult(dict):
    def __init__(__self__, *,
                 id: str,
                 is_offline_delay: int,
                 master_instance_id: str,
                 max_delay_time: int,
                 min_instances: int,
                 name: str,
                 readonly_instance_sets: Sequence[str],
                 status: int,
                 vip: str,
                 vport: int):
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "is_offline_delay", is_offline_delay)
        pulumi.set(__self__, "master_instance_id", master_instance_id)
        pulumi.set(__self__, "max_delay_time", max_delay_time)
        pulumi.set(__self__, "min_instances", min_instances)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "readonly_instance_sets", readonly_instance_sets)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "vip", vip)
        pulumi.set(__self__, "vport", vport)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isOfflineDelay")
    def is_offline_delay(self) -> int:
        return pulumi.get(self, "is_offline_delay")

    @property
    @pulumi.getter(name="masterInstanceId")
    def master_instance_id(self) -> str:
        return pulumi.get(self, "master_instance_id")

    @property
    @pulumi.getter(name="maxDelayTime")
    def max_delay_time(self) -> int:
        return pulumi.get(self, "max_delay_time")

    @property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> int:
        return pulumi.get(self, "min_instances")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="readonlyInstanceSets")
    def readonly_instance_sets(self) -> Sequence[str]:
        return pulumi.get(self, "readonly_instance_sets")

    @property
    @pulumi.getter
    def status(self) -> int:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def vip(self) -> str:
        return pulumi.get(self, "vip")

    @property
    @pulumi.getter
    def vport(self) -> int:
        return pulumi.get(self, "vport")


@pulumi.output_type
class ZoneConfigZoneListResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 specinfo_lists: Sequence['outputs.ZoneConfigZoneListSpecinfoListResult'],
                 zone_id: int):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "specinfo_lists", specinfo_lists)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="specinfoLists")
    def specinfo_lists(self) -> Sequence['outputs.ZoneConfigZoneListSpecinfoListResult']:
        return pulumi.get(self, "specinfo_lists")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> int:
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class ZoneConfigZoneListSpecinfoListResult(dict):
    def __init__(__self__, *,
                 charge_type: str,
                 cpu: int,
                 db_version: str,
                 db_version_name: str,
                 machine_type: str,
                 max_storage_size: int,
                 memory: int,
                 min_storage_size: int,
                 qps: int,
                 spec_id: int):
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "db_version", db_version)
        pulumi.set(__self__, "db_version_name", db_version_name)
        pulumi.set(__self__, "machine_type", machine_type)
        pulumi.set(__self__, "max_storage_size", max_storage_size)
        pulumi.set(__self__, "memory", memory)
        pulumi.set(__self__, "min_storage_size", min_storage_size)
        pulumi.set(__self__, "qps", qps)
        pulumi.set(__self__, "spec_id", spec_id)

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter
    def cpu(self) -> int:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> str:
        return pulumi.get(self, "db_version")

    @property
    @pulumi.getter(name="dbVersionName")
    def db_version_name(self) -> str:
        return pulumi.get(self, "db_version_name")

    @property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> str:
        return pulumi.get(self, "machine_type")

    @property
    @pulumi.getter(name="maxStorageSize")
    def max_storage_size(self) -> int:
        return pulumi.get(self, "max_storage_size")

    @property
    @pulumi.getter
    def memory(self) -> int:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter(name="minStorageSize")
    def min_storage_size(self) -> int:
        return pulumi.get(self, "min_storage_size")

    @property
    @pulumi.getter
    def qps(self) -> int:
        return pulumi.get(self, "qps")

    @property
    @pulumi.getter(name="specId")
    def spec_id(self) -> int:
        return pulumi.get(self, "spec_id")


