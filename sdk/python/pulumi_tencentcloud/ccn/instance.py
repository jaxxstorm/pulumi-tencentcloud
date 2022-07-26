# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 bandwidth_limit_type: Optional[pulumi.Input[str]] = None,
                 charge_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 qos: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] bandwidth_limit_type: The speed limit type. Valid values: `INTER_REGION_LIMIT`, `OUTER_REGION_LIMIT`. `OUTER_REGION_LIMIT` represents the
               regional export speed limit, `INTER_REGION_LIMIT` is the inter-regional speed limit. The default is
               `OUTER_REGION_LIMIT`.
        :param pulumi.Input[str] charge_type: Billing mode. Valid values: `PREPAID`, `POSTPAID`. `PREPAID` means prepaid, which means annual and monthly subscription,
               `POSTPAID` means post-payment, which means billing by volume. The default is `POSTPAID`. The prepaid model only supports
               inter-regional speed limit, and the post-paid model supports inter-regional speed limit and regional export speed limit.
        :param pulumi.Input[str] description: Description of CCN, and maximum length does not exceed 100 bytes.
        :param pulumi.Input[str] name: Name of the CCN to be queried, and maximum length does not exceed 60 bytes.
        :param pulumi.Input[str] qos: Service quality of CCN. Valid values: `PT`, `AU`, `AG`. The default is `AU`.
        :param pulumi.Input[Mapping[str, Any]] tags: Instance tag.
        """
        if bandwidth_limit_type is not None:
            pulumi.set(__self__, "bandwidth_limit_type", bandwidth_limit_type)
        if charge_type is not None:
            pulumi.set(__self__, "charge_type", charge_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if qos is not None:
            pulumi.set(__self__, "qos", qos)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="bandwidthLimitType")
    def bandwidth_limit_type(self) -> Optional[pulumi.Input[str]]:
        """
        The speed limit type. Valid values: `INTER_REGION_LIMIT`, `OUTER_REGION_LIMIT`. `OUTER_REGION_LIMIT` represents the
        regional export speed limit, `INTER_REGION_LIMIT` is the inter-regional speed limit. The default is
        `OUTER_REGION_LIMIT`.
        """
        return pulumi.get(self, "bandwidth_limit_type")

    @bandwidth_limit_type.setter
    def bandwidth_limit_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bandwidth_limit_type", value)

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> Optional[pulumi.Input[str]]:
        """
        Billing mode. Valid values: `PREPAID`, `POSTPAID`. `PREPAID` means prepaid, which means annual and monthly subscription,
        `POSTPAID` means post-payment, which means billing by volume. The default is `POSTPAID`. The prepaid model only supports
        inter-regional speed limit, and the post-paid model supports inter-regional speed limit and regional export speed limit.
        """
        return pulumi.get(self, "charge_type")

    @charge_type.setter
    def charge_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "charge_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of CCN, and maximum length does not exceed 100 bytes.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the CCN to be queried, and maximum length does not exceed 60 bytes.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def qos(self) -> Optional[pulumi.Input[str]]:
        """
        Service quality of CCN. Valid values: `PT`, `AU`, `AG`. The default is `AU`.
        """
        return pulumi.get(self, "qos")

    @qos.setter
    def qos(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "qos", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Instance tag.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *,
                 bandwidth_limit_type: Optional[pulumi.Input[str]] = None,
                 charge_type: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 qos: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering Instance resources.
        :param pulumi.Input[str] bandwidth_limit_type: The speed limit type. Valid values: `INTER_REGION_LIMIT`, `OUTER_REGION_LIMIT`. `OUTER_REGION_LIMIT` represents the
               regional export speed limit, `INTER_REGION_LIMIT` is the inter-regional speed limit. The default is
               `OUTER_REGION_LIMIT`.
        :param pulumi.Input[str] charge_type: Billing mode. Valid values: `PREPAID`, `POSTPAID`. `PREPAID` means prepaid, which means annual and monthly subscription,
               `POSTPAID` means post-payment, which means billing by volume. The default is `POSTPAID`. The prepaid model only supports
               inter-regional speed limit, and the post-paid model supports inter-regional speed limit and regional export speed limit.
        :param pulumi.Input[str] create_time: Creation time of resource.
        :param pulumi.Input[str] description: Description of CCN, and maximum length does not exceed 100 bytes.
        :param pulumi.Input[int] instance_count: Number of attached instances.
        :param pulumi.Input[str] name: Name of the CCN to be queried, and maximum length does not exceed 60 bytes.
        :param pulumi.Input[str] qos: Service quality of CCN. Valid values: `PT`, `AU`, `AG`. The default is `AU`.
        :param pulumi.Input[str] state: States of instance. Valid values: `ISOLATED`(arrears) and `AVAILABLE`.
        :param pulumi.Input[Mapping[str, Any]] tags: Instance tag.
        """
        if bandwidth_limit_type is not None:
            pulumi.set(__self__, "bandwidth_limit_type", bandwidth_limit_type)
        if charge_type is not None:
            pulumi.set(__self__, "charge_type", charge_type)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_count is not None:
            pulumi.set(__self__, "instance_count", instance_count)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if qos is not None:
            pulumi.set(__self__, "qos", qos)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="bandwidthLimitType")
    def bandwidth_limit_type(self) -> Optional[pulumi.Input[str]]:
        """
        The speed limit type. Valid values: `INTER_REGION_LIMIT`, `OUTER_REGION_LIMIT`. `OUTER_REGION_LIMIT` represents the
        regional export speed limit, `INTER_REGION_LIMIT` is the inter-regional speed limit. The default is
        `OUTER_REGION_LIMIT`.
        """
        return pulumi.get(self, "bandwidth_limit_type")

    @bandwidth_limit_type.setter
    def bandwidth_limit_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bandwidth_limit_type", value)

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> Optional[pulumi.Input[str]]:
        """
        Billing mode. Valid values: `PREPAID`, `POSTPAID`. `PREPAID` means prepaid, which means annual and monthly subscription,
        `POSTPAID` means post-payment, which means billing by volume. The default is `POSTPAID`. The prepaid model only supports
        inter-regional speed limit, and the post-paid model supports inter-regional speed limit and regional export speed limit.
        """
        return pulumi.get(self, "charge_type")

    @charge_type.setter
    def charge_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "charge_type", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of resource.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of CCN, and maximum length does not exceed 100 bytes.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of attached instances.
        """
        return pulumi.get(self, "instance_count")

    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the CCN to be queried, and maximum length does not exceed 60 bytes.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def qos(self) -> Optional[pulumi.Input[str]]:
        """
        Service quality of CCN. Valid values: `PT`, `AU`, `AG`. The default is `AU`.
        """
        return pulumi.get(self, "qos")

    @qos.setter
    def qos(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "qos", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        States of instance. Valid values: `ISOLATED`(arrears) and `AVAILABLE`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Instance tag.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_limit_type: Optional[pulumi.Input[str]] = None,
                 charge_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 qos: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Create a Instance resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bandwidth_limit_type: The speed limit type. Valid values: `INTER_REGION_LIMIT`, `OUTER_REGION_LIMIT`. `OUTER_REGION_LIMIT` represents the
               regional export speed limit, `INTER_REGION_LIMIT` is the inter-regional speed limit. The default is
               `OUTER_REGION_LIMIT`.
        :param pulumi.Input[str] charge_type: Billing mode. Valid values: `PREPAID`, `POSTPAID`. `PREPAID` means prepaid, which means annual and monthly subscription,
               `POSTPAID` means post-payment, which means billing by volume. The default is `POSTPAID`. The prepaid model only supports
               inter-regional speed limit, and the post-paid model supports inter-regional speed limit and regional export speed limit.
        :param pulumi.Input[str] description: Description of CCN, and maximum length does not exceed 100 bytes.
        :param pulumi.Input[str] name: Name of the CCN to be queried, and maximum length does not exceed 60 bytes.
        :param pulumi.Input[str] qos: Service quality of CCN. Valid values: `PT`, `AU`, `AG`. The default is `AU`.
        :param pulumi.Input[Mapping[str, Any]] tags: Instance tag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstanceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Instance resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_limit_type: Optional[pulumi.Input[str]] = None,
                 charge_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 qos: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["bandwidth_limit_type"] = bandwidth_limit_type
            __props__.__dict__["charge_type"] = charge_type
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["qos"] = qos
            __props__.__dict__["tags"] = tags
            __props__.__dict__["create_time"] = None
            __props__.__dict__["instance_count"] = None
            __props__.__dict__["state"] = None
        super(Instance, __self__).__init__(
            'tencentcloud:Ccn/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bandwidth_limit_type: Optional[pulumi.Input[str]] = None,
            charge_type: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            instance_count: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            qos: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bandwidth_limit_type: The speed limit type. Valid values: `INTER_REGION_LIMIT`, `OUTER_REGION_LIMIT`. `OUTER_REGION_LIMIT` represents the
               regional export speed limit, `INTER_REGION_LIMIT` is the inter-regional speed limit. The default is
               `OUTER_REGION_LIMIT`.
        :param pulumi.Input[str] charge_type: Billing mode. Valid values: `PREPAID`, `POSTPAID`. `PREPAID` means prepaid, which means annual and monthly subscription,
               `POSTPAID` means post-payment, which means billing by volume. The default is `POSTPAID`. The prepaid model only supports
               inter-regional speed limit, and the post-paid model supports inter-regional speed limit and regional export speed limit.
        :param pulumi.Input[str] create_time: Creation time of resource.
        :param pulumi.Input[str] description: Description of CCN, and maximum length does not exceed 100 bytes.
        :param pulumi.Input[int] instance_count: Number of attached instances.
        :param pulumi.Input[str] name: Name of the CCN to be queried, and maximum length does not exceed 60 bytes.
        :param pulumi.Input[str] qos: Service quality of CCN. Valid values: `PT`, `AU`, `AG`. The default is `AU`.
        :param pulumi.Input[str] state: States of instance. Valid values: `ISOLATED`(arrears) and `AVAILABLE`.
        :param pulumi.Input[Mapping[str, Any]] tags: Instance tag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceState.__new__(_InstanceState)

        __props__.__dict__["bandwidth_limit_type"] = bandwidth_limit_type
        __props__.__dict__["charge_type"] = charge_type
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["instance_count"] = instance_count
        __props__.__dict__["name"] = name
        __props__.__dict__["qos"] = qos
        __props__.__dict__["state"] = state
        __props__.__dict__["tags"] = tags
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bandwidthLimitType")
    def bandwidth_limit_type(self) -> pulumi.Output[Optional[str]]:
        """
        The speed limit type. Valid values: `INTER_REGION_LIMIT`, `OUTER_REGION_LIMIT`. `OUTER_REGION_LIMIT` represents the
        regional export speed limit, `INTER_REGION_LIMIT` is the inter-regional speed limit. The default is
        `OUTER_REGION_LIMIT`.
        """
        return pulumi.get(self, "bandwidth_limit_type")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> pulumi.Output[Optional[str]]:
        """
        Billing mode. Valid values: `PREPAID`, `POSTPAID`. `PREPAID` means prepaid, which means annual and monthly subscription,
        `POSTPAID` means post-payment, which means billing by volume. The default is `POSTPAID`. The prepaid model only supports
        inter-regional speed limit, and the post-paid model supports inter-regional speed limit and regional export speed limit.
        """
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of CCN, and maximum length does not exceed 100 bytes.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Output[int]:
        """
        Number of attached instances.
        """
        return pulumi.get(self, "instance_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the CCN to be queried, and maximum length does not exceed 60 bytes.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def qos(self) -> pulumi.Output[Optional[str]]:
        """
        Service quality of CCN. Valid values: `PT`, `AU`, `AG`. The default is `AU`.
        """
        return pulumi.get(self, "qos")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        States of instance. Valid values: `ISOLATED`(arrears) and `AVAILABLE`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Instance tag.
        """
        return pulumi.get(self, "tags")

