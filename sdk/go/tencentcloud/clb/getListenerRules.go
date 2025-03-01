// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query detailed information of CLB listener rule
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
// 		_, err := Clb.GetListenerRules(ctx, &clb.GetListenerRulesArgs{
// 			ClbId:      "lb-k2zjp9lv",
// 			Domain:     pulumi.StringRef("abc.com"),
// 			ListenerId: "lbl-mwr6vbtv",
// 			RuleId:     pulumi.StringRef("loc-inem40hz"),
// 			Scheduler:  pulumi.StringRef("WRR"),
// 			Url:        pulumi.StringRef("/"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetListenerRules(ctx *pulumi.Context, args *GetListenerRulesArgs, opts ...pulumi.InvokeOption) (*GetListenerRulesResult, error) {
	var rv GetListenerRulesResult
	err := ctx.Invoke("tencentcloud:Clb/getListenerRules:getListenerRules", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getListenerRules.
type GetListenerRulesArgs struct {
	// ID of the CLB to be queried.
	ClbId string `pulumi:"clbId"`
	// Domain name of the forwarding rule to be queried.
	Domain *string `pulumi:"domain"`
	// ID of the CLB listener to be queried.
	ListenerId string `pulumi:"listenerId"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// ID of the forwarding rule to be queried.
	RuleId *string `pulumi:"ruleId"`
	// Scheduling method of the forwarding rule of thr CLB listener, and available values include `WRR`, `IP HASH` and `LEAST_CONN`. The default is `WRR`.
	Scheduler *string `pulumi:"scheduler"`
	// Url of the forwarding rule to be queried.
	Url *string `pulumi:"url"`
}

// A collection of values returned by getListenerRules.
type GetListenerRulesResult struct {
	// ID of the CLB.
	ClbId  string  `pulumi:"clbId"`
	Domain *string `pulumi:"domain"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// ID of the listener.
	ListenerId       string  `pulumi:"listenerId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// ID of the rule.
	RuleId *string `pulumi:"ruleId"`
	// A list of forward rules of listeners. Each element contains the following attributes:
	RuleLists []GetListenerRulesRuleList `pulumi:"ruleLists"`
	// Scheduling method of the CLB listener, and available values include 'WRR', 'IP_HASH' and 'LEAST_CONN'. The default is 'WRR'. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in tencentcloud_clb_listener_rule.
	Scheduler *string `pulumi:"scheduler"`
	Url       *string `pulumi:"url"`
}

func GetListenerRulesOutput(ctx *pulumi.Context, args GetListenerRulesOutputArgs, opts ...pulumi.InvokeOption) GetListenerRulesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetListenerRulesResult, error) {
			args := v.(GetListenerRulesArgs)
			r, err := GetListenerRules(ctx, &args, opts...)
			var s GetListenerRulesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetListenerRulesResultOutput)
}

// A collection of arguments for invoking getListenerRules.
type GetListenerRulesOutputArgs struct {
	// ID of the CLB to be queried.
	ClbId pulumi.StringInput `pulumi:"clbId"`
	// Domain name of the forwarding rule to be queried.
	Domain pulumi.StringPtrInput `pulumi:"domain"`
	// ID of the CLB listener to be queried.
	ListenerId pulumi.StringInput `pulumi:"listenerId"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	// ID of the forwarding rule to be queried.
	RuleId pulumi.StringPtrInput `pulumi:"ruleId"`
	// Scheduling method of the forwarding rule of thr CLB listener, and available values include `WRR`, `IP HASH` and `LEAST_CONN`. The default is `WRR`.
	Scheduler pulumi.StringPtrInput `pulumi:"scheduler"`
	// Url of the forwarding rule to be queried.
	Url pulumi.StringPtrInput `pulumi:"url"`
}

func (GetListenerRulesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetListenerRulesArgs)(nil)).Elem()
}

// A collection of values returned by getListenerRules.
type GetListenerRulesResultOutput struct{ *pulumi.OutputState }

func (GetListenerRulesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetListenerRulesResult)(nil)).Elem()
}

func (o GetListenerRulesResultOutput) ToGetListenerRulesResultOutput() GetListenerRulesResultOutput {
	return o
}

func (o GetListenerRulesResultOutput) ToGetListenerRulesResultOutputWithContext(ctx context.Context) GetListenerRulesResultOutput {
	return o
}

// ID of the CLB.
func (o GetListenerRulesResultOutput) ClbId() pulumi.StringOutput {
	return o.ApplyT(func(v GetListenerRulesResult) string { return v.ClbId }).(pulumi.StringOutput)
}

func (o GetListenerRulesResultOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListenerRulesResult) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetListenerRulesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetListenerRulesResult) string { return v.Id }).(pulumi.StringOutput)
}

// ID of the listener.
func (o GetListenerRulesResultOutput) ListenerId() pulumi.StringOutput {
	return o.ApplyT(func(v GetListenerRulesResult) string { return v.ListenerId }).(pulumi.StringOutput)
}

func (o GetListenerRulesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListenerRulesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

// ID of the rule.
func (o GetListenerRulesResultOutput) RuleId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListenerRulesResult) *string { return v.RuleId }).(pulumi.StringPtrOutput)
}

// A list of forward rules of listeners. Each element contains the following attributes:
func (o GetListenerRulesResultOutput) RuleLists() GetListenerRulesRuleListArrayOutput {
	return o.ApplyT(func(v GetListenerRulesResult) []GetListenerRulesRuleList { return v.RuleLists }).(GetListenerRulesRuleListArrayOutput)
}

// Scheduling method of the CLB listener, and available values include 'WRR', 'IP_HASH' and 'LEAST_CONN'. The default is 'WRR'. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in tencentcloud_clb_listener_rule.
func (o GetListenerRulesResultOutput) Scheduler() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListenerRulesResult) *string { return v.Scheduler }).(pulumi.StringPtrOutput)
}

func (o GetListenerRulesResultOutput) Url() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListenerRulesResult) *string { return v.Url }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetListenerRulesResultOutput{})
}
