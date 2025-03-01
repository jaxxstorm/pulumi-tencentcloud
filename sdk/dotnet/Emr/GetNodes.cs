// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Emr
{
    public static class GetNodes
    {
        /// <summary>
        /// Provides an available EMR for the user.
        /// 
        /// The EMR data source obtain the hardware node information by using the emr cluster ID.
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
        ///         var myEmrNodes = Output.Create(Tencentcloud.Emr.GetNodes.InvokeAsync(new Tencentcloud.Emr.GetNodesArgs
        ///         {
        ///             InstanceId = "emr-rnzqrleq",
        ///             NodeFlag = "master",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetNodesResult> InvokeAsync(GetNodesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNodesResult>("tencentcloud:Emr/getNodes:getNodes", args ?? new GetNodesArgs(), options.WithDefaults());

        /// <summary>
        /// Provides an available EMR for the user.
        /// 
        /// The EMR data source obtain the hardware node information by using the emr cluster ID.
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
        ///         var myEmrNodes = Output.Create(Tencentcloud.Emr.GetNodes.InvokeAsync(new Tencentcloud.Emr.GetNodesArgs
        ///         {
        ///             InstanceId = "emr-rnzqrleq",
        ///             NodeFlag = "master",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetNodesResult> Invoke(GetNodesInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetNodesResult>("tencentcloud:Emr/getNodes:getNodes", args ?? new GetNodesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNodesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Resource type: Support all/host/pod, default is all.
        /// </summary>
        [Input("hardwareResourceType")]
        public string? HardwareResourceType { get; set; }

        /// <summary>
        /// Cluster instance ID, the instance ID is as follows: emr-xxxxxxxx.
        /// </summary>
        [Input("instanceId", required: true)]
        public string InstanceId { get; set; } = null!;

        /// <summary>
        /// The number returned per page, the default value is 100, and the maximum value is 100.
        /// </summary>
        [Input("limit")]
        public int? Limit { get; set; }

        /// <summary>
        /// Node ID, the value is:
        /// - all: Means to get all type nodes, except cdb information.
        /// - master: Indicates that the master node information is obtained.
        /// - core: Indicates that the core node information is obtained.
        /// - task: indicates obtaining task node information.
        /// - common: means to get common node information.
        /// - router: Indicates obtaining router node information.
        /// - db: Indicates that the cdb information for the normal state is obtained.
        /// - recyle: Indicates that the node information in the Recycle Bin isolation, including the cdb information, is obtained.
        /// - renew: Indicates that all node information to be renewed, including cddb information, is obtained, and the auto-renewal node will not be returned.
        /// </summary>
        [Input("nodeFlag", required: true)]
        public string NodeFlag { get; set; } = null!;

        /// <summary>
        /// Page number, with a default value of 0, represents the first page.
        /// </summary>
        [Input("offset")]
        public int? Offset { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetNodesArgs()
        {
        }
    }

    public sealed class GetNodesInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Resource type: Support all/host/pod, default is all.
        /// </summary>
        [Input("hardwareResourceType")]
        public Input<string>? HardwareResourceType { get; set; }

        /// <summary>
        /// Cluster instance ID, the instance ID is as follows: emr-xxxxxxxx.
        /// </summary>
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        /// <summary>
        /// The number returned per page, the default value is 100, and the maximum value is 100.
        /// </summary>
        [Input("limit")]
        public Input<int>? Limit { get; set; }

        /// <summary>
        /// Node ID, the value is:
        /// - all: Means to get all type nodes, except cdb information.
        /// - master: Indicates that the master node information is obtained.
        /// - core: Indicates that the core node information is obtained.
        /// - task: indicates obtaining task node information.
        /// - common: means to get common node information.
        /// - router: Indicates obtaining router node information.
        /// - db: Indicates that the cdb information for the normal state is obtained.
        /// - recyle: Indicates that the node information in the Recycle Bin isolation, including the cdb information, is obtained.
        /// - renew: Indicates that all node information to be renewed, including cddb information, is obtained, and the auto-renewal node will not be returned.
        /// </summary>
        [Input("nodeFlag", required: true)]
        public Input<string> NodeFlag { get; set; } = null!;

        /// <summary>
        /// Page number, with a default value of 0, represents the first page.
        /// </summary>
        [Input("offset")]
        public Input<int>? Offset { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetNodesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetNodesResult
    {
        /// <summary>
        /// Resource type, host/pod.
        /// </summary>
        public readonly string? HardwareResourceType;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string InstanceId;
        public readonly int? Limit;
        public readonly string NodeFlag;
        /// <summary>
        /// List of node details.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNodesNodeResult> EmrNodes;
        public readonly int? Offset;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetNodesResult(
            string? hardwareResourceType,

            string id,

            string instanceId,

            int? limit,

            string nodeFlag,

            ImmutableArray<Outputs.GetNodesNodeResult> nodes,

            int? offset,

            string? resultOutputFile)
        {
            HardwareResourceType = hardwareResourceType;
            Id = id;
            InstanceId = instanceId;
            Limit = limit;
            NodeFlag = nodeFlag;
            EmrNodes = nodes;
            Offset = offset;
            ResultOutputFile = resultOutputFile;
        }
    }
}
