// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Postgresql.Outputs
{

    [OutputType]
    public sealed class XlogsListResult
    {
        public readonly string EndTime;
        public readonly string ExternalAddr;
        public readonly int Id;
        public readonly string InternalAddr;
        public readonly int Size;
        public readonly string StartTime;

        [OutputConstructor]
        private XlogsListResult(
            string endTime,

            string externalAddr,

            int id,

            string internalAddr,

            int size,

            string startTime)
        {
            EndTime = endTime;
            ExternalAddr = externalAddr;
            Id = id;
            InternalAddr = internalAddr;
            Size = size;
            StartTime = startTime;
        }
    }
}
