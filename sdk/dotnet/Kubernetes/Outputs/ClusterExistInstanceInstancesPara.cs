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
    public sealed class ClusterExistInstanceInstancesPara
    {
        /// <summary>
        /// Cluster IDs.
        /// </summary>
        public readonly ImmutableArray<string> InstanceIds;

        [OutputConstructor]
        private ClusterExistInstanceInstancesPara(ImmutableArray<string> instanceIds)
        {
            InstanceIds = instanceIds;
        }
    }
}
