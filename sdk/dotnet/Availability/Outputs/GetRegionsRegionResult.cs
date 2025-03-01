// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Availability.Outputs
{

    [OutputType]
    public sealed class GetRegionsRegionResult
    {
        /// <summary>
        /// The description of the region, like `Guangzhou Region`.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// When specified, only the region with the exactly name match will be returned. `default` value means it consistent with the provider region.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The state of the region, indicate availability using `AVAILABLE` and `UNAVAILABLE` values.
        /// </summary>
        public readonly string State;

        [OutputConstructor]
        private GetRegionsRegionResult(
            string description,

            string name,

            string state)
        {
            Description = description;
            Name = name;
            State = state;
        }
    }
}
