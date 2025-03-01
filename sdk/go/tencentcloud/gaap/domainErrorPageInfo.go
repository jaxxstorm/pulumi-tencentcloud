// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gaap

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type DomainErrorPageInfo struct {
	pulumi.CustomResourceState

	// New response body.
	Body pulumi.StringOutput `pulumi:"body"`
	// Response headers to be removed.
	ClearHeaders pulumi.StringArrayOutput `pulumi:"clearHeaders"`
	// HTTP domain.
	Domain pulumi.StringOutput `pulumi:"domain"`
	// Original error codes.
	ErrorCodes pulumi.IntArrayOutput `pulumi:"errorCodes"`
	// ID of the layer7 listener.
	ListenerId pulumi.StringOutput `pulumi:"listenerId"`
	// New error code.
	NewErrorCode pulumi.IntPtrOutput `pulumi:"newErrorCode"`
	// Response headers to be set.
	SetHeaders pulumi.MapOutput `pulumi:"setHeaders"`
}

// NewDomainErrorPageInfo registers a new resource with the given unique name, arguments, and options.
func NewDomainErrorPageInfo(ctx *pulumi.Context,
	name string, args *DomainErrorPageInfoArgs, opts ...pulumi.ResourceOption) (*DomainErrorPageInfo, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Body == nil {
		return nil, errors.New("invalid value for required argument 'Body'")
	}
	if args.Domain == nil {
		return nil, errors.New("invalid value for required argument 'Domain'")
	}
	if args.ErrorCodes == nil {
		return nil, errors.New("invalid value for required argument 'ErrorCodes'")
	}
	if args.ListenerId == nil {
		return nil, errors.New("invalid value for required argument 'ListenerId'")
	}
	var resource DomainErrorPageInfo
	err := ctx.RegisterResource("tencentcloud:Gaap/domainErrorPageInfo:DomainErrorPageInfo", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomainErrorPageInfo gets an existing DomainErrorPageInfo resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomainErrorPageInfo(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainErrorPageInfoState, opts ...pulumi.ResourceOption) (*DomainErrorPageInfo, error) {
	var resource DomainErrorPageInfo
	err := ctx.ReadResource("tencentcloud:Gaap/domainErrorPageInfo:DomainErrorPageInfo", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DomainErrorPageInfo resources.
type domainErrorPageInfoState struct {
	// New response body.
	Body *string `pulumi:"body"`
	// Response headers to be removed.
	ClearHeaders []string `pulumi:"clearHeaders"`
	// HTTP domain.
	Domain *string `pulumi:"domain"`
	// Original error codes.
	ErrorCodes []int `pulumi:"errorCodes"`
	// ID of the layer7 listener.
	ListenerId *string `pulumi:"listenerId"`
	// New error code.
	NewErrorCode *int `pulumi:"newErrorCode"`
	// Response headers to be set.
	SetHeaders map[string]interface{} `pulumi:"setHeaders"`
}

type DomainErrorPageInfoState struct {
	// New response body.
	Body pulumi.StringPtrInput
	// Response headers to be removed.
	ClearHeaders pulumi.StringArrayInput
	// HTTP domain.
	Domain pulumi.StringPtrInput
	// Original error codes.
	ErrorCodes pulumi.IntArrayInput
	// ID of the layer7 listener.
	ListenerId pulumi.StringPtrInput
	// New error code.
	NewErrorCode pulumi.IntPtrInput
	// Response headers to be set.
	SetHeaders pulumi.MapInput
}

func (DomainErrorPageInfoState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainErrorPageInfoState)(nil)).Elem()
}

type domainErrorPageInfoArgs struct {
	// New response body.
	Body string `pulumi:"body"`
	// Response headers to be removed.
	ClearHeaders []string `pulumi:"clearHeaders"`
	// HTTP domain.
	Domain string `pulumi:"domain"`
	// Original error codes.
	ErrorCodes []int `pulumi:"errorCodes"`
	// ID of the layer7 listener.
	ListenerId string `pulumi:"listenerId"`
	// New error code.
	NewErrorCode *int `pulumi:"newErrorCode"`
	// Response headers to be set.
	SetHeaders map[string]interface{} `pulumi:"setHeaders"`
}

// The set of arguments for constructing a DomainErrorPageInfo resource.
type DomainErrorPageInfoArgs struct {
	// New response body.
	Body pulumi.StringInput
	// Response headers to be removed.
	ClearHeaders pulumi.StringArrayInput
	// HTTP domain.
	Domain pulumi.StringInput
	// Original error codes.
	ErrorCodes pulumi.IntArrayInput
	// ID of the layer7 listener.
	ListenerId pulumi.StringInput
	// New error code.
	NewErrorCode pulumi.IntPtrInput
	// Response headers to be set.
	SetHeaders pulumi.MapInput
}

func (DomainErrorPageInfoArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainErrorPageInfoArgs)(nil)).Elem()
}

type DomainErrorPageInfoInput interface {
	pulumi.Input

	ToDomainErrorPageInfoOutput() DomainErrorPageInfoOutput
	ToDomainErrorPageInfoOutputWithContext(ctx context.Context) DomainErrorPageInfoOutput
}

func (*DomainErrorPageInfo) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainErrorPageInfo)(nil)).Elem()
}

func (i *DomainErrorPageInfo) ToDomainErrorPageInfoOutput() DomainErrorPageInfoOutput {
	return i.ToDomainErrorPageInfoOutputWithContext(context.Background())
}

func (i *DomainErrorPageInfo) ToDomainErrorPageInfoOutputWithContext(ctx context.Context) DomainErrorPageInfoOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainErrorPageInfoOutput)
}

// DomainErrorPageInfoArrayInput is an input type that accepts DomainErrorPageInfoArray and DomainErrorPageInfoArrayOutput values.
// You can construct a concrete instance of `DomainErrorPageInfoArrayInput` via:
//
//          DomainErrorPageInfoArray{ DomainErrorPageInfoArgs{...} }
type DomainErrorPageInfoArrayInput interface {
	pulumi.Input

	ToDomainErrorPageInfoArrayOutput() DomainErrorPageInfoArrayOutput
	ToDomainErrorPageInfoArrayOutputWithContext(context.Context) DomainErrorPageInfoArrayOutput
}

type DomainErrorPageInfoArray []DomainErrorPageInfoInput

func (DomainErrorPageInfoArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DomainErrorPageInfo)(nil)).Elem()
}

func (i DomainErrorPageInfoArray) ToDomainErrorPageInfoArrayOutput() DomainErrorPageInfoArrayOutput {
	return i.ToDomainErrorPageInfoArrayOutputWithContext(context.Background())
}

func (i DomainErrorPageInfoArray) ToDomainErrorPageInfoArrayOutputWithContext(ctx context.Context) DomainErrorPageInfoArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainErrorPageInfoArrayOutput)
}

// DomainErrorPageInfoMapInput is an input type that accepts DomainErrorPageInfoMap and DomainErrorPageInfoMapOutput values.
// You can construct a concrete instance of `DomainErrorPageInfoMapInput` via:
//
//          DomainErrorPageInfoMap{ "key": DomainErrorPageInfoArgs{...} }
type DomainErrorPageInfoMapInput interface {
	pulumi.Input

	ToDomainErrorPageInfoMapOutput() DomainErrorPageInfoMapOutput
	ToDomainErrorPageInfoMapOutputWithContext(context.Context) DomainErrorPageInfoMapOutput
}

type DomainErrorPageInfoMap map[string]DomainErrorPageInfoInput

func (DomainErrorPageInfoMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DomainErrorPageInfo)(nil)).Elem()
}

func (i DomainErrorPageInfoMap) ToDomainErrorPageInfoMapOutput() DomainErrorPageInfoMapOutput {
	return i.ToDomainErrorPageInfoMapOutputWithContext(context.Background())
}

func (i DomainErrorPageInfoMap) ToDomainErrorPageInfoMapOutputWithContext(ctx context.Context) DomainErrorPageInfoMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainErrorPageInfoMapOutput)
}

type DomainErrorPageInfoOutput struct{ *pulumi.OutputState }

func (DomainErrorPageInfoOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainErrorPageInfo)(nil)).Elem()
}

func (o DomainErrorPageInfoOutput) ToDomainErrorPageInfoOutput() DomainErrorPageInfoOutput {
	return o
}

func (o DomainErrorPageInfoOutput) ToDomainErrorPageInfoOutputWithContext(ctx context.Context) DomainErrorPageInfoOutput {
	return o
}

// New response body.
func (o DomainErrorPageInfoOutput) Body() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainErrorPageInfo) pulumi.StringOutput { return v.Body }).(pulumi.StringOutput)
}

// Response headers to be removed.
func (o DomainErrorPageInfoOutput) ClearHeaders() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DomainErrorPageInfo) pulumi.StringArrayOutput { return v.ClearHeaders }).(pulumi.StringArrayOutput)
}

// HTTP domain.
func (o DomainErrorPageInfoOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainErrorPageInfo) pulumi.StringOutput { return v.Domain }).(pulumi.StringOutput)
}

// Original error codes.
func (o DomainErrorPageInfoOutput) ErrorCodes() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *DomainErrorPageInfo) pulumi.IntArrayOutput { return v.ErrorCodes }).(pulumi.IntArrayOutput)
}

// ID of the layer7 listener.
func (o DomainErrorPageInfoOutput) ListenerId() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainErrorPageInfo) pulumi.StringOutput { return v.ListenerId }).(pulumi.StringOutput)
}

// New error code.
func (o DomainErrorPageInfoOutput) NewErrorCode() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DomainErrorPageInfo) pulumi.IntPtrOutput { return v.NewErrorCode }).(pulumi.IntPtrOutput)
}

// Response headers to be set.
func (o DomainErrorPageInfoOutput) SetHeaders() pulumi.MapOutput {
	return o.ApplyT(func(v *DomainErrorPageInfo) pulumi.MapOutput { return v.SetHeaders }).(pulumi.MapOutput)
}

type DomainErrorPageInfoArrayOutput struct{ *pulumi.OutputState }

func (DomainErrorPageInfoArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DomainErrorPageInfo)(nil)).Elem()
}

func (o DomainErrorPageInfoArrayOutput) ToDomainErrorPageInfoArrayOutput() DomainErrorPageInfoArrayOutput {
	return o
}

func (o DomainErrorPageInfoArrayOutput) ToDomainErrorPageInfoArrayOutputWithContext(ctx context.Context) DomainErrorPageInfoArrayOutput {
	return o
}

func (o DomainErrorPageInfoArrayOutput) Index(i pulumi.IntInput) DomainErrorPageInfoOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DomainErrorPageInfo {
		return vs[0].([]*DomainErrorPageInfo)[vs[1].(int)]
	}).(DomainErrorPageInfoOutput)
}

type DomainErrorPageInfoMapOutput struct{ *pulumi.OutputState }

func (DomainErrorPageInfoMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DomainErrorPageInfo)(nil)).Elem()
}

func (o DomainErrorPageInfoMapOutput) ToDomainErrorPageInfoMapOutput() DomainErrorPageInfoMapOutput {
	return o
}

func (o DomainErrorPageInfoMapOutput) ToDomainErrorPageInfoMapOutputWithContext(ctx context.Context) DomainErrorPageInfoMapOutput {
	return o
}

func (o DomainErrorPageInfoMapOutput) MapIndex(k pulumi.StringInput) DomainErrorPageInfoOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DomainErrorPageInfo {
		return vs[0].(map[string]*DomainErrorPageInfo)[vs[1].(string)]
	}).(DomainErrorPageInfoOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DomainErrorPageInfoInput)(nil)).Elem(), &DomainErrorPageInfo{})
	pulumi.RegisterInputType(reflect.TypeOf((*DomainErrorPageInfoArrayInput)(nil)).Elem(), DomainErrorPageInfoArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DomainErrorPageInfoMapInput)(nil)).Elem(), DomainErrorPageInfoMap{})
	pulumi.RegisterOutputType(DomainErrorPageInfoOutput{})
	pulumi.RegisterOutputType(DomainErrorPageInfoArrayOutput{})
	pulumi.RegisterOutputType(DomainErrorPageInfoMapOutput{})
}
