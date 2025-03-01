// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Ckafka.Outputs
{

    [OutputType]
    public sealed class GetInstancesFilterResult
    {
        /// <summary>
        /// The field that needs to be filtered.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The filtered value of the field.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetInstancesFilterResult(
            string name,

            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
}
