// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cls.Inputs
{

    public sealed class CosShipperContentCsvArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Field delimiter.
        /// </summary>
        [Input("delimiter", required: true)]
        public Input<string> Delimiter { get; set; } = null!;

        /// <summary>
        /// Field delimiter.
        /// </summary>
        [Input("escapeChar", required: true)]
        public Input<string> EscapeChar { get; set; } = null!;

        [Input("keys", required: true)]
        private InputList<string>? _keys;

        /// <summary>
        /// Names of keys.Note: this field may return null, indicating that no valid values can be obtained.
        /// </summary>
        public InputList<string> Keys
        {
            get => _keys ?? (_keys = new InputList<string>());
            set => _keys = value;
        }

        /// <summary>
        /// Content used to populate non-existing fields.
        /// </summary>
        [Input("nonExistingField", required: true)]
        public Input<string> NonExistingField { get; set; } = null!;

        /// <summary>
        /// Whether to print key on the first row of the CSV file.
        /// </summary>
        [Input("printKey", required: true)]
        public Input<bool> PrintKey { get; set; } = null!;

        public CosShipperContentCsvArgs()
        {
        }
    }
}
