// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu
{
    public static class DdosPolicyCases
    {
        public static Task<DdosPolicyCasesResult> InvokeAsync(DdosPolicyCasesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<DdosPolicyCasesResult>("tencentcloud:Dayu/ddosPolicyCases:DdosPolicyCases", args ?? new DdosPolicyCasesArgs(), options.WithDefaults());

        public static Output<DdosPolicyCasesResult> Invoke(DdosPolicyCasesInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<DdosPolicyCasesResult>("tencentcloud:Dayu/ddosPolicyCases:DdosPolicyCases", args ?? new DdosPolicyCasesInvokeArgs(), options.WithDefaults());
    }


    public sealed class DdosPolicyCasesArgs : Pulumi.InvokeArgs
    {
        [Input("resourceType", required: true)]
        public string ResourceType { get; set; } = null!;

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        [Input("sceneId", required: true)]
        public string SceneId { get; set; } = null!;

        public DdosPolicyCasesArgs()
        {
        }
    }

    public sealed class DdosPolicyCasesInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("resourceType", required: true)]
        public Input<string> ResourceType { get; set; } = null!;

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        [Input("sceneId", required: true)]
        public Input<string> SceneId { get; set; } = null!;

        public DdosPolicyCasesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class DdosPolicyCasesResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.DdosPolicyCasesListResult> Lists;
        public readonly string ResourceType;
        public readonly string? ResultOutputFile;
        public readonly string SceneId;

        [OutputConstructor]
        private DdosPolicyCasesResult(
            string id,

            ImmutableArray<Outputs.DdosPolicyCasesListResult> lists,

            string resourceType,

            string? resultOutputFile,

            string sceneId)
        {
            Id = id;
            Lists = lists;
            ResourceType = resourceType;
            ResultOutputFile = resultOutputFile;
            SceneId = sceneId;
        }
    }
}
