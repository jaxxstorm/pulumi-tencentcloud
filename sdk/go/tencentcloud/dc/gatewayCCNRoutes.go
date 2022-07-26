// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dc

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GatewayCCNRoutes(ctx *pulumi.Context, args *GatewayCCNRoutesArgs, opts ...pulumi.InvokeOption) (*GatewayCCNRoutesResult, error) {
	var rv GatewayCCNRoutesResult
	err := ctx.Invoke("tencentcloud:Dc/gatewayCCNRoutes:GatewayCCNRoutes", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking GatewayCCNRoutes.
type GatewayCCNRoutesArgs struct {
	DcgId            string  `pulumi:"dcgId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by GatewayCCNRoutes.
type GatewayCCNRoutesResult struct {
	DcgId string `pulumi:"dcgId"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                         `pulumi:"id"`
	InstanceLists    []GatewayCCNRoutesInstanceList `pulumi:"instanceLists"`
	ResultOutputFile *string                        `pulumi:"resultOutputFile"`
}

func GatewayCCNRoutesOutput(ctx *pulumi.Context, args GatewayCCNRoutesOutputArgs, opts ...pulumi.InvokeOption) GatewayCCNRoutesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GatewayCCNRoutesResult, error) {
			args := v.(GatewayCCNRoutesArgs)
			r, err := GatewayCCNRoutes(ctx, &args, opts...)
			var s GatewayCCNRoutesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GatewayCCNRoutesResultOutput)
}

// A collection of arguments for invoking GatewayCCNRoutes.
type GatewayCCNRoutesOutputArgs struct {
	DcgId            pulumi.StringInput    `pulumi:"dcgId"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (GatewayCCNRoutesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GatewayCCNRoutesArgs)(nil)).Elem()
}

// A collection of values returned by GatewayCCNRoutes.
type GatewayCCNRoutesResultOutput struct{ *pulumi.OutputState }

func (GatewayCCNRoutesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GatewayCCNRoutesResult)(nil)).Elem()
}

func (o GatewayCCNRoutesResultOutput) ToGatewayCCNRoutesResultOutput() GatewayCCNRoutesResultOutput {
	return o
}

func (o GatewayCCNRoutesResultOutput) ToGatewayCCNRoutesResultOutputWithContext(ctx context.Context) GatewayCCNRoutesResultOutput {
	return o
}

func (o GatewayCCNRoutesResultOutput) DcgId() pulumi.StringOutput {
	return o.ApplyT(func(v GatewayCCNRoutesResult) string { return v.DcgId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GatewayCCNRoutesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GatewayCCNRoutesResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GatewayCCNRoutesResultOutput) InstanceLists() GatewayCCNRoutesInstanceListArrayOutput {
	return o.ApplyT(func(v GatewayCCNRoutesResult) []GatewayCCNRoutesInstanceList { return v.InstanceLists }).(GatewayCCNRoutesInstanceListArrayOutput)
}

func (o GatewayCCNRoutesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GatewayCCNRoutesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GatewayCCNRoutesResultOutput{})
}
