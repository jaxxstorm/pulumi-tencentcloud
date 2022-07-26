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

__all__ = ['ProcedureTemplateArgs', 'ProcedureTemplate']

@pulumi.input_type
class ProcedureTemplateArgs:
    def __init__(__self__, *,
                 comment: Optional[pulumi.Input[str]] = None,
                 media_process_task: Optional[pulumi.Input['ProcedureTemplateMediaProcessTaskArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sub_app_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ProcedureTemplate resource.
        :param pulumi.Input[str] comment: Template description. Length limit: 256 characters.
        :param pulumi.Input['ProcedureTemplateMediaProcessTaskArgs'] media_process_task: Parameter of video processing task.
        :param pulumi.Input[str] name: Task flow name (up to 20 characters).
        :param pulumi.Input[int] sub_app_id: Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this
               field; otherwise, leave it empty.
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if media_process_task is not None:
            pulumi.set(__self__, "media_process_task", media_process_task)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sub_app_id is not None:
            pulumi.set(__self__, "sub_app_id", sub_app_id)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Template description. Length limit: 256 characters.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="mediaProcessTask")
    def media_process_task(self) -> Optional[pulumi.Input['ProcedureTemplateMediaProcessTaskArgs']]:
        """
        Parameter of video processing task.
        """
        return pulumi.get(self, "media_process_task")

    @media_process_task.setter
    def media_process_task(self, value: Optional[pulumi.Input['ProcedureTemplateMediaProcessTaskArgs']]):
        pulumi.set(self, "media_process_task", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Task flow name (up to 20 characters).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="subAppId")
    def sub_app_id(self) -> Optional[pulumi.Input[int]]:
        """
        Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this
        field; otherwise, leave it empty.
        """
        return pulumi.get(self, "sub_app_id")

    @sub_app_id.setter
    def sub_app_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sub_app_id", value)


@pulumi.input_type
class _ProcedureTemplateState:
    def __init__(__self__, *,
                 comment: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 media_process_task: Optional[pulumi.Input['ProcedureTemplateMediaProcessTaskArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sub_app_id: Optional[pulumi.Input[int]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProcedureTemplate resources.
        :param pulumi.Input[str] comment: Template description. Length limit: 256 characters.
        :param pulumi.Input[str] create_time: Creation time of template in ISO date format.
        :param pulumi.Input['ProcedureTemplateMediaProcessTaskArgs'] media_process_task: Parameter of video processing task.
        :param pulumi.Input[str] name: Task flow name (up to 20 characters).
        :param pulumi.Input[int] sub_app_id: Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this
               field; otherwise, leave it empty.
        :param pulumi.Input[str] update_time: Last modified time of template in ISO date format.
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if media_process_task is not None:
            pulumi.set(__self__, "media_process_task", media_process_task)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sub_app_id is not None:
            pulumi.set(__self__, "sub_app_id", sub_app_id)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Template description. Length limit: 256 characters.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of template in ISO date format.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="mediaProcessTask")
    def media_process_task(self) -> Optional[pulumi.Input['ProcedureTemplateMediaProcessTaskArgs']]:
        """
        Parameter of video processing task.
        """
        return pulumi.get(self, "media_process_task")

    @media_process_task.setter
    def media_process_task(self, value: Optional[pulumi.Input['ProcedureTemplateMediaProcessTaskArgs']]):
        pulumi.set(self, "media_process_task", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Task flow name (up to 20 characters).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="subAppId")
    def sub_app_id(self) -> Optional[pulumi.Input[int]]:
        """
        Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this
        field; otherwise, leave it empty.
        """
        return pulumi.get(self, "sub_app_id")

    @sub_app_id.setter
    def sub_app_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sub_app_id", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Last modified time of template in ISO date format.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class ProcedureTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 media_process_task: Optional[pulumi.Input[pulumi.InputType['ProcedureTemplateMediaProcessTaskArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sub_app_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a ProcedureTemplate resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: Template description. Length limit: 256 characters.
        :param pulumi.Input[pulumi.InputType['ProcedureTemplateMediaProcessTaskArgs']] media_process_task: Parameter of video processing task.
        :param pulumi.Input[str] name: Task flow name (up to 20 characters).
        :param pulumi.Input[int] sub_app_id: Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this
               field; otherwise, leave it empty.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProcedureTemplateArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ProcedureTemplate resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ProcedureTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProcedureTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 media_process_task: Optional[pulumi.Input[pulumi.InputType['ProcedureTemplateMediaProcessTaskArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sub_app_id: Optional[pulumi.Input[int]] = None,
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
            __props__ = ProcedureTemplateArgs.__new__(ProcedureTemplateArgs)

            __props__.__dict__["comment"] = comment
            __props__.__dict__["media_process_task"] = media_process_task
            __props__.__dict__["name"] = name
            __props__.__dict__["sub_app_id"] = sub_app_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        super(ProcedureTemplate, __self__).__init__(
            'tencentcloud:Vod/procedureTemplate:ProcedureTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            comment: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            media_process_task: Optional[pulumi.Input[pulumi.InputType['ProcedureTemplateMediaProcessTaskArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sub_app_id: Optional[pulumi.Input[int]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'ProcedureTemplate':
        """
        Get an existing ProcedureTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: Template description. Length limit: 256 characters.
        :param pulumi.Input[str] create_time: Creation time of template in ISO date format.
        :param pulumi.Input[pulumi.InputType['ProcedureTemplateMediaProcessTaskArgs']] media_process_task: Parameter of video processing task.
        :param pulumi.Input[str] name: Task flow name (up to 20 characters).
        :param pulumi.Input[int] sub_app_id: Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this
               field; otherwise, leave it empty.
        :param pulumi.Input[str] update_time: Last modified time of template in ISO date format.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProcedureTemplateState.__new__(_ProcedureTemplateState)

        __props__.__dict__["comment"] = comment
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["media_process_task"] = media_process_task
        __props__.__dict__["name"] = name
        __props__.__dict__["sub_app_id"] = sub_app_id
        __props__.__dict__["update_time"] = update_time
        return ProcedureTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Template description. Length limit: 256 characters.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of template in ISO date format.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="mediaProcessTask")
    def media_process_task(self) -> pulumi.Output[Optional['outputs.ProcedureTemplateMediaProcessTask']]:
        """
        Parameter of video processing task.
        """
        return pulumi.get(self, "media_process_task")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Task flow name (up to 20 characters).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subAppId")
    def sub_app_id(self) -> pulumi.Output[Optional[int]]:
        """
        Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this
        field; otherwise, leave it empty.
        """
        return pulumi.get(self, "sub_app_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Last modified time of template in ISO date format.
        """
        return pulumi.get(self, "update_time")

