// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mysql

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func DefaultParams(ctx *pulumi.Context, args *DefaultParamsArgs, opts ...pulumi.InvokeOption) (*DefaultParamsResult, error) {
	var rv DefaultParamsResult
	err := ctx.Invoke("tencentcloud:Mysql/defaultParams:DefaultParams", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking DefaultParams.
type DefaultParamsArgs struct {
	DbVersion        *string `pulumi:"dbVersion"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by DefaultParams.
type DefaultParamsResult struct {
	DbVersion *string `pulumi:"dbVersion"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                   `pulumi:"id"`
	ParamLists       []DefaultParamsParamList `pulumi:"paramLists"`
	ResultOutputFile *string                  `pulumi:"resultOutputFile"`
}

func DefaultParamsOutput(ctx *pulumi.Context, args DefaultParamsOutputArgs, opts ...pulumi.InvokeOption) DefaultParamsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (DefaultParamsResult, error) {
			args := v.(DefaultParamsArgs)
			r, err := DefaultParams(ctx, &args, opts...)
			var s DefaultParamsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(DefaultParamsResultOutput)
}

// A collection of arguments for invoking DefaultParams.
type DefaultParamsOutputArgs struct {
	DbVersion        pulumi.StringPtrInput `pulumi:"dbVersion"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (DefaultParamsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DefaultParamsArgs)(nil)).Elem()
}

// A collection of values returned by DefaultParams.
type DefaultParamsResultOutput struct{ *pulumi.OutputState }

func (DefaultParamsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DefaultParamsResult)(nil)).Elem()
}

func (o DefaultParamsResultOutput) ToDefaultParamsResultOutput() DefaultParamsResultOutput {
	return o
}

func (o DefaultParamsResultOutput) ToDefaultParamsResultOutputWithContext(ctx context.Context) DefaultParamsResultOutput {
	return o
}

func (o DefaultParamsResultOutput) DbVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DefaultParamsResult) *string { return v.DbVersion }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o DefaultParamsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v DefaultParamsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o DefaultParamsResultOutput) ParamLists() DefaultParamsParamListArrayOutput {
	return o.ApplyT(func(v DefaultParamsResult) []DefaultParamsParamList { return v.ParamLists }).(DefaultParamsParamListArrayOutput)
}

func (o DefaultParamsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DefaultParamsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(DefaultParamsResultOutput{})
}
