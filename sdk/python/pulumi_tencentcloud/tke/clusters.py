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
    'ClustersResult',
    'AwaitableClustersResult',
    'clusters',
    'clusters_output',
]

@pulumi.output_type
class ClustersResult:
    """
    A collection of values returned by Clusters.
    """
    def __init__(__self__, cluster_id=None, cluster_name=None, id=None, lists=None, result_output_file=None, tags=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lists and not isinstance(lists, list):
            raise TypeError("Expected argument 'lists' to be a list")
        pulumi.set(__self__, "lists", lists)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[str]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[str]:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lists(self) -> Sequence['outputs.ClustersListResult']:
        return pulumi.get(self, "lists")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")


class AwaitableClustersResult(ClustersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ClustersResult(
            cluster_id=self.cluster_id,
            cluster_name=self.cluster_name,
            id=self.id,
            lists=self.lists,
            result_output_file=self.result_output_file,
            tags=self.tags)


def clusters(cluster_id: Optional[str] = None,
             cluster_name: Optional[str] = None,
             result_output_file: Optional[str] = None,
             tags: Optional[Mapping[str, Any]] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableClustersResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['clusterName'] = cluster_name
    __args__['resultOutputFile'] = result_output_file
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Tke/clusters:Clusters', __args__, opts=opts, typ=ClustersResult).value

    return AwaitableClustersResult(
        cluster_id=__ret__.cluster_id,
        cluster_name=__ret__.cluster_name,
        id=__ret__.id,
        lists=__ret__.lists,
        result_output_file=__ret__.result_output_file,
        tags=__ret__.tags)


@_utilities.lift_output_func(clusters)
def clusters_output(cluster_id: Optional[pulumi.Input[Optional[str]]] = None,
                    cluster_name: Optional[pulumi.Input[Optional[str]]] = None,
                    result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                    tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ClustersResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
