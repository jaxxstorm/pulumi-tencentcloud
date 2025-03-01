// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Mongodb.Outputs
{

    [OutputType]
    public sealed class GetZoneConfigListResult
    {
        /// <summary>
        /// The available zone of the Mongodb.
        /// </summary>
        public readonly string AvailableZone;
        /// <summary>
        /// Type of Mongodb cluster.
        /// </summary>
        public readonly string ClusterType;
        /// <summary>
        /// Number of cpu's core.
        /// </summary>
        public readonly int Cpu;
        /// <summary>
        /// Default disk size.
        /// </summary>
        public readonly int DefaultStorage;
        /// <summary>
        /// Version of the Mongodb version.
        /// </summary>
        public readonly string EngineVersion;
        /// <summary>
        /// Type of Mongodb instance.
        /// </summary>
        public readonly string MachineType;
        /// <summary>
        /// Maximum replicate set num for sharding cluster.
        /// </summary>
        public readonly int MaxReplicateSetNum;
        /// <summary>
        /// Maximum size of the disk.
        /// </summary>
        public readonly int MaxStorage;
        /// <summary>
        /// Memory size.
        /// </summary>
        public readonly int Memory;
        /// <summary>
        /// Minimum replicate set num for sharding cluster.
        /// </summary>
        public readonly int MinReplicateSetNum;
        /// <summary>
        /// Minimum sie of the disk.
        /// </summary>
        public readonly int MinStorage;

        [OutputConstructor]
        private GetZoneConfigListResult(
            string availableZone,

            string clusterType,

            int cpu,

            int defaultStorage,

            string engineVersion,

            string machineType,

            int maxReplicateSetNum,

            int maxStorage,

            int memory,

            int minReplicateSetNum,

            int minStorage)
        {
            AvailableZone = availableZone;
            ClusterType = clusterType;
            Cpu = cpu;
            DefaultStorage = defaultStorage;
            EngineVersion = engineVersion;
            MachineType = machineType;
            MaxReplicateSetNum = maxReplicateSetNum;
            MaxStorage = maxStorage;
            Memory = memory;
            MinReplicateSetNum = minReplicateSetNum;
            MinStorage = minStorage;
        }
    }
}
