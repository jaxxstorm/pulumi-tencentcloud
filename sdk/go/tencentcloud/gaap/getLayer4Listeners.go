// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gaap

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query gaap layer4 listeners.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Gaap"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Gaap"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		fooProxy, err := Gaap.NewProxy(ctx, "fooProxy", &Gaap.ProxyArgs{
// 			Bandwidth:        pulumi.Int(10),
// 			Concurrent:       pulumi.Int(2),
// 			AccessRegion:     pulumi.String("SouthChina"),
// 			RealserverRegion: pulumi.String("NorthChina"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooRealserver, err := Gaap.NewRealserver(ctx, "fooRealserver", &Gaap.RealserverArgs{
// 			Ip: pulumi.String("1.1.1.1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooLayer4Listener, err := Gaap.NewLayer4Listener(ctx, "fooLayer4Listener", &Gaap.Layer4ListenerArgs{
// 			Protocol:       pulumi.String("TCP"),
// 			Port:           pulumi.Int(80),
// 			RealserverType: pulumi.String("IP"),
// 			ProxyId:        fooProxy.ID(),
// 			HealthCheck:    pulumi.Bool(true),
// 			Interval:       pulumi.Int(5),
// 			ConnectTimeout: pulumi.Int(2),
// 			RealserverBindSets: gaap.Layer4ListenerRealserverBindSetArray{
// 				&gaap.Layer4ListenerRealserverBindSetArgs{
// 					Id:   fooRealserver.ID(),
// 					Ip:   fooRealserver.Ip,
// 					Port: pulumi.Int(80),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_ = Gaap.GetLayer4ListenersOutput(ctx, gaap.GetLayer4ListenersOutputArgs{
// 			Protocol:   pulumi.String("TCP"),
// 			ProxyId:    fooProxy.ID(),
// 			ListenerId: fooLayer4Listener.ID(),
// 		}, nil)
// 		return nil
// 	})
// }
// ```
func GetLayer4Listeners(ctx *pulumi.Context, args *GetLayer4ListenersArgs, opts ...pulumi.InvokeOption) (*GetLayer4ListenersResult, error) {
	var rv GetLayer4ListenersResult
	err := ctx.Invoke("tencentcloud:Gaap/getLayer4Listeners:getLayer4Listeners", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLayer4Listeners.
type GetLayer4ListenersArgs struct {
	// ID of the layer4 listener to be queried.
	ListenerId *string `pulumi:"listenerId"`
	// Name of the layer4 listener to be queried.
	ListenerName *string `pulumi:"listenerName"`
	// Port of the layer4 listener to be queried.
	Port *int `pulumi:"port"`
	// Protocol of the layer4 listener to be queried. Valid values: `TCP` and `UDP`.
	Protocol string `pulumi:"protocol"`
	// ID of the GAAP proxy to be queried.
	ProxyId *string `pulumi:"proxyId"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by getLayer4Listeners.
type GetLayer4ListenersResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id           string  `pulumi:"id"`
	ListenerId   *string `pulumi:"listenerId"`
	ListenerName *string `pulumi:"listenerName"`
	// An information list of layer4 listeners. Each element contains the following attributes:
	Listeners []GetLayer4ListenersListener `pulumi:"listeners"`
	// Port of the layer4 listener.
	Port *int `pulumi:"port"`
	// Protocol of the layer4 listener.
	Protocol         string  `pulumi:"protocol"`
	ProxyId          *string `pulumi:"proxyId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

func GetLayer4ListenersOutput(ctx *pulumi.Context, args GetLayer4ListenersOutputArgs, opts ...pulumi.InvokeOption) GetLayer4ListenersResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetLayer4ListenersResult, error) {
			args := v.(GetLayer4ListenersArgs)
			r, err := GetLayer4Listeners(ctx, &args, opts...)
			var s GetLayer4ListenersResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetLayer4ListenersResultOutput)
}

// A collection of arguments for invoking getLayer4Listeners.
type GetLayer4ListenersOutputArgs struct {
	// ID of the layer4 listener to be queried.
	ListenerId pulumi.StringPtrInput `pulumi:"listenerId"`
	// Name of the layer4 listener to be queried.
	ListenerName pulumi.StringPtrInput `pulumi:"listenerName"`
	// Port of the layer4 listener to be queried.
	Port pulumi.IntPtrInput `pulumi:"port"`
	// Protocol of the layer4 listener to be queried. Valid values: `TCP` and `UDP`.
	Protocol pulumi.StringInput `pulumi:"protocol"`
	// ID of the GAAP proxy to be queried.
	ProxyId pulumi.StringPtrInput `pulumi:"proxyId"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (GetLayer4ListenersOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetLayer4ListenersArgs)(nil)).Elem()
}

// A collection of values returned by getLayer4Listeners.
type GetLayer4ListenersResultOutput struct{ *pulumi.OutputState }

func (GetLayer4ListenersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetLayer4ListenersResult)(nil)).Elem()
}

func (o GetLayer4ListenersResultOutput) ToGetLayer4ListenersResultOutput() GetLayer4ListenersResultOutput {
	return o
}

func (o GetLayer4ListenersResultOutput) ToGetLayer4ListenersResultOutputWithContext(ctx context.Context) GetLayer4ListenersResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetLayer4ListenersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetLayer4ListenersResultOutput) ListenerId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) *string { return v.ListenerId }).(pulumi.StringPtrOutput)
}

func (o GetLayer4ListenersResultOutput) ListenerName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) *string { return v.ListenerName }).(pulumi.StringPtrOutput)
}

// An information list of layer4 listeners. Each element contains the following attributes:
func (o GetLayer4ListenersResultOutput) Listeners() GetLayer4ListenersListenerArrayOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) []GetLayer4ListenersListener { return v.Listeners }).(GetLayer4ListenersListenerArrayOutput)
}

// Port of the layer4 listener.
func (o GetLayer4ListenersResultOutput) Port() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) *int { return v.Port }).(pulumi.IntPtrOutput)
}

// Protocol of the layer4 listener.
func (o GetLayer4ListenersResultOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) string { return v.Protocol }).(pulumi.StringOutput)
}

func (o GetLayer4ListenersResultOutput) ProxyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) *string { return v.ProxyId }).(pulumi.StringPtrOutput)
}

func (o GetLayer4ListenersResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetLayer4ListenersResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetLayer4ListenersResultOutput{})
}
