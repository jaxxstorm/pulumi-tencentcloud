// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.As
{
    [TencentcloudResourceType("tencentcloud:As/scalingGroup:ScalingGroup")]
    public partial class ScalingGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// An available ID for a launch configuration.
        /// </summary>
        [Output("configurationId")]
        public Output<string> ConfigurationId { get; private set; } = null!;

        /// <summary>
        /// The time when the AS group was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Default cooldown time in second, and default value is `300`.
        /// </summary>
        [Output("defaultCooldown")]
        public Output<int?> DefaultCooldown { get; private set; } = null!;

        /// <summary>
        /// Desired volume of CVM instances, which is between `max_size` and `min_size`.
        /// </summary>
        [Output("desiredCapacity")]
        public Output<int> DesiredCapacity { get; private set; } = null!;

        /// <summary>
        /// List of application load balancers, which can't be specified with `load_balancer_ids` together.
        /// </summary>
        [Output("forwardBalancerIds")]
        public Output<ImmutableArray<Outputs.ScalingGroupForwardBalancerId>> ForwardBalancerIds { get; private set; } = null!;

        /// <summary>
        /// Instance number of a scaling group.
        /// </summary>
        [Output("instanceCount")]
        public Output<int> InstanceCount { get; private set; } = null!;

        /// <summary>
        /// ID list of traditional load balancers.
        /// </summary>
        [Output("loadBalancerIds")]
        public Output<ImmutableArray<string>> LoadBalancerIds { get; private set; } = null!;

        /// <summary>
        /// Maximum number of CVM instances. Valid value ranges: (0~2000).
        /// </summary>
        [Output("maxSize")]
        public Output<int> MaxSize { get; private set; } = null!;

        /// <summary>
        /// Minimum number of CVM instances. Valid value ranges: (0~2000).
        /// </summary>
        [Output("minSize")]
        public Output<int> MinSize { get; private set; } = null!;

        /// <summary>
        /// Multi zone or subnet strategy, Valid values: PRIORITY and EQUALITY.
        /// </summary>
        [Output("multiZoneSubnetPolicy")]
        public Output<string?> MultiZoneSubnetPolicy { get; private set; } = null!;

        /// <summary>
        /// Specifies to which project the scaling group belongs.
        /// </summary>
        [Output("projectId")]
        public Output<int?> ProjectId { get; private set; } = null!;

        /// <summary>
        /// Enable unhealthy instance replacement. If set to `true`, AS will replace instances that are found unhealthy in the CLB
        /// health check.
        /// </summary>
        [Output("replaceLoadBalancerUnhealthy")]
        public Output<bool?> ReplaceLoadBalancerUnhealthy { get; private set; } = null!;

        /// <summary>
        /// Enables unhealthy instance replacement. If set to `true`, AS will replace instances that are flagged as unhealthy by
        /// Cloud Monitor.
        /// </summary>
        [Output("replaceMonitorUnhealthy")]
        public Output<bool?> ReplaceMonitorUnhealthy { get; private set; } = null!;

        /// <summary>
        /// Available values for retry policies. Valid values: IMMEDIATE_RETRY and INCREMENTAL_INTERVALS.
        /// </summary>
        [Output("retryPolicy")]
        public Output<string?> RetryPolicy { get; private set; } = null!;

        /// <summary>
        /// Name of a scaling group.
        /// </summary>
        [Output("scalingGroupName")]
        public Output<string> ScalingGroupName { get; private set; } = null!;

        /// <summary>
        /// Indicates scaling mode which creates and terminates instances (classic method), or method first tries to start stopped
        /// instances (wake up stopped) to perform scaling operations. Available values: `CLASSIC_SCALING`,
        /// `WAKE_UP_STOPPED_SCALING`. Default: `CLASSIC_SCALING`.
        /// </summary>
        [Output("scalingMode")]
        public Output<string?> ScalingMode { get; private set; } = null!;

        /// <summary>
        /// Current status of a scaling group.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// ID list of subnet, and for VPC it is required.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// Tags of a scaling group.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// Available values for termination policies. Valid values: OLDEST_INSTANCE and NEWEST_INSTANCE.
        /// </summary>
        [Output("terminationPolicies")]
        public Output<string> TerminationPolicies { get; private set; } = null!;

        /// <summary>
        /// ID of VPC network.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;

        /// <summary>
        /// List of available zones, for Basic network it is required.
        /// </summary>
        [Output("zones")]
        public Output<ImmutableArray<string>> Zones { get; private set; } = null!;


        /// <summary>
        /// Create a ScalingGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ScalingGroup(string name, ScalingGroupArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:As/scalingGroup:ScalingGroup", name, args ?? new ScalingGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ScalingGroup(string name, Input<string> id, ScalingGroupState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:As/scalingGroup:ScalingGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ScalingGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ScalingGroup Get(string name, Input<string> id, ScalingGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new ScalingGroup(name, id, state, options);
        }
    }

    public sealed class ScalingGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An available ID for a launch configuration.
        /// </summary>
        [Input("configurationId", required: true)]
        public Input<string> ConfigurationId { get; set; } = null!;

        /// <summary>
        /// Default cooldown time in second, and default value is `300`.
        /// </summary>
        [Input("defaultCooldown")]
        public Input<int>? DefaultCooldown { get; set; }

        /// <summary>
        /// Desired volume of CVM instances, which is between `max_size` and `min_size`.
        /// </summary>
        [Input("desiredCapacity")]
        public Input<int>? DesiredCapacity { get; set; }

        [Input("forwardBalancerIds")]
        private InputList<Inputs.ScalingGroupForwardBalancerIdArgs>? _forwardBalancerIds;

        /// <summary>
        /// List of application load balancers, which can't be specified with `load_balancer_ids` together.
        /// </summary>
        public InputList<Inputs.ScalingGroupForwardBalancerIdArgs> ForwardBalancerIds
        {
            get => _forwardBalancerIds ?? (_forwardBalancerIds = new InputList<Inputs.ScalingGroupForwardBalancerIdArgs>());
            set => _forwardBalancerIds = value;
        }

        [Input("loadBalancerIds")]
        private InputList<string>? _loadBalancerIds;

        /// <summary>
        /// ID list of traditional load balancers.
        /// </summary>
        public InputList<string> LoadBalancerIds
        {
            get => _loadBalancerIds ?? (_loadBalancerIds = new InputList<string>());
            set => _loadBalancerIds = value;
        }

        /// <summary>
        /// Maximum number of CVM instances. Valid value ranges: (0~2000).
        /// </summary>
        [Input("maxSize", required: true)]
        public Input<int> MaxSize { get; set; } = null!;

        /// <summary>
        /// Minimum number of CVM instances. Valid value ranges: (0~2000).
        /// </summary>
        [Input("minSize", required: true)]
        public Input<int> MinSize { get; set; } = null!;

        /// <summary>
        /// Multi zone or subnet strategy, Valid values: PRIORITY and EQUALITY.
        /// </summary>
        [Input("multiZoneSubnetPolicy")]
        public Input<string>? MultiZoneSubnetPolicy { get; set; }

        /// <summary>
        /// Specifies to which project the scaling group belongs.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// Enable unhealthy instance replacement. If set to `true`, AS will replace instances that are found unhealthy in the CLB
        /// health check.
        /// </summary>
        [Input("replaceLoadBalancerUnhealthy")]
        public Input<bool>? ReplaceLoadBalancerUnhealthy { get; set; }

        /// <summary>
        /// Enables unhealthy instance replacement. If set to `true`, AS will replace instances that are flagged as unhealthy by
        /// Cloud Monitor.
        /// </summary>
        [Input("replaceMonitorUnhealthy")]
        public Input<bool>? ReplaceMonitorUnhealthy { get; set; }

        /// <summary>
        /// Available values for retry policies. Valid values: IMMEDIATE_RETRY and INCREMENTAL_INTERVALS.
        /// </summary>
        [Input("retryPolicy")]
        public Input<string>? RetryPolicy { get; set; }

        /// <summary>
        /// Name of a scaling group.
        /// </summary>
        [Input("scalingGroupName", required: true)]
        public Input<string> ScalingGroupName { get; set; } = null!;

        /// <summary>
        /// Indicates scaling mode which creates and terminates instances (classic method), or method first tries to start stopped
        /// instances (wake up stopped) to perform scaling operations. Available values: `CLASSIC_SCALING`,
        /// `WAKE_UP_STOPPED_SCALING`. Default: `CLASSIC_SCALING`.
        /// </summary>
        [Input("scalingMode")]
        public Input<string>? ScalingMode { get; set; }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// ID list of subnet, and for VPC it is required.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Tags of a scaling group.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Available values for termination policies. Valid values: OLDEST_INSTANCE and NEWEST_INSTANCE.
        /// </summary>
        [Input("terminationPolicies")]
        public Input<string>? TerminationPolicies { get; set; }

        /// <summary>
        /// ID of VPC network.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        [Input("zones")]
        private InputList<string>? _zones;

        /// <summary>
        /// List of available zones, for Basic network it is required.
        /// </summary>
        public InputList<string> Zones
        {
            get => _zones ?? (_zones = new InputList<string>());
            set => _zones = value;
        }

        public ScalingGroupArgs()
        {
        }
    }

    public sealed class ScalingGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An available ID for a launch configuration.
        /// </summary>
        [Input("configurationId")]
        public Input<string>? ConfigurationId { get; set; }

        /// <summary>
        /// The time when the AS group was created.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// Default cooldown time in second, and default value is `300`.
        /// </summary>
        [Input("defaultCooldown")]
        public Input<int>? DefaultCooldown { get; set; }

        /// <summary>
        /// Desired volume of CVM instances, which is between `max_size` and `min_size`.
        /// </summary>
        [Input("desiredCapacity")]
        public Input<int>? DesiredCapacity { get; set; }

        [Input("forwardBalancerIds")]
        private InputList<Inputs.ScalingGroupForwardBalancerIdGetArgs>? _forwardBalancerIds;

        /// <summary>
        /// List of application load balancers, which can't be specified with `load_balancer_ids` together.
        /// </summary>
        public InputList<Inputs.ScalingGroupForwardBalancerIdGetArgs> ForwardBalancerIds
        {
            get => _forwardBalancerIds ?? (_forwardBalancerIds = new InputList<Inputs.ScalingGroupForwardBalancerIdGetArgs>());
            set => _forwardBalancerIds = value;
        }

        /// <summary>
        /// Instance number of a scaling group.
        /// </summary>
        [Input("instanceCount")]
        public Input<int>? InstanceCount { get; set; }

        [Input("loadBalancerIds")]
        private InputList<string>? _loadBalancerIds;

        /// <summary>
        /// ID list of traditional load balancers.
        /// </summary>
        public InputList<string> LoadBalancerIds
        {
            get => _loadBalancerIds ?? (_loadBalancerIds = new InputList<string>());
            set => _loadBalancerIds = value;
        }

        /// <summary>
        /// Maximum number of CVM instances. Valid value ranges: (0~2000).
        /// </summary>
        [Input("maxSize")]
        public Input<int>? MaxSize { get; set; }

        /// <summary>
        /// Minimum number of CVM instances. Valid value ranges: (0~2000).
        /// </summary>
        [Input("minSize")]
        public Input<int>? MinSize { get; set; }

        /// <summary>
        /// Multi zone or subnet strategy, Valid values: PRIORITY and EQUALITY.
        /// </summary>
        [Input("multiZoneSubnetPolicy")]
        public Input<string>? MultiZoneSubnetPolicy { get; set; }

        /// <summary>
        /// Specifies to which project the scaling group belongs.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// Enable unhealthy instance replacement. If set to `true`, AS will replace instances that are found unhealthy in the CLB
        /// health check.
        /// </summary>
        [Input("replaceLoadBalancerUnhealthy")]
        public Input<bool>? ReplaceLoadBalancerUnhealthy { get; set; }

        /// <summary>
        /// Enables unhealthy instance replacement. If set to `true`, AS will replace instances that are flagged as unhealthy by
        /// Cloud Monitor.
        /// </summary>
        [Input("replaceMonitorUnhealthy")]
        public Input<bool>? ReplaceMonitorUnhealthy { get; set; }

        /// <summary>
        /// Available values for retry policies. Valid values: IMMEDIATE_RETRY and INCREMENTAL_INTERVALS.
        /// </summary>
        [Input("retryPolicy")]
        public Input<string>? RetryPolicy { get; set; }

        /// <summary>
        /// Name of a scaling group.
        /// </summary>
        [Input("scalingGroupName")]
        public Input<string>? ScalingGroupName { get; set; }

        /// <summary>
        /// Indicates scaling mode which creates and terminates instances (classic method), or method first tries to start stopped
        /// instances (wake up stopped) to perform scaling operations. Available values: `CLASSIC_SCALING`,
        /// `WAKE_UP_STOPPED_SCALING`. Default: `CLASSIC_SCALING`.
        /// </summary>
        [Input("scalingMode")]
        public Input<string>? ScalingMode { get; set; }

        /// <summary>
        /// Current status of a scaling group.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// ID list of subnet, and for VPC it is required.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Tags of a scaling group.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Available values for termination policies. Valid values: OLDEST_INSTANCE and NEWEST_INSTANCE.
        /// </summary>
        [Input("terminationPolicies")]
        public Input<string>? TerminationPolicies { get; set; }

        /// <summary>
        /// ID of VPC network.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        [Input("zones")]
        private InputList<string>? _zones;

        /// <summary>
        /// List of available zones, for Basic network it is required.
        /// </summary>
        public InputList<string> Zones
        {
            get => _zones ?? (_zones = new InputList<string>());
            set => _zones = value;
        }

        public ScalingGroupState()
        {
        }
    }
}
