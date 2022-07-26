// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package user

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Info(ctx *pulumi.Context, args *InfoArgs, opts ...pulumi.InvokeOption) (*InfoResult, error) {
	var rv InfoResult
	err := ctx.Invoke("tencentcloud:User/info:Info", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Info.
type InfoArgs struct {
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by Info.
type InfoResult struct {
	AppId string `pulumi:"appId"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	Name             string  `pulumi:"name"`
	OwnerUin         string  `pulumi:"ownerUin"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	Uin              string  `pulumi:"uin"`
}

func InfoOutput(ctx *pulumi.Context, args InfoOutputArgs, opts ...pulumi.InvokeOption) InfoResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (InfoResult, error) {
			args := v.(InfoArgs)
			r, err := Info(ctx, &args, opts...)
			var s InfoResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(InfoResultOutput)
}

// A collection of arguments for invoking Info.
type InfoOutputArgs struct {
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (InfoOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InfoArgs)(nil)).Elem()
}

// A collection of values returned by Info.
type InfoResultOutput struct{ *pulumi.OutputState }

func (InfoResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InfoResult)(nil)).Elem()
}

func (o InfoResultOutput) ToInfoResultOutput() InfoResultOutput {
	return o
}

func (o InfoResultOutput) ToInfoResultOutputWithContext(ctx context.Context) InfoResultOutput {
	return o
}

func (o InfoResultOutput) AppId() pulumi.StringOutput {
	return o.ApplyT(func(v InfoResult) string { return v.AppId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o InfoResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v InfoResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o InfoResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v InfoResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o InfoResultOutput) OwnerUin() pulumi.StringOutput {
	return o.ApplyT(func(v InfoResult) string { return v.OwnerUin }).(pulumi.StringOutput)
}

func (o InfoResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InfoResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o InfoResultOutput) Uin() pulumi.StringOutput {
	return o.ApplyT(func(v InfoResult) string { return v.Uin }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(InfoResultOutput{})
}
