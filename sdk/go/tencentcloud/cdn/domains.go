// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cdn

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Domains(ctx *pulumi.Context, args *DomainsArgs, opts ...pulumi.InvokeOption) (*DomainsResult, error) {
	var rv DomainsResult
	err := ctx.Invoke("tencentcloud:Cdn/domains:Domains", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Domains.
type DomainsArgs struct {
	Domain             *string `pulumi:"domain"`
	FullUrlCache       *bool   `pulumi:"fullUrlCache"`
	HttpsSwitch        *string `pulumi:"httpsSwitch"`
	OriginPullProtocol *string `pulumi:"originPullProtocol"`
	ResultOutputFile   *string `pulumi:"resultOutputFile"`
	ServiceType        *string `pulumi:"serviceType"`
}

// A collection of values returned by Domains.
type DomainsResult struct {
	Domain       *string             `pulumi:"domain"`
	DomainLists  []DomainsDomainList `pulumi:"domainLists"`
	FullUrlCache *bool               `pulumi:"fullUrlCache"`
	HttpsSwitch  *string             `pulumi:"httpsSwitch"`
	// The provider-assigned unique ID for this managed resource.
	Id                 string  `pulumi:"id"`
	OriginPullProtocol *string `pulumi:"originPullProtocol"`
	ResultOutputFile   *string `pulumi:"resultOutputFile"`
	ServiceType        *string `pulumi:"serviceType"`
}

func DomainsOutput(ctx *pulumi.Context, args DomainsOutputArgs, opts ...pulumi.InvokeOption) DomainsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (DomainsResult, error) {
			args := v.(DomainsArgs)
			r, err := Domains(ctx, &args, opts...)
			var s DomainsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(DomainsResultOutput)
}

// A collection of arguments for invoking Domains.
type DomainsOutputArgs struct {
	Domain             pulumi.StringPtrInput `pulumi:"domain"`
	FullUrlCache       pulumi.BoolPtrInput   `pulumi:"fullUrlCache"`
	HttpsSwitch        pulumi.StringPtrInput `pulumi:"httpsSwitch"`
	OriginPullProtocol pulumi.StringPtrInput `pulumi:"originPullProtocol"`
	ResultOutputFile   pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	ServiceType        pulumi.StringPtrInput `pulumi:"serviceType"`
}

func (DomainsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DomainsArgs)(nil)).Elem()
}

// A collection of values returned by Domains.
type DomainsResultOutput struct{ *pulumi.OutputState }

func (DomainsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DomainsResult)(nil)).Elem()
}

func (o DomainsResultOutput) ToDomainsResultOutput() DomainsResultOutput {
	return o
}

func (o DomainsResultOutput) ToDomainsResultOutputWithContext(ctx context.Context) DomainsResultOutput {
	return o
}

func (o DomainsResultOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DomainsResult) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

func (o DomainsResultOutput) DomainLists() DomainsDomainListArrayOutput {
	return o.ApplyT(func(v DomainsResult) []DomainsDomainList { return v.DomainLists }).(DomainsDomainListArrayOutput)
}

func (o DomainsResultOutput) FullUrlCache() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v DomainsResult) *bool { return v.FullUrlCache }).(pulumi.BoolPtrOutput)
}

func (o DomainsResultOutput) HttpsSwitch() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DomainsResult) *string { return v.HttpsSwitch }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o DomainsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v DomainsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o DomainsResultOutput) OriginPullProtocol() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DomainsResult) *string { return v.OriginPullProtocol }).(pulumi.StringPtrOutput)
}

func (o DomainsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DomainsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o DomainsResultOutput) ServiceType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DomainsResult) *string { return v.ServiceType }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(DomainsResultOutput{})
}
