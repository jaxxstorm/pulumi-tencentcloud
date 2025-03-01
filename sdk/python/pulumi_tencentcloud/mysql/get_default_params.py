# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDefaultParamsResult',
    'AwaitableGetDefaultParamsResult',
    'get_default_params',
    'get_default_params_output',
]

@pulumi.output_type
class GetDefaultParamsResult:
    """
    A collection of values returned by getDefaultParams.
    """
    def __init__(__self__, db_version=None, id=None, param_lists=None, result_output_file=None):
        if db_version and not isinstance(db_version, str):
            raise TypeError("Expected argument 'db_version' to be a str")
        pulumi.set(__self__, "db_version", db_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if param_lists and not isinstance(param_lists, list):
            raise TypeError("Expected argument 'param_lists' to be a list")
        pulumi.set(__self__, "param_lists", param_lists)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)

    @property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> Optional[str]:
        return pulumi.get(self, "db_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="paramLists")
    def param_lists(self) -> Sequence['outputs.GetDefaultParamsParamListResult']:
        """
        List of param detail.
        """
        return pulumi.get(self, "param_lists")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableGetDefaultParamsResult(GetDefaultParamsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefaultParamsResult(
            db_version=self.db_version,
            id=self.id,
            param_lists=self.param_lists,
            result_output_file=self.result_output_file)


def get_default_params(db_version: Optional[str] = None,
                       result_output_file: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefaultParamsResult:
    """
    Provide a datasource to query default mysql parameters.


    :param str db_version: MySQL database version.
    :param str result_output_file: Used for save results.
    """
    __args__ = dict()
    __args__['dbVersion'] = db_version
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Mysql/getDefaultParams:getDefaultParams', __args__, opts=opts, typ=GetDefaultParamsResult).value

    return AwaitableGetDefaultParamsResult(
        db_version=__ret__.db_version,
        id=__ret__.id,
        param_lists=__ret__.param_lists,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(get_default_params)
def get_default_params_output(db_version: Optional[pulumi.Input[Optional[str]]] = None,
                              result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDefaultParamsResult]:
    """
    Provide a datasource to query default mysql parameters.


    :param str db_version: MySQL database version.
    :param str result_output_file: Used for save results.
    """
    ...
