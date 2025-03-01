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
    'GetTablegroupsResult',
    'AwaitableGetTablegroupsResult',
    'get_tablegroups',
    'get_tablegroups_output',
]

@pulumi.output_type
class GetTablegroupsResult:
    """
    A collection of values returned by getTablegroups.
    """
    def __init__(__self__, cluster_id=None, id=None, lists=None, result_output_file=None, tablegroup_id=None, tablegroup_name=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lists and not isinstance(lists, list):
            raise TypeError("Expected argument 'lists' to be a list")
        pulumi.set(__self__, "lists", lists)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if tablegroup_id and not isinstance(tablegroup_id, str):
            raise TypeError("Expected argument 'tablegroup_id' to be a str")
        pulumi.set(__self__, "tablegroup_id", tablegroup_id)
        if tablegroup_name and not isinstance(tablegroup_name, str):
            raise TypeError("Expected argument 'tablegroup_name' to be a str")
        pulumi.set(__self__, "tablegroup_name", tablegroup_name)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lists(self) -> Sequence['outputs.GetTablegroupsListResult']:
        """
        A list of table group. Each element contains the following attributes.
        """
        return pulumi.get(self, "lists")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="tablegroupId")
    def tablegroup_id(self) -> Optional[str]:
        """
        Id of the table group.
        """
        return pulumi.get(self, "tablegroup_id")

    @property
    @pulumi.getter(name="tablegroupName")
    def tablegroup_name(self) -> Optional[str]:
        """
        Name of the table group.
        """
        return pulumi.get(self, "tablegroup_name")


class AwaitableGetTablegroupsResult(GetTablegroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTablegroupsResult(
            cluster_id=self.cluster_id,
            id=self.id,
            lists=self.lists,
            result_output_file=self.result_output_file,
            tablegroup_id=self.tablegroup_id,
            tablegroup_name=self.tablegroup_name)


def get_tablegroups(cluster_id: Optional[str] = None,
                    result_output_file: Optional[str] = None,
                    tablegroup_id: Optional[str] = None,
                    tablegroup_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTablegroupsResult:
    """
    Use this data source to query table groups of the TcaplusDB cluster.


    :param str cluster_id: Id of the TcaplusDB cluster to be query.
    :param str result_output_file: File for saving results.
    :param str tablegroup_id: Id of the table group to be query.
    :param str tablegroup_name: Name of the table group to be query.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['resultOutputFile'] = result_output_file
    __args__['tablegroupId'] = tablegroup_id
    __args__['tablegroupName'] = tablegroup_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Tcaplus/getTablegroups:getTablegroups', __args__, opts=opts, typ=GetTablegroupsResult).value

    return AwaitableGetTablegroupsResult(
        cluster_id=__ret__.cluster_id,
        id=__ret__.id,
        lists=__ret__.lists,
        result_output_file=__ret__.result_output_file,
        tablegroup_id=__ret__.tablegroup_id,
        tablegroup_name=__ret__.tablegroup_name)


@_utilities.lift_output_func(get_tablegroups)
def get_tablegroups_output(cluster_id: Optional[pulumi.Input[str]] = None,
                           result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                           tablegroup_id: Optional[pulumi.Input[Optional[str]]] = None,
                           tablegroup_name: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTablegroupsResult]:
    """
    Use this data source to query table groups of the TcaplusDB cluster.


    :param str cluster_id: Id of the TcaplusDB cluster to be query.
    :param str result_output_file: File for saving results.
    :param str tablegroup_id: Id of the table group to be query.
    :param str tablegroup_name: Name of the table group to be query.
    """
    ...
