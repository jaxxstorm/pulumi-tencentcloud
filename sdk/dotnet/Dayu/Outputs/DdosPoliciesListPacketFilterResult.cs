// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Dayu.Outputs
{

    [OutputType]
    public sealed class DdosPoliciesListPacketFilterResult
    {
        public readonly string Action;
        public readonly int DEndPort;
        public readonly int DStartPort;
        public readonly int Depth;
        public readonly bool IsInclude;
        public readonly string MatchBegin;
        public readonly string MatchStr;
        public readonly string MatchType;
        public readonly int Offset;
        public readonly int PktLengthMax;
        public readonly int PktLengthMin;
        public readonly string Protocol;
        public readonly int SEndPort;
        public readonly int SStartPort;

        [OutputConstructor]
        private DdosPoliciesListPacketFilterResult(
            string action,

            int dEndPort,

            int dStartPort,

            int depth,

            bool isInclude,

            string matchBegin,

            string matchStr,

            string matchType,

            int offset,

            int pktLengthMax,

            int pktLengthMin,

            string protocol,

            int sEndPort,

            int sStartPort)
        {
            Action = action;
            DEndPort = dEndPort;
            DStartPort = dStartPort;
            Depth = depth;
            IsInclude = isInclude;
            MatchBegin = matchBegin;
            MatchStr = matchStr;
            MatchType = matchType;
            Offset = offset;
            PktLengthMax = pktLengthMax;
            PktLengthMin = pktLengthMin;
            Protocol = protocol;
            SEndPort = sEndPort;
            SStartPort = sStartPort;
        }
    }
}
