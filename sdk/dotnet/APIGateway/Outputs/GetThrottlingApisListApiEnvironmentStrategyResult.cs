// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.ApiGateway.Outputs
{

    [OutputType]
    public sealed class GetThrottlingApisListApiEnvironmentStrategyResult
    {
        /// <summary>
        /// Unique API ID.
        /// </summary>
        public readonly string ApiId;
        /// <summary>
        /// Custom API name.
        /// </summary>
        public readonly string ApiName;
        /// <summary>
        /// API method.
        /// </summary>
        public readonly string Method;
        /// <summary>
        /// API path.
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// Environment throttling information.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetThrottlingApisListApiEnvironmentStrategyStrategyListResult> StrategyLists;

        [OutputConstructor]
        private GetThrottlingApisListApiEnvironmentStrategyResult(
            string apiId,

            string apiName,

            string method,

            string path,

            ImmutableArray<Outputs.GetThrottlingApisListApiEnvironmentStrategyStrategyListResult> strategyLists)
        {
            ApiId = apiId;
            ApiName = apiName;
            Method = method;
            Path = path;
            StrategyLists = strategyLists;
        }
    }
}
