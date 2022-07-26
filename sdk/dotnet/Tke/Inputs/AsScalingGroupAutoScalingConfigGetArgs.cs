// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Tke.Inputs
{

    public sealed class AsScalingGroupAutoScalingConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("configurationName", required: true)]
        public Input<string> ConfigurationName { get; set; } = null!;

        [Input("dataDisks")]
        private InputList<Inputs.AsScalingGroupAutoScalingConfigDataDiskGetArgs>? _dataDisks;
        public InputList<Inputs.AsScalingGroupAutoScalingConfigDataDiskGetArgs> DataDisks
        {
            get => _dataDisks ?? (_dataDisks = new InputList<Inputs.AsScalingGroupAutoScalingConfigDataDiskGetArgs>());
            set => _dataDisks = value;
        }

        [Input("enhancedMonitorService")]
        public Input<bool>? EnhancedMonitorService { get; set; }

        [Input("enhancedSecurityService")]
        public Input<bool>? EnhancedSecurityService { get; set; }

        [Input("instanceTags")]
        private InputMap<object>? _instanceTags;
        public InputMap<object> InstanceTags
        {
            get => _instanceTags ?? (_instanceTags = new InputMap<object>());
            set => _instanceTags = value;
        }

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

        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        [Input("publicIpAssigned")]
        public Input<bool>? PublicIpAssigned { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("systemDiskSize")]
        public Input<int>? SystemDiskSize { get; set; }

        [Input("systemDiskType")]
        public Input<string>? SystemDiskType { get; set; }

        public AsScalingGroupAutoScalingConfigGetArgs()
        {
        }
    }
}
