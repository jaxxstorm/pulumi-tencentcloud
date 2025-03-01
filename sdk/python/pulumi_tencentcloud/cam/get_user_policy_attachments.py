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
    'GetUserPolicyAttachmentsResult',
    'AwaitableGetUserPolicyAttachmentsResult',
    'get_user_policy_attachments',
    'get_user_policy_attachments_output',
]

@pulumi.output_type
class GetUserPolicyAttachmentsResult:
    """
    A collection of values returned by getUserPolicyAttachments.
    """
    def __init__(__self__, create_mode=None, id=None, policy_id=None, policy_type=None, result_output_file=None, user_id=None, user_name=None, user_policy_attachment_lists=None):
        if create_mode and not isinstance(create_mode, int):
            raise TypeError("Expected argument 'create_mode' to be a int")
        pulumi.set(__self__, "create_mode", create_mode)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        if user_id is not None:
            warnings.warn("""It has been deprecated from version 1.59.6. Use `user_name` instead.""", DeprecationWarning)
            pulumi.log.warn("""user_id is deprecated: It has been deprecated from version 1.59.6. Use `user_name` instead.""")

        pulumi.set(__self__, "user_id", user_id)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)
        if user_policy_attachment_lists and not isinstance(user_policy_attachment_lists, list):
            raise TypeError("Expected argument 'user_policy_attachment_lists' to be a list")
        pulumi.set(__self__, "user_policy_attachment_lists", user_policy_attachment_lists)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[int]:
        """
        Mode of Creation of the CAM user policy attachment. `1` means the cam policy attachment is created by production, and the others indicate syntax strategy ways.
        """
        return pulumi.get(self, "create_mode")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[str]:
        """
        Name of CAM user.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[str]:
        """
        Type of the policy strategy. 'User' means customer strategy and 'QCS' means preset strategy.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[str]:
        """
        (**Deprecated**) It has been deprecated from version 1.59.6. Use `user_name` instead. ID of CAM user.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[str]:
        """
        Name of CAM user as unique key.
        """
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter(name="userPolicyAttachmentLists")
    def user_policy_attachment_lists(self) -> Sequence['outputs.GetUserPolicyAttachmentsUserPolicyAttachmentListResult']:
        """
        A list of CAM user policy attachments. Each element contains the following attributes:
        """
        return pulumi.get(self, "user_policy_attachment_lists")


class AwaitableGetUserPolicyAttachmentsResult(GetUserPolicyAttachmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPolicyAttachmentsResult(
            create_mode=self.create_mode,
            id=self.id,
            policy_id=self.policy_id,
            policy_type=self.policy_type,
            result_output_file=self.result_output_file,
            user_id=self.user_id,
            user_name=self.user_name,
            user_policy_attachment_lists=self.user_policy_attachment_lists)


def get_user_policy_attachments(create_mode: Optional[int] = None,
                                policy_id: Optional[str] = None,
                                policy_type: Optional[str] = None,
                                result_output_file: Optional[str] = None,
                                user_id: Optional[str] = None,
                                user_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPolicyAttachmentsResult:
    """
    Use this data source to query detailed information of CAM user policy attachments

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Cam.get_user_policy_attachments(user_id=tencentcloud_cam_user["foo"]["id"])
    bar = tencentcloud.Cam.get_user_policy_attachments(user_id=tencentcloud_cam_user["foo"]["id"],
        policy_id=tencentcloud_cam_policy["foo"]["id"])
    ```


    :param int create_mode: Mode of Creation of the CAM user policy attachment. `1` means the CAM policy attachment is created by production, and the others indicate syntax strategy ways.
    :param str policy_id: ID of CAM policy to be queried.
    :param str policy_type: Type of the policy strategy. 'User' means customer strategy and 'QCS' means preset strategy.
    :param str result_output_file: Used to save results.
    :param str user_id: It has been deprecated from version 1.59.6. Use `user_name` instead. ID of the attached CAM user to be queried.
    :param str user_name: Name of the attached CAM user as unique key to be queried.
    """
    __args__ = dict()
    __args__['createMode'] = create_mode
    __args__['policyId'] = policy_id
    __args__['policyType'] = policy_type
    __args__['resultOutputFile'] = result_output_file
    __args__['userId'] = user_id
    __args__['userName'] = user_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Cam/getUserPolicyAttachments:getUserPolicyAttachments', __args__, opts=opts, typ=GetUserPolicyAttachmentsResult).value

    return AwaitableGetUserPolicyAttachmentsResult(
        create_mode=__ret__.create_mode,
        id=__ret__.id,
        policy_id=__ret__.policy_id,
        policy_type=__ret__.policy_type,
        result_output_file=__ret__.result_output_file,
        user_id=__ret__.user_id,
        user_name=__ret__.user_name,
        user_policy_attachment_lists=__ret__.user_policy_attachment_lists)


@_utilities.lift_output_func(get_user_policy_attachments)
def get_user_policy_attachments_output(create_mode: Optional[pulumi.Input[Optional[int]]] = None,
                                       policy_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       policy_type: Optional[pulumi.Input[Optional[str]]] = None,
                                       result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                       user_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       user_name: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPolicyAttachmentsResult]:
    """
    Use this data source to query detailed information of CAM user policy attachments

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo = tencentcloud.Cam.get_user_policy_attachments(user_id=tencentcloud_cam_user["foo"]["id"])
    bar = tencentcloud.Cam.get_user_policy_attachments(user_id=tencentcloud_cam_user["foo"]["id"],
        policy_id=tencentcloud_cam_policy["foo"]["id"])
    ```


    :param int create_mode: Mode of Creation of the CAM user policy attachment. `1` means the CAM policy attachment is created by production, and the others indicate syntax strategy ways.
    :param str policy_id: ID of CAM policy to be queried.
    :param str policy_type: Type of the policy strategy. 'User' means customer strategy and 'QCS' means preset strategy.
    :param str result_output_file: Used to save results.
    :param str user_id: It has been deprecated from version 1.59.6. Use `user_name` instead. ID of the attached CAM user to be queried.
    :param str user_name: Name of the attached CAM user as unique key to be queried.
    """
    ...
