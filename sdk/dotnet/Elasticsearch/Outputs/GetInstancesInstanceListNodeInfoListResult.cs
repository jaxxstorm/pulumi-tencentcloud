// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Elasticsearch.Outputs
{

    [OutputType]
    public sealed class GetInstancesInstanceListNodeInfoListResult
    {
        /// <summary>
        /// Node disk size.
        /// </summary>
        public readonly int DiskSize;
        /// <summary>
        /// Node disk type.
        /// </summary>
        public readonly string DiskType;
        /// <summary>
        /// Decides this disk encrypted or not.
        /// </summary>
        public readonly bool Encrypt;
        /// <summary>
        /// Number of nodes.
        /// </summary>
        public readonly int NodeNum;
        /// <summary>
        /// Node specification.
        /// </summary>
        public readonly string NodeType;
        /// <summary>
        /// Node type.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetInstancesInstanceListNodeInfoListResult(
            int diskSize,

            string diskType,

            bool encrypt,

            int nodeNum,

            string nodeType,

            string type)
        {
            DiskSize = diskSize;
            DiskType = diskType;
            Encrypt = encrypt;
            NodeNum = nodeNum;
            NodeType = nodeType;
            Type = type;
        }
    }
}
