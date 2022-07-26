// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cloud.Outputs
{

    [OutputType]
    public sealed class APIGatewayUsagePlanEnvironmentsListResult
    {
        public readonly string ApiId;
        public readonly string ApiName;
        public readonly string CreateTime;
        public readonly string Environment;
        public readonly string Method;
        public readonly string ModifyTime;
        public readonly string Path;
        public readonly string ServiceId;
        public readonly string ServiceName;

        [OutputConstructor]
        private APIGatewayUsagePlanEnvironmentsListResult(
            string apiId,

            string apiName,

            string createTime,

            string environment,

            string method,

            string modifyTime,

            string path,

            string serviceId,

            string serviceName)
        {
            ApiId = apiId;
            ApiName = apiName;
            CreateTime = createTime;
            Environment = environment;
            Method = method;
            ModifyTime = modifyTime;
            Path = path;
            ServiceId = serviceId;
            ServiceName = serviceName;
        }
    }
}
