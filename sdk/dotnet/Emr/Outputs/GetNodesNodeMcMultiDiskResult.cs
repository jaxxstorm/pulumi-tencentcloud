// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Emr.Outputs
{

    [OutputType]
    public sealed class GetNodesNodeMcMultiDiskResult
    {
        /// <summary>
        /// The number of cloud disks of this type.
        /// </summary>
        public readonly int Count;
        /// <summary>
        /// Disk type.
        /// </summary>
        public readonly int Type;
        /// <summary>
        /// The size of the cloud disk.
        /// </summary>
        public readonly int Volume;

        [OutputConstructor]
        private GetNodesNodeMcMultiDiskResult(
            int count,

            int type,

            int volume)
        {
            Count = count;
            Type = type;
            Volume = volume;
        }
    }
}
