// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cloud
{
    public static class APIGatewayUsagePlans
    {
        public static Task<APIGatewayUsagePlansResult> InvokeAsync(APIGatewayUsagePlansArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<APIGatewayUsagePlansResult>("tencentcloud:Cloud/aPIGatewayUsagePlans:APIGatewayUsagePlans", args ?? new APIGatewayUsagePlansArgs(), options.WithDefaults());

        public static Output<APIGatewayUsagePlansResult> Invoke(APIGatewayUsagePlansInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<APIGatewayUsagePlansResult>("tencentcloud:Cloud/aPIGatewayUsagePlans:APIGatewayUsagePlans", args ?? new APIGatewayUsagePlansInvokeArgs(), options.WithDefaults());
    }


    public sealed class APIGatewayUsagePlansArgs : Pulumi.InvokeArgs
    {
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        [Input("usagePlanId")]
        public string? UsagePlanId { get; set; }

        [Input("usagePlanName")]
        public string? UsagePlanName { get; set; }

        public APIGatewayUsagePlansArgs()
        {
        }
    }

    public sealed class APIGatewayUsagePlansInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        [Input("usagePlanId")]
        public Input<string>? UsagePlanId { get; set; }

        [Input("usagePlanName")]
        public Input<string>? UsagePlanName { get; set; }

        public APIGatewayUsagePlansInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class APIGatewayUsagePlansResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.APIGatewayUsagePlansListResult> Lists;
        public readonly string? ResultOutputFile;
        public readonly string? UsagePlanId;
        public readonly string? UsagePlanName;

        [OutputConstructor]
        private APIGatewayUsagePlansResult(
            string id,

            ImmutableArray<Outputs.APIGatewayUsagePlansListResult> lists,

            string? resultOutputFile,

            string? usagePlanId,

            string? usagePlanName)
        {
            Id = id;
            Lists = lists;
            ResultOutputFile = resultOutputFile;
            UsagePlanId = usagePlanId;
            UsagePlanName = usagePlanName;
        }
    }
}
