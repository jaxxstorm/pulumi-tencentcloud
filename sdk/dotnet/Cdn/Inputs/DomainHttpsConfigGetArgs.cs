// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Inputs
{

    public sealed class DomainHttpsConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Client certificate configuration information.
        /// </summary>
        [Input("clientCertificateConfig")]
        public Input<Inputs.DomainHttpsConfigClientCertificateConfigGetArgs>? ClientCertificateConfig { get; set; }

        /// <summary>
        /// Configuration of forced HTTP or HTTPS redirects.
        /// </summary>
        [Input("forceRedirect")]
        public Input<Inputs.DomainHttpsConfigForceRedirectGetArgs>? ForceRedirect { get; set; }

        /// <summary>
        /// HTTP2 configuration switch. Valid values are `on` and `off`. and default value is `off`.
        /// </summary>
        [Input("http2Switch")]
        public Input<string>? Http2Switch { get; set; }

        /// <summary>
        /// HTTPS configuration switch. Valid values are `on` and `off`.
        /// </summary>
        [Input("httpsSwitch", required: true)]
        public Input<string> HttpsSwitch { get; set; } = null!;

        /// <summary>
        /// OCSP configuration switch. Valid values are `on` and `off`. and default value is `off`.
        /// </summary>
        [Input("ocspStaplingSwitch")]
        public Input<string>? OcspStaplingSwitch { get; set; }

        /// <summary>
        /// Server certificate configuration information.
        /// </summary>
        [Input("serverCertificateConfig")]
        public Input<Inputs.DomainHttpsConfigServerCertificateConfigGetArgs>? ServerCertificateConfig { get; set; }

        /// <summary>
        /// Spdy configuration switch. Valid values are `on` and `off`. and default value is `off`. This parameter is for white-list customer.
        /// </summary>
        [Input("spdySwitch")]
        public Input<string>? SpdySwitch { get; set; }

        /// <summary>
        /// Client certificate authentication feature. Valid values are `on` and `off`. and default value is `off`.
        /// </summary>
        [Input("verifyClient")]
        public Input<string>? VerifyClient { get; set; }

        public DomainHttpsConfigGetArgs()
        {
        }
    }
}
