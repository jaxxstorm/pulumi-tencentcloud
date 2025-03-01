// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cam
{
    /// <summary>
    /// Provides a resource to create a CAM group policy attachment.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Tencentcloud = Pulumi.Tencentcloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var foo = new Tencentcloud.Cam.GroupPolicyAttachment("foo", new Tencentcloud.Cam.GroupPolicyAttachmentArgs
    ///         {
    ///             GroupId = tencentcloud_cam_group.Foo.Id,
    ///             PolicyId = tencentcloud_cam_policy.Foo.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// CAM group policy attachment can be imported using the id, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Cam/groupPolicyAttachment:GroupPolicyAttachment foo 12515263#26800353
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Cam/groupPolicyAttachment:GroupPolicyAttachment")]
    public partial class GroupPolicyAttachment : Pulumi.CustomResource
    {
        /// <summary>
        /// Mode of Creation of the CAM group policy attachment. `1` means the cam policy attachment is created by production, and the others indicate syntax strategy ways.
        /// </summary>
        [Output("createMode")]
        public Output<int> CreateMode { get; private set; } = null!;

        /// <summary>
        /// Create time of the CAM group policy attachment.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// ID of the attached CAM group.
        /// </summary>
        [Output("groupId")]
        public Output<string> GroupId { get; private set; } = null!;

        /// <summary>
        /// ID of the policy.
        /// </summary>
        [Output("policyId")]
        public Output<string> PolicyId { get; private set; } = null!;

        /// <summary>
        /// Name of the policy.
        /// </summary>
        [Output("policyName")]
        public Output<string> PolicyName { get; private set; } = null!;

        /// <summary>
        /// Type of the policy strategy. 'Group' means customer strategy and 'QCS' means preset strategy.
        /// </summary>
        [Output("policyType")]
        public Output<string> PolicyType { get; private set; } = null!;


        /// <summary>
        /// Create a GroupPolicyAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GroupPolicyAttachment(string name, GroupPolicyAttachmentArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Cam/groupPolicyAttachment:GroupPolicyAttachment", name, args ?? new GroupPolicyAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GroupPolicyAttachment(string name, Input<string> id, GroupPolicyAttachmentState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Cam/groupPolicyAttachment:GroupPolicyAttachment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GroupPolicyAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GroupPolicyAttachment Get(string name, Input<string> id, GroupPolicyAttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new GroupPolicyAttachment(name, id, state, options);
        }
    }

    public sealed class GroupPolicyAttachmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the attached CAM group.
        /// </summary>
        [Input("groupId", required: true)]
        public Input<string> GroupId { get; set; } = null!;

        /// <summary>
        /// ID of the policy.
        /// </summary>
        [Input("policyId", required: true)]
        public Input<string> PolicyId { get; set; } = null!;

        public GroupPolicyAttachmentArgs()
        {
        }
    }

    public sealed class GroupPolicyAttachmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Mode of Creation of the CAM group policy attachment. `1` means the cam policy attachment is created by production, and the others indicate syntax strategy ways.
        /// </summary>
        [Input("createMode")]
        public Input<int>? CreateMode { get; set; }

        /// <summary>
        /// Create time of the CAM group policy attachment.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// ID of the attached CAM group.
        /// </summary>
        [Input("groupId")]
        public Input<string>? GroupId { get; set; }

        /// <summary>
        /// ID of the policy.
        /// </summary>
        [Input("policyId")]
        public Input<string>? PolicyId { get; set; }

        /// <summary>
        /// Name of the policy.
        /// </summary>
        [Input("policyName")]
        public Input<string>? PolicyName { get; set; }

        /// <summary>
        /// Type of the policy strategy. 'Group' means customer strategy and 'QCS' means preset strategy.
        /// </summary>
        [Input("policyType")]
        public Input<string>? PolicyType { get; set; }

        public GroupPolicyAttachmentState()
        {
        }
    }
}
