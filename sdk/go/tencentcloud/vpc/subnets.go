// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpc

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Subnets(ctx *pulumi.Context, args *SubnetsArgs, opts ...pulumi.InvokeOption) (*SubnetsResult, error) {
	var rv SubnetsResult
	err := ctx.Invoke("tencentcloud:Vpc/subnets:Subnets", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Subnets.
type SubnetsArgs struct {
	AvailabilityZone *string                `pulumi:"availabilityZone"`
	CidrBlock        *string                `pulumi:"cidrBlock"`
	IsDefault        *bool                  `pulumi:"isDefault"`
	IsRemoteVpcSnat  *bool                  `pulumi:"isRemoteVpcSnat"`
	Name             *string                `pulumi:"name"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	SubnetId         *string                `pulumi:"subnetId"`
	TagKey           *string                `pulumi:"tagKey"`
	Tags             map[string]interface{} `pulumi:"tags"`
	VpcId            *string                `pulumi:"vpcId"`
}

// A collection of values returned by Subnets.
type SubnetsResult struct {
	AvailabilityZone *string `pulumi:"availabilityZone"`
	CidrBlock        *string `pulumi:"cidrBlock"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                 `pulumi:"id"`
	InstanceLists    []SubnetsInstanceList  `pulumi:"instanceLists"`
	IsDefault        *bool                  `pulumi:"isDefault"`
	IsRemoteVpcSnat  *bool                  `pulumi:"isRemoteVpcSnat"`
	Name             *string                `pulumi:"name"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	SubnetId         *string                `pulumi:"subnetId"`
	TagKey           *string                `pulumi:"tagKey"`
	Tags             map[string]interface{} `pulumi:"tags"`
	VpcId            *string                `pulumi:"vpcId"`
}

func SubnetsOutput(ctx *pulumi.Context, args SubnetsOutputArgs, opts ...pulumi.InvokeOption) SubnetsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (SubnetsResult, error) {
			args := v.(SubnetsArgs)
			r, err := Subnets(ctx, &args, opts...)
			var s SubnetsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(SubnetsResultOutput)
}

// A collection of arguments for invoking Subnets.
type SubnetsOutputArgs struct {
	AvailabilityZone pulumi.StringPtrInput `pulumi:"availabilityZone"`
	CidrBlock        pulumi.StringPtrInput `pulumi:"cidrBlock"`
	IsDefault        pulumi.BoolPtrInput   `pulumi:"isDefault"`
	IsRemoteVpcSnat  pulumi.BoolPtrInput   `pulumi:"isRemoteVpcSnat"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	SubnetId         pulumi.StringPtrInput `pulumi:"subnetId"`
	TagKey           pulumi.StringPtrInput `pulumi:"tagKey"`
	Tags             pulumi.MapInput       `pulumi:"tags"`
	VpcId            pulumi.StringPtrInput `pulumi:"vpcId"`
}

func (SubnetsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SubnetsArgs)(nil)).Elem()
}

// A collection of values returned by Subnets.
type SubnetsResultOutput struct{ *pulumi.OutputState }

func (SubnetsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SubnetsResult)(nil)).Elem()
}

func (o SubnetsResultOutput) ToSubnetsResultOutput() SubnetsResultOutput {
	return o
}

func (o SubnetsResultOutput) ToSubnetsResultOutputWithContext(ctx context.Context) SubnetsResultOutput {
	return o
}

func (o SubnetsResultOutput) AvailabilityZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *string { return v.AvailabilityZone }).(pulumi.StringPtrOutput)
}

func (o SubnetsResultOutput) CidrBlock() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *string { return v.CidrBlock }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o SubnetsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v SubnetsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o SubnetsResultOutput) InstanceLists() SubnetsInstanceListArrayOutput {
	return o.ApplyT(func(v SubnetsResult) []SubnetsInstanceList { return v.InstanceLists }).(SubnetsInstanceListArrayOutput)
}

func (o SubnetsResultOutput) IsDefault() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *bool { return v.IsDefault }).(pulumi.BoolPtrOutput)
}

func (o SubnetsResultOutput) IsRemoteVpcSnat() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *bool { return v.IsRemoteVpcSnat }).(pulumi.BoolPtrOutput)
}

func (o SubnetsResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o SubnetsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o SubnetsResultOutput) SubnetId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *string { return v.SubnetId }).(pulumi.StringPtrOutput)
}

func (o SubnetsResultOutput) TagKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *string { return v.TagKey }).(pulumi.StringPtrOutput)
}

func (o SubnetsResultOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v SubnetsResult) map[string]interface{} { return v.Tags }).(pulumi.MapOutput)
}

func (o SubnetsResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SubnetsResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(SubnetsResultOutput{})
}
