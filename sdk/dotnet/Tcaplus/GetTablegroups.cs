// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Tcaplus
{
    public static class GetTablegroups
    {
        /// <summary>
        /// Use this data source to query table groups of the TcaplusDB cluster.
        /// </summary>
        public static Task<GetTablegroupsResult> InvokeAsync(GetTablegroupsArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTablegroupsResult>("tencentcloud:Tcaplus/getTablegroups:getTablegroups", args ?? new GetTablegroupsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query table groups of the TcaplusDB cluster.
        /// </summary>
        public static Output<GetTablegroupsResult> Invoke(GetTablegroupsInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetTablegroupsResult>("tencentcloud:Tcaplus/getTablegroups:getTablegroups", args ?? new GetTablegroupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTablegroupsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of the TcaplusDB cluster to be query.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// File for saving results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        /// <summary>
        /// Id of the table group to be query.
        /// </summary>
        [Input("tablegroupId")]
        public string? TablegroupId { get; set; }

        /// <summary>
        /// Name of the table group to be query.
        /// </summary>
        [Input("tablegroupName")]
        public string? TablegroupName { get; set; }

        public GetTablegroupsArgs()
        {
        }
    }

    public sealed class GetTablegroupsInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of the TcaplusDB cluster to be query.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// File for saving results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        /// <summary>
        /// Id of the table group to be query.
        /// </summary>
        [Input("tablegroupId")]
        public Input<string>? TablegroupId { get; set; }

        /// <summary>
        /// Name of the table group to be query.
        /// </summary>
        [Input("tablegroupName")]
        public Input<string>? TablegroupName { get; set; }

        public GetTablegroupsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetTablegroupsResult
    {
        public readonly string ClusterId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A list of table group. Each element contains the following attributes.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetTablegroupsListResult> Lists;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// Id of the table group.
        /// </summary>
        public readonly string? TablegroupId;
        /// <summary>
        /// Name of the table group.
        /// </summary>
        public readonly string? TablegroupName;

        [OutputConstructor]
        private GetTablegroupsResult(
            string clusterId,

            string id,

            ImmutableArray<Outputs.GetTablegroupsListResult> lists,

            string? resultOutputFile,

            string? tablegroupId,

            string? tablegroupName)
        {
            ClusterId = clusterId;
            Id = id;
            Lists = lists;
            ResultOutputFile = resultOutputFile;
            TablegroupId = tablegroupId;
            TablegroupName = tablegroupName;
        }
    }
}
