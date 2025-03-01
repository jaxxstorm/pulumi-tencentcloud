// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Scf
{
    public static class GetNamespaces
    {
        /// <summary>
        /// Use this data source to query SCF namespaces.
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
        ///         var fooNamespace = new Tencentcloud.Scf.Namespace("fooNamespace", new Tencentcloud.Scf.NamespaceArgs
        ///         {
        ///             Namespace = "ci-test-scf",
        ///         });
        ///         var fooNamespaces = Tencentcloud.Scf.GetNamespaces.Invoke(new Tencentcloud.Scf.GetNamespacesInvokeArgs
        ///         {
        ///             Namespace = fooNamespace.Id,
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetNamespacesResult> InvokeAsync(GetNamespacesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNamespacesResult>("tencentcloud:Scf/getNamespaces:getNamespaces", args ?? new GetNamespacesArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query SCF namespaces.
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
        ///         var fooNamespace = new Tencentcloud.Scf.Namespace("fooNamespace", new Tencentcloud.Scf.NamespaceArgs
        ///         {
        ///             Namespace = "ci-test-scf",
        ///         });
        ///         var fooNamespaces = Tencentcloud.Scf.GetNamespaces.Invoke(new Tencentcloud.Scf.GetNamespacesInvokeArgs
        ///         {
        ///             Namespace = fooNamespace.Id,
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetNamespacesResult> Invoke(GetNamespacesInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetNamespacesResult>("tencentcloud:Scf/getNamespaces:getNamespaces", args ?? new GetNamespacesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNamespacesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of the SCF namespace to be queried.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// Name of the SCF namespace to be queried.
        /// </summary>
        [Input("namespace")]
        public string? Namespace { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetNamespacesArgs()
        {
        }
    }

    public sealed class GetNamespacesInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of the SCF namespace to be queried.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the SCF namespace to be queried.
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetNamespacesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetNamespacesResult
    {
        /// <summary>
        /// Description of the SCF namespace.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of the SCF namespace.
        /// </summary>
        public readonly string? Namespace;
        /// <summary>
        /// An information list of namespace. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNamespacesNamespaceResult> ScfNamespaces;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetNamespacesResult(
            string? description,

            string id,

            string? @namespace,

            ImmutableArray<Outputs.GetNamespacesNamespaceResult> namespaces,

            string? resultOutputFile)
        {
            Description = description;
            Id = id;
            Namespace = @namespace;
            ScfNamespaces = namespaces;
            ResultOutputFile = resultOutputFile;
        }
    }
}
