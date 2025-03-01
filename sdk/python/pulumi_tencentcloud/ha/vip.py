# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VipArgs', 'Vip']

@pulumi.input_type
class VipArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 vpc_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 vip: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Vip resource.
        :param pulumi.Input[str] subnet_id: Subnet ID.
        :param pulumi.Input[str] vpc_id: VPC ID.
        :param pulumi.Input[str] name: Name of the HA VIP. The length of character is limited to 1-60.
        :param pulumi.Input[str] vip: Virtual IP address, it must not be occupied and in this VPC network segment. If not set, it will be assigned after resource created automatically.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if vip is not None:
            pulumi.set(__self__, "vip", vip)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        Subnet ID.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        VPC ID.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the HA VIP. The length of character is limited to 1-60.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def vip(self) -> Optional[pulumi.Input[str]]:
        """
        Virtual IP address, it must not be occupied and in this VPC network segment. If not set, it will be assigned after resource created automatically.
        """
        return pulumi.get(self, "vip")

    @vip.setter
    def vip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vip", value)


@pulumi.input_type
class _VipState:
    def __init__(__self__, *,
                 address_ip: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vip: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Vip resources.
        :param pulumi.Input[str] address_ip: EIP that is associated.
        :param pulumi.Input[str] create_time: Create time of the HA VIP.
        :param pulumi.Input[str] instance_id: Instance ID that is associated.
        :param pulumi.Input[str] name: Name of the HA VIP. The length of character is limited to 1-60.
        :param pulumi.Input[str] network_interface_id: Network interface ID that is associated.
        :param pulumi.Input[str] state: State of the HA VIP. Valid value: `AVAILABLE`, `UNBIND`.
        :param pulumi.Input[str] subnet_id: Subnet ID.
        :param pulumi.Input[str] vip: Virtual IP address, it must not be occupied and in this VPC network segment. If not set, it will be assigned after resource created automatically.
        :param pulumi.Input[str] vpc_id: VPC ID.
        """
        if address_ip is not None:
            pulumi.set(__self__, "address_ip", address_ip)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if vip is not None:
            pulumi.set(__self__, "vip", vip)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="addressIp")
    def address_ip(self) -> Optional[pulumi.Input[str]]:
        """
        EIP that is associated.
        """
        return pulumi.get(self, "address_ip")

    @address_ip.setter
    def address_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_ip", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Create time of the HA VIP.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        Instance ID that is associated.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the HA VIP. The length of character is limited to 1-60.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[str]]:
        """
        Network interface ID that is associated.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the HA VIP. Valid value: `AVAILABLE`, `UNBIND`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        Subnet ID.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def vip(self) -> Optional[pulumi.Input[str]]:
        """
        Virtual IP address, it must not be occupied and in this VPC network segment. If not set, it will be assigned after resource created automatically.
        """
        return pulumi.get(self, "vip")

    @vip.setter
    def vip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vip", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        VPC ID.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class Vip(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vip: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to create a HA VIP.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.ha.Vip("foo",
            subnet_id="subnet-4d4m4cd4s",
            vip="10.0.4.16",
            vpc_id="vpc-gzea3dd7")
        ```

        ## Import

        HA VIP can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Ha/vip:Vip foo havip-kjqwe4ba
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the HA VIP. The length of character is limited to 1-60.
        :param pulumi.Input[str] subnet_id: Subnet ID.
        :param pulumi.Input[str] vip: Virtual IP address, it must not be occupied and in this VPC network segment. If not set, it will be assigned after resource created automatically.
        :param pulumi.Input[str] vpc_id: VPC ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a HA VIP.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.ha.Vip("foo",
            subnet_id="subnet-4d4m4cd4s",
            vip="10.0.4.16",
            vpc_id="vpc-gzea3dd7")
        ```

        ## Import

        HA VIP can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Ha/vip:Vip foo havip-kjqwe4ba
        ```

        :param str resource_name: The name of the resource.
        :param VipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vip: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = VipArgs.__new__(VipArgs)

            __props__.__dict__["name"] = name
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["vip"] = vip
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["address_ip"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["instance_id"] = None
            __props__.__dict__["network_interface_id"] = None
            __props__.__dict__["state"] = None
        super(Vip, __self__).__init__(
            'tencentcloud:Ha/vip:Vip',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_ip: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_interface_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            vip: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'Vip':
        """
        Get an existing Vip resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_ip: EIP that is associated.
        :param pulumi.Input[str] create_time: Create time of the HA VIP.
        :param pulumi.Input[str] instance_id: Instance ID that is associated.
        :param pulumi.Input[str] name: Name of the HA VIP. The length of character is limited to 1-60.
        :param pulumi.Input[str] network_interface_id: Network interface ID that is associated.
        :param pulumi.Input[str] state: State of the HA VIP. Valid value: `AVAILABLE`, `UNBIND`.
        :param pulumi.Input[str] subnet_id: Subnet ID.
        :param pulumi.Input[str] vip: Virtual IP address, it must not be occupied and in this VPC network segment. If not set, it will be assigned after resource created automatically.
        :param pulumi.Input[str] vpc_id: VPC ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VipState.__new__(_VipState)

        __props__.__dict__["address_ip"] = address_ip
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["name"] = name
        __props__.__dict__["network_interface_id"] = network_interface_id
        __props__.__dict__["state"] = state
        __props__.__dict__["subnet_id"] = subnet_id
        __props__.__dict__["vip"] = vip
        __props__.__dict__["vpc_id"] = vpc_id
        return Vip(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressIp")
    def address_ip(self) -> pulumi.Output[str]:
        """
        EIP that is associated.
        """
        return pulumi.get(self, "address_ip")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time of the HA VIP.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        Instance ID that is associated.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the HA VIP. The length of character is limited to 1-60.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[str]:
        """
        Network interface ID that is associated.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the HA VIP. Valid value: `AVAILABLE`, `UNBIND`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        Subnet ID.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def vip(self) -> pulumi.Output[str]:
        """
        Virtual IP address, it must not be occupied and in this VPC network segment. If not set, it will be assigned after resource created automatically.
        """
        return pulumi.get(self, "vip")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        VPC ID.
        """
        return pulumi.get(self, "vpc_id")

