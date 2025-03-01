// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Eks.Inputs
{

    public sealed class ContainerInstanceInitContainerGetArgs : Pulumi.ResourceArgs
    {
        [Input("args")]
        private InputList<string>? _args;

        /// <summary>
        /// Container launch argument list.
        /// </summary>
        public InputList<string> Args
        {
            get => _args ?? (_args = new InputList<string>());
            set => _args = value;
        }

        [Input("commands")]
        private InputList<string>? _commands;

        /// <summary>
        /// Container launch command list.
        /// </summary>
        public InputList<string> Commands
        {
            get => _commands ?? (_commands = new InputList<string>());
            set => _commands = value;
        }

        /// <summary>
        /// Number of cpu core of container.
        /// </summary>
        [Input("cpu")]
        public Input<double>? Cpu { get; set; }

        [Input("envVars")]
        private InputMap<object>? _envVars;

        /// <summary>
        /// Map of environment variables of container OS.
        /// </summary>
        public InputMap<object> EnvVars
        {
            get => _envVars ?? (_envVars = new InputMap<object>());
            set => _envVars = value;
        }

        /// <summary>
        /// Image of Container.
        /// </summary>
        [Input("image", required: true)]
        public Input<string> Image { get; set; } = null!;

        /// <summary>
        /// Memory size of container.
        /// </summary>
        [Input("memory")]
        public Input<double>? Memory { get; set; }

        /// <summary>
        /// Name of Container.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("volumeMounts")]
        private InputList<Inputs.ContainerInstanceInitContainerVolumeMountGetArgs>? _volumeMounts;

        /// <summary>
        /// List of volume mount informations.
        /// </summary>
        public InputList<Inputs.ContainerInstanceInitContainerVolumeMountGetArgs> VolumeMounts
        {
            get => _volumeMounts ?? (_volumeMounts = new InputList<Inputs.ContainerInstanceInitContainerVolumeMountGetArgs>());
            set => _volumeMounts = value;
        }

        /// <summary>
        /// Container working directory.
        /// </summary>
        [Input("workingDir")]
        public Input<string>? WorkingDir { get; set; }

        public ContainerInstanceInitContainerGetArgs()
        {
        }
    }
}
