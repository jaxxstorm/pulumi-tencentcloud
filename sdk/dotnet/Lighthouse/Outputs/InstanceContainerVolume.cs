// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Lighthouse.Outputs
{

    [OutputType]
    public sealed class InstanceContainerVolume
    {
        /// <summary>
        /// Container path.
        /// </summary>
        public readonly string ContainerPath;
        /// <summary>
        /// Host path.
        /// </summary>
        public readonly string HostPath;

        [OutputConstructor]
        private InstanceContainerVolume(
            string containerPath,

            string hostPath)
        {
            ContainerPath = containerPath;
            HostPath = hostPath;
        }
    }
}
