# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AccessRuleArgs', 'AccessRule']

@pulumi.input_type
class AccessRuleArgs:
    def __init__(__self__, *,
                 access_group_id: pulumi.Input[str],
                 auth_client_ip: pulumi.Input[str],
                 priority: pulumi.Input[int],
                 rw_permission: Optional[pulumi.Input[str]] = None,
                 user_permission: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessRule resource.
        :param pulumi.Input[str] access_group_id: ID of a access group.
        :param pulumi.Input[str] auth_client_ip: A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.
        :param pulumi.Input[int] priority: The priority level of rule. Valid value ranges: (1~100). `1` indicates the highest priority.
        :param pulumi.Input[str] rw_permission: Read and write permissions. Valid values are `RO` and `RW`. and default is `RO`.
        :param pulumi.Input[str] user_permission: The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`. and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.
        """
        pulumi.set(__self__, "access_group_id", access_group_id)
        pulumi.set(__self__, "auth_client_ip", auth_client_ip)
        pulumi.set(__self__, "priority", priority)
        if rw_permission is not None:
            pulumi.set(__self__, "rw_permission", rw_permission)
        if user_permission is not None:
            pulumi.set(__self__, "user_permission", user_permission)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> pulumi.Input[str]:
        """
        ID of a access group.
        """
        return pulumi.get(self, "access_group_id")

    @access_group_id.setter
    def access_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_group_id", value)

    @property
    @pulumi.getter(name="authClientIp")
    def auth_client_ip(self) -> pulumi.Input[str]:
        """
        A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.
        """
        return pulumi.get(self, "auth_client_ip")

    @auth_client_ip.setter
    def auth_client_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_client_ip", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        """
        The priority level of rule. Valid value ranges: (1~100). `1` indicates the highest priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="rwPermission")
    def rw_permission(self) -> Optional[pulumi.Input[str]]:
        """
        Read and write permissions. Valid values are `RO` and `RW`. and default is `RO`.
        """
        return pulumi.get(self, "rw_permission")

    @rw_permission.setter
    def rw_permission(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rw_permission", value)

    @property
    @pulumi.getter(name="userPermission")
    def user_permission(self) -> Optional[pulumi.Input[str]]:
        """
        The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`. and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.
        """
        return pulumi.get(self, "user_permission")

    @user_permission.setter
    def user_permission(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_permission", value)


@pulumi.input_type
class _AccessRuleState:
    def __init__(__self__, *,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 auth_client_ip: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rw_permission: Optional[pulumi.Input[str]] = None,
                 user_permission: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessRule resources.
        :param pulumi.Input[str] access_group_id: ID of a access group.
        :param pulumi.Input[str] auth_client_ip: A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.
        :param pulumi.Input[int] priority: The priority level of rule. Valid value ranges: (1~100). `1` indicates the highest priority.
        :param pulumi.Input[str] rw_permission: Read and write permissions. Valid values are `RO` and `RW`. and default is `RO`.
        :param pulumi.Input[str] user_permission: The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`. and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.
        """
        if access_group_id is not None:
            pulumi.set(__self__, "access_group_id", access_group_id)
        if auth_client_ip is not None:
            pulumi.set(__self__, "auth_client_ip", auth_client_ip)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if rw_permission is not None:
            pulumi.set(__self__, "rw_permission", rw_permission)
        if user_permission is not None:
            pulumi.set(__self__, "user_permission", user_permission)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of a access group.
        """
        return pulumi.get(self, "access_group_id")

    @access_group_id.setter
    def access_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_group_id", value)

    @property
    @pulumi.getter(name="authClientIp")
    def auth_client_ip(self) -> Optional[pulumi.Input[str]]:
        """
        A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.
        """
        return pulumi.get(self, "auth_client_ip")

    @auth_client_ip.setter
    def auth_client_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_client_ip", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority level of rule. Valid value ranges: (1~100). `1` indicates the highest priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="rwPermission")
    def rw_permission(self) -> Optional[pulumi.Input[str]]:
        """
        Read and write permissions. Valid values are `RO` and `RW`. and default is `RO`.
        """
        return pulumi.get(self, "rw_permission")

    @rw_permission.setter
    def rw_permission(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rw_permission", value)

    @property
    @pulumi.getter(name="userPermission")
    def user_permission(self) -> Optional[pulumi.Input[str]]:
        """
        The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`. and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.
        """
        return pulumi.get(self, "user_permission")

    @user_permission.setter
    def user_permission(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_permission", value)


class AccessRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 auth_client_ip: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rw_permission: Optional[pulumi.Input[str]] = None,
                 user_permission: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to create a CFS access rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.cfs.AccessRule("foo",
            access_group_id="pgroup-7nx89k7l",
            auth_client_ip="10.10.1.0/24",
            priority=1,
            rw_permission="RO",
            user_permission="root_squash")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_group_id: ID of a access group.
        :param pulumi.Input[str] auth_client_ip: A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.
        :param pulumi.Input[int] priority: The priority level of rule. Valid value ranges: (1~100). `1` indicates the highest priority.
        :param pulumi.Input[str] rw_permission: Read and write permissions. Valid values are `RO` and `RW`. and default is `RO`.
        :param pulumi.Input[str] user_permission: The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`. and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a CFS access rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.cfs.AccessRule("foo",
            access_group_id="pgroup-7nx89k7l",
            auth_client_ip="10.10.1.0/24",
            priority=1,
            rw_permission="RO",
            user_permission="root_squash")
        ```

        :param str resource_name: The name of the resource.
        :param AccessRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 auth_client_ip: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rw_permission: Optional[pulumi.Input[str]] = None,
                 user_permission: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccessRuleArgs.__new__(AccessRuleArgs)

            if access_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'access_group_id'")
            __props__.__dict__["access_group_id"] = access_group_id
            if auth_client_ip is None and not opts.urn:
                raise TypeError("Missing required property 'auth_client_ip'")
            __props__.__dict__["auth_client_ip"] = auth_client_ip
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            __props__.__dict__["rw_permission"] = rw_permission
            __props__.__dict__["user_permission"] = user_permission
        super(AccessRule, __self__).__init__(
            'tencentcloud:Cfs/accessRule:AccessRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_group_id: Optional[pulumi.Input[str]] = None,
            auth_client_ip: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            rw_permission: Optional[pulumi.Input[str]] = None,
            user_permission: Optional[pulumi.Input[str]] = None) -> 'AccessRule':
        """
        Get an existing AccessRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_group_id: ID of a access group.
        :param pulumi.Input[str] auth_client_ip: A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.
        :param pulumi.Input[int] priority: The priority level of rule. Valid value ranges: (1~100). `1` indicates the highest priority.
        :param pulumi.Input[str] rw_permission: Read and write permissions. Valid values are `RO` and `RW`. and default is `RO`.
        :param pulumi.Input[str] user_permission: The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`. and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessRuleState.__new__(_AccessRuleState)

        __props__.__dict__["access_group_id"] = access_group_id
        __props__.__dict__["auth_client_ip"] = auth_client_ip
        __props__.__dict__["priority"] = priority
        __props__.__dict__["rw_permission"] = rw_permission
        __props__.__dict__["user_permission"] = user_permission
        return AccessRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> pulumi.Output[str]:
        """
        ID of a access group.
        """
        return pulumi.get(self, "access_group_id")

    @property
    @pulumi.getter(name="authClientIp")
    def auth_client_ip(self) -> pulumi.Output[str]:
        """
        A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.
        """
        return pulumi.get(self, "auth_client_ip")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The priority level of rule. Valid value ranges: (1~100). `1` indicates the highest priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="rwPermission")
    def rw_permission(self) -> pulumi.Output[Optional[str]]:
        """
        Read and write permissions. Valid values are `RO` and `RW`. and default is `RO`.
        """
        return pulumi.get(self, "rw_permission")

    @property
    @pulumi.getter(name="userPermission")
    def user_permission(self) -> pulumi.Output[Optional[str]]:
        """
        The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`. and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.
        """
        return pulumi.get(self, "user_permission")

