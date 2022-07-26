// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Gaap
{
    [TencentcloudResourceType("tencentcloud:Gaap/layer7Listener:Layer7Listener")]
    public partial class Layer7Listener : Pulumi.CustomResource
    {
        /// <summary>
        /// Authentication type of the layer7 listener. `0` is one-way authentication and `1` is mutual authentication. NOTES: Only
        /// supports listeners of `HTTPS` protocol.
        /// </summary>
        [Output("authType")]
        public Output<int?> AuthType { get; private set; } = null!;

        /// <summary>
        /// Certificate ID of the layer7 listener. NOTES: Only supports listeners of `HTTPS` protocol.
        /// </summary>
        [Output("certificateId")]
        public Output<string?> CertificateId { get; private set; } = null!;

        /// <summary>
        /// ID of the client certificate. Set only when `auth_type` is specified as mutual authentication. NOTES: Only supports
        /// listeners of `HTTPS` protocol.
        /// </summary>
        [Output("clientCertificateId")]
        public Output<string> ClientCertificateId { get; private set; } = null!;

        /// <summary>
        /// ID list of the client certificate. Set only when `auth_type` is specified as mutual authentication. NOTES: Only supports
        /// listeners of `HTTPS` protocol.
        /// </summary>
        [Output("clientCertificateIds")]
        public Output<ImmutableArray<string>> ClientCertificateIds { get; private set; } = null!;

        /// <summary>
        /// Creation time of the layer7 listener.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Protocol type of the forwarding. Valid value: `HTTP` and `HTTPS`. NOTES: Only supports listeners of `HTTPS` protocol.
        /// </summary>
        [Output("forwardProtocol")]
        public Output<string?> ForwardProtocol { get; private set; } = null!;

        /// <summary>
        /// Name of the layer7 listener, the maximum length is 30.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Port of the layer7 listener.
        /// </summary>
        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// Protocol of the layer7 listener. Valid value: `HTTP` and `HTTPS`.
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// ID of the GAAP proxy.
        /// </summary>
        [Output("proxyId")]
        public Output<string> ProxyId { get; private set; } = null!;

        /// <summary>
        /// Status of the layer7 listener.
        /// </summary>
        [Output("status")]
        public Output<int> Status { get; private set; } = null!;


        /// <summary>
        /// Create a Layer7Listener resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Layer7Listener(string name, Layer7ListenerArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Gaap/layer7Listener:Layer7Listener", name, args ?? new Layer7ListenerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Layer7Listener(string name, Input<string> id, Layer7ListenerState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Gaap/layer7Listener:Layer7Listener", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Layer7Listener resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Layer7Listener Get(string name, Input<string> id, Layer7ListenerState? state = null, CustomResourceOptions? options = null)
        {
            return new Layer7Listener(name, id, state, options);
        }
    }

    public sealed class Layer7ListenerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Authentication type of the layer7 listener. `0` is one-way authentication and `1` is mutual authentication. NOTES: Only
        /// supports listeners of `HTTPS` protocol.
        /// </summary>
        [Input("authType")]
        public Input<int>? AuthType { get; set; }

        /// <summary>
        /// Certificate ID of the layer7 listener. NOTES: Only supports listeners of `HTTPS` protocol.
        /// </summary>
        [Input("certificateId")]
        public Input<string>? CertificateId { get; set; }

        /// <summary>
        /// ID of the client certificate. Set only when `auth_type` is specified as mutual authentication. NOTES: Only supports
        /// listeners of `HTTPS` protocol.
        /// </summary>
        [Input("clientCertificateId")]
        public Input<string>? ClientCertificateId { get; set; }

        [Input("clientCertificateIds")]
        private InputList<string>? _clientCertificateIds;

        /// <summary>
        /// ID list of the client certificate. Set only when `auth_type` is specified as mutual authentication. NOTES: Only supports
        /// listeners of `HTTPS` protocol.
        /// </summary>
        public InputList<string> ClientCertificateIds
        {
            get => _clientCertificateIds ?? (_clientCertificateIds = new InputList<string>());
            set => _clientCertificateIds = value;
        }

        /// <summary>
        /// Protocol type of the forwarding. Valid value: `HTTP` and `HTTPS`. NOTES: Only supports listeners of `HTTPS` protocol.
        /// </summary>
        [Input("forwardProtocol")]
        public Input<string>? ForwardProtocol { get; set; }

        /// <summary>
        /// Name of the layer7 listener, the maximum length is 30.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Port of the layer7 listener.
        /// </summary>
        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        /// <summary>
        /// Protocol of the layer7 listener. Valid value: `HTTP` and `HTTPS`.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// ID of the GAAP proxy.
        /// </summary>
        [Input("proxyId", required: true)]
        public Input<string> ProxyId { get; set; } = null!;

        public Layer7ListenerArgs()
        {
        }
    }

    public sealed class Layer7ListenerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Authentication type of the layer7 listener. `0` is one-way authentication and `1` is mutual authentication. NOTES: Only
        /// supports listeners of `HTTPS` protocol.
        /// </summary>
        [Input("authType")]
        public Input<int>? AuthType { get; set; }

        /// <summary>
        /// Certificate ID of the layer7 listener. NOTES: Only supports listeners of `HTTPS` protocol.
        /// </summary>
        [Input("certificateId")]
        public Input<string>? CertificateId { get; set; }

        /// <summary>
        /// ID of the client certificate. Set only when `auth_type` is specified as mutual authentication. NOTES: Only supports
        /// listeners of `HTTPS` protocol.
        /// </summary>
        [Input("clientCertificateId")]
        public Input<string>? ClientCertificateId { get; set; }

        [Input("clientCertificateIds")]
        private InputList<string>? _clientCertificateIds;

        /// <summary>
        /// ID list of the client certificate. Set only when `auth_type` is specified as mutual authentication. NOTES: Only supports
        /// listeners of `HTTPS` protocol.
        /// </summary>
        public InputList<string> ClientCertificateIds
        {
            get => _clientCertificateIds ?? (_clientCertificateIds = new InputList<string>());
            set => _clientCertificateIds = value;
        }

        /// <summary>
        /// Creation time of the layer7 listener.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// Protocol type of the forwarding. Valid value: `HTTP` and `HTTPS`. NOTES: Only supports listeners of `HTTPS` protocol.
        /// </summary>
        [Input("forwardProtocol")]
        public Input<string>? ForwardProtocol { get; set; }

        /// <summary>
        /// Name of the layer7 listener, the maximum length is 30.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Port of the layer7 listener.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// Protocol of the layer7 listener. Valid value: `HTTP` and `HTTPS`.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// ID of the GAAP proxy.
        /// </summary>
        [Input("proxyId")]
        public Input<string>? ProxyId { get; set; }

        /// <summary>
        /// Status of the layer7 listener.
        /// </summary>
        [Input("status")]
        public Input<int>? Status { get; set; }

        public Layer7ListenerState()
        {
        }
    }
}
