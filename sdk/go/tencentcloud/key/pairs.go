// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package key

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Pairs(ctx *pulumi.Context, args *PairsArgs, opts ...pulumi.InvokeOption) (*PairsResult, error) {
	var rv PairsResult
	err := ctx.Invoke("tencentcloud:Key/pairs:Pairs", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Pairs.
type PairsArgs struct {
	KeyId            *string `pulumi:"keyId"`
	KeyName          *string `pulumi:"keyName"`
	ProjectId        *int    `pulumi:"projectId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by Pairs.
type PairsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id               string             `pulumi:"id"`
	KeyId            *string            `pulumi:"keyId"`
	KeyName          *string            `pulumi:"keyName"`
	KeyPairLists     []PairsKeyPairList `pulumi:"keyPairLists"`
	ProjectId        *int               `pulumi:"projectId"`
	ResultOutputFile *string            `pulumi:"resultOutputFile"`
}

func PairsOutput(ctx *pulumi.Context, args PairsOutputArgs, opts ...pulumi.InvokeOption) PairsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (PairsResult, error) {
			args := v.(PairsArgs)
			r, err := Pairs(ctx, &args, opts...)
			var s PairsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(PairsResultOutput)
}

// A collection of arguments for invoking Pairs.
type PairsOutputArgs struct {
	KeyId            pulumi.StringPtrInput `pulumi:"keyId"`
	KeyName          pulumi.StringPtrInput `pulumi:"keyName"`
	ProjectId        pulumi.IntPtrInput    `pulumi:"projectId"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (PairsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PairsArgs)(nil)).Elem()
}

// A collection of values returned by Pairs.
type PairsResultOutput struct{ *pulumi.OutputState }

func (PairsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PairsResult)(nil)).Elem()
}

func (o PairsResultOutput) ToPairsResultOutput() PairsResultOutput {
	return o
}

func (o PairsResultOutput) ToPairsResultOutputWithContext(ctx context.Context) PairsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o PairsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v PairsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o PairsResultOutput) KeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v PairsResult) *string { return v.KeyId }).(pulumi.StringPtrOutput)
}

func (o PairsResultOutput) KeyName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v PairsResult) *string { return v.KeyName }).(pulumi.StringPtrOutput)
}

func (o PairsResultOutput) KeyPairLists() PairsKeyPairListArrayOutput {
	return o.ApplyT(func(v PairsResult) []PairsKeyPairList { return v.KeyPairLists }).(PairsKeyPairListArrayOutput)
}

func (o PairsResultOutput) ProjectId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v PairsResult) *int { return v.ProjectId }).(pulumi.IntPtrOutput)
}

func (o PairsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v PairsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(PairsResultOutput{})
}
