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
    'SecretVersionsResult',
    'AwaitableSecretVersionsResult',
    'secret_versions',
    'secret_versions_output',
]

@pulumi.output_type
class SecretVersionsResult:
    """
    A collection of values returned by SecretVersions.
    """
    def __init__(__self__, id=None, result_output_file=None, secret_name=None, secret_version_lists=None, version_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if secret_name and not isinstance(secret_name, str):
            raise TypeError("Expected argument 'secret_name' to be a str")
        pulumi.set(__self__, "secret_name", secret_name)
        if secret_version_lists and not isinstance(secret_version_lists, list):
            raise TypeError("Expected argument 'secret_version_lists' to be a list")
        pulumi.set(__self__, "secret_version_lists", secret_version_lists)
        if version_id and not isinstance(version_id, str):
            raise TypeError("Expected argument 'version_id' to be a str")
        pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> str:
        return pulumi.get(self, "secret_name")

    @property
    @pulumi.getter(name="secretVersionLists")
    def secret_version_lists(self) -> Sequence['outputs.SecretVersionsSecretVersionListResult']:
        return pulumi.get(self, "secret_version_lists")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[str]:
        return pulumi.get(self, "version_id")


class AwaitableSecretVersionsResult(SecretVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return SecretVersionsResult(
            id=self.id,
            result_output_file=self.result_output_file,
            secret_name=self.secret_name,
            secret_version_lists=self.secret_version_lists,
            version_id=self.version_id)


def secret_versions(result_output_file: Optional[str] = None,
                    secret_name: Optional[str] = None,
                    version_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableSecretVersionsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['resultOutputFile'] = result_output_file
    __args__['secretName'] = secret_name
    __args__['versionId'] = version_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Ssm/secretVersions:SecretVersions', __args__, opts=opts, typ=SecretVersionsResult).value

    return AwaitableSecretVersionsResult(
        id=__ret__.id,
        result_output_file=__ret__.result_output_file,
        secret_name=__ret__.secret_name,
        secret_version_lists=__ret__.secret_version_lists,
        version_id=__ret__.version_id)


@_utilities.lift_output_func(secret_versions)
def secret_versions_output(result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                           secret_name: Optional[pulumi.Input[str]] = None,
                           version_id: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[SecretVersionsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
