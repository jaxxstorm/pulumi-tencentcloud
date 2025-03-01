// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cfs
{
    public static class GetFileSystems
    {
        /// <summary>
        /// Use this data source to query the detail information of cloud file systems(CFS).
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
        ///         var fileSystems = Output.Create(Tencentcloud.Cfs.GetFileSystems.InvokeAsync(new Tencentcloud.Cfs.GetFileSystemsArgs
        ///         {
        ///             AvailabilityZone = "ap-guangzhou-3",
        ///             FileSystemId = "cfs-6hgquxmj",
        ///             Name = "test",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetFileSystemsResult> InvokeAsync(GetFileSystemsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetFileSystemsResult>("tencentcloud:Cfs/getFileSystems:getFileSystems", args ?? new GetFileSystemsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query the detail information of cloud file systems(CFS).
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
        ///         var fileSystems = Output.Create(Tencentcloud.Cfs.GetFileSystems.InvokeAsync(new Tencentcloud.Cfs.GetFileSystemsArgs
        ///         {
        ///             AvailabilityZone = "ap-guangzhou-3",
        ///             FileSystemId = "cfs-6hgquxmj",
        ///             Name = "test",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetFileSystemsResult> Invoke(GetFileSystemsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetFileSystemsResult>("tencentcloud:Cfs/getFileSystems:getFileSystems", args ?? new GetFileSystemsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFileSystemsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The available zone that the file system locates at.
        /// </summary>
        [Input("availabilityZone")]
        public string? AvailabilityZone { get; set; }

        /// <summary>
        /// A specified file system ID used to query.
        /// </summary>
        [Input("fileSystemId")]
        public string? FileSystemId { get; set; }

        /// <summary>
        /// A file system name used to query.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        /// <summary>
        /// ID of a vpc subnet.
        /// </summary>
        [Input("subnetId")]
        public string? SubnetId { get; set; }

        /// <summary>
        /// ID of the vpc to be queried.
        /// </summary>
        [Input("vpcId")]
        public string? VpcId { get; set; }

        public GetFileSystemsArgs()
        {
        }
    }

    public sealed class GetFileSystemsInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The available zone that the file system locates at.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// A specified file system ID used to query.
        /// </summary>
        [Input("fileSystemId")]
        public Input<string>? FileSystemId { get; set; }

        /// <summary>
        /// A file system name used to query.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        /// <summary>
        /// ID of a vpc subnet.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        /// <summary>
        /// ID of the vpc to be queried.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public GetFileSystemsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetFileSystemsResult
    {
        /// <summary>
        /// The available zone that the file system locates at.
        /// </summary>
        public readonly string? AvailabilityZone;
        /// <summary>
        /// ID of the file system.
        /// </summary>
        public readonly string? FileSystemId;
        /// <summary>
        /// An information list of cloud file system. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetFileSystemsFileSystemListResult> FileSystemLists;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of the file system.
        /// </summary>
        public readonly string? Name;
        public readonly string? ResultOutputFile;
        public readonly string? SubnetId;
        public readonly string? VpcId;

        [OutputConstructor]
        private GetFileSystemsResult(
            string? availabilityZone,

            string? fileSystemId,

            ImmutableArray<Outputs.GetFileSystemsFileSystemListResult> fileSystemLists,

            string id,

            string? name,

            string? resultOutputFile,

            string? subnetId,

            string? vpcId)
        {
            AvailabilityZone = availabilityZone;
            FileSystemId = fileSystemId;
            FileSystemLists = fileSystemLists;
            Id = id;
            Name = name;
            ResultOutputFile = resultOutputFile;
            SubnetId = subnetId;
            VpcId = vpcId;
        }
    }
}
