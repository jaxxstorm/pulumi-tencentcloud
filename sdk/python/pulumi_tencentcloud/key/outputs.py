# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetPairsKeyPairListResult',
]

@pulumi.output_type
class GetPairsKeyPairListResult(dict):
    def __init__(__self__, *,
                 create_time: str,
                 key_id: str,
                 key_name: str,
                 project_id: int,
                 public_key: str):
        """
        :param str create_time: Creation time of the key pair.
        :param str key_id: ID of the key pair to be queried.
        :param str key_name: Name of the key pair to be queried. Support regular expression search, only `^` and `$` are supported.
        :param int project_id: Project ID of the key pair to be queried.
        :param str public_key: public key of the key pair.
        """
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "key_id", key_id)
        pulumi.set(__self__, "key_name", key_name)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "public_key", public_key)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of the key pair.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> str:
        """
        ID of the key pair to be queried.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        Name of the key pair to be queried. Support regular expression search, only `^` and `$` are supported.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> int:
        """
        Project ID of the key pair to be queried.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        public key of the key pair.
        """
        return pulumi.get(self, "public_key")


