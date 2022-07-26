// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clb

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type TGAttachmentInstance struct {
	pulumi.CustomResourceState

	// The Intranet IP of the target group instance.
	BindIp pulumi.StringOutput `pulumi:"bindIp"`
	// Port of the target group instance.
	Port pulumi.IntOutput `pulumi:"port"`
	// Target group ID.
	TargetGroupId pulumi.StringOutput `pulumi:"targetGroupId"`
	// The weight of the target group instance.
	Weight pulumi.IntOutput `pulumi:"weight"`
}

// NewTGAttachmentInstance registers a new resource with the given unique name, arguments, and options.
func NewTGAttachmentInstance(ctx *pulumi.Context,
	name string, args *TGAttachmentInstanceArgs, opts ...pulumi.ResourceOption) (*TGAttachmentInstance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BindIp == nil {
		return nil, errors.New("invalid value for required argument 'BindIp'")
	}
	if args.Port == nil {
		return nil, errors.New("invalid value for required argument 'Port'")
	}
	if args.TargetGroupId == nil {
		return nil, errors.New("invalid value for required argument 'TargetGroupId'")
	}
	if args.Weight == nil {
		return nil, errors.New("invalid value for required argument 'Weight'")
	}
	var resource TGAttachmentInstance
	err := ctx.RegisterResource("tencentcloud:Clb/tGAttachmentInstance:TGAttachmentInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTGAttachmentInstance gets an existing TGAttachmentInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTGAttachmentInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TGAttachmentInstanceState, opts ...pulumi.ResourceOption) (*TGAttachmentInstance, error) {
	var resource TGAttachmentInstance
	err := ctx.ReadResource("tencentcloud:Clb/tGAttachmentInstance:TGAttachmentInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TGAttachmentInstance resources.
type tgattachmentInstanceState struct {
	// The Intranet IP of the target group instance.
	BindIp *string `pulumi:"bindIp"`
	// Port of the target group instance.
	Port *int `pulumi:"port"`
	// Target group ID.
	TargetGroupId *string `pulumi:"targetGroupId"`
	// The weight of the target group instance.
	Weight *int `pulumi:"weight"`
}

type TGAttachmentInstanceState struct {
	// The Intranet IP of the target group instance.
	BindIp pulumi.StringPtrInput
	// Port of the target group instance.
	Port pulumi.IntPtrInput
	// Target group ID.
	TargetGroupId pulumi.StringPtrInput
	// The weight of the target group instance.
	Weight pulumi.IntPtrInput
}

func (TGAttachmentInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*tgattachmentInstanceState)(nil)).Elem()
}

type tgattachmentInstanceArgs struct {
	// The Intranet IP of the target group instance.
	BindIp string `pulumi:"bindIp"`
	// Port of the target group instance.
	Port int `pulumi:"port"`
	// Target group ID.
	TargetGroupId string `pulumi:"targetGroupId"`
	// The weight of the target group instance.
	Weight int `pulumi:"weight"`
}

// The set of arguments for constructing a TGAttachmentInstance resource.
type TGAttachmentInstanceArgs struct {
	// The Intranet IP of the target group instance.
	BindIp pulumi.StringInput
	// Port of the target group instance.
	Port pulumi.IntInput
	// Target group ID.
	TargetGroupId pulumi.StringInput
	// The weight of the target group instance.
	Weight pulumi.IntInput
}

func (TGAttachmentInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tgattachmentInstanceArgs)(nil)).Elem()
}

type TGAttachmentInstanceInput interface {
	pulumi.Input

	ToTGAttachmentInstanceOutput() TGAttachmentInstanceOutput
	ToTGAttachmentInstanceOutputWithContext(ctx context.Context) TGAttachmentInstanceOutput
}

func (*TGAttachmentInstance) ElementType() reflect.Type {
	return reflect.TypeOf((**TGAttachmentInstance)(nil)).Elem()
}

func (i *TGAttachmentInstance) ToTGAttachmentInstanceOutput() TGAttachmentInstanceOutput {
	return i.ToTGAttachmentInstanceOutputWithContext(context.Background())
}

func (i *TGAttachmentInstance) ToTGAttachmentInstanceOutputWithContext(ctx context.Context) TGAttachmentInstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TGAttachmentInstanceOutput)
}

// TGAttachmentInstanceArrayInput is an input type that accepts TGAttachmentInstanceArray and TGAttachmentInstanceArrayOutput values.
// You can construct a concrete instance of `TGAttachmentInstanceArrayInput` via:
//
//          TGAttachmentInstanceArray{ TGAttachmentInstanceArgs{...} }
type TGAttachmentInstanceArrayInput interface {
	pulumi.Input

	ToTGAttachmentInstanceArrayOutput() TGAttachmentInstanceArrayOutput
	ToTGAttachmentInstanceArrayOutputWithContext(context.Context) TGAttachmentInstanceArrayOutput
}

type TGAttachmentInstanceArray []TGAttachmentInstanceInput

func (TGAttachmentInstanceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TGAttachmentInstance)(nil)).Elem()
}

func (i TGAttachmentInstanceArray) ToTGAttachmentInstanceArrayOutput() TGAttachmentInstanceArrayOutput {
	return i.ToTGAttachmentInstanceArrayOutputWithContext(context.Background())
}

func (i TGAttachmentInstanceArray) ToTGAttachmentInstanceArrayOutputWithContext(ctx context.Context) TGAttachmentInstanceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TGAttachmentInstanceArrayOutput)
}

// TGAttachmentInstanceMapInput is an input type that accepts TGAttachmentInstanceMap and TGAttachmentInstanceMapOutput values.
// You can construct a concrete instance of `TGAttachmentInstanceMapInput` via:
//
//          TGAttachmentInstanceMap{ "key": TGAttachmentInstanceArgs{...} }
type TGAttachmentInstanceMapInput interface {
	pulumi.Input

	ToTGAttachmentInstanceMapOutput() TGAttachmentInstanceMapOutput
	ToTGAttachmentInstanceMapOutputWithContext(context.Context) TGAttachmentInstanceMapOutput
}

type TGAttachmentInstanceMap map[string]TGAttachmentInstanceInput

func (TGAttachmentInstanceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TGAttachmentInstance)(nil)).Elem()
}

func (i TGAttachmentInstanceMap) ToTGAttachmentInstanceMapOutput() TGAttachmentInstanceMapOutput {
	return i.ToTGAttachmentInstanceMapOutputWithContext(context.Background())
}

func (i TGAttachmentInstanceMap) ToTGAttachmentInstanceMapOutputWithContext(ctx context.Context) TGAttachmentInstanceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TGAttachmentInstanceMapOutput)
}

type TGAttachmentInstanceOutput struct{ *pulumi.OutputState }

func (TGAttachmentInstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TGAttachmentInstance)(nil)).Elem()
}

func (o TGAttachmentInstanceOutput) ToTGAttachmentInstanceOutput() TGAttachmentInstanceOutput {
	return o
}

func (o TGAttachmentInstanceOutput) ToTGAttachmentInstanceOutputWithContext(ctx context.Context) TGAttachmentInstanceOutput {
	return o
}

// The Intranet IP of the target group instance.
func (o TGAttachmentInstanceOutput) BindIp() pulumi.StringOutput {
	return o.ApplyT(func(v *TGAttachmentInstance) pulumi.StringOutput { return v.BindIp }).(pulumi.StringOutput)
}

// Port of the target group instance.
func (o TGAttachmentInstanceOutput) Port() pulumi.IntOutput {
	return o.ApplyT(func(v *TGAttachmentInstance) pulumi.IntOutput { return v.Port }).(pulumi.IntOutput)
}

// Target group ID.
func (o TGAttachmentInstanceOutput) TargetGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *TGAttachmentInstance) pulumi.StringOutput { return v.TargetGroupId }).(pulumi.StringOutput)
}

// The weight of the target group instance.
func (o TGAttachmentInstanceOutput) Weight() pulumi.IntOutput {
	return o.ApplyT(func(v *TGAttachmentInstance) pulumi.IntOutput { return v.Weight }).(pulumi.IntOutput)
}

type TGAttachmentInstanceArrayOutput struct{ *pulumi.OutputState }

func (TGAttachmentInstanceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TGAttachmentInstance)(nil)).Elem()
}

func (o TGAttachmentInstanceArrayOutput) ToTGAttachmentInstanceArrayOutput() TGAttachmentInstanceArrayOutput {
	return o
}

func (o TGAttachmentInstanceArrayOutput) ToTGAttachmentInstanceArrayOutputWithContext(ctx context.Context) TGAttachmentInstanceArrayOutput {
	return o
}

func (o TGAttachmentInstanceArrayOutput) Index(i pulumi.IntInput) TGAttachmentInstanceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TGAttachmentInstance {
		return vs[0].([]*TGAttachmentInstance)[vs[1].(int)]
	}).(TGAttachmentInstanceOutput)
}

type TGAttachmentInstanceMapOutput struct{ *pulumi.OutputState }

func (TGAttachmentInstanceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TGAttachmentInstance)(nil)).Elem()
}

func (o TGAttachmentInstanceMapOutput) ToTGAttachmentInstanceMapOutput() TGAttachmentInstanceMapOutput {
	return o
}

func (o TGAttachmentInstanceMapOutput) ToTGAttachmentInstanceMapOutputWithContext(ctx context.Context) TGAttachmentInstanceMapOutput {
	return o
}

func (o TGAttachmentInstanceMapOutput) MapIndex(k pulumi.StringInput) TGAttachmentInstanceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TGAttachmentInstance {
		return vs[0].(map[string]*TGAttachmentInstance)[vs[1].(string)]
	}).(TGAttachmentInstanceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TGAttachmentInstanceInput)(nil)).Elem(), &TGAttachmentInstance{})
	pulumi.RegisterInputType(reflect.TypeOf((*TGAttachmentInstanceArrayInput)(nil)).Elem(), TGAttachmentInstanceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TGAttachmentInstanceMapInput)(nil)).Elem(), TGAttachmentInstanceMap{})
	pulumi.RegisterOutputType(TGAttachmentInstanceOutput{})
	pulumi.RegisterOutputType(TGAttachmentInstanceArrayOutput{})
	pulumi.RegisterOutputType(TGAttachmentInstanceMapOutput{})
}
