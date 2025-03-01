// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Gaap
{
    public static class GetLayer7Listeners
    {
        /// <summary>
        /// Use this data source to query gaap layer7 listeners.
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
        ///         var fooLayer7Listener = new Tencentcloud.Gaap.Layer7Listener("fooLayer7Listener", new Tencentcloud.Gaap.Layer7ListenerArgs
        ///         {
        ///             Protocol = "HTTP",
        ///             Port = 80,
        ///             ProxyId = fooProxy.Id,
        ///         });
        ///         var listenerId = Tencentcloud.Gaap.GetLayer7Listeners.Invoke(new Tencentcloud.Gaap.GetLayer7ListenersInvokeArgs
        ///         {
        ///             Protocol = "HTTP",
        ///             ProxyId = fooProxy.Id,
        ///             ListenerId = fooLayer7Listener.Id,
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetLayer7ListenersResult> InvokeAsync(GetLayer7ListenersArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetLayer7ListenersResult>("tencentcloud:Gaap/getLayer7Listeners:getLayer7Listeners", args ?? new GetLayer7ListenersArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query gaap layer7 listeners.
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
        ///         var fooLayer7Listener = new Tencentcloud.Gaap.Layer7Listener("fooLayer7Listener", new Tencentcloud.Gaap.Layer7ListenerArgs
        ///         {
        ///             Protocol = "HTTP",
        ///             Port = 80,
        ///             ProxyId = fooProxy.Id,
        ///         });
        ///         var listenerId = Tencentcloud.Gaap.GetLayer7Listeners.Invoke(new Tencentcloud.Gaap.GetLayer7ListenersInvokeArgs
        ///         {
        ///             Protocol = "HTTP",
        ///             ProxyId = fooProxy.Id,
        ///             ListenerId = fooLayer7Listener.Id,
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetLayer7ListenersResult> Invoke(GetLayer7ListenersInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetLayer7ListenersResult>("tencentcloud:Gaap/getLayer7Listeners:getLayer7Listeners", args ?? new GetLayer7ListenersInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLayer7ListenersArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the layer7 listener to be queried.
        /// </summary>
        [Input("listenerId")]
        public string? ListenerId { get; set; }

        /// <summary>
        /// Name of the layer7 listener to be queried.
        /// </summary>
        [Input("listenerName")]
        public string? ListenerName { get; set; }

        /// <summary>
        /// Port of the layer7 listener to be queried.
        /// </summary>
        [Input("port")]
        public int? Port { get; set; }

        /// <summary>
        /// Protocol of the layer7 listener to be queried. Valid values: `HTTP` and `HTTPS`.
        /// </summary>
        [Input("protocol", required: true)]
        public string Protocol { get; set; } = null!;

        /// <summary>
        /// ID of the GAAP proxy to be queried.
        /// </summary>
        [Input("proxyId")]
        public string? ProxyId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetLayer7ListenersArgs()
        {
        }
    }

    public sealed class GetLayer7ListenersInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the layer7 listener to be queried.
        /// </summary>
        [Input("listenerId")]
        public Input<string>? ListenerId { get; set; }

        /// <summary>
        /// Name of the layer7 listener to be queried.
        /// </summary>
        [Input("listenerName")]
        public Input<string>? ListenerName { get; set; }

        /// <summary>
        /// Port of the layer7 listener to be queried.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// Protocol of the layer7 listener to be queried. Valid values: `HTTP` and `HTTPS`.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// ID of the GAAP proxy to be queried.
        /// </summary>
        [Input("proxyId")]
        public Input<string>? ProxyId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetLayer7ListenersInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetLayer7ListenersResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? ListenerId;
        public readonly string? ListenerName;
        /// <summary>
        /// An information list of layer7 listeners. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetLayer7ListenersListenerResult> Listeners;
        /// <summary>
        /// Port of the layer7 listener.
        /// </summary>
        public readonly int? Port;
        /// <summary>
        /// Protocol of the layer7 listener.
        /// </summary>
        public readonly string Protocol;
        public readonly string? ProxyId;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetLayer7ListenersResult(
            string id,

            string? listenerId,

            string? listenerName,

            ImmutableArray<Outputs.GetLayer7ListenersListenerResult> listeners,

            int? port,

            string protocol,

            string? proxyId,

            string? resultOutputFile)
        {
            Id = id;
            ListenerId = listenerId;
            ListenerName = listenerName;
            Listeners = listeners;
            Port = port;
            Protocol = protocol;
            ProxyId = proxyId;
            ResultOutputFile = resultOutputFile;
        }
    }
}
