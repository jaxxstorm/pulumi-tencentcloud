// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Secrets(ctx *pulumi.Context, args *SecretsArgs, opts ...pulumi.InvokeOption) (*SecretsResult, error) {
	var rv SecretsResult
	err := ctx.Invoke("tencentcloud:Ssm/secrets:Secrets", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Secrets.
type SecretsArgs struct {
	OrderType        *int                   `pulumi:"orderType"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	SecretName       *string                `pulumi:"secretName"`
	State            *int                   `pulumi:"state"`
	Tags             map[string]interface{} `pulumi:"tags"`
}

// A collection of values returned by Secrets.
type SecretsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id               string                 `pulumi:"id"`
	OrderType        *int                   `pulumi:"orderType"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	SecretLists      []SecretsSecretList    `pulumi:"secretLists"`
	SecretName       *string                `pulumi:"secretName"`
	State            *int                   `pulumi:"state"`
	Tags             map[string]interface{} `pulumi:"tags"`
}

func SecretsOutput(ctx *pulumi.Context, args SecretsOutputArgs, opts ...pulumi.InvokeOption) SecretsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (SecretsResult, error) {
			args := v.(SecretsArgs)
			r, err := Secrets(ctx, &args, opts...)
			var s SecretsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(SecretsResultOutput)
}

// A collection of arguments for invoking Secrets.
type SecretsOutputArgs struct {
	OrderType        pulumi.IntPtrInput    `pulumi:"orderType"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	SecretName       pulumi.StringPtrInput `pulumi:"secretName"`
	State            pulumi.IntPtrInput    `pulumi:"state"`
	Tags             pulumi.MapInput       `pulumi:"tags"`
}

func (SecretsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretsArgs)(nil)).Elem()
}

// A collection of values returned by Secrets.
type SecretsResultOutput struct{ *pulumi.OutputState }

func (SecretsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretsResult)(nil)).Elem()
}

func (o SecretsResultOutput) ToSecretsResultOutput() SecretsResultOutput {
	return o
}

func (o SecretsResultOutput) ToSecretsResultOutputWithContext(ctx context.Context) SecretsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o SecretsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v SecretsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o SecretsResultOutput) OrderType() pulumi.IntPtrOutput {
	return o.ApplyT(func(v SecretsResult) *int { return v.OrderType }).(pulumi.IntPtrOutput)
}

func (o SecretsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SecretsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o SecretsResultOutput) SecretLists() SecretsSecretListArrayOutput {
	return o.ApplyT(func(v SecretsResult) []SecretsSecretList { return v.SecretLists }).(SecretsSecretListArrayOutput)
}

func (o SecretsResultOutput) SecretName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SecretsResult) *string { return v.SecretName }).(pulumi.StringPtrOutput)
}

func (o SecretsResultOutput) State() pulumi.IntPtrOutput {
	return o.ApplyT(func(v SecretsResult) *int { return v.State }).(pulumi.IntPtrOutput)
}

func (o SecretsResultOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v SecretsResult) map[string]interface{} { return v.Tags }).(pulumi.MapOutput)
}

func init() {
	pulumi.RegisterOutputType(SecretsResultOutput{})
}
