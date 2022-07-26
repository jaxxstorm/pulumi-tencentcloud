// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sqlserver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func ReadonlyGroups(ctx *pulumi.Context, args *ReadonlyGroupsArgs, opts ...pulumi.InvokeOption) (*ReadonlyGroupsResult, error) {
	var rv ReadonlyGroupsResult
	err := ctx.Invoke("tencentcloud:Sqlserver/readonlyGroups:ReadonlyGroups", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking ReadonlyGroups.
type ReadonlyGroupsArgs struct {
	MasterInstanceId *string `pulumi:"masterInstanceId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by ReadonlyGroups.
type ReadonlyGroupsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id               string               `pulumi:"id"`
	Lists            []ReadonlyGroupsList `pulumi:"lists"`
	MasterInstanceId *string              `pulumi:"masterInstanceId"`
	ResultOutputFile *string              `pulumi:"resultOutputFile"`
}

func ReadonlyGroupsOutput(ctx *pulumi.Context, args ReadonlyGroupsOutputArgs, opts ...pulumi.InvokeOption) ReadonlyGroupsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ReadonlyGroupsResult, error) {
			args := v.(ReadonlyGroupsArgs)
			r, err := ReadonlyGroups(ctx, &args, opts...)
			var s ReadonlyGroupsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(ReadonlyGroupsResultOutput)
}

// A collection of arguments for invoking ReadonlyGroups.
type ReadonlyGroupsOutputArgs struct {
	MasterInstanceId pulumi.StringPtrInput `pulumi:"masterInstanceId"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (ReadonlyGroupsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ReadonlyGroupsArgs)(nil)).Elem()
}

// A collection of values returned by ReadonlyGroups.
type ReadonlyGroupsResultOutput struct{ *pulumi.OutputState }

func (ReadonlyGroupsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ReadonlyGroupsResult)(nil)).Elem()
}

func (o ReadonlyGroupsResultOutput) ToReadonlyGroupsResultOutput() ReadonlyGroupsResultOutput {
	return o
}

func (o ReadonlyGroupsResultOutput) ToReadonlyGroupsResultOutputWithContext(ctx context.Context) ReadonlyGroupsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o ReadonlyGroupsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v ReadonlyGroupsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o ReadonlyGroupsResultOutput) Lists() ReadonlyGroupsListArrayOutput {
	return o.ApplyT(func(v ReadonlyGroupsResult) []ReadonlyGroupsList { return v.Lists }).(ReadonlyGroupsListArrayOutput)
}

func (o ReadonlyGroupsResultOutput) MasterInstanceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ReadonlyGroupsResult) *string { return v.MasterInstanceId }).(pulumi.StringPtrOutput)
}

func (o ReadonlyGroupsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ReadonlyGroupsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ReadonlyGroupsResultOutput{})
}
