// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu.Inputs
{

    public sealed class CCPolicyV2CcPrecisionReqLimitPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        [Input("cookie")]
        public Input<string>? Cookie { get; set; }

        [Input("executeDuration", required: true)]
        public Input<int> ExecuteDuration { get; set; } = null!;

        [Input("mode", required: true)]
        public Input<string> Mode { get; set; } = null!;

        [Input("period", required: true)]
        public Input<int> Period { get; set; } = null!;

        [Input("requestNum", required: true)]
        public Input<int> RequestNum { get; set; } = null!;

        [Input("uri")]
        public Input<string>? Uri { get; set; }

        [Input("userAgent")]
        public Input<string>? UserAgent { get; set; }

        public CCPolicyV2CcPrecisionReqLimitPolicyArgs()
        {
        }
    }
}
