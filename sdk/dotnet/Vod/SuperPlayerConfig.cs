// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Vod
{
    /// <summary>
    /// Provide a resource to create a VOD super player config.
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
    ///         var fooAdaptiveDynamicStreamingTemplate = new Tencentcloud.Vod.AdaptiveDynamicStreamingTemplate("fooAdaptiveDynamicStreamingTemplate", new Tencentcloud.Vod.AdaptiveDynamicStreamingTemplateArgs
    ///         {
    ///             Format = "HLS",
    ///             DrmType = "SimpleAES",
    ///             DisableHigherVideoBitrate = false,
    ///             DisableHigherVideoResolution = false,
    ///             Comment = "test",
    ///             StreamInfos = 
    ///             {
    ///                 new Tencentcloud.Vod.Inputs.AdaptiveDynamicStreamingTemplateStreamInfoArgs
    ///                 {
    ///                     Video = new Tencentcloud.Vod.Inputs.AdaptiveDynamicStreamingTemplateStreamInfoVideoArgs
    ///                     {
    ///                         Codec = "libx265",
    ///                         Fps = 4,
    ///                         Bitrate = 129,
    ///                         ResolutionAdaptive = false,
    ///                         Width = 128,
    ///                         Height = 128,
    ///                         FillType = "stretch",
    ///                     },
    ///                     Audio = new Tencentcloud.Vod.Inputs.AdaptiveDynamicStreamingTemplateStreamInfoAudioArgs
    ///                     {
    ///                         Codec = "libmp3lame",
    ///                         Bitrate = 129,
    ///                         SampleRate = 44100,
    ///                         AudioChannel = "dual",
    ///                     },
    ///                     RemoveAudio = false,
    ///                 },
    ///                 new Tencentcloud.Vod.Inputs.AdaptiveDynamicStreamingTemplateStreamInfoArgs
    ///                 {
    ///                     Video = new Tencentcloud.Vod.Inputs.AdaptiveDynamicStreamingTemplateStreamInfoVideoArgs
    ///                     {
    ///                         Codec = "libx264",
    ///                         Fps = 4,
    ///                         Bitrate = 256,
    ///                     },
    ///                     Audio = new Tencentcloud.Vod.Inputs.AdaptiveDynamicStreamingTemplateStreamInfoAudioArgs
    ///                     {
    ///                         Codec = "libfdk_aac",
    ///                         Bitrate = 256,
    ///                         SampleRate = 44100,
    ///                     },
    ///                     RemoveAudio = true,
    ///                 },
    ///             },
    ///         });
    ///         var fooImageSpriteTemplate = new Tencentcloud.Vod.ImageSpriteTemplate("fooImageSpriteTemplate", new Tencentcloud.Vod.ImageSpriteTemplateArgs
    ///         {
    ///             SampleType = "Percent",
    ///             SampleInterval = 10,
    ///             RowCount = 3,
    ///             ColumnCount = 3,
    ///             Comment = "test",
    ///             FillType = "stretch",
    ///             Width = 128,
    ///             Height = 128,
    ///             ResolutionAdaptive = false,
    ///         });
    ///         var fooSuperPlayerConfig = new Tencentcloud.Vod.SuperPlayerConfig("fooSuperPlayerConfig", new Tencentcloud.Vod.SuperPlayerConfigArgs
    ///         {
    ///             DrmSwitch = true,
    ///             DrmStreamingInfo = new Tencentcloud.Vod.Inputs.SuperPlayerConfigDrmStreamingInfoArgs
    ///             {
    ///                 SimpleAesDefinition = fooAdaptiveDynamicStreamingTemplate.Id,
    ///             },
    ///             ImageSpriteDefinition = fooImageSpriteTemplate.Id,
    ///             ResolutionNames = 
    ///             {
    ///                 new Tencentcloud.Vod.Inputs.SuperPlayerConfigResolutionNameArgs
    ///                 {
    ///                     MinEdgeLength = 889,
    ///                     Name = "test1",
    ///                 },
    ///                 new Tencentcloud.Vod.Inputs.SuperPlayerConfigResolutionNameArgs
    ///                 {
    ///                     MinEdgeLength = 890,
    ///                     Name = "test2",
    ///                 },
    ///             },
    ///             Domain = "Default",
    ///             Scheme = "Default",
    ///             Comment = "test",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// VOD super player config can be imported using the name, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Vod/superPlayerConfig:SuperPlayerConfig foo tf-super-player
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Vod/superPlayerConfig:SuperPlayerConfig")]
    public partial class SuperPlayerConfig : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of the unencrypted adaptive bitrate streaming template that allows output, which is required if `drm_switch` is `false`.
        /// </summary>
        [Output("adaptiveDynamicStreamingDefinition")]
        public Output<string?> AdaptiveDynamicStreamingDefinition { get; private set; } = null!;

        /// <summary>
        /// Template description. Length limit: 256 characters.
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        /// <summary>
        /// Creation time of template in ISO date format.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Domain name used for playback. If it is left empty or set to `Default`, the domain name configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. `Default` by default.
        /// </summary>
        [Output("domain")]
        public Output<string?> Domain { get; private set; } = null!;

        /// <summary>
        /// Content of the DRM-protected adaptive bitrate streaming template that allows output, which is required if `drm_switch` is `true`.
        /// </summary>
        [Output("drmStreamingInfo")]
        public Output<Outputs.SuperPlayerConfigDrmStreamingInfo?> DrmStreamingInfo { get; private set; } = null!;

        /// <summary>
        /// Switch of DRM-protected adaptive bitstream playback: `true`: enabled, indicating to play back only output adaptive bitstreams protected by DRM; `false`: disabled, indicating to play back unencrypted output adaptive bitstreams. Default value: `false`.
        /// </summary>
        [Output("drmSwitch")]
        public Output<bool?> DrmSwitch { get; private set; } = null!;

        /// <summary>
        /// ID of the image sprite template that allows output.
        /// </summary>
        [Output("imageSpriteDefinition")]
        public Output<string?> ImageSpriteDefinition { get; private set; } = null!;

        /// <summary>
        /// Player configuration name, which can contain up to 64 letters, digits, underscores, and hyphens (such as test_ABC-123) and must be unique under a user.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Display name of player for substreams with different resolutions. If this parameter is left empty or an empty array, the default configuration will be used: `min_edge_length: 240, name: LD`; `min_edge_length: 480, name: SD`; `min_edge_length: 720, name: HD`; `min_edge_length: 1080, name: FHD`; `min_edge_length: 1440, name: 2K`; `min_edge_length: 2160, name: 4K`; `min_edge_length: 4320, name: 8K`.
        /// </summary>
        [Output("resolutionNames")]
        public Output<ImmutableArray<Outputs.SuperPlayerConfigResolutionName>> ResolutionNames { get; private set; } = null!;

        /// <summary>
        /// Scheme used for playback. If it is left empty or set to `Default`, the scheme configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. Other valid values: `HTTP`; `HTTPS`.
        /// </summary>
        [Output("scheme")]
        public Output<string?> Scheme { get; private set; } = null!;

        /// <summary>
        /// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
        /// </summary>
        [Output("subAppId")]
        public Output<int?> SubAppId { get; private set; } = null!;

        /// <summary>
        /// Last modified time of template in ISO date format.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a SuperPlayerConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SuperPlayerConfig(string name, SuperPlayerConfigArgs? args = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Vod/superPlayerConfig:SuperPlayerConfig", name, args ?? new SuperPlayerConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SuperPlayerConfig(string name, Input<string> id, SuperPlayerConfigState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Vod/superPlayerConfig:SuperPlayerConfig", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SuperPlayerConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SuperPlayerConfig Get(string name, Input<string> id, SuperPlayerConfigState? state = null, CustomResourceOptions? options = null)
        {
            return new SuperPlayerConfig(name, id, state, options);
        }
    }

    public sealed class SuperPlayerConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the unencrypted adaptive bitrate streaming template that allows output, which is required if `drm_switch` is `false`.
        /// </summary>
        [Input("adaptiveDynamicStreamingDefinition")]
        public Input<string>? AdaptiveDynamicStreamingDefinition { get; set; }

        /// <summary>
        /// Template description. Length limit: 256 characters.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Domain name used for playback. If it is left empty or set to `Default`, the domain name configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. `Default` by default.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// Content of the DRM-protected adaptive bitrate streaming template that allows output, which is required if `drm_switch` is `true`.
        /// </summary>
        [Input("drmStreamingInfo")]
        public Input<Inputs.SuperPlayerConfigDrmStreamingInfoArgs>? DrmStreamingInfo { get; set; }

        /// <summary>
        /// Switch of DRM-protected adaptive bitstream playback: `true`: enabled, indicating to play back only output adaptive bitstreams protected by DRM; `false`: disabled, indicating to play back unencrypted output adaptive bitstreams. Default value: `false`.
        /// </summary>
        [Input("drmSwitch")]
        public Input<bool>? DrmSwitch { get; set; }

        /// <summary>
        /// ID of the image sprite template that allows output.
        /// </summary>
        [Input("imageSpriteDefinition")]
        public Input<string>? ImageSpriteDefinition { get; set; }

        /// <summary>
        /// Player configuration name, which can contain up to 64 letters, digits, underscores, and hyphens (such as test_ABC-123) and must be unique under a user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resolutionNames")]
        private InputList<Inputs.SuperPlayerConfigResolutionNameArgs>? _resolutionNames;

        /// <summary>
        /// Display name of player for substreams with different resolutions. If this parameter is left empty or an empty array, the default configuration will be used: `min_edge_length: 240, name: LD`; `min_edge_length: 480, name: SD`; `min_edge_length: 720, name: HD`; `min_edge_length: 1080, name: FHD`; `min_edge_length: 1440, name: 2K`; `min_edge_length: 2160, name: 4K`; `min_edge_length: 4320, name: 8K`.
        /// </summary>
        public InputList<Inputs.SuperPlayerConfigResolutionNameArgs> ResolutionNames
        {
            get => _resolutionNames ?? (_resolutionNames = new InputList<Inputs.SuperPlayerConfigResolutionNameArgs>());
            set => _resolutionNames = value;
        }

        /// <summary>
        /// Scheme used for playback. If it is left empty or set to `Default`, the scheme configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. Other valid values: `HTTP`; `HTTPS`.
        /// </summary>
        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        /// <summary>
        /// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
        /// </summary>
        [Input("subAppId")]
        public Input<int>? SubAppId { get; set; }

        public SuperPlayerConfigArgs()
        {
        }
    }

    public sealed class SuperPlayerConfigState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the unencrypted adaptive bitrate streaming template that allows output, which is required if `drm_switch` is `false`.
        /// </summary>
        [Input("adaptiveDynamicStreamingDefinition")]
        public Input<string>? AdaptiveDynamicStreamingDefinition { get; set; }

        /// <summary>
        /// Template description. Length limit: 256 characters.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Creation time of template in ISO date format.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// Domain name used for playback. If it is left empty or set to `Default`, the domain name configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. `Default` by default.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// Content of the DRM-protected adaptive bitrate streaming template that allows output, which is required if `drm_switch` is `true`.
        /// </summary>
        [Input("drmStreamingInfo")]
        public Input<Inputs.SuperPlayerConfigDrmStreamingInfoGetArgs>? DrmStreamingInfo { get; set; }

        /// <summary>
        /// Switch of DRM-protected adaptive bitstream playback: `true`: enabled, indicating to play back only output adaptive bitstreams protected by DRM; `false`: disabled, indicating to play back unencrypted output adaptive bitstreams. Default value: `false`.
        /// </summary>
        [Input("drmSwitch")]
        public Input<bool>? DrmSwitch { get; set; }

        /// <summary>
        /// ID of the image sprite template that allows output.
        /// </summary>
        [Input("imageSpriteDefinition")]
        public Input<string>? ImageSpriteDefinition { get; set; }

        /// <summary>
        /// Player configuration name, which can contain up to 64 letters, digits, underscores, and hyphens (such as test_ABC-123) and must be unique under a user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resolutionNames")]
        private InputList<Inputs.SuperPlayerConfigResolutionNameGetArgs>? _resolutionNames;

        /// <summary>
        /// Display name of player for substreams with different resolutions. If this parameter is left empty or an empty array, the default configuration will be used: `min_edge_length: 240, name: LD`; `min_edge_length: 480, name: SD`; `min_edge_length: 720, name: HD`; `min_edge_length: 1080, name: FHD`; `min_edge_length: 1440, name: 2K`; `min_edge_length: 2160, name: 4K`; `min_edge_length: 4320, name: 8K`.
        /// </summary>
        public InputList<Inputs.SuperPlayerConfigResolutionNameGetArgs> ResolutionNames
        {
            get => _resolutionNames ?? (_resolutionNames = new InputList<Inputs.SuperPlayerConfigResolutionNameGetArgs>());
            set => _resolutionNames = value;
        }

        /// <summary>
        /// Scheme used for playback. If it is left empty or set to `Default`, the scheme configured in [Default Distribution Configuration](https://cloud.tencent.com/document/product/266/33373) will be used. Other valid values: `HTTP`; `HTTPS`.
        /// </summary>
        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        /// <summary>
        /// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
        /// </summary>
        [Input("subAppId")]
        public Input<int>? SubAppId { get; set; }

        /// <summary>
        /// Last modified time of template in ISO date format.
        /// </summary>
        [Input("updateTime")]
        public Input<string>? UpdateTime { get; set; }

        public SuperPlayerConfigState()
        {
        }
    }
}
