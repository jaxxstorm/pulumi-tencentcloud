// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Eks.Outputs
{

    [OutputType]
    public sealed class ContainerInstanceInitContainerVolumeMount
    {
        public readonly string? MountPropagation;
        public readonly string Name;
        public readonly string Path;
        public readonly bool? ReadOnly;
        public readonly string? SubPath;
        public readonly string? SubPathExpr;

        [OutputConstructor]
        private ContainerInstanceInitContainerVolumeMount(
            string? mountPropagation,

            string name,

            string path,

            bool? readOnly,

            string? subPath,

            string? subPathExpr)
        {
            MountPropagation = mountPropagation;
            Name = name;
            Path = path;
            ReadOnly = readOnly;
            SubPath = subPath;
            SubPathExpr = subPathExpr;
        }
    }
}
