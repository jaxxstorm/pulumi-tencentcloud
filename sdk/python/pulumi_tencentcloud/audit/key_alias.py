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
    'KeyAliasResult',
    'AwaitableKeyAliasResult',
    'key_alias',
    'key_alias_output',
]

@pulumi.output_type
class KeyAliasResult:
    """
    A collection of values returned by KeyAlias.
    """
    def __init__(__self__, audit_key_alias_lists=None, id=None, region=None, result_output_file=None):
        if audit_key_alias_lists and not isinstance(audit_key_alias_lists, list):
            raise TypeError("Expected argument 'audit_key_alias_lists' to be a list")
        pulumi.set(__self__, "audit_key_alias_lists", audit_key_alias_lists)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)

    @property
    @pulumi.getter(name="auditKeyAliasLists")
    def audit_key_alias_lists(self) -> Sequence['outputs.KeyAliasAuditKeyAliasListResult']:
        return pulumi.get(self, "audit_key_alias_lists")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableKeyAliasResult(KeyAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return KeyAliasResult(
            audit_key_alias_lists=self.audit_key_alias_lists,
            id=self.id,
            region=self.region,
            result_output_file=self.result_output_file)


def key_alias(region: Optional[str] = None,
              result_output_file: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableKeyAliasResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['region'] = region
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Audit/keyAlias:KeyAlias', __args__, opts=opts, typ=KeyAliasResult).value

    return AwaitableKeyAliasResult(
        audit_key_alias_lists=__ret__.audit_key_alias_lists,
        id=__ret__.id,
        region=__ret__.region,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(key_alias)
def key_alias_output(region: Optional[pulumi.Input[str]] = None,
                     result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[KeyAliasResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
