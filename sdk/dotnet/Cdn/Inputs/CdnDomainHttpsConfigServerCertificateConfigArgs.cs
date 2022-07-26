// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Inputs
{

    public sealed class CdnDomainHttpsConfigServerCertificateConfigArgs : Pulumi.ResourceArgs
    {
        [Input("certificateContent")]
        public Input<string>? CertificateContent { get; set; }

        [Input("certificateId")]
        public Input<string>? CertificateId { get; set; }

        [Input("certificateName")]
        public Input<string>? CertificateName { get; set; }

        [Input("deployTime")]
        public Input<string>? DeployTime { get; set; }

        [Input("expireTime")]
        public Input<string>? ExpireTime { get; set; }

        [Input("message")]
        public Input<string>? Message { get; set; }

        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        public CdnDomainHttpsConfigServerCertificateConfigArgs()
        {
        }
    }
}
