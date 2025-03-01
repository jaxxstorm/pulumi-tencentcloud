// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Eks
{
    public static class GetClusterCredential
    {
        /// <summary>
        /// Provide a datasource to query EKS cluster credential info.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Tencentcloud = Pulumi.Tencentcloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var foo = Output.Create(Tencentcloud.Eks.GetClusterCredential.InvokeAsync(new Tencentcloud.Eks.GetClusterCredentialArgs
        ///         {
        ///             ClusterId = "cls-xxxxxxxx",
        ///         }));
        ///         this.Addresses = data.Tencentcloud_eks_cluster_credential.Cred.Addresses;
        ///         this.CaCert = data.Tencentcloud_eks_cluster_credential.Cred.Credential.Ca_cert;
        ///         this.Token = data.Tencentcloud_eks_cluster_credential.Cred.Credential.Token;
        ///         this.PublicLbParam = data.Tencentcloud_eks_cluster_credential.Cred.Public_lb[0].Extra_param;
        ///         this.InternalLbSubnet = data.Tencentcloud_eks_cluster_credential.Cred.Internal_lb[0].Subnet_id;
        ///     }
        /// 
        ///     [Output("addresses")]
        ///     public Output&lt;string&gt; Addresses { get; set; }
        ///     [Output("caCert")]
        ///     public Output&lt;string&gt; CaCert { get; set; }
        ///     [Output("token")]
        ///     public Output&lt;string&gt; Token { get; set; }
        ///     [Output("publicLbParam")]
        ///     public Output&lt;string&gt; PublicLbParam { get; set; }
        ///     [Output("internalLbSubnet")]
        ///     public Output&lt;string&gt; InternalLbSubnet { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetClusterCredentialResult> InvokeAsync(GetClusterCredentialArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClusterCredentialResult>("tencentcloud:Eks/getClusterCredential:getClusterCredential", args ?? new GetClusterCredentialArgs(), options.WithDefaults());

        /// <summary>
        /// Provide a datasource to query EKS cluster credential info.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Tencentcloud = Pulumi.Tencentcloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var foo = Output.Create(Tencentcloud.Eks.GetClusterCredential.InvokeAsync(new Tencentcloud.Eks.GetClusterCredentialArgs
        ///         {
        ///             ClusterId = "cls-xxxxxxxx",
        ///         }));
        ///         this.Addresses = data.Tencentcloud_eks_cluster_credential.Cred.Addresses;
        ///         this.CaCert = data.Tencentcloud_eks_cluster_credential.Cred.Credential.Ca_cert;
        ///         this.Token = data.Tencentcloud_eks_cluster_credential.Cred.Credential.Token;
        ///         this.PublicLbParam = data.Tencentcloud_eks_cluster_credential.Cred.Public_lb[0].Extra_param;
        ///         this.InternalLbSubnet = data.Tencentcloud_eks_cluster_credential.Cred.Internal_lb[0].Subnet_id;
        ///     }
        /// 
        ///     [Output("addresses")]
        ///     public Output&lt;string&gt; Addresses { get; set; }
        ///     [Output("caCert")]
        ///     public Output&lt;string&gt; CaCert { get; set; }
        ///     [Output("token")]
        ///     public Output&lt;string&gt; Token { get; set; }
        ///     [Output("publicLbParam")]
        ///     public Output&lt;string&gt; PublicLbParam { get; set; }
        ///     [Output("internalLbSubnet")]
        ///     public Output&lt;string&gt; InternalLbSubnet { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetClusterCredentialResult> Invoke(GetClusterCredentialInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetClusterCredentialResult>("tencentcloud:Eks/getClusterCredential:getClusterCredential", args ?? new GetClusterCredentialInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClusterCredentialArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// EKS Cluster ID.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// Used for save result.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetClusterCredentialArgs()
        {
        }
    }

    public sealed class GetClusterCredentialInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// EKS Cluster ID.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Used for save result.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetClusterCredentialInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetClusterCredentialResult
    {
        /// <summary>
        /// List of IP Address information.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetClusterCredentialAddressResult> Addresses;
        public readonly string ClusterId;
        /// <summary>
        /// Credential info. Format `{ ca_cert: String, token: String }`.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Credential;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Cluster internal access LoadBalancer info.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetClusterCredentialInternalLbResult> InternalLbs;
        /// <summary>
        /// EKS cluster kubeconfig.
        /// </summary>
        public readonly string KubeConfig;
        /// <summary>
        /// Indicates whether the new internal/public network function.
        /// </summary>
        public readonly bool ProxyLb;
        /// <summary>
        /// Cluster public access LoadBalancer info.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetClusterCredentialPublicLbResult> PublicLbs;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetClusterCredentialResult(
            ImmutableArray<Outputs.GetClusterCredentialAddressResult> addresses,

            string clusterId,

            ImmutableDictionary<string, object> credential,

            string id,

            ImmutableArray<Outputs.GetClusterCredentialInternalLbResult> internalLbs,

            string kubeConfig,

            bool proxyLb,

            ImmutableArray<Outputs.GetClusterCredentialPublicLbResult> publicLbs,

            string? resultOutputFile)
        {
            Addresses = addresses;
            ClusterId = clusterId;
            Credential = credential;
            Id = id;
            InternalLbs = internalLbs;
            KubeConfig = kubeConfig;
            ProxyLb = proxyLb;
            PublicLbs = publicLbs;
            ResultOutputFile = resultOutputFile;
        }
    }
}
