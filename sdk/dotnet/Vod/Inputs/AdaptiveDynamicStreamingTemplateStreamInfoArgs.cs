// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Vod.Inputs
{

    public sealed class AdaptiveDynamicStreamingTemplateStreamInfoArgs : Pulumi.ResourceArgs
    {
        [Input("audio", required: true)]
        public Input<Inputs.AdaptiveDynamicStreamingTemplateStreamInfoAudioArgs> Audio { get; set; } = null!;

        [Input("removeAudio")]
        public Input<bool>? RemoveAudio { get; set; }

        [Input("video", required: true)]
        public Input<Inputs.AdaptiveDynamicStreamingTemplateStreamInfoVideoArgs> Video { get; set; } = null!;

        public AdaptiveDynamicStreamingTemplateStreamInfoArgs()
        {
        }
    }
}
