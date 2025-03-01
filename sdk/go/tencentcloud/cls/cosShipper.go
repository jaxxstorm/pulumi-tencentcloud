// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cls

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a resource to create a cls cos shipper.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Cls"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Cls"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Cls.NewCosShipper(ctx, "shipper", &Cls.CosShipperArgs{
// 			Bucket: pulumi.String("preset-scf-bucket-1308919341"),
// 			Compress: &cls.CosShipperCompressArgs{
// 				Format: pulumi.String("lzop"),
// 			},
// 			Content: &cls.CosShipperContentArgs{
// 				Format: pulumi.String("json"),
// 				Json: &cls.CosShipperContentJsonArgs{
// 					EnableTag: pulumi.Bool(true),
// 					MetaFields: pulumi.StringArray{
// 						pulumi.String("__FILENAME__"),
// 						pulumi.String("__SOURCE__"),
// 						pulumi.String("__TIMESTAMP__"),
// 					},
// 				},
// 			},
// 			Interval:    pulumi.Int(300),
// 			MaxSize:     pulumi.Int(200),
// 			Partition:   pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v", "/", "%", "Y/", "%", "m/", "%", "d/", "%", "H/")),
// 			Prefix:      pulumi.String("ap-guangzhou-fffsasad-1649734752"),
// 			ShipperName: pulumi.String("ap-guangzhou-fffsasad-1649734752"),
// 			TopicId:     pulumi.String("4d07fba0-b93e-4e0b-9a7f-d58542560bbb"),
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
// cls cos shipper can be imported using the id, e.g.
//
// ```sh
//  $ pulumi import tencentcloud:Cls/cosShipper:CosShipper shipper 5d1b7b2a-c163-4c48-bb01-9ee00584d761
// ```
type CosShipper struct {
	pulumi.CustomResourceState

	// Destination bucket in the shipping rule to be created.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// Compression configuration of shipped log.
	Compress CosShipperCompressPtrOutput `pulumi:"compress"`
	// Format configuration of shipped log content.
	Content CosShipperContentPtrOutput `pulumi:"content"`
	// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
	FilterRules CosShipperFilterRuleArrayOutput `pulumi:"filterRules"`
	// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
	Interval pulumi.IntPtrOutput `pulumi:"interval"`
	// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
	MaxSize pulumi.IntPtrOutput `pulumi:"maxSize"`
	// Partition rule of shipped log, which can be represented in strftime time format.
	Partition pulumi.StringPtrOutput `pulumi:"partition"`
	// Prefix of the shipping directory in the shipping rule to be created.
	Prefix pulumi.StringOutput `pulumi:"prefix"`
	// Shipping rule name.
	ShipperName pulumi.StringOutput `pulumi:"shipperName"`
	// ID of the log topic to which the shipping rule to be created belongs.
	TopicId pulumi.StringOutput `pulumi:"topicId"`
}

// NewCosShipper registers a new resource with the given unique name, arguments, and options.
func NewCosShipper(ctx *pulumi.Context,
	name string, args *CosShipperArgs, opts ...pulumi.ResourceOption) (*CosShipper, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bucket == nil {
		return nil, errors.New("invalid value for required argument 'Bucket'")
	}
	if args.Prefix == nil {
		return nil, errors.New("invalid value for required argument 'Prefix'")
	}
	if args.ShipperName == nil {
		return nil, errors.New("invalid value for required argument 'ShipperName'")
	}
	if args.TopicId == nil {
		return nil, errors.New("invalid value for required argument 'TopicId'")
	}
	var resource CosShipper
	err := ctx.RegisterResource("tencentcloud:Cls/cosShipper:CosShipper", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCosShipper gets an existing CosShipper resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCosShipper(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CosShipperState, opts ...pulumi.ResourceOption) (*CosShipper, error) {
	var resource CosShipper
	err := ctx.ReadResource("tencentcloud:Cls/cosShipper:CosShipper", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CosShipper resources.
type cosShipperState struct {
	// Destination bucket in the shipping rule to be created.
	Bucket *string `pulumi:"bucket"`
	// Compression configuration of shipped log.
	Compress *CosShipperCompress `pulumi:"compress"`
	// Format configuration of shipped log content.
	Content *CosShipperContent `pulumi:"content"`
	// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
	FilterRules []CosShipperFilterRule `pulumi:"filterRules"`
	// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
	Interval *int `pulumi:"interval"`
	// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
	MaxSize *int `pulumi:"maxSize"`
	// Partition rule of shipped log, which can be represented in strftime time format.
	Partition *string `pulumi:"partition"`
	// Prefix of the shipping directory in the shipping rule to be created.
	Prefix *string `pulumi:"prefix"`
	// Shipping rule name.
	ShipperName *string `pulumi:"shipperName"`
	// ID of the log topic to which the shipping rule to be created belongs.
	TopicId *string `pulumi:"topicId"`
}

type CosShipperState struct {
	// Destination bucket in the shipping rule to be created.
	Bucket pulumi.StringPtrInput
	// Compression configuration of shipped log.
	Compress CosShipperCompressPtrInput
	// Format configuration of shipped log content.
	Content CosShipperContentPtrInput
	// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
	FilterRules CosShipperFilterRuleArrayInput
	// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
	Interval pulumi.IntPtrInput
	// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
	MaxSize pulumi.IntPtrInput
	// Partition rule of shipped log, which can be represented in strftime time format.
	Partition pulumi.StringPtrInput
	// Prefix of the shipping directory in the shipping rule to be created.
	Prefix pulumi.StringPtrInput
	// Shipping rule name.
	ShipperName pulumi.StringPtrInput
	// ID of the log topic to which the shipping rule to be created belongs.
	TopicId pulumi.StringPtrInput
}

func (CosShipperState) ElementType() reflect.Type {
	return reflect.TypeOf((*cosShipperState)(nil)).Elem()
}

type cosShipperArgs struct {
	// Destination bucket in the shipping rule to be created.
	Bucket string `pulumi:"bucket"`
	// Compression configuration of shipped log.
	Compress *CosShipperCompress `pulumi:"compress"`
	// Format configuration of shipped log content.
	Content *CosShipperContent `pulumi:"content"`
	// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
	FilterRules []CosShipperFilterRule `pulumi:"filterRules"`
	// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
	Interval *int `pulumi:"interval"`
	// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
	MaxSize *int `pulumi:"maxSize"`
	// Partition rule of shipped log, which can be represented in strftime time format.
	Partition *string `pulumi:"partition"`
	// Prefix of the shipping directory in the shipping rule to be created.
	Prefix string `pulumi:"prefix"`
	// Shipping rule name.
	ShipperName string `pulumi:"shipperName"`
	// ID of the log topic to which the shipping rule to be created belongs.
	TopicId string `pulumi:"topicId"`
}

// The set of arguments for constructing a CosShipper resource.
type CosShipperArgs struct {
	// Destination bucket in the shipping rule to be created.
	Bucket pulumi.StringInput
	// Compression configuration of shipped log.
	Compress CosShipperCompressPtrInput
	// Format configuration of shipped log content.
	Content CosShipperContentPtrInput
	// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
	FilterRules CosShipperFilterRuleArrayInput
	// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
	Interval pulumi.IntPtrInput
	// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
	MaxSize pulumi.IntPtrInput
	// Partition rule of shipped log, which can be represented in strftime time format.
	Partition pulumi.StringPtrInput
	// Prefix of the shipping directory in the shipping rule to be created.
	Prefix pulumi.StringInput
	// Shipping rule name.
	ShipperName pulumi.StringInput
	// ID of the log topic to which the shipping rule to be created belongs.
	TopicId pulumi.StringInput
}

func (CosShipperArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cosShipperArgs)(nil)).Elem()
}

type CosShipperInput interface {
	pulumi.Input

	ToCosShipperOutput() CosShipperOutput
	ToCosShipperOutputWithContext(ctx context.Context) CosShipperOutput
}

func (*CosShipper) ElementType() reflect.Type {
	return reflect.TypeOf((**CosShipper)(nil)).Elem()
}

func (i *CosShipper) ToCosShipperOutput() CosShipperOutput {
	return i.ToCosShipperOutputWithContext(context.Background())
}

func (i *CosShipper) ToCosShipperOutputWithContext(ctx context.Context) CosShipperOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CosShipperOutput)
}

// CosShipperArrayInput is an input type that accepts CosShipperArray and CosShipperArrayOutput values.
// You can construct a concrete instance of `CosShipperArrayInput` via:
//
//          CosShipperArray{ CosShipperArgs{...} }
type CosShipperArrayInput interface {
	pulumi.Input

	ToCosShipperArrayOutput() CosShipperArrayOutput
	ToCosShipperArrayOutputWithContext(context.Context) CosShipperArrayOutput
}

type CosShipperArray []CosShipperInput

func (CosShipperArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CosShipper)(nil)).Elem()
}

func (i CosShipperArray) ToCosShipperArrayOutput() CosShipperArrayOutput {
	return i.ToCosShipperArrayOutputWithContext(context.Background())
}

func (i CosShipperArray) ToCosShipperArrayOutputWithContext(ctx context.Context) CosShipperArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CosShipperArrayOutput)
}

// CosShipperMapInput is an input type that accepts CosShipperMap and CosShipperMapOutput values.
// You can construct a concrete instance of `CosShipperMapInput` via:
//
//          CosShipperMap{ "key": CosShipperArgs{...} }
type CosShipperMapInput interface {
	pulumi.Input

	ToCosShipperMapOutput() CosShipperMapOutput
	ToCosShipperMapOutputWithContext(context.Context) CosShipperMapOutput
}

type CosShipperMap map[string]CosShipperInput

func (CosShipperMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CosShipper)(nil)).Elem()
}

func (i CosShipperMap) ToCosShipperMapOutput() CosShipperMapOutput {
	return i.ToCosShipperMapOutputWithContext(context.Background())
}

func (i CosShipperMap) ToCosShipperMapOutputWithContext(ctx context.Context) CosShipperMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CosShipperMapOutput)
}

type CosShipperOutput struct{ *pulumi.OutputState }

func (CosShipperOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CosShipper)(nil)).Elem()
}

func (o CosShipperOutput) ToCosShipperOutput() CosShipperOutput {
	return o
}

func (o CosShipperOutput) ToCosShipperOutputWithContext(ctx context.Context) CosShipperOutput {
	return o
}

// Destination bucket in the shipping rule to be created.
func (o CosShipperOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v *CosShipper) pulumi.StringOutput { return v.Bucket }).(pulumi.StringOutput)
}

// Compression configuration of shipped log.
func (o CosShipperOutput) Compress() CosShipperCompressPtrOutput {
	return o.ApplyT(func(v *CosShipper) CosShipperCompressPtrOutput { return v.Compress }).(CosShipperCompressPtrOutput)
}

// Format configuration of shipped log content.
func (o CosShipperOutput) Content() CosShipperContentPtrOutput {
	return o.ApplyT(func(v *CosShipper) CosShipperContentPtrOutput { return v.Content }).(CosShipperContentPtrOutput)
}

// Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
func (o CosShipperOutput) FilterRules() CosShipperFilterRuleArrayOutput {
	return o.ApplyT(func(v *CosShipper) CosShipperFilterRuleArrayOutput { return v.FilterRules }).(CosShipperFilterRuleArrayOutput)
}

// Shipping time interval in seconds. Default value: 300. Value range: 300~900.
func (o CosShipperOutput) Interval() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *CosShipper) pulumi.IntPtrOutput { return v.Interval }).(pulumi.IntPtrOutput)
}

// Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
func (o CosShipperOutput) MaxSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *CosShipper) pulumi.IntPtrOutput { return v.MaxSize }).(pulumi.IntPtrOutput)
}

// Partition rule of shipped log, which can be represented in strftime time format.
func (o CosShipperOutput) Partition() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CosShipper) pulumi.StringPtrOutput { return v.Partition }).(pulumi.StringPtrOutput)
}

// Prefix of the shipping directory in the shipping rule to be created.
func (o CosShipperOutput) Prefix() pulumi.StringOutput {
	return o.ApplyT(func(v *CosShipper) pulumi.StringOutput { return v.Prefix }).(pulumi.StringOutput)
}

// Shipping rule name.
func (o CosShipperOutput) ShipperName() pulumi.StringOutput {
	return o.ApplyT(func(v *CosShipper) pulumi.StringOutput { return v.ShipperName }).(pulumi.StringOutput)
}

// ID of the log topic to which the shipping rule to be created belongs.
func (o CosShipperOutput) TopicId() pulumi.StringOutput {
	return o.ApplyT(func(v *CosShipper) pulumi.StringOutput { return v.TopicId }).(pulumi.StringOutput)
}

type CosShipperArrayOutput struct{ *pulumi.OutputState }

func (CosShipperArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CosShipper)(nil)).Elem()
}

func (o CosShipperArrayOutput) ToCosShipperArrayOutput() CosShipperArrayOutput {
	return o
}

func (o CosShipperArrayOutput) ToCosShipperArrayOutputWithContext(ctx context.Context) CosShipperArrayOutput {
	return o
}

func (o CosShipperArrayOutput) Index(i pulumi.IntInput) CosShipperOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CosShipper {
		return vs[0].([]*CosShipper)[vs[1].(int)]
	}).(CosShipperOutput)
}

type CosShipperMapOutput struct{ *pulumi.OutputState }

func (CosShipperMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CosShipper)(nil)).Elem()
}

func (o CosShipperMapOutput) ToCosShipperMapOutput() CosShipperMapOutput {
	return o
}

func (o CosShipperMapOutput) ToCosShipperMapOutputWithContext(ctx context.Context) CosShipperMapOutput {
	return o
}

func (o CosShipperMapOutput) MapIndex(k pulumi.StringInput) CosShipperOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CosShipper {
		return vs[0].(map[string]*CosShipper)[vs[1].(string)]
	}).(CosShipperOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CosShipperInput)(nil)).Elem(), &CosShipper{})
	pulumi.RegisterInputType(reflect.TypeOf((*CosShipperArrayInput)(nil)).Elem(), CosShipperArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CosShipperMapInput)(nil)).Elem(), CosShipperMap{})
	pulumi.RegisterOutputType(CosShipperOutput{})
	pulumi.RegisterOutputType(CosShipperArrayOutput{})
	pulumi.RegisterOutputType(CosShipperMapOutput{})
}
