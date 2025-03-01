// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cam
{
    public static class GetPolicies
    {
        /// <summary>
        /// Use this data source to query detailed information of CAM policies
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
        ///         var foo = Output.Create(Tencentcloud.Cam.GetPolicies.InvokeAsync(new Tencentcloud.Cam.GetPoliciesArgs
        ///         {
        ///             PolicyId = tencentcloud_cam_policy.Foo.Id,
        ///         }));
        ///         var bar = Output.Create(Tencentcloud.Cam.GetPolicies.InvokeAsync(new Tencentcloud.Cam.GetPoliciesArgs
        ///         {
        ///             PolicyId = tencentcloud_cam_policy.Foo.Id,
        ///             Name = "tf-auto-test",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPoliciesResult> InvokeAsync(GetPoliciesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPoliciesResult>("tencentcloud:Cam/getPolicies:getPolicies", args ?? new GetPoliciesArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query detailed information of CAM policies
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
        ///         var foo = Output.Create(Tencentcloud.Cam.GetPolicies.InvokeAsync(new Tencentcloud.Cam.GetPoliciesArgs
        ///         {
        ///             PolicyId = tencentcloud_cam_policy.Foo.Id,
        ///         }));
        ///         var bar = Output.Create(Tencentcloud.Cam.GetPolicies.InvokeAsync(new Tencentcloud.Cam.GetPoliciesArgs
        ///         {
        ///             PolicyId = tencentcloud_cam_policy.Foo.Id,
        ///             Name = "tf-auto-test",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetPoliciesResult> Invoke(GetPoliciesInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPoliciesResult>("tencentcloud:Cam/getPolicies:getPolicies", args ?? new GetPoliciesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPoliciesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Mode of creation of policy strategy. Valid values: `1`, `2`. `1` means policy was created with console, and `2` means it was created by strategies.
        /// </summary>
        [Input("createMode")]
        public int? CreateMode { get; set; }

        /// <summary>
        /// The description of the CAM policy.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// Name of the CAM policy to be queried.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// ID of CAM policy to be queried.
        /// </summary>
        [Input("policyId")]
        public string? PolicyId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        /// <summary>
        /// Type of the policy strategy. Valid values: `1`, `2`. `1` means customer strategy and `2` means preset strategy.
        /// </summary>
        [Input("type")]
        public int? Type { get; set; }

        public GetPoliciesArgs()
        {
        }
    }

    public sealed class GetPoliciesInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Mode of creation of policy strategy. Valid values: `1`, `2`. `1` means policy was created with console, and `2` means it was created by strategies.
        /// </summary>
        [Input("createMode")]
        public Input<int>? CreateMode { get; set; }

        /// <summary>
        /// The description of the CAM policy.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the CAM policy to be queried.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// ID of CAM policy to be queried.
        /// </summary>
        [Input("policyId")]
        public Input<string>? PolicyId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        /// <summary>
        /// Type of the policy strategy. Valid values: `1`, `2`. `1` means customer strategy and `2` means preset strategy.
        /// </summary>
        [Input("type")]
        public Input<int>? Type { get; set; }

        public GetPoliciesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPoliciesResult
    {
        /// <summary>
        /// Mode of creation of policy strategy. `1` means policy was created with console, and `2` means it was created by strategies.
        /// </summary>
        public readonly int? CreateMode;
        /// <summary>
        /// Description of CAM policy.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of CAM policy.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// ID of the policy strategy.
        /// </summary>
        public readonly string? PolicyId;
        /// <summary>
        /// A list of CAM policies. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPoliciesPolicyListResult> PolicyLists;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// Type of the policy strategy. `1` means customer strategy and `2` means preset strategy.
        /// </summary>
        public readonly int? Type;

        [OutputConstructor]
        private GetPoliciesResult(
            int? createMode,

            string? description,

            string id,

            string? name,

            string? policyId,

            ImmutableArray<Outputs.GetPoliciesPolicyListResult> policyLists,

            string? resultOutputFile,

            int? type)
        {
            CreateMode = createMode;
            Description = description;
            Id = id;
            Name = name;
            PolicyId = policyId;
            PolicyLists = policyLists;
            ResultOutputFile = resultOutputFile;
            Type = type;
        }
    }
}
