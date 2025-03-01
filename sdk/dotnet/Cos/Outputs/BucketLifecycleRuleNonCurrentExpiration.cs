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
    public sealed class BucketLifecycleRuleNonCurrentExpiration
    {
        /// <summary>
        /// Number of days after non current object creation when the specific rule action takes effect. The maximum value is 3650.
        /// </summary>
        public readonly int? NonCurrentDays;

        [OutputConstructor]
        private BucketLifecycleRuleNonCurrentExpiration(int? nonCurrentDays)
        {
            NonCurrentDays = nonCurrentDays;
        }
    }
}
