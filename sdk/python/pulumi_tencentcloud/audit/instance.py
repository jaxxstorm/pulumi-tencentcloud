# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 audit_switch: pulumi.Input[bool],
                 cos_bucket: pulumi.Input[str],
                 cos_region: pulumi.Input[str],
                 read_write_attribute: pulumi.Input[int],
                 enable_kms_encry: Optional[pulumi.Input[bool]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 log_file_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[bool] audit_switch: Indicate whether to turn on audit logging or not.
        :param pulumi.Input[str] cos_bucket: Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by
               terraform.
        :param pulumi.Input[str] cos_region: Region of the cos bucket.
        :param pulumi.Input[int] read_write_attribute: Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.
        :param pulumi.Input[bool] enable_kms_encry: Indicate whether the log is encrypt with KMS algorithm or not.
        :param pulumi.Input[str] key_id: Existing CMK unique key. This field can be get by data source `_audit.get_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.
        :param pulumi.Input[str] log_file_prefix: The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.
        :param pulumi.Input[str] name: Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.
        """
        pulumi.set(__self__, "audit_switch", audit_switch)
        pulumi.set(__self__, "cos_bucket", cos_bucket)
        pulumi.set(__self__, "cos_region", cos_region)
        pulumi.set(__self__, "read_write_attribute", read_write_attribute)
        if enable_kms_encry is not None:
            pulumi.set(__self__, "enable_kms_encry", enable_kms_encry)
        if key_id is not None:
            pulumi.set(__self__, "key_id", key_id)
        if log_file_prefix is not None:
            pulumi.set(__self__, "log_file_prefix", log_file_prefix)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="auditSwitch")
    def audit_switch(self) -> pulumi.Input[bool]:
        """
        Indicate whether to turn on audit logging or not.
        """
        return pulumi.get(self, "audit_switch")

    @audit_switch.setter
    def audit_switch(self, value: pulumi.Input[bool]):
        pulumi.set(self, "audit_switch", value)

    @property
    @pulumi.getter(name="cosBucket")
    def cos_bucket(self) -> pulumi.Input[str]:
        """
        Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by
        terraform.
        """
        return pulumi.get(self, "cos_bucket")

    @cos_bucket.setter
    def cos_bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "cos_bucket", value)

    @property
    @pulumi.getter(name="cosRegion")
    def cos_region(self) -> pulumi.Input[str]:
        """
        Region of the cos bucket.
        """
        return pulumi.get(self, "cos_region")

    @cos_region.setter
    def cos_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "cos_region", value)

    @property
    @pulumi.getter(name="readWriteAttribute")
    def read_write_attribute(self) -> pulumi.Input[int]:
        """
        Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.
        """
        return pulumi.get(self, "read_write_attribute")

    @read_write_attribute.setter
    def read_write_attribute(self, value: pulumi.Input[int]):
        pulumi.set(self, "read_write_attribute", value)

    @property
    @pulumi.getter(name="enableKmsEncry")
    def enable_kms_encry(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicate whether the log is encrypt with KMS algorithm or not.
        """
        return pulumi.get(self, "enable_kms_encry")

    @enable_kms_encry.setter
    def enable_kms_encry(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_kms_encry", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Existing CMK unique key. This field can be get by data source `_audit.get_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter(name="logFilePrefix")
    def log_file_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.
        """
        return pulumi.get(self, "log_file_prefix")

    @log_file_prefix.setter
    def log_file_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_file_prefix", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *,
                 audit_switch: Optional[pulumi.Input[bool]] = None,
                 cos_bucket: Optional[pulumi.Input[str]] = None,
                 cos_region: Optional[pulumi.Input[str]] = None,
                 enable_kms_encry: Optional[pulumi.Input[bool]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 log_file_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_write_attribute: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Instance resources.
        :param pulumi.Input[bool] audit_switch: Indicate whether to turn on audit logging or not.
        :param pulumi.Input[str] cos_bucket: Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by
               terraform.
        :param pulumi.Input[str] cos_region: Region of the cos bucket.
        :param pulumi.Input[bool] enable_kms_encry: Indicate whether the log is encrypt with KMS algorithm or not.
        :param pulumi.Input[str] key_id: Existing CMK unique key. This field can be get by data source `_audit.get_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.
        :param pulumi.Input[str] log_file_prefix: The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.
        :param pulumi.Input[str] name: Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.
        :param pulumi.Input[int] read_write_attribute: Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.
        """
        if audit_switch is not None:
            pulumi.set(__self__, "audit_switch", audit_switch)
        if cos_bucket is not None:
            pulumi.set(__self__, "cos_bucket", cos_bucket)
        if cos_region is not None:
            pulumi.set(__self__, "cos_region", cos_region)
        if enable_kms_encry is not None:
            pulumi.set(__self__, "enable_kms_encry", enable_kms_encry)
        if key_id is not None:
            pulumi.set(__self__, "key_id", key_id)
        if log_file_prefix is not None:
            pulumi.set(__self__, "log_file_prefix", log_file_prefix)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if read_write_attribute is not None:
            pulumi.set(__self__, "read_write_attribute", read_write_attribute)

    @property
    @pulumi.getter(name="auditSwitch")
    def audit_switch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicate whether to turn on audit logging or not.
        """
        return pulumi.get(self, "audit_switch")

    @audit_switch.setter
    def audit_switch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "audit_switch", value)

    @property
    @pulumi.getter(name="cosBucket")
    def cos_bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by
        terraform.
        """
        return pulumi.get(self, "cos_bucket")

    @cos_bucket.setter
    def cos_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cos_bucket", value)

    @property
    @pulumi.getter(name="cosRegion")
    def cos_region(self) -> Optional[pulumi.Input[str]]:
        """
        Region of the cos bucket.
        """
        return pulumi.get(self, "cos_region")

    @cos_region.setter
    def cos_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cos_region", value)

    @property
    @pulumi.getter(name="enableKmsEncry")
    def enable_kms_encry(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicate whether the log is encrypt with KMS algorithm or not.
        """
        return pulumi.get(self, "enable_kms_encry")

    @enable_kms_encry.setter
    def enable_kms_encry(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_kms_encry", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Existing CMK unique key. This field can be get by data source `_audit.get_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter(name="logFilePrefix")
    def log_file_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.
        """
        return pulumi.get(self, "log_file_prefix")

    @log_file_prefix.setter
    def log_file_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_file_prefix", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readWriteAttribute")
    def read_write_attribute(self) -> Optional[pulumi.Input[int]]:
        """
        Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.
        """
        return pulumi.get(self, "read_write_attribute")

    @read_write_attribute.setter
    def read_write_attribute(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "read_write_attribute", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_switch: Optional[pulumi.Input[bool]] = None,
                 cos_bucket: Optional[pulumi.Input[str]] = None,
                 cos_region: Optional[pulumi.Input[str]] = None,
                 enable_kms_encry: Optional[pulumi.Input[bool]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 log_file_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_write_attribute: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a resource to create an audit.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.audit.Instance("foo",
            audit_switch=True,
            cos_bucket="test",
            cos_region="ap-hongkong",
            log_file_prefix="test",
            read_write_attribute=3)
        ```

        ## Import

        Audit can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Audit/instance:Instance foo audit-test
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audit_switch: Indicate whether to turn on audit logging or not.
        :param pulumi.Input[str] cos_bucket: Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by
               terraform.
        :param pulumi.Input[str] cos_region: Region of the cos bucket.
        :param pulumi.Input[bool] enable_kms_encry: Indicate whether the log is encrypt with KMS algorithm or not.
        :param pulumi.Input[str] key_id: Existing CMK unique key. This field can be get by data source `_audit.get_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.
        :param pulumi.Input[str] log_file_prefix: The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.
        :param pulumi.Input[str] name: Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.
        :param pulumi.Input[int] read_write_attribute: Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create an audit.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tencentcloud as tencentcloud

        foo = tencentcloud.audit.Instance("foo",
            audit_switch=True,
            cos_bucket="test",
            cos_region="ap-hongkong",
            log_file_prefix="test",
            read_write_attribute=3)
        ```

        ## Import

        Audit can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Audit/instance:Instance foo audit-test
        ```

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_switch: Optional[pulumi.Input[bool]] = None,
                 cos_bucket: Optional[pulumi.Input[str]] = None,
                 cos_region: Optional[pulumi.Input[str]] = None,
                 enable_kms_encry: Optional[pulumi.Input[bool]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 log_file_prefix: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_write_attribute: Optional[pulumi.Input[int]] = None,
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
            __props__ = InstanceArgs.__new__(InstanceArgs)

            if audit_switch is None and not opts.urn:
                raise TypeError("Missing required property 'audit_switch'")
            __props__.__dict__["audit_switch"] = audit_switch
            if cos_bucket is None and not opts.urn:
                raise TypeError("Missing required property 'cos_bucket'")
            __props__.__dict__["cos_bucket"] = cos_bucket
            if cos_region is None and not opts.urn:
                raise TypeError("Missing required property 'cos_region'")
            __props__.__dict__["cos_region"] = cos_region
            __props__.__dict__["enable_kms_encry"] = enable_kms_encry
            __props__.__dict__["key_id"] = key_id
            __props__.__dict__["log_file_prefix"] = log_file_prefix
            __props__.__dict__["name"] = name
            if read_write_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'read_write_attribute'")
            __props__.__dict__["read_write_attribute"] = read_write_attribute
        super(Instance, __self__).__init__(
            'tencentcloud:Audit/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            audit_switch: Optional[pulumi.Input[bool]] = None,
            cos_bucket: Optional[pulumi.Input[str]] = None,
            cos_region: Optional[pulumi.Input[str]] = None,
            enable_kms_encry: Optional[pulumi.Input[bool]] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            log_file_prefix: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            read_write_attribute: Optional[pulumi.Input[int]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audit_switch: Indicate whether to turn on audit logging or not.
        :param pulumi.Input[str] cos_bucket: Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by
               terraform.
        :param pulumi.Input[str] cos_region: Region of the cos bucket.
        :param pulumi.Input[bool] enable_kms_encry: Indicate whether the log is encrypt with KMS algorithm or not.
        :param pulumi.Input[str] key_id: Existing CMK unique key. This field can be get by data source `_audit.get_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.
        :param pulumi.Input[str] log_file_prefix: The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.
        :param pulumi.Input[str] name: Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.
        :param pulumi.Input[int] read_write_attribute: Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceState.__new__(_InstanceState)

        __props__.__dict__["audit_switch"] = audit_switch
        __props__.__dict__["cos_bucket"] = cos_bucket
        __props__.__dict__["cos_region"] = cos_region
        __props__.__dict__["enable_kms_encry"] = enable_kms_encry
        __props__.__dict__["key_id"] = key_id
        __props__.__dict__["log_file_prefix"] = log_file_prefix
        __props__.__dict__["name"] = name
        __props__.__dict__["read_write_attribute"] = read_write_attribute
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="auditSwitch")
    def audit_switch(self) -> pulumi.Output[bool]:
        """
        Indicate whether to turn on audit logging or not.
        """
        return pulumi.get(self, "audit_switch")

    @property
    @pulumi.getter(name="cosBucket")
    def cos_bucket(self) -> pulumi.Output[str]:
        """
        Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by
        terraform.
        """
        return pulumi.get(self, "cos_bucket")

    @property
    @pulumi.getter(name="cosRegion")
    def cos_region(self) -> pulumi.Output[str]:
        """
        Region of the cos bucket.
        """
        return pulumi.get(self, "cos_region")

    @property
    @pulumi.getter(name="enableKmsEncry")
    def enable_kms_encry(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicate whether the log is encrypt with KMS algorithm or not.
        """
        return pulumi.get(self, "enable_kms_encry")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[Optional[str]]:
        """
        Existing CMK unique key. This field can be get by data source `_audit.get_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="logFilePrefix")
    def log_file_prefix(self) -> pulumi.Output[str]:
        """
        The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.
        """
        return pulumi.get(self, "log_file_prefix")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="readWriteAttribute")
    def read_write_attribute(self) -> pulumi.Output[int]:
        """
        Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.
        """
        return pulumi.get(self, "read_write_attribute")

