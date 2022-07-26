// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Eip
{
    [TencentcloudResourceType("tencentcloud:Eip/association:Association")]
    public partial class Association : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of EIP.
        /// </summary>
        [Output("eipId")]
        public Output<string> EipId { get; private set; } = null!;

        /// <summary>
        /// The CVM or CLB instance id going to bind with the EIP. This field is conflict with `network_interface_id` and
        /// `private_ip fields`.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        /// <summary>
        /// Indicates the network interface id like `eni-xxxxxx`. This field is conflict with `instance_id`.
        /// </summary>
        [Output("networkInterfaceId")]
        public Output<string> NetworkInterfaceId { get; private set; } = null!;

        /// <summary>
        /// Indicates an IP belongs to the `network_interface_id`. This field is conflict with `instance_id`.
        /// </summary>
        [Output("privateIp")]
        public Output<string> PrivateIp { get; private set; } = null!;


        /// <summary>
        /// Create a Association resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Association(string name, AssociationArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Eip/association:Association", name, args ?? new AssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Association(string name, Input<string> id, AssociationState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Eip/association:Association", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Association resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Association Get(string name, Input<string> id, AssociationState? state = null, CustomResourceOptions? options = null)
        {
            return new Association(name, id, state, options);
        }
    }

    public sealed class AssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of EIP.
        /// </summary>
        [Input("eipId", required: true)]
        public Input<string> EipId { get; set; } = null!;

        /// <summary>
        /// The CVM or CLB instance id going to bind with the EIP. This field is conflict with `network_interface_id` and
        /// `private_ip fields`.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// Indicates the network interface id like `eni-xxxxxx`. This field is conflict with `instance_id`.
        /// </summary>
        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        /// <summary>
        /// Indicates an IP belongs to the `network_interface_id`. This field is conflict with `instance_id`.
        /// </summary>
        [Input("privateIp")]
        public Input<string>? PrivateIp { get; set; }

        public AssociationArgs()
        {
        }
    }

    public sealed class AssociationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of EIP.
        /// </summary>
        [Input("eipId")]
        public Input<string>? EipId { get; set; }

        /// <summary>
        /// The CVM or CLB instance id going to bind with the EIP. This field is conflict with `network_interface_id` and
        /// `private_ip fields`.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// Indicates the network interface id like `eni-xxxxxx`. This field is conflict with `instance_id`.
        /// </summary>
        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        /// <summary>
        /// Indicates an IP belongs to the `network_interface_id`. This field is conflict with `instance_id`.
        /// </summary>
        [Input("privateIp")]
        public Input<string>? PrivateIp { get; set; }

        public AssociationState()
        {
        }
    }
}
