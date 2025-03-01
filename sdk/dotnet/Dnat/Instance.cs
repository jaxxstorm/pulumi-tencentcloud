// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dnat
{
    /// <summary>
    /// Provides a resource to create a NAT forwarding.
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
    ///         var foo = new Tencentcloud.Dnat.Instance("foo", new Tencentcloud.Dnat.InstanceArgs
    ///         {
    ///             Description = "test",
    ///             ElasticIp = "139.199.232.238",
    ///             ElasticPort = "80",
    ///             NatId = "nat-2515tdg",
    ///             PrivateIp = "10.0.0.1",
    ///             PrivatePort = "22",
    ///             Protocol = "tcp",
    ///             VpcId = "vpc-asg3sfa3",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// NAT forwarding can be imported using the id, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Dnat/instance:Instance foo tcp://vpc-asg3sfa3:nat-1asg3t63@127.15.2.3:8080
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Dnat/instance:Instance")]
    public partial class Instance : Pulumi.CustomResource
    {
        /// <summary>
        /// Description of the NAT forward.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Network address of the EIP.
        /// </summary>
        [Output("elasticIp")]
        public Output<string> ElasticIp { get; private set; } = null!;

        /// <summary>
        /// Port of the EIP.
        /// </summary>
        [Output("elasticPort")]
        public Output<string> ElasticPort { get; private set; } = null!;

        /// <summary>
        /// ID of the NAT gateway.
        /// </summary>
        [Output("natId")]
        public Output<string> NatId { get; private set; } = null!;

        /// <summary>
        /// Network address of the backend service.
        /// </summary>
        [Output("privateIp")]
        public Output<string> PrivateIp { get; private set; } = null!;

        /// <summary>
        /// Port of intranet.
        /// </summary>
        [Output("privatePort")]
        public Output<string> PrivatePort { get; private set; } = null!;

        /// <summary>
        /// Type of the network protocol. Valid value: `TCP` and `UDP`.
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// ID of the VPC.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Dnat/instance:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Dnat/instance:Instance", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, state, options);
        }
    }

    public sealed class InstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of the NAT forward.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Network address of the EIP.
        /// </summary>
        [Input("elasticIp", required: true)]
        public Input<string> ElasticIp { get; set; } = null!;

        /// <summary>
        /// Port of the EIP.
        /// </summary>
        [Input("elasticPort", required: true)]
        public Input<string> ElasticPort { get; set; } = null!;

        /// <summary>
        /// ID of the NAT gateway.
        /// </summary>
        [Input("natId", required: true)]
        public Input<string> NatId { get; set; } = null!;

        /// <summary>
        /// Network address of the backend service.
        /// </summary>
        [Input("privateIp", required: true)]
        public Input<string> PrivateIp { get; set; } = null!;

        /// <summary>
        /// Port of intranet.
        /// </summary>
        [Input("privatePort", required: true)]
        public Input<string> PrivatePort { get; set; } = null!;

        /// <summary>
        /// Type of the network protocol. Valid value: `TCP` and `UDP`.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// ID of the VPC.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public InstanceArgs()
        {
        }
    }

    public sealed class InstanceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of the NAT forward.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Network address of the EIP.
        /// </summary>
        [Input("elasticIp")]
        public Input<string>? ElasticIp { get; set; }

        /// <summary>
        /// Port of the EIP.
        /// </summary>
        [Input("elasticPort")]
        public Input<string>? ElasticPort { get; set; }

        /// <summary>
        /// ID of the NAT gateway.
        /// </summary>
        [Input("natId")]
        public Input<string>? NatId { get; set; }

        /// <summary>
        /// Network address of the backend service.
        /// </summary>
        [Input("privateIp")]
        public Input<string>? PrivateIp { get; set; }

        /// <summary>
        /// Port of intranet.
        /// </summary>
        [Input("privatePort")]
        public Input<string>? PrivatePort { get; set; }

        /// <summary>
        /// Type of the network protocol. Valid value: `TCP` and `UDP`.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// ID of the VPC.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public InstanceState()
        {
        }
    }
}
