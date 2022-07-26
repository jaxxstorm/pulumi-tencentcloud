// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Sqlserver
{
    public static class ReadonlyGroups
    {
        public static Task<ReadonlyGroupsResult> InvokeAsync(ReadonlyGroupsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<ReadonlyGroupsResult>("tencentcloud:Sqlserver/readonlyGroups:ReadonlyGroups", args ?? new ReadonlyGroupsArgs(), options.WithDefaults());

        public static Output<ReadonlyGroupsResult> Invoke(ReadonlyGroupsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<ReadonlyGroupsResult>("tencentcloud:Sqlserver/readonlyGroups:ReadonlyGroups", args ?? new ReadonlyGroupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class ReadonlyGroupsArgs : Pulumi.InvokeArgs
    {
        [Input("masterInstanceId")]
        public string? MasterInstanceId { get; set; }

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public ReadonlyGroupsArgs()
        {
        }
    }

    public sealed class ReadonlyGroupsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("masterInstanceId")]
        public Input<string>? MasterInstanceId { get; set; }

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public ReadonlyGroupsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class ReadonlyGroupsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.ReadonlyGroupsListResult> Lists;
        public readonly string? MasterInstanceId;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private ReadonlyGroupsResult(
            string id,

            ImmutableArray<Outputs.ReadonlyGroupsListResult> lists,

            string? masterInstanceId,

            string? resultOutputFile)
        {
            Id = id;
            Lists = lists;
            MasterInstanceId = masterInstanceId;
            ResultOutputFile = resultOutputFile;
        }
    }
}
