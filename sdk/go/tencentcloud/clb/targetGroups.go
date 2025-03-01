// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func TargetGroups(ctx *pulumi.Context, args *TargetGroupsArgs, opts ...pulumi.InvokeOption) (*TargetGroupsResult, error) {
	var rv TargetGroupsResult
	err := ctx.Invoke("tencentcloud:Clb/targetGroups:TargetGroups", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking TargetGroups.
type TargetGroupsArgs struct {
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	TargetGroupId    *string `pulumi:"targetGroupId"`
	TargetGroupName  *string `pulumi:"targetGroupName"`
	VpcId            *string `pulumi:"vpcId"`
}

// A collection of values returned by TargetGroups.
type TargetGroupsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id               string             `pulumi:"id"`
	Lists            []TargetGroupsList `pulumi:"lists"`
	ResultOutputFile *string            `pulumi:"resultOutputFile"`
	TargetGroupId    *string            `pulumi:"targetGroupId"`
	TargetGroupName  *string            `pulumi:"targetGroupName"`
	VpcId            *string            `pulumi:"vpcId"`
}

func TargetGroupsOutput(ctx *pulumi.Context, args TargetGroupsOutputArgs, opts ...pulumi.InvokeOption) TargetGroupsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (TargetGroupsResult, error) {
			args := v.(TargetGroupsArgs)
			r, err := TargetGroups(ctx, &args, opts...)
			var s TargetGroupsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(TargetGroupsResultOutput)
}

// A collection of arguments for invoking TargetGroups.
type TargetGroupsOutputArgs struct {
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	TargetGroupId    pulumi.StringPtrInput `pulumi:"targetGroupId"`
	TargetGroupName  pulumi.StringPtrInput `pulumi:"targetGroupName"`
	VpcId            pulumi.StringPtrInput `pulumi:"vpcId"`
}

func (TargetGroupsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TargetGroupsArgs)(nil)).Elem()
}

// A collection of values returned by TargetGroups.
type TargetGroupsResultOutput struct{ *pulumi.OutputState }

func (TargetGroupsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TargetGroupsResult)(nil)).Elem()
}

func (o TargetGroupsResultOutput) ToTargetGroupsResultOutput() TargetGroupsResultOutput {
	return o
}

func (o TargetGroupsResultOutput) ToTargetGroupsResultOutputWithContext(ctx context.Context) TargetGroupsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o TargetGroupsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v TargetGroupsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o TargetGroupsResultOutput) Lists() TargetGroupsListArrayOutput {
	return o.ApplyT(func(v TargetGroupsResult) []TargetGroupsList { return v.Lists }).(TargetGroupsListArrayOutput)
}

func (o TargetGroupsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TargetGroupsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o TargetGroupsResultOutput) TargetGroupId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TargetGroupsResult) *string { return v.TargetGroupId }).(pulumi.StringPtrOutput)
}

func (o TargetGroupsResultOutput) TargetGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TargetGroupsResult) *string { return v.TargetGroupName }).(pulumi.StringPtrOutput)
}

func (o TargetGroupsResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TargetGroupsResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(TargetGroupsResultOutput{})
}
