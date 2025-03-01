// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Eks
{
    /// <summary>
    /// Provides an elastic kubernetes cluster resource.
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
    ///         var vpc = new Tencentcloud.Vpc.Instance("vpc", new Tencentcloud.Vpc.InstanceArgs
    ///         {
    ///             CidrBlock = "10.2.0.0/16",
    ///         });
    ///         var sub = new Tencentcloud.Subnet.Instance("sub", new Tencentcloud.Subnet.InstanceArgs
    ///         {
    ///             VpcId = vpc.Id,
    ///             CidrBlock = "10.2.11.0/24",
    ///             AvailabilityZone = "ap-guangzhou-3",
    ///         });
    ///         var sub2 = new Tencentcloud.Subnet.Instance("sub2", new Tencentcloud.Subnet.InstanceArgs
    ///         {
    ///             VpcId = vpc.Id,
    ///             CidrBlock = "10.2.10.0/24",
    ///             AvailabilityZone = "ap-guangzhou-3",
    ///         });
    ///         var foo = new Tencentcloud.Eks.Cluster("foo", new Tencentcloud.Eks.ClusterArgs
    ///         {
    ///             ClusterName = "tf-test-eks",
    ///             K8sVersion = "1.18.4",
    ///             VpcId = vpc.Id,
    ///             SubnetIds = 
    ///             {
    ///                 sub.Id,
    ///                 sub2.Id,
    ///             },
    ///             ClusterDesc = "test eks cluster created by terraform",
    ///             ServiceSubnetId = sub.Id,
    ///             DnsServers = 
    ///             {
    ///                 new Tencentcloud.Eks.Inputs.ClusterDnsServerArgs
    ///                 {
    ///                     Domain = "www.example1.com",
    ///                     Servers = 
    ///                     {
    ///                         "1.1.1.1:8080",
    ///                         "1.1.1.1:8081",
    ///                         "1.1.1.1:8082",
    ///                     },
    ///                 },
    ///             },
    ///             EnableVpcCoreDns = true,
    ///             NeedDeleteCbs = true,
    ///             Tags = 
    ///             {
    ///                 { "hello", "world" },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Eks/cluster:Cluster foo cluster-id
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Eks/cluster:Cluster")]
    public partial class Cluster : Pulumi.CustomResource
    {
        /// <summary>
        /// Description of EKS cluster.
        /// </summary>
        [Output("clusterDesc")]
        public Output<string?> ClusterDesc { get; private set; } = null!;

        /// <summary>
        /// Name of EKS cluster.
        /// </summary>
        [Output("clusterName")]
        public Output<string> ClusterName { get; private set; } = null!;

        /// <summary>
        /// List of cluster custom DNS Server info.
        /// </summary>
        [Output("dnsServers")]
        public Output<ImmutableArray<Outputs.ClusterDnsServer>> DnsServers { get; private set; } = null!;

        /// <summary>
        /// Indicates whether to enable dns in user cluster, default value is `true`.
        /// </summary>
        [Output("enableVpcCoreDns")]
        public Output<bool?> EnableVpcCoreDns { get; private set; } = null!;

        /// <summary>
        /// Extend parameters.
        /// </summary>
        [Output("extraParam")]
        public Output<ImmutableDictionary<string, object>?> ExtraParam { get; private set; } = null!;

        /// <summary>
        /// Cluster internal access LoadBalancer info.
        /// </summary>
        [Output("internalLb")]
        public Output<Outputs.ClusterInternalLb?> InternalLb { get; private set; } = null!;

        /// <summary>
        /// Kubernetes version of EKS cluster.
        /// </summary>
        [Output("k8sVersion")]
        public Output<string> K8sVersion { get; private set; } = null!;

        /// <summary>
        /// EKS cluster kubeconfig.
        /// </summary>
        [Output("kubeConfig")]
        public Output<string> KubeConfig { get; private set; } = null!;

        /// <summary>
        /// Delete CBS after EKS cluster remove.
        /// </summary>
        [Output("needDeleteCbs")]
        public Output<bool?> NeedDeleteCbs { get; private set; } = null!;

        /// <summary>
        /// Cluster public access LoadBalancer info.
        /// </summary>
        [Output("publicLb")]
        public Output<Outputs.ClusterPublicLb?> PublicLb { get; private set; } = null!;

        /// <summary>
        /// Subnet id of service.
        /// </summary>
        [Output("serviceSubnetId")]
        public Output<string?> ServiceSubnetId { get; private set; } = null!;

        /// <summary>
        /// Subnet Ids for EKS cluster.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// Tags of EKS cluster.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// Vpc Id of EKS cluster.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a Cluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cluster(string name, ClusterArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Eks/cluster:Cluster", name, args ?? new ClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Cluster(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Eks/cluster:Cluster", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Cluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Cluster Get(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new Cluster(name, id, state, options);
        }
    }

    public sealed class ClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of EKS cluster.
        /// </summary>
        [Input("clusterDesc")]
        public Input<string>? ClusterDesc { get; set; }

        /// <summary>
        /// Name of EKS cluster.
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        [Input("dnsServers")]
        private InputList<Inputs.ClusterDnsServerArgs>? _dnsServers;

        /// <summary>
        /// List of cluster custom DNS Server info.
        /// </summary>
        public InputList<Inputs.ClusterDnsServerArgs> DnsServers
        {
            get => _dnsServers ?? (_dnsServers = new InputList<Inputs.ClusterDnsServerArgs>());
            set => _dnsServers = value;
        }

        /// <summary>
        /// Indicates whether to enable dns in user cluster, default value is `true`.
        /// </summary>
        [Input("enableVpcCoreDns")]
        public Input<bool>? EnableVpcCoreDns { get; set; }

        [Input("extraParam")]
        private InputMap<object>? _extraParam;

        /// <summary>
        /// Extend parameters.
        /// </summary>
        public InputMap<object> ExtraParam
        {
            get => _extraParam ?? (_extraParam = new InputMap<object>());
            set => _extraParam = value;
        }

        /// <summary>
        /// Cluster internal access LoadBalancer info.
        /// </summary>
        [Input("internalLb")]
        public Input<Inputs.ClusterInternalLbArgs>? InternalLb { get; set; }

        /// <summary>
        /// Kubernetes version of EKS cluster.
        /// </summary>
        [Input("k8sVersion", required: true)]
        public Input<string> K8sVersion { get; set; } = null!;

        /// <summary>
        /// Delete CBS after EKS cluster remove.
        /// </summary>
        [Input("needDeleteCbs")]
        public Input<bool>? NeedDeleteCbs { get; set; }

        /// <summary>
        /// Cluster public access LoadBalancer info.
        /// </summary>
        [Input("publicLb")]
        public Input<Inputs.ClusterPublicLbArgs>? PublicLb { get; set; }

        /// <summary>
        /// Subnet id of service.
        /// </summary>
        [Input("serviceSubnetId")]
        public Input<string>? ServiceSubnetId { get; set; }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// Subnet Ids for EKS cluster.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Tags of EKS cluster.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Vpc Id of EKS cluster.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public ClusterArgs()
        {
        }
    }

    public sealed class ClusterState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of EKS cluster.
        /// </summary>
        [Input("clusterDesc")]
        public Input<string>? ClusterDesc { get; set; }

        /// <summary>
        /// Name of EKS cluster.
        /// </summary>
        [Input("clusterName")]
        public Input<string>? ClusterName { get; set; }

        [Input("dnsServers")]
        private InputList<Inputs.ClusterDnsServerGetArgs>? _dnsServers;

        /// <summary>
        /// List of cluster custom DNS Server info.
        /// </summary>
        public InputList<Inputs.ClusterDnsServerGetArgs> DnsServers
        {
            get => _dnsServers ?? (_dnsServers = new InputList<Inputs.ClusterDnsServerGetArgs>());
            set => _dnsServers = value;
        }

        /// <summary>
        /// Indicates whether to enable dns in user cluster, default value is `true`.
        /// </summary>
        [Input("enableVpcCoreDns")]
        public Input<bool>? EnableVpcCoreDns { get; set; }

        [Input("extraParam")]
        private InputMap<object>? _extraParam;

        /// <summary>
        /// Extend parameters.
        /// </summary>
        public InputMap<object> ExtraParam
        {
            get => _extraParam ?? (_extraParam = new InputMap<object>());
            set => _extraParam = value;
        }

        /// <summary>
        /// Cluster internal access LoadBalancer info.
        /// </summary>
        [Input("internalLb")]
        public Input<Inputs.ClusterInternalLbGetArgs>? InternalLb { get; set; }

        /// <summary>
        /// Kubernetes version of EKS cluster.
        /// </summary>
        [Input("k8sVersion")]
        public Input<string>? K8sVersion { get; set; }

        /// <summary>
        /// EKS cluster kubeconfig.
        /// </summary>
        [Input("kubeConfig")]
        public Input<string>? KubeConfig { get; set; }

        /// <summary>
        /// Delete CBS after EKS cluster remove.
        /// </summary>
        [Input("needDeleteCbs")]
        public Input<bool>? NeedDeleteCbs { get; set; }

        /// <summary>
        /// Cluster public access LoadBalancer info.
        /// </summary>
        [Input("publicLb")]
        public Input<Inputs.ClusterPublicLbGetArgs>? PublicLb { get; set; }

        /// <summary>
        /// Subnet id of service.
        /// </summary>
        [Input("serviceSubnetId")]
        public Input<string>? ServiceSubnetId { get; set; }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// Subnet Ids for EKS cluster.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Tags of EKS cluster.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Vpc Id of EKS cluster.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public ClusterState()
        {
        }
    }
}
