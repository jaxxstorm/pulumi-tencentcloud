// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Tcaplus
{
    /// <summary>
    /// Use this resource to create TcaplusDB table group.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Tencentcloud = Pulumi.Tencentcloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var test = new Tencentcloud.Tcaplus.Cluster("test", new Tencentcloud.Tcaplus.ClusterArgs
    ///         {
    ///             IdlType = "PROTO",
    ///             ClusterName = "tf_tcaplus_cluster_test",
    ///             VpcId = "vpc-7k6gzox6",
    ///             SubnetId = "subnet-akwgvfa3",
    ///             Password = "1qaA2k1wgvfa3ZZZ",
    ///             OldPasswordExpireLast = 3600,
    ///         });
    ///         var tablegroup = new Tencentcloud.Tcaplus.Tablegroup("tablegroup", new Tencentcloud.Tcaplus.TablegroupArgs
    ///         {
    ///             ClusterId = test.Id,
    ///             TablegroupName = "tf_test_group_name",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Tcaplus/tablegroup:Tablegroup")]
    public partial class Tablegroup : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of the TcaplusDB cluster to which the table group belongs.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// Create time of the TcaplusDB table group.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Number of tables.
        /// </summary>
        [Output("tableCount")]
        public Output<int> TableCount { get; private set; } = null!;

        /// <summary>
        /// Name of the TcaplusDB table group. Name length should be between 1 and 30.
        /// </summary>
        [Output("tablegroupName")]
        public Output<string> TablegroupName { get; private set; } = null!;

        /// <summary>
        /// Total storage size (MB).
        /// </summary>
        [Output("totalSize")]
        public Output<int> TotalSize { get; private set; } = null!;


        /// <summary>
        /// Create a Tablegroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Tablegroup(string name, TablegroupArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Tcaplus/tablegroup:Tablegroup", name, args ?? new TablegroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Tablegroup(string name, Input<string> id, TablegroupState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Tcaplus/tablegroup:Tablegroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Tablegroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Tablegroup Get(string name, Input<string> id, TablegroupState? state = null, CustomResourceOptions? options = null)
        {
            return new Tablegroup(name, id, state, options);
        }
    }

    public sealed class TablegroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the TcaplusDB cluster to which the table group belongs.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Name of the TcaplusDB table group. Name length should be between 1 and 30.
        /// </summary>
        [Input("tablegroupName", required: true)]
        public Input<string> TablegroupName { get; set; } = null!;

        public TablegroupArgs()
        {
        }
    }

    public sealed class TablegroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the TcaplusDB cluster to which the table group belongs.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// Create time of the TcaplusDB table group.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// Number of tables.
        /// </summary>
        [Input("tableCount")]
        public Input<int>? TableCount { get; set; }

        /// <summary>
        /// Name of the TcaplusDB table group. Name length should be between 1 and 30.
        /// </summary>
        [Input("tablegroupName")]
        public Input<string>? TablegroupName { get; set; }

        /// <summary>
        /// Total storage size (MB).
        /// </summary>
        [Input("totalSize")]
        public Input<int>? TotalSize { get; set; }

        public TablegroupState()
        {
        }
    }
}
