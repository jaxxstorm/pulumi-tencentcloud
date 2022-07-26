// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Monitor.Outputs
{

    [OutputType]
    public sealed class ProductNamespaceListResult
    {
        public readonly string Namespace;
        public readonly string ProductChineseName;
        public readonly string ProductName;

        [OutputConstructor]
        private ProductNamespaceListResult(
            string @namespace,

            string productChineseName,

            string productName)
        {
            Namespace = @namespace;
            ProductChineseName = productChineseName;
            ProductName = productName;
        }
    }
}
