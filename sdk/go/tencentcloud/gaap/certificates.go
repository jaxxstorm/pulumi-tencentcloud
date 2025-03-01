// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gaap

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Certificates(ctx *pulumi.Context, args *CertificatesArgs, opts ...pulumi.InvokeOption) (*CertificatesResult, error) {
	var rv CertificatesResult
	err := ctx.Invoke("tencentcloud:Gaap/certificates:Certificates", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Certificates.
type CertificatesArgs struct {
	Id               *string `pulumi:"id"`
	Name             *string `pulumi:"name"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	Type             *string `pulumi:"type"`
}

// A collection of values returned by Certificates.
type CertificatesResult struct {
	Certificates     []CertificatesCertificate `pulumi:"certificates"`
	Id               *string                   `pulumi:"id"`
	Name             *string                   `pulumi:"name"`
	ResultOutputFile *string                   `pulumi:"resultOutputFile"`
	Type             *string                   `pulumi:"type"`
}

func CertificatesOutput(ctx *pulumi.Context, args CertificatesOutputArgs, opts ...pulumi.InvokeOption) CertificatesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (CertificatesResult, error) {
			args := v.(CertificatesArgs)
			r, err := Certificates(ctx, &args, opts...)
			var s CertificatesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(CertificatesResultOutput)
}

// A collection of arguments for invoking Certificates.
type CertificatesOutputArgs struct {
	Id               pulumi.StringPtrInput `pulumi:"id"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	Type             pulumi.StringPtrInput `pulumi:"type"`
}

func (CertificatesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificatesArgs)(nil)).Elem()
}

// A collection of values returned by Certificates.
type CertificatesResultOutput struct{ *pulumi.OutputState }

func (CertificatesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificatesResult)(nil)).Elem()
}

func (o CertificatesResultOutput) ToCertificatesResultOutput() CertificatesResultOutput {
	return o
}

func (o CertificatesResultOutput) ToCertificatesResultOutputWithContext(ctx context.Context) CertificatesResultOutput {
	return o
}

func (o CertificatesResultOutput) Certificates() CertificatesCertificateArrayOutput {
	return o.ApplyT(func(v CertificatesResult) []CertificatesCertificate { return v.Certificates }).(CertificatesCertificateArrayOutput)
}

func (o CertificatesResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v CertificatesResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o CertificatesResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v CertificatesResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o CertificatesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v CertificatesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o CertificatesResultOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v CertificatesResult) *string { return v.Type }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(CertificatesResultOutput{})
}
