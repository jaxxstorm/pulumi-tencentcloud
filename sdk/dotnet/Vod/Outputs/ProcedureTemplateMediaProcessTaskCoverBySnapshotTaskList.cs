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
    public sealed class ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskList
    {
        /// <summary>
        /// Time point screen capturing template ID.
        /// </summary>
        public readonly string Definition;
        /// <summary>
        /// Screen capturing mode. Valid values: `Time`, `Percent`. `Time`: screen captures by time point, `Percent`: screen captures by percentage.
        /// </summary>
        public readonly string PositionType;
        /// <summary>
        /// Screenshot position: For time point screen capturing, this means to take a screenshot at a specified time point (in seconds) and use it as the cover. For percentage screen capturing, this value means to take a screenshot at a specified percentage of the video duration and use it as the cover.
        /// </summary>
        public readonly double PositionValue;
        /// <summary>
        /// List of up to `10` image or text watermarks. Note: this field may return null, indicating that no valid values can be obtained.
        /// </summary>
        public readonly ImmutableArray<Outputs.ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskListWatermarkList> WatermarkLists;

        [OutputConstructor]
        private ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskList(
            string definition,

            string positionType,

            double positionValue,

            ImmutableArray<Outputs.ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskListWatermarkList> watermarkLists)
        {
            Definition = definition;
            PositionType = positionType;
            PositionValue = positionValue;
            WatermarkLists = watermarkLists;
        }
    }
}
