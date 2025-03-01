// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func APIGatewayIpStrategy(ctx *pulumi.Context, args *APIGatewayIpStrategyArgs, opts ...pulumi.InvokeOption) (*APIGatewayIpStrategyResult, error) {
	var rv APIGatewayIpStrategyResult
	err := ctx.Invoke("tencentcloud:Cloud/aPIGatewayIpStrategy:APIGatewayIpStrategy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking APIGatewayIpStrategy.
type APIGatewayIpStrategyArgs struct {
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	ServiceId        string  `pulumi:"serviceId"`
	StrategyName     *string `pulumi:"strategyName"`
}

// A collection of values returned by APIGatewayIpStrategy.
type APIGatewayIpStrategyResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id               string                     `pulumi:"id"`
	Lists            []APIGatewayIpStrategyList `pulumi:"lists"`
	ResultOutputFile *string                    `pulumi:"resultOutputFile"`
	ServiceId        string                     `pulumi:"serviceId"`
	StrategyName     *string                    `pulumi:"strategyName"`
}

func APIGatewayIpStrategyOutput(ctx *pulumi.Context, args APIGatewayIpStrategyOutputArgs, opts ...pulumi.InvokeOption) APIGatewayIpStrategyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (APIGatewayIpStrategyResult, error) {
			args := v.(APIGatewayIpStrategyArgs)
			r, err := APIGatewayIpStrategy(ctx, &args, opts...)
			var s APIGatewayIpStrategyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(APIGatewayIpStrategyResultOutput)
}

// A collection of arguments for invoking APIGatewayIpStrategy.
type APIGatewayIpStrategyOutputArgs struct {
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	ServiceId        pulumi.StringInput    `pulumi:"serviceId"`
	StrategyName     pulumi.StringPtrInput `pulumi:"strategyName"`
}

func (APIGatewayIpStrategyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayIpStrategyArgs)(nil)).Elem()
}

// A collection of values returned by APIGatewayIpStrategy.
type APIGatewayIpStrategyResultOutput struct{ *pulumi.OutputState }

func (APIGatewayIpStrategyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayIpStrategyResult)(nil)).Elem()
}

func (o APIGatewayIpStrategyResultOutput) ToAPIGatewayIpStrategyResultOutput() APIGatewayIpStrategyResultOutput {
	return o
}

func (o APIGatewayIpStrategyResultOutput) ToAPIGatewayIpStrategyResultOutputWithContext(ctx context.Context) APIGatewayIpStrategyResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o APIGatewayIpStrategyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v APIGatewayIpStrategyResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o APIGatewayIpStrategyResultOutput) Lists() APIGatewayIpStrategyListArrayOutput {
	return o.ApplyT(func(v APIGatewayIpStrategyResult) []APIGatewayIpStrategyList { return v.Lists }).(APIGatewayIpStrategyListArrayOutput)
}

func (o APIGatewayIpStrategyResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayIpStrategyResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o APIGatewayIpStrategyResultOutput) ServiceId() pulumi.StringOutput {
	return o.ApplyT(func(v APIGatewayIpStrategyResult) string { return v.ServiceId }).(pulumi.StringOutput)
}

func (o APIGatewayIpStrategyResultOutput) StrategyName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayIpStrategyResult) *string { return v.StrategyName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(APIGatewayIpStrategyResultOutput{})
}
