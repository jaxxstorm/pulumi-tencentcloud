// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cos
{
    public static class GetBucketObject
    {
        /// <summary>
        /// Use this data source to query the metadata of an object stored inside a bucket.
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
        ///         var mycos = Output.Create(Tencentcloud.Cos.GetBucketObject.InvokeAsync(new Tencentcloud.Cos.GetBucketObjectArgs
        ///         {
        ///             Bucket = "mycos-test-1258798060",
        ///             Key = "hello-world.py",
        ///             ResultOutputFile = "TFresults",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetBucketObjectResult> InvokeAsync(GetBucketObjectArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBucketObjectResult>("tencentcloud:Cos/getBucketObject:getBucketObject", args ?? new GetBucketObjectArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query the metadata of an object stored inside a bucket.
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
        ///         var mycos = Output.Create(Tencentcloud.Cos.GetBucketObject.InvokeAsync(new Tencentcloud.Cos.GetBucketObjectArgs
        ///         {
        ///             Bucket = "mycos-test-1258798060",
        ///             Key = "hello-world.py",
        ///             ResultOutputFile = "TFresults",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetBucketObjectResult> Invoke(GetBucketObjectInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetBucketObjectResult>("tencentcloud:Cos/getBucketObject:getBucketObject", args ?? new GetBucketObjectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBucketObjectArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the bucket that contains the objects to query.
        /// </summary>
        [Input("bucket", required: true)]
        public string Bucket { get; set; } = null!;

        /// <summary>
        /// The full path to the object inside the bucket.
        /// </summary>
        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetBucketObjectArgs()
        {
        }
    }

    public sealed class GetBucketObjectInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the bucket that contains the objects to query.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// The full path to the object inside the bucket.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetBucketObjectInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetBucketObjectResult
    {
        public readonly string Bucket;
        /// <summary>
        /// Specifies caching behavior along the request/reply chain.
        /// </summary>
        public readonly string CacheControl;
        /// <summary>
        /// Specifies presentational information for the object.
        /// </summary>
        public readonly string ContentDisposition;
        /// <summary>
        /// Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        /// </summary>
        public readonly string ContentEncoding;
        /// <summary>
        /// A standard MIME type describing the format of the object data.
        /// </summary>
        public readonly string ContentType;
        /// <summary>
        /// ETag generated for the object, which is may not equal to MD5 value.
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Key;
        /// <summary>
        /// Last modified date of the object.
        /// </summary>
        public readonly string LastModified;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// Object storage type such as STANDARD.
        /// </summary>
        public readonly string StorageClass;

        [OutputConstructor]
        private GetBucketObjectResult(
            string bucket,

            string cacheControl,

            string contentDisposition,

            string contentEncoding,

            string contentType,

            string etag,

            string id,

            string key,

            string lastModified,

            string? resultOutputFile,

            string storageClass)
        {
            Bucket = bucket;
            CacheControl = cacheControl;
            ContentDisposition = contentDisposition;
            ContentEncoding = contentEncoding;
            ContentType = contentType;
            Etag = etag;
            Id = id;
            Key = key;
            LastModified = lastModified;
            ResultOutputFile = resultOutputFile;
            StorageClass = storageClass;
        }
    }
}
