// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu.Outputs
{

    [OutputType]
    public sealed class L7RulesListResult
    {
        public readonly string Domain;
        public readonly int HealthCheckCode;
        public readonly int HealthCheckHealthNum;
        public readonly int HealthCheckInterval;
        public readonly string HealthCheckMethod;
        public readonly string HealthCheckPath;
        public readonly bool HealthCheckSwitch;
        public readonly int HealthCheckUnhealthNum;
        public readonly string Name;
        public readonly string Protocol;
        public readonly string RuleId;
        public readonly ImmutableArray<string> SourceLists;
        public readonly int SourceType;
        public readonly string SslId;
        public readonly int Status;
        public readonly bool Switch;
        public readonly int Threshold;

        [OutputConstructor]
        private L7RulesListResult(
            string domain,

            int healthCheckCode,

            int healthCheckHealthNum,

            int healthCheckInterval,

            string healthCheckMethod,

            string healthCheckPath,

            bool healthCheckSwitch,

            int healthCheckUnhealthNum,

            string name,

            string protocol,

            string ruleId,

            ImmutableArray<string> sourceLists,

            int sourceType,

            string sslId,

            int status,

            bool @switch,

            int threshold)
        {
            Domain = domain;
            HealthCheckCode = healthCheckCode;
            HealthCheckHealthNum = healthCheckHealthNum;
            HealthCheckInterval = healthCheckInterval;
            HealthCheckMethod = healthCheckMethod;
            HealthCheckPath = healthCheckPath;
            HealthCheckSwitch = healthCheckSwitch;
            HealthCheckUnhealthNum = healthCheckUnhealthNum;
            Name = name;
            Protocol = protocol;
            RuleId = ruleId;
            SourceLists = sourceLists;
            SourceType = sourceType;
            SslId = sslId;
            Status = status;
            Switch = @switch;
            Threshold = threshold;
        }
    }
}
