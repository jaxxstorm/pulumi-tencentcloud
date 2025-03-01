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
    'GetClustersResult',
    'AwaitableGetClustersResult',
    'get_clusters',
    'get_clusters_output',
]

@pulumi.output_type
class GetClustersResult:
    """
    A collection of values returned by getClusters.
    """
    def __init__(__self__, cluster_id=None, cluster_lists=None, cluster_name=None, db_type=None, id=None, project_id=None, result_output_file=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_lists and not isinstance(cluster_lists, list):
            raise TypeError("Expected argument 'cluster_lists' to be a list")
        pulumi.set(__self__, "cluster_lists", cluster_lists)
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if db_type and not isinstance(db_type, str):
            raise TypeError("Expected argument 'db_type' to be a str")
        pulumi.set(__self__, "db_type", db_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project_id and not isinstance(project_id, int):
            raise TypeError("Expected argument 'project_id' to be a int")
        pulumi.set(__self__, "project_id", project_id)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[str]:
        """
        ID of CynosDB cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterLists")
    def cluster_lists(self) -> Sequence['outputs.GetClustersClusterListResult']:
        """
        A list of clusters. Each element contains the following attributes:
        """
        return pulumi.get(self, "cluster_lists")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[str]:
        """
        Name of CynosDB cluster.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="dbType")
    def db_type(self) -> Optional[str]:
        """
        Type of CynosDB, and available values include `MYSQL`.
        """
        return pulumi.get(self, "db_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[int]:
        """
        ID of the project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableGetClustersResult(GetClustersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClustersResult(
            cluster_id=self.cluster_id,
            cluster_lists=self.cluster_lists,
            cluster_name=self.cluster_name,
            db_type=self.db_type,
            id=self.id,
            project_id=self.project_id,
            result_output_file=self.result_output_file)


def get_clusters(cluster_id: Optional[str] = None,
                 cluster_name: Optional[str] = None,
                 db_type: Optional[str] = None,
                 project_id: Optional[int] = None,
                 result_output_file: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClustersResult:
    """
    Use this data source to query detailed information of Cynosdb clusters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Cynosdb.get_clusters(cluster_id="cynosdbmysql-dzj5l8gz",
        cluster_name="test",
        db_type="MYSQL",
        project_id=0)
    ```


    :param str cluster_id: ID of the cluster to be queried.
    :param str cluster_name: Name of the cluster to be queried.
    :param str db_type: Type of CynosDB, and available values include `MYSQL`, `POSTGRESQL`.
    :param int project_id: ID of the project to be queried.
    :param str result_output_file: Used to save results.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['clusterName'] = cluster_name
    __args__['dbType'] = db_type
    __args__['projectId'] = project_id
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Cynosdb/getClusters:getClusters', __args__, opts=opts, typ=GetClustersResult).value

    return AwaitableGetClustersResult(
        cluster_id=__ret__.cluster_id,
        cluster_lists=__ret__.cluster_lists,
        cluster_name=__ret__.cluster_name,
        db_type=__ret__.db_type,
        id=__ret__.id,
        project_id=__ret__.project_id,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(get_clusters)
def get_clusters_output(cluster_id: Optional[pulumi.Input[Optional[str]]] = None,
                        cluster_name: Optional[pulumi.Input[Optional[str]]] = None,
                        db_type: Optional[pulumi.Input[Optional[str]]] = None,
                        project_id: Optional[pulumi.Input[Optional[int]]] = None,
                        result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClustersResult]:
    """
    Use this data source to query detailed information of Cynosdb clusters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Cynosdb.get_clusters(cluster_id="cynosdbmysql-dzj5l8gz",
        cluster_name="test",
        db_type="MYSQL",
        project_id=0)
    ```


    :param str cluster_id: ID of the cluster to be queried.
    :param str cluster_name: Name of the cluster to be queried.
    :param str db_type: Type of CynosDB, and available values include `MYSQL`, `POSTGRESQL`.
    :param int project_id: ID of the project to be queried.
    :param str result_output_file: Used to save results.
    """
    ...
