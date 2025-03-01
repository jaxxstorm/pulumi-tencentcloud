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
    public sealed class DdosPolicyV2DdosConnectLimit
    {
        /// <summary>
        /// Based on connection suppression trigger threshold, value range [0,4294967295].
        /// </summary>
        public readonly int BadConnThreshold;
        /// <summary>
        /// Abnormal connection detection condition, connection timeout, value range [0,65535].
        /// </summary>
        public readonly int ConnTimeout;
        /// <summary>
        /// Concurrent connection control based on destination IP+ destination port.
        /// </summary>
        public readonly int DstConnLimit;
        /// <summary>
        /// Limit on the number of news per second based on the destination IP.
        /// </summary>
        public readonly int DstNewLimit;
        /// <summary>
        /// Abnormal connection detection conditions, empty connection guard switch, value range[0,1].
        /// </summary>
        public readonly int NullConnEnable;
        /// <summary>
        /// Concurrent connection control based on source IP + destination IP.
        /// </summary>
        public readonly int SdConnLimit;
        /// <summary>
        /// The limit on the number of news per second based on source IP + destination IP.
        /// </summary>
        public readonly int SdNewLimit;
        /// <summary>
        /// Anomaly connection detection condition, syn threshold, value range [0,100].
        /// </summary>
        public readonly int SynLimit;
        /// <summary>
        /// Anomalous connection detection condition, percentage of syn ack, value range [0,100].
        /// </summary>
        public readonly int SynRate;

        [OutputConstructor]
        private DdosPolicyV2DdosConnectLimit(
            int badConnThreshold,

            int connTimeout,

            int dstConnLimit,

            int dstNewLimit,

            int nullConnEnable,

            int sdConnLimit,

            int sdNewLimit,

            int synLimit,

            int synRate)
        {
            BadConnThreshold = badConnThreshold;
            ConnTimeout = connTimeout;
            DstConnLimit = dstConnLimit;
            DstNewLimit = dstNewLimit;
            NullConnEnable = nullConnEnable;
            SdConnLimit = sdConnLimit;
            SdNewLimit = sdNewLimit;
            SynLimit = synLimit;
            SynRate = synRate;
        }
    }
}
