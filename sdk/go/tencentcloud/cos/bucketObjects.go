// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cos

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func BucketObjects(ctx *pulumi.Context, args *BucketObjectsArgs, opts ...pulumi.InvokeOption) (*BucketObjectsResult, error) {
	var rv BucketObjectsResult
	err := ctx.Invoke("tencentcloud:Cos/bucketObjects:BucketObjects", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking BucketObjects.
type BucketObjectsArgs struct {
	Bucket           string  `pulumi:"bucket"`
	Key              string  `pulumi:"key"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by BucketObjects.
type BucketObjectsResult struct {
	Bucket             string `pulumi:"bucket"`
	CacheControl       string `pulumi:"cacheControl"`
	ContentDisposition string `pulumi:"contentDisposition"`
	ContentEncoding    string `pulumi:"contentEncoding"`
	ContentType        string `pulumi:"contentType"`
	Etag               string `pulumi:"etag"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	Key              string  `pulumi:"key"`
	LastModified     string  `pulumi:"lastModified"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	StorageClass     string  `pulumi:"storageClass"`
}

func BucketObjectsOutput(ctx *pulumi.Context, args BucketObjectsOutputArgs, opts ...pulumi.InvokeOption) BucketObjectsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (BucketObjectsResult, error) {
			args := v.(BucketObjectsArgs)
			r, err := BucketObjects(ctx, &args, opts...)
			var s BucketObjectsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(BucketObjectsResultOutput)
}

// A collection of arguments for invoking BucketObjects.
type BucketObjectsOutputArgs struct {
	Bucket           pulumi.StringInput    `pulumi:"bucket"`
	Key              pulumi.StringInput    `pulumi:"key"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (BucketObjectsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*BucketObjectsArgs)(nil)).Elem()
}

// A collection of values returned by BucketObjects.
type BucketObjectsResultOutput struct{ *pulumi.OutputState }

func (BucketObjectsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*BucketObjectsResult)(nil)).Elem()
}

func (o BucketObjectsResultOutput) ToBucketObjectsResultOutput() BucketObjectsResultOutput {
	return o
}

func (o BucketObjectsResultOutput) ToBucketObjectsResultOutputWithContext(ctx context.Context) BucketObjectsResultOutput {
	return o
}

func (o BucketObjectsResultOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.Bucket }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) CacheControl() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.CacheControl }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) ContentDisposition() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.ContentDisposition }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) ContentEncoding() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.ContentEncoding }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) ContentType() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.ContentType }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.Etag }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o BucketObjectsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.Key }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) LastModified() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.LastModified }).(pulumi.StringOutput)
}

func (o BucketObjectsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v BucketObjectsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o BucketObjectsResultOutput) StorageClass() pulumi.StringOutput {
	return o.ApplyT(func(v BucketObjectsResult) string { return v.StorageClass }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(BucketObjectsResultOutput{})
}
