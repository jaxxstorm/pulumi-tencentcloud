// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cls.Inputs
{

    public sealed class IndexRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Full-Text index configuration.
        /// </summary>
        [Input("fullText")]
        public Input<Inputs.IndexRuleFullTextArgs>? FullText { get; set; }

        /// <summary>
        /// Key-Value index configuration.
        /// </summary>
        [Input("keyValue")]
        public Input<Inputs.IndexRuleKeyValueArgs>? KeyValue { get; set; }

        /// <summary>
        /// Metafield index configuration.
        /// </summary>
        [Input("tag")]
        public Input<Inputs.IndexRuleTagArgs>? Tag { get; set; }

        public IndexRuleArgs()
        {
        }
    }
}
