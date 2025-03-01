// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cls.Inputs
{

    public sealed class ConfigExtraContainerStdoutWorkloadGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// container name.
        /// </summary>
        [Input("container")]
        public Input<string>? Container { get; set; }

        /// <summary>
        /// workload type.
        /// </summary>
        [Input("kind", required: true)]
        public Input<string> Kind { get; set; } = null!;

        /// <summary>
        /// workload name.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// namespace.
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        public ConfigExtraContainerStdoutWorkloadGetArgs()
        {
        }
    }
}
