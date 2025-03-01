// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Outputs
{

    [OutputType]
    public sealed class DomainBandWidthAlertStatisticItem
    {
        /// <summary>
        /// Alert percentage.
        /// </summary>
        public readonly int? AlertPercentage;
        /// <summary>
        /// Switch alert.
        /// </summary>
        public readonly string? AlertSwitch;
        /// <summary>
        /// threshold of bps.
        /// </summary>
        public readonly int? BpsThreshold;
        /// <summary>
        /// Counter measure, values: `RETURN_404`, `RESOLVE_DNS_TO_ORIGIN`.
        /// </summary>
        public readonly string? CounterMeasure;
        /// <summary>
        /// Cycle of checking in minutes, values `60`, `1440`.
        /// </summary>
        public readonly int? Cycle;
        /// <summary>
        /// Metric.
        /// </summary>
        public readonly string? Metric;
        /// <summary>
        /// Configuration switch, available values: `on`, `off` (default).
        /// </summary>
        public readonly string Switch;
        /// <summary>
        /// Type of statistic item.
        /// </summary>
        public readonly string? Type;
        /// <summary>
        /// Time of auto unblock.
        /// </summary>
        public readonly int? UnblockTime;

        [OutputConstructor]
        private DomainBandWidthAlertStatisticItem(
            int? alertPercentage,

            string? alertSwitch,

            int? bpsThreshold,

            string? counterMeasure,

            int? cycle,

            string? metric,

            string @switch,

            string? type,

            int? unblockTime)
        {
            AlertPercentage = alertPercentage;
            AlertSwitch = alertSwitch;
            BpsThreshold = bpsThreshold;
            CounterMeasure = counterMeasure;
            Cycle = cycle;
            Metric = metric;
            Switch = @switch;
            Type = type;
            UnblockTime = unblockTime;
        }
    }
}
