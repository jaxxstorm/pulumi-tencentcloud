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
    public sealed class GetScalingGroupsScalingGroupListForwardBalancerIdResult
    {
        /// <summary>
        /// Listener ID for application load balancers.
        /// </summary>
        public readonly string ListenerId;
        /// <summary>
        /// ID of available load balancers.
        /// </summary>
        public readonly string LoadBalancerId;
        /// <summary>
        /// ID of forwarding rules.
        /// </summary>
        public readonly string LocationId;
        /// <summary>
        /// Attribute list of target rules.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetScalingGroupsScalingGroupListForwardBalancerIdTargetAttributeResult> TargetAttributes;

        [OutputConstructor]
        private GetScalingGroupsScalingGroupListForwardBalancerIdResult(
            string listenerId,

            string loadBalancerId,

            string locationId,

            ImmutableArray<Outputs.GetScalingGroupsScalingGroupListForwardBalancerIdTargetAttributeResult> targetAttributes)
        {
            ListenerId = listenerId;
            LoadBalancerId = loadBalancerId;
            LocationId = locationId;
            TargetAttributes = targetAttributes;
        }
    }
}
