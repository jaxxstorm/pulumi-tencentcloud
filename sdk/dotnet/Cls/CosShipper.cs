// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cls
{
    /// <summary>
    /// Provides a resource to create a cls cos shipper.
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
    ///         var shipper = new Tencentcloud.Cls.CosShipper("shipper", new Tencentcloud.Cls.CosShipperArgs
    ///         {
    ///             Bucket = "preset-scf-bucket-1308919341",
    ///             Compress = new Tencentcloud.Cls.Inputs.CosShipperCompressArgs
    ///             {
    ///                 Format = "lzop",
    ///             },
    ///             Content = new Tencentcloud.Cls.Inputs.CosShipperContentArgs
    ///             {
    ///                 Format = "json",
    ///                 Json = new Tencentcloud.Cls.Inputs.CosShipperContentJsonArgs
    ///                 {
    ///                     EnableTag = true,
    ///                     MetaFields = 
    ///                     {
    ///                         "__FILENAME__",
    ///                         "__SOURCE__",
    ///                         "__TIMESTAMP__",
    ///                     },
    ///                 },
    ///             },
    ///             Interval = 300,
    ///             MaxSize = 200,
    ///             Partition = "/%Y/%m/%d/%H/",
    ///             Prefix = "ap-guangzhou-fffsasad-1649734752",
    ///             ShipperName = "ap-guangzhou-fffsasad-1649734752",
    ///             TopicId = "4d07fba0-b93e-4e0b-9a7f-d58542560bbb",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// cls cos shipper can be imported using the id, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Cls/cosShipper:CosShipper shipper 5d1b7b2a-c163-4c48-bb01-9ee00584d761
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Cls/cosShipper:CosShipper")]
    public partial class CosShipper : Pulumi.CustomResource
    {
        /// <summary>
        /// Destination bucket in the shipping rule to be created.
        /// </summary>
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        /// <summary>
        /// Compression configuration of shipped log.
        /// </summary>
        [Output("compress")]
        public Output<Outputs.CosShipperCompress?> Compress { get; private set; } = null!;

        /// <summary>
        /// Format configuration of shipped log content.
        /// </summary>
        [Output("content")]
        public Output<Outputs.CosShipperContent?> Content { get; private set; } = null!;

        /// <summary>
        /// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        /// </summary>
        [Output("filterRules")]
        public Output<ImmutableArray<Outputs.CosShipperFilterRule>> FilterRules { get; private set; } = null!;

        /// <summary>
        /// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        /// </summary>
        [Output("interval")]
        public Output<int?> Interval { get; private set; } = null!;

        /// <summary>
        /// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        /// </summary>
        [Output("maxSize")]
        public Output<int?> MaxSize { get; private set; } = null!;

        /// <summary>
        /// Partition rule of shipped log, which can be represented in strftime time format.
        /// </summary>
        [Output("partition")]
        public Output<string?> Partition { get; private set; } = null!;

        /// <summary>
        /// Prefix of the shipping directory in the shipping rule to be created.
        /// </summary>
        [Output("prefix")]
        public Output<string> Prefix { get; private set; } = null!;

        /// <summary>
        /// Shipping rule name.
        /// </summary>
        [Output("shipperName")]
        public Output<string> ShipperName { get; private set; } = null!;

        /// <summary>
        /// ID of the log topic to which the shipping rule to be created belongs.
        /// </summary>
        [Output("topicId")]
        public Output<string> TopicId { get; private set; } = null!;


        /// <summary>
        /// Create a CosShipper resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CosShipper(string name, CosShipperArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Cls/cosShipper:CosShipper", name, args ?? new CosShipperArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CosShipper(string name, Input<string> id, CosShipperState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Cls/cosShipper:CosShipper", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing CosShipper resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CosShipper Get(string name, Input<string> id, CosShipperState? state = null, CustomResourceOptions? options = null)
        {
            return new CosShipper(name, id, state, options);
        }
    }

    public sealed class CosShipperArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Destination bucket in the shipping rule to be created.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// Compression configuration of shipped log.
        /// </summary>
        [Input("compress")]
        public Input<Inputs.CosShipperCompressArgs>? Compress { get; set; }

        /// <summary>
        /// Format configuration of shipped log content.
        /// </summary>
        [Input("content")]
        public Input<Inputs.CosShipperContentArgs>? Content { get; set; }

        [Input("filterRules")]
        private InputList<Inputs.CosShipperFilterRuleArgs>? _filterRules;

        /// <summary>
        /// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        /// </summary>
        public InputList<Inputs.CosShipperFilterRuleArgs> FilterRules
        {
            get => _filterRules ?? (_filterRules = new InputList<Inputs.CosShipperFilterRuleArgs>());
            set => _filterRules = value;
        }

        /// <summary>
        /// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        /// <summary>
        /// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        /// </summary>
        [Input("maxSize")]
        public Input<int>? MaxSize { get; set; }

        /// <summary>
        /// Partition rule of shipped log, which can be represented in strftime time format.
        /// </summary>
        [Input("partition")]
        public Input<string>? Partition { get; set; }

        /// <summary>
        /// Prefix of the shipping directory in the shipping rule to be created.
        /// </summary>
        [Input("prefix", required: true)]
        public Input<string> Prefix { get; set; } = null!;

        /// <summary>
        /// Shipping rule name.
        /// </summary>
        [Input("shipperName", required: true)]
        public Input<string> ShipperName { get; set; } = null!;

        /// <summary>
        /// ID of the log topic to which the shipping rule to be created belongs.
        /// </summary>
        [Input("topicId", required: true)]
        public Input<string> TopicId { get; set; } = null!;

        public CosShipperArgs()
        {
        }
    }

    public sealed class CosShipperState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Destination bucket in the shipping rule to be created.
        /// </summary>
        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        /// <summary>
        /// Compression configuration of shipped log.
        /// </summary>
        [Input("compress")]
        public Input<Inputs.CosShipperCompressGetArgs>? Compress { get; set; }

        /// <summary>
        /// Format configuration of shipped log content.
        /// </summary>
        [Input("content")]
        public Input<Inputs.CosShipperContentGetArgs>? Content { get; set; }

        [Input("filterRules")]
        private InputList<Inputs.CosShipperFilterRuleGetArgs>? _filterRules;

        /// <summary>
        /// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        /// </summary>
        public InputList<Inputs.CosShipperFilterRuleGetArgs> FilterRules
        {
            get => _filterRules ?? (_filterRules = new InputList<Inputs.CosShipperFilterRuleGetArgs>());
            set => _filterRules = value;
        }

        /// <summary>
        /// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        /// <summary>
        /// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        /// </summary>
        [Input("maxSize")]
        public Input<int>? MaxSize { get; set; }

        /// <summary>
        /// Partition rule of shipped log, which can be represented in strftime time format.
        /// </summary>
        [Input("partition")]
        public Input<string>? Partition { get; set; }

        /// <summary>
        /// Prefix of the shipping directory in the shipping rule to be created.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        /// <summary>
        /// Shipping rule name.
        /// </summary>
        [Input("shipperName")]
        public Input<string>? ShipperName { get; set; }

        /// <summary>
        /// ID of the log topic to which the shipping rule to be created belongs.
        /// </summary>
        [Input("topicId")]
        public Input<string>? TopicId { get; set; }

        public CosShipperState()
        {
        }
    }
}
