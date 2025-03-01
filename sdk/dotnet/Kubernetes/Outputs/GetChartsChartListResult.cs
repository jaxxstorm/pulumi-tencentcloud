// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Kubernetes.Outputs
{

    [OutputType]
    public sealed class GetChartsChartListResult
    {
        /// <summary>
        /// Label of chart.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Label;
        /// <summary>
        /// Chart latest version.
        /// </summary>
        public readonly string LatestVersion;
        /// <summary>
        /// Name of chart.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetChartsChartListResult(
            ImmutableDictionary<string, object> label,

            string latestVersion,

            string name)
        {
            Label = label;
            LatestVersion = latestVersion;
            Name = name;
        }
    }
}
