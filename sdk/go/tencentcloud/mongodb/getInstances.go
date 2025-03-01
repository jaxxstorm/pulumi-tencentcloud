// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mongodb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query detailed information of Mongodb instances.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Mongodb"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Mongodb"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Mongodb.GetInstances(ctx, &mongodb.GetInstancesArgs{
// 			ClusterType: pulumi.StringRef("REPLSET"),
// 			InstanceId:  pulumi.StringRef("cmgo-l6lwdsel"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetInstances(ctx *pulumi.Context, args *GetInstancesArgs, opts ...pulumi.InvokeOption) (*GetInstancesResult, error) {
	var rv GetInstancesResult
	err := ctx.Invoke("tencentcloud:Mongodb/getInstances:getInstances", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInstances.
type GetInstancesArgs struct {
	// Type of Mongodb cluster, and available values include replica set cluster(expressed with `REPLSET`), sharding cluster(expressed with `SHARD`).
	ClusterType *string `pulumi:"clusterType"`
	// ID of the Mongodb instance to be queried.
	InstanceId *string `pulumi:"instanceId"`
	// Name prefix of the Mongodb instance.
	InstanceNamePrefix *string `pulumi:"instanceNamePrefix"`
	// Used to store results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// Tags of the Mongodb instance to be queried.
	Tags map[string]interface{} `pulumi:"tags"`
}

// A collection of values returned by getInstances.
type GetInstancesResult struct {
	// Type of Mongodb cluster.
	ClusterType *string `pulumi:"clusterType"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// ID of the Mongodb instance.
	InstanceId *string `pulumi:"instanceId"`
	// A list of instances. Each element contains the following attributes:
	InstanceLists      []GetInstancesInstanceList `pulumi:"instanceLists"`
	InstanceNamePrefix *string                    `pulumi:"instanceNamePrefix"`
	ResultOutputFile   *string                    `pulumi:"resultOutputFile"`
	// Tags of the Mongodb instance.
	Tags map[string]interface{} `pulumi:"tags"`
}

func GetInstancesOutput(ctx *pulumi.Context, args GetInstancesOutputArgs, opts ...pulumi.InvokeOption) GetInstancesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetInstancesResult, error) {
			args := v.(GetInstancesArgs)
			r, err := GetInstances(ctx, &args, opts...)
			var s GetInstancesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetInstancesResultOutput)
}

// A collection of arguments for invoking getInstances.
type GetInstancesOutputArgs struct {
	// Type of Mongodb cluster, and available values include replica set cluster(expressed with `REPLSET`), sharding cluster(expressed with `SHARD`).
	ClusterType pulumi.StringPtrInput `pulumi:"clusterType"`
	// ID of the Mongodb instance to be queried.
	InstanceId pulumi.StringPtrInput `pulumi:"instanceId"`
	// Name prefix of the Mongodb instance.
	InstanceNamePrefix pulumi.StringPtrInput `pulumi:"instanceNamePrefix"`
	// Used to store results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	// Tags of the Mongodb instance to be queried.
	Tags pulumi.MapInput `pulumi:"tags"`
}

func (GetInstancesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetInstancesArgs)(nil)).Elem()
}

// A collection of values returned by getInstances.
type GetInstancesResultOutput struct{ *pulumi.OutputState }

func (GetInstancesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetInstancesResult)(nil)).Elem()
}

func (o GetInstancesResultOutput) ToGetInstancesResultOutput() GetInstancesResultOutput {
	return o
}

func (o GetInstancesResultOutput) ToGetInstancesResultOutputWithContext(ctx context.Context) GetInstancesResultOutput {
	return o
}

// Type of Mongodb cluster.
func (o GetInstancesResultOutput) ClusterType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetInstancesResult) *string { return v.ClusterType }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetInstancesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetInstancesResult) string { return v.Id }).(pulumi.StringOutput)
}

// ID of the Mongodb instance.
func (o GetInstancesResultOutput) InstanceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetInstancesResult) *string { return v.InstanceId }).(pulumi.StringPtrOutput)
}

// A list of instances. Each element contains the following attributes:
func (o GetInstancesResultOutput) InstanceLists() GetInstancesInstanceListArrayOutput {
	return o.ApplyT(func(v GetInstancesResult) []GetInstancesInstanceList { return v.InstanceLists }).(GetInstancesInstanceListArrayOutput)
}

func (o GetInstancesResultOutput) InstanceNamePrefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetInstancesResult) *string { return v.InstanceNamePrefix }).(pulumi.StringPtrOutput)
}

func (o GetInstancesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetInstancesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

// Tags of the Mongodb instance.
func (o GetInstancesResultOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v GetInstancesResult) map[string]interface{} { return v.Tags }).(pulumi.MapOutput)
}

func init() {
	pulumi.RegisterOutputType(GetInstancesResultOutput{})
}
