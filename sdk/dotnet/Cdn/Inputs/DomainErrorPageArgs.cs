// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Inputs
{

    public sealed class DomainErrorPageArgs : Pulumi.ResourceArgs
    {
        [Input("pageRules")]
        private InputList<Inputs.DomainErrorPagePageRuleArgs>? _pageRules;

        /// <summary>
        /// List of error page rule.
        /// </summary>
        public InputList<Inputs.DomainErrorPagePageRuleArgs> PageRules
        {
            get => _pageRules ?? (_pageRules = new InputList<Inputs.DomainErrorPagePageRuleArgs>());
            set => _pageRules = value;
        }

        /// <summary>
        /// Configuration switch, available values: `on`, `off` (default).
        /// </summary>
        [Input("switch", required: true)]
        public Input<string> Switch { get; set; } = null!;

        public DomainErrorPageArgs()
        {
        }
    }
}
