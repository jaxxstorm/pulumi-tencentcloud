// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func APIGatewayUsagePlanEnvironments(ctx *pulumi.Context, args *APIGatewayUsagePlanEnvironmentsArgs, opts ...pulumi.InvokeOption) (*APIGatewayUsagePlanEnvironmentsResult, error) {
	var rv APIGatewayUsagePlanEnvironmentsResult
	err := ctx.Invoke("tencentcloud:Cloud/aPIGatewayUsagePlanEnvironments:APIGatewayUsagePlanEnvironments", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking APIGatewayUsagePlanEnvironments.
type APIGatewayUsagePlanEnvironmentsArgs struct {
	BindType         *string `pulumi:"bindType"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	UsagePlanId      string  `pulumi:"usagePlanId"`
}

// A collection of values returned by APIGatewayUsagePlanEnvironments.
type APIGatewayUsagePlanEnvironmentsResult struct {
	BindType *string `pulumi:"bindType"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                                `pulumi:"id"`
	Lists            []APIGatewayUsagePlanEnvironmentsList `pulumi:"lists"`
	ResultOutputFile *string                               `pulumi:"resultOutputFile"`
	UsagePlanId      string                                `pulumi:"usagePlanId"`
}

func APIGatewayUsagePlanEnvironmentsOutput(ctx *pulumi.Context, args APIGatewayUsagePlanEnvironmentsOutputArgs, opts ...pulumi.InvokeOption) APIGatewayUsagePlanEnvironmentsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (APIGatewayUsagePlanEnvironmentsResult, error) {
			args := v.(APIGatewayUsagePlanEnvironmentsArgs)
			r, err := APIGatewayUsagePlanEnvironments(ctx, &args, opts...)
			var s APIGatewayUsagePlanEnvironmentsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(APIGatewayUsagePlanEnvironmentsResultOutput)
}

// A collection of arguments for invoking APIGatewayUsagePlanEnvironments.
type APIGatewayUsagePlanEnvironmentsOutputArgs struct {
	BindType         pulumi.StringPtrInput `pulumi:"bindType"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	UsagePlanId      pulumi.StringInput    `pulumi:"usagePlanId"`
}

func (APIGatewayUsagePlanEnvironmentsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayUsagePlanEnvironmentsArgs)(nil)).Elem()
}

// A collection of values returned by APIGatewayUsagePlanEnvironments.
type APIGatewayUsagePlanEnvironmentsResultOutput struct{ *pulumi.OutputState }

func (APIGatewayUsagePlanEnvironmentsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayUsagePlanEnvironmentsResult)(nil)).Elem()
}

func (o APIGatewayUsagePlanEnvironmentsResultOutput) ToAPIGatewayUsagePlanEnvironmentsResultOutput() APIGatewayUsagePlanEnvironmentsResultOutput {
	return o
}

func (o APIGatewayUsagePlanEnvironmentsResultOutput) ToAPIGatewayUsagePlanEnvironmentsResultOutputWithContext(ctx context.Context) APIGatewayUsagePlanEnvironmentsResultOutput {
	return o
}

func (o APIGatewayUsagePlanEnvironmentsResultOutput) BindType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayUsagePlanEnvironmentsResult) *string { return v.BindType }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o APIGatewayUsagePlanEnvironmentsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v APIGatewayUsagePlanEnvironmentsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o APIGatewayUsagePlanEnvironmentsResultOutput) Lists() APIGatewayUsagePlanEnvironmentsListArrayOutput {
	return o.ApplyT(func(v APIGatewayUsagePlanEnvironmentsResult) []APIGatewayUsagePlanEnvironmentsList { return v.Lists }).(APIGatewayUsagePlanEnvironmentsListArrayOutput)
}

func (o APIGatewayUsagePlanEnvironmentsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayUsagePlanEnvironmentsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o APIGatewayUsagePlanEnvironmentsResultOutput) UsagePlanId() pulumi.StringOutput {
	return o.ApplyT(func(v APIGatewayUsagePlanEnvironmentsResult) string { return v.UsagePlanId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(APIGatewayUsagePlanEnvironmentsResultOutput{})
}
