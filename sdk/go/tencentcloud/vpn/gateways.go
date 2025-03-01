// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpn

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Gateways(ctx *pulumi.Context, args *GatewaysArgs, opts ...pulumi.InvokeOption) (*GatewaysResult, error) {
	var rv GatewaysResult
	err := ctx.Invoke("tencentcloud:Vpn/gateways:Gateways", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Gateways.
type GatewaysArgs struct {
	Id               *string                `pulumi:"id"`
	Name             *string                `pulumi:"name"`
	PublicIpAddress  *string                `pulumi:"publicIpAddress"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	Tags             map[string]interface{} `pulumi:"tags"`
	VpcId            *string                `pulumi:"vpcId"`
	Zone             *string                `pulumi:"zone"`
}

// A collection of values returned by Gateways.
type GatewaysResult struct {
	GatewayLists     []GatewaysGatewayList  `pulumi:"gatewayLists"`
	Id               *string                `pulumi:"id"`
	Name             *string                `pulumi:"name"`
	PublicIpAddress  *string                `pulumi:"publicIpAddress"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	Tags             map[string]interface{} `pulumi:"tags"`
	VpcId            *string                `pulumi:"vpcId"`
	Zone             *string                `pulumi:"zone"`
}

func GatewaysOutput(ctx *pulumi.Context, args GatewaysOutputArgs, opts ...pulumi.InvokeOption) GatewaysResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GatewaysResult, error) {
			args := v.(GatewaysArgs)
			r, err := Gateways(ctx, &args, opts...)
			var s GatewaysResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GatewaysResultOutput)
}

// A collection of arguments for invoking Gateways.
type GatewaysOutputArgs struct {
	Id               pulumi.StringPtrInput `pulumi:"id"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	PublicIpAddress  pulumi.StringPtrInput `pulumi:"publicIpAddress"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	Tags             pulumi.MapInput       `pulumi:"tags"`
	VpcId            pulumi.StringPtrInput `pulumi:"vpcId"`
	Zone             pulumi.StringPtrInput `pulumi:"zone"`
}

func (GatewaysOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GatewaysArgs)(nil)).Elem()
}

// A collection of values returned by Gateways.
type GatewaysResultOutput struct{ *pulumi.OutputState }

func (GatewaysResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GatewaysResult)(nil)).Elem()
}

func (o GatewaysResultOutput) ToGatewaysResultOutput() GatewaysResultOutput {
	return o
}

func (o GatewaysResultOutput) ToGatewaysResultOutputWithContext(ctx context.Context) GatewaysResultOutput {
	return o
}

func (o GatewaysResultOutput) GatewayLists() GatewaysGatewayListArrayOutput {
	return o.ApplyT(func(v GatewaysResult) []GatewaysGatewayList { return v.GatewayLists }).(GatewaysGatewayListArrayOutput)
}

func (o GatewaysResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GatewaysResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o GatewaysResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GatewaysResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GatewaysResultOutput) PublicIpAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GatewaysResult) *string { return v.PublicIpAddress }).(pulumi.StringPtrOutput)
}

func (o GatewaysResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GatewaysResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o GatewaysResultOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v GatewaysResult) map[string]interface{} { return v.Tags }).(pulumi.MapOutput)
}

func (o GatewaysResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GatewaysResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func (o GatewaysResultOutput) Zone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GatewaysResult) *string { return v.Zone }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GatewaysResultOutput{})
}
