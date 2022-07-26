// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Mysql.Outputs
{

    [OutputType]
    public sealed class DefaultParamsParamListResult
    {
        public readonly string CurrentValue;
        public readonly string Default;
        public readonly string Description;
        public readonly ImmutableArray<string> EnumValues;
        public readonly int Max;
        public readonly int Min;
        public readonly string Name;
        public readonly int NeedReboot;
        public readonly string ParamType;

        [OutputConstructor]
        private DefaultParamsParamListResult(
            string currentValue,

            string @default,

            string description,

            ImmutableArray<string> enumValues,

            int max,

            int min,

            string name,

            int needReboot,

            string paramType)
        {
            CurrentValue = currentValue;
            Default = @default;
            Description = description;
            EnumValues = enumValues;
            Max = max;
            Min = min;
            Name = name;
            NeedReboot = needReboot;
            ParamType = paramType;
        }
    }
}
