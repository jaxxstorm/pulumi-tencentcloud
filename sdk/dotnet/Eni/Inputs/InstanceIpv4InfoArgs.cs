// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Eni.Inputs
{

    public sealed class InstanceIpv4InfoArgs : Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("ip")]
        public Input<string>? Ip { get; set; }

        [Input("primary")]
        public Input<bool>? Primary { get; set; }

        public InstanceIpv4InfoArgs()
        {
        }
    }
}
