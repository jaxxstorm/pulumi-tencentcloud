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
    'GetCcHttpPoliciesResult',
    'AwaitableGetCcHttpPoliciesResult',
    'get_cc_http_policies',
    'get_cc_http_policies_output',
]

@pulumi.output_type
class GetCcHttpPoliciesResult:
    """
    A collection of values returned by getCcHttpPolicies.
    """
    def __init__(__self__, id=None, lists=None, name=None, policy_id=None, resource_id=None, resource_type=None, result_output_file=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lists and not isinstance(lists, list):
            raise TypeError("Expected argument 'lists' to be a list")
        pulumi.set(__self__, "lists", lists)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lists(self) -> Sequence['outputs.GetCcHttpPoliciesListResult']:
        """
        A list of CC http policies. Each element contains the following attributes:
        """
        return pulumi.get(self, "lists")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the CC self-define http policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[str]:
        """
        ID of the CC self-define http policy.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        ID of the resource that the CC self-define http policy works for.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> str:
        """
        Type of the resource that the CC self-define http policy works for.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableGetCcHttpPoliciesResult(GetCcHttpPoliciesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCcHttpPoliciesResult(
            id=self.id,
            lists=self.lists,
            name=self.name,
            policy_id=self.policy_id,
            resource_id=self.resource_id,
            resource_type=self.resource_type,
            result_output_file=self.result_output_file)


def get_cc_http_policies(name: Optional[str] = None,
                         policy_id: Optional[str] = None,
                         resource_id: Optional[str] = None,
                         resource_type: Optional[str] = None,
                         result_output_file: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCcHttpPoliciesResult:
    """
    Use this data source to query dayu CC http policies

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    id_test = tencentcloud.Dayu.get_cc_http_policies(resource_type=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_type"],
        resource_id=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_id"],
        policy_id=tencentcloud_dayu_cc_http_policy["test_policy"]["policy_id"])
    name_test = tencentcloud.Dayu.get_cc_http_policies(resource_type=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_type"],
        resource_id=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_id"],
        name=tencentcloud_dayu_cc_http_policy["test_policy"]["name"])
    ```


    :param str name: Name of the CC http policy to be queried.
    :param str policy_id: Id of the CC http policy to be queried.
    :param str resource_id: ID of the resource that the CC http policy works for.
    :param str resource_type: Type of the resource that the CC http policy works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
    :param str result_output_file: Used to save results.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['policyId'] = policy_id
    __args__['resourceId'] = resource_id
    __args__['resourceType'] = resource_type
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Dayu/getCcHttpPolicies:getCcHttpPolicies', __args__, opts=opts, typ=GetCcHttpPoliciesResult).value

    return AwaitableGetCcHttpPoliciesResult(
        id=__ret__.id,
        lists=__ret__.lists,
        name=__ret__.name,
        policy_id=__ret__.policy_id,
        resource_id=__ret__.resource_id,
        resource_type=__ret__.resource_type,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(get_cc_http_policies)
def get_cc_http_policies_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                                policy_id: Optional[pulumi.Input[Optional[str]]] = None,
                                resource_id: Optional[pulumi.Input[str]] = None,
                                resource_type: Optional[pulumi.Input[str]] = None,
                                result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCcHttpPoliciesResult]:
    """
    Use this data source to query dayu CC http policies

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    id_test = tencentcloud.Dayu.get_cc_http_policies(resource_type=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_type"],
        resource_id=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_id"],
        policy_id=tencentcloud_dayu_cc_http_policy["test_policy"]["policy_id"])
    name_test = tencentcloud.Dayu.get_cc_http_policies(resource_type=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_type"],
        resource_id=tencentcloud_dayu_cc_http_policy["test_policy"]["resource_id"],
        name=tencentcloud_dayu_cc_http_policy["test_policy"]["name"])
    ```


    :param str name: Name of the CC http policy to be queried.
    :param str policy_id: Id of the CC http policy to be queried.
    :param str resource_id: ID of the resource that the CC http policy works for.
    :param str resource_type: Type of the resource that the CC http policy works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
    :param str result_output_file: Used to save results.
    """
    ...
