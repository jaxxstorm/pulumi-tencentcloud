// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func APIGatewayThrottlingApis(ctx *pulumi.Context, args *APIGatewayThrottlingApisArgs, opts ...pulumi.InvokeOption) (*APIGatewayThrottlingApisResult, error) {
	var rv APIGatewayThrottlingApisResult
	err := ctx.Invoke("tencentcloud:Cloud/aPIGatewayThrottlingApis:APIGatewayThrottlingApis", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking APIGatewayThrottlingApis.
type APIGatewayThrottlingApisArgs struct {
	EnvironmentNames []string `pulumi:"environmentNames"`
	ResultOutputFile *string  `pulumi:"resultOutputFile"`
	ServiceId        *string  `pulumi:"serviceId"`
}

// A collection of values returned by APIGatewayThrottlingApis.
type APIGatewayThrottlingApisResult struct {
	EnvironmentNames []string `pulumi:"environmentNames"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                         `pulumi:"id"`
	Lists            []APIGatewayThrottlingApisList `pulumi:"lists"`
	ResultOutputFile *string                        `pulumi:"resultOutputFile"`
	ServiceId        *string                        `pulumi:"serviceId"`
}

func APIGatewayThrottlingApisOutput(ctx *pulumi.Context, args APIGatewayThrottlingApisOutputArgs, opts ...pulumi.InvokeOption) APIGatewayThrottlingApisResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (APIGatewayThrottlingApisResult, error) {
			args := v.(APIGatewayThrottlingApisArgs)
			r, err := APIGatewayThrottlingApis(ctx, &args, opts...)
			var s APIGatewayThrottlingApisResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(APIGatewayThrottlingApisResultOutput)
}

// A collection of arguments for invoking APIGatewayThrottlingApis.
type APIGatewayThrottlingApisOutputArgs struct {
	EnvironmentNames pulumi.StringArrayInput `pulumi:"environmentNames"`
	ResultOutputFile pulumi.StringPtrInput   `pulumi:"resultOutputFile"`
	ServiceId        pulumi.StringPtrInput   `pulumi:"serviceId"`
}

func (APIGatewayThrottlingApisOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayThrottlingApisArgs)(nil)).Elem()
}

// A collection of values returned by APIGatewayThrottlingApis.
type APIGatewayThrottlingApisResultOutput struct{ *pulumi.OutputState }

func (APIGatewayThrottlingApisResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayThrottlingApisResult)(nil)).Elem()
}

func (o APIGatewayThrottlingApisResultOutput) ToAPIGatewayThrottlingApisResultOutput() APIGatewayThrottlingApisResultOutput {
	return o
}

func (o APIGatewayThrottlingApisResultOutput) ToAPIGatewayThrottlingApisResultOutputWithContext(ctx context.Context) APIGatewayThrottlingApisResultOutput {
	return o
}

func (o APIGatewayThrottlingApisResultOutput) EnvironmentNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v APIGatewayThrottlingApisResult) []string { return v.EnvironmentNames }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o APIGatewayThrottlingApisResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v APIGatewayThrottlingApisResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o APIGatewayThrottlingApisResultOutput) Lists() APIGatewayThrottlingApisListArrayOutput {
	return o.ApplyT(func(v APIGatewayThrottlingApisResult) []APIGatewayThrottlingApisList { return v.Lists }).(APIGatewayThrottlingApisListArrayOutput)
}

func (o APIGatewayThrottlingApisResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayThrottlingApisResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o APIGatewayThrottlingApisResultOutput) ServiceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayThrottlingApisResult) *string { return v.ServiceId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(APIGatewayThrottlingApisResultOutput{})
}
