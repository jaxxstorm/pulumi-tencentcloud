// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpc

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Acls(ctx *pulumi.Context, args *AclsArgs, opts ...pulumi.InvokeOption) (*AclsResult, error) {
	var rv AclsResult
	err := ctx.Invoke("tencentcloud:Vpc/acls:Acls", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Acls.
type AclsArgs struct {
	Id               *string `pulumi:"id"`
	Name             *string `pulumi:"name"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	VpcId            *string `pulumi:"vpcId"`
}

// A collection of values returned by Acls.
type AclsResult struct {
	AclLists         []AclsAclList `pulumi:"aclLists"`
	Id               *string       `pulumi:"id"`
	Name             *string       `pulumi:"name"`
	ResultOutputFile *string       `pulumi:"resultOutputFile"`
	VpcId            *string       `pulumi:"vpcId"`
}

func AclsOutput(ctx *pulumi.Context, args AclsOutputArgs, opts ...pulumi.InvokeOption) AclsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (AclsResult, error) {
			args := v.(AclsArgs)
			r, err := Acls(ctx, &args, opts...)
			var s AclsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(AclsResultOutput)
}

// A collection of arguments for invoking Acls.
type AclsOutputArgs struct {
	Id               pulumi.StringPtrInput `pulumi:"id"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	VpcId            pulumi.StringPtrInput `pulumi:"vpcId"`
}

func (AclsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AclsArgs)(nil)).Elem()
}

// A collection of values returned by Acls.
type AclsResultOutput struct{ *pulumi.OutputState }

func (AclsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AclsResult)(nil)).Elem()
}

func (o AclsResultOutput) ToAclsResultOutput() AclsResultOutput {
	return o
}

func (o AclsResultOutput) ToAclsResultOutputWithContext(ctx context.Context) AclsResultOutput {
	return o
}

func (o AclsResultOutput) AclLists() AclsAclListArrayOutput {
	return o.ApplyT(func(v AclsResult) []AclsAclList { return v.AclLists }).(AclsAclListArrayOutput)
}

func (o AclsResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AclsResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o AclsResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AclsResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o AclsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AclsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o AclsResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AclsResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(AclsResultOutput{})
}
