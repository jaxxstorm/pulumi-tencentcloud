// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cfs
{
    /// <summary>
    /// Provides a resource to create a cloud file system(CFS).
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
    ///         var foo = new Tencentcloud.Cfs.FileSystem("foo", new Tencentcloud.Cfs.FileSystemArgs
    ///         {
    ///             AccessGroupId = "pgroup-7nx89k7l",
    ///             AvailabilityZone = "ap-guangzhou-3",
    ///             Protocol = "NFS",
    ///             SubnetId = "subnet-9mu2t9iw",
    ///             VpcId = "vpc-ah9fbkap",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Cloud file system can be imported using the id, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Cfs/fileSystem:FileSystem foo cfs-6hgquxmj
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Cfs/fileSystem:FileSystem")]
    public partial class FileSystem : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of a access group.
        /// </summary>
        [Output("accessGroupId")]
        public Output<string> AccessGroupId { get; private set; } = null!;

        /// <summary>
        /// The available zone that the file system locates at.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// Create time of the file system.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// IP of mount point.
        /// </summary>
        [Output("mountIp")]
        public Output<string> MountIp { get; private set; } = null!;

        /// <summary>
        /// Name of a file system.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// File service protocol. Valid values are `NFS` and `CIFS`. and the default is `NFS`.
        /// </summary>
        [Output("protocol")]
        public Output<string?> Protocol { get; private set; } = null!;

        /// <summary>
        /// File service StorageType. Valid values are `SD` and `HP`. and the default is `SD`.
        /// </summary>
        [Output("storageType")]
        public Output<string?> StorageType { get; private set; } = null!;

        /// <summary>
        /// ID of a subnet.
        /// </summary>
        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;

        /// <summary>
        /// Instance tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// ID of a VPC network.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a FileSystem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FileSystem(string name, FileSystemArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Cfs/fileSystem:FileSystem", name, args ?? new FileSystemArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FileSystem(string name, Input<string> id, FileSystemState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Cfs/fileSystem:FileSystem", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing FileSystem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FileSystem Get(string name, Input<string> id, FileSystemState? state = null, CustomResourceOptions? options = null)
        {
            return new FileSystem(name, id, state, options);
        }
    }

    public sealed class FileSystemArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of a access group.
        /// </summary>
        [Input("accessGroupId", required: true)]
        public Input<string> AccessGroupId { get; set; } = null!;

        /// <summary>
        /// The available zone that the file system locates at.
        /// </summary>
        [Input("availabilityZone", required: true)]
        public Input<string> AvailabilityZone { get; set; } = null!;

        /// <summary>
        /// IP of mount point.
        /// </summary>
        [Input("mountIp")]
        public Input<string>? MountIp { get; set; }

        /// <summary>
        /// Name of a file system.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// File service protocol. Valid values are `NFS` and `CIFS`. and the default is `NFS`.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// File service StorageType. Valid values are `SD` and `HP`. and the default is `SD`.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// ID of a subnet.
        /// </summary>
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Instance tags.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// ID of a VPC network.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public FileSystemArgs()
        {
        }
    }

    public sealed class FileSystemState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of a access group.
        /// </summary>
        [Input("accessGroupId")]
        public Input<string>? AccessGroupId { get; set; }

        /// <summary>
        /// The available zone that the file system locates at.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// Create time of the file system.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// IP of mount point.
        /// </summary>
        [Input("mountIp")]
        public Input<string>? MountIp { get; set; }

        /// <summary>
        /// Name of a file system.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// File service protocol. Valid values are `NFS` and `CIFS`. and the default is `NFS`.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// File service StorageType. Valid values are `SD` and `HP`. and the default is `SD`.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// ID of a subnet.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Instance tags.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// ID of a VPC network.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public FileSystemState()
        {
        }
    }
}
