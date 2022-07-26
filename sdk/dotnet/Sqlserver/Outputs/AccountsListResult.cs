// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Sqlserver.Outputs
{

    [OutputType]
    public sealed class AccountsListResult
    {
        public readonly string CreateTime;
        public readonly string InstanceId;
        public readonly string Name;
        public readonly string Remark;
        public readonly int Status;
        public readonly string UpdateTime;

        [OutputConstructor]
        private AccountsListResult(
            string createTime,

            string instanceId,

            string name,

            string remark,

            int status,

            string updateTime)
        {
            CreateTime = createTime;
            InstanceId = instanceId;
            Name = name;
            Remark = remark;
            Status = status;
            UpdateTime = updateTime;
        }
    }
}
