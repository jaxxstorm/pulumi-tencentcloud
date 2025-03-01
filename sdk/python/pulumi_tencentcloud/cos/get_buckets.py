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
    'GetBucketsResult',
    'AwaitableGetBucketsResult',
    'get_buckets',
    'get_buckets_output',
]

@pulumi.output_type
class GetBucketsResult:
    """
    A collection of values returned by getBuckets.
    """
    def __init__(__self__, bucket_lists=None, bucket_prefix=None, id=None, result_output_file=None, tags=None):
        if bucket_lists and not isinstance(bucket_lists, list):
            raise TypeError("Expected argument 'bucket_lists' to be a list")
        pulumi.set(__self__, "bucket_lists", bucket_lists)
        if bucket_prefix and not isinstance(bucket_prefix, str):
            raise TypeError("Expected argument 'bucket_prefix' to be a str")
        pulumi.set(__self__, "bucket_prefix", bucket_prefix)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="bucketLists")
    def bucket_lists(self) -> Sequence['outputs.GetBucketsBucketListResult']:
        """
        A list of bucket. Each element contains the following attributes:
        """
        return pulumi.get(self, "bucket_lists")

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[str]:
        return pulumi.get(self, "bucket_prefix")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        """
        The tags of a bucket.
        """
        return pulumi.get(self, "tags")


class AwaitableGetBucketsResult(GetBucketsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketsResult(
            bucket_lists=self.bucket_lists,
            bucket_prefix=self.bucket_prefix,
            id=self.id,
            result_output_file=self.result_output_file,
            tags=self.tags)


def get_buckets(bucket_prefix: Optional[str] = None,
                result_output_file: Optional[str] = None,
                tags: Optional[Mapping[str, Any]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketsResult:
    """
    Use this data source to query the COS buckets of the current Tencent Cloud user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    cos_buckets = tencentcloud.Cos.get_buckets(bucket_prefix="tf-bucket-",
        result_output_file="mytestpath")
    ```


    :param str bucket_prefix: A prefix string to filter results by bucket name.
    :param str result_output_file: Used to save results.
    :param Mapping[str, Any] tags: Tags to filter bucket.
    """
    __args__ = dict()
    __args__['bucketPrefix'] = bucket_prefix
    __args__['resultOutputFile'] = result_output_file
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Cos/getBuckets:getBuckets', __args__, opts=opts, typ=GetBucketsResult).value

    return AwaitableGetBucketsResult(
        bucket_lists=__ret__.bucket_lists,
        bucket_prefix=__ret__.bucket_prefix,
        id=__ret__.id,
        result_output_file=__ret__.result_output_file,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_buckets)
def get_buckets_output(bucket_prefix: Optional[pulumi.Input[Optional[str]]] = None,
                       result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                       tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBucketsResult]:
    """
    Use this data source to query the COS buckets of the current Tencent Cloud user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    cos_buckets = tencentcloud.Cos.get_buckets(bucket_prefix="tf-bucket-",
        result_output_file="mytestpath")
    ```


    :param str bucket_prefix: A prefix string to filter results by bucket name.
    :param str result_output_file: Used to save results.
    :param Mapping[str, Any] tags: Tags to filter bucket.
    """
    ...
