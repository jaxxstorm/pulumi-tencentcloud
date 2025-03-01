// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func APIGatewayAPIKeys(ctx *pulumi.Context, args *APIGatewayAPIKeysArgs, opts ...pulumi.InvokeOption) (*APIGatewayAPIKeysResult, error) {
	var rv APIGatewayAPIKeysResult
	err := ctx.Invoke("tencentcloud:Cloud/aPIGatewayAPIKeys:APIGatewayAPIKeys", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking APIGatewayAPIKeys.
type APIGatewayAPIKeysArgs struct {
	ApiKeyId         *string `pulumi:"apiKeyId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	SecretName       *string `pulumi:"secretName"`
}

// A collection of values returned by APIGatewayAPIKeys.
type APIGatewayAPIKeysResult struct {
	ApiKeyId *string `pulumi:"apiKeyId"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                  `pulumi:"id"`
	Lists            []APIGatewayAPIKeysList `pulumi:"lists"`
	ResultOutputFile *string                 `pulumi:"resultOutputFile"`
	SecretName       *string                 `pulumi:"secretName"`
}

func APIGatewayAPIKeysOutput(ctx *pulumi.Context, args APIGatewayAPIKeysOutputArgs, opts ...pulumi.InvokeOption) APIGatewayAPIKeysResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (APIGatewayAPIKeysResult, error) {
			args := v.(APIGatewayAPIKeysArgs)
			r, err := APIGatewayAPIKeys(ctx, &args, opts...)
			var s APIGatewayAPIKeysResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(APIGatewayAPIKeysResultOutput)
}

// A collection of arguments for invoking APIGatewayAPIKeys.
type APIGatewayAPIKeysOutputArgs struct {
	ApiKeyId         pulumi.StringPtrInput `pulumi:"apiKeyId"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	SecretName       pulumi.StringPtrInput `pulumi:"secretName"`
}

func (APIGatewayAPIKeysOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayAPIKeysArgs)(nil)).Elem()
}

// A collection of values returned by APIGatewayAPIKeys.
type APIGatewayAPIKeysResultOutput struct{ *pulumi.OutputState }

func (APIGatewayAPIKeysResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*APIGatewayAPIKeysResult)(nil)).Elem()
}

func (o APIGatewayAPIKeysResultOutput) ToAPIGatewayAPIKeysResultOutput() APIGatewayAPIKeysResultOutput {
	return o
}

func (o APIGatewayAPIKeysResultOutput) ToAPIGatewayAPIKeysResultOutputWithContext(ctx context.Context) APIGatewayAPIKeysResultOutput {
	return o
}

func (o APIGatewayAPIKeysResultOutput) ApiKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayAPIKeysResult) *string { return v.ApiKeyId }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o APIGatewayAPIKeysResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v APIGatewayAPIKeysResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o APIGatewayAPIKeysResultOutput) Lists() APIGatewayAPIKeysListArrayOutput {
	return o.ApplyT(func(v APIGatewayAPIKeysResult) []APIGatewayAPIKeysList { return v.Lists }).(APIGatewayAPIKeysListArrayOutput)
}

func (o APIGatewayAPIKeysResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayAPIKeysResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o APIGatewayAPIKeysResultOutput) SecretName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v APIGatewayAPIKeysResult) *string { return v.SecretName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(APIGatewayAPIKeysResultOutput{})
}
