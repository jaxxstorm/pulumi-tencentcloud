// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cbs
{
    /// <summary>
    /// Provides a resource to create a CBS.
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
    ///         var storage = new Tencentcloud.Cbs.Storage("storage", new Tencentcloud.Cbs.StorageArgs
    ///         {
    ///             AvailabilityZone = "ap-guangzhou-3",
    ///             Encrypt = false,
    ///             ProjectId = 0,
    ///             StorageName = "mystorage",
    ///             StorageSize = 100,
    ///             StorageType = "CLOUD_SSD",
    ///             Tags = 
    ///             {
    ///                 { "test", "tf" },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// CBS storage can be imported using the id, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Cbs/storage:Storage storage disk-41s6jwy4
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Cbs/storage:Storage")]
    public partial class Storage : Pulumi.CustomResource
    {
        /// <summary>
        /// Indicates whether the CBS is mounted the CVM.
        /// </summary>
        [Output("attached")]
        public Output<bool> Attached { get; private set; } = null!;

        /// <summary>
        /// The available zone that the CBS instance locates at.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The charge type of CBS instance. Valid values are `PREPAID` and `POSTPAID_BY_HOUR`. The default is `POSTPAID_BY_HOUR`.
        /// </summary>
        [Output("chargeType")]
        public Output<string?> ChargeType { get; private set; } = null!;

        /// <summary>
        /// Indicates whether CBS is encrypted.
        /// </summary>
        [Output("encrypt")]
        public Output<bool?> Encrypt { get; private set; } = null!;

        /// <summary>
        /// Indicate whether to delete CBS instance directly or not. Default is false. If set true, the instance will be deleted instead of staying recycle bin.
        /// </summary>
        [Output("forceDelete")]
        public Output<bool?> ForceDelete { get; private set; } = null!;

        /// <summary>
        /// It has been deprecated from version 1.33.0. Set `prepaid_period` instead. The purchased usage period of CBS. Valid values: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36].
        /// </summary>
        [Output("period")]
        public Output<int?> Period { get; private set; } = null!;

        /// <summary>
        /// The tenancy (time unit is month) of the prepaid instance, NOTE: it only works when charge_type is set to `PREPAID`. Valid values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        /// </summary>
        [Output("prepaidPeriod")]
        public Output<int> PrepaidPeriod { get; private set; } = null!;

        /// <summary>
        /// Auto Renewal flag. Value range: `NOTIFY_AND_AUTO_RENEW`: Notify expiry and renew automatically, `NOTIFY_AND_MANUAL_RENEW`: Notify expiry but do not renew automatically, `DISABLE_NOTIFY_AND_MANUAL_RENEW`: Neither notify expiry nor renew automatically. Default value range: `NOTIFY_AND_MANUAL_RENEW`: Notify expiry but do not renew automatically. NOTE: it only works when charge_type is set to `PREPAID`.
        /// </summary>
        [Output("prepaidRenewFlag")]
        public Output<string> PrepaidRenewFlag { get; private set; } = null!;

        /// <summary>
        /// ID of the project to which the instance belongs.
        /// </summary>
        [Output("projectId")]
        public Output<int?> ProjectId { get; private set; } = null!;

        /// <summary>
        /// ID of the snapshot. If specified, created the CBS by this snapshot.
        /// </summary>
        [Output("snapshotId")]
        public Output<string> SnapshotId { get; private set; } = null!;

        /// <summary>
        /// Name of CBS. The maximum length can not exceed 60 bytes.
        /// </summary>
        [Output("storageName")]
        public Output<string> StorageName { get; private set; } = null!;

        /// <summary>
        /// Volume of CBS, and unit is GB. If storage type is `CLOUD_SSD`, the size range is [100, 16000], and the others are [10-16000].
        /// </summary>
        [Output("storageSize")]
        public Output<int> StorageSize { get; private set; } = null!;

        /// <summary>
        /// Status of CBS. Valid values: UNATTACHED, ATTACHING, ATTACHED, DETACHING, EXPANDING, ROLLBACKING, TORECYCLE and DUMPING.
        /// </summary>
        [Output("storageStatus")]
        public Output<string> StorageStatus { get; private set; } = null!;

        /// <summary>
        /// Type of CBS medium. Valid values: CLOUD_PREMIUM, CLOUD_SSD, CLOUD_TSSD and CLOUD_HSSD.
        /// </summary>
        [Output("storageType")]
        public Output<string> StorageType { get; private set; } = null!;

        /// <summary>
        /// The available tags within this CBS.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// Add extra performance to the data disk. Only works when disk type is `CLOUD_TSSD` or `CLOUD_HSSD`.
        /// </summary>
        [Output("throughputPerformance")]
        public Output<int?> ThroughputPerformance { get; private set; } = null!;


        /// <summary>
        /// Create a Storage resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Storage(string name, StorageArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Cbs/storage:Storage", name, args ?? new StorageArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Storage(string name, Input<string> id, StorageState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Cbs/storage:Storage", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Storage resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Storage Get(string name, Input<string> id, StorageState? state = null, CustomResourceOptions? options = null)
        {
            return new Storage(name, id, state, options);
        }
    }

    public sealed class StorageArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The available zone that the CBS instance locates at.
        /// </summary>
        [Input("availabilityZone", required: true)]
        public Input<string> AvailabilityZone { get; set; } = null!;

        /// <summary>
        /// The charge type of CBS instance. Valid values are `PREPAID` and `POSTPAID_BY_HOUR`. The default is `POSTPAID_BY_HOUR`.
        /// </summary>
        [Input("chargeType")]
        public Input<string>? ChargeType { get; set; }

        /// <summary>
        /// Indicates whether CBS is encrypted.
        /// </summary>
        [Input("encrypt")]
        public Input<bool>? Encrypt { get; set; }

        /// <summary>
        /// Indicate whether to delete CBS instance directly or not. Default is false. If set true, the instance will be deleted instead of staying recycle bin.
        /// </summary>
        [Input("forceDelete")]
        public Input<bool>? ForceDelete { get; set; }

        /// <summary>
        /// It has been deprecated from version 1.33.0. Set `prepaid_period` instead. The purchased usage period of CBS. Valid values: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36].
        /// </summary>
        [Input("period")]
        public Input<int>? Period { get; set; }

        /// <summary>
        /// The tenancy (time unit is month) of the prepaid instance, NOTE: it only works when charge_type is set to `PREPAID`. Valid values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        /// </summary>
        [Input("prepaidPeriod")]
        public Input<int>? PrepaidPeriod { get; set; }

        /// <summary>
        /// Auto Renewal flag. Value range: `NOTIFY_AND_AUTO_RENEW`: Notify expiry and renew automatically, `NOTIFY_AND_MANUAL_RENEW`: Notify expiry but do not renew automatically, `DISABLE_NOTIFY_AND_MANUAL_RENEW`: Neither notify expiry nor renew automatically. Default value range: `NOTIFY_AND_MANUAL_RENEW`: Notify expiry but do not renew automatically. NOTE: it only works when charge_type is set to `PREPAID`.
        /// </summary>
        [Input("prepaidRenewFlag")]
        public Input<string>? PrepaidRenewFlag { get; set; }

        /// <summary>
        /// ID of the project to which the instance belongs.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// ID of the snapshot. If specified, created the CBS by this snapshot.
        /// </summary>
        [Input("snapshotId")]
        public Input<string>? SnapshotId { get; set; }

        /// <summary>
        /// Name of CBS. The maximum length can not exceed 60 bytes.
        /// </summary>
        [Input("storageName", required: true)]
        public Input<string> StorageName { get; set; } = null!;

        /// <summary>
        /// Volume of CBS, and unit is GB. If storage type is `CLOUD_SSD`, the size range is [100, 16000], and the others are [10-16000].
        /// </summary>
        [Input("storageSize", required: true)]
        public Input<int> StorageSize { get; set; } = null!;

        /// <summary>
        /// Type of CBS medium. Valid values: CLOUD_PREMIUM, CLOUD_SSD, CLOUD_TSSD and CLOUD_HSSD.
        /// </summary>
        [Input("storageType", required: true)]
        public Input<string> StorageType { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// The available tags within this CBS.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Add extra performance to the data disk. Only works when disk type is `CLOUD_TSSD` or `CLOUD_HSSD`.
        /// </summary>
        [Input("throughputPerformance")]
        public Input<int>? ThroughputPerformance { get; set; }

        public StorageArgs()
        {
        }
    }

    public sealed class StorageState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether the CBS is mounted the CVM.
        /// </summary>
        [Input("attached")]
        public Input<bool>? Attached { get; set; }

        /// <summary>
        /// The available zone that the CBS instance locates at.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The charge type of CBS instance. Valid values are `PREPAID` and `POSTPAID_BY_HOUR`. The default is `POSTPAID_BY_HOUR`.
        /// </summary>
        [Input("chargeType")]
        public Input<string>? ChargeType { get; set; }

        /// <summary>
        /// Indicates whether CBS is encrypted.
        /// </summary>
        [Input("encrypt")]
        public Input<bool>? Encrypt { get; set; }

        /// <summary>
        /// Indicate whether to delete CBS instance directly or not. Default is false. If set true, the instance will be deleted instead of staying recycle bin.
        /// </summary>
        [Input("forceDelete")]
        public Input<bool>? ForceDelete { get; set; }

        /// <summary>
        /// It has been deprecated from version 1.33.0. Set `prepaid_period` instead. The purchased usage period of CBS. Valid values: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36].
        /// </summary>
        [Input("period")]
        public Input<int>? Period { get; set; }

        /// <summary>
        /// The tenancy (time unit is month) of the prepaid instance, NOTE: it only works when charge_type is set to `PREPAID`. Valid values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        /// </summary>
        [Input("prepaidPeriod")]
        public Input<int>? PrepaidPeriod { get; set; }

        /// <summary>
        /// Auto Renewal flag. Value range: `NOTIFY_AND_AUTO_RENEW`: Notify expiry and renew automatically, `NOTIFY_AND_MANUAL_RENEW`: Notify expiry but do not renew automatically, `DISABLE_NOTIFY_AND_MANUAL_RENEW`: Neither notify expiry nor renew automatically. Default value range: `NOTIFY_AND_MANUAL_RENEW`: Notify expiry but do not renew automatically. NOTE: it only works when charge_type is set to `PREPAID`.
        /// </summary>
        [Input("prepaidRenewFlag")]
        public Input<string>? PrepaidRenewFlag { get; set; }

        /// <summary>
        /// ID of the project to which the instance belongs.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// ID of the snapshot. If specified, created the CBS by this snapshot.
        /// </summary>
        [Input("snapshotId")]
        public Input<string>? SnapshotId { get; set; }

        /// <summary>
        /// Name of CBS. The maximum length can not exceed 60 bytes.
        /// </summary>
        [Input("storageName")]
        public Input<string>? StorageName { get; set; }

        /// <summary>
        /// Volume of CBS, and unit is GB. If storage type is `CLOUD_SSD`, the size range is [100, 16000], and the others are [10-16000].
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// Status of CBS. Valid values: UNATTACHED, ATTACHING, ATTACHED, DETACHING, EXPANDING, ROLLBACKING, TORECYCLE and DUMPING.
        /// </summary>
        [Input("storageStatus")]
        public Input<string>? StorageStatus { get; set; }

        /// <summary>
        /// Type of CBS medium. Valid values: CLOUD_PREMIUM, CLOUD_SSD, CLOUD_TSSD and CLOUD_HSSD.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// The available tags within this CBS.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Add extra performance to the data disk. Only works when disk type is `CLOUD_TSSD` or `CLOUD_HSSD`.
        /// </summary>
        [Input("throughputPerformance")]
        public Input<int>? ThroughputPerformance { get; set; }

        public StorageState()
        {
        }
    }
}
