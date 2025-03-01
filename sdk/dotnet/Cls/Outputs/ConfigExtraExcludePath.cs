// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cls.Outputs
{

    [OutputType]
    public sealed class ConfigExtraExcludePath
    {
        /// <summary>
        /// Type. Valid values: File, Path.
        /// </summary>
        public readonly string? Type;
        /// <summary>
        /// Specific content corresponding to Type.
        /// </summary>
        public readonly string? Value;

        [OutputConstructor]
        private ConfigExtraExcludePath(
            string? type,

            string? value)
        {
            Type = type;
            Value = value;
        }
    }
}
