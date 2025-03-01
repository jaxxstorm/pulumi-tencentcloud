// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cbs.Outputs
{

    [OutputType]
    public sealed class GetSnapshotPoliciesSnapshotPolicyListResult
    {
        /// <summary>
        /// Storage IDs that the snapshot policy attached.
        /// </summary>
        public readonly ImmutableArray<string> AttachedStorageIds;
        /// <summary>
        /// Create time of the snapshot policy.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Trigger hours of periodic snapshot.
        /// </summary>
        public readonly ImmutableArray<int> RepeatHours;
        /// <summary>
        /// Trigger days of periodic snapshot.
        /// </summary>
        public readonly ImmutableArray<int> RepeatWeekdays;
        /// <summary>
        /// Retention days of the snapshot.
        /// </summary>
        public readonly int RetentionDays;
        /// <summary>
        /// ID of the snapshot policy to be queried.
        /// </summary>
        public readonly string SnapshotPolicyId;
        /// <summary>
        /// Name of the snapshot policy to be queried.
        /// </summary>
        public readonly string SnapshotPolicyName;
        /// <summary>
        /// Status of the snapshot policy.
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private GetSnapshotPoliciesSnapshotPolicyListResult(
            ImmutableArray<string> attachedStorageIds,

            string createTime,

            ImmutableArray<int> repeatHours,

            ImmutableArray<int> repeatWeekdays,

            int retentionDays,

            string snapshotPolicyId,

            string snapshotPolicyName,

            string status)
        {
            AttachedStorageIds = attachedStorageIds;
            CreateTime = createTime;
            RepeatHours = repeatHours;
            RepeatWeekdays = repeatWeekdays;
            RetentionDays = retentionDays;
            SnapshotPolicyId = snapshotPolicyId;
            SnapshotPolicyName = snapshotPolicyName;
            Status = status;
        }
    }
}
