// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Monitor
{
    public static class GetProductEvent
    {
        /// <summary>
        /// Use this data source to query monitor events(There is a lot of data and it is recommended to output to a file)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Tencentcloud = Pulumi.Tencentcloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var cvmEventData = Output.Create(Tencentcloud.Monitor.GetProductEvent.InvokeAsync(new Tencentcloud.Monitor.GetProductEventArgs
        ///         {
        ///             IsAlarmConfig = 0,
        ///             ProductNames = 
        ///             {
        ///                 "cvm",
        ///             },
        ///             StartTime = 1588700283,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetProductEventResult> InvokeAsync(GetProductEventArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProductEventResult>("tencentcloud:Monitor/getProductEvent:getProductEvent", args ?? new GetProductEventArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query monitor events(There is a lot of data and it is recommended to output to a file)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Tencentcloud = Pulumi.Tencentcloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var cvmEventData = Output.Create(Tencentcloud.Monitor.GetProductEvent.InvokeAsync(new Tencentcloud.Monitor.GetProductEventArgs
        ///         {
        ///             IsAlarmConfig = 0,
        ///             ProductNames = 
        ///             {
        ///                 "cvm",
        ///             },
        ///             StartTime = 1588700283,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetProductEventResult> Invoke(GetProductEventInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetProductEventResult>("tencentcloud:Monitor/getProductEvent:getProductEvent", args ?? new GetProductEventInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetProductEventArgs : Pulumi.InvokeArgs
    {
        [Input("dimensions")]
        private List<Inputs.GetProductEventDimensionArgs>? _dimensions;

        /// <summary>
        /// Dimensional composition of instance objects.
        /// </summary>
        public List<Inputs.GetProductEventDimensionArgs> Dimensions
        {
            get => _dimensions ?? (_dimensions = new List<Inputs.GetProductEventDimensionArgs>());
            set => _dimensions = value;
        }

        /// <summary>
        /// End timestamp for this query, eg:`1588232111`. Default start time is `now-3000`.
        /// </summary>
        [Input("endTime")]
        public int? EndTime { get; set; }

        [Input("eventNames")]
        private List<string>? _eventNames;

        /// <summary>
        /// Event name filtering, such as `guest_reboot` indicates that the machine restart.
        /// </summary>
        public List<string> EventNames
        {
            get => _eventNames ?? (_eventNames = new List<string>());
            set => _eventNames = value;
        }

        [Input("instanceIds")]
        private List<string>? _instanceIds;

        /// <summary>
        /// Affect objects, such as `ins-19708ino`.
        /// </summary>
        public List<string> InstanceIds
        {
            get => _instanceIds ?? (_instanceIds = new List<string>());
            set => _instanceIds = value;
        }

        /// <summary>
        /// Alarm status configuration filter, 1means configured, 0(default) means not configured.
        /// </summary>
        [Input("isAlarmConfig")]
        public int? IsAlarmConfig { get; set; }

        [Input("productNames")]
        private List<string>? _productNames;

        /// <summary>
        /// Product type filtering, such as `cvm` for cloud server.
        /// </summary>
        public List<string> ProductNames
        {
            get => _productNames ?? (_productNames = new List<string>());
            set => _productNames = value;
        }

        [Input("projectIds")]
        private List<string>? _projectIds;

        /// <summary>
        /// Project ID filter.
        /// </summary>
        public List<string> ProjectIds
        {
            get => _projectIds ?? (_projectIds = new List<string>());
            set => _projectIds = value;
        }

        [Input("regionLists")]
        private List<string>? _regionLists;

        /// <summary>
        /// Region filter, such as `gz`.
        /// </summary>
        public List<string> RegionLists
        {
            get => _regionLists ?? (_regionLists = new List<string>());
            set => _regionLists = value;
        }

        /// <summary>
        /// Used to store results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        /// <summary>
        /// Start timestamp for this query, eg:`1588230000`. Default start time is `now-3600`.
        /// </summary>
        [Input("startTime")]
        public int? StartTime { get; set; }

        [Input("statuses")]
        private List<string>? _statuses;

        /// <summary>
        /// Event status filter, value range `-`,`alarm`,`recover`, indicating recovered, unrecovered and stateless.
        /// </summary>
        public List<string> Statuses
        {
            get => _statuses ?? (_statuses = new List<string>());
            set => _statuses = value;
        }

        [Input("types")]
        private List<string>? _types;

        /// <summary>
        /// Event type filtering, with value range `abnormal`,`status_change`, indicating state change and abnormal events.
        /// </summary>
        public List<string> Types
        {
            get => _types ?? (_types = new List<string>());
            set => _types = value;
        }

        public GetProductEventArgs()
        {
        }
    }

    public sealed class GetProductEventInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("dimensions")]
        private InputList<Inputs.GetProductEventDimensionInputArgs>? _dimensions;

        /// <summary>
        /// Dimensional composition of instance objects.
        /// </summary>
        public InputList<Inputs.GetProductEventDimensionInputArgs> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputList<Inputs.GetProductEventDimensionInputArgs>());
            set => _dimensions = value;
        }

        /// <summary>
        /// End timestamp for this query, eg:`1588232111`. Default start time is `now-3000`.
        /// </summary>
        [Input("endTime")]
        public Input<int>? EndTime { get; set; }

        [Input("eventNames")]
        private InputList<string>? _eventNames;

        /// <summary>
        /// Event name filtering, such as `guest_reboot` indicates that the machine restart.
        /// </summary>
        public InputList<string> EventNames
        {
            get => _eventNames ?? (_eventNames = new InputList<string>());
            set => _eventNames = value;
        }

        [Input("instanceIds")]
        private InputList<string>? _instanceIds;

        /// <summary>
        /// Affect objects, such as `ins-19708ino`.
        /// </summary>
        public InputList<string> InstanceIds
        {
            get => _instanceIds ?? (_instanceIds = new InputList<string>());
            set => _instanceIds = value;
        }

        /// <summary>
        /// Alarm status configuration filter, 1means configured, 0(default) means not configured.
        /// </summary>
        [Input("isAlarmConfig")]
        public Input<int>? IsAlarmConfig { get; set; }

        [Input("productNames")]
        private InputList<string>? _productNames;

        /// <summary>
        /// Product type filtering, such as `cvm` for cloud server.
        /// </summary>
        public InputList<string> ProductNames
        {
            get => _productNames ?? (_productNames = new InputList<string>());
            set => _productNames = value;
        }

        [Input("projectIds")]
        private InputList<string>? _projectIds;

        /// <summary>
        /// Project ID filter.
        /// </summary>
        public InputList<string> ProjectIds
        {
            get => _projectIds ?? (_projectIds = new InputList<string>());
            set => _projectIds = value;
        }

        [Input("regionLists")]
        private InputList<string>? _regionLists;

        /// <summary>
        /// Region filter, such as `gz`.
        /// </summary>
        public InputList<string> RegionLists
        {
            get => _regionLists ?? (_regionLists = new InputList<string>());
            set => _regionLists = value;
        }

        /// <summary>
        /// Used to store results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        /// <summary>
        /// Start timestamp for this query, eg:`1588230000`. Default start time is `now-3600`.
        /// </summary>
        [Input("startTime")]
        public Input<int>? StartTime { get; set; }

        [Input("statuses")]
        private InputList<string>? _statuses;

        /// <summary>
        /// Event status filter, value range `-`,`alarm`,`recover`, indicating recovered, unrecovered and stateless.
        /// </summary>
        public InputList<string> Statuses
        {
            get => _statuses ?? (_statuses = new InputList<string>());
            set => _statuses = value;
        }

        [Input("types")]
        private InputList<string>? _types;

        /// <summary>
        /// Event type filtering, with value range `abnormal`,`status_change`, indicating state change and abnormal events.
        /// </summary>
        public InputList<string> Types
        {
            get => _types ?? (_types = new InputList<string>());
            set => _types = value;
        }

        public GetProductEventInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetProductEventResult
    {
        /// <summary>
        /// A list of event dimensions. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProductEventDimensionResult> Dimensions;
        public readonly int? EndTime;
        /// <summary>
        /// Event short name.
        /// </summary>
        public readonly ImmutableArray<string> EventNames;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The instance ID of this event.
        /// </summary>
        public readonly ImmutableArray<string> InstanceIds;
        /// <summary>
        /// Whether to configure alarm.
        /// </summary>
        public readonly int? IsAlarmConfig;
        /// <summary>
        /// A list events. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetProductEventListResult> Lists;
        /// <summary>
        /// Product short name.
        /// </summary>
        public readonly ImmutableArray<string> ProductNames;
        /// <summary>
        /// Project ID of this instance.
        /// </summary>
        public readonly ImmutableArray<string> ProjectIds;
        public readonly ImmutableArray<string> RegionLists;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// The start timestamp of this event.
        /// </summary>
        public readonly int? StartTime;
        /// <summary>
        /// The status of this event.
        /// </summary>
        public readonly ImmutableArray<string> Statuses;
        /// <summary>
        /// The type of this event.
        /// </summary>
        public readonly ImmutableArray<string> Types;

        [OutputConstructor]
        private GetProductEventResult(
            ImmutableArray<Outputs.GetProductEventDimensionResult> dimensions,

            int? endTime,

            ImmutableArray<string> eventNames,

            string id,

            ImmutableArray<string> instanceIds,

            int? isAlarmConfig,

            ImmutableArray<Outputs.GetProductEventListResult> lists,

            ImmutableArray<string> productNames,

            ImmutableArray<string> projectIds,

            ImmutableArray<string> regionLists,

            string? resultOutputFile,

            int? startTime,

            ImmutableArray<string> statuses,

            ImmutableArray<string> types)
        {
            Dimensions = dimensions;
            EndTime = endTime;
            EventNames = eventNames;
            Id = id;
            InstanceIds = instanceIds;
            IsAlarmConfig = isAlarmConfig;
            Lists = lists;
            ProductNames = productNames;
            ProjectIds = projectIds;
            RegionLists = regionLists;
            ResultOutputFile = resultOutputFile;
            StartTime = startTime;
            Statuses = statuses;
            Types = types;
        }
    }
}
