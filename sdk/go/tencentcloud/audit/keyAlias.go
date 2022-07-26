// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package audit

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func KeyAlias(ctx *pulumi.Context, args *KeyAliasArgs, opts ...pulumi.InvokeOption) (*KeyAliasResult, error) {
	var rv KeyAliasResult
	err := ctx.Invoke("tencentcloud:Audit/keyAlias:KeyAlias", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking KeyAlias.
type KeyAliasArgs struct {
	Region           string  `pulumi:"region"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by KeyAlias.
type KeyAliasResult struct {
	AuditKeyAliasLists []KeyAliasAuditKeyAliasList `pulumi:"auditKeyAliasLists"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	Region           string  `pulumi:"region"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

func KeyAliasOutput(ctx *pulumi.Context, args KeyAliasOutputArgs, opts ...pulumi.InvokeOption) KeyAliasResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (KeyAliasResult, error) {
			args := v.(KeyAliasArgs)
			r, err := KeyAlias(ctx, &args, opts...)
			var s KeyAliasResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(KeyAliasResultOutput)
}

// A collection of arguments for invoking KeyAlias.
type KeyAliasOutputArgs struct {
	Region           pulumi.StringInput    `pulumi:"region"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (KeyAliasOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*KeyAliasArgs)(nil)).Elem()
}

// A collection of values returned by KeyAlias.
type KeyAliasResultOutput struct{ *pulumi.OutputState }

func (KeyAliasResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*KeyAliasResult)(nil)).Elem()
}

func (o KeyAliasResultOutput) ToKeyAliasResultOutput() KeyAliasResultOutput {
	return o
}

func (o KeyAliasResultOutput) ToKeyAliasResultOutputWithContext(ctx context.Context) KeyAliasResultOutput {
	return o
}

func (o KeyAliasResultOutput) AuditKeyAliasLists() KeyAliasAuditKeyAliasListArrayOutput {
	return o.ApplyT(func(v KeyAliasResult) []KeyAliasAuditKeyAliasList { return v.AuditKeyAliasLists }).(KeyAliasAuditKeyAliasListArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o KeyAliasResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v KeyAliasResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o KeyAliasResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v KeyAliasResult) string { return v.Region }).(pulumi.StringOutput)
}

func (o KeyAliasResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v KeyAliasResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(KeyAliasResultOutput{})
}
