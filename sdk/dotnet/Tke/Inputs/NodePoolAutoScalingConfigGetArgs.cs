// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Tke.Inputs
{

    public sealed class NodePoolAutoScalingConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("backupInstanceTypes")]
        private InputList<string>? _backupInstanceTypes;
        public InputList<string> BackupInstanceTypes
        {
            get => _backupInstanceTypes ?? (_backupInstanceTypes = new InputList<string>());
            set => _backupInstanceTypes = value;
        }

        [Input("bandwidthPackageId")]
        public Input<string>? BandwidthPackageId { get; set; }

        [Input("camRoleName")]
        public Input<string>? CamRoleName { get; set; }

        [Input("dataDisks")]
        private InputList<Inputs.NodePoolAutoScalingConfigDataDiskGetArgs>? _dataDisks;
        public InputList<Inputs.NodePoolAutoScalingConfigDataDiskGetArgs> DataDisks
        {
            get => _dataDisks ?? (_dataDisks = new InputList<Inputs.NodePoolAutoScalingConfigDataDiskGetArgs>());
            set => _dataDisks = value;
        }

        [Input("enhancedMonitorService")]
        public Input<bool>? EnhancedMonitorService { get; set; }

        [Input("enhancedSecurityService")]
        public Input<bool>? EnhancedSecurityService { get; set; }

        [Input("instanceChargeType")]
        public Input<string>? InstanceChargeType { get; set; }

        [Input("instanceChargeTypePrepaidPeriod")]
        public Input<int>? InstanceChargeTypePrepaidPeriod { get; set; }

        [Input("instanceChargeTypePrepaidRenewFlag")]
        public Input<string>? InstanceChargeTypePrepaidRenewFlag { get; set; }

        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        [Input("internetChargeType")]
        public Input<string>? InternetChargeType { get; set; }

        [Input("internetMaxBandwidthOut")]
        public Input<int>? InternetMaxBandwidthOut { get; set; }

        [Input("keyIds")]
        private InputList<string>? _keyIds;
        public InputList<string> KeyIds
        {
            get => _keyIds ?? (_keyIds = new InputList<string>());
            set => _keyIds = value;
        }

        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("publicIpAssigned")]
        public Input<bool>? PublicIpAssigned { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("spotInstanceType")]
        public Input<string>? SpotInstanceType { get; set; }

        [Input("spotMaxPrice")]
        public Input<string>? SpotMaxPrice { get; set; }

        [Input("systemDiskSize")]
        public Input<int>? SystemDiskSize { get; set; }

        [Input("systemDiskType")]
        public Input<string>? SystemDiskType { get; set; }

        public NodePoolAutoScalingConfigGetArgs()
        {
        }
    }
}
