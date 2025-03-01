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
    public sealed class UrlPurgePurgeHistory
    {
        /// <summary>
        /// Purge task create time.
        /// </summary>
        public readonly string? CreateTime;
        /// <summary>
        /// Purge flush type of `flush` or `delete`.
        /// </summary>
        public readonly string? FlushType;
        /// <summary>
        /// Purge category in of `url` or `path`.
        /// </summary>
        public readonly string? PurgeType;
        /// <summary>
        /// Purge status of `fail`, `done`, `process`.
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// Task id of last operation.
        /// </summary>
        public readonly string? TaskId;
        /// <summary>
        /// Purge url.
        /// </summary>
        public readonly string? Url;

        [OutputConstructor]
        private UrlPurgePurgeHistory(
            string? createTime,

            string? flushType,

            string? purgeType,

            string? status,

            string? taskId,

            string? url)
        {
            CreateTime = createTime;
            FlushType = flushType;
            PurgeType = purgeType;
            Status = status;
            TaskId = taskId;
            Url = url;
        }
    }
}
