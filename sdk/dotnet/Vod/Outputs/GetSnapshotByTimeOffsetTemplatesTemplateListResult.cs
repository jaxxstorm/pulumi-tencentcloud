// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Vod.Outputs
{

    [OutputType]
    public sealed class GetSnapshotByTimeOffsetTemplatesTemplateListResult
    {
        /// <summary>
        /// Template description.
        /// </summary>
        public readonly string Comment;
        /// <summary>
        /// Creation time of template in ISO date format.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Unique ID filter of snapshot by time offset template.
        /// </summary>
        public readonly string Definition;
        /// <summary>
        /// Fill refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported: `stretch`: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot `shorter` or `longer`; `black`: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks. `white`: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks. `gauss`: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.
        /// </summary>
        public readonly string FillType;
        /// <summary>
        /// Image format. Valid values: `jpg`, `png`.
        /// </summary>
        public readonly string Format;
        /// <summary>
        /// Maximum value of the `height` (or short side) of a screenshot in px. Value range: 0 and [128, 4,096]. If both `width` and `height` are `0`, the resolution will be the same as that of the source video; If `width` is `0`, but `height` is not `0`, `width` will be proportionally scaled; If `width` is not `0`, but `height` is `0`, `height` will be proportionally scaled; If both `width` and `height` are not `0`, the custom resolution will be used.
        /// </summary>
        public readonly int Height;
        /// <summary>
        /// Name of a time point screen capturing template.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Resolution adaption. Valid values: `true`, `false`. `true`: enabled. In this case, `width` represents the long side of a video, while `height` the short side; `false`: disabled. In this case, `width` represents the width of a video, while `height` the height.
        /// </summary>
        public readonly bool ResolutionAdaptive;
        /// <summary>
        /// Template type filter. Valid values: `Preset`, `Custom`. `Preset`: preset template; `Custom`: custom template.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// Last modified time of template in ISO date format.
        /// </summary>
        public readonly string UpdateTime;
        /// <summary>
        /// Maximum value of the `width` (or long side) of a screenshot in px. Value range: 0 and [128, 4,096]. If both `width` and `height` are `0`, the resolution will be the same as that of the source video; If `width` is `0`, but `height` is not `0`, width will be proportionally scaled; If `width` is not `0`, but `height` is `0`, `height` will be proportionally scaled; If both `width` and `height` are not `0`, the custom resolution will be used.
        /// </summary>
        public readonly int Width;

        [OutputConstructor]
        private GetSnapshotByTimeOffsetTemplatesTemplateListResult(
            string comment,

            string createTime,

            string definition,

            string fillType,

            string format,

            int height,

            string name,

            bool resolutionAdaptive,

            string type,

            string updateTime,

            int width)
        {
            Comment = comment;
            CreateTime = createTime;
            Definition = definition;
            FillType = fillType;
            Format = format;
            Height = height;
            Name = name;
            ResolutionAdaptive = resolutionAdaptive;
            Type = type;
            UpdateTime = updateTime;
            Width = width;
        }
    }
}
