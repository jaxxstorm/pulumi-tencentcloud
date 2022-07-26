// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Instances(ctx *pulumi.Context, args *InstancesArgs, opts ...pulumi.InvokeOption) (*InstancesResult, error) {
	var rv InstancesResult
	err := ctx.Invoke("tencentcloud:Clb/instances:Instances", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Instances.
type InstancesArgs struct {
	ClbId            *string `pulumi:"clbId"`
	ClbName          *string `pulumi:"clbName"`
	MasterZone       *string `pulumi:"masterZone"`
	NetworkType      *string `pulumi:"networkType"`
	ProjectId        *int    `pulumi:"projectId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by Instances.
type InstancesResult struct {
	ClbId    *string            `pulumi:"clbId"`
	ClbLists []InstancesClbList `pulumi:"clbLists"`
	ClbName  *string            `pulumi:"clbName"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	MasterZone       *string `pulumi:"masterZone"`
	NetworkType      *string `pulumi:"networkType"`
	ProjectId        *int    `pulumi:"projectId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

func InstancesOutput(ctx *pulumi.Context, args InstancesOutputArgs, opts ...pulumi.InvokeOption) InstancesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (InstancesResult, error) {
			args := v.(InstancesArgs)
			r, err := Instances(ctx, &args, opts...)
			var s InstancesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(InstancesResultOutput)
}

// A collection of arguments for invoking Instances.
type InstancesOutputArgs struct {
	ClbId            pulumi.StringPtrInput `pulumi:"clbId"`
	ClbName          pulumi.StringPtrInput `pulumi:"clbName"`
	MasterZone       pulumi.StringPtrInput `pulumi:"masterZone"`
	NetworkType      pulumi.StringPtrInput `pulumi:"networkType"`
	ProjectId        pulumi.IntPtrInput    `pulumi:"projectId"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (InstancesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstancesArgs)(nil)).Elem()
}

// A collection of values returned by Instances.
type InstancesResultOutput struct{ *pulumi.OutputState }

func (InstancesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstancesResult)(nil)).Elem()
}

func (o InstancesResultOutput) ToInstancesResultOutput() InstancesResultOutput {
	return o
}

func (o InstancesResultOutput) ToInstancesResultOutputWithContext(ctx context.Context) InstancesResultOutput {
	return o
}

func (o InstancesResultOutput) ClbId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.ClbId }).(pulumi.StringPtrOutput)
}

func (o InstancesResultOutput) ClbLists() InstancesClbListArrayOutput {
	return o.ApplyT(func(v InstancesResult) []InstancesClbList { return v.ClbLists }).(InstancesClbListArrayOutput)
}

func (o InstancesResultOutput) ClbName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.ClbName }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o InstancesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v InstancesResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o InstancesResultOutput) MasterZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.MasterZone }).(pulumi.StringPtrOutput)
}

func (o InstancesResultOutput) NetworkType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.NetworkType }).(pulumi.StringPtrOutput)
}

func (o InstancesResultOutput) ProjectId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v InstancesResult) *int { return v.ProjectId }).(pulumi.IntPtrOutput)
}

func (o InstancesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(InstancesResultOutput{})
}
