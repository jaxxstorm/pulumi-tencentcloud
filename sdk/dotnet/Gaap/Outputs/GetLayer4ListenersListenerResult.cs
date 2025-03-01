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
    public sealed class GetLayer4ListenersListenerResult
    {
        /// <summary>
        /// Timeout of the health check response.
        /// </summary>
        public readonly int ConnectTimeout;
        /// <summary>
        /// Creation time of the layer4 listener.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Indicates whether health check is enable.
        /// </summary>
        public readonly bool HealthCheck;
        /// <summary>
        /// ID of the layer4 listener.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Interval of the health check.
        /// </summary>
        public readonly int Interval;
        /// <summary>
        /// Name of the layer4 listener.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Port of the layer4 listener to be queried.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// Protocol of the layer4 listener to be queried. Valid values: `TCP` and `UDP`.
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// Type of the realserver.
        /// </summary>
        public readonly string RealserverType;
        /// <summary>
        /// Scheduling policy of the layer4 listener.
        /// </summary>
        public readonly string Scheduler;
        /// <summary>
        /// Status of the layer4 listener.
        /// </summary>
        public readonly int Status;

        [OutputConstructor]
        private GetLayer4ListenersListenerResult(
            int connectTimeout,

            string createTime,

            bool healthCheck,

            string id,

            int interval,

            string name,

            int port,

            string protocol,

            string realserverType,

            string scheduler,

            int status)
        {
            ConnectTimeout = connectTimeout;
            CreateTime = createTime;
            HealthCheck = healthCheck;
            Id = id;
            Interval = interval;
            Name = name;
            Port = port;
            Protocol = protocol;
            RealserverType = realserverType;
            Scheduler = scheduler;
            Status = status;
        }
    }
}
