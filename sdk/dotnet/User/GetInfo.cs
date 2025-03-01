// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.User
{
    public static class GetInfo
    {
        /// <summary>
        /// Use this data source to query user appid, uin and ownerUin.
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
        ///         var foo = Output.Create(Tencentcloud.User.GetInfo.InvokeAsync());
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetInfoResult> InvokeAsync(GetInfoArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInfoResult>("tencentcloud:User/getInfo:getInfo", args ?? new GetInfoArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query user appid, uin and ownerUin.
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
        ///         var foo = Output.Create(Tencentcloud.User.GetInfo.InvokeAsync());
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetInfoResult> Invoke(GetInfoInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetInfoResult>("tencentcloud:User/getInfo:getInfo", args ?? new GetInfoInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInfoArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Used for save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetInfoArgs()
        {
        }
    }

    public sealed class GetInfoInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Used for save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetInfoInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetInfoResult
    {
        /// <summary>
        /// Current account App ID.
        /// </summary>
        public readonly string AppId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Current account Name. NOTE: only support subaccount.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Current account OwnerUIN.
        /// </summary>
        public readonly string OwnerUin;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// Current account UIN.
        /// </summary>
        public readonly string Uin;

        [OutputConstructor]
        private GetInfoResult(
            string appId,

            string id,

            string name,

            string ownerUin,

            string? resultOutputFile,

            string uin)
        {
            AppId = appId;
            Id = id;
            Name = name;
            OwnerUin = ownerUin;
            ResultOutputFile = resultOutputFile;
            Uin = uin;
        }
    }
}
