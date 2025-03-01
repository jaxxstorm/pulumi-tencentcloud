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
    'GetGatewayRoutesResult',
    'AwaitableGetGatewayRoutesResult',
    'get_gateway_routes',
    'get_gateway_routes_output',
]

@pulumi.output_type
class GetGatewayRoutesResult:
    """
    A collection of values returned by getGatewayRoutes.
    """
    def __init__(__self__, destination_cidr=None, id=None, instance_id=None, instance_type=None, result_output_file=None, vpn_gateway_id=None, vpn_gateway_route_lists=None):
        if destination_cidr and not isinstance(destination_cidr, str):
            raise TypeError("Expected argument 'destination_cidr' to be a str")
        pulumi.set(__self__, "destination_cidr", destination_cidr)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if vpn_gateway_id and not isinstance(vpn_gateway_id, str):
            raise TypeError("Expected argument 'vpn_gateway_id' to be a str")
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)
        if vpn_gateway_route_lists and not isinstance(vpn_gateway_route_lists, list):
            raise TypeError("Expected argument 'vpn_gateway_route_lists' to be a list")
        pulumi.set(__self__, "vpn_gateway_route_lists", vpn_gateway_route_lists)

    @property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[str]:
        return pulumi.get(self, "destination_cidr")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> str:
        return pulumi.get(self, "vpn_gateway_id")

    @property
    @pulumi.getter(name="vpnGatewayRouteLists")
    def vpn_gateway_route_lists(self) -> Sequence['outputs.GetGatewayRoutesVpnGatewayRouteListResult']:
        """
        Information list of the vpn gateway routes.
        """
        return pulumi.get(self, "vpn_gateway_route_lists")


class AwaitableGetGatewayRoutesResult(GetGatewayRoutesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGatewayRoutesResult(
            destination_cidr=self.destination_cidr,
            id=self.id,
            instance_id=self.instance_id,
            instance_type=self.instance_type,
            result_output_file=self.result_output_file,
            vpn_gateway_id=self.vpn_gateway_id,
            vpn_gateway_route_lists=self.vpn_gateway_route_lists)


def get_gateway_routes(destination_cidr: Optional[str] = None,
                       instance_id: Optional[str] = None,
                       instance_type: Optional[str] = None,
                       result_output_file: Optional[str] = None,
                       vpn_gateway_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGatewayRoutesResult:
    """
    Use this data source to query detailed information of VPN gateways.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Vpn.get_gateways(destination_cidr_block="vpngw-8ccsnclt",
        instance_id="ap-guangzhou-3",
        instance_type="1.1.1.1",
        tags={
            "test": "tf",
        },
        vpn_gateway_id="main")
    ```


    :param str destination_cidr: Destination IDC IP range.
    :param str instance_id: Instance ID of the next hop.
    :param str instance_type: Next hop type (type of the associated instance). Valid values: VPNCONN (VPN tunnel) and CCN (CCN instance).
    :param str result_output_file: Used to save results.
    :param str vpn_gateway_id: VPN gateway ID.
    """
    __args__ = dict()
    __args__['destinationCidr'] = destination_cidr
    __args__['instanceId'] = instance_id
    __args__['instanceType'] = instance_type
    __args__['resultOutputFile'] = result_output_file
    __args__['vpnGatewayId'] = vpn_gateway_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Vpn/getGatewayRoutes:getGatewayRoutes', __args__, opts=opts, typ=GetGatewayRoutesResult).value

    return AwaitableGetGatewayRoutesResult(
        destination_cidr=__ret__.destination_cidr,
        id=__ret__.id,
        instance_id=__ret__.instance_id,
        instance_type=__ret__.instance_type,
        result_output_file=__ret__.result_output_file,
        vpn_gateway_id=__ret__.vpn_gateway_id,
        vpn_gateway_route_lists=__ret__.vpn_gateway_route_lists)


@_utilities.lift_output_func(get_gateway_routes)
def get_gateway_routes_output(destination_cidr: Optional[pulumi.Input[Optional[str]]] = None,
                              instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                              instance_type: Optional[pulumi.Input[Optional[str]]] = None,
                              result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                              vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGatewayRoutesResult]:
    """
    Use this data source to query detailed information of VPN gateways.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Vpn.get_gateways(destination_cidr_block="vpngw-8ccsnclt",
        instance_id="ap-guangzhou-3",
        instance_type="1.1.1.1",
        tags={
            "test": "tf",
        },
        vpn_gateway_id="main")
    ```


    :param str destination_cidr: Destination IDC IP range.
    :param str instance_id: Instance ID of the next hop.
    :param str instance_type: Next hop type (type of the associated instance). Valid values: VPNCONN (VPN tunnel) and CCN (CCN instance).
    :param str result_output_file: Used to save results.
    :param str vpn_gateway_id: VPN gateway ID.
    """
    ...
