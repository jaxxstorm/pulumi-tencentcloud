# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['LogSetArgs', 'LogSet']

@pulumi.input_type
class LogSetArgs:
    def __init__(__self__, *,
                 period: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a LogSet resource.
        :param pulumi.Input[int] period: Logset retention period in days. Maximun value is `90`.
        """
        if period is not None:
            pulumi.set(__self__, "period", period)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[int]]:
        """
        Logset retention period in days. Maximun value is `90`.
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "period", value)


@pulumi.input_type
class _LogSetState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 topic_count: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LogSet resources.
        :param pulumi.Input[str] create_time: Logset creation time.
        :param pulumi.Input[str] name: Logset name, which unique and fixed `clb_logset` among all CLS logsets.
        :param pulumi.Input[int] period: Logset retention period in days. Maximun value is `90`.
        :param pulumi.Input[str] topic_count: Number of log topics in logset.
        """
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if topic_count is not None:
            pulumi.set(__self__, "topic_count", topic_count)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Logset creation time.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Logset name, which unique and fixed `clb_logset` among all CLS logsets.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[int]]:
        """
        Logset retention period in days. Maximun value is `90`.
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="topicCount")
    def topic_count(self) -> Optional[pulumi.Input[str]]:
        """
        Number of log topics in logset.
        """
        return pulumi.get(self, "topic_count")

    @topic_count.setter
    def topic_count(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_count", value)


class LogSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a resource to create an exclusive CLB Logset.

        ## Import

        CLB log set can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Clb/logSet:LogSet foo 4eb9e3a8-9c42-4b32-9ddf-e215e9c92764
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] period: Logset retention period in days. Maximun value is `90`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[LogSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create an exclusive CLB Logset.

        ## Import

        CLB log set can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Clb/logSet:LogSet foo 4eb9e3a8-9c42-4b32-9ddf-e215e9c92764
        ```

        :param str resource_name: The name of the resource.
        :param LogSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 period: Optional[pulumi.Input[int]] = None,
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
            __props__ = LogSetArgs.__new__(LogSetArgs)

            __props__.__dict__["period"] = period
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["topic_count"] = None
        super(LogSet, __self__).__init__(
            'tencentcloud:Clb/logSet:LogSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            period: Optional[pulumi.Input[int]] = None,
            topic_count: Optional[pulumi.Input[str]] = None) -> 'LogSet':
        """
        Get an existing LogSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Logset creation time.
        :param pulumi.Input[str] name: Logset name, which unique and fixed `clb_logset` among all CLS logsets.
        :param pulumi.Input[int] period: Logset retention period in days. Maximun value is `90`.
        :param pulumi.Input[str] topic_count: Number of log topics in logset.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogSetState.__new__(_LogSetState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["name"] = name
        __props__.__dict__["period"] = period
        __props__.__dict__["topic_count"] = topic_count
        return LogSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Logset creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Logset name, which unique and fixed `clb_logset` among all CLS logsets.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[int]]:
        """
        Logset retention period in days. Maximun value is `90`.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="topicCount")
    def topic_count(self) -> pulumi.Output[str]:
        """
        Number of log topics in logset.
        """
        return pulumi.get(self, "topic_count")

