// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dayu

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func L4RulesV2(ctx *pulumi.Context, args *L4RulesV2Args, opts ...pulumi.InvokeOption) (*L4RulesV2Result, error) {
	var rv L4RulesV2Result
	err := ctx.Invoke("tencentcloud:Dayu/l4RulesV2:L4RulesV2", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking L4RulesV2.
type L4RulesV2Args struct {
	Business         string  `pulumi:"business"`
	Ip               *string `pulumi:"ip"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	VirtualPort      *int    `pulumi:"virtualPort"`
}

// A collection of values returned by L4RulesV2.
type L4RulesV2Result struct {
	Business string `pulumi:"business"`
	// The provider-assigned unique ID for this managed resource.
	Id               string          `pulumi:"id"`
	Ip               *string         `pulumi:"ip"`
	Lists            []L4RulesV2List `pulumi:"lists"`
	ResultOutputFile *string         `pulumi:"resultOutputFile"`
	VirtualPort      *int            `pulumi:"virtualPort"`
}

func L4RulesV2Output(ctx *pulumi.Context, args L4RulesV2OutputArgs, opts ...pulumi.InvokeOption) L4RulesV2ResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (L4RulesV2Result, error) {
			args := v.(L4RulesV2Args)
			r, err := L4RulesV2(ctx, &args, opts...)
			var s L4RulesV2Result
			if r != nil {
				s = *r
			}
			return s, err
		}).(L4RulesV2ResultOutput)
}

// A collection of arguments for invoking L4RulesV2.
type L4RulesV2OutputArgs struct {
	Business         pulumi.StringInput    `pulumi:"business"`
	Ip               pulumi.StringPtrInput `pulumi:"ip"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	VirtualPort      pulumi.IntPtrInput    `pulumi:"virtualPort"`
}

func (L4RulesV2OutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*L4RulesV2Args)(nil)).Elem()
}

// A collection of values returned by L4RulesV2.
type L4RulesV2ResultOutput struct{ *pulumi.OutputState }

func (L4RulesV2ResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*L4RulesV2Result)(nil)).Elem()
}

func (o L4RulesV2ResultOutput) ToL4RulesV2ResultOutput() L4RulesV2ResultOutput {
	return o
}

func (o L4RulesV2ResultOutput) ToL4RulesV2ResultOutputWithContext(ctx context.Context) L4RulesV2ResultOutput {
	return o
}

func (o L4RulesV2ResultOutput) Business() pulumi.StringOutput {
	return o.ApplyT(func(v L4RulesV2Result) string { return v.Business }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o L4RulesV2ResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v L4RulesV2Result) string { return v.Id }).(pulumi.StringOutput)
}

func (o L4RulesV2ResultOutput) Ip() pulumi.StringPtrOutput {
	return o.ApplyT(func(v L4RulesV2Result) *string { return v.Ip }).(pulumi.StringPtrOutput)
}

func (o L4RulesV2ResultOutput) Lists() L4RulesV2ListArrayOutput {
	return o.ApplyT(func(v L4RulesV2Result) []L4RulesV2List { return v.Lists }).(L4RulesV2ListArrayOutput)
}

func (o L4RulesV2ResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v L4RulesV2Result) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o L4RulesV2ResultOutput) VirtualPort() pulumi.IntPtrOutput {
	return o.ApplyT(func(v L4RulesV2Result) *int { return v.VirtualPort }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(L4RulesV2ResultOutput{})
}
