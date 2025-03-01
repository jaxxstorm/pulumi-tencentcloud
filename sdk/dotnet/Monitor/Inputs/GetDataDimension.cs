// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Monitor.Inputs
{

    public sealed class GetDataDimensionArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Instance dimension name, eg: `InstanceId` for cvm.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// Instance dimension value, eg: `ins-j0hk02zo` for cvm.
        /// </summary>
        [Input("value", required: true)]
        public string Value { get; set; } = null!;

        public GetDataDimensionArgs()
        {
        }
    }
}
