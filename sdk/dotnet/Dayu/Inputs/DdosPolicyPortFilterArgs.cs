// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu.Inputs
{

    public sealed class DdosPolicyPortFilterArgs : Pulumi.ResourceArgs
    {
        [Input("action")]
        public Input<string>? Action { get; set; }

        [Input("endPort")]
        public Input<int>? EndPort { get; set; }

        [Input("kind")]
        public Input<int>? Kind { get; set; }

        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        [Input("startPort")]
        public Input<int>? StartPort { get; set; }

        public DdosPolicyPortFilterArgs()
        {
        }
    }
}
