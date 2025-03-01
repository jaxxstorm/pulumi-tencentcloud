// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu
{
    public static class GetL7RulesV2
    {
        /// <summary>
        /// Use this data source to query new dayu layer 7 rules
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
        ///         var test = Output.Create(Tencentcloud.Dayu.GetL7RulesV2.InvokeAsync(new Tencentcloud.Dayu.GetL7RulesV2Args
        ///         {
        ///             Business = "bgpip",
        ///             Limit = 10,
        ///             Offset = 0,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetL7RulesV2Result> InvokeAsync(GetL7RulesV2Args args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetL7RulesV2Result>("tencentcloud:Dayu/getL7RulesV2:getL7RulesV2", args ?? new GetL7RulesV2Args(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query new dayu layer 7 rules
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
        ///         var test = Output.Create(Tencentcloud.Dayu.GetL7RulesV2.InvokeAsync(new Tencentcloud.Dayu.GetL7RulesV2Args
        ///         {
        ///             Business = "bgpip",
        ///             Limit = 10,
        ///             Offset = 0,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetL7RulesV2Result> Invoke(GetL7RulesV2InvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetL7RulesV2Result>("tencentcloud:Dayu/getL7RulesV2:getL7RulesV2", args ?? new GetL7RulesV2InvokeArgs(), options.WithDefaults());
    }


    public sealed class GetL7RulesV2Args : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Type of the resource that the layer 4 rule works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
        /// </summary>
        [Input("business", required: true)]
        public string Business { get; set; } = null!;

        /// <summary>
        /// Domain of resource.
        /// </summary>
        [Input("domain")]
        public string? Domain { get; set; }

        /// <summary>
        /// Ip of the resource.
        /// </summary>
        [Input("ip")]
        public string? Ip { get; set; }

        /// <summary>
        /// The number of pages, default is `10`.
        /// </summary>
        [Input("limit")]
        public int? Limit { get; set; }

        /// <summary>
        /// The page start offset, default is `0`.
        /// </summary>
        [Input("offset")]
        public int? Offset { get; set; }

        /// <summary>
        /// Protocol of resource, value range [`http`, `https`].
        /// </summary>
        [Input("protocol")]
        public string? Protocol { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetL7RulesV2Args()
        {
        }
    }

    public sealed class GetL7RulesV2InvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Type of the resource that the layer 4 rule works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
        /// </summary>
        [Input("business", required: true)]
        public Input<string> Business { get; set; } = null!;

        /// <summary>
        /// Domain of resource.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// Ip of the resource.
        /// </summary>
        [Input("ip")]
        public Input<string>? Ip { get; set; }

        /// <summary>
        /// The number of pages, default is `10`.
        /// </summary>
        [Input("limit")]
        public Input<int>? Limit { get; set; }

        /// <summary>
        /// The page start offset, default is `0`.
        /// </summary>
        [Input("offset")]
        public Input<int>? Offset { get; set; }

        /// <summary>
        /// Protocol of resource, value range [`http`, `https`].
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetL7RulesV2InvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetL7RulesV2Result
    {
        public readonly string Business;
        /// <summary>
        /// Domain of resource.
        /// </summary>
        public readonly string? Domain;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Ip of the resource.
        /// </summary>
        public readonly string? Ip;
        public readonly int? Limit;
        /// <summary>
        /// A list of layer 4 rules. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetL7RulesV2ListResult> Lists;
        public readonly int? Offset;
        /// <summary>
        /// Protocol of resource, value range [`http`, `https`].
        /// </summary>
        public readonly string? Protocol;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetL7RulesV2Result(
            string business,

            string? domain,

            string id,

            string? ip,

            int? limit,

            ImmutableArray<Outputs.GetL7RulesV2ListResult> lists,

            int? offset,

            string? protocol,

            string? resultOutputFile)
        {
            Business = business;
            Domain = domain;
            Id = id;
            Ip = ip;
            Limit = limit;
            Lists = lists;
            Offset = offset;
            Protocol = protocol;
            ResultOutputFile = resultOutputFile;
        }
    }
}
