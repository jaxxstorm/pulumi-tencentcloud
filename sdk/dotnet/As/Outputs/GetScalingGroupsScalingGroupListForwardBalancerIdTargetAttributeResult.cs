// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.As.Outputs
{

    [OutputType]
    public sealed class GetScalingGroupsScalingGroupListForwardBalancerIdTargetAttributeResult
    {
        /// <summary>
        /// Port number.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// Weight.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private GetScalingGroupsScalingGroupListForwardBalancerIdTargetAttributeResult(
            int port,

            int weight)
        {
            Port = port;
            Weight = weight;
        }
    }
}
