// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.APIGateway.Inputs
{

    public sealed class ServiceUsagePlanListGetArgs : Pulumi.ResourceArgs
    {
        [Input("apiId")]
        public Input<string>? ApiId { get; set; }

        [Input("bindType")]
        public Input<string>? BindType { get; set; }

        [Input("usagePlanId")]
        public Input<string>? UsagePlanId { get; set; }

        [Input("usagePlanName")]
        public Input<string>? UsagePlanName { get; set; }

        public ServiceUsagePlanListGetArgs()
        {
        }
    }
}
