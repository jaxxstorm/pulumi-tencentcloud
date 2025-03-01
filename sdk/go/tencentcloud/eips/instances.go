// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package eips

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Instances(ctx *pulumi.Context, args *InstancesArgs, opts ...pulumi.InvokeOption) (*InstancesResult, error) {
	var rv InstancesResult
	err := ctx.Invoke("tencentcloud:Eips/instances:Instances", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Instances.
type InstancesArgs struct {
	EipId            *string                `pulumi:"eipId"`
	EipName          *string                `pulumi:"eipName"`
	PublicIp         *string                `pulumi:"publicIp"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	Tags             map[string]interface{} `pulumi:"tags"`
}

// A collection of values returned by Instances.
type InstancesResult struct {
	EipId    *string            `pulumi:"eipId"`
	EipLists []InstancesEipList `pulumi:"eipLists"`
	EipName  *string            `pulumi:"eipName"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                 `pulumi:"id"`
	PublicIp         *string                `pulumi:"publicIp"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	Tags             map[string]interface{} `pulumi:"tags"`
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
	EipId            pulumi.StringPtrInput `pulumi:"eipId"`
	EipName          pulumi.StringPtrInput `pulumi:"eipName"`
	PublicIp         pulumi.StringPtrInput `pulumi:"publicIp"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	Tags             pulumi.MapInput       `pulumi:"tags"`
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

func (o InstancesResultOutput) EipId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.EipId }).(pulumi.StringPtrOutput)
}

func (o InstancesResultOutput) EipLists() InstancesEipListArrayOutput {
	return o.ApplyT(func(v InstancesResult) []InstancesEipList { return v.EipLists }).(InstancesEipListArrayOutput)
}

func (o InstancesResultOutput) EipName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.EipName }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o InstancesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v InstancesResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o InstancesResultOutput) PublicIp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.PublicIp }).(pulumi.StringPtrOutput)
}

func (o InstancesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstancesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o InstancesResultOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v InstancesResult) map[string]interface{} { return v.Tags }).(pulumi.MapOutput)
}

func init() {
	pulumi.RegisterOutputType(InstancesResultOutput{})
}
