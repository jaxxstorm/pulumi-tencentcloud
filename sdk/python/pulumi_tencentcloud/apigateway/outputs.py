# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'APIRequestParameter',
    'APIResponseErrorCode',
    'ServiceApiList',
    'ServiceUsagePlanList',
    'UsagePlanAttachList',
]

@pulumi.output_type
class APIRequestParameter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultValue":
            suggest = "default_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in APIRequestParameter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        APIRequestParameter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        APIRequestParameter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 position: str,
                 type: str,
                 default_value: Optional[str] = None,
                 desc: Optional[str] = None,
                 required: Optional[bool] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "type", type)
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if desc is not None:
            pulumi.set(__self__, "desc", desc)
        if required is not None:
            pulumi.set(__self__, "required", required)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def position(self) -> str:
        return pulumi.get(self, "position")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[str]:
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def desc(self) -> Optional[str]:
        return pulumi.get(self, "desc")

    @property
    @pulumi.getter
    def required(self) -> Optional[bool]:
        return pulumi.get(self, "required")


@pulumi.output_type
class APIResponseErrorCode(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "convertedCode":
            suggest = "converted_code"
        elif key == "needConvert":
            suggest = "need_convert"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in APIResponseErrorCode. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        APIResponseErrorCode.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        APIResponseErrorCode.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 code: int,
                 msg: str,
                 converted_code: Optional[int] = None,
                 desc: Optional[str] = None,
                 need_convert: Optional[bool] = None):
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "msg", msg)
        if converted_code is not None:
            pulumi.set(__self__, "converted_code", converted_code)
        if desc is not None:
            pulumi.set(__self__, "desc", desc)
        if need_convert is not None:
            pulumi.set(__self__, "need_convert", need_convert)

    @property
    @pulumi.getter
    def code(self) -> int:
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def msg(self) -> str:
        return pulumi.get(self, "msg")

    @property
    @pulumi.getter(name="convertedCode")
    def converted_code(self) -> Optional[int]:
        return pulumi.get(self, "converted_code")

    @property
    @pulumi.getter
    def desc(self) -> Optional[str]:
        return pulumi.get(self, "desc")

    @property
    @pulumi.getter(name="needConvert")
    def need_convert(self) -> Optional[bool]:
        return pulumi.get(self, "need_convert")


@pulumi.output_type
class ServiceApiList(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiDesc":
            suggest = "api_desc"
        elif key == "apiId":
            suggest = "api_id"
        elif key == "apiName":
            suggest = "api_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceApiList. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceApiList.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceApiList.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_desc: Optional[str] = None,
                 api_id: Optional[str] = None,
                 api_name: Optional[str] = None,
                 method: Optional[str] = None,
                 path: Optional[str] = None):
        if api_desc is not None:
            pulumi.set(__self__, "api_desc", api_desc)
        if api_id is not None:
            pulumi.set(__self__, "api_id", api_id)
        if api_name is not None:
            pulumi.set(__self__, "api_name", api_name)
        if method is not None:
            pulumi.set(__self__, "method", method)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="apiDesc")
    def api_desc(self) -> Optional[str]:
        return pulumi.get(self, "api_desc")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiName")
    def api_name(self) -> Optional[str]:
        return pulumi.get(self, "api_name")

    @property
    @pulumi.getter
    def method(self) -> Optional[str]:
        return pulumi.get(self, "method")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        return pulumi.get(self, "path")


@pulumi.output_type
class ServiceUsagePlanList(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiId":
            suggest = "api_id"
        elif key == "bindType":
            suggest = "bind_type"
        elif key == "usagePlanId":
            suggest = "usage_plan_id"
        elif key == "usagePlanName":
            suggest = "usage_plan_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceUsagePlanList. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceUsagePlanList.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceUsagePlanList.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_id: Optional[str] = None,
                 bind_type: Optional[str] = None,
                 usage_plan_id: Optional[str] = None,
                 usage_plan_name: Optional[str] = None):
        if api_id is not None:
            pulumi.set(__self__, "api_id", api_id)
        if bind_type is not None:
            pulumi.set(__self__, "bind_type", bind_type)
        if usage_plan_id is not None:
            pulumi.set(__self__, "usage_plan_id", usage_plan_id)
        if usage_plan_name is not None:
            pulumi.set(__self__, "usage_plan_name", usage_plan_name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="bindType")
    def bind_type(self) -> Optional[str]:
        return pulumi.get(self, "bind_type")

    @property
    @pulumi.getter(name="usagePlanId")
    def usage_plan_id(self) -> Optional[str]:
        return pulumi.get(self, "usage_plan_id")

    @property
    @pulumi.getter(name="usagePlanName")
    def usage_plan_name(self) -> Optional[str]:
        return pulumi.get(self, "usage_plan_name")


@pulumi.output_type
class UsagePlanAttachList(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiId":
            suggest = "api_id"
        elif key == "apiName":
            suggest = "api_name"
        elif key == "createTime":
            suggest = "create_time"
        elif key == "modifyTime":
            suggest = "modify_time"
        elif key == "serviceId":
            suggest = "service_id"
        elif key == "serviceName":
            suggest = "service_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UsagePlanAttachList. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UsagePlanAttachList.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UsagePlanAttachList.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_id: Optional[str] = None,
                 api_name: Optional[str] = None,
                 create_time: Optional[str] = None,
                 environment: Optional[str] = None,
                 method: Optional[str] = None,
                 modify_time: Optional[str] = None,
                 path: Optional[str] = None,
                 service_id: Optional[str] = None,
                 service_name: Optional[str] = None):
        if api_id is not None:
            pulumi.set(__self__, "api_id", api_id)
        if api_name is not None:
            pulumi.set(__self__, "api_name", api_name)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if method is not None:
            pulumi.set(__self__, "method", method)
        if modify_time is not None:
            pulumi.set(__self__, "modify_time", modify_time)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiName")
    def api_name(self) -> Optional[str]:
        return pulumi.get(self, "api_name")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[str]:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def environment(self) -> Optional[str]:
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def method(self) -> Optional[str]:
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="modifyTime")
    def modify_time(self) -> Optional[str]:
        return pulumi.get(self, "modify_time")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[str]:
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[str]:
        return pulumi.get(self, "service_name")


