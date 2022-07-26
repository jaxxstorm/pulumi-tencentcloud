# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserPolicyAttachmentArgs', 'UserPolicyAttachment']

@pulumi.input_type
class UserPolicyAttachmentArgs:
    def __init__(__self__, *,
                 policy_id: pulumi.Input[str],
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserPolicyAttachment resource.
        :param pulumi.Input[str] policy_id: ID of the policy.
        :param pulumi.Input[str] user_id: ID of the attached CAM user.
        :param pulumi.Input[str] user_name: Name of the attached CAM user as uniq key.
        """
        pulumi.set(__self__, "policy_id", policy_id)
        if user_id is not None:
            warnings.warn("""It has been deprecated from version 1.59.5. Use `user_name` instead.""", DeprecationWarning)
            pulumi.log.warn("""user_id is deprecated: It has been deprecated from version 1.59.5. Use `user_name` instead.""")
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[str]:
        """
        ID of the policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the attached CAM user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attached CAM user as uniq key.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


@pulumi.input_type
class _UserPolicyAttachmentState:
    def __init__(__self__, *,
                 create_mode: Optional[pulumi.Input[int]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserPolicyAttachment resources.
        :param pulumi.Input[int] create_mode: Mode of Creation of the CAM user policy attachment. `1` means the CAM policy attachment is created by production, and
               the others indicate syntax strategy ways.
        :param pulumi.Input[str] create_time: Create time of the CAM user policy attachment.
        :param pulumi.Input[str] policy_id: ID of the policy.
        :param pulumi.Input[str] policy_name: Name of the policy.
        :param pulumi.Input[str] policy_type: Type of the policy strategy. `User` means customer strategy and `QCS` means preset strategy.
        :param pulumi.Input[str] user_id: ID of the attached CAM user.
        :param pulumi.Input[str] user_name: Name of the attached CAM user as uniq key.
        """
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if user_id is not None:
            warnings.warn("""It has been deprecated from version 1.59.5. Use `user_name` instead.""", DeprecationWarning)
            pulumi.log.warn("""user_id is deprecated: It has been deprecated from version 1.59.5. Use `user_name` instead.""")
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[int]]:
        """
        Mode of Creation of the CAM user policy attachment. `1` means the CAM policy attachment is created by production, and
        the others indicate syntax strategy ways.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Create time of the CAM user policy attachment.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the policy strategy. `User` means customer strategy and `QCS` means preset strategy.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the attached CAM user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the attached CAM user as uniq key.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class UserPolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a UserPolicyAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] policy_id: ID of the policy.
        :param pulumi.Input[str] user_id: ID of the attached CAM user.
        :param pulumi.Input[str] user_name: Name of the attached CAM user as uniq key.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserPolicyAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a UserPolicyAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param UserPolicyAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserPolicyAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = UserPolicyAttachmentArgs.__new__(UserPolicyAttachmentArgs)

            if policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_id'")
            __props__.__dict__["policy_id"] = policy_id
            if user_id is not None and not opts.urn:
                warnings.warn("""It has been deprecated from version 1.59.5. Use `user_name` instead.""", DeprecationWarning)
                pulumi.log.warn("""user_id is deprecated: It has been deprecated from version 1.59.5. Use `user_name` instead.""")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["create_mode"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["policy_name"] = None
            __props__.__dict__["policy_type"] = None
        super(UserPolicyAttachment, __self__).__init__(
            'tencentcloud:Cam/userPolicyAttachment:UserPolicyAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_mode: Optional[pulumi.Input[int]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            policy_id: Optional[pulumi.Input[str]] = None,
            policy_name: Optional[pulumi.Input[str]] = None,
            policy_type: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None,
            user_name: Optional[pulumi.Input[str]] = None) -> 'UserPolicyAttachment':
        """
        Get an existing UserPolicyAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] create_mode: Mode of Creation of the CAM user policy attachment. `1` means the CAM policy attachment is created by production, and
               the others indicate syntax strategy ways.
        :param pulumi.Input[str] create_time: Create time of the CAM user policy attachment.
        :param pulumi.Input[str] policy_id: ID of the policy.
        :param pulumi.Input[str] policy_name: Name of the policy.
        :param pulumi.Input[str] policy_type: Type of the policy strategy. `User` means customer strategy and `QCS` means preset strategy.
        :param pulumi.Input[str] user_id: ID of the attached CAM user.
        :param pulumi.Input[str] user_name: Name of the attached CAM user as uniq key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserPolicyAttachmentState.__new__(_UserPolicyAttachmentState)

        __props__.__dict__["create_mode"] = create_mode
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["policy_id"] = policy_id
        __props__.__dict__["policy_name"] = policy_name
        __props__.__dict__["policy_type"] = policy_type
        __props__.__dict__["user_id"] = user_id
        __props__.__dict__["user_name"] = user_name
        return UserPolicyAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Output[int]:
        """
        Mode of Creation of the CAM user policy attachment. `1` means the CAM policy attachment is created by production, and
        the others indicate syntax strategy ways.
        """
        return pulumi.get(self, "create_mode")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time of the CAM user policy attachment.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        ID of the policy.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        """
        Type of the policy strategy. `User` means customer strategy and `QCS` means preset strategy.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the attached CAM user.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the attached CAM user as uniq key.
        """
        return pulumi.get(self, "user_name")

