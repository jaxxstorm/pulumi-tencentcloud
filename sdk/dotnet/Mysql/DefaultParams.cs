// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Mysql
{
    public static class DefaultParams
    {
        public static Task<DefaultParamsResult> InvokeAsync(DefaultParamsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<DefaultParamsResult>("tencentcloud:Mysql/defaultParams:DefaultParams", args ?? new DefaultParamsArgs(), options.WithDefaults());

        public static Output<DefaultParamsResult> Invoke(DefaultParamsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<DefaultParamsResult>("tencentcloud:Mysql/defaultParams:DefaultParams", args ?? new DefaultParamsInvokeArgs(), options.WithDefaults());
    }


    public sealed class DefaultParamsArgs : Pulumi.InvokeArgs
    {
        [Input("dbVersion")]
        public string? DbVersion { get; set; }

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public DefaultParamsArgs()
        {
        }
    }

    public sealed class DefaultParamsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("dbVersion")]
        public Input<string>? DbVersion { get; set; }

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public DefaultParamsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class DefaultParamsResult
    {
        public readonly string? DbVersion;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.DefaultParamsParamListResult> ParamLists;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private DefaultParamsResult(
            string? dbVersion,

            string id,

            ImmutableArray<Outputs.DefaultParamsParamListResult> paramLists,

            string? resultOutputFile)
        {
            DbVersion = dbVersion;
            Id = id;
            ParamLists = paramLists;
            ResultOutputFile = resultOutputFile;
        }
    }
}
