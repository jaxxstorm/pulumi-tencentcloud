# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 type: pulumi.Input[str],
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] content: Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.
        :param pulumi.Input[str] type: Type of the certificate. Valid value: `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`. `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.
        :param pulumi.Input[str] key: Key of the `SSL` certificate.
        :param pulumi.Input[str] name: Name of the certificate.
        """
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "type", type)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of the certificate. Valid value: `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`. `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Key of the `SSL` certificate.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the certificate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CertificateState:
    def __init__(__self__, *,
                 begin_time: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 issuer_cn: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subject_cn: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Certificate resources.
        :param pulumi.Input[str] begin_time: Beginning time of the certificate.
        :param pulumi.Input[str] content: Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.
        :param pulumi.Input[str] create_time: Creation time of the certificate.
        :param pulumi.Input[str] end_time: Ending time of the certificate.
        :param pulumi.Input[str] issuer_cn: Issuer name of the certificate.
        :param pulumi.Input[str] key: Key of the `SSL` certificate.
        :param pulumi.Input[str] name: Name of the certificate.
        :param pulumi.Input[str] subject_cn: Subject name of the certificate.
        :param pulumi.Input[str] type: Type of the certificate. Valid value: `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`. `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.
        """
        if begin_time is not None:
            pulumi.set(__self__, "begin_time", begin_time)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if issuer_cn is not None:
            pulumi.set(__self__, "issuer_cn", issuer_cn)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subject_cn is not None:
            pulumi.set(__self__, "subject_cn", subject_cn)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="beginTime")
    def begin_time(self) -> Optional[pulumi.Input[str]]:
        """
        Beginning time of the certificate.
        """
        return pulumi.get(self, "begin_time")

    @begin_time.setter
    def begin_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "begin_time", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of the certificate.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        Ending time of the certificate.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter(name="issuerCn")
    def issuer_cn(self) -> Optional[pulumi.Input[str]]:
        """
        Issuer name of the certificate.
        """
        return pulumi.get(self, "issuer_cn")

    @issuer_cn.setter
    def issuer_cn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer_cn", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Key of the `SSL` certificate.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the certificate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="subjectCn")
    def subject_cn(self) -> Optional[pulumi.Input[str]]:
        """
        Subject name of the certificate.
        """
        return pulumi.get(self, "subject_cn")

    @subject_cn.setter
    def subject_cn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject_cn", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the certificate. Valid value: `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`. `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to create a certificate of GAAP.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.gaap.Certificate("foo",
            content="test:tx2KGdo3zJg/.",
            type="BASIC")
        ```

        ## Import

        GAAP certificate can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Gaap/certificate:Certificate tencentcloud_gaap_certificate.foo cert-d5y6ei3b
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.
        :param pulumi.Input[str] key: Key of the `SSL` certificate.
        :param pulumi.Input[str] name: Name of the certificate.
        :param pulumi.Input[str] type: Type of the certificate. Valid value: `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`. `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a certificate of GAAP.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.gaap.Certificate("foo",
            content="test:tx2KGdo3zJg/.",
            type="BASIC")
        ```

        ## Import

        GAAP certificate can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Gaap/certificate:Certificate tencentcloud_gaap_certificate.foo cert-d5y6ei3b
        ```

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = CertificateArgs.__new__(CertificateArgs)

            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            __props__.__dict__["key"] = key
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["begin_time"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["end_time"] = None
            __props__.__dict__["issuer_cn"] = None
            __props__.__dict__["subject_cn"] = None
        super(Certificate, __self__).__init__(
            'tencentcloud:Gaap/certificate:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            begin_time: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            end_time: Optional[pulumi.Input[str]] = None,
            issuer_cn: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            subject_cn: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] begin_time: Beginning time of the certificate.
        :param pulumi.Input[str] content: Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.
        :param pulumi.Input[str] create_time: Creation time of the certificate.
        :param pulumi.Input[str] end_time: Ending time of the certificate.
        :param pulumi.Input[str] issuer_cn: Issuer name of the certificate.
        :param pulumi.Input[str] key: Key of the `SSL` certificate.
        :param pulumi.Input[str] name: Name of the certificate.
        :param pulumi.Input[str] subject_cn: Subject name of the certificate.
        :param pulumi.Input[str] type: Type of the certificate. Valid value: `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`. `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CertificateState.__new__(_CertificateState)

        __props__.__dict__["begin_time"] = begin_time
        __props__.__dict__["content"] = content
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["end_time"] = end_time
        __props__.__dict__["issuer_cn"] = issuer_cn
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        __props__.__dict__["subject_cn"] = subject_cn
        __props__.__dict__["type"] = type
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="beginTime")
    def begin_time(self) -> pulumi.Output[str]:
        """
        Beginning time of the certificate.
        """
        return pulumi.get(self, "begin_time")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of the certificate.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        Ending time of the certificate.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="issuerCn")
    def issuer_cn(self) -> pulumi.Output[str]:
        """
        Issuer name of the certificate.
        """
        return pulumi.get(self, "issuer_cn")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        Key of the `SSL` certificate.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the certificate.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subjectCn")
    def subject_cn(self) -> pulumi.Output[str]:
        """
        Subject name of the certificate.
        """
        return pulumi.get(self, "subject_cn")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the certificate. Valid value: `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`. `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.
        """
        return pulumi.get(self, "type")

