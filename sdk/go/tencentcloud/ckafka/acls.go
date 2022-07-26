// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ckafka

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Acls(ctx *pulumi.Context, args *AclsArgs, opts ...pulumi.InvokeOption) (*AclsResult, error) {
	var rv AclsResult
	err := ctx.Invoke("tencentcloud:Ckafka/acls:Acls", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Acls.
type AclsArgs struct {
	Host             *string `pulumi:"host"`
	InstanceId       string  `pulumi:"instanceId"`
	ResourceName     string  `pulumi:"resourceName"`
	ResourceType     string  `pulumi:"resourceType"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by Acls.
type AclsResult struct {
	AclLists []AclsAclList `pulumi:"aclLists"`
	Host     *string       `pulumi:"host"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	InstanceId       string  `pulumi:"instanceId"`
	ResourceName     string  `pulumi:"resourceName"`
	ResourceType     string  `pulumi:"resourceType"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
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
	Host             pulumi.StringPtrInput `pulumi:"host"`
	InstanceId       pulumi.StringInput    `pulumi:"instanceId"`
	ResourceName     pulumi.StringInput    `pulumi:"resourceName"`
	ResourceType     pulumi.StringInput    `pulumi:"resourceType"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
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

func (o AclsResultOutput) Host() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AclsResult) *string { return v.Host }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o AclsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v AclsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o AclsResultOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v AclsResult) string { return v.InstanceId }).(pulumi.StringOutput)
}

func (o AclsResultOutput) ResourceName() pulumi.StringOutput {
	return o.ApplyT(func(v AclsResult) string { return v.ResourceName }).(pulumi.StringOutput)
}

func (o AclsResultOutput) ResourceType() pulumi.StringOutput {
	return o.ApplyT(func(v AclsResult) string { return v.ResourceType }).(pulumi.StringOutput)
}

func (o AclsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v AclsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(AclsResultOutput{})
}
