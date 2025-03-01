// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Postgresql
{
    public static class GetInstances
    {
        /// <summary>
        /// Use this data source to query postgresql instances
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
        ///         var name = Output.Create(Tencentcloud.Postgresql.GetInstances.InvokeAsync(new Tencentcloud.Postgresql.GetInstancesArgs
        ///         {
        ///             Name = "test",
        ///         }));
        ///         var project = Output.Create(Tencentcloud.Postgresql.GetInstances.InvokeAsync(new Tencentcloud.Postgresql.GetInstancesArgs
        ///         {
        ///             ProjectId = 0,
        ///         }));
        ///         var id = Output.Create(Tencentcloud.Postgresql.GetInstances.InvokeAsync(new Tencentcloud.Postgresql.GetInstancesArgs
        ///         {
        ///             Id = "postgres-h9t4fde1",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetInstancesResult> InvokeAsync(GetInstancesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstancesResult>("tencentcloud:Postgresql/getInstances:getInstances", args ?? new GetInstancesArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query postgresql instances
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
        ///         var name = Output.Create(Tencentcloud.Postgresql.GetInstances.InvokeAsync(new Tencentcloud.Postgresql.GetInstancesArgs
        ///         {
        ///             Name = "test",
        ///         }));
        ///         var project = Output.Create(Tencentcloud.Postgresql.GetInstances.InvokeAsync(new Tencentcloud.Postgresql.GetInstancesArgs
        ///         {
        ///             ProjectId = 0,
        ///         }));
        ///         var id = Output.Create(Tencentcloud.Postgresql.GetInstances.InvokeAsync(new Tencentcloud.Postgresql.GetInstancesArgs
        ///         {
        ///             Id = "postgres-h9t4fde1",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetInstancesResult> Invoke(GetInstancesInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetInstancesResult>("tencentcloud:Postgresql/getInstances:getInstances", args ?? new GetInstancesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInstancesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the postgresql instance to be query.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of the postgresql instance to be query.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Project ID of the postgresql instance to be query.
        /// </summary>
        [Input("projectId")]
        public int? ProjectId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetInstancesArgs()
        {
        }
    }

    public sealed class GetInstancesInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the postgresql instance to be query.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of the postgresql instance to be query.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Project ID of the postgresql instance to be query.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetInstancesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetInstancesResult
    {
        /// <summary>
        /// ID of the postgresql instance.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// A list of postgresql instances. Each element contains the following attributes.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInstancesInstanceListResult> InstanceLists;
        /// <summary>
        /// Name of the postgresql instance.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Project id, default value is 0.
        /// </summary>
        public readonly int? ProjectId;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetInstancesResult(
            string? id,

            ImmutableArray<Outputs.GetInstancesInstanceListResult> instanceLists,

            string? name,

            int? projectId,

            string? resultOutputFile)
        {
            Id = id;
            InstanceLists = instanceLists;
            Name = name;
            ProjectId = projectId;
            ResultOutputFile = resultOutputFile;
        }
    }
}
