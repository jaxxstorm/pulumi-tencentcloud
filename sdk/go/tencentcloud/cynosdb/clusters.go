// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cynosdb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Clusters(ctx *pulumi.Context, args *ClustersArgs, opts ...pulumi.InvokeOption) (*ClustersResult, error) {
	var rv ClustersResult
	err := ctx.Invoke("tencentcloud:Cynosdb/clusters:Clusters", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Clusters.
type ClustersArgs struct {
	ClusterId        *string `pulumi:"clusterId"`
	ClusterName      *string `pulumi:"clusterName"`
	DbType           *string `pulumi:"dbType"`
	ProjectId        *int    `pulumi:"projectId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by Clusters.
type ClustersResult struct {
	ClusterId    *string               `pulumi:"clusterId"`
	ClusterLists []ClustersClusterList `pulumi:"clusterLists"`
	ClusterName  *string               `pulumi:"clusterName"`
	DbType       *string               `pulumi:"dbType"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	ProjectId        *int    `pulumi:"projectId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

func ClustersOutput(ctx *pulumi.Context, args ClustersOutputArgs, opts ...pulumi.InvokeOption) ClustersResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ClustersResult, error) {
			args := v.(ClustersArgs)
			r, err := Clusters(ctx, &args, opts...)
			var s ClustersResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(ClustersResultOutput)
}

// A collection of arguments for invoking Clusters.
type ClustersOutputArgs struct {
	ClusterId        pulumi.StringPtrInput `pulumi:"clusterId"`
	ClusterName      pulumi.StringPtrInput `pulumi:"clusterName"`
	DbType           pulumi.StringPtrInput `pulumi:"dbType"`
	ProjectId        pulumi.IntPtrInput    `pulumi:"projectId"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (ClustersOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ClustersArgs)(nil)).Elem()
}

// A collection of values returned by Clusters.
type ClustersResultOutput struct{ *pulumi.OutputState }

func (ClustersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClustersResult)(nil)).Elem()
}

func (o ClustersResultOutput) ToClustersResultOutput() ClustersResultOutput {
	return o
}

func (o ClustersResultOutput) ToClustersResultOutputWithContext(ctx context.Context) ClustersResultOutput {
	return o
}

func (o ClustersResultOutput) ClusterId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClustersResult) *string { return v.ClusterId }).(pulumi.StringPtrOutput)
}

func (o ClustersResultOutput) ClusterLists() ClustersClusterListArrayOutput {
	return o.ApplyT(func(v ClustersResult) []ClustersClusterList { return v.ClusterLists }).(ClustersClusterListArrayOutput)
}

func (o ClustersResultOutput) ClusterName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClustersResult) *string { return v.ClusterName }).(pulumi.StringPtrOutput)
}

func (o ClustersResultOutput) DbType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClustersResult) *string { return v.DbType }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o ClustersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v ClustersResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o ClustersResultOutput) ProjectId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ClustersResult) *int { return v.ProjectId }).(pulumi.IntPtrOutput)
}

func (o ClustersResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClustersResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ClustersResultOutput{})
}
