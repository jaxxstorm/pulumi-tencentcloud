// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Gaap.Outputs
{

    [OutputType]
    public sealed class GetProxiesProxyResult
    {
        /// <summary>
        /// Access region of the GAAP proxy to be queried. Conflict with `ids`.
        /// </summary>
        public readonly string AccessRegion;
        /// <summary>
        /// Maximum bandwidth of the GAAP proxy, unit is Mbps.
        /// </summary>
        public readonly int Bandwidth;
        /// <summary>
        /// Maximum concurrency of the GAAP proxy, unit is 10k.
        /// </summary>
        public readonly int Concurrent;
        /// <summary>
        /// Creation time of the GAAP proxy.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Access domain of the GAAP proxy.
        /// </summary>
        public readonly string Domain;
        /// <summary>
        /// Forwarding IP of the GAAP proxy.
        /// </summary>
        public readonly string ForwardIp;
        /// <summary>
        /// ID of the GAAP proxy.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Access domain of the GAAP proxy.
        /// </summary>
        public readonly string Ip;
        /// <summary>
        /// Name of the GAAP proxy.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Security policy ID of the GAAP proxy.
        /// </summary>
        public readonly string PolicyId;
        /// <summary>
        /// Project ID of the GAAP proxy to be queried. Conflict with `ids`.
        /// </summary>
        public readonly int ProjectId;
        /// <summary>
        /// Region of the GAAP realserver to be queried. Conflict with `ids`.
        /// </summary>
        public readonly string RealserverRegion;
        /// <summary>
        /// Indicates whether GAAP proxy can scalable.
        /// </summary>
        public readonly bool Scalable;
        /// <summary>
        /// Status of the GAAP proxy.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Supported protocols of the GAAP proxy.
        /// </summary>
        public readonly ImmutableArray<string> SupportProtocols;
        /// <summary>
        /// Tags of the GAAP proxy to be queried. Support up to 5, display the information as long as it matches one.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Tags;
        /// <summary>
        /// Version of the GAAP proxy.
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetProxiesProxyResult(
            string accessRegion,

            int bandwidth,

            int concurrent,

            string createTime,

            string domain,

            string forwardIp,

            string id,

            string ip,

            string name,

            string policyId,

            int projectId,

            string realserverRegion,

            bool scalable,

            string status,

            ImmutableArray<string> supportProtocols,

            ImmutableDictionary<string, object> tags,

            string version)
        {
            AccessRegion = accessRegion;
            Bandwidth = bandwidth;
            Concurrent = concurrent;
            CreateTime = createTime;
            Domain = domain;
            ForwardIp = forwardIp;
            Id = id;
            Ip = ip;
            Name = name;
            PolicyId = policyId;
            ProjectId = projectId;
            RealserverRegion = realserverRegion;
            Scalable = scalable;
            Status = status;
            SupportProtocols = supportProtocols;
            Tags = tags;
            Version = version;
        }
    }
}
