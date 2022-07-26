// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cloud.Outputs
{

    [OutputType]
    public sealed class APIGatewayIpStrategyListResult
    {
        public readonly ImmutableArray<Outputs.APIGatewayIpStrategyListAttachListResult> AttachLists;
        public readonly int BindApiTotalCount;
        public readonly string CreateTime;
        public readonly string IpList;
        public readonly string ModifyTime;
        public readonly string ServiceId;
        public readonly string StrategyId;
        public readonly string StrategyName;
        public readonly string StrategyType;

        [OutputConstructor]
        private APIGatewayIpStrategyListResult(
            ImmutableArray<Outputs.APIGatewayIpStrategyListAttachListResult> attachLists,

            int bindApiTotalCount,

            string createTime,

            string ipList,

            string modifyTime,

            string serviceId,

            string strategyId,

            string strategyName,

            string strategyType)
        {
            AttachLists = attachLists;
            BindApiTotalCount = bindApiTotalCount;
            CreateTime = createTime;
            IpList = ipList;
            ModifyTime = modifyTime;
            ServiceId = serviceId;
            StrategyId = strategyId;
            StrategyName = strategyName;
            StrategyType = strategyType;
        }
    }
}
