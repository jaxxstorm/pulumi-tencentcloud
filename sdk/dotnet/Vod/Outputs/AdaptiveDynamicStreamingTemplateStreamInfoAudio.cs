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
    public sealed class AdaptiveDynamicStreamingTemplateStreamInfoAudio
    {
        public readonly string? AudioChannel;
        public readonly int Bitrate;
        public readonly string Codec;
        public readonly int SampleRate;

        [OutputConstructor]
        private AdaptiveDynamicStreamingTemplateStreamInfoAudio(
            string? audioChannel,

            int bitrate,

            string codec,

            int sampleRate)
        {
            AudioChannel = audioChannel;
            Bitrate = bitrate;
            Codec = codec;
            SampleRate = sampleRate;
        }
    }
}
