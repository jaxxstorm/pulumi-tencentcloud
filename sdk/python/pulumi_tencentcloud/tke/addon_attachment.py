# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AddonAttachmentArgs', 'AddonAttachment']

@pulumi.input_type
class AddonAttachmentArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 request_body: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AddonAttachment resource.
        :param pulumi.Input[str] cluster_id: ID of cluster.
        :param pulumi.Input[str] name: Name of addon.
        :param pulumi.Input[str] request_body: Serialized json string as request body of addon spec. If set, will ignore `version` and `values`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Values the addon passthroughs. Conflict with `request_body`.
        :param pulumi.Input[str] version: Addon version, default latest version. Conflict with `request_body`.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if request_body is not None:
            pulumi.set(__self__, "request_body", request_body)
        if values is not None:
            pulumi.set(__self__, "values", values)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        ID of cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of addon.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> Optional[pulumi.Input[str]]:
        """
        Serialized json string as request body of addon spec. If set, will ignore `version` and `values`.
        """
        return pulumi.get(self, "request_body")

    @request_body.setter
    def request_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_body", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Values the addon passthroughs. Conflict with `request_body`.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Addon version, default latest version. Conflict with `request_body`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class _AddonAttachmentState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 request_body: Optional[pulumi.Input[str]] = None,
                 response_body: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AddonAttachment resources.
        :param pulumi.Input[str] cluster_id: ID of cluster.
        :param pulumi.Input[str] name: Name of addon.
        :param pulumi.Input[str] request_body: Serialized json string as request body of addon spec. If set, will ignore `version` and `values`.
        :param pulumi.Input[str] response_body: Addon response body.
        :param pulumi.Input[Mapping[str, Any]] status: Addon current status.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Values the addon passthroughs. Conflict with `request_body`.
        :param pulumi.Input[str] version: Addon version, default latest version. Conflict with `request_body`.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if request_body is not None:
            pulumi.set(__self__, "request_body", request_body)
        if response_body is not None:
            pulumi.set(__self__, "response_body", response_body)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if values is not None:
            pulumi.set(__self__, "values", values)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of addon.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> Optional[pulumi.Input[str]]:
        """
        Serialized json string as request body of addon spec. If set, will ignore `version` and `values`.
        """
        return pulumi.get(self, "request_body")

    @request_body.setter
    def request_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_body", value)

    @property
    @pulumi.getter(name="responseBody")
    def response_body(self) -> Optional[pulumi.Input[str]]:
        """
        Addon response body.
        """
        return pulumi.get(self, "response_body")

    @response_body.setter
    def response_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "response_body", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Addon current status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Values the addon passthroughs. Conflict with `request_body`.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Addon version, default latest version. Conflict with `request_body`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class AddonAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 request_body: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AddonAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: ID of cluster.
        :param pulumi.Input[str] name: Name of addon.
        :param pulumi.Input[str] request_body: Serialized json string as request body of addon spec. If set, will ignore `version` and `values`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Values the addon passthroughs. Conflict with `request_body`.
        :param pulumi.Input[str] version: Addon version, default latest version. Conflict with `request_body`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AddonAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AddonAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AddonAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddonAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 request_body: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
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
            __props__ = AddonAttachmentArgs.__new__(AddonAttachmentArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["name"] = name
            __props__.__dict__["request_body"] = request_body
            __props__.__dict__["values"] = values
            __props__.__dict__["version"] = version
            __props__.__dict__["response_body"] = None
            __props__.__dict__["status"] = None
        super(AddonAttachment, __self__).__init__(
            'tencentcloud:Tke/addonAttachment:AddonAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            request_body: Optional[pulumi.Input[str]] = None,
            response_body: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'AddonAttachment':
        """
        Get an existing AddonAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: ID of cluster.
        :param pulumi.Input[str] name: Name of addon.
        :param pulumi.Input[str] request_body: Serialized json string as request body of addon spec. If set, will ignore `version` and `values`.
        :param pulumi.Input[str] response_body: Addon response body.
        :param pulumi.Input[Mapping[str, Any]] status: Addon current status.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Values the addon passthroughs. Conflict with `request_body`.
        :param pulumi.Input[str] version: Addon version, default latest version. Conflict with `request_body`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AddonAttachmentState.__new__(_AddonAttachmentState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["name"] = name
        __props__.__dict__["request_body"] = request_body
        __props__.__dict__["response_body"] = response_body
        __props__.__dict__["status"] = status
        __props__.__dict__["values"] = values
        __props__.__dict__["version"] = version
        return AddonAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        ID of cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of addon.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> pulumi.Output[Optional[str]]:
        """
        Serialized json string as request body of addon spec. If set, will ignore `version` and `values`.
        """
        return pulumi.get(self, "request_body")

    @property
    @pulumi.getter(name="responseBody")
    def response_body(self) -> pulumi.Output[str]:
        """
        Addon response body.
        """
        return pulumi.get(self, "response_body")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Addon current status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def values(self) -> pulumi.Output[Sequence[str]]:
        """
        Values the addon passthroughs. Conflict with `request_body`.
        """
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Addon version, default latest version. Conflict with `request_body`.
        """
        return pulumi.get(self, "version")

