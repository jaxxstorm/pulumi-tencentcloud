// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Mongodb.Inputs
{

    public sealed class InstanceStandbyInstanceListGetArgs : Pulumi.ResourceArgs
    {
        [Input("standbyInstanceId")]
        public Input<string>? StandbyInstanceId { get; set; }

        [Input("standbyInstanceRegion")]
        public Input<string>? StandbyInstanceRegion { get; set; }

        public InstanceStandbyInstanceListGetArgs()
        {
        }
    }
}
