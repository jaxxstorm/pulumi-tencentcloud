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
    public sealed class CcPolicyV2CcPrecisionReqLimit
    {
        /// <summary>
        /// Domain.
        /// </summary>
        public readonly string Domain;
        public readonly string? InstanceId;
        /// <summary>
        /// Ip address.
        /// </summary>
        public readonly string? Ip;
        /// <summary>
        /// Protection rating, the optional value of default means default policy, loose means loose, and strict means strict.
        /// </summary>
        public readonly string Level;
        /// <summary>
        /// The CC Frequency Limit Policy Item field.
        /// </summary>
        public readonly ImmutableArray<Outputs.CcPolicyV2CcPrecisionReqLimitPolicy> Policys;
        /// <summary>
        /// Protocol, preferably HTTP, HTTPS.
        /// </summary>
        public readonly string Protocol;

        [OutputConstructor]
        private CcPolicyV2CcPrecisionReqLimit(
            string domain,

            string? instanceId,

            string? ip,

            string level,

            ImmutableArray<Outputs.CcPolicyV2CcPrecisionReqLimitPolicy> policys,

            string protocol)
        {
            Domain = domain;
            InstanceId = instanceId;
            Ip = ip;
            Level = level;
            Policys = policys;
            Protocol = protocol;
        }
    }
}
