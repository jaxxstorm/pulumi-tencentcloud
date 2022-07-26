// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package address

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Templates(ctx *pulumi.Context, args *TemplatesArgs, opts ...pulumi.InvokeOption) (*TemplatesResult, error) {
	var rv TemplatesResult
	err := ctx.Invoke("tencentcloud:Address/templates:Templates", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Templates.
type TemplatesArgs struct {
	Id               *string `pulumi:"id"`
	Name             *string `pulumi:"name"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by Templates.
type TemplatesResult struct {
	Id               *string                 `pulumi:"id"`
	Name             *string                 `pulumi:"name"`
	ResultOutputFile *string                 `pulumi:"resultOutputFile"`
	TemplateLists    []TemplatesTemplateList `pulumi:"templateLists"`
}

func TemplatesOutput(ctx *pulumi.Context, args TemplatesOutputArgs, opts ...pulumi.InvokeOption) TemplatesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (TemplatesResult, error) {
			args := v.(TemplatesArgs)
			r, err := Templates(ctx, &args, opts...)
			var s TemplatesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(TemplatesResultOutput)
}

// A collection of arguments for invoking Templates.
type TemplatesOutputArgs struct {
	Id               pulumi.StringPtrInput `pulumi:"id"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (TemplatesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplatesArgs)(nil)).Elem()
}

// A collection of values returned by Templates.
type TemplatesResultOutput struct{ *pulumi.OutputState }

func (TemplatesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplatesResult)(nil)).Elem()
}

func (o TemplatesResultOutput) ToTemplatesResultOutput() TemplatesResultOutput {
	return o
}

func (o TemplatesResultOutput) ToTemplatesResultOutputWithContext(ctx context.Context) TemplatesResultOutput {
	return o
}

func (o TemplatesResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TemplatesResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o TemplatesResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TemplatesResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o TemplatesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TemplatesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o TemplatesResultOutput) TemplateLists() TemplatesTemplateListArrayOutput {
	return o.ApplyT(func(v TemplatesResult) []TemplatesTemplateList { return v.TemplateLists }).(TemplatesTemplateListArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(TemplatesResultOutput{})
}
