// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cam
{
    public static class Groups
    {
        public static Task<GroupsResult> InvokeAsync(GroupsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GroupsResult>("tencentcloud:Cam/groups:Groups", args ?? new GroupsArgs(), options.WithDefaults());

        public static Output<GroupsResult> Invoke(GroupsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GroupsResult>("tencentcloud:Cam/groups:Groups", args ?? new GroupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GroupsArgs : Pulumi.InvokeArgs
    {
        [Input("groupId")]
        public string? GroupId { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        [Input("remark")]
        public string? Remark { get; set; }

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GroupsArgs()
        {
        }
    }

    public sealed class GroupsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("groupId")]
        public Input<string>? GroupId { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("remark")]
        public Input<string>? Remark { get; set; }

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GroupsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GroupsResult
    {
        public readonly string? GroupId;
        public readonly ImmutableArray<Outputs.GroupsGroupListResult> GroupLists;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? Name;
        public readonly string? Remark;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GroupsResult(
            string? groupId,

            ImmutableArray<Outputs.GroupsGroupListResult> groupLists,

            string id,

            string? name,

            string? remark,

            string? resultOutputFile)
        {
            GroupId = groupId;
            GroupLists = groupLists;
            Id = id;
            Name = name;
            Remark = remark;
            ResultOutputFile = resultOutputFile;
        }
    }
}
