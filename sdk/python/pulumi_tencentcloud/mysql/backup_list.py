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
    'BackupListResult',
    'AwaitableBackupListResult',
    'backup_list',
    'backup_list_output',
]

@pulumi.output_type
class BackupListResult:
    """
    A collection of values returned by BackupList.
    """
    def __init__(__self__, id=None, lists=None, max_number=None, mysql_id=None, result_output_file=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lists and not isinstance(lists, list):
            raise TypeError("Expected argument 'lists' to be a list")
        pulumi.set(__self__, "lists", lists)
        if max_number and not isinstance(max_number, int):
            raise TypeError("Expected argument 'max_number' to be a int")
        pulumi.set(__self__, "max_number", max_number)
        if mysql_id and not isinstance(mysql_id, str):
            raise TypeError("Expected argument 'mysql_id' to be a str")
        pulumi.set(__self__, "mysql_id", mysql_id)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lists(self) -> Sequence['outputs.BackupListListResult']:
        return pulumi.get(self, "lists")

    @property
    @pulumi.getter(name="maxNumber")
    def max_number(self) -> Optional[int]:
        return pulumi.get(self, "max_number")

    @property
    @pulumi.getter(name="mysqlId")
    def mysql_id(self) -> str:
        return pulumi.get(self, "mysql_id")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableBackupListResult(BackupListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return BackupListResult(
            id=self.id,
            lists=self.lists,
            max_number=self.max_number,
            mysql_id=self.mysql_id,
            result_output_file=self.result_output_file)


def backup_list(max_number: Optional[int] = None,
                mysql_id: Optional[str] = None,
                result_output_file: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableBackupListResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['maxNumber'] = max_number
    __args__['mysqlId'] = mysql_id
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Mysql/backupList:BackupList', __args__, opts=opts, typ=BackupListResult).value

    return AwaitableBackupListResult(
        id=__ret__.id,
        lists=__ret__.lists,
        max_number=__ret__.max_number,
        mysql_id=__ret__.mysql_id,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(backup_list)
def backup_list_output(max_number: Optional[pulumi.Input[Optional[int]]] = None,
                       mysql_id: Optional[pulumi.Input[str]] = None,
                       result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[BackupListResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
