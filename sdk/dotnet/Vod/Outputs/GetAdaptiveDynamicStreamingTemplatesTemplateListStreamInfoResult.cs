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
    public sealed class GetAdaptiveDynamicStreamingTemplatesTemplateListStreamInfoResult
    {
        /// <summary>
        /// Audio parameter information.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetAdaptiveDynamicStreamingTemplatesTemplateListStreamInfoAudioResult> Audios;
        /// <summary>
        /// Whether to remove audio stream. `false`: no, `true`: yes.
        /// </summary>
        public readonly bool RemoveAudio;
        /// <summary>
        /// Video parameter information.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetAdaptiveDynamicStreamingTemplatesTemplateListStreamInfoVideoResult> Videos;

        [OutputConstructor]
        private GetAdaptiveDynamicStreamingTemplatesTemplateListStreamInfoResult(
            ImmutableArray<Outputs.GetAdaptiveDynamicStreamingTemplatesTemplateListStreamInfoAudioResult> audios,

            bool removeAudio,

            ImmutableArray<Outputs.GetAdaptiveDynamicStreamingTemplatesTemplateListStreamInfoVideoResult> videos)
        {
            Audios = audios;
            RemoveAudio = removeAudio;
            Videos = videos;
        }
    }
}
