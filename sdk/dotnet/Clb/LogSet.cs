// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Clb
{
    [TencentcloudResourceType("tencentcloud:Clb/logSet:LogSet")]
    public partial class LogSet : Pulumi.CustomResource
    {
        /// <summary>
        /// Logset creation time.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Logset name, which unique and fixed `clb_logset` among all CLS logsets.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Logset retention period in days. Maximun value is `90`.
        /// </summary>
        [Output("period")]
        public Output<int?> Period { get; private set; } = null!;

        /// <summary>
        /// Number of log topics in logset.
        /// </summary>
        [Output("topicCount")]
        public Output<string> TopicCount { get; private set; } = null!;


        /// <summary>
        /// Create a LogSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LogSet(string name, LogSetArgs? args = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Clb/logSet:LogSet", name, args ?? new LogSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LogSet(string name, Input<string> id, LogSetState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Clb/logSet:LogSet", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LogSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LogSet Get(string name, Input<string> id, LogSetState? state = null, CustomResourceOptions? options = null)
        {
            return new LogSet(name, id, state, options);
        }
    }

    public sealed class LogSetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Logset retention period in days. Maximun value is `90`.
        /// </summary>
        [Input("period")]
        public Input<int>? Period { get; set; }

        public LogSetArgs()
        {
        }
    }

    public sealed class LogSetState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Logset creation time.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// Logset name, which unique and fixed `clb_logset` among all CLS logsets.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Logset retention period in days. Maximun value is `90`.
        /// </summary>
        [Input("period")]
        public Input<int>? Period { get; set; }

        /// <summary>
        /// Number of log topics in logset.
        /// </summary>
        [Input("topicCount")]
        public Input<string>? TopicCount { get; set; }

        public LogSetState()
        {
        }
    }
}
