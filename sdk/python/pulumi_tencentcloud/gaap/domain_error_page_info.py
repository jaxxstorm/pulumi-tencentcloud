# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DomainErrorPageInfoArgs', 'DomainErrorPageInfo']

@pulumi.input_type
class DomainErrorPageInfoArgs:
    def __init__(__self__, *,
                 body: pulumi.Input[str],
                 domain: pulumi.Input[str],
                 error_codes: pulumi.Input[Sequence[pulumi.Input[int]]],
                 listener_id: pulumi.Input[str],
                 clear_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 new_error_code: Optional[pulumi.Input[int]] = None,
                 set_headers: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a DomainErrorPageInfo resource.
        :param pulumi.Input[str] body: New response body.
        :param pulumi.Input[str] domain: HTTP domain.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] error_codes: Original error codes.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] clear_headers: Response headers to be removed.
        :param pulumi.Input[int] new_error_code: New error code.
        :param pulumi.Input[Mapping[str, Any]] set_headers: Response headers to be set.
        """
        pulumi.set(__self__, "body", body)
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "error_codes", error_codes)
        pulumi.set(__self__, "listener_id", listener_id)
        if clear_headers is not None:
            pulumi.set(__self__, "clear_headers", clear_headers)
        if new_error_code is not None:
            pulumi.set(__self__, "new_error_code", new_error_code)
        if set_headers is not None:
            pulumi.set(__self__, "set_headers", set_headers)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[str]:
        """
        New response body.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[str]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        HTTP domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="errorCodes")
    def error_codes(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Original error codes.
        """
        return pulumi.get(self, "error_codes")

    @error_codes.setter
    def error_codes(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "error_codes", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        """
        ID of the layer7 listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="clearHeaders")
    def clear_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Response headers to be removed.
        """
        return pulumi.get(self, "clear_headers")

    @clear_headers.setter
    def clear_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "clear_headers", value)

    @property
    @pulumi.getter(name="newErrorCode")
    def new_error_code(self) -> Optional[pulumi.Input[int]]:
        """
        New error code.
        """
        return pulumi.get(self, "new_error_code")

    @new_error_code.setter
    def new_error_code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "new_error_code", value)

    @property
    @pulumi.getter(name="setHeaders")
    def set_headers(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Response headers to be set.
        """
        return pulumi.get(self, "set_headers")

    @set_headers.setter
    def set_headers(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "set_headers", value)


@pulumi.input_type
class _DomainErrorPageInfoState:
    def __init__(__self__, *,
                 body: Optional[pulumi.Input[str]] = None,
                 clear_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 error_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 new_error_code: Optional[pulumi.Input[int]] = None,
                 set_headers: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering DomainErrorPageInfo resources.
        :param pulumi.Input[str] body: New response body.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] clear_headers: Response headers to be removed.
        :param pulumi.Input[str] domain: HTTP domain.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] error_codes: Original error codes.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[int] new_error_code: New error code.
        :param pulumi.Input[Mapping[str, Any]] set_headers: Response headers to be set.
        """
        if body is not None:
            pulumi.set(__self__, "body", body)
        if clear_headers is not None:
            pulumi.set(__self__, "clear_headers", clear_headers)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if error_codes is not None:
            pulumi.set(__self__, "error_codes", error_codes)
        if listener_id is not None:
            pulumi.set(__self__, "listener_id", listener_id)
        if new_error_code is not None:
            pulumi.set(__self__, "new_error_code", new_error_code)
        if set_headers is not None:
            pulumi.set(__self__, "set_headers", set_headers)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        New response body.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="clearHeaders")
    def clear_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Response headers to be removed.
        """
        return pulumi.get(self, "clear_headers")

    @clear_headers.setter
    def clear_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "clear_headers", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        HTTP domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="errorCodes")
    def error_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Original error codes.
        """
        return pulumi.get(self, "error_codes")

    @error_codes.setter
    def error_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "error_codes", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the layer7 listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="newErrorCode")
    def new_error_code(self) -> Optional[pulumi.Input[int]]:
        """
        New error code.
        """
        return pulumi.get(self, "new_error_code")

    @new_error_code.setter
    def new_error_code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "new_error_code", value)

    @property
    @pulumi.getter(name="setHeaders")
    def set_headers(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Response headers to be set.
        """
        return pulumi.get(self, "set_headers")

    @set_headers.setter
    def set_headers(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "set_headers", value)


class DomainErrorPageInfo(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 clear_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 error_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 new_error_code: Optional[pulumi.Input[int]] = None,
                 set_headers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Create a DomainErrorPageInfo resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: New response body.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] clear_headers: Response headers to be removed.
        :param pulumi.Input[str] domain: HTTP domain.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] error_codes: Original error codes.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[int] new_error_code: New error code.
        :param pulumi.Input[Mapping[str, Any]] set_headers: Response headers to be set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainErrorPageInfoArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DomainErrorPageInfo resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DomainErrorPageInfoArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainErrorPageInfoArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 clear_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 error_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 new_error_code: Optional[pulumi.Input[int]] = None,
                 set_headers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = DomainErrorPageInfoArgs.__new__(DomainErrorPageInfoArgs)

            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
            __props__.__dict__["clear_headers"] = clear_headers
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            if error_codes is None and not opts.urn:
                raise TypeError("Missing required property 'error_codes'")
            __props__.__dict__["error_codes"] = error_codes
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            __props__.__dict__["new_error_code"] = new_error_code
            __props__.__dict__["set_headers"] = set_headers
        super(DomainErrorPageInfo, __self__).__init__(
            'tencentcloud:Gaap/domainErrorPageInfo:DomainErrorPageInfo',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            body: Optional[pulumi.Input[str]] = None,
            clear_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            error_codes: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            new_error_code: Optional[pulumi.Input[int]] = None,
            set_headers: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'DomainErrorPageInfo':
        """
        Get an existing DomainErrorPageInfo resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: New response body.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] clear_headers: Response headers to be removed.
        :param pulumi.Input[str] domain: HTTP domain.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] error_codes: Original error codes.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[int] new_error_code: New error code.
        :param pulumi.Input[Mapping[str, Any]] set_headers: Response headers to be set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainErrorPageInfoState.__new__(_DomainErrorPageInfoState)

        __props__.__dict__["body"] = body
        __props__.__dict__["clear_headers"] = clear_headers
        __props__.__dict__["domain"] = domain
        __props__.__dict__["error_codes"] = error_codes
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["new_error_code"] = new_error_code
        __props__.__dict__["set_headers"] = set_headers
        return DomainErrorPageInfo(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        New response body.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="clearHeaders")
    def clear_headers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Response headers to be removed.
        """
        return pulumi.get(self, "clear_headers")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        HTTP domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="errorCodes")
    def error_codes(self) -> pulumi.Output[Sequence[int]]:
        """
        Original error codes.
        """
        return pulumi.get(self, "error_codes")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        ID of the layer7 listener.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter(name="newErrorCode")
    def new_error_code(self) -> pulumi.Output[Optional[int]]:
        """
        New error code.
        """
        return pulumi.get(self, "new_error_code")

    @property
    @pulumi.getter(name="setHeaders")
    def set_headers(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Response headers to be set.
        """
        return pulumi.get(self, "set_headers")

