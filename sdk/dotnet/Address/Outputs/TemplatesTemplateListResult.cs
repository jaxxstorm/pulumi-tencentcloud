// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Address.Outputs
{

    [OutputType]
    public sealed class TemplatesTemplateListResult
    {
        public readonly ImmutableArray<string> Addresses;
        public readonly string Id;
        public readonly string Name;

        [OutputConstructor]
        private TemplatesTemplateListResult(
            ImmutableArray<string> addresses,

            string id,

            string name)
        {
            Addresses = addresses;
            Id = id;
            Name = name;
        }
    }
}
