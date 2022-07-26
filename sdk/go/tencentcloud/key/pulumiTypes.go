// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package key

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type PairsKeyPairList struct {
	CreateTime string `pulumi:"createTime"`
	KeyId      string `pulumi:"keyId"`
	KeyName    string `pulumi:"keyName"`
	ProjectId  int    `pulumi:"projectId"`
	PublicKey  string `pulumi:"publicKey"`
}

// PairsKeyPairListInput is an input type that accepts PairsKeyPairListArgs and PairsKeyPairListOutput values.
// You can construct a concrete instance of `PairsKeyPairListInput` via:
//
//          PairsKeyPairListArgs{...}
type PairsKeyPairListInput interface {
	pulumi.Input

	ToPairsKeyPairListOutput() PairsKeyPairListOutput
	ToPairsKeyPairListOutputWithContext(context.Context) PairsKeyPairListOutput
}

type PairsKeyPairListArgs struct {
	CreateTime pulumi.StringInput `pulumi:"createTime"`
	KeyId      pulumi.StringInput `pulumi:"keyId"`
	KeyName    pulumi.StringInput `pulumi:"keyName"`
	ProjectId  pulumi.IntInput    `pulumi:"projectId"`
	PublicKey  pulumi.StringInput `pulumi:"publicKey"`
}

func (PairsKeyPairListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PairsKeyPairList)(nil)).Elem()
}

func (i PairsKeyPairListArgs) ToPairsKeyPairListOutput() PairsKeyPairListOutput {
	return i.ToPairsKeyPairListOutputWithContext(context.Background())
}

func (i PairsKeyPairListArgs) ToPairsKeyPairListOutputWithContext(ctx context.Context) PairsKeyPairListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PairsKeyPairListOutput)
}

// PairsKeyPairListArrayInput is an input type that accepts PairsKeyPairListArray and PairsKeyPairListArrayOutput values.
// You can construct a concrete instance of `PairsKeyPairListArrayInput` via:
//
//          PairsKeyPairListArray{ PairsKeyPairListArgs{...} }
type PairsKeyPairListArrayInput interface {
	pulumi.Input

	ToPairsKeyPairListArrayOutput() PairsKeyPairListArrayOutput
	ToPairsKeyPairListArrayOutputWithContext(context.Context) PairsKeyPairListArrayOutput
}

type PairsKeyPairListArray []PairsKeyPairListInput

func (PairsKeyPairListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PairsKeyPairList)(nil)).Elem()
}

func (i PairsKeyPairListArray) ToPairsKeyPairListArrayOutput() PairsKeyPairListArrayOutput {
	return i.ToPairsKeyPairListArrayOutputWithContext(context.Background())
}

func (i PairsKeyPairListArray) ToPairsKeyPairListArrayOutputWithContext(ctx context.Context) PairsKeyPairListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PairsKeyPairListArrayOutput)
}

type PairsKeyPairListOutput struct{ *pulumi.OutputState }

func (PairsKeyPairListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PairsKeyPairList)(nil)).Elem()
}

func (o PairsKeyPairListOutput) ToPairsKeyPairListOutput() PairsKeyPairListOutput {
	return o
}

func (o PairsKeyPairListOutput) ToPairsKeyPairListOutputWithContext(ctx context.Context) PairsKeyPairListOutput {
	return o
}

func (o PairsKeyPairListOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v PairsKeyPairList) string { return v.CreateTime }).(pulumi.StringOutput)
}

func (o PairsKeyPairListOutput) KeyId() pulumi.StringOutput {
	return o.ApplyT(func(v PairsKeyPairList) string { return v.KeyId }).(pulumi.StringOutput)
}

func (o PairsKeyPairListOutput) KeyName() pulumi.StringOutput {
	return o.ApplyT(func(v PairsKeyPairList) string { return v.KeyName }).(pulumi.StringOutput)
}

func (o PairsKeyPairListOutput) ProjectId() pulumi.IntOutput {
	return o.ApplyT(func(v PairsKeyPairList) int { return v.ProjectId }).(pulumi.IntOutput)
}

func (o PairsKeyPairListOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v PairsKeyPairList) string { return v.PublicKey }).(pulumi.StringOutput)
}

type PairsKeyPairListArrayOutput struct{ *pulumi.OutputState }

func (PairsKeyPairListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PairsKeyPairList)(nil)).Elem()
}

func (o PairsKeyPairListArrayOutput) ToPairsKeyPairListArrayOutput() PairsKeyPairListArrayOutput {
	return o
}

func (o PairsKeyPairListArrayOutput) ToPairsKeyPairListArrayOutputWithContext(ctx context.Context) PairsKeyPairListArrayOutput {
	return o
}

func (o PairsKeyPairListArrayOutput) Index(i pulumi.IntInput) PairsKeyPairListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PairsKeyPairList {
		return vs[0].([]PairsKeyPairList)[vs[1].(int)]
	}).(PairsKeyPairListOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PairsKeyPairListInput)(nil)).Elem(), PairsKeyPairListArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PairsKeyPairListArrayInput)(nil)).Elem(), PairsKeyPairListArray{})
	pulumi.RegisterOutputType(PairsKeyPairListOutput{})
	pulumi.RegisterOutputType(PairsKeyPairListArrayOutput{})
}
