# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 assume_role: Optional[pulumi.Input['ProviderAssumeRoleArgs']] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input['ProviderAssumeRoleArgs'] assume_role: The `assume_role` block. If provided, terraform will attempt to assume this role using the supplied credentials.
        :param pulumi.Input[str] domain: The root domain of the API request, Default is `tencentcloudapi.com`.
        :param pulumi.Input[str] protocol: The protocol of the API request. Valid values: `HTTP` and `HTTPS`. Default is `HTTPS`.
        :param pulumi.Input[str] region: This is the TencentCloud region. It must be provided, but it can also be sourced from the `TENCENTCLOUD_REGION`
               environment variables. The default input value is ap-guangzhou.
        :param pulumi.Input[str] secret_id: This is the TencentCloud access key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_ID`
               environment variable.
        :param pulumi.Input[str] secret_key: This is the TencentCloud secret key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_KEY`
               environment variable.
        :param pulumi.Input[str] security_token: TencentCloud Security Token of temporary access credentials. It can be sourced from the `TENCENTCLOUD_SECURITY_TOKEN`
               environment variable. Notice: for supported products, please refer to: [temporary key supported
               products](https://intl.cloud.tencent.com/document/product/598/10588).
        """
        if assume_role is not None:
            pulumi.set(__self__, "assume_role", assume_role)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if region is None:
            region = _utilities.get_env('TENCENTCLOUD_REGION')
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secret_id is None:
            secret_id = _utilities.get_env('TENCENTCLOUD_SECRET_ID')
        if secret_id is not None:
            pulumi.set(__self__, "secret_id", secret_id)
        if secret_key is None:
            secret_key = _utilities.get_env('TENCENTCLOUD_SECRET_KEY')
        if secret_key is not None:
            pulumi.set(__self__, "secret_key", secret_key)
        if security_token is None:
            security_token = _utilities.get_env('TENCENTCLOUD_SECURITY_TOKEN')
        if security_token is not None:
            pulumi.set(__self__, "security_token", security_token)

    @property
    @pulumi.getter(name="assumeRole")
    def assume_role(self) -> Optional[pulumi.Input['ProviderAssumeRoleArgs']]:
        """
        The `assume_role` block. If provided, terraform will attempt to assume this role using the supplied credentials.
        """
        return pulumi.get(self, "assume_role")

    @assume_role.setter
    def assume_role(self, value: Optional[pulumi.Input['ProviderAssumeRoleArgs']]):
        pulumi.set(self, "assume_role", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The root domain of the API request, Default is `tencentcloudapi.com`.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol of the API request. Valid values: `HTTP` and `HTTPS`. Default is `HTTPS`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        This is the TencentCloud region. It must be provided, but it can also be sourced from the `TENCENTCLOUD_REGION`
        environment variables. The default input value is ap-guangzhou.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[pulumi.Input[str]]:
        """
        This is the TencentCloud access key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_ID`
        environment variable.
        """
        return pulumi.get(self, "secret_id")

    @secret_id.setter
    def secret_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_id", value)

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        This is the TencentCloud secret key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_KEY`
        environment variable.
        """
        return pulumi.get(self, "secret_key")

    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_key", value)

    @property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[pulumi.Input[str]]:
        """
        TencentCloud Security Token of temporary access credentials. It can be sourced from the `TENCENTCLOUD_SECURITY_TOKEN`
        environment variable. Notice: for supported products, please refer to: [temporary key supported
        products](https://intl.cloud.tencent.com/document/product/598/10588).
        """
        return pulumi.get(self, "security_token")

    @security_token.setter
    def security_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_token", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assume_role: Optional[pulumi.Input[pulumi.InputType['ProviderAssumeRoleArgs']]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the tencentcloud package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ProviderAssumeRoleArgs']] assume_role: The `assume_role` block. If provided, terraform will attempt to assume this role using the supplied credentials.
        :param pulumi.Input[str] domain: The root domain of the API request, Default is `tencentcloudapi.com`.
        :param pulumi.Input[str] protocol: The protocol of the API request. Valid values: `HTTP` and `HTTPS`. Default is `HTTPS`.
        :param pulumi.Input[str] region: This is the TencentCloud region. It must be provided, but it can also be sourced from the `TENCENTCLOUD_REGION`
               environment variables. The default input value is ap-guangzhou.
        :param pulumi.Input[str] secret_id: This is the TencentCloud access key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_ID`
               environment variable.
        :param pulumi.Input[str] secret_key: This is the TencentCloud secret key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_KEY`
               environment variable.
        :param pulumi.Input[str] security_token: TencentCloud Security Token of temporary access credentials. It can be sourced from the `TENCENTCLOUD_SECURITY_TOKEN`
               environment variable. Notice: for supported products, please refer to: [temporary key supported
               products](https://intl.cloud.tencent.com/document/product/598/10588).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the tencentcloud package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assume_role: Optional[pulumi.Input[pulumi.InputType['ProviderAssumeRoleArgs']]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["assume_role"] = pulumi.Output.from_input(assume_role).apply(pulumi.runtime.to_json) if assume_role is not None else None
            __props__.__dict__["domain"] = domain
            __props__.__dict__["protocol"] = protocol
            if region is None:
                region = _utilities.get_env('TENCENTCLOUD_REGION')
            __props__.__dict__["region"] = region
            if secret_id is None:
                secret_id = _utilities.get_env('TENCENTCLOUD_SECRET_ID')
            __props__.__dict__["secret_id"] = secret_id
            if secret_key is None:
                secret_key = _utilities.get_env('TENCENTCLOUD_SECRET_KEY')
            __props__.__dict__["secret_key"] = secret_key
            if security_token is None:
                security_token = _utilities.get_env('TENCENTCLOUD_SECURITY_TOKEN')
            __props__.__dict__["security_token"] = security_token
        super(Provider, __self__).__init__(
            'tencentcloud',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        """
        The root domain of the API request, Default is `tencentcloudapi.com`.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[str]]:
        """
        The protocol of the API request. Valid values: `HTTP` and `HTTPS`. Default is `HTTPS`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        This is the TencentCloud region. It must be provided, but it can also be sourced from the `TENCENTCLOUD_REGION`
        environment variables. The default input value is ap-guangzhou.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Output[Optional[str]]:
        """
        This is the TencentCloud access key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_ID`
        environment variable.
        """
        return pulumi.get(self, "secret_id")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[Optional[str]]:
        """
        This is the TencentCloud secret key. It must be provided, but it can also be sourced from the `TENCENTCLOUD_SECRET_KEY`
        environment variable.
        """
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> pulumi.Output[Optional[str]]:
        """
        TencentCloud Security Token of temporary access credentials. It can be sourced from the `TENCENTCLOUD_SECURITY_TOKEN`
        environment variable. Notice: for supported products, please refer to: [temporary key supported
        products](https://intl.cloud.tencent.com/document/product/598/10588).
        """
        return pulumi.get(self, "security_token")

