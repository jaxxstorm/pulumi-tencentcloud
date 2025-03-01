// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cos.Outputs
{

    [OutputType]
    public sealed class BucketLifecycleRuleExpiration
    {
        /// <summary>
        /// Specifies the date after which you want the corresponding action to take effect.
        /// </summary>
        public readonly string? Date;
        /// <summary>
        /// Specifies the number of days after object creation when the specific rule action takes effect.
        /// </summary>
        public readonly int? Days;
        /// <summary>
        /// Indicates whether the delete marker of an expired object will be removed.
        /// </summary>
        public readonly bool? DeleteMarker;

        [OutputConstructor]
        private BucketLifecycleRuleExpiration(
            string? date,

            int? days,

            bool? deleteMarker)
        {
            Date = date;
            Days = days;
            DeleteMarker = deleteMarker;
        }
    }
}
