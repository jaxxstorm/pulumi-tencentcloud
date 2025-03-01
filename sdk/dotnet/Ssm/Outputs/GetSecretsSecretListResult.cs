// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Ssm.Outputs
{

    [OutputType]
    public sealed class GetSecretsSecretListResult
    {
        /// <summary>
        /// Create time of secret.
        /// </summary>
        public readonly int CreateTime;
        /// <summary>
        /// Uin of Creator.
        /// </summary>
        public readonly int CreateUin;
        /// <summary>
        /// Delete time of CMK.
        /// </summary>
        public readonly int DeleteTime;
        /// <summary>
        /// Description of secret.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// KMS keyId used to encrypt secret.
        /// </summary>
        public readonly string KmsKeyId;
        /// <summary>
        /// Secret name used to filter result.
        /// </summary>
        public readonly string SecretName;
        /// <summary>
        /// Status of secret.
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private GetSecretsSecretListResult(
            int createTime,

            int createUin,

            int deleteTime,

            string description,

            string kmsKeyId,

            string secretName,

            string status)
        {
            CreateTime = createTime;
            CreateUin = createUin;
            DeleteTime = deleteTime;
            Description = description;
            KmsKeyId = kmsKeyId;
            SecretName = secretName;
            Status = status;
        }
    }
}
