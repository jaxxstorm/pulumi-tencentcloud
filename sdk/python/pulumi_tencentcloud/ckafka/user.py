# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 password: pulumi.Input[str]):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] account_name: Account name used to access to ckafka instance.
        :param pulumi.Input[str] instance_id: ID of the ckafka instance.
        :param pulumi.Input[str] password: Password of the account.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Account name used to access to ckafka instance.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        ID of the ckafka instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        Password of the account.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 account_name: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[str] account_name: Account name used to access to ckafka instance.
        :param pulumi.Input[str] create_time: Creation time of the account.
        :param pulumi.Input[str] instance_id: ID of the ckafka instance.
        :param pulumi.Input[str] password: Password of the account.
        :param pulumi.Input[str] update_time: The last update time of the account.
        """
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Account name used to access to ckafka instance.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of the account.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the ckafka instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password of the account.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The last update time of the account.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a User resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Account name used to access to ckafka instance.
        :param pulumi.Input[str] instance_id: ID of the ckafka instance.
        :param pulumi.Input[str] password: Password of the account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a User resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
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
            __props__ = UserArgs.__new__(UserArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = password
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        super(User, __self__).__init__(
            'tencentcloud:Ckafka/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Account name used to access to ckafka instance.
        :param pulumi.Input[str] create_time: Creation time of the account.
        :param pulumi.Input[str] instance_id: ID of the ckafka instance.
        :param pulumi.Input[str] password: Password of the account.
        :param pulumi.Input[str] update_time: The last update time of the account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["account_name"] = account_name
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["password"] = password
        __props__.__dict__["update_time"] = update_time
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        Account name used to access to ckafka instance.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of the account.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        ID of the ckafka instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        Password of the account.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update time of the account.
        """
        return pulumi.get(self, "update_time")

