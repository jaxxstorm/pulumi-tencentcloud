// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vod

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provide a resource to create a VOD adaptive dynamic streaming template.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Vod"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Vod"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Vod.NewAdaptiveDynamicStreamingTemplate(ctx, "foo", &Vod.AdaptiveDynamicStreamingTemplateArgs{
// 			Comment:                      pulumi.String("test"),
// 			DisableHigherVideoBitrate:    pulumi.Bool(false),
// 			DisableHigherVideoResolution: pulumi.Bool(false),
// 			DrmType:                      pulumi.String("SimpleAES"),
// 			Format:                       pulumi.String("HLS"),
// 			StreamInfos: vod.AdaptiveDynamicStreamingTemplateStreamInfoArray{
// 				&vod.AdaptiveDynamicStreamingTemplateStreamInfoArgs{
// 					Audio: &vod.AdaptiveDynamicStreamingTemplateStreamInfoAudioArgs{
// 						AudioChannel: pulumi.String("dual"),
// 						Bitrate:      pulumi.Int(129),
// 						Codec:        pulumi.String("libmp3lame"),
// 						SampleRate:   pulumi.Int(44100),
// 					},
// 					RemoveAudio: pulumi.Bool(false),
// 					Video: &vod.AdaptiveDynamicStreamingTemplateStreamInfoVideoArgs{
// 						Bitrate:            pulumi.Int(129),
// 						Codec:              pulumi.String("libx265"),
// 						FillType:           pulumi.String("stretch"),
// 						Fps:                pulumi.Int(4),
// 						Height:             pulumi.Int(128),
// 						ResolutionAdaptive: pulumi.Bool(false),
// 						Width:              pulumi.Int(128),
// 					},
// 				},
// 				&vod.AdaptiveDynamicStreamingTemplateStreamInfoArgs{
// 					Audio: &vod.AdaptiveDynamicStreamingTemplateStreamInfoAudioArgs{
// 						Bitrate:    pulumi.Int(256),
// 						Codec:      pulumi.String("libfdk_aac"),
// 						SampleRate: pulumi.Int(44100),
// 					},
// 					RemoveAudio: pulumi.Bool(true),
// 					Video: &vod.AdaptiveDynamicStreamingTemplateStreamInfoVideoArgs{
// 						Bitrate: pulumi.Int(256),
// 						Codec:   pulumi.String("libx264"),
// 						Fps:     pulumi.Int(4),
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// VOD adaptive dynamic streaming template can be imported using the id, e.g.
//
// ```sh
//  $ pulumi import tencentcloud:Vod/adaptiveDynamicStreamingTemplate:AdaptiveDynamicStreamingTemplate foo 169141
// ```
type AdaptiveDynamicStreamingTemplate struct {
	pulumi.CustomResourceState

	// Template description. Length limit: 256 characters.
	Comment pulumi.StringPtrOutput `pulumi:"comment"`
	// Creation time of template in ISO date format.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoBitrate pulumi.BoolPtrOutput `pulumi:"disableHigherVideoBitrate"`
	// Whether to prohibit transcoding from low resolution to high resolution. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoResolution pulumi.BoolPtrOutput `pulumi:"disableHigherVideoResolution"`
	// DRM scheme type. Valid values: `SimpleAES`. If this field is an empty string, DRM will not be performed on the video.
	DrmType pulumi.StringPtrOutput `pulumi:"drmType"`
	// Adaptive bitstream format. Valid values: `HLS`.
	Format pulumi.StringOutput `pulumi:"format"`
	// Template name. Length limit: 64 characters.
	Name pulumi.StringOutput `pulumi:"name"`
	// List of AdaptiveStreamTemplate parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output. Note: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate.
	StreamInfos AdaptiveDynamicStreamingTemplateStreamInfoArrayOutput `pulumi:"streamInfos"`
	// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
	SubAppId pulumi.IntPtrOutput `pulumi:"subAppId"`
	// Last modified time of template in ISO date format.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewAdaptiveDynamicStreamingTemplate registers a new resource with the given unique name, arguments, and options.
func NewAdaptiveDynamicStreamingTemplate(ctx *pulumi.Context,
	name string, args *AdaptiveDynamicStreamingTemplateArgs, opts ...pulumi.ResourceOption) (*AdaptiveDynamicStreamingTemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Format == nil {
		return nil, errors.New("invalid value for required argument 'Format'")
	}
	if args.StreamInfos == nil {
		return nil, errors.New("invalid value for required argument 'StreamInfos'")
	}
	var resource AdaptiveDynamicStreamingTemplate
	err := ctx.RegisterResource("tencentcloud:Vod/adaptiveDynamicStreamingTemplate:AdaptiveDynamicStreamingTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAdaptiveDynamicStreamingTemplate gets an existing AdaptiveDynamicStreamingTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAdaptiveDynamicStreamingTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AdaptiveDynamicStreamingTemplateState, opts ...pulumi.ResourceOption) (*AdaptiveDynamicStreamingTemplate, error) {
	var resource AdaptiveDynamicStreamingTemplate
	err := ctx.ReadResource("tencentcloud:Vod/adaptiveDynamicStreamingTemplate:AdaptiveDynamicStreamingTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AdaptiveDynamicStreamingTemplate resources.
type adaptiveDynamicStreamingTemplateState struct {
	// Template description. Length limit: 256 characters.
	Comment *string `pulumi:"comment"`
	// Creation time of template in ISO date format.
	CreateTime *string `pulumi:"createTime"`
	// Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoBitrate *bool `pulumi:"disableHigherVideoBitrate"`
	// Whether to prohibit transcoding from low resolution to high resolution. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoResolution *bool `pulumi:"disableHigherVideoResolution"`
	// DRM scheme type. Valid values: `SimpleAES`. If this field is an empty string, DRM will not be performed on the video.
	DrmType *string `pulumi:"drmType"`
	// Adaptive bitstream format. Valid values: `HLS`.
	Format *string `pulumi:"format"`
	// Template name. Length limit: 64 characters.
	Name *string `pulumi:"name"`
	// List of AdaptiveStreamTemplate parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output. Note: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate.
	StreamInfos []AdaptiveDynamicStreamingTemplateStreamInfo `pulumi:"streamInfos"`
	// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
	SubAppId *int `pulumi:"subAppId"`
	// Last modified time of template in ISO date format.
	UpdateTime *string `pulumi:"updateTime"`
}

type AdaptiveDynamicStreamingTemplateState struct {
	// Template description. Length limit: 256 characters.
	Comment pulumi.StringPtrInput
	// Creation time of template in ISO date format.
	CreateTime pulumi.StringPtrInput
	// Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoBitrate pulumi.BoolPtrInput
	// Whether to prohibit transcoding from low resolution to high resolution. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoResolution pulumi.BoolPtrInput
	// DRM scheme type. Valid values: `SimpleAES`. If this field is an empty string, DRM will not be performed on the video.
	DrmType pulumi.StringPtrInput
	// Adaptive bitstream format. Valid values: `HLS`.
	Format pulumi.StringPtrInput
	// Template name. Length limit: 64 characters.
	Name pulumi.StringPtrInput
	// List of AdaptiveStreamTemplate parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output. Note: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate.
	StreamInfos AdaptiveDynamicStreamingTemplateStreamInfoArrayInput
	// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
	SubAppId pulumi.IntPtrInput
	// Last modified time of template in ISO date format.
	UpdateTime pulumi.StringPtrInput
}

func (AdaptiveDynamicStreamingTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*adaptiveDynamicStreamingTemplateState)(nil)).Elem()
}

type adaptiveDynamicStreamingTemplateArgs struct {
	// Template description. Length limit: 256 characters.
	Comment *string `pulumi:"comment"`
	// Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoBitrate *bool `pulumi:"disableHigherVideoBitrate"`
	// Whether to prohibit transcoding from low resolution to high resolution. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoResolution *bool `pulumi:"disableHigherVideoResolution"`
	// DRM scheme type. Valid values: `SimpleAES`. If this field is an empty string, DRM will not be performed on the video.
	DrmType *string `pulumi:"drmType"`
	// Adaptive bitstream format. Valid values: `HLS`.
	Format string `pulumi:"format"`
	// Template name. Length limit: 64 characters.
	Name *string `pulumi:"name"`
	// List of AdaptiveStreamTemplate parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output. Note: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate.
	StreamInfos []AdaptiveDynamicStreamingTemplateStreamInfo `pulumi:"streamInfos"`
	// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
	SubAppId *int `pulumi:"subAppId"`
}

// The set of arguments for constructing a AdaptiveDynamicStreamingTemplate resource.
type AdaptiveDynamicStreamingTemplateArgs struct {
	// Template description. Length limit: 256 characters.
	Comment pulumi.StringPtrInput
	// Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoBitrate pulumi.BoolPtrInput
	// Whether to prohibit transcoding from low resolution to high resolution. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
	DisableHigherVideoResolution pulumi.BoolPtrInput
	// DRM scheme type. Valid values: `SimpleAES`. If this field is an empty string, DRM will not be performed on the video.
	DrmType pulumi.StringPtrInput
	// Adaptive bitstream format. Valid values: `HLS`.
	Format pulumi.StringInput
	// Template name. Length limit: 64 characters.
	Name pulumi.StringPtrInput
	// List of AdaptiveStreamTemplate parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output. Note: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate.
	StreamInfos AdaptiveDynamicStreamingTemplateStreamInfoArrayInput
	// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
	SubAppId pulumi.IntPtrInput
}

func (AdaptiveDynamicStreamingTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*adaptiveDynamicStreamingTemplateArgs)(nil)).Elem()
}

type AdaptiveDynamicStreamingTemplateInput interface {
	pulumi.Input

	ToAdaptiveDynamicStreamingTemplateOutput() AdaptiveDynamicStreamingTemplateOutput
	ToAdaptiveDynamicStreamingTemplateOutputWithContext(ctx context.Context) AdaptiveDynamicStreamingTemplateOutput
}

func (*AdaptiveDynamicStreamingTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**AdaptiveDynamicStreamingTemplate)(nil)).Elem()
}

func (i *AdaptiveDynamicStreamingTemplate) ToAdaptiveDynamicStreamingTemplateOutput() AdaptiveDynamicStreamingTemplateOutput {
	return i.ToAdaptiveDynamicStreamingTemplateOutputWithContext(context.Background())
}

func (i *AdaptiveDynamicStreamingTemplate) ToAdaptiveDynamicStreamingTemplateOutputWithContext(ctx context.Context) AdaptiveDynamicStreamingTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AdaptiveDynamicStreamingTemplateOutput)
}

// AdaptiveDynamicStreamingTemplateArrayInput is an input type that accepts AdaptiveDynamicStreamingTemplateArray and AdaptiveDynamicStreamingTemplateArrayOutput values.
// You can construct a concrete instance of `AdaptiveDynamicStreamingTemplateArrayInput` via:
//
//          AdaptiveDynamicStreamingTemplateArray{ AdaptiveDynamicStreamingTemplateArgs{...} }
type AdaptiveDynamicStreamingTemplateArrayInput interface {
	pulumi.Input

	ToAdaptiveDynamicStreamingTemplateArrayOutput() AdaptiveDynamicStreamingTemplateArrayOutput
	ToAdaptiveDynamicStreamingTemplateArrayOutputWithContext(context.Context) AdaptiveDynamicStreamingTemplateArrayOutput
}

type AdaptiveDynamicStreamingTemplateArray []AdaptiveDynamicStreamingTemplateInput

func (AdaptiveDynamicStreamingTemplateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AdaptiveDynamicStreamingTemplate)(nil)).Elem()
}

func (i AdaptiveDynamicStreamingTemplateArray) ToAdaptiveDynamicStreamingTemplateArrayOutput() AdaptiveDynamicStreamingTemplateArrayOutput {
	return i.ToAdaptiveDynamicStreamingTemplateArrayOutputWithContext(context.Background())
}

func (i AdaptiveDynamicStreamingTemplateArray) ToAdaptiveDynamicStreamingTemplateArrayOutputWithContext(ctx context.Context) AdaptiveDynamicStreamingTemplateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AdaptiveDynamicStreamingTemplateArrayOutput)
}

// AdaptiveDynamicStreamingTemplateMapInput is an input type that accepts AdaptiveDynamicStreamingTemplateMap and AdaptiveDynamicStreamingTemplateMapOutput values.
// You can construct a concrete instance of `AdaptiveDynamicStreamingTemplateMapInput` via:
//
//          AdaptiveDynamicStreamingTemplateMap{ "key": AdaptiveDynamicStreamingTemplateArgs{...} }
type AdaptiveDynamicStreamingTemplateMapInput interface {
	pulumi.Input

	ToAdaptiveDynamicStreamingTemplateMapOutput() AdaptiveDynamicStreamingTemplateMapOutput
	ToAdaptiveDynamicStreamingTemplateMapOutputWithContext(context.Context) AdaptiveDynamicStreamingTemplateMapOutput
}

type AdaptiveDynamicStreamingTemplateMap map[string]AdaptiveDynamicStreamingTemplateInput

func (AdaptiveDynamicStreamingTemplateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AdaptiveDynamicStreamingTemplate)(nil)).Elem()
}

func (i AdaptiveDynamicStreamingTemplateMap) ToAdaptiveDynamicStreamingTemplateMapOutput() AdaptiveDynamicStreamingTemplateMapOutput {
	return i.ToAdaptiveDynamicStreamingTemplateMapOutputWithContext(context.Background())
}

func (i AdaptiveDynamicStreamingTemplateMap) ToAdaptiveDynamicStreamingTemplateMapOutputWithContext(ctx context.Context) AdaptiveDynamicStreamingTemplateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AdaptiveDynamicStreamingTemplateMapOutput)
}

type AdaptiveDynamicStreamingTemplateOutput struct{ *pulumi.OutputState }

func (AdaptiveDynamicStreamingTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AdaptiveDynamicStreamingTemplate)(nil)).Elem()
}

func (o AdaptiveDynamicStreamingTemplateOutput) ToAdaptiveDynamicStreamingTemplateOutput() AdaptiveDynamicStreamingTemplateOutput {
	return o
}

func (o AdaptiveDynamicStreamingTemplateOutput) ToAdaptiveDynamicStreamingTemplateOutputWithContext(ctx context.Context) AdaptiveDynamicStreamingTemplateOutput {
	return o
}

// Template description. Length limit: 256 characters.
func (o AdaptiveDynamicStreamingTemplateOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.StringPtrOutput { return v.Comment }).(pulumi.StringPtrOutput)
}

// Creation time of template in ISO date format.
func (o AdaptiveDynamicStreamingTemplateOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
func (o AdaptiveDynamicStreamingTemplateOutput) DisableHigherVideoBitrate() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.BoolPtrOutput { return v.DisableHigherVideoBitrate }).(pulumi.BoolPtrOutput)
}

// Whether to prohibit transcoding from low resolution to high resolution. Valid values: `false`,`true`. `false`: no, `true`: yes. Default value: `false`.
func (o AdaptiveDynamicStreamingTemplateOutput) DisableHigherVideoResolution() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.BoolPtrOutput { return v.DisableHigherVideoResolution }).(pulumi.BoolPtrOutput)
}

// DRM scheme type. Valid values: `SimpleAES`. If this field is an empty string, DRM will not be performed on the video.
func (o AdaptiveDynamicStreamingTemplateOutput) DrmType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.StringPtrOutput { return v.DrmType }).(pulumi.StringPtrOutput)
}

// Adaptive bitstream format. Valid values: `HLS`.
func (o AdaptiveDynamicStreamingTemplateOutput) Format() pulumi.StringOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.StringOutput { return v.Format }).(pulumi.StringOutput)
}

// Template name. Length limit: 64 characters.
func (o AdaptiveDynamicStreamingTemplateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// List of AdaptiveStreamTemplate parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output. Note: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate.
func (o AdaptiveDynamicStreamingTemplateOutput) StreamInfos() AdaptiveDynamicStreamingTemplateStreamInfoArrayOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) AdaptiveDynamicStreamingTemplateStreamInfoArrayOutput {
		return v.StreamInfos
	}).(AdaptiveDynamicStreamingTemplateStreamInfoArrayOutput)
}

// Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
func (o AdaptiveDynamicStreamingTemplateOutput) SubAppId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.IntPtrOutput { return v.SubAppId }).(pulumi.IntPtrOutput)
}

// Last modified time of template in ISO date format.
func (o AdaptiveDynamicStreamingTemplateOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *AdaptiveDynamicStreamingTemplate) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

type AdaptiveDynamicStreamingTemplateArrayOutput struct{ *pulumi.OutputState }

func (AdaptiveDynamicStreamingTemplateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AdaptiveDynamicStreamingTemplate)(nil)).Elem()
}

func (o AdaptiveDynamicStreamingTemplateArrayOutput) ToAdaptiveDynamicStreamingTemplateArrayOutput() AdaptiveDynamicStreamingTemplateArrayOutput {
	return o
}

func (o AdaptiveDynamicStreamingTemplateArrayOutput) ToAdaptiveDynamicStreamingTemplateArrayOutputWithContext(ctx context.Context) AdaptiveDynamicStreamingTemplateArrayOutput {
	return o
}

func (o AdaptiveDynamicStreamingTemplateArrayOutput) Index(i pulumi.IntInput) AdaptiveDynamicStreamingTemplateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AdaptiveDynamicStreamingTemplate {
		return vs[0].([]*AdaptiveDynamicStreamingTemplate)[vs[1].(int)]
	}).(AdaptiveDynamicStreamingTemplateOutput)
}

type AdaptiveDynamicStreamingTemplateMapOutput struct{ *pulumi.OutputState }

func (AdaptiveDynamicStreamingTemplateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AdaptiveDynamicStreamingTemplate)(nil)).Elem()
}

func (o AdaptiveDynamicStreamingTemplateMapOutput) ToAdaptiveDynamicStreamingTemplateMapOutput() AdaptiveDynamicStreamingTemplateMapOutput {
	return o
}

func (o AdaptiveDynamicStreamingTemplateMapOutput) ToAdaptiveDynamicStreamingTemplateMapOutputWithContext(ctx context.Context) AdaptiveDynamicStreamingTemplateMapOutput {
	return o
}

func (o AdaptiveDynamicStreamingTemplateMapOutput) MapIndex(k pulumi.StringInput) AdaptiveDynamicStreamingTemplateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AdaptiveDynamicStreamingTemplate {
		return vs[0].(map[string]*AdaptiveDynamicStreamingTemplate)[vs[1].(string)]
	}).(AdaptiveDynamicStreamingTemplateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AdaptiveDynamicStreamingTemplateInput)(nil)).Elem(), &AdaptiveDynamicStreamingTemplate{})
	pulumi.RegisterInputType(reflect.TypeOf((*AdaptiveDynamicStreamingTemplateArrayInput)(nil)).Elem(), AdaptiveDynamicStreamingTemplateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AdaptiveDynamicStreamingTemplateMapInput)(nil)).Elem(), AdaptiveDynamicStreamingTemplateMap{})
	pulumi.RegisterOutputType(AdaptiveDynamicStreamingTemplateOutput{})
	pulumi.RegisterOutputType(AdaptiveDynamicStreamingTemplateArrayOutput{})
	pulumi.RegisterOutputType(AdaptiveDynamicStreamingTemplateMapOutput{})
}
