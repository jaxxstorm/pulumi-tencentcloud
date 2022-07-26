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
    'TCRTokensResult',
    'AwaitableTCRTokensResult',
    'tcr_tokens',
    'tcr_tokens_output',
]

@pulumi.output_type
class TCRTokensResult:
    """
    A collection of values returned by TCRTokens.
    """
    def __init__(__self__, id=None, instance_id=None, result_output_file=None, token_id=None, token_lists=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if token_id and not isinstance(token_id, str):
            raise TypeError("Expected argument 'token_id' to be a str")
        pulumi.set(__self__, "token_id", token_id)
        if token_lists and not isinstance(token_lists, list):
            raise TypeError("Expected argument 'token_lists' to be a list")
        pulumi.set(__self__, "token_lists", token_lists)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> Optional[str]:
        return pulumi.get(self, "token_id")

    @property
    @pulumi.getter(name="tokenLists")
    def token_lists(self) -> Sequence['outputs.TCRTokensTokenListResult']:
        return pulumi.get(self, "token_lists")


class AwaitableTCRTokensResult(TCRTokensResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return TCRTokensResult(
            id=self.id,
            instance_id=self.instance_id,
            result_output_file=self.result_output_file,
            token_id=self.token_id,
            token_lists=self.token_lists)


def tcr_tokens(instance_id: Optional[str] = None,
               result_output_file: Optional[str] = None,
               token_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableTCRTokensResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    __args__['resultOutputFile'] = result_output_file
    __args__['tokenId'] = token_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Cloud/tCRTokens:TCRTokens', __args__, opts=opts, typ=TCRTokensResult).value

    return AwaitableTCRTokensResult(
        id=__ret__.id,
        instance_id=__ret__.instance_id,
        result_output_file=__ret__.result_output_file,
        token_id=__ret__.token_id,
        token_lists=__ret__.token_lists)


@_utilities.lift_output_func(tcr_tokens)
def tcr_tokens_output(instance_id: Optional[pulumi.Input[str]] = None,
                      result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                      token_id: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[TCRTokensResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
