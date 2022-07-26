// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Vpn.Outputs
{

    [OutputType]
    public sealed class ConnectionsConnectionListSecurityGroupPolicyResult
    {
        public readonly string LocalCidrBlock;
        public readonly ImmutableArray<string> RemoteCidrBlocks;

        [OutputConstructor]
        private ConnectionsConnectionListSecurityGroupPolicyResult(
            string localCidrBlock,

            ImmutableArray<string> remoteCidrBlocks)
        {
            LocalCidrBlock = localCidrBlock;
            RemoteCidrBlocks = remoteCidrBlocks;
        }
    }
}
