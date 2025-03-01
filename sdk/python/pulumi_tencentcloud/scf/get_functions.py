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
    'GetFunctionsResult',
    'AwaitableGetFunctionsResult',
    'get_functions',
    'get_functions_output',
]

@pulumi.output_type
class GetFunctionsResult:
    """
    A collection of values returned by getFunctions.
    """
    def __init__(__self__, description=None, functions=None, id=None, name=None, namespace=None, result_output_file=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if functions and not isinstance(functions, list):
            raise TypeError("Expected argument 'functions' to be a list")
        pulumi.set(__self__, "functions", functions)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the SCF function.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def functions(self) -> Sequence['outputs.GetFunctionsFunctionResult']:
        """
        An information list of functions. Each element contains the following attributes:
        """
        return pulumi.get(self, "functions")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the SCF function trigger.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        Namespace of the SCF function.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        """
        Tags of the SCF function.
        """
        return pulumi.get(self, "tags")


class AwaitableGetFunctionsResult(GetFunctionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFunctionsResult(
            description=self.description,
            functions=self.functions,
            id=self.id,
            name=self.name,
            namespace=self.namespace,
            result_output_file=self.result_output_file,
            tags=self.tags)


def get_functions(description: Optional[str] = None,
                  name: Optional[str] = None,
                  namespace: Optional[str] = None,
                  result_output_file: Optional[str] = None,
                  tags: Optional[Mapping[str, Any]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFunctionsResult:
    """
    Use this data source to query SCF functions.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo_function = tencentcloud.scf.Function("fooFunction",
        handler="main.do_it",
        runtime="Python3.6",
        cos_bucket_name="scf-code-1234567890",
        cos_object_name="code.zip",
        cos_bucket_region="ap-guangzhou")
    foo_functions = tencentcloud.Scf.get_functions_output(name=foo_function.name)
    ```


    :param str description: Description of the SCF function to be queried.
    :param str name: Name of the SCF function to be queried.
    :param str namespace: Namespace of the SCF function to be queried.
    :param str result_output_file: Used to save results.
    :param Mapping[str, Any] tags: Tags of the SCF function to be queried, can use up to 10 tags.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['name'] = name
    __args__['namespace'] = namespace
    __args__['resultOutputFile'] = result_output_file
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Scf/getFunctions:getFunctions', __args__, opts=opts, typ=GetFunctionsResult).value

    return AwaitableGetFunctionsResult(
        description=__ret__.description,
        functions=__ret__.functions,
        id=__ret__.id,
        name=__ret__.name,
        namespace=__ret__.namespace,
        result_output_file=__ret__.result_output_file,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_functions)
def get_functions_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         namespace: Optional[pulumi.Input[Optional[str]]] = None,
                         result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFunctionsResult]:
    """
    Use this data source to query SCF functions.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    foo_function = tencentcloud.scf.Function("fooFunction",
        handler="main.do_it",
        runtime="Python3.6",
        cos_bucket_name="scf-code-1234567890",
        cos_object_name="code.zip",
        cos_bucket_region="ap-guangzhou")
    foo_functions = tencentcloud.Scf.get_functions_output(name=foo_function.name)
    ```


    :param str description: Description of the SCF function to be queried.
    :param str name: Name of the SCF function to be queried.
    :param str namespace: Namespace of the SCF function to be queried.
    :param str result_output_file: Used to save results.
    :param Mapping[str, Any] tags: Tags of the SCF function to be queried, can use up to 10 tags.
    """
    ...
