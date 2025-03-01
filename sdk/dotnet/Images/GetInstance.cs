// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Images
{
    public static class GetInstance
    {
        /// <summary>
        /// Use this data source to query images.
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
        ///         var foo = Output.Create(Tencentcloud.Images.GetInstance.InvokeAsync(new Tencentcloud.Images.GetInstanceArgs
        ///         {
        ///             ImageTypes = 
        ///             {
        ///                 "PUBLIC_IMAGE",
        ///             },
        ///             OsName = "centos 7.5",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetInstanceResult> InvokeAsync(GetInstanceArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstanceResult>("tencentcloud:Images/getInstance:getInstance", args ?? new GetInstanceArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query images.
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
        ///         var foo = Output.Create(Tencentcloud.Images.GetInstance.InvokeAsync(new Tencentcloud.Images.GetInstanceArgs
        ///         {
        ///             ImageTypes = 
        ///             {
        ///                 "PUBLIC_IMAGE",
        ///             },
        ///             OsName = "centos 7.5",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetInstanceResult> Invoke(GetInstanceInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetInstanceResult>("tencentcloud:Images/getInstance:getInstance", args ?? new GetInstanceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInstanceArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the image to be queried.
        /// </summary>
        [Input("imageId")]
        public string? ImageId { get; set; }

        /// <summary>
        /// A regex string to apply to the image list returned by TencentCloud, conflict with 'os_name'. **NOTE**: it is not wildcard, should look like `image_name_regex = "^CentOS\s+6\.8\s+64\w*"`.
        /// </summary>
        [Input("imageNameRegex")]
        public string? ImageNameRegex { get; set; }

        [Input("imageTypes")]
        private List<string>? _imageTypes;

        /// <summary>
        /// A list of the image type to be queried. Valid values: 'PUBLIC_IMAGE', 'PRIVATE_IMAGE', 'SHARED_IMAGE', 'MARKET_IMAGE'.
        /// </summary>
        public List<string> ImageTypes
        {
            get => _imageTypes ?? (_imageTypes = new List<string>());
            set => _imageTypes = value;
        }

        /// <summary>
        /// Instance type, such as `S1.SMALL1`.
        /// </summary>
        [Input("instanceType")]
        public string? InstanceType { get; set; }

        /// <summary>
        /// A string to apply with fuzzy match to the os_name attribute on the image list returned by TencentCloud, conflict with 'image_name_regex'.
        /// </summary>
        [Input("osName")]
        public string? OsName { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetInstanceArgs()
        {
        }
    }

    public sealed class GetInstanceInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the image to be queried.
        /// </summary>
        [Input("imageId")]
        public Input<string>? ImageId { get; set; }

        /// <summary>
        /// A regex string to apply to the image list returned by TencentCloud, conflict with 'os_name'. **NOTE**: it is not wildcard, should look like `image_name_regex = "^CentOS\s+6\.8\s+64\w*"`.
        /// </summary>
        [Input("imageNameRegex")]
        public Input<string>? ImageNameRegex { get; set; }

        [Input("imageTypes")]
        private InputList<string>? _imageTypes;

        /// <summary>
        /// A list of the image type to be queried. Valid values: 'PUBLIC_IMAGE', 'PRIVATE_IMAGE', 'SHARED_IMAGE', 'MARKET_IMAGE'.
        /// </summary>
        public InputList<string> ImageTypes
        {
            get => _imageTypes ?? (_imageTypes = new InputList<string>());
            set => _imageTypes = value;
        }

        /// <summary>
        /// Instance type, such as `S1.SMALL1`.
        /// </summary>
        [Input("instanceType")]
        public Input<string>? InstanceType { get; set; }

        /// <summary>
        /// A string to apply with fuzzy match to the os_name attribute on the image list returned by TencentCloud, conflict with 'image_name_regex'.
        /// </summary>
        [Input("osName")]
        public Input<string>? OsName { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetInstanceInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetInstanceResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// ID of the image.
        /// </summary>
        public readonly string? ImageId;
        public readonly string? ImageNameRegex;
        /// <summary>
        /// Type of the image.
        /// </summary>
        public readonly ImmutableArray<string> ImageTypes;
        /// <summary>
        /// An information list of image. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInstanceImageResult> Images;
        public readonly string? InstanceType;
        /// <summary>
        /// OS name of the image.
        /// </summary>
        public readonly string? OsName;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetInstanceResult(
            string id,

            string? imageId,

            string? imageNameRegex,

            ImmutableArray<string> imageTypes,

            ImmutableArray<Outputs.GetInstanceImageResult> images,

            string? instanceType,

            string? osName,

            string? resultOutputFile)
        {
            Id = id;
            ImageId = imageId;
            ImageNameRegex = imageNameRegex;
            ImageTypes = imageTypes;
            Images = images;
            InstanceType = instanceType;
            OsName = osName;
            ResultOutputFile = resultOutputFile;
        }
    }
}
