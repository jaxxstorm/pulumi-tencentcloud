// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu
{
    [TencentcloudResourceType("tencentcloud:Dayu/cCHttpsPolicy:CCHttpsPolicy")]
    public partial class CCHttpsPolicy : Pulumi.CustomResource
    {
        /// <summary>
        /// Action mode. Valid values are `alg` and `drop`.
        /// </summary>
        [Output("action")]
        public Output<string> Action { get; private set; } = null!;

        /// <summary>
        /// Create time of the CC self-define https policy.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        /// </summary>
        [Output("domain")]
        public Output<string> Domain { get; private set; } = null!;

        /// <summary>
        /// Ip of the CC self-define https policy.
        /// </summary>
        [Output("ipLists")]
        public Output<ImmutableArray<string>> IpLists { get; private set; } = null!;

        /// <summary>
        /// Name of the CC self-define https policy. Length should between 1 and 20.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Id of the CC self-define https policy.
        /// </summary>
        [Output("policyId")]
        public Output<string> PolicyId { get; private set; } = null!;

        /// <summary>
        /// ID of the resource that the CC self-define https policy works for.
        /// </summary>
        [Output("resourceId")]
        public Output<string> ResourceId { get; private set; } = null!;

        /// <summary>
        /// Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        /// </summary>
        [Output("resourceType")]
        public Output<string> ResourceType { get; private set; } = null!;

        /// <summary>
        /// Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        /// </summary>
        [Output("ruleId")]
        public Output<string> RuleId { get; private set; } = null!;

        /// <summary>
        /// Rule list of the CC self-define https policy.
        /// </summary>
        [Output("ruleLists")]
        public Output<ImmutableArray<Outputs.CCHttpsPolicyRuleList>> RuleLists { get; private set; } = null!;

        /// <summary>
        /// Indicate the CC self-define https policy takes effect or not.
        /// </summary>
        [Output("switch")]
        public Output<bool?> Switch { get; private set; } = null!;


        /// <summary>
        /// Create a CCHttpsPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CCHttpsPolicy(string name, CCHttpsPolicyArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Dayu/cCHttpsPolicy:CCHttpsPolicy", name, args ?? new CCHttpsPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CCHttpsPolicy(string name, Input<string> id, CCHttpsPolicyState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Dayu/cCHttpsPolicy:CCHttpsPolicy", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CCHttpsPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CCHttpsPolicy Get(string name, Input<string> id, CCHttpsPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new CCHttpsPolicy(name, id, state, options);
        }
    }

    public sealed class CCHttpsPolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Action mode. Valid values are `alg` and `drop`.
        /// </summary>
        [Input("action")]
        public Input<string>? Action { get; set; }

        /// <summary>
        /// Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        /// </summary>
        [Input("domain", required: true)]
        public Input<string> Domain { get; set; } = null!;

        /// <summary>
        /// Name of the CC self-define https policy. Length should between 1 and 20.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// ID of the resource that the CC self-define https policy works for.
        /// </summary>
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        /// <summary>
        /// Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        /// </summary>
        [Input("resourceType", required: true)]
        public Input<string> ResourceType { get; set; } = null!;

        /// <summary>
        /// Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        /// </summary>
        [Input("ruleId", required: true)]
        public Input<string> RuleId { get; set; } = null!;

        [Input("ruleLists", required: true)]
        private InputList<Inputs.CCHttpsPolicyRuleListArgs>? _ruleLists;

        /// <summary>
        /// Rule list of the CC self-define https policy.
        /// </summary>
        public InputList<Inputs.CCHttpsPolicyRuleListArgs> RuleLists
        {
            get => _ruleLists ?? (_ruleLists = new InputList<Inputs.CCHttpsPolicyRuleListArgs>());
            set => _ruleLists = value;
        }

        /// <summary>
        /// Indicate the CC self-define https policy takes effect or not.
        /// </summary>
        [Input("switch")]
        public Input<bool>? Switch { get; set; }

        public CCHttpsPolicyArgs()
        {
        }
    }

    public sealed class CCHttpsPolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Action mode. Valid values are `alg` and `drop`.
        /// </summary>
        [Input("action")]
        public Input<string>? Action { get; set; }

        /// <summary>
        /// Create time of the CC self-define https policy.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        [Input("ipLists")]
        private InputList<string>? _ipLists;

        /// <summary>
        /// Ip of the CC self-define https policy.
        /// </summary>
        public InputList<string> IpLists
        {
            get => _ipLists ?? (_ipLists = new InputList<string>());
            set => _ipLists = value;
        }

        /// <summary>
        /// Name of the CC self-define https policy. Length should between 1 and 20.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Id of the CC self-define https policy.
        /// </summary>
        [Input("policyId")]
        public Input<string>? PolicyId { get; set; }

        /// <summary>
        /// ID of the resource that the CC self-define https policy works for.
        /// </summary>
        [Input("resourceId")]
        public Input<string>? ResourceId { get; set; }

        /// <summary>
        /// Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        /// </summary>
        [Input("resourceType")]
        public Input<string>? ResourceType { get; set; }

        /// <summary>
        /// Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        /// </summary>
        [Input("ruleId")]
        public Input<string>? RuleId { get; set; }

        [Input("ruleLists")]
        private InputList<Inputs.CCHttpsPolicyRuleListGetArgs>? _ruleLists;

        /// <summary>
        /// Rule list of the CC self-define https policy.
        /// </summary>
        public InputList<Inputs.CCHttpsPolicyRuleListGetArgs> RuleLists
        {
            get => _ruleLists ?? (_ruleLists = new InputList<Inputs.CCHttpsPolicyRuleListGetArgs>());
            set => _ruleLists = value;
        }

        /// <summary>
        /// Indicate the CC self-define https policy takes effect or not.
        /// </summary>
        [Input("switch")]
        public Input<bool>? Switch { get; set; }

        public CCHttpsPolicyState()
        {
        }
    }
}
