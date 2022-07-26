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
    public sealed class PolicyGroupsListConditionResult
    {
        public readonly int AlarmNotifyPeriod;
        public readonly int AlarmNotifyType;
        public readonly int CalcType;
        public readonly string CalcValue;
        public readonly int ContinueTime;
        public readonly int MetricId;
        public readonly string MetricShowName;
        public readonly string MetricUnit;
        public readonly int Period;
        public readonly int RuleId;

        [OutputConstructor]
        private PolicyGroupsListConditionResult(
            int alarmNotifyPeriod,

            int alarmNotifyType,

            int calcType,

            string calcValue,

            int continueTime,

            int metricId,

            string metricShowName,

            string metricUnit,

            int period,

            int ruleId)
        {
            AlarmNotifyPeriod = alarmNotifyPeriod;
            AlarmNotifyType = alarmNotifyType;
            CalcType = calcType;
            CalcValue = calcValue;
            ContinueTime = continueTime;
            MetricId = metricId;
            MetricShowName = metricShowName;
            MetricUnit = metricUnit;
            Period = period;
            RuleId = ruleId;
        }
    }
}
