// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cos.Inputs
{

    public sealed class BucketLifecycleRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies a period in the object's expire (documented below).
        /// </summary>
        [Input("expiration")]
        public Input<Inputs.BucketLifecycleRuleExpirationArgs>? Expiration { get; set; }

        /// <summary>
        /// Object key prefix identifying one or more objects to which the rule applies.
        /// </summary>
        [Input("filterPrefix", required: true)]
        public Input<string> FilterPrefix { get; set; } = null!;

        /// <summary>
        /// A unique identifier for the rule. It can be up to 255 characters.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies when non current object versions shall expire.
        /// </summary>
        [Input("nonCurrentExpiration")]
        public Input<Inputs.BucketLifecycleRuleNonCurrentExpirationArgs>? NonCurrentExpiration { get; set; }

        [Input("nonCurrentTransitions")]
        private InputList<Inputs.BucketLifecycleRuleNonCurrentTransitionArgs>? _nonCurrentTransitions;

        /// <summary>
        /// Specifies a period in the non current object's transitions.
        /// </summary>
        public InputList<Inputs.BucketLifecycleRuleNonCurrentTransitionArgs> NonCurrentTransitions
        {
            get => _nonCurrentTransitions ?? (_nonCurrentTransitions = new InputList<Inputs.BucketLifecycleRuleNonCurrentTransitionArgs>());
            set => _nonCurrentTransitions = value;
        }

        [Input("transitions")]
        private InputList<Inputs.BucketLifecycleRuleTransitionArgs>? _transitions;

        /// <summary>
        /// Specifies a period in the object's transitions (documented below).
        /// </summary>
        public InputList<Inputs.BucketLifecycleRuleTransitionArgs> Transitions
        {
            get => _transitions ?? (_transitions = new InputList<Inputs.BucketLifecycleRuleTransitionArgs>());
            set => _transitions = value;
        }

        public BucketLifecycleRuleArgs()
        {
        }
    }
}
