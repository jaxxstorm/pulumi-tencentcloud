// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Ssl
{
    [TencentcloudResourceType("tencentcloud:Ssl/instance:Instance")]
    public partial class Instance : Pulumi.CustomResource
    {
        /// <summary>
        /// Remark name.
        /// </summary>
        [Output("alias")]
        public Output<string> Alias { get; private set; } = null!;

        /// <summary>
        /// Returned certificate ID.
        /// </summary>
        [Output("certificateId")]
        public Output<string> CertificateId { get; private set; } = null!;

        /// <summary>
        /// Number of domain names included in the certificate.
        /// </summary>
        [Output("domainNum")]
        public Output<int> DomainNum { get; private set; } = null!;

        /// <summary>
        /// Certificate information.
        /// </summary>
        [Output("information")]
        public Output<Outputs.InstanceInformation> Information { get; private set; } = null!;

        /// <summary>
        /// Order ID returned.
        /// </summary>
        [Output("orderId")]
        public Output<string> OrderId { get; private set; } = null!;

        /// <summary>
        /// Certificate commodity ID. Valid value ranges: (3~42). `3` means SecureSite Enhanced Enterprise Edition (EV Pro), `4`
        /// means SecureSite Enhanced (EV), `5` means SecureSite Enterprise Professional Edition (OV Pro), `6` means SecureSite
        /// Enterprise (OV), `7` means SecureSite Enterprise Type (OV) wildcard, `8` means Geotrust enhanced (EV), `9` means
        /// Geotrust enterprise (OV), `10` means Geotrust enterprise (OV) wildcard, `11` means TrustAsia domain type multi-domain
        /// SSL certificate, `12` means TrustAsia domain type ( DV) wildcard, `13` means TrustAsia enterprise wildcard (OV) SSL
        /// certificate (D3), `14` means TrustAsia enterprise (OV) SSL certificate (D3), `15` means TrustAsia enterprise
        /// multi-domain (OV) SSL certificate (D3), `16` means TrustAsia Enhanced (EV) SSL Certificate (D3), `17` means TrustAsia
        /// Enhanced Multiple Domain (EV) SSL Certificate (D3), `18` means GlobalSign Enterprise (OV) SSL Certificate, `19` means
        /// GlobalSign Enterprise Wildcard (OV) SSL Certificate, `20` means GlobalSign Enhanced (EV) SSL Certificate, `21` means
        /// TrustAsia Enterprise Wildcard Multiple Domain (OV) SSL Certificate (D3), `22` means GlobalSign Enterprise Multiple
        /// Domain (OV) SSL Certificate, `23` means GlobalSign Enterprise Multiple Wildcard Domain name (OV) SSL certificate, `24`
        /// means GlobalSign enhanced multi-domain (EV) SSL certificate, `25` means Wotrus domain type certificate, `26` means
        /// Wotrus domain type multi-domain certificate, `27` means Wotrus domain type wildcard certificate, `28` means Wotrus
        /// enterprise type certificate, `29` means Wotrus enterprise multi-domain certificate, `30` means Wotrus enterprise
        /// wildcard certificate, `31` means Wotrus enhanced certificate, `32` means Wotrus enhanced multi-domain certificate, `33`
        /// means DNSPod national secret domain name certificate, `34` means DNSPod national secret domain name certificate
        /// Multi-domain certificate, `35` means DNSPod national secret domain name wildcard certificate, `37` means DNSPod national
        /// secret enterprise certificate, `38` means DNSPod national secret enterprise multi-domain certificate, `39` means DNSPod
        /// national secret enterprise wildcard certificate, `40` means DNSPod national secret increase Strong certificate, `41`
        /// means DNSPod national secret enhanced multi-domain certificate, `42` means TrustAsia domain-type wildcard multi-domain
        /// certificate.
        /// </summary>
        [Output("productId")]
        public Output<int> ProductId { get; private set; } = null!;

        /// <summary>
        /// The ID of project.
        /// </summary>
        [Output("projectId")]
        public Output<int> ProjectId { get; private set; } = null!;

        /// <summary>
        /// SSL certificate status.
        /// </summary>
        [Output("status")]
        public Output<int> Status { get; private set; } = null!;

        /// <summary>
        /// Certificate period, currently only supports 1 year certificate purchase.
        /// </summary>
        [Output("timeSpan")]
        public Output<int?> TimeSpan { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Ssl/instance:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Ssl/instance:Instance", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, state, options);
        }
    }

    public sealed class InstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Remark name.
        /// </summary>
        [Input("alias")]
        public Input<string>? Alias { get; set; }

        /// <summary>
        /// Number of domain names included in the certificate.
        /// </summary>
        [Input("domainNum", required: true)]
        public Input<int> DomainNum { get; set; } = null!;

        /// <summary>
        /// Certificate information.
        /// </summary>
        [Input("information", required: true)]
        public Input<Inputs.InstanceInformationArgs> Information { get; set; } = null!;

        /// <summary>
        /// Certificate commodity ID. Valid value ranges: (3~42). `3` means SecureSite Enhanced Enterprise Edition (EV Pro), `4`
        /// means SecureSite Enhanced (EV), `5` means SecureSite Enterprise Professional Edition (OV Pro), `6` means SecureSite
        /// Enterprise (OV), `7` means SecureSite Enterprise Type (OV) wildcard, `8` means Geotrust enhanced (EV), `9` means
        /// Geotrust enterprise (OV), `10` means Geotrust enterprise (OV) wildcard, `11` means TrustAsia domain type multi-domain
        /// SSL certificate, `12` means TrustAsia domain type ( DV) wildcard, `13` means TrustAsia enterprise wildcard (OV) SSL
        /// certificate (D3), `14` means TrustAsia enterprise (OV) SSL certificate (D3), `15` means TrustAsia enterprise
        /// multi-domain (OV) SSL certificate (D3), `16` means TrustAsia Enhanced (EV) SSL Certificate (D3), `17` means TrustAsia
        /// Enhanced Multiple Domain (EV) SSL Certificate (D3), `18` means GlobalSign Enterprise (OV) SSL Certificate, `19` means
        /// GlobalSign Enterprise Wildcard (OV) SSL Certificate, `20` means GlobalSign Enhanced (EV) SSL Certificate, `21` means
        /// TrustAsia Enterprise Wildcard Multiple Domain (OV) SSL Certificate (D3), `22` means GlobalSign Enterprise Multiple
        /// Domain (OV) SSL Certificate, `23` means GlobalSign Enterprise Multiple Wildcard Domain name (OV) SSL certificate, `24`
        /// means GlobalSign enhanced multi-domain (EV) SSL certificate, `25` means Wotrus domain type certificate, `26` means
        /// Wotrus domain type multi-domain certificate, `27` means Wotrus domain type wildcard certificate, `28` means Wotrus
        /// enterprise type certificate, `29` means Wotrus enterprise multi-domain certificate, `30` means Wotrus enterprise
        /// wildcard certificate, `31` means Wotrus enhanced certificate, `32` means Wotrus enhanced multi-domain certificate, `33`
        /// means DNSPod national secret domain name certificate, `34` means DNSPod national secret domain name certificate
        /// Multi-domain certificate, `35` means DNSPod national secret domain name wildcard certificate, `37` means DNSPod national
        /// secret enterprise certificate, `38` means DNSPod national secret enterprise multi-domain certificate, `39` means DNSPod
        /// national secret enterprise wildcard certificate, `40` means DNSPod national secret increase Strong certificate, `41`
        /// means DNSPod national secret enhanced multi-domain certificate, `42` means TrustAsia domain-type wildcard multi-domain
        /// certificate.
        /// </summary>
        [Input("productId", required: true)]
        public Input<int> ProductId { get; set; } = null!;

        /// <summary>
        /// The ID of project.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// Certificate period, currently only supports 1 year certificate purchase.
        /// </summary>
        [Input("timeSpan")]
        public Input<int>? TimeSpan { get; set; }

        public InstanceArgs()
        {
        }
    }

    public sealed class InstanceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Remark name.
        /// </summary>
        [Input("alias")]
        public Input<string>? Alias { get; set; }

        /// <summary>
        /// Returned certificate ID.
        /// </summary>
        [Input("certificateId")]
        public Input<string>? CertificateId { get; set; }

        /// <summary>
        /// Number of domain names included in the certificate.
        /// </summary>
        [Input("domainNum")]
        public Input<int>? DomainNum { get; set; }

        /// <summary>
        /// Certificate information.
        /// </summary>
        [Input("information")]
        public Input<Inputs.InstanceInformationGetArgs>? Information { get; set; }

        /// <summary>
        /// Order ID returned.
        /// </summary>
        [Input("orderId")]
        public Input<string>? OrderId { get; set; }

        /// <summary>
        /// Certificate commodity ID. Valid value ranges: (3~42). `3` means SecureSite Enhanced Enterprise Edition (EV Pro), `4`
        /// means SecureSite Enhanced (EV), `5` means SecureSite Enterprise Professional Edition (OV Pro), `6` means SecureSite
        /// Enterprise (OV), `7` means SecureSite Enterprise Type (OV) wildcard, `8` means Geotrust enhanced (EV), `9` means
        /// Geotrust enterprise (OV), `10` means Geotrust enterprise (OV) wildcard, `11` means TrustAsia domain type multi-domain
        /// SSL certificate, `12` means TrustAsia domain type ( DV) wildcard, `13` means TrustAsia enterprise wildcard (OV) SSL
        /// certificate (D3), `14` means TrustAsia enterprise (OV) SSL certificate (D3), `15` means TrustAsia enterprise
        /// multi-domain (OV) SSL certificate (D3), `16` means TrustAsia Enhanced (EV) SSL Certificate (D3), `17` means TrustAsia
        /// Enhanced Multiple Domain (EV) SSL Certificate (D3), `18` means GlobalSign Enterprise (OV) SSL Certificate, `19` means
        /// GlobalSign Enterprise Wildcard (OV) SSL Certificate, `20` means GlobalSign Enhanced (EV) SSL Certificate, `21` means
        /// TrustAsia Enterprise Wildcard Multiple Domain (OV) SSL Certificate (D3), `22` means GlobalSign Enterprise Multiple
        /// Domain (OV) SSL Certificate, `23` means GlobalSign Enterprise Multiple Wildcard Domain name (OV) SSL certificate, `24`
        /// means GlobalSign enhanced multi-domain (EV) SSL certificate, `25` means Wotrus domain type certificate, `26` means
        /// Wotrus domain type multi-domain certificate, `27` means Wotrus domain type wildcard certificate, `28` means Wotrus
        /// enterprise type certificate, `29` means Wotrus enterprise multi-domain certificate, `30` means Wotrus enterprise
        /// wildcard certificate, `31` means Wotrus enhanced certificate, `32` means Wotrus enhanced multi-domain certificate, `33`
        /// means DNSPod national secret domain name certificate, `34` means DNSPod national secret domain name certificate
        /// Multi-domain certificate, `35` means DNSPod national secret domain name wildcard certificate, `37` means DNSPod national
        /// secret enterprise certificate, `38` means DNSPod national secret enterprise multi-domain certificate, `39` means DNSPod
        /// national secret enterprise wildcard certificate, `40` means DNSPod national secret increase Strong certificate, `41`
        /// means DNSPod national secret enhanced multi-domain certificate, `42` means TrustAsia domain-type wildcard multi-domain
        /// certificate.
        /// </summary>
        [Input("productId")]
        public Input<int>? ProductId { get; set; }

        /// <summary>
        /// The ID of project.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// SSL certificate status.
        /// </summary>
        [Input("status")]
        public Input<int>? Status { get; set; }

        /// <summary>
        /// Certificate period, currently only supports 1 year certificate purchase.
        /// </summary>
        [Input("timeSpan")]
        public Input<int>? TimeSpan { get; set; }

        public InstanceState()
        {
        }
    }
}
