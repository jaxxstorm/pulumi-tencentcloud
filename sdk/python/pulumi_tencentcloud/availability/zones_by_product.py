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
    'ZonesByProductResult',
    'AwaitableZonesByProductResult',
    'zones_by_product',
    'zones_by_product_output',
]

@pulumi.output_type
class ZonesByProductResult:
    """
    A collection of values returned by ZonesByProduct.
    """
    def __init__(__self__, id=None, include_unavailable=None, name=None, product=None, result_output_file=None, zones=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_unavailable and not isinstance(include_unavailable, bool):
            raise TypeError("Expected argument 'include_unavailable' to be a bool")
        pulumi.set(__self__, "include_unavailable", include_unavailable)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if product and not isinstance(product, str):
            raise TypeError("Expected argument 'product' to be a str")
        pulumi.set(__self__, "product", product)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

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
    def product(self) -> str:
        return pulumi.get(self, "product")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter
    def zones(self) -> Sequence['outputs.ZonesByProductZoneResult']:
        return pulumi.get(self, "zones")


class AwaitableZonesByProductResult(ZonesByProductResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ZonesByProductResult(
            id=self.id,
            include_unavailable=self.include_unavailable,
            name=self.name,
            product=self.product,
            result_output_file=self.result_output_file,
            zones=self.zones)


def zones_by_product(include_unavailable: Optional[bool] = None,
                     name: Optional[str] = None,
                     product: Optional[str] = None,
                     result_output_file: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableZonesByProductResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['includeUnavailable'] = include_unavailable
    __args__['name'] = name
    __args__['product'] = product
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Availability/zonesByProduct:ZonesByProduct', __args__, opts=opts, typ=ZonesByProductResult).value

    return AwaitableZonesByProductResult(
        id=__ret__.id,
        include_unavailable=__ret__.include_unavailable,
        name=__ret__.name,
        product=__ret__.product,
        result_output_file=__ret__.result_output_file,
        zones=__ret__.zones)


@_utilities.lift_output_func(zones_by_product)
def zones_by_product_output(include_unavailable: Optional[pulumi.Input[Optional[bool]]] = None,
                            name: Optional[pulumi.Input[Optional[str]]] = None,
                            product: Optional[pulumi.Input[str]] = None,
                            result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ZonesByProductResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
