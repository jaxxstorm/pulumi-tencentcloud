// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Ckafka
{
    public static class GetUsers
    {
        /// <summary>
        /// Use this data source to query detailed user information of Ckafka
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
        ///         var foo = Output.Create(Tencentcloud.Ckafka.GetUsers.InvokeAsync(new Tencentcloud.Ckafka.GetUsersArgs
        ///         {
        ///             AccountName = "test",
        ///             InstanceId = "ckafka-f9ife4zz",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetUsersResult> InvokeAsync(GetUsersArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetUsersResult>("tencentcloud:Ckafka/getUsers:getUsers", args ?? new GetUsersArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query detailed user information of Ckafka
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
        ///         var foo = Output.Create(Tencentcloud.Ckafka.GetUsers.InvokeAsync(new Tencentcloud.Ckafka.GetUsersArgs
        ///         {
        ///             AccountName = "test",
        ///             InstanceId = "ckafka-f9ife4zz",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetUsersResult> Invoke(GetUsersInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetUsersResult>("tencentcloud:Ckafka/getUsers:getUsers", args ?? new GetUsersInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUsersArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Account name used when query ckafka users' infos. Could be a substr of user name.
        /// </summary>
        [Input("accountName")]
        public string? AccountName { get; set; }

        /// <summary>
        /// Id of the ckafka instance.
        /// </summary>
        [Input("instanceId", required: true)]
        public string InstanceId { get; set; } = null!;

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetUsersArgs()
        {
        }
    }

    public sealed class GetUsersInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Account name used when query ckafka users' infos. Could be a substr of user name.
        /// </summary>
        [Input("accountName")]
        public Input<string>? AccountName { get; set; }

        /// <summary>
        /// Id of the ckafka instance.
        /// </summary>
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetUsersInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetUsersResult
    {
        /// <summary>
        /// Account name of user.
        /// </summary>
        public readonly string? AccountName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string InstanceId;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// A list of ckafka users. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetUsersUserListResult> UserLists;

        [OutputConstructor]
        private GetUsersResult(
            string? accountName,

            string id,

            string instanceId,

            string? resultOutputFile,

            ImmutableArray<Outputs.GetUsersUserListResult> userLists)
        {
            AccountName = accountName;
            Id = id;
            InstanceId = instanceId;
            ResultOutputFile = resultOutputFile;
            UserLists = userLists;
        }
    }
}
