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
    public sealed class ClusterWorkerConfigDataDisk
    {
        /// <summary>
        /// Indicate whether to auto format and mount or not. Default is `false`.
        /// </summary>
        public readonly bool? AutoFormatAndMount;
        /// <summary>
        /// The name of the device or partition to mount.
        /// </summary>
        public readonly string? DiskPartition;
        /// <summary>
        /// Volume of disk in GB. Default is `0`.
        /// </summary>
        public readonly int? DiskSize;
        /// <summary>
        /// Types of disk, available values: `CLOUD_PREMIUM` and `CLOUD_SSD` and `CLOUD_HSSD` and `CLOUD_TSSD`.
        /// </summary>
        public readonly string? DiskType;
        /// <summary>
        /// Indicates whether to encrypt data disk, default `false`.
        /// </summary>
        public readonly bool? Encrypt;
        /// <summary>
        /// File system, e.g. `ext3/ext4/xfs`.
        /// </summary>
        public readonly string? FileSystem;
        /// <summary>
        /// ID of the custom CMK in the format of UUID or `kms-abcd1234`. This parameter is used to encrypt cloud disks.
        /// </summary>
        public readonly string? KmsKeyId;
        /// <summary>
        /// Mount target.
        /// </summary>
        public readonly string? MountTarget;
        /// <summary>
        /// Data disk snapshot ID.
        /// </summary>
        public readonly string? SnapshotId;

        [OutputConstructor]
        private ClusterWorkerConfigDataDisk(
            bool? autoFormatAndMount,

            string? diskPartition,

            int? diskSize,

            string? diskType,

            bool? encrypt,

            string? fileSystem,

            string? kmsKeyId,

            string? mountTarget,

            string? snapshotId)
        {
            AutoFormatAndMount = autoFormatAndMount;
            DiskPartition = diskPartition;
            DiskSize = diskSize;
            DiskType = diskType;
            Encrypt = encrypt;
            FileSystem = fileSystem;
            KmsKeyId = kmsKeyId;
            MountTarget = mountTarget;
            SnapshotId = snapshotId;
        }
    }
}
