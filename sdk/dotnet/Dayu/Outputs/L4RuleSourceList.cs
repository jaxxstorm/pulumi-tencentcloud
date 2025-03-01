// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu.Outputs
{

    [OutputType]
    public sealed class L4RuleSourceList
    {
        /// <summary>
        /// Source IP or domain, valid format of ip is like `1.1.1.1` and valid format of host source is like `abc.com`.
        /// </summary>
        public readonly string Source;
        /// <summary>
        /// Weight of the source, the valid value ranges from 0 to 100.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private L4RuleSourceList(
            string source,

            int weight)
        {
            Source = source;
            Weight = weight;
        }
    }
}
