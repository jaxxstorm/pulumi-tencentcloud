// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Clb.Inputs
{

    public sealed class TargetGroupTargetGroupInstanceGetArgs : Pulumi.ResourceArgs
    {
        [Input("bindIp", required: true)]
        public Input<string> BindIp { get; set; } = null!;

        [Input("newPort")]
        public Input<int>? NewPort { get; set; }

        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public TargetGroupTargetGroupInstanceGetArgs()
        {
        }
    }
}
