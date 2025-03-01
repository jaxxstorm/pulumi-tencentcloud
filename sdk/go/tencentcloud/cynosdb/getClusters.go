// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cynosdb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query detailed information of Cynosdb clusters.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Cynosdb"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Cynosdb"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Cynosdb.GetClusters(ctx, &cynosdb.GetClustersArgs{
// 			ClusterId:   pulumi.StringRef("cynosdbmysql-dzj5l8gz"),
// 			ClusterName: pulumi.StringRef("test"),
// 			DbType:      pulumi.StringRef("MYSQL"),
// 			ProjectId:   pulumi.IntRef(0),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetClusters(ctx *pulumi.Context, args *GetClustersArgs, opts ...pulumi.InvokeOption) (*GetClustersResult, error) {
	var rv GetClustersResult
	err := ctx.Invoke("tencentcloud:Cynosdb/getClusters:getClusters", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getClusters.
type GetClustersArgs struct {
	// ID of the cluster to be queried.
	ClusterId *string `pulumi:"clusterId"`
	// Name of the cluster to be queried.
	ClusterName *string `pulumi:"clusterName"`
	// Type of CynosDB, and available values include `MYSQL`, `POSTGRESQL`.
	DbType *string `pulumi:"dbType"`
	// ID of the project to be queried.
	ProjectId *int `pulumi:"projectId"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by getClusters.
type GetClustersResult struct {
	// ID of CynosDB cluster.
	ClusterId *string `pulumi:"clusterId"`
	// A list of clusters. Each element contains the following attributes:
	ClusterLists []GetClustersClusterList `pulumi:"clusterLists"`
	// Name of CynosDB cluster.
	ClusterName *string `pulumi:"clusterName"`
	// Type of CynosDB, and available values include `MYSQL`.
	DbType *string `pulumi:"dbType"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// ID of the project.
	ProjectId        *int    `pulumi:"projectId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

func GetClustersOutput(ctx *pulumi.Context, args GetClustersOutputArgs, opts ...pulumi.InvokeOption) GetClustersResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetClustersResult, error) {
			args := v.(GetClustersArgs)
			r, err := GetClusters(ctx, &args, opts...)
			var s GetClustersResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetClustersResultOutput)
}

// A collection of arguments for invoking getClusters.
type GetClustersOutputArgs struct {
	// ID of the cluster to be queried.
	ClusterId pulumi.StringPtrInput `pulumi:"clusterId"`
	// Name of the cluster to be queried.
	ClusterName pulumi.StringPtrInput `pulumi:"clusterName"`
	// Type of CynosDB, and available values include `MYSQL`, `POSTGRESQL`.
	DbType pulumi.StringPtrInput `pulumi:"dbType"`
	// ID of the project to be queried.
	ProjectId pulumi.IntPtrInput `pulumi:"projectId"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (GetClustersOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetClustersArgs)(nil)).Elem()
}

// A collection of values returned by getClusters.
type GetClustersResultOutput struct{ *pulumi.OutputState }

func (GetClustersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetClustersResult)(nil)).Elem()
}

func (o GetClustersResultOutput) ToGetClustersResultOutput() GetClustersResultOutput {
	return o
}

func (o GetClustersResultOutput) ToGetClustersResultOutputWithContext(ctx context.Context) GetClustersResultOutput {
	return o
}

// ID of CynosDB cluster.
func (o GetClustersResultOutput) ClusterId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetClustersResult) *string { return v.ClusterId }).(pulumi.StringPtrOutput)
}

// A list of clusters. Each element contains the following attributes:
func (o GetClustersResultOutput) ClusterLists() GetClustersClusterListArrayOutput {
	return o.ApplyT(func(v GetClustersResult) []GetClustersClusterList { return v.ClusterLists }).(GetClustersClusterListArrayOutput)
}

// Name of CynosDB cluster.
func (o GetClustersResultOutput) ClusterName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetClustersResult) *string { return v.ClusterName }).(pulumi.StringPtrOutput)
}

// Type of CynosDB, and available values include `MYSQL`.
func (o GetClustersResultOutput) DbType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetClustersResult) *string { return v.DbType }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetClustersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersResult) string { return v.Id }).(pulumi.StringOutput)
}

// ID of the project.
func (o GetClustersResultOutput) ProjectId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetClustersResult) *int { return v.ProjectId }).(pulumi.IntPtrOutput)
}

func (o GetClustersResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetClustersResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetClustersResultOutput{})
}
