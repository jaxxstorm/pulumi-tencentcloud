# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CcnBandwidthLimitArgs', 'CcnBandwidthLimit']

@pulumi.input_type
class CcnBandwidthLimitArgs:
    def __init__(__self__, *,
                 ccn_id: pulumi.Input[str],
                 region: pulumi.Input[str],
                 bandwidth_limit: Optional[pulumi.Input[int]] = None,
                 dst_region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CcnBandwidthLimit resource.
        :param pulumi.Input[str] ccn_id: ID of the CCN.
        :param pulumi.Input[str] region: Limitation of region.
        :param pulumi.Input[int] bandwidth_limit: Limitation of bandwidth.
        :param pulumi.Input[str] dst_region: Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.
        """
        pulumi.set(__self__, "ccn_id", ccn_id)
        pulumi.set(__self__, "region", region)
        if bandwidth_limit is not None:
            pulumi.set(__self__, "bandwidth_limit", bandwidth_limit)
        if dst_region is not None:
            pulumi.set(__self__, "dst_region", dst_region)

    @property
    @pulumi.getter(name="ccnId")
    def ccn_id(self) -> pulumi.Input[str]:
        """
        ID of the CCN.
        """
        return pulumi.get(self, "ccn_id")

    @ccn_id.setter
    def ccn_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ccn_id", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        Limitation of region.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="bandwidthLimit")
    def bandwidth_limit(self) -> Optional[pulumi.Input[int]]:
        """
        Limitation of bandwidth.
        """
        return pulumi.get(self, "bandwidth_limit")

    @bandwidth_limit.setter
    def bandwidth_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bandwidth_limit", value)

    @property
    @pulumi.getter(name="dstRegion")
    def dst_region(self) -> Optional[pulumi.Input[str]]:
        """
        Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.
        """
        return pulumi.get(self, "dst_region")

    @dst_region.setter
    def dst_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dst_region", value)


@pulumi.input_type
class _CcnBandwidthLimitState:
    def __init__(__self__, *,
                 bandwidth_limit: Optional[pulumi.Input[int]] = None,
                 ccn_id: Optional[pulumi.Input[str]] = None,
                 dst_region: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CcnBandwidthLimit resources.
        :param pulumi.Input[int] bandwidth_limit: Limitation of bandwidth.
        :param pulumi.Input[str] ccn_id: ID of the CCN.
        :param pulumi.Input[str] dst_region: Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.
        :param pulumi.Input[str] region: Limitation of region.
        """
        if bandwidth_limit is not None:
            pulumi.set(__self__, "bandwidth_limit", bandwidth_limit)
        if ccn_id is not None:
            pulumi.set(__self__, "ccn_id", ccn_id)
        if dst_region is not None:
            pulumi.set(__self__, "dst_region", dst_region)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="bandwidthLimit")
    def bandwidth_limit(self) -> Optional[pulumi.Input[int]]:
        """
        Limitation of bandwidth.
        """
        return pulumi.get(self, "bandwidth_limit")

    @bandwidth_limit.setter
    def bandwidth_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bandwidth_limit", value)

    @property
    @pulumi.getter(name="ccnId")
    def ccn_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the CCN.
        """
        return pulumi.get(self, "ccn_id")

    @ccn_id.setter
    def ccn_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ccn_id", value)

    @property
    @pulumi.getter(name="dstRegion")
    def dst_region(self) -> Optional[pulumi.Input[str]]:
        """
        Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.
        """
        return pulumi.get(self, "dst_region")

    @dst_region.setter
    def dst_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dst_region", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Limitation of region.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class CcnBandwidthLimit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_limit: Optional[pulumi.Input[int]] = None,
                 ccn_id: Optional[pulumi.Input[str]] = None,
                 dst_region: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CcnBandwidthLimit resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bandwidth_limit: Limitation of bandwidth.
        :param pulumi.Input[str] ccn_id: ID of the CCN.
        :param pulumi.Input[str] dst_region: Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.
        :param pulumi.Input[str] region: Limitation of region.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CcnBandwidthLimitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CcnBandwidthLimit resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CcnBandwidthLimitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CcnBandwidthLimitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_limit: Optional[pulumi.Input[int]] = None,
                 ccn_id: Optional[pulumi.Input[str]] = None,
                 dst_region: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CcnBandwidthLimitArgs.__new__(CcnBandwidthLimitArgs)

            __props__.__dict__["bandwidth_limit"] = bandwidth_limit
            if ccn_id is None and not opts.urn:
                raise TypeError("Missing required property 'ccn_id'")
            __props__.__dict__["ccn_id"] = ccn_id
            __props__.__dict__["dst_region"] = dst_region
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
        super(CcnBandwidthLimit, __self__).__init__(
            'tencentcloud:Ccn/ccnBandwidthLimit:CcnBandwidthLimit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bandwidth_limit: Optional[pulumi.Input[int]] = None,
            ccn_id: Optional[pulumi.Input[str]] = None,
            dst_region: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'CcnBandwidthLimit':
        """
        Get an existing CcnBandwidthLimit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bandwidth_limit: Limitation of bandwidth.
        :param pulumi.Input[str] ccn_id: ID of the CCN.
        :param pulumi.Input[str] dst_region: Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.
        :param pulumi.Input[str] region: Limitation of region.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CcnBandwidthLimitState.__new__(_CcnBandwidthLimitState)

        __props__.__dict__["bandwidth_limit"] = bandwidth_limit
        __props__.__dict__["ccn_id"] = ccn_id
        __props__.__dict__["dst_region"] = dst_region
        __props__.__dict__["region"] = region
        return CcnBandwidthLimit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bandwidthLimit")
    def bandwidth_limit(self) -> pulumi.Output[int]:
        """
        Limitation of bandwidth.
        """
        return pulumi.get(self, "bandwidth_limit")

    @property
    @pulumi.getter(name="ccnId")
    def ccn_id(self) -> pulumi.Output[str]:
        """
        ID of the CCN.
        """
        return pulumi.get(self, "ccn_id")

    @property
    @pulumi.getter(name="dstRegion")
    def dst_region(self) -> pulumi.Output[Optional[str]]:
        """
        Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.
        """
        return pulumi.get(self, "dst_region")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Limitation of region.
        """
        return pulumi.get(self, "region")

