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
    public sealed class GetProcedureTemplatesTemplateListMediaProcessTaskSnapshotByTimeOffsetTaskListResult
    {
        /// <summary>
        /// Video transcoding template ID.
        /// </summary>
        public readonly string Definition;
        /// <summary>
        /// The list of screenshot time points. `s` and `%` formats are supported: When a time point string ends with `s`, its unit is second. For example, `3.5s` means the 3.5th second of the video; When a time point string ends with `%`, it is marked with corresponding percentage of the video duration. For example, `10%` means that the time point is at the 10% of the video entire duration.
        /// </summary>
        public readonly ImmutableArray<string> ExtTimeOffsetLists;
        /// <summary>
        /// List of up to `10` image or text watermarks. Note: this field may return null, indicating that no valid values can be obtained.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProcedureTemplatesTemplateListMediaProcessTaskSnapshotByTimeOffsetTaskListWatermarkListResult> WatermarkLists;

        [OutputConstructor]
        private GetProcedureTemplatesTemplateListMediaProcessTaskSnapshotByTimeOffsetTaskListResult(
            string definition,

            ImmutableArray<string> extTimeOffsetLists,

            ImmutableArray<Outputs.GetProcedureTemplatesTemplateListMediaProcessTaskSnapshotByTimeOffsetTaskListWatermarkListResult> watermarkLists)
        {
            Definition = definition;
            ExtTimeOffsetLists = extTimeOffsetLists;
            WatermarkLists = watermarkLists;
        }
    }
}
