# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetTypesResult',
    'AwaitableGetTypesResult',
    'get_types',
    'get_types_output',
]

@pulumi.output_type
class GetTypesResult:
    """
    A collection of values returned by getTypes.
    """
    def __init__(__self__, availability_zone=None, cpu_core_count=None, exclude_sold_out=None, filters=None, gpu_core_count=None, id=None, instance_types=None, memory_size=None, result_output_file=None):
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if cpu_core_count and not isinstance(cpu_core_count, int):
            raise TypeError("Expected argument 'cpu_core_count' to be a int")
        pulumi.set(__self__, "cpu_core_count", cpu_core_count)
        if exclude_sold_out and not isinstance(exclude_sold_out, bool):
            raise TypeError("Expected argument 'exclude_sold_out' to be a bool")
        pulumi.set(__self__, "exclude_sold_out", exclude_sold_out)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if gpu_core_count and not isinstance(gpu_core_count, int):
            raise TypeError("Expected argument 'gpu_core_count' to be a int")
        pulumi.set(__self__, "gpu_core_count", gpu_core_count)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_types and not isinstance(instance_types, list):
            raise TypeError("Expected argument 'instance_types' to be a list")
        pulumi.set(__self__, "instance_types", instance_types)
        if memory_size and not isinstance(memory_size, int):
            raise TypeError("Expected argument 'memory_size' to be a int")
        pulumi.set(__self__, "memory_size", memory_size)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        The available zone that the CVM instance locates at.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> Optional[int]:
        """
        The number of CPU cores of the instance.
        """
        return pulumi.get(self, "cpu_core_count")

    @property
    @pulumi.getter(name="excludeSoldOut")
    def exclude_sold_out(self) -> Optional[bool]:
        return pulumi.get(self, "exclude_sold_out")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetTypesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="gpuCoreCount")
    def gpu_core_count(self) -> Optional[int]:
        """
        The number of GPU cores of the instance.
        """
        return pulumi.get(self, "gpu_core_count")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence['outputs.GetTypesInstanceTypeResult']:
        """
        An information list of cvm instance. Each element contains the following attributes:
        """
        return pulumi.get(self, "instance_types")

    @property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> Optional[int]:
        """
        Instance memory capacity, unit in GB.
        """
        return pulumi.get(self, "memory_size")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableGetTypesResult(GetTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTypesResult(
            availability_zone=self.availability_zone,
            cpu_core_count=self.cpu_core_count,
            exclude_sold_out=self.exclude_sold_out,
            filters=self.filters,
            gpu_core_count=self.gpu_core_count,
            id=self.id,
            instance_types=self.instance_types,
            memory_size=self.memory_size,
            result_output_file=self.result_output_file)


def get_types(availability_zone: Optional[str] = None,
              cpu_core_count: Optional[int] = None,
              exclude_sold_out: Optional[bool] = None,
              filters: Optional[Sequence[pulumi.InputType['GetTypesFilterArgs']]] = None,
              gpu_core_count: Optional[int] = None,
              memory_size: Optional[int] = None,
              result_output_file: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTypesResult:
    """
    Use this data source to query instances type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Instance.get_types(availability_zone="ap-guangzhou-2",
        cpu_core_count=2,
        memory_size=4)
    t1c1g = tencentcloud.Instance.get_types(cpu_core_count=1,
        exclude_sold_out=True,
        filters=[
            tencentcloud.instance.GetTypesFilterArgs(
                name="instance-charge-type",
                values=["POSTPAID_BY_HOUR"],
            ),
            tencentcloud.instance.GetTypesFilterArgs(
                name="zone",
                values=["ap-shanghai-2"],
            ),
        ],
        memory_size=1)
    ```


    :param str availability_zone: The available zone that the CVM instance locates at. This field is conflict with `filter`.
    :param int cpu_core_count: The number of CPU cores of the instance.
    :param bool exclude_sold_out: Indicate to filter instances types that is sold out or not, default is false.
    :param Sequence[pulumi.InputType['GetTypesFilterArgs']] filters: One or more name/value pairs to filter. This field is conflict with `availability_zone`.
    :param int gpu_core_count: The number of GPU cores of the instance.
    :param int memory_size: Instance memory capacity, unit in GB.
    :param str result_output_file: Used to save results.
    """
    __args__ = dict()
    __args__['availabilityZone'] = availability_zone
    __args__['cpuCoreCount'] = cpu_core_count
    __args__['excludeSoldOut'] = exclude_sold_out
    __args__['filters'] = filters
    __args__['gpuCoreCount'] = gpu_core_count
    __args__['memorySize'] = memory_size
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Instance/getTypes:getTypes', __args__, opts=opts, typ=GetTypesResult).value

    return AwaitableGetTypesResult(
        availability_zone=__ret__.availability_zone,
        cpu_core_count=__ret__.cpu_core_count,
        exclude_sold_out=__ret__.exclude_sold_out,
        filters=__ret__.filters,
        gpu_core_count=__ret__.gpu_core_count,
        id=__ret__.id,
        instance_types=__ret__.instance_types,
        memory_size=__ret__.memory_size,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(get_types)
def get_types_output(availability_zone: Optional[pulumi.Input[Optional[str]]] = None,
                     cpu_core_count: Optional[pulumi.Input[Optional[int]]] = None,
                     exclude_sold_out: Optional[pulumi.Input[Optional[bool]]] = None,
                     filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTypesFilterArgs']]]]] = None,
                     gpu_core_count: Optional[pulumi.Input[Optional[int]]] = None,
                     memory_size: Optional[pulumi.Input[Optional[int]]] = None,
                     result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTypesResult]:
    """
    Use this data source to query instances type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Instance.get_types(availability_zone="ap-guangzhou-2",
        cpu_core_count=2,
        memory_size=4)
    t1c1g = tencentcloud.Instance.get_types(cpu_core_count=1,
        exclude_sold_out=True,
        filters=[
            tencentcloud.instance.GetTypesFilterArgs(
                name="instance-charge-type",
                values=["POSTPAID_BY_HOUR"],
            ),
            tencentcloud.instance.GetTypesFilterArgs(
                name="zone",
                values=["ap-shanghai-2"],
            ),
        ],
        memory_size=1)
    ```


    :param str availability_zone: The available zone that the CVM instance locates at. This field is conflict with `filter`.
    :param int cpu_core_count: The number of CPU cores of the instance.
    :param bool exclude_sold_out: Indicate to filter instances types that is sold out or not, default is false.
    :param Sequence[pulumi.InputType['GetTypesFilterArgs']] filters: One or more name/value pairs to filter. This field is conflict with `availability_zone`.
    :param int gpu_core_count: The number of GPU cores of the instance.
    :param int memory_size: Instance memory capacity, unit in GB.
    :param str result_output_file: Used to save results.
    """
    ...
