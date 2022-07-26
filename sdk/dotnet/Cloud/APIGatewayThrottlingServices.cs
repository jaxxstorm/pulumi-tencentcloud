// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cloud
{
    public static class APIGatewayThrottlingServices
    {
        public static Task<APIGatewayThrottlingServicesResult> InvokeAsync(APIGatewayThrottlingServicesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<APIGatewayThrottlingServicesResult>("tencentcloud:Cloud/aPIGatewayThrottlingServices:APIGatewayThrottlingServices", args ?? new APIGatewayThrottlingServicesArgs(), options.WithDefaults());

        public static Output<APIGatewayThrottlingServicesResult> Invoke(APIGatewayThrottlingServicesInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<APIGatewayThrottlingServicesResult>("tencentcloud:Cloud/aPIGatewayThrottlingServices:APIGatewayThrottlingServices", args ?? new APIGatewayThrottlingServicesInvokeArgs(), options.WithDefaults());
    }


    public sealed class APIGatewayThrottlingServicesArgs : Pulumi.InvokeArgs
    {
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        [Input("serviceId")]
        public string? ServiceId { get; set; }

        public APIGatewayThrottlingServicesArgs()
        {
        }
    }

    public sealed class APIGatewayThrottlingServicesInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        [Input("serviceId")]
        public Input<string>? ServiceId { get; set; }

        public APIGatewayThrottlingServicesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class APIGatewayThrottlingServicesResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.APIGatewayThrottlingServicesListResult> Lists;
        public readonly string? ResultOutputFile;
        public readonly string? ServiceId;

        [OutputConstructor]
        private APIGatewayThrottlingServicesResult(
            string id,

            ImmutableArray<Outputs.APIGatewayThrottlingServicesListResult> lists,

            string? resultOutputFile,

            string? serviceId)
        {
            Id = id;
            Lists = lists;
            ResultOutputFile = resultOutputFile;
            ServiceId = serviceId;
        }
    }
}
