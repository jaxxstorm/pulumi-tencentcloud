// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ccn

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query detailed information of CCN bandwidth limits.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Ccn"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Ccn"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		cfg := config.New(ctx, "")
// 		otherRegion1 := "ap-shanghai"
// 		if param := cfg.Get("otherRegion1"); param != "" {
// 			otherRegion1 = param
// 		}
// 		main, err := Ccn.NewInstance(ctx, "main", &Ccn.InstanceArgs{
// 			Description: pulumi.String("ci-temp-test-ccn-des"),
// 			Qos:         pulumi.String("AG"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_ = Ccn.GetBandwidthLimitsOutput(ctx, ccn.GetBandwidthLimitsOutputArgs{
// 			CcnId: main.ID(),
// 		}, nil)
// 		_, err = Ccn.NewBandwidthLimit(ctx, "limit1", &Ccn.BandwidthLimitArgs{
// 			CcnId:          main.ID(),
// 			Region:         pulumi.String(otherRegion1),
// 			BandwidthLimit: pulumi.Int(500),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetBandwidthLimits(ctx *pulumi.Context, args *GetBandwidthLimitsArgs, opts ...pulumi.InvokeOption) (*GetBandwidthLimitsResult, error) {
	var rv GetBandwidthLimitsResult
	err := ctx.Invoke("tencentcloud:Ccn/getBandwidthLimits:getBandwidthLimits", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBandwidthLimits.
type GetBandwidthLimitsArgs struct {
	// ID of the CCN to be queried.
	CcnId string `pulumi:"ccnId"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by getBandwidthLimits.
type GetBandwidthLimitsResult struct {
	CcnId string `pulumi:"ccnId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The bandwidth limits of regions:
	Limits           []GetBandwidthLimitsLimit `pulumi:"limits"`
	ResultOutputFile *string                   `pulumi:"resultOutputFile"`
}

func GetBandwidthLimitsOutput(ctx *pulumi.Context, args GetBandwidthLimitsOutputArgs, opts ...pulumi.InvokeOption) GetBandwidthLimitsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetBandwidthLimitsResult, error) {
			args := v.(GetBandwidthLimitsArgs)
			r, err := GetBandwidthLimits(ctx, &args, opts...)
			var s GetBandwidthLimitsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetBandwidthLimitsResultOutput)
}

// A collection of arguments for invoking getBandwidthLimits.
type GetBandwidthLimitsOutputArgs struct {
	// ID of the CCN to be queried.
	CcnId pulumi.StringInput `pulumi:"ccnId"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (GetBandwidthLimitsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetBandwidthLimitsArgs)(nil)).Elem()
}

// A collection of values returned by getBandwidthLimits.
type GetBandwidthLimitsResultOutput struct{ *pulumi.OutputState }

func (GetBandwidthLimitsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetBandwidthLimitsResult)(nil)).Elem()
}

func (o GetBandwidthLimitsResultOutput) ToGetBandwidthLimitsResultOutput() GetBandwidthLimitsResultOutput {
	return o
}

func (o GetBandwidthLimitsResultOutput) ToGetBandwidthLimitsResultOutputWithContext(ctx context.Context) GetBandwidthLimitsResultOutput {
	return o
}

func (o GetBandwidthLimitsResultOutput) CcnId() pulumi.StringOutput {
	return o.ApplyT(func(v GetBandwidthLimitsResult) string { return v.CcnId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetBandwidthLimitsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetBandwidthLimitsResult) string { return v.Id }).(pulumi.StringOutput)
}

// The bandwidth limits of regions:
func (o GetBandwidthLimitsResultOutput) Limits() GetBandwidthLimitsLimitArrayOutput {
	return o.ApplyT(func(v GetBandwidthLimitsResult) []GetBandwidthLimitsLimit { return v.Limits }).(GetBandwidthLimitsLimitArrayOutput)
}

func (o GetBandwidthLimitsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetBandwidthLimitsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetBandwidthLimitsResultOutput{})
}
