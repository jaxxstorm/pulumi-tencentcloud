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
    'InstancesResult',
    'AwaitableInstancesResult',
    'instances',
    'instances_output',
]

@pulumi.output_type
class InstancesResult:
    """
    A collection of values returned by Instances.
    """
    def __init__(__self__, charge_type=None, engine_version=None, id=None, init_flag=None, instance_lists=None, instance_name=None, instance_role=None, limit=None, mysql_id=None, offset=None, pay_type=None, result_output_file=None, security_group_id=None, status=None, with_dr=None, with_master=None, with_ro=None):
        if charge_type and not isinstance(charge_type, str):
            raise TypeError("Expected argument 'charge_type' to be a str")
        pulumi.set(__self__, "charge_type", charge_type)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if init_flag and not isinstance(init_flag, int):
            raise TypeError("Expected argument 'init_flag' to be a int")
        pulumi.set(__self__, "init_flag", init_flag)
        if instance_lists and not isinstance(instance_lists, list):
            raise TypeError("Expected argument 'instance_lists' to be a list")
        pulumi.set(__self__, "instance_lists", instance_lists)
        if instance_name and not isinstance(instance_name, str):
            raise TypeError("Expected argument 'instance_name' to be a str")
        pulumi.set(__self__, "instance_name", instance_name)
        if instance_role and not isinstance(instance_role, str):
            raise TypeError("Expected argument 'instance_role' to be a str")
        pulumi.set(__self__, "instance_role", instance_role)
        if limit and not isinstance(limit, int):
            raise TypeError("Expected argument 'limit' to be a int")
        pulumi.set(__self__, "limit", limit)
        if mysql_id and not isinstance(mysql_id, str):
            raise TypeError("Expected argument 'mysql_id' to be a str")
        pulumi.set(__self__, "mysql_id", mysql_id)
        if offset and not isinstance(offset, int):
            raise TypeError("Expected argument 'offset' to be a int")
        pulumi.set(__self__, "offset", offset)
        if pay_type and not isinstance(pay_type, int):
            raise TypeError("Expected argument 'pay_type' to be a int")
        if pay_type is not None:
            warnings.warn("""It has been deprecated from version 1.36.0. Please use `charge_type` instead.""", DeprecationWarning)
            pulumi.log.warn("""pay_type is deprecated: It has been deprecated from version 1.36.0. Please use `charge_type` instead.""")

        pulumi.set(__self__, "pay_type", pay_type)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if security_group_id and not isinstance(security_group_id, str):
            raise TypeError("Expected argument 'security_group_id' to be a str")
        pulumi.set(__self__, "security_group_id", security_group_id)
        if status and not isinstance(status, int):
            raise TypeError("Expected argument 'status' to be a int")
        pulumi.set(__self__, "status", status)
        if with_dr and not isinstance(with_dr, int):
            raise TypeError("Expected argument 'with_dr' to be a int")
        pulumi.set(__self__, "with_dr", with_dr)
        if with_master and not isinstance(with_master, int):
            raise TypeError("Expected argument 'with_master' to be a int")
        pulumi.set(__self__, "with_master", with_master)
        if with_ro and not isinstance(with_ro, int):
            raise TypeError("Expected argument 'with_ro' to be a int")
        pulumi.set(__self__, "with_ro", with_ro)

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> Optional[str]:
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[str]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initFlag")
    def init_flag(self) -> Optional[int]:
        return pulumi.get(self, "init_flag")

    @property
    @pulumi.getter(name="instanceLists")
    def instance_lists(self) -> Sequence['outputs.InstancesInstanceListResult']:
        return pulumi.get(self, "instance_lists")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[str]:
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> Optional[str]:
        return pulumi.get(self, "instance_role")

    @property
    @pulumi.getter
    def limit(self) -> Optional[int]:
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter(name="mysqlId")
    def mysql_id(self) -> Optional[str]:
        return pulumi.get(self, "mysql_id")

    @property
    @pulumi.getter
    def offset(self) -> Optional[int]:
        return pulumi.get(self, "offset")

    @property
    @pulumi.getter(name="payType")
    def pay_type(self) -> Optional[int]:
        return pulumi.get(self, "pay_type")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[str]:
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[int]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="withDr")
    def with_dr(self) -> Optional[int]:
        return pulumi.get(self, "with_dr")

    @property
    @pulumi.getter(name="withMaster")
    def with_master(self) -> Optional[int]:
        return pulumi.get(self, "with_master")

    @property
    @pulumi.getter(name="withRo")
    def with_ro(self) -> Optional[int]:
        return pulumi.get(self, "with_ro")


class AwaitableInstancesResult(InstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return InstancesResult(
            charge_type=self.charge_type,
            engine_version=self.engine_version,
            id=self.id,
            init_flag=self.init_flag,
            instance_lists=self.instance_lists,
            instance_name=self.instance_name,
            instance_role=self.instance_role,
            limit=self.limit,
            mysql_id=self.mysql_id,
            offset=self.offset,
            pay_type=self.pay_type,
            result_output_file=self.result_output_file,
            security_group_id=self.security_group_id,
            status=self.status,
            with_dr=self.with_dr,
            with_master=self.with_master,
            with_ro=self.with_ro)


def instances(charge_type: Optional[str] = None,
              engine_version: Optional[str] = None,
              init_flag: Optional[int] = None,
              instance_name: Optional[str] = None,
              instance_role: Optional[str] = None,
              limit: Optional[int] = None,
              mysql_id: Optional[str] = None,
              offset: Optional[int] = None,
              pay_type: Optional[int] = None,
              result_output_file: Optional[str] = None,
              security_group_id: Optional[str] = None,
              status: Optional[int] = None,
              with_dr: Optional[int] = None,
              with_master: Optional[int] = None,
              with_ro: Optional[int] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableInstancesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['chargeType'] = charge_type
    __args__['engineVersion'] = engine_version
    __args__['initFlag'] = init_flag
    __args__['instanceName'] = instance_name
    __args__['instanceRole'] = instance_role
    __args__['limit'] = limit
    __args__['mysqlId'] = mysql_id
    __args__['offset'] = offset
    __args__['payType'] = pay_type
    __args__['resultOutputFile'] = result_output_file
    __args__['securityGroupId'] = security_group_id
    __args__['status'] = status
    __args__['withDr'] = with_dr
    __args__['withMaster'] = with_master
    __args__['withRo'] = with_ro
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Mysql/instances:Instances', __args__, opts=opts, typ=InstancesResult).value

    return AwaitableInstancesResult(
        charge_type=__ret__.charge_type,
        engine_version=__ret__.engine_version,
        id=__ret__.id,
        init_flag=__ret__.init_flag,
        instance_lists=__ret__.instance_lists,
        instance_name=__ret__.instance_name,
        instance_role=__ret__.instance_role,
        limit=__ret__.limit,
        mysql_id=__ret__.mysql_id,
        offset=__ret__.offset,
        pay_type=__ret__.pay_type,
        result_output_file=__ret__.result_output_file,
        security_group_id=__ret__.security_group_id,
        status=__ret__.status,
        with_dr=__ret__.with_dr,
        with_master=__ret__.with_master,
        with_ro=__ret__.with_ro)


@_utilities.lift_output_func(instances)
def instances_output(charge_type: Optional[pulumi.Input[Optional[str]]] = None,
                     engine_version: Optional[pulumi.Input[Optional[str]]] = None,
                     init_flag: Optional[pulumi.Input[Optional[int]]] = None,
                     instance_name: Optional[pulumi.Input[Optional[str]]] = None,
                     instance_role: Optional[pulumi.Input[Optional[str]]] = None,
                     limit: Optional[pulumi.Input[Optional[int]]] = None,
                     mysql_id: Optional[pulumi.Input[Optional[str]]] = None,
                     offset: Optional[pulumi.Input[Optional[int]]] = None,
                     pay_type: Optional[pulumi.Input[Optional[int]]] = None,
                     result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                     security_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                     status: Optional[pulumi.Input[Optional[int]]] = None,
                     with_dr: Optional[pulumi.Input[Optional[int]]] = None,
                     with_master: Optional[pulumi.Input[Optional[int]]] = None,
                     with_ro: Optional[pulumi.Input[Optional[int]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[InstancesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
