// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Inputs
{

    public sealed class CdnDomainDownstreamCappingCappingRuleGetArgs : Pulumi.ResourceArgs
    {
        [Input("kbpsThreshold", required: true)]
        public Input<int> KbpsThreshold { get; set; } = null!;

        [Input("rulePaths", required: true)]
        private InputList<string>? _rulePaths;
        public InputList<string> RulePaths
        {
            get => _rulePaths ?? (_rulePaths = new InputList<string>());
            set => _rulePaths = value;
        }

        [Input("ruleType", required: true)]
        public Input<string> RuleType { get; set; } = null!;

        public CdnDomainDownstreamCappingCappingRuleGetArgs()
        {
        }
    }
}
