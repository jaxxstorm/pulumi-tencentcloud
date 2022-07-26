// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Vod.Inputs
{

    public sealed class ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskListGetArgs : Pulumi.ResourceArgs
    {
        [Input("definition", required: true)]
        public Input<string> Definition { get; set; } = null!;

        [Input("positionType", required: true)]
        public Input<string> PositionType { get; set; } = null!;

        [Input("positionValue", required: true)]
        public Input<double> PositionValue { get; set; } = null!;

        [Input("watermarkLists")]
        private InputList<Inputs.ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskListWatermarkListGetArgs>? _watermarkLists;
        public InputList<Inputs.ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskListWatermarkListGetArgs> WatermarkLists
        {
            get => _watermarkLists ?? (_watermarkLists = new InputList<Inputs.ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskListWatermarkListGetArgs>());
            set => _watermarkLists = value;
        }

        public ProcedureTemplateMediaProcessTaskCoverBySnapshotTaskListGetArgs()
        {
        }
    }
}
