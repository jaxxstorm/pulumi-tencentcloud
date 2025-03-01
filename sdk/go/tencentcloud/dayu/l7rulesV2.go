// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dayu

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func L7RulesV2(ctx *pulumi.Context, args *L7RulesV2Args, opts ...pulumi.InvokeOption) (*L7RulesV2Result, error) {
	var rv L7RulesV2Result
	err := ctx.Invoke("tencentcloud:Dayu/l7RulesV2:L7RulesV2", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking L7RulesV2.
type L7RulesV2Args struct {
	Business         string  `pulumi:"business"`
	Domain           *string `pulumi:"domain"`
	Ip               *string `pulumi:"ip"`
	Limit            *int    `pulumi:"limit"`
	Offset           *int    `pulumi:"offset"`
	Protocol         *string `pulumi:"protocol"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by L7RulesV2.
type L7RulesV2Result struct {
	Business string  `pulumi:"business"`
	Domain   *string `pulumi:"domain"`
	// The provider-assigned unique ID for this managed resource.
	Id               string          `pulumi:"id"`
	Ip               *string         `pulumi:"ip"`
	Limit            *int            `pulumi:"limit"`
	Lists            []L7RulesV2List `pulumi:"lists"`
	Offset           *int            `pulumi:"offset"`
	Protocol         *string         `pulumi:"protocol"`
	ResultOutputFile *string         `pulumi:"resultOutputFile"`
}

func L7RulesV2Output(ctx *pulumi.Context, args L7RulesV2OutputArgs, opts ...pulumi.InvokeOption) L7RulesV2ResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (L7RulesV2Result, error) {
			args := v.(L7RulesV2Args)
			r, err := L7RulesV2(ctx, &args, opts...)
			var s L7RulesV2Result
			if r != nil {
				s = *r
			}
			return s, err
		}).(L7RulesV2ResultOutput)
}

// A collection of arguments for invoking L7RulesV2.
type L7RulesV2OutputArgs struct {
	Business         pulumi.StringInput    `pulumi:"business"`
	Domain           pulumi.StringPtrInput `pulumi:"domain"`
	Ip               pulumi.StringPtrInput `pulumi:"ip"`
	Limit            pulumi.IntPtrInput    `pulumi:"limit"`
	Offset           pulumi.IntPtrInput    `pulumi:"offset"`
	Protocol         pulumi.StringPtrInput `pulumi:"protocol"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (L7RulesV2OutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*L7RulesV2Args)(nil)).Elem()
}

// A collection of values returned by L7RulesV2.
type L7RulesV2ResultOutput struct{ *pulumi.OutputState }

func (L7RulesV2ResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*L7RulesV2Result)(nil)).Elem()
}

func (o L7RulesV2ResultOutput) ToL7RulesV2ResultOutput() L7RulesV2ResultOutput {
	return o
}

func (o L7RulesV2ResultOutput) ToL7RulesV2ResultOutputWithContext(ctx context.Context) L7RulesV2ResultOutput {
	return o
}

func (o L7RulesV2ResultOutput) Business() pulumi.StringOutput {
	return o.ApplyT(func(v L7RulesV2Result) string { return v.Business }).(pulumi.StringOutput)
}

func (o L7RulesV2ResultOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v L7RulesV2Result) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o L7RulesV2ResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v L7RulesV2Result) string { return v.Id }).(pulumi.StringOutput)
}

func (o L7RulesV2ResultOutput) Ip() pulumi.StringPtrOutput {
	return o.ApplyT(func(v L7RulesV2Result) *string { return v.Ip }).(pulumi.StringPtrOutput)
}

func (o L7RulesV2ResultOutput) Limit() pulumi.IntPtrOutput {
	return o.ApplyT(func(v L7RulesV2Result) *int { return v.Limit }).(pulumi.IntPtrOutput)
}

func (o L7RulesV2ResultOutput) Lists() L7RulesV2ListArrayOutput {
	return o.ApplyT(func(v L7RulesV2Result) []L7RulesV2List { return v.Lists }).(L7RulesV2ListArrayOutput)
}

func (o L7RulesV2ResultOutput) Offset() pulumi.IntPtrOutput {
	return o.ApplyT(func(v L7RulesV2Result) *int { return v.Offset }).(pulumi.IntPtrOutput)
}

func (o L7RulesV2ResultOutput) Protocol() pulumi.StringPtrOutput {
	return o.ApplyT(func(v L7RulesV2Result) *string { return v.Protocol }).(pulumi.StringPtrOutput)
}

func (o L7RulesV2ResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v L7RulesV2Result) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(L7RulesV2ResultOutput{})
}
