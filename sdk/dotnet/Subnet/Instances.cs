// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Subnet
{
    public static class Instances
    {
        public static Task<InstancesResult> InvokeAsync(InstancesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<InstancesResult>("tencentcloud:Subnet/instances:Instances", args ?? new InstancesArgs(), options.WithDefaults());

        public static Output<InstancesResult> Invoke(InstancesInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<InstancesResult>("tencentcloud:Subnet/instances:Instances", args ?? new InstancesInvokeArgs(), options.WithDefaults());
    }


    public sealed class InstancesArgs : Pulumi.InvokeArgs
    {
        [Input("subnetId", required: true)]
        public string SubnetId { get; set; } = null!;

        [Input("vpcId", required: true)]
        public string VpcId { get; set; } = null!;

        public InstancesArgs()
        {
        }
    }

    public sealed class InstancesInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public InstancesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class InstancesResult
    {
        public readonly string AvailabilityZone;
        public readonly string CidrBlock;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string RouteTableId;
        public readonly string SubnetId;
        public readonly string VpcId;

        [OutputConstructor]
        private InstancesResult(
            string availabilityZone,

            string cidrBlock,

            string id,

            string name,

            string routeTableId,

            string subnetId,

            string vpcId)
        {
            AvailabilityZone = availabilityZone;
            CidrBlock = cidrBlock;
            Id = id;
            Name = name;
            RouteTableId = routeTableId;
            SubnetId = subnetId;
            VpcId = vpcId;
        }
    }
}
