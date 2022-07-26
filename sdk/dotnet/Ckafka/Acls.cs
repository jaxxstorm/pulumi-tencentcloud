// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Ckafka
{
    public static class Acls
    {
        public static Task<AclsResult> InvokeAsync(AclsArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<AclsResult>("tencentcloud:Ckafka/acls:Acls", args ?? new AclsArgs(), options.WithDefaults());

        public static Output<AclsResult> Invoke(AclsInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<AclsResult>("tencentcloud:Ckafka/acls:Acls", args ?? new AclsInvokeArgs(), options.WithDefaults());
    }


    public sealed class AclsArgs : Pulumi.InvokeArgs
    {
        [Input("host")]
        public string? Host { get; set; }

        [Input("instanceId", required: true)]
        public string InstanceId { get; set; } = null!;

        [Input("resourceName", required: true)]
        public string ResourceName { get; set; } = null!;

        [Input("resourceType", required: true)]
        public string ResourceType { get; set; } = null!;

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public AclsArgs()
        {
        }
    }

    public sealed class AclsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        [Input("resourceName", required: true)]
        public Input<string> ResourceName { get; set; } = null!;

        [Input("resourceType", required: true)]
        public Input<string> ResourceType { get; set; } = null!;

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public AclsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class AclsResult
    {
        public readonly ImmutableArray<Outputs.AclsAclListResult> AclLists;
        public readonly string? Host;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string InstanceId;
        public readonly string ResourceName;
        public readonly string ResourceType;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private AclsResult(
            ImmutableArray<Outputs.AclsAclListResult> aclLists,

            string? host,

            string id,

            string instanceId,

            string resourceName,

            string resourceType,

            string? resultOutputFile)
        {
            AclLists = aclLists;
            Host = host;
            Id = id;
            InstanceId = instanceId;
            ResourceName = resourceName;
            ResourceType = resourceType;
            ResultOutputFile = resultOutputFile;
        }
    }
}
