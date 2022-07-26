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
    'AvailabilityRegionsResult',
    'AwaitableAvailabilityRegionsResult',
    'availability_regions',
    'availability_regions_output',
]

@pulumi.output_type
class AvailabilityRegionsResult:
    """
    A collection of values returned by AvailabilityRegions.
    """
    def __init__(__self__, id=None, include_unavailable=None, name=None, regions=None, result_output_file=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_unavailable and not isinstance(include_unavailable, bool):
            raise TypeError("Expected argument 'include_unavailable' to be a bool")
        pulumi.set(__self__, "include_unavailable", include_unavailable)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if regions and not isinstance(regions, list):
            raise TypeError("Expected argument 'regions' to be a list")
        pulumi.set(__self__, "regions", regions)
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
    @pulumi.getter(name="includeUnavailable")
    def include_unavailable(self) -> Optional[bool]:
        return pulumi.get(self, "include_unavailable")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def regions(self) -> Sequence['outputs.AvailabilityRegionsRegionResult']:
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableAvailabilityRegionsResult(AvailabilityRegionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return AvailabilityRegionsResult(
            id=self.id,
            include_unavailable=self.include_unavailable,
            name=self.name,
            regions=self.regions,
            result_output_file=self.result_output_file)


def availability_regions(include_unavailable: Optional[bool] = None,
                         name: Optional[str] = None,
                         result_output_file: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableAvailabilityRegionsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['includeUnavailable'] = include_unavailable
    __args__['name'] = name
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Api/availabilityRegions:AvailabilityRegions', __args__, opts=opts, typ=AvailabilityRegionsResult).value

    return AwaitableAvailabilityRegionsResult(
        id=__ret__.id,
        include_unavailable=__ret__.include_unavailable,
        name=__ret__.name,
        regions=__ret__.regions,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(availability_regions)
def availability_regions_output(include_unavailable: Optional[pulumi.Input[Optional[bool]]] = None,
                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[AvailabilityRegionsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
