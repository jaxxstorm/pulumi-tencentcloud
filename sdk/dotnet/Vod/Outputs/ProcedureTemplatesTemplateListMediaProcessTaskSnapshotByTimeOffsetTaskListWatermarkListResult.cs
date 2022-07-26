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
    public sealed class ProcedureTemplatesTemplateListMediaProcessTaskSnapshotByTimeOffsetTaskListWatermarkListResult
    {
        public readonly string Definition;
        public readonly double? EndTimeOffset;
        public readonly double? StartTimeOffset;
        public readonly string? SvgContent;
        public readonly string? TextContent;

        [OutputConstructor]
        private ProcedureTemplatesTemplateListMediaProcessTaskSnapshotByTimeOffsetTaskListWatermarkListResult(
            string definition,

            double? endTimeOffset,

            double? startTimeOffset,

            string? svgContent,

            string? textContent)
        {
            Definition = definition;
            EndTimeOffset = endTimeOffset;
            StartTimeOffset = startTimeOffset;
            SvgContent = svgContent;
            TextContent = textContent;
        }
    }
}
