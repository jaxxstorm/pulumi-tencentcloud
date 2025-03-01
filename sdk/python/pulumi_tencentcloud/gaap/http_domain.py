# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HttpDomainArgs', 'HttpDomain']

@pulumi.input_type
class HttpDomainArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 listener_id: pulumi.Input[str],
                 basic_auth: Optional[pulumi.Input[bool]] = None,
                 basic_auth_id: Optional[pulumi.Input[str]] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gaap_auth: Optional[pulumi.Input[bool]] = None,
                 gaap_auth_id: Optional[pulumi.Input[str]] = None,
                 realserver_auth: Optional[pulumi.Input[bool]] = None,
                 realserver_certificate_domain: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_id: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a HttpDomain resource.
        :param pulumi.Input[str] domain: Forward domain of the layer7 listener.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[bool] basic_auth: Indicates whether basic authentication is enable, default value is `false`.
        :param pulumi.Input[str] basic_auth_id: ID of the basic authentication.
        :param pulumi.Input[str] certificate_id: ID of the server certificate, default value is `default`.
        :param pulumi.Input[str] client_certificate_id: It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_certificate_ids: ID list of the poly client certificate.
        :param pulumi.Input[bool] gaap_auth: Indicates whether SSL certificate authentication is enable, default value is `false`.
        :param pulumi.Input[str] gaap_auth_id: ID of the SSL certificate.
        :param pulumi.Input[bool] realserver_auth: Indicates whether realserver authentication is enable, default value is `false`.
        :param pulumi.Input[str] realserver_certificate_domain: CA certificate domain of the realserver. It has been deprecated.
        :param pulumi.Input[str] realserver_certificate_id: It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realserver_certificate_ids: CA certificate ID list of the realserver.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "listener_id", listener_id)
        if basic_auth is not None:
            pulumi.set(__self__, "basic_auth", basic_auth)
        if basic_auth_id is not None:
            pulumi.set(__self__, "basic_auth_id", basic_auth_id)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if client_certificate_id is not None:
            warnings.warn("""It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead.""", DeprecationWarning)
            pulumi.log.warn("""client_certificate_id is deprecated: It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead.""")
        if client_certificate_id is not None:
            pulumi.set(__self__, "client_certificate_id", client_certificate_id)
        if client_certificate_ids is not None:
            pulumi.set(__self__, "client_certificate_ids", client_certificate_ids)
        if gaap_auth is not None:
            pulumi.set(__self__, "gaap_auth", gaap_auth)
        if gaap_auth_id is not None:
            pulumi.set(__self__, "gaap_auth_id", gaap_auth_id)
        if realserver_auth is not None:
            pulumi.set(__self__, "realserver_auth", realserver_auth)
        if realserver_certificate_domain is not None:
            pulumi.set(__self__, "realserver_certificate_domain", realserver_certificate_domain)
        if realserver_certificate_id is not None:
            warnings.warn("""It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead.""", DeprecationWarning)
            pulumi.log.warn("""realserver_certificate_id is deprecated: It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead.""")
        if realserver_certificate_id is not None:
            pulumi.set(__self__, "realserver_certificate_id", realserver_certificate_id)
        if realserver_certificate_ids is not None:
            pulumi.set(__self__, "realserver_certificate_ids", realserver_certificate_ids)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        Forward domain of the layer7 listener.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

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
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether basic authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "basic_auth")

    @basic_auth.setter
    def basic_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "basic_auth", value)

    @property
    @pulumi.getter(name="basicAuthId")
    def basic_auth_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the basic authentication.
        """
        return pulumi.get(self, "basic_auth_id")

    @basic_auth_id.setter
    def basic_auth_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_id", value)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the server certificate, default value is `default`.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.
        """
        return pulumi.get(self, "client_certificate_id")

    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate_id", value)

    @property
    @pulumi.getter(name="clientCertificateIds")
    def client_certificate_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        ID list of the poly client certificate.
        """
        return pulumi.get(self, "client_certificate_ids")

    @client_certificate_ids.setter
    def client_certificate_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "client_certificate_ids", value)

    @property
    @pulumi.getter(name="gaapAuth")
    def gaap_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether SSL certificate authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "gaap_auth")

    @gaap_auth.setter
    def gaap_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "gaap_auth", value)

    @property
    @pulumi.getter(name="gaapAuthId")
    def gaap_auth_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the SSL certificate.
        """
        return pulumi.get(self, "gaap_auth_id")

    @gaap_auth_id.setter
    def gaap_auth_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gaap_auth_id", value)

    @property
    @pulumi.getter(name="realserverAuth")
    def realserver_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether realserver authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "realserver_auth")

    @realserver_auth.setter
    def realserver_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "realserver_auth", value)

    @property
    @pulumi.getter(name="realserverCertificateDomain")
    def realserver_certificate_domain(self) -> Optional[pulumi.Input[str]]:
        """
        CA certificate domain of the realserver. It has been deprecated.
        """
        return pulumi.get(self, "realserver_certificate_domain")

    @realserver_certificate_domain.setter
    def realserver_certificate_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realserver_certificate_domain", value)

    @property
    @pulumi.getter(name="realserverCertificateId")
    def realserver_certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.
        """
        return pulumi.get(self, "realserver_certificate_id")

    @realserver_certificate_id.setter
    def realserver_certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realserver_certificate_id", value)

    @property
    @pulumi.getter(name="realserverCertificateIds")
    def realserver_certificate_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        CA certificate ID list of the realserver.
        """
        return pulumi.get(self, "realserver_certificate_ids")

    @realserver_certificate_ids.setter
    def realserver_certificate_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "realserver_certificate_ids", value)


@pulumi.input_type
class _HttpDomainState:
    def __init__(__self__, *,
                 basic_auth: Optional[pulumi.Input[bool]] = None,
                 basic_auth_id: Optional[pulumi.Input[str]] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 gaap_auth: Optional[pulumi.Input[bool]] = None,
                 gaap_auth_id: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 realserver_auth: Optional[pulumi.Input[bool]] = None,
                 realserver_certificate_domain: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_id: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering HttpDomain resources.
        :param pulumi.Input[bool] basic_auth: Indicates whether basic authentication is enable, default value is `false`.
        :param pulumi.Input[str] basic_auth_id: ID of the basic authentication.
        :param pulumi.Input[str] certificate_id: ID of the server certificate, default value is `default`.
        :param pulumi.Input[str] client_certificate_id: It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_certificate_ids: ID list of the poly client certificate.
        :param pulumi.Input[str] domain: Forward domain of the layer7 listener.
        :param pulumi.Input[bool] gaap_auth: Indicates whether SSL certificate authentication is enable, default value is `false`.
        :param pulumi.Input[str] gaap_auth_id: ID of the SSL certificate.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[bool] realserver_auth: Indicates whether realserver authentication is enable, default value is `false`.
        :param pulumi.Input[str] realserver_certificate_domain: CA certificate domain of the realserver. It has been deprecated.
        :param pulumi.Input[str] realserver_certificate_id: It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realserver_certificate_ids: CA certificate ID list of the realserver.
        """
        if basic_auth is not None:
            pulumi.set(__self__, "basic_auth", basic_auth)
        if basic_auth_id is not None:
            pulumi.set(__self__, "basic_auth_id", basic_auth_id)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if client_certificate_id is not None:
            warnings.warn("""It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead.""", DeprecationWarning)
            pulumi.log.warn("""client_certificate_id is deprecated: It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead.""")
        if client_certificate_id is not None:
            pulumi.set(__self__, "client_certificate_id", client_certificate_id)
        if client_certificate_ids is not None:
            pulumi.set(__self__, "client_certificate_ids", client_certificate_ids)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if gaap_auth is not None:
            pulumi.set(__self__, "gaap_auth", gaap_auth)
        if gaap_auth_id is not None:
            pulumi.set(__self__, "gaap_auth_id", gaap_auth_id)
        if listener_id is not None:
            pulumi.set(__self__, "listener_id", listener_id)
        if realserver_auth is not None:
            pulumi.set(__self__, "realserver_auth", realserver_auth)
        if realserver_certificate_domain is not None:
            pulumi.set(__self__, "realserver_certificate_domain", realserver_certificate_domain)
        if realserver_certificate_id is not None:
            warnings.warn("""It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead.""", DeprecationWarning)
            pulumi.log.warn("""realserver_certificate_id is deprecated: It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead.""")
        if realserver_certificate_id is not None:
            pulumi.set(__self__, "realserver_certificate_id", realserver_certificate_id)
        if realserver_certificate_ids is not None:
            pulumi.set(__self__, "realserver_certificate_ids", realserver_certificate_ids)

    @property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether basic authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "basic_auth")

    @basic_auth.setter
    def basic_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "basic_auth", value)

    @property
    @pulumi.getter(name="basicAuthId")
    def basic_auth_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the basic authentication.
        """
        return pulumi.get(self, "basic_auth_id")

    @basic_auth_id.setter
    def basic_auth_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_id", value)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the server certificate, default value is `default`.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.
        """
        return pulumi.get(self, "client_certificate_id")

    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate_id", value)

    @property
    @pulumi.getter(name="clientCertificateIds")
    def client_certificate_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        ID list of the poly client certificate.
        """
        return pulumi.get(self, "client_certificate_ids")

    @client_certificate_ids.setter
    def client_certificate_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "client_certificate_ids", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Forward domain of the layer7 listener.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="gaapAuth")
    def gaap_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether SSL certificate authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "gaap_auth")

    @gaap_auth.setter
    def gaap_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "gaap_auth", value)

    @property
    @pulumi.getter(name="gaapAuthId")
    def gaap_auth_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the SSL certificate.
        """
        return pulumi.get(self, "gaap_auth_id")

    @gaap_auth_id.setter
    def gaap_auth_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gaap_auth_id", value)

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
    @pulumi.getter(name="realserverAuth")
    def realserver_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether realserver authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "realserver_auth")

    @realserver_auth.setter
    def realserver_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "realserver_auth", value)

    @property
    @pulumi.getter(name="realserverCertificateDomain")
    def realserver_certificate_domain(self) -> Optional[pulumi.Input[str]]:
        """
        CA certificate domain of the realserver. It has been deprecated.
        """
        return pulumi.get(self, "realserver_certificate_domain")

    @realserver_certificate_domain.setter
    def realserver_certificate_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realserver_certificate_domain", value)

    @property
    @pulumi.getter(name="realserverCertificateId")
    def realserver_certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.
        """
        return pulumi.get(self, "realserver_certificate_id")

    @realserver_certificate_id.setter
    def realserver_certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realserver_certificate_id", value)

    @property
    @pulumi.getter(name="realserverCertificateIds")
    def realserver_certificate_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        CA certificate ID list of the realserver.
        """
        return pulumi.get(self, "realserver_certificate_ids")

    @realserver_certificate_ids.setter
    def realserver_certificate_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "realserver_certificate_ids", value)


class HttpDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 basic_auth: Optional[pulumi.Input[bool]] = None,
                 basic_auth_id: Optional[pulumi.Input[str]] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 gaap_auth: Optional[pulumi.Input[bool]] = None,
                 gaap_auth_id: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 realserver_auth: Optional[pulumi.Input[bool]] = None,
                 realserver_certificate_domain: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_id: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a resource to create a forward domain of layer7 listener.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo_proxy = tencentcloud.gaap.Proxy("fooProxy",
            bandwidth=10,
            concurrent=2,
            access_region="SouthChina",
            realserver_region="NorthChina")
        foo_layer7_listener = tencentcloud.gaap.Layer7Listener("fooLayer7Listener",
            protocol="HTTP",
            port=80,
            proxy_id=foo_proxy.id)
        foo_http_domain = tencentcloud.gaap.HttpDomain("fooHttpDomain",
            listener_id=foo_layer7_listener.id,
            domain="www.qq.com")
        ```

        ## Import

        GAAP http domain can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Gaap/httpDomain:HttpDomain tencentcloud_gaap_http_domain.foo listener-11112222+HTTP+www.qq.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] basic_auth: Indicates whether basic authentication is enable, default value is `false`.
        :param pulumi.Input[str] basic_auth_id: ID of the basic authentication.
        :param pulumi.Input[str] certificate_id: ID of the server certificate, default value is `default`.
        :param pulumi.Input[str] client_certificate_id: It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_certificate_ids: ID list of the poly client certificate.
        :param pulumi.Input[str] domain: Forward domain of the layer7 listener.
        :param pulumi.Input[bool] gaap_auth: Indicates whether SSL certificate authentication is enable, default value is `false`.
        :param pulumi.Input[str] gaap_auth_id: ID of the SSL certificate.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[bool] realserver_auth: Indicates whether realserver authentication is enable, default value is `false`.
        :param pulumi.Input[str] realserver_certificate_domain: CA certificate domain of the realserver. It has been deprecated.
        :param pulumi.Input[str] realserver_certificate_id: It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realserver_certificate_ids: CA certificate ID list of the realserver.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HttpDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a forward domain of layer7 listener.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo_proxy = tencentcloud.gaap.Proxy("fooProxy",
            bandwidth=10,
            concurrent=2,
            access_region="SouthChina",
            realserver_region="NorthChina")
        foo_layer7_listener = tencentcloud.gaap.Layer7Listener("fooLayer7Listener",
            protocol="HTTP",
            port=80,
            proxy_id=foo_proxy.id)
        foo_http_domain = tencentcloud.gaap.HttpDomain("fooHttpDomain",
            listener_id=foo_layer7_listener.id,
            domain="www.qq.com")
        ```

        ## Import

        GAAP http domain can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Gaap/httpDomain:HttpDomain tencentcloud_gaap_http_domain.foo listener-11112222+HTTP+www.qq.com
        ```

        :param str resource_name: The name of the resource.
        :param HttpDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HttpDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 basic_auth: Optional[pulumi.Input[bool]] = None,
                 basic_auth_id: Optional[pulumi.Input[str]] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_id: Optional[pulumi.Input[str]] = None,
                 client_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 gaap_auth: Optional[pulumi.Input[bool]] = None,
                 gaap_auth_id: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 realserver_auth: Optional[pulumi.Input[bool]] = None,
                 realserver_certificate_domain: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_id: Optional[pulumi.Input[str]] = None,
                 realserver_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = HttpDomainArgs.__new__(HttpDomainArgs)

            __props__.__dict__["basic_auth"] = basic_auth
            __props__.__dict__["basic_auth_id"] = basic_auth_id
            __props__.__dict__["certificate_id"] = certificate_id
            if client_certificate_id is not None and not opts.urn:
                warnings.warn("""It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead.""", DeprecationWarning)
                pulumi.log.warn("""client_certificate_id is deprecated: It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead.""")
            __props__.__dict__["client_certificate_id"] = client_certificate_id
            __props__.__dict__["client_certificate_ids"] = client_certificate_ids
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["gaap_auth"] = gaap_auth
            __props__.__dict__["gaap_auth_id"] = gaap_auth_id
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            __props__.__dict__["realserver_auth"] = realserver_auth
            __props__.__dict__["realserver_certificate_domain"] = realserver_certificate_domain
            if realserver_certificate_id is not None and not opts.urn:
                warnings.warn("""It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead.""", DeprecationWarning)
                pulumi.log.warn("""realserver_certificate_id is deprecated: It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead.""")
            __props__.__dict__["realserver_certificate_id"] = realserver_certificate_id
            __props__.__dict__["realserver_certificate_ids"] = realserver_certificate_ids
        super(HttpDomain, __self__).__init__(
            'tencentcloud:Gaap/httpDomain:HttpDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            basic_auth: Optional[pulumi.Input[bool]] = None,
            basic_auth_id: Optional[pulumi.Input[str]] = None,
            certificate_id: Optional[pulumi.Input[str]] = None,
            client_certificate_id: Optional[pulumi.Input[str]] = None,
            client_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            gaap_auth: Optional[pulumi.Input[bool]] = None,
            gaap_auth_id: Optional[pulumi.Input[str]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            realserver_auth: Optional[pulumi.Input[bool]] = None,
            realserver_certificate_domain: Optional[pulumi.Input[str]] = None,
            realserver_certificate_id: Optional[pulumi.Input[str]] = None,
            realserver_certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'HttpDomain':
        """
        Get an existing HttpDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] basic_auth: Indicates whether basic authentication is enable, default value is `false`.
        :param pulumi.Input[str] basic_auth_id: ID of the basic authentication.
        :param pulumi.Input[str] certificate_id: ID of the server certificate, default value is `default`.
        :param pulumi.Input[str] client_certificate_id: It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_certificate_ids: ID list of the poly client certificate.
        :param pulumi.Input[str] domain: Forward domain of the layer7 listener.
        :param pulumi.Input[bool] gaap_auth: Indicates whether SSL certificate authentication is enable, default value is `false`.
        :param pulumi.Input[str] gaap_auth_id: ID of the SSL certificate.
        :param pulumi.Input[str] listener_id: ID of the layer7 listener.
        :param pulumi.Input[bool] realserver_auth: Indicates whether realserver authentication is enable, default value is `false`.
        :param pulumi.Input[str] realserver_certificate_domain: CA certificate domain of the realserver. It has been deprecated.
        :param pulumi.Input[str] realserver_certificate_id: It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] realserver_certificate_ids: CA certificate ID list of the realserver.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HttpDomainState.__new__(_HttpDomainState)

        __props__.__dict__["basic_auth"] = basic_auth
        __props__.__dict__["basic_auth_id"] = basic_auth_id
        __props__.__dict__["certificate_id"] = certificate_id
        __props__.__dict__["client_certificate_id"] = client_certificate_id
        __props__.__dict__["client_certificate_ids"] = client_certificate_ids
        __props__.__dict__["domain"] = domain
        __props__.__dict__["gaap_auth"] = gaap_auth
        __props__.__dict__["gaap_auth_id"] = gaap_auth_id
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["realserver_auth"] = realserver_auth
        __props__.__dict__["realserver_certificate_domain"] = realserver_certificate_domain
        __props__.__dict__["realserver_certificate_id"] = realserver_certificate_id
        __props__.__dict__["realserver_certificate_ids"] = realserver_certificate_ids
        return HttpDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether basic authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "basic_auth")

    @property
    @pulumi.getter(name="basicAuthId")
    def basic_auth_id(self) -> pulumi.Output[str]:
        """
        ID of the basic authentication.
        """
        return pulumi.get(self, "basic_auth_id")

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the server certificate, default value is `default`.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> pulumi.Output[str]:
        """
        It has been deprecated from version 1.26.0. Set `client_certificate_ids` instead. ID of the client certificate, default value is `default`.
        """
        return pulumi.get(self, "client_certificate_id")

    @property
    @pulumi.getter(name="clientCertificateIds")
    def client_certificate_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        ID list of the poly client certificate.
        """
        return pulumi.get(self, "client_certificate_ids")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        Forward domain of the layer7 listener.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="gaapAuth")
    def gaap_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether SSL certificate authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "gaap_auth")

    @property
    @pulumi.getter(name="gaapAuthId")
    def gaap_auth_id(self) -> pulumi.Output[str]:
        """
        ID of the SSL certificate.
        """
        return pulumi.get(self, "gaap_auth_id")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        ID of the layer7 listener.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter(name="realserverAuth")
    def realserver_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether realserver authentication is enable, default value is `false`.
        """
        return pulumi.get(self, "realserver_auth")

    @property
    @pulumi.getter(name="realserverCertificateDomain")
    def realserver_certificate_domain(self) -> pulumi.Output[str]:
        """
        CA certificate domain of the realserver. It has been deprecated.
        """
        return pulumi.get(self, "realserver_certificate_domain")

    @property
    @pulumi.getter(name="realserverCertificateId")
    def realserver_certificate_id(self) -> pulumi.Output[str]:
        """
        It has been deprecated from version 1.28.0. Set `realserver_certificate_ids` instead. CA certificate ID of the realserver.
        """
        return pulumi.get(self, "realserver_certificate_id")

    @property
    @pulumi.getter(name="realserverCertificateIds")
    def realserver_certificate_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        CA certificate ID list of the realserver.
        """
        return pulumi.get(self, "realserver_certificate_ids")

