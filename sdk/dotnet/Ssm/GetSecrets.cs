// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Ssm
{
    public static class GetSecrets
    {
        /// <summary>
        /// Use this data source to query detailed information of SSM secret
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
        ///         var foo = Output.Create(Tencentcloud.Ssm.GetSecrets.InvokeAsync(new Tencentcloud.Ssm.GetSecretsArgs
        ///         {
        ///             OrderType = 1,
        ///             SecretName = "test",
        ///             State = 1,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSecretsResult> InvokeAsync(GetSecretsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSecretsResult>("tencentcloud:Ssm/getSecrets:getSecrets", args ?? new GetSecretsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query detailed information of SSM secret
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
        ///         var foo = Output.Create(Tencentcloud.Ssm.GetSecrets.InvokeAsync(new Tencentcloud.Ssm.GetSecretsArgs
        ///         {
        ///             OrderType = 1,
        ///             SecretName = "test",
        ///             State = 1,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetSecretsResult> Invoke(GetSecretsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSecretsResult>("tencentcloud:Ssm/getSecrets:getSecrets", args ?? new GetSecretsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSecretsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The order to sort the create time of secret. `0` - desc, `1` - asc. Default value is `0`.
        /// </summary>
        [Input("orderType")]
        public int? OrderType { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        /// <summary>
        /// Secret name used to filter result.
        /// </summary>
        [Input("secretName")]
        public string? SecretName { get; set; }

        /// <summary>
        /// Filter by state of secret. `0` - all secrets are queried, `1` - only Enabled secrets are queried, `2` - only Disabled secrets are queried, `3` - only PendingDelete secrets are queried.
        /// </summary>
        [Input("state")]
        public int? State { get; set; }

        [Input("tags")]
        private Dictionary<string, object>? _tags;

        /// <summary>
        /// Tags to filter secret.
        /// </summary>
        public Dictionary<string, object> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, object>());
            set => _tags = value;
        }

        public GetSecretsArgs()
        {
        }
    }

    public sealed class GetSecretsInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The order to sort the create time of secret. `0` - desc, `1` - asc. Default value is `0`.
        /// </summary>
        [Input("orderType")]
        public Input<int>? OrderType { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        /// <summary>
        /// Secret name used to filter result.
        /// </summary>
        [Input("secretName")]
        public Input<string>? SecretName { get; set; }

        /// <summary>
        /// Filter by state of secret. `0` - all secrets are queried, `1` - only Enabled secrets are queried, `2` - only Disabled secrets are queried, `3` - only PendingDelete secrets are queried.
        /// </summary>
        [Input("state")]
        public Input<int>? State { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Tags to filter secret.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public GetSecretsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSecretsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly int? OrderType;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// A list of SSM secrets.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSecretsSecretListResult> SecretLists;
        /// <summary>
        /// Name of secret.
        /// </summary>
        public readonly string? SecretName;
        public readonly int? State;
        public readonly ImmutableDictionary<string, object>? Tags;

        [OutputConstructor]
        private GetSecretsResult(
            string id,

            int? orderType,

            string? resultOutputFile,

            ImmutableArray<Outputs.GetSecretsSecretListResult> secretLists,

            string? secretName,

            int? state,

            ImmutableDictionary<string, object>? tags)
        {
            Id = id;
            OrderType = orderType;
            ResultOutputFile = resultOutputFile;
            SecretLists = secretLists;
            SecretName = secretName;
            State = state;
            Tags = tags;
        }
    }
}
