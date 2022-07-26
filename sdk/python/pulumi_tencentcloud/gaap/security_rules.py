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
    'SecurityRulesResult',
    'AwaitableSecurityRulesResult',
    'security_rules',
    'security_rules_output',
]

@pulumi.output_type
class SecurityRulesResult:
    """
    A collection of values returned by SecurityRules.
    """
    def __init__(__self__, action=None, cidr_ip=None, id=None, name=None, policy_id=None, port=None, protocol=None, result_output_file=None, rule_id=None, rules=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if cidr_ip and not isinstance(cidr_ip, str):
            raise TypeError("Expected argument 'cidr_ip' to be a str")
        pulumi.set(__self__, "cidr_ip", cidr_ip)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)
        if port and not isinstance(port, str):
            raise TypeError("Expected argument 'port' to be a str")
        pulumi.set(__self__, "port", port)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if rule_id and not isinstance(rule_id, str):
            raise TypeError("Expected argument 'rule_id' to be a str")
        pulumi.set(__self__, "rule_id", rule_id)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def action(self) -> Optional[str]:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="cidrIp")
    def cidr_ip(self) -> Optional[str]:
        return pulumi.get(self, "cidr_ip")

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
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> str:
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[str]:
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.SecurityRulesRuleResult']:
        return pulumi.get(self, "rules")


class AwaitableSecurityRulesResult(SecurityRulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return SecurityRulesResult(
            action=self.action,
            cidr_ip=self.cidr_ip,
            id=self.id,
            name=self.name,
            policy_id=self.policy_id,
            port=self.port,
            protocol=self.protocol,
            result_output_file=self.result_output_file,
            rule_id=self.rule_id,
            rules=self.rules)


def security_rules(action: Optional[str] = None,
                   cidr_ip: Optional[str] = None,
                   name: Optional[str] = None,
                   policy_id: Optional[str] = None,
                   port: Optional[str] = None,
                   protocol: Optional[str] = None,
                   result_output_file: Optional[str] = None,
                   rule_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableSecurityRulesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['action'] = action
    __args__['cidrIp'] = cidr_ip
    __args__['name'] = name
    __args__['policyId'] = policy_id
    __args__['port'] = port
    __args__['protocol'] = protocol
    __args__['resultOutputFile'] = result_output_file
    __args__['ruleId'] = rule_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Gaap/securityRules:SecurityRules', __args__, opts=opts, typ=SecurityRulesResult).value

    return AwaitableSecurityRulesResult(
        action=__ret__.action,
        cidr_ip=__ret__.cidr_ip,
        id=__ret__.id,
        name=__ret__.name,
        policy_id=__ret__.policy_id,
        port=__ret__.port,
        protocol=__ret__.protocol,
        result_output_file=__ret__.result_output_file,
        rule_id=__ret__.rule_id,
        rules=__ret__.rules)


@_utilities.lift_output_func(security_rules)
def security_rules_output(action: Optional[pulumi.Input[Optional[str]]] = None,
                          cidr_ip: Optional[pulumi.Input[Optional[str]]] = None,
                          name: Optional[pulumi.Input[Optional[str]]] = None,
                          policy_id: Optional[pulumi.Input[str]] = None,
                          port: Optional[pulumi.Input[Optional[str]]] = None,
                          protocol: Optional[pulumi.Input[Optional[str]]] = None,
                          result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                          rule_id: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[SecurityRulesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
