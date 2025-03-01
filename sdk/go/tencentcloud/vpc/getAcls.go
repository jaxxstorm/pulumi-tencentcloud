// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpc

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query VPC Network ACL information.
func GetAcls(ctx *pulumi.Context, args *GetAclsArgs, opts ...pulumi.InvokeOption) (*GetAclsResult, error) {
	var rv GetAclsResult
	err := ctx.Invoke("tencentcloud:Vpc/getAcls:getAcls", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAcls.
type GetAclsArgs struct {
	// ID of the network ACL instance.
	Id *string `pulumi:"id"`
	// Name of the network ACL.
	Name *string `pulumi:"name"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// ID of the VPC instance.
	VpcId *string `pulumi:"vpcId"`
}

// A collection of values returned by getAcls.
type GetAclsResult struct {
	// The information list of the VPC. Each element contains the following attributes:
	AclLists []GetAclsAclList `pulumi:"aclLists"`
	// ID of the network ACL instance.
	Id *string `pulumi:"id"`
	// Name of the network ACL.
	Name             *string `pulumi:"name"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// ID of the VPC instance.
	VpcId *string `pulumi:"vpcId"`
}

func GetAclsOutput(ctx *pulumi.Context, args GetAclsOutputArgs, opts ...pulumi.InvokeOption) GetAclsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAclsResult, error) {
			args := v.(GetAclsArgs)
			r, err := GetAcls(ctx, &args, opts...)
			var s GetAclsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetAclsResultOutput)
}

// A collection of arguments for invoking getAcls.
type GetAclsOutputArgs struct {
	// ID of the network ACL instance.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of the network ACL.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	// ID of the VPC instance.
	VpcId pulumi.StringPtrInput `pulumi:"vpcId"`
}

func (GetAclsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAclsArgs)(nil)).Elem()
}

// A collection of values returned by getAcls.
type GetAclsResultOutput struct{ *pulumi.OutputState }

func (GetAclsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAclsResult)(nil)).Elem()
}

func (o GetAclsResultOutput) ToGetAclsResultOutput() GetAclsResultOutput {
	return o
}

func (o GetAclsResultOutput) ToGetAclsResultOutputWithContext(ctx context.Context) GetAclsResultOutput {
	return o
}

// The information list of the VPC. Each element contains the following attributes:
func (o GetAclsResultOutput) AclLists() GetAclsAclListArrayOutput {
	return o.ApplyT(func(v GetAclsResult) []GetAclsAclList { return v.AclLists }).(GetAclsAclListArrayOutput)
}

// ID of the network ACL instance.
func (o GetAclsResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAclsResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Name of the network ACL.
func (o GetAclsResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAclsResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GetAclsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAclsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

// ID of the VPC instance.
func (o GetAclsResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAclsResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAclsResultOutput{})
}
