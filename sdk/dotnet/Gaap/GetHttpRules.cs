// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Gaap
{
    public static class GetHttpRules
    {
        /// <summary>
        /// Use this data source to query forward rule of layer7 listeners.
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
        ///         var fooRealserver = new Tencentcloud.Gaap.Realserver("fooRealserver", new Tencentcloud.Gaap.RealserverArgs
        ///         {
        ///             Ip = "1.1.1.1",
        ///         });
        ///         var fooHttpRule = new Tencentcloud.Gaap.HttpRule("fooHttpRule", new Tencentcloud.Gaap.HttpRuleArgs
        ///         {
        ///             ListenerId = fooLayer7Listener.Id,
        ///             Domain = "www.qq.com",
        ///             Path = "/",
        ///             RealserverType = "IP",
        ///             HealthCheck = true,
        ///             Realservers = 
        ///             {
        ///                 new Tencentcloud.Gaap.Inputs.HttpRuleRealserverArgs
        ///                 {
        ///                     Id = fooRealserver.Id,
        ///                     Ip = fooRealserver.Ip,
        ///                     Port = 80,
        ///                 },
        ///             },
        ///         });
        ///         var fooHttpRules = Tencentcloud.Gaap.GetHttpRules.Invoke(new Tencentcloud.Gaap.GetHttpRulesInvokeArgs
        ///         {
        ///             ListenerId = fooLayer7Listener.Id,
        ///             Domain = fooHttpRule.Domain,
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetHttpRulesResult> InvokeAsync(GetHttpRulesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetHttpRulesResult>("tencentcloud:Gaap/getHttpRules:getHttpRules", args ?? new GetHttpRulesArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query forward rule of layer7 listeners.
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
        ///         var fooRealserver = new Tencentcloud.Gaap.Realserver("fooRealserver", new Tencentcloud.Gaap.RealserverArgs
        ///         {
        ///             Ip = "1.1.1.1",
        ///         });
        ///         var fooHttpRule = new Tencentcloud.Gaap.HttpRule("fooHttpRule", new Tencentcloud.Gaap.HttpRuleArgs
        ///         {
        ///             ListenerId = fooLayer7Listener.Id,
        ///             Domain = "www.qq.com",
        ///             Path = "/",
        ///             RealserverType = "IP",
        ///             HealthCheck = true,
        ///             Realservers = 
        ///             {
        ///                 new Tencentcloud.Gaap.Inputs.HttpRuleRealserverArgs
        ///                 {
        ///                     Id = fooRealserver.Id,
        ///                     Ip = fooRealserver.Ip,
        ///                     Port = 80,
        ///                 },
        ///             },
        ///         });
        ///         var fooHttpRules = Tencentcloud.Gaap.GetHttpRules.Invoke(new Tencentcloud.Gaap.GetHttpRulesInvokeArgs
        ///         {
        ///             ListenerId = fooLayer7Listener.Id,
        ///             Domain = fooHttpRule.Domain,
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetHttpRulesResult> Invoke(GetHttpRulesInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetHttpRulesResult>("tencentcloud:Gaap/getHttpRules:getHttpRules", args ?? new GetHttpRulesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetHttpRulesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Forward domain of the layer7 listener to be queried.
        /// </summary>
        [Input("domain")]
        public string? Domain { get; set; }

        /// <summary>
        /// Requested host which is forwarded to the realserver by the listener to be queried.
        /// </summary>
        [Input("forwardHost")]
        public string? ForwardHost { get; set; }

        /// <summary>
        /// ID of the layer7 listener to be queried.
        /// </summary>
        [Input("listenerId", required: true)]
        public string ListenerId { get; set; } = null!;

        /// <summary>
        /// Path of the forward rule to be queried.
        /// </summary>
        [Input("path")]
        public string? Path { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetHttpRulesArgs()
        {
        }
    }

    public sealed class GetHttpRulesInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Forward domain of the layer7 listener to be queried.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// Requested host which is forwarded to the realserver by the listener to be queried.
        /// </summary>
        [Input("forwardHost")]
        public Input<string>? ForwardHost { get; set; }

        /// <summary>
        /// ID of the layer7 listener to be queried.
        /// </summary>
        [Input("listenerId", required: true)]
        public Input<string> ListenerId { get; set; } = null!;

        /// <summary>
        /// Path of the forward rule to be queried.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetHttpRulesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetHttpRulesResult
    {
        /// <summary>
        /// Domain of the GAAP realserver.
        /// </summary>
        public readonly string? Domain;
        /// <summary>
        /// Requested host which is forwarded to the realserver by the listener.
        /// </summary>
        public readonly string? ForwardHost;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// ID of the layer7 listener.
        /// </summary>
        public readonly string ListenerId;
        /// <summary>
        /// Path of the forward rule.
        /// </summary>
        public readonly string? Path;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// An information list of forward rule of the layer7 listeners. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetHttpRulesRuleResult> Rules;

        [OutputConstructor]
        private GetHttpRulesResult(
            string? domain,

            string? forwardHost,

            string id,

            string listenerId,

            string? path,

            string? resultOutputFile,

            ImmutableArray<Outputs.GetHttpRulesRuleResult> rules)
        {
            Domain = domain;
            ForwardHost = forwardHost;
            Id = id;
            ListenerId = listenerId;
            Path = path;
            ResultOutputFile = resultOutputFile;
            Rules = rules;
        }
    }
}
