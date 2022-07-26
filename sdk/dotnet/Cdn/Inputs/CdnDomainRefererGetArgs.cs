// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Inputs
{

    public sealed class CdnDomainRefererGetArgs : Pulumi.ResourceArgs
    {
        [Input("refererRules")]
        private InputList<Inputs.CdnDomainRefererRefererRuleGetArgs>? _refererRules;
        public InputList<Inputs.CdnDomainRefererRefererRuleGetArgs> RefererRules
        {
            get => _refererRules ?? (_refererRules = new InputList<Inputs.CdnDomainRefererRefererRuleGetArgs>());
            set => _refererRules = value;
        }

        [Input("switch", required: true)]
        public Input<string> Switch { get; set; } = null!;

        public CdnDomainRefererGetArgs()
        {
        }
    }
}
