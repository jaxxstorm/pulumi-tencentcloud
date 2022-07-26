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
    'ClusterCredentialAddressResult',
    'ClusterCredentialInternalLbResult',
    'ClusterCredentialPublicLbResult',
    'ClusterDnsServer',
    'ClusterInternalLb',
    'ClusterPublicLb',
    'ClustersListResult',
    'ClustersListDnsServerResult',
    'ContainerInstanceCbsVolume',
    'ContainerInstanceContainer',
    'ContainerInstanceContainerLivenessProbe',
    'ContainerInstanceContainerReadinessProbe',
    'ContainerInstanceContainerVolumeMount',
    'ContainerInstanceImageRegistryCredential',
    'ContainerInstanceInitContainer',
    'ContainerInstanceInitContainerVolumeMount',
    'ContainerInstanceNfsVolume',
]

@pulumi.output_type
class ClusterCredentialAddressResult(dict):
    def __init__(__self__, *,
                 ip: str,
                 port: str,
                 type: str):
        pulumi.set(__self__, "ip", ip)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def ip(self) -> str:
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def port(self) -> str:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class ClusterCredentialInternalLbResult(dict):
    def __init__(__self__, *,
                 enabled: bool,
                 subnet_id: str):
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class ClusterCredentialPublicLbResult(dict):
    def __init__(__self__, *,
                 allow_from_cidrs: Sequence[str],
                 enabled: bool,
                 extra_param: str,
                 security_group: str,
                 security_policies: Sequence[str]):
        pulumi.set(__self__, "allow_from_cidrs", allow_from_cidrs)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "extra_param", extra_param)
        pulumi.set(__self__, "security_group", security_group)
        pulumi.set(__self__, "security_policies", security_policies)

    @property
    @pulumi.getter(name="allowFromCidrs")
    def allow_from_cidrs(self) -> Sequence[str]:
        return pulumi.get(self, "allow_from_cidrs")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="extraParam")
    def extra_param(self) -> str:
        return pulumi.get(self, "extra_param")

    @property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> str:
        return pulumi.get(self, "security_group")

    @property
    @pulumi.getter(name="securityPolicies")
    def security_policies(self) -> Sequence[str]:
        return pulumi.get(self, "security_policies")


@pulumi.output_type
class ClusterDnsServer(dict):
    def __init__(__self__, *,
                 domain: Optional[str] = None,
                 servers: Optional[Sequence[str]] = None):
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if servers is not None:
            pulumi.set(__self__, "servers", servers)

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def servers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "servers")


@pulumi.output_type
class ClusterInternalLb(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterInternalLb. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterInternalLb.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterInternalLb.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 subnet_id: Optional[str] = None):
        pulumi.set(__self__, "enabled", enabled)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class ClusterPublicLb(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowFromCidrs":
            suggest = "allow_from_cidrs"
        elif key == "extraParam":
            suggest = "extra_param"
        elif key == "securityGroup":
            suggest = "security_group"
        elif key == "securityPolicies":
            suggest = "security_policies"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterPublicLb. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterPublicLb.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterPublicLb.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 allow_from_cidrs: Optional[Sequence[str]] = None,
                 extra_param: Optional[str] = None,
                 security_group: Optional[str] = None,
                 security_policies: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "enabled", enabled)
        if allow_from_cidrs is not None:
            pulumi.set(__self__, "allow_from_cidrs", allow_from_cidrs)
        if extra_param is not None:
            pulumi.set(__self__, "extra_param", extra_param)
        if security_group is not None:
            pulumi.set(__self__, "security_group", security_group)
        if security_policies is not None:
            pulumi.set(__self__, "security_policies", security_policies)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="allowFromCidrs")
    def allow_from_cidrs(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allow_from_cidrs")

    @property
    @pulumi.getter(name="extraParam")
    def extra_param(self) -> Optional[str]:
        return pulumi.get(self, "extra_param")

    @property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> Optional[str]:
        return pulumi.get(self, "security_group")

    @property
    @pulumi.getter(name="securityPolicies")
    def security_policies(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "security_policies")


@pulumi.output_type
class ClustersListResult(dict):
    def __init__(__self__, *,
                 cluster_desc: str,
                 cluster_id: str,
                 cluster_name: str,
                 created_time: str,
                 dns_servers: Sequence['outputs.ClustersListDnsServerResult'],
                 enable_vpc_core_dns: bool,
                 k8s_version: str,
                 need_delete_cbs: bool,
                 service_subnet_id: str,
                 status: str,
                 subnet_ids: Sequence[str],
                 tags: Mapping[str, Any],
                 vpc_id: str):
        pulumi.set(__self__, "cluster_desc", cluster_desc)
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "created_time", created_time)
        pulumi.set(__self__, "dns_servers", dns_servers)
        pulumi.set(__self__, "enable_vpc_core_dns", enable_vpc_core_dns)
        pulumi.set(__self__, "k8s_version", k8s_version)
        pulumi.set(__self__, "need_delete_cbs", need_delete_cbs)
        pulumi.set(__self__, "service_subnet_id", service_subnet_id)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="clusterDesc")
    def cluster_desc(self) -> str:
        return pulumi.get(self, "cluster_desc")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Sequence['outputs.ClustersListDnsServerResult']:
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter(name="enableVpcCoreDns")
    def enable_vpc_core_dns(self) -> bool:
        return pulumi.get(self, "enable_vpc_core_dns")

    @property
    @pulumi.getter(name="k8sVersion")
    def k8s_version(self) -> str:
        return pulumi.get(self, "k8s_version")

    @property
    @pulumi.getter(name="needDeleteCbs")
    def need_delete_cbs(self) -> bool:
        return pulumi.get(self, "need_delete_cbs")

    @property
    @pulumi.getter(name="serviceSubnetId")
    def service_subnet_id(self) -> str:
        return pulumi.get(self, "service_subnet_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class ClustersListDnsServerResult(dict):
    def __init__(__self__, *,
                 domain: str,
                 servers: Sequence[str]):
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "servers", servers)

    @property
    @pulumi.getter
    def domain(self) -> str:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def servers(self) -> Sequence[str]:
        return pulumi.get(self, "servers")


@pulumi.output_type
class ContainerInstanceCbsVolume(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "diskId":
            suggest = "disk_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceCbsVolume. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceCbsVolume.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceCbsVolume.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 disk_id: str,
                 name: str):
        pulumi.set(__self__, "disk_id", disk_id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> str:
        return pulumi.get(self, "disk_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class ContainerInstanceContainer(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "envVars":
            suggest = "env_vars"
        elif key == "livenessProbe":
            suggest = "liveness_probe"
        elif key == "readinessProbe":
            suggest = "readiness_probe"
        elif key == "volumeMounts":
            suggest = "volume_mounts"
        elif key == "workingDir":
            suggest = "working_dir"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceContainer. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceContainer.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceContainer.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 image: str,
                 name: str,
                 args: Optional[Sequence[str]] = None,
                 commands: Optional[Sequence[str]] = None,
                 cpu: Optional[float] = None,
                 env_vars: Optional[Mapping[str, Any]] = None,
                 liveness_probe: Optional['outputs.ContainerInstanceContainerLivenessProbe'] = None,
                 memory: Optional[float] = None,
                 readiness_probe: Optional['outputs.ContainerInstanceContainerReadinessProbe'] = None,
                 volume_mounts: Optional[Sequence['outputs.ContainerInstanceContainerVolumeMount']] = None,
                 working_dir: Optional[str] = None):
        pulumi.set(__self__, "image", image)
        pulumi.set(__self__, "name", name)
        if args is not None:
            pulumi.set(__self__, "args", args)
        if commands is not None:
            pulumi.set(__self__, "commands", commands)
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if env_vars is not None:
            pulumi.set(__self__, "env_vars", env_vars)
        if liveness_probe is not None:
            pulumi.set(__self__, "liveness_probe", liveness_probe)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if readiness_probe is not None:
            pulumi.set(__self__, "readiness_probe", readiness_probe)
        if volume_mounts is not None:
            pulumi.set(__self__, "volume_mounts", volume_mounts)
        if working_dir is not None:
            pulumi.set(__self__, "working_dir", working_dir)

    @property
    @pulumi.getter
    def image(self) -> str:
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def args(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "args")

    @property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "commands")

    @property
    @pulumi.getter
    def cpu(self) -> Optional[float]:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter(name="envVars")
    def env_vars(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "env_vars")

    @property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional['outputs.ContainerInstanceContainerLivenessProbe']:
        return pulumi.get(self, "liveness_probe")

    @property
    @pulumi.getter
    def memory(self) -> Optional[float]:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(self) -> Optional['outputs.ContainerInstanceContainerReadinessProbe']:
        return pulumi.get(self, "readiness_probe")

    @property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence['outputs.ContainerInstanceContainerVolumeMount']]:
        return pulumi.get(self, "volume_mounts")

    @property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[str]:
        return pulumi.get(self, "working_dir")


@pulumi.output_type
class ContainerInstanceContainerLivenessProbe(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "execCommands":
            suggest = "exec_commands"
        elif key == "failureThreshold":
            suggest = "failure_threshold"
        elif key == "httpGetPath":
            suggest = "http_get_path"
        elif key == "httpGetPort":
            suggest = "http_get_port"
        elif key == "httpGetScheme":
            suggest = "http_get_scheme"
        elif key == "initDelaySeconds":
            suggest = "init_delay_seconds"
        elif key == "periodSeconds":
            suggest = "period_seconds"
        elif key == "successThreshold":
            suggest = "success_threshold"
        elif key == "tcpSocketPort":
            suggest = "tcp_socket_port"
        elif key == "timeoutSeconds":
            suggest = "timeout_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceContainerLivenessProbe. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceContainerLivenessProbe.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceContainerLivenessProbe.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 exec_commands: Optional[Sequence[str]] = None,
                 failure_threshold: Optional[int] = None,
                 http_get_path: Optional[str] = None,
                 http_get_port: Optional[int] = None,
                 http_get_scheme: Optional[str] = None,
                 init_delay_seconds: Optional[int] = None,
                 period_seconds: Optional[int] = None,
                 success_threshold: Optional[int] = None,
                 tcp_socket_port: Optional[int] = None,
                 timeout_seconds: Optional[int] = None):
        if exec_commands is not None:
            pulumi.set(__self__, "exec_commands", exec_commands)
        if failure_threshold is not None:
            pulumi.set(__self__, "failure_threshold", failure_threshold)
        if http_get_path is not None:
            pulumi.set(__self__, "http_get_path", http_get_path)
        if http_get_port is not None:
            pulumi.set(__self__, "http_get_port", http_get_port)
        if http_get_scheme is not None:
            pulumi.set(__self__, "http_get_scheme", http_get_scheme)
        if init_delay_seconds is not None:
            pulumi.set(__self__, "init_delay_seconds", init_delay_seconds)
        if period_seconds is not None:
            pulumi.set(__self__, "period_seconds", period_seconds)
        if success_threshold is not None:
            pulumi.set(__self__, "success_threshold", success_threshold)
        if tcp_socket_port is not None:
            pulumi.set(__self__, "tcp_socket_port", tcp_socket_port)
        if timeout_seconds is not None:
            pulumi.set(__self__, "timeout_seconds", timeout_seconds)

    @property
    @pulumi.getter(name="execCommands")
    def exec_commands(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "exec_commands")

    @property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[int]:
        return pulumi.get(self, "failure_threshold")

    @property
    @pulumi.getter(name="httpGetPath")
    def http_get_path(self) -> Optional[str]:
        return pulumi.get(self, "http_get_path")

    @property
    @pulumi.getter(name="httpGetPort")
    def http_get_port(self) -> Optional[int]:
        return pulumi.get(self, "http_get_port")

    @property
    @pulumi.getter(name="httpGetScheme")
    def http_get_scheme(self) -> Optional[str]:
        return pulumi.get(self, "http_get_scheme")

    @property
    @pulumi.getter(name="initDelaySeconds")
    def init_delay_seconds(self) -> Optional[int]:
        return pulumi.get(self, "init_delay_seconds")

    @property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[int]:
        return pulumi.get(self, "period_seconds")

    @property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[int]:
        return pulumi.get(self, "success_threshold")

    @property
    @pulumi.getter(name="tcpSocketPort")
    def tcp_socket_port(self) -> Optional[int]:
        return pulumi.get(self, "tcp_socket_port")

    @property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[int]:
        return pulumi.get(self, "timeout_seconds")


@pulumi.output_type
class ContainerInstanceContainerReadinessProbe(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "execCommands":
            suggest = "exec_commands"
        elif key == "failureThreshold":
            suggest = "failure_threshold"
        elif key == "httpGetPath":
            suggest = "http_get_path"
        elif key == "httpGetPort":
            suggest = "http_get_port"
        elif key == "httpGetScheme":
            suggest = "http_get_scheme"
        elif key == "initDelaySeconds":
            suggest = "init_delay_seconds"
        elif key == "periodSeconds":
            suggest = "period_seconds"
        elif key == "successThreshold":
            suggest = "success_threshold"
        elif key == "tcpSocketPort":
            suggest = "tcp_socket_port"
        elif key == "timeoutSeconds":
            suggest = "timeout_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceContainerReadinessProbe. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceContainerReadinessProbe.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceContainerReadinessProbe.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 exec_commands: Optional[Sequence[str]] = None,
                 failure_threshold: Optional[int] = None,
                 http_get_path: Optional[str] = None,
                 http_get_port: Optional[int] = None,
                 http_get_scheme: Optional[str] = None,
                 init_delay_seconds: Optional[int] = None,
                 period_seconds: Optional[int] = None,
                 success_threshold: Optional[int] = None,
                 tcp_socket_port: Optional[int] = None,
                 timeout_seconds: Optional[int] = None):
        if exec_commands is not None:
            pulumi.set(__self__, "exec_commands", exec_commands)
        if failure_threshold is not None:
            pulumi.set(__self__, "failure_threshold", failure_threshold)
        if http_get_path is not None:
            pulumi.set(__self__, "http_get_path", http_get_path)
        if http_get_port is not None:
            pulumi.set(__self__, "http_get_port", http_get_port)
        if http_get_scheme is not None:
            pulumi.set(__self__, "http_get_scheme", http_get_scheme)
        if init_delay_seconds is not None:
            pulumi.set(__self__, "init_delay_seconds", init_delay_seconds)
        if period_seconds is not None:
            pulumi.set(__self__, "period_seconds", period_seconds)
        if success_threshold is not None:
            pulumi.set(__self__, "success_threshold", success_threshold)
        if tcp_socket_port is not None:
            pulumi.set(__self__, "tcp_socket_port", tcp_socket_port)
        if timeout_seconds is not None:
            pulumi.set(__self__, "timeout_seconds", timeout_seconds)

    @property
    @pulumi.getter(name="execCommands")
    def exec_commands(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "exec_commands")

    @property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[int]:
        return pulumi.get(self, "failure_threshold")

    @property
    @pulumi.getter(name="httpGetPath")
    def http_get_path(self) -> Optional[str]:
        return pulumi.get(self, "http_get_path")

    @property
    @pulumi.getter(name="httpGetPort")
    def http_get_port(self) -> Optional[int]:
        return pulumi.get(self, "http_get_port")

    @property
    @pulumi.getter(name="httpGetScheme")
    def http_get_scheme(self) -> Optional[str]:
        return pulumi.get(self, "http_get_scheme")

    @property
    @pulumi.getter(name="initDelaySeconds")
    def init_delay_seconds(self) -> Optional[int]:
        return pulumi.get(self, "init_delay_seconds")

    @property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[int]:
        return pulumi.get(self, "period_seconds")

    @property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[int]:
        return pulumi.get(self, "success_threshold")

    @property
    @pulumi.getter(name="tcpSocketPort")
    def tcp_socket_port(self) -> Optional[int]:
        return pulumi.get(self, "tcp_socket_port")

    @property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[int]:
        return pulumi.get(self, "timeout_seconds")


@pulumi.output_type
class ContainerInstanceContainerVolumeMount(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mountPropagation":
            suggest = "mount_propagation"
        elif key == "readOnly":
            suggest = "read_only"
        elif key == "subPath":
            suggest = "sub_path"
        elif key == "subPathExpr":
            suggest = "sub_path_expr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceContainerVolumeMount. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceContainerVolumeMount.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceContainerVolumeMount.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 path: str,
                 mount_propagation: Optional[str] = None,
                 read_only: Optional[bool] = None,
                 sub_path: Optional[str] = None,
                 sub_path_expr: Optional[str] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "path", path)
        if mount_propagation is not None:
            pulumi.set(__self__, "mount_propagation", mount_propagation)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)
        if sub_path is not None:
            pulumi.set(__self__, "sub_path", sub_path)
        if sub_path_expr is not None:
            pulumi.set(__self__, "sub_path_expr", sub_path_expr)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="mountPropagation")
    def mount_propagation(self) -> Optional[str]:
        return pulumi.get(self, "mount_propagation")

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[bool]:
        return pulumi.get(self, "read_only")

    @property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[str]:
        return pulumi.get(self, "sub_path")

    @property
    @pulumi.getter(name="subPathExpr")
    def sub_path_expr(self) -> Optional[str]:
        return pulumi.get(self, "sub_path_expr")


@pulumi.output_type
class ContainerInstanceImageRegistryCredential(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 password: Optional[str] = None,
                 server: Optional[str] = None,
                 username: Optional[str] = None):
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if server is not None:
            pulumi.set(__self__, "server", server)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def server(self) -> Optional[str]:
        return pulumi.get(self, "server")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        return pulumi.get(self, "username")


@pulumi.output_type
class ContainerInstanceInitContainer(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "envVars":
            suggest = "env_vars"
        elif key == "volumeMounts":
            suggest = "volume_mounts"
        elif key == "workingDir":
            suggest = "working_dir"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceInitContainer. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceInitContainer.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceInitContainer.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 image: str,
                 name: str,
                 args: Optional[Sequence[str]] = None,
                 commands: Optional[Sequence[str]] = None,
                 cpu: Optional[float] = None,
                 env_vars: Optional[Mapping[str, Any]] = None,
                 memory: Optional[float] = None,
                 volume_mounts: Optional[Sequence['outputs.ContainerInstanceInitContainerVolumeMount']] = None,
                 working_dir: Optional[str] = None):
        pulumi.set(__self__, "image", image)
        pulumi.set(__self__, "name", name)
        if args is not None:
            pulumi.set(__self__, "args", args)
        if commands is not None:
            pulumi.set(__self__, "commands", commands)
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if env_vars is not None:
            pulumi.set(__self__, "env_vars", env_vars)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if volume_mounts is not None:
            pulumi.set(__self__, "volume_mounts", volume_mounts)
        if working_dir is not None:
            pulumi.set(__self__, "working_dir", working_dir)

    @property
    @pulumi.getter
    def image(self) -> str:
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def args(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "args")

    @property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "commands")

    @property
    @pulumi.getter
    def cpu(self) -> Optional[float]:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter(name="envVars")
    def env_vars(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "env_vars")

    @property
    @pulumi.getter
    def memory(self) -> Optional[float]:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence['outputs.ContainerInstanceInitContainerVolumeMount']]:
        return pulumi.get(self, "volume_mounts")

    @property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[str]:
        return pulumi.get(self, "working_dir")


@pulumi.output_type
class ContainerInstanceInitContainerVolumeMount(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mountPropagation":
            suggest = "mount_propagation"
        elif key == "readOnly":
            suggest = "read_only"
        elif key == "subPath":
            suggest = "sub_path"
        elif key == "subPathExpr":
            suggest = "sub_path_expr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceInitContainerVolumeMount. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceInitContainerVolumeMount.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceInitContainerVolumeMount.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 path: str,
                 mount_propagation: Optional[str] = None,
                 read_only: Optional[bool] = None,
                 sub_path: Optional[str] = None,
                 sub_path_expr: Optional[str] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "path", path)
        if mount_propagation is not None:
            pulumi.set(__self__, "mount_propagation", mount_propagation)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)
        if sub_path is not None:
            pulumi.set(__self__, "sub_path", sub_path)
        if sub_path_expr is not None:
            pulumi.set(__self__, "sub_path_expr", sub_path_expr)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="mountPropagation")
    def mount_propagation(self) -> Optional[str]:
        return pulumi.get(self, "mount_propagation")

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[bool]:
        return pulumi.get(self, "read_only")

    @property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[str]:
        return pulumi.get(self, "sub_path")

    @property
    @pulumi.getter(name="subPathExpr")
    def sub_path_expr(self) -> Optional[str]:
        return pulumi.get(self, "sub_path_expr")


@pulumi.output_type
class ContainerInstanceNfsVolume(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "readOnly":
            suggest = "read_only"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInstanceNfsVolume. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInstanceNfsVolume.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInstanceNfsVolume.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 path: str,
                 server: str,
                 read_only: Optional[bool] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "server", server)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def server(self) -> str:
        return pulumi.get(self, "server")

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[bool]:
        return pulumi.get(self, "read_only")


