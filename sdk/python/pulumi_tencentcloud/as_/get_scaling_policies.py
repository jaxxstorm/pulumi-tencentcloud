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
    'GetScalingPoliciesResult',
    'AwaitableGetScalingPoliciesResult',
    'get_scaling_policies',
    'get_scaling_policies_output',
]

@pulumi.output_type
class GetScalingPoliciesResult:
    """
    A collection of values returned by getScalingPolicies.
    """
    def __init__(__self__, id=None, policy_name=None, result_output_file=None, scaling_group_id=None, scaling_policy_id=None, scaling_policy_lists=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_name and not isinstance(policy_name, str):
            raise TypeError("Expected argument 'policy_name' to be a str")
        pulumi.set(__self__, "policy_name", policy_name)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if scaling_group_id and not isinstance(scaling_group_id, str):
            raise TypeError("Expected argument 'scaling_group_id' to be a str")
        pulumi.set(__self__, "scaling_group_id", scaling_group_id)
        if scaling_policy_id and not isinstance(scaling_policy_id, str):
            raise TypeError("Expected argument 'scaling_policy_id' to be a str")
        pulumi.set(__self__, "scaling_policy_id", scaling_policy_id)
        if scaling_policy_lists and not isinstance(scaling_policy_lists, list):
            raise TypeError("Expected argument 'scaling_policy_lists' to be a list")
        pulumi.set(__self__, "scaling_policy_lists", scaling_policy_lists)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[str]:
        """
        Scaling policy name.
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> Optional[str]:
        """
        Scaling policy ID.
        """
        return pulumi.get(self, "scaling_group_id")

    @property
    @pulumi.getter(name="scalingPolicyId")
    def scaling_policy_id(self) -> Optional[str]:
        return pulumi.get(self, "scaling_policy_id")

    @property
    @pulumi.getter(name="scalingPolicyLists")
    def scaling_policy_lists(self) -> Sequence['outputs.GetScalingPoliciesScalingPolicyListResult']:
        """
        A list of scaling policy. Each element contains the following attributes:
        """
        return pulumi.get(self, "scaling_policy_lists")


class AwaitableGetScalingPoliciesResult(GetScalingPoliciesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScalingPoliciesResult(
            id=self.id,
            policy_name=self.policy_name,
            result_output_file=self.result_output_file,
            scaling_group_id=self.scaling_group_id,
            scaling_policy_id=self.scaling_policy_id,
            scaling_policy_lists=self.scaling_policy_lists)


def get_scaling_policies(policy_name: Optional[str] = None,
                         result_output_file: Optional[str] = None,
                         scaling_group_id: Optional[str] = None,
                         scaling_policy_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScalingPoliciesResult:
    """
    Use this data source to query detailed information of scaling policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    as_scaling_policies = tencentcloud.As.get_scaling_policies(result_output_file="mytestpath",
        scaling_policy_id="asg-mvyghxu7")
    ```


    :param str policy_name: Scaling policy name.
    :param str result_output_file: Used to save results.
    :param str scaling_group_id: Scaling group ID.
    :param str scaling_policy_id: Scaling policy ID.
    """
    __args__ = dict()
    __args__['policyName'] = policy_name
    __args__['resultOutputFile'] = result_output_file
    __args__['scalingGroupId'] = scaling_group_id
    __args__['scalingPolicyId'] = scaling_policy_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:As/getScalingPolicies:getScalingPolicies', __args__, opts=opts, typ=GetScalingPoliciesResult).value

    return AwaitableGetScalingPoliciesResult(
        id=__ret__.id,
        policy_name=__ret__.policy_name,
        result_output_file=__ret__.result_output_file,
        scaling_group_id=__ret__.scaling_group_id,
        scaling_policy_id=__ret__.scaling_policy_id,
        scaling_policy_lists=__ret__.scaling_policy_lists)


@_utilities.lift_output_func(get_scaling_policies)
def get_scaling_policies_output(policy_name: Optional[pulumi.Input[Optional[str]]] = None,
                                result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                scaling_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                                scaling_policy_id: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScalingPoliciesResult]:
    """
    Use this data source to query detailed information of scaling policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    as_scaling_policies = tencentcloud.As.get_scaling_policies(result_output_file="mytestpath",
        scaling_policy_id="asg-mvyghxu7")
    ```


    :param str policy_name: Scaling policy name.
    :param str result_output_file: Used to save results.
    :param str scaling_group_id: Scaling group ID.
    :param str scaling_policy_id: Scaling policy ID.
    """
    ...
