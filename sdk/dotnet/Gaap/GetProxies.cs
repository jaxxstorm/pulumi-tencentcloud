// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Gaap
{
    public static class GetProxies
    {
        /// <summary>
        /// Use this data source to query gaap proxies.
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
        ///         var fooProxy = new Tencentcloud.Gaap.Proxy("fooProxy", new Tencentcloud.Gaap.ProxyArgs
        ///         {
        ///             Bandwidth = 10,
        ///             Concurrent = 2,
        ///             AccessRegion = "SouthChina",
        ///             RealserverRegion = "NorthChina",
        ///         });
        ///         var fooProxies = Tencentcloud.Gaap.GetProxies.Invoke(new Tencentcloud.Gaap.GetProxiesInvokeArgs
        ///         {
        ///             Ids = 
        ///             {
        ///                 fooProxy.Id,
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetProxiesResult> InvokeAsync(GetProxiesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProxiesResult>("tencentcloud:Gaap/getProxies:getProxies", args ?? new GetProxiesArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query gaap proxies.
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
        ///         var fooProxy = new Tencentcloud.Gaap.Proxy("fooProxy", new Tencentcloud.Gaap.ProxyArgs
        ///         {
        ///             Bandwidth = 10,
        ///             Concurrent = 2,
        ///             AccessRegion = "SouthChina",
        ///             RealserverRegion = "NorthChina",
        ///         });
        ///         var fooProxies = Tencentcloud.Gaap.GetProxies.Invoke(new Tencentcloud.Gaap.GetProxiesInvokeArgs
        ///         {
        ///             Ids = 
        ///             {
        ///                 fooProxy.Id,
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetProxiesResult> Invoke(GetProxiesInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetProxiesResult>("tencentcloud:Gaap/getProxies:getProxies", args ?? new GetProxiesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetProxiesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Access region of the GAAP proxy to be queried. Conflict with `ids`.
        /// </summary>
        [Input("accessRegion")]
        public string? AccessRegion { get; set; }

        [Input("ids")]
        private List<string>? _ids;

        /// <summary>
        /// ID of the GAAP proxy to be queried. Conflict with `project_id`, `access_region` and `realserver_region`.
        /// </summary>
        public List<string> Ids
        {
            get => _ids ?? (_ids = new List<string>());
            set => _ids = value;
        }

        /// <summary>
        /// Project ID of the GAAP proxy to be queried. Conflict with `ids`.
        /// </summary>
        [Input("projectId")]
        public int? ProjectId { get; set; }

        /// <summary>
        /// Region of the GAAP realserver to be queried. Conflict with `ids`.
        /// </summary>
        [Input("realserverRegion")]
        public string? RealserverRegion { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        [Input("tags")]
        private Dictionary<string, object>? _tags;

        /// <summary>
        /// Tags of the GAAP proxy to be queried. Support up to 5, display the information as long as it matches one.
        /// </summary>
        public Dictionary<string, object> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, object>());
            set => _tags = value;
        }

        public GetProxiesArgs()
        {
        }
    }

    public sealed class GetProxiesInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Access region of the GAAP proxy to be queried. Conflict with `ids`.
        /// </summary>
        [Input("accessRegion")]
        public Input<string>? AccessRegion { get; set; }

        [Input("ids")]
        private InputList<string>? _ids;

        /// <summary>
        /// ID of the GAAP proxy to be queried. Conflict with `project_id`, `access_region` and `realserver_region`.
        /// </summary>
        public InputList<string> Ids
        {
            get => _ids ?? (_ids = new InputList<string>());
            set => _ids = value;
        }

        /// <summary>
        /// Project ID of the GAAP proxy to be queried. Conflict with `ids`.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// Region of the GAAP realserver to be queried. Conflict with `ids`.
        /// </summary>
        [Input("realserverRegion")]
        public Input<string>? RealserverRegion { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Tags of the GAAP proxy to be queried. Support up to 5, display the information as long as it matches one.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public GetProxiesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetProxiesResult
    {
        /// <summary>
        /// Access region of the GAAP proxy.
        /// </summary>
        public readonly string? AccessRegion;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<string> Ids;
        /// <summary>
        /// ID of the project within the GAAP proxy, '0' means is default project.
        /// </summary>
        public readonly int? ProjectId;
        /// <summary>
        /// An information list of GAAP proxy. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProxiesProxyResult> GaapProxies;
        /// <summary>
        /// Region of the GAAP realserver.
        /// </summary>
        public readonly string? RealserverRegion;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// Tags of the GAAP proxy.
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Tags;

        [OutputConstructor]
        private GetProxiesResult(
            string? accessRegion,

            string id,

            ImmutableArray<string> ids,

            int? projectId,

            ImmutableArray<Outputs.GetProxiesProxyResult> proxies,

            string? realserverRegion,

            string? resultOutputFile,

            ImmutableDictionary<string, object>? tags)
        {
            AccessRegion = accessRegion;
            Id = id;
            Ids = ids;
            ProjectId = projectId;
            GaapProxies = proxies;
            RealserverRegion = realserverRegion;
            ResultOutputFile = resultOutputFile;
            Tags = tags;
        }
    }
}
