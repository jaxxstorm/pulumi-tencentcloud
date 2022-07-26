// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cls.Inputs
{

    public sealed class CosShipperContentJsonArgs : Pulumi.ResourceArgs
    {
        [Input("enableTag", required: true)]
        public Input<bool> EnableTag { get; set; } = null!;

        [Input("metaFields", required: true)]
        private InputList<string>? _metaFields;
        public InputList<string> MetaFields
        {
            get => _metaFields ?? (_metaFields = new InputList<string>());
            set => _metaFields = value;
        }

        public CosShipperContentJsonArgs()
        {
        }
    }
}
