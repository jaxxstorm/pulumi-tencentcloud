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
    public sealed class ClusterEventPersistence
    {
        /// <summary>
        /// Specify weather the Event Persistence enabled.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// Specify id of existing CLS log set, or auto create a new set by leave it empty.
        /// </summary>
        public readonly string? LogSetId;
        /// <summary>
        /// Specify id of existing CLS log topic, or auto create a new topic by leave it empty.
        /// </summary>
        public readonly string? TopicId;

        [OutputConstructor]
        private ClusterEventPersistence(
            bool enabled,

            string? logSetId,

            string? topicId)
        {
            Enabled = enabled;
            LogSetId = logSetId;
            TopicId = topicId;
        }
    }
}
