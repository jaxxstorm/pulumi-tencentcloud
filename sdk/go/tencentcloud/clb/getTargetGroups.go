// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query target group information.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Clb"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Clb"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		clbBasic, err := Clb.NewInstance(ctx, "clbBasic", &Clb.InstanceArgs{
// 			NetworkType: pulumi.String("OPEN"),
// 			ClbName:     pulumi.String("tf-clb-rule-basic"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		listenerBasic, err := Clb.NewListener(ctx, "listenerBasic", &Clb.ListenerArgs{
// 			ClbId:        clbBasic.ID(),
// 			Port:         pulumi.Int(1),
// 			Protocol:     pulumi.String("HTTP"),
// 			ListenerName: pulumi.String("listener_basic"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		ruleBasic, err := Clb.NewListenerRule(ctx, "ruleBasic", &Clb.ListenerRuleArgs{
// 			ClbId:             clbBasic.ID(),
// 			ListenerId:        listenerBasic.ListenerId,
// 			Domain:            pulumi.String("abc.com"),
// 			Url:               pulumi.String("/"),
// 			SessionExpireTime: pulumi.Int(30),
// 			Scheduler:         pulumi.String("WRR"),
// 			TargetType:        pulumi.String("TARGETGROUP"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		test, err := Clb.NewTargetGroup(ctx, "test", &Clb.TargetGroupArgs{
// 			TargetGroupName: pulumi.String("test-target-keep-1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = Clb.NewTargetGroupAttachment(ctx, "group", &Clb.TargetGroupAttachmentArgs{
// 			ClbId:         clbBasic.ID(),
// 			ListenerId:    listenerBasic.ListenerId,
// 			RuleId:        ruleBasic.RuleId,
// 			TargrtGroupId: test.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_ = Clb.GetTargetGroupsOutput(ctx, clb.GetTargetGroupsOutputArgs{
// 			TargetGroupId: test.ID(),
// 		}, nil)
// 		return nil
// 	})
// }
// ```
func GetTargetGroups(ctx *pulumi.Context, args *GetTargetGroupsArgs, opts ...pulumi.InvokeOption) (*GetTargetGroupsResult, error) {
	var rv GetTargetGroupsResult
	err := ctx.Invoke("tencentcloud:Clb/getTargetGroups:getTargetGroups", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTargetGroups.
type GetTargetGroupsArgs struct {
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// ID of Target group. Mutually exclusive with `vpcId` and `targetGroupName`. `targetGroupId` is preferred.
	TargetGroupId *string `pulumi:"targetGroupId"`
	// Name of target group. Mutually exclusive with `targetGroupId`. `targetGroupId` is preferred.
	TargetGroupName *string `pulumi:"targetGroupName"`
	// Target group VPC ID. Mutually exclusive with `targetGroupId`. `targetGroupId` is preferred.
	VpcId *string `pulumi:"vpcId"`
}

// A collection of values returned by getTargetGroups.
type GetTargetGroupsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Target group info list.
	Lists            []GetTargetGroupsList `pulumi:"lists"`
	ResultOutputFile *string               `pulumi:"resultOutputFile"`
	// ID of Target group.
	TargetGroupId *string `pulumi:"targetGroupId"`
	// Target group VPC ID.
	TargetGroupName *string `pulumi:"targetGroupName"`
	// Name of target group.
	VpcId *string `pulumi:"vpcId"`
}

func GetTargetGroupsOutput(ctx *pulumi.Context, args GetTargetGroupsOutputArgs, opts ...pulumi.InvokeOption) GetTargetGroupsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetTargetGroupsResult, error) {
			args := v.(GetTargetGroupsArgs)
			r, err := GetTargetGroups(ctx, &args, opts...)
			var s GetTargetGroupsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetTargetGroupsResultOutput)
}

// A collection of arguments for invoking getTargetGroups.
type GetTargetGroupsOutputArgs struct {
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	// ID of Target group. Mutually exclusive with `vpcId` and `targetGroupName`. `targetGroupId` is preferred.
	TargetGroupId pulumi.StringPtrInput `pulumi:"targetGroupId"`
	// Name of target group. Mutually exclusive with `targetGroupId`. `targetGroupId` is preferred.
	TargetGroupName pulumi.StringPtrInput `pulumi:"targetGroupName"`
	// Target group VPC ID. Mutually exclusive with `targetGroupId`. `targetGroupId` is preferred.
	VpcId pulumi.StringPtrInput `pulumi:"vpcId"`
}

func (GetTargetGroupsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTargetGroupsArgs)(nil)).Elem()
}

// A collection of values returned by getTargetGroups.
type GetTargetGroupsResultOutput struct{ *pulumi.OutputState }

func (GetTargetGroupsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTargetGroupsResult)(nil)).Elem()
}

func (o GetTargetGroupsResultOutput) ToGetTargetGroupsResultOutput() GetTargetGroupsResultOutput {
	return o
}

func (o GetTargetGroupsResultOutput) ToGetTargetGroupsResultOutputWithContext(ctx context.Context) GetTargetGroupsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetTargetGroupsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetTargetGroupsResult) string { return v.Id }).(pulumi.StringOutput)
}

// Target group info list.
func (o GetTargetGroupsResultOutput) Lists() GetTargetGroupsListArrayOutput {
	return o.ApplyT(func(v GetTargetGroupsResult) []GetTargetGroupsList { return v.Lists }).(GetTargetGroupsListArrayOutput)
}

func (o GetTargetGroupsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTargetGroupsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

// ID of Target group.
func (o GetTargetGroupsResultOutput) TargetGroupId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTargetGroupsResult) *string { return v.TargetGroupId }).(pulumi.StringPtrOutput)
}

// Target group VPC ID.
func (o GetTargetGroupsResultOutput) TargetGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTargetGroupsResult) *string { return v.TargetGroupName }).(pulumi.StringPtrOutput)
}

// Name of target group.
func (o GetTargetGroupsResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTargetGroupsResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetTargetGroupsResultOutput{})
}
