// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package protocol

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func TemplateGroups(ctx *pulumi.Context, args *TemplateGroupsArgs, opts ...pulumi.InvokeOption) (*TemplateGroupsResult, error) {
	var rv TemplateGroupsResult
	err := ctx.Invoke("tencentcloud:Protocol/templateGroups:TemplateGroups", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking TemplateGroups.
type TemplateGroupsArgs struct {
	Id               *string `pulumi:"id"`
	Name             *string `pulumi:"name"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by TemplateGroups.
type TemplateGroupsResult struct {
	GroupLists       []TemplateGroupsGroupList `pulumi:"groupLists"`
	Id               *string                   `pulumi:"id"`
	Name             *string                   `pulumi:"name"`
	ResultOutputFile *string                   `pulumi:"resultOutputFile"`
}

func TemplateGroupsOutput(ctx *pulumi.Context, args TemplateGroupsOutputArgs, opts ...pulumi.InvokeOption) TemplateGroupsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (TemplateGroupsResult, error) {
			args := v.(TemplateGroupsArgs)
			r, err := TemplateGroups(ctx, &args, opts...)
			var s TemplateGroupsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(TemplateGroupsResultOutput)
}

// A collection of arguments for invoking TemplateGroups.
type TemplateGroupsOutputArgs struct {
	Id               pulumi.StringPtrInput `pulumi:"id"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (TemplateGroupsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplateGroupsArgs)(nil)).Elem()
}

// A collection of values returned by TemplateGroups.
type TemplateGroupsResultOutput struct{ *pulumi.OutputState }

func (TemplateGroupsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplateGroupsResult)(nil)).Elem()
}

func (o TemplateGroupsResultOutput) ToTemplateGroupsResultOutput() TemplateGroupsResultOutput {
	return o
}

func (o TemplateGroupsResultOutput) ToTemplateGroupsResultOutputWithContext(ctx context.Context) TemplateGroupsResultOutput {
	return o
}

func (o TemplateGroupsResultOutput) GroupLists() TemplateGroupsGroupListArrayOutput {
	return o.ApplyT(func(v TemplateGroupsResult) []TemplateGroupsGroupList { return v.GroupLists }).(TemplateGroupsGroupListArrayOutput)
}

func (o TemplateGroupsResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TemplateGroupsResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o TemplateGroupsResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TemplateGroupsResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o TemplateGroupsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TemplateGroupsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(TemplateGroupsResultOutput{})
}
