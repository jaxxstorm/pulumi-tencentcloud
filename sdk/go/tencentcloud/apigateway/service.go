// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Service struct {
	pulumi.CustomResourceState

	// A list of APIs.
	ApiLists ServiceApiListArrayOutput `pulumi:"apiLists"`
	// Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.
	ExclusiveSetName pulumi.StringPtrOutput `pulumi:"exclusiveSetName"`
	// Port number for http access over private network.
	InnerHttpPort pulumi.IntOutput `pulumi:"innerHttpPort"`
	// Port number for https access over private network.
	InnerHttpsPort pulumi.IntOutput `pulumi:"innerHttpsPort"`
	// Private network access subdomain name.
	InternalSubDomain pulumi.StringOutput `pulumi:"internalSubDomain"`
	// IP version number. Valid values: `IPv4`, `IPv6`. Default value: `IPv4`.
	IpVersion pulumi.StringPtrOutput `pulumi:"ipVersion"`
	// Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
	ModifyTime pulumi.StringOutput `pulumi:"modifyTime"`
	// Network type list, which is used to specify the supported network types. Valid values: `INNER`, `OUTER`. `INNER`
	// indicates access over private network, and `OUTER` indicates access over public network.
	NetTypes pulumi.StringArrayOutput `pulumi:"netTypes"`
	// Public network access subdomain name.
	OuterSubDomain pulumi.StringOutput `pulumi:"outerSubDomain"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	PreLimit pulumi.IntOutput `pulumi:"preLimit"`
	// Service frontend request type. Valid values: `http`, `https`, `http&https`.
	Protocol pulumi.StringOutput `pulumi:"protocol"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	ReleaseLimit pulumi.IntOutput `pulumi:"releaseLimit"`
	// Custom service description.
	ServiceDesc pulumi.StringPtrOutput `pulumi:"serviceDesc"`
	// Custom service name.
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	TestLimit pulumi.IntOutput `pulumi:"testLimit"`
	// A list of attach usage plans.
	UsagePlanLists ServiceUsagePlanListArrayOutput `pulumi:"usagePlanLists"`
}

// NewService registers a new resource with the given unique name, arguments, and options.
func NewService(ctx *pulumi.Context,
	name string, args *ServiceArgs, opts ...pulumi.ResourceOption) (*Service, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.NetTypes == nil {
		return nil, errors.New("invalid value for required argument 'NetTypes'")
	}
	if args.Protocol == nil {
		return nil, errors.New("invalid value for required argument 'Protocol'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	var resource Service
	err := ctx.RegisterResource("tencentcloud:APIGateway/service:Service", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetService gets an existing Service resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceState, opts ...pulumi.ResourceOption) (*Service, error) {
	var resource Service
	err := ctx.ReadResource("tencentcloud:APIGateway/service:Service", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Service resources.
type serviceState struct {
	// A list of APIs.
	ApiLists []ServiceApiList `pulumi:"apiLists"`
	// Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
	CreateTime *string `pulumi:"createTime"`
	// Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.
	ExclusiveSetName *string `pulumi:"exclusiveSetName"`
	// Port number for http access over private network.
	InnerHttpPort *int `pulumi:"innerHttpPort"`
	// Port number for https access over private network.
	InnerHttpsPort *int `pulumi:"innerHttpsPort"`
	// Private network access subdomain name.
	InternalSubDomain *string `pulumi:"internalSubDomain"`
	// IP version number. Valid values: `IPv4`, `IPv6`. Default value: `IPv4`.
	IpVersion *string `pulumi:"ipVersion"`
	// Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
	ModifyTime *string `pulumi:"modifyTime"`
	// Network type list, which is used to specify the supported network types. Valid values: `INNER`, `OUTER`. `INNER`
	// indicates access over private network, and `OUTER` indicates access over public network.
	NetTypes []string `pulumi:"netTypes"`
	// Public network access subdomain name.
	OuterSubDomain *string `pulumi:"outerSubDomain"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	PreLimit *int `pulumi:"preLimit"`
	// Service frontend request type. Valid values: `http`, `https`, `http&https`.
	Protocol *string `pulumi:"protocol"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	ReleaseLimit *int `pulumi:"releaseLimit"`
	// Custom service description.
	ServiceDesc *string `pulumi:"serviceDesc"`
	// Custom service name.
	ServiceName *string `pulumi:"serviceName"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	TestLimit *int `pulumi:"testLimit"`
	// A list of attach usage plans.
	UsagePlanLists []ServiceUsagePlanList `pulumi:"usagePlanLists"`
}

type ServiceState struct {
	// A list of APIs.
	ApiLists ServiceApiListArrayInput
	// Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
	CreateTime pulumi.StringPtrInput
	// Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.
	ExclusiveSetName pulumi.StringPtrInput
	// Port number for http access over private network.
	InnerHttpPort pulumi.IntPtrInput
	// Port number for https access over private network.
	InnerHttpsPort pulumi.IntPtrInput
	// Private network access subdomain name.
	InternalSubDomain pulumi.StringPtrInput
	// IP version number. Valid values: `IPv4`, `IPv6`. Default value: `IPv4`.
	IpVersion pulumi.StringPtrInput
	// Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
	ModifyTime pulumi.StringPtrInput
	// Network type list, which is used to specify the supported network types. Valid values: `INNER`, `OUTER`. `INNER`
	// indicates access over private network, and `OUTER` indicates access over public network.
	NetTypes pulumi.StringArrayInput
	// Public network access subdomain name.
	OuterSubDomain pulumi.StringPtrInput
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	PreLimit pulumi.IntPtrInput
	// Service frontend request type. Valid values: `http`, `https`, `http&https`.
	Protocol pulumi.StringPtrInput
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	ReleaseLimit pulumi.IntPtrInput
	// Custom service description.
	ServiceDesc pulumi.StringPtrInput
	// Custom service name.
	ServiceName pulumi.StringPtrInput
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	TestLimit pulumi.IntPtrInput
	// A list of attach usage plans.
	UsagePlanLists ServiceUsagePlanListArrayInput
}

func (ServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceState)(nil)).Elem()
}

type serviceArgs struct {
	// Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.
	ExclusiveSetName *string `pulumi:"exclusiveSetName"`
	// IP version number. Valid values: `IPv4`, `IPv6`. Default value: `IPv4`.
	IpVersion *string `pulumi:"ipVersion"`
	// Network type list, which is used to specify the supported network types. Valid values: `INNER`, `OUTER`. `INNER`
	// indicates access over private network, and `OUTER` indicates access over public network.
	NetTypes []string `pulumi:"netTypes"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	PreLimit *int `pulumi:"preLimit"`
	// Service frontend request type. Valid values: `http`, `https`, `http&https`.
	Protocol string `pulumi:"protocol"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	ReleaseLimit *int `pulumi:"releaseLimit"`
	// Custom service description.
	ServiceDesc *string `pulumi:"serviceDesc"`
	// Custom service name.
	ServiceName string `pulumi:"serviceName"`
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	TestLimit *int `pulumi:"testLimit"`
}

// The set of arguments for constructing a Service resource.
type ServiceArgs struct {
	// Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.
	ExclusiveSetName pulumi.StringPtrInput
	// IP version number. Valid values: `IPv4`, `IPv6`. Default value: `IPv4`.
	IpVersion pulumi.StringPtrInput
	// Network type list, which is used to specify the supported network types. Valid values: `INNER`, `OUTER`. `INNER`
	// indicates access over private network, and `OUTER` indicates access over public network.
	NetTypes pulumi.StringArrayInput
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	PreLimit pulumi.IntPtrInput
	// Service frontend request type. Valid values: `http`, `https`, `http&https`.
	Protocol pulumi.StringInput
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	ReleaseLimit pulumi.IntPtrInput
	// Custom service description.
	ServiceDesc pulumi.StringPtrInput
	// Custom service name.
	ServiceName pulumi.StringInput
	// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
	TestLimit pulumi.IntPtrInput
}

func (ServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceArgs)(nil)).Elem()
}

type ServiceInput interface {
	pulumi.Input

	ToServiceOutput() ServiceOutput
	ToServiceOutputWithContext(ctx context.Context) ServiceOutput
}

func (*Service) ElementType() reflect.Type {
	return reflect.TypeOf((**Service)(nil)).Elem()
}

func (i *Service) ToServiceOutput() ServiceOutput {
	return i.ToServiceOutputWithContext(context.Background())
}

func (i *Service) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceOutput)
}

// ServiceArrayInput is an input type that accepts ServiceArray and ServiceArrayOutput values.
// You can construct a concrete instance of `ServiceArrayInput` via:
//
//          ServiceArray{ ServiceArgs{...} }
type ServiceArrayInput interface {
	pulumi.Input

	ToServiceArrayOutput() ServiceArrayOutput
	ToServiceArrayOutputWithContext(context.Context) ServiceArrayOutput
}

type ServiceArray []ServiceInput

func (ServiceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Service)(nil)).Elem()
}

func (i ServiceArray) ToServiceArrayOutput() ServiceArrayOutput {
	return i.ToServiceArrayOutputWithContext(context.Background())
}

func (i ServiceArray) ToServiceArrayOutputWithContext(ctx context.Context) ServiceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceArrayOutput)
}

// ServiceMapInput is an input type that accepts ServiceMap and ServiceMapOutput values.
// You can construct a concrete instance of `ServiceMapInput` via:
//
//          ServiceMap{ "key": ServiceArgs{...} }
type ServiceMapInput interface {
	pulumi.Input

	ToServiceMapOutput() ServiceMapOutput
	ToServiceMapOutputWithContext(context.Context) ServiceMapOutput
}

type ServiceMap map[string]ServiceInput

func (ServiceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Service)(nil)).Elem()
}

func (i ServiceMap) ToServiceMapOutput() ServiceMapOutput {
	return i.ToServiceMapOutputWithContext(context.Background())
}

func (i ServiceMap) ToServiceMapOutputWithContext(ctx context.Context) ServiceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceMapOutput)
}

type ServiceOutput struct{ *pulumi.OutputState }

func (ServiceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Service)(nil)).Elem()
}

func (o ServiceOutput) ToServiceOutput() ServiceOutput {
	return o
}

func (o ServiceOutput) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return o
}

// A list of APIs.
func (o ServiceOutput) ApiLists() ServiceApiListArrayOutput {
	return o.ApplyT(func(v *Service) ServiceApiListArrayOutput { return v.ApiLists }).(ServiceApiListArrayOutput)
}

// Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
func (o ServiceOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Service) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.
func (o ServiceOutput) ExclusiveSetName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Service) pulumi.StringPtrOutput { return v.ExclusiveSetName }).(pulumi.StringPtrOutput)
}

// Port number for http access over private network.
func (o ServiceOutput) InnerHttpPort() pulumi.IntOutput {
	return o.ApplyT(func(v *Service) pulumi.IntOutput { return v.InnerHttpPort }).(pulumi.IntOutput)
}

// Port number for https access over private network.
func (o ServiceOutput) InnerHttpsPort() pulumi.IntOutput {
	return o.ApplyT(func(v *Service) pulumi.IntOutput { return v.InnerHttpsPort }).(pulumi.IntOutput)
}

// Private network access subdomain name.
func (o ServiceOutput) InternalSubDomain() pulumi.StringOutput {
	return o.ApplyT(func(v *Service) pulumi.StringOutput { return v.InternalSubDomain }).(pulumi.StringOutput)
}

// IP version number. Valid values: `IPv4`, `IPv6`. Default value: `IPv4`.
func (o ServiceOutput) IpVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Service) pulumi.StringPtrOutput { return v.IpVersion }).(pulumi.StringPtrOutput)
}

// Last modified time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
func (o ServiceOutput) ModifyTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Service) pulumi.StringOutput { return v.ModifyTime }).(pulumi.StringOutput)
}

// Network type list, which is used to specify the supported network types. Valid values: `INNER`, `OUTER`. `INNER`
// indicates access over private network, and `OUTER` indicates access over public network.
func (o ServiceOutput) NetTypes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Service) pulumi.StringArrayOutput { return v.NetTypes }).(pulumi.StringArrayOutput)
}

// Public network access subdomain name.
func (o ServiceOutput) OuterSubDomain() pulumi.StringOutput {
	return o.ApplyT(func(v *Service) pulumi.StringOutput { return v.OuterSubDomain }).(pulumi.StringOutput)
}

// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
func (o ServiceOutput) PreLimit() pulumi.IntOutput {
	return o.ApplyT(func(v *Service) pulumi.IntOutput { return v.PreLimit }).(pulumi.IntOutput)
}

// Service frontend request type. Valid values: `http`, `https`, `http&https`.
func (o ServiceOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v *Service) pulumi.StringOutput { return v.Protocol }).(pulumi.StringOutput)
}

// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
func (o ServiceOutput) ReleaseLimit() pulumi.IntOutput {
	return o.ApplyT(func(v *Service) pulumi.IntOutput { return v.ReleaseLimit }).(pulumi.IntOutput)
}

// Custom service description.
func (o ServiceOutput) ServiceDesc() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Service) pulumi.StringPtrOutput { return v.ServiceDesc }).(pulumi.StringPtrOutput)
}

// Custom service name.
func (o ServiceOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Service) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// API QPS value. Enter a positive number to limit the API query rate per second `QPS`.
func (o ServiceOutput) TestLimit() pulumi.IntOutput {
	return o.ApplyT(func(v *Service) pulumi.IntOutput { return v.TestLimit }).(pulumi.IntOutput)
}

// A list of attach usage plans.
func (o ServiceOutput) UsagePlanLists() ServiceUsagePlanListArrayOutput {
	return o.ApplyT(func(v *Service) ServiceUsagePlanListArrayOutput { return v.UsagePlanLists }).(ServiceUsagePlanListArrayOutput)
}

type ServiceArrayOutput struct{ *pulumi.OutputState }

func (ServiceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Service)(nil)).Elem()
}

func (o ServiceArrayOutput) ToServiceArrayOutput() ServiceArrayOutput {
	return o
}

func (o ServiceArrayOutput) ToServiceArrayOutputWithContext(ctx context.Context) ServiceArrayOutput {
	return o
}

func (o ServiceArrayOutput) Index(i pulumi.IntInput) ServiceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Service {
		return vs[0].([]*Service)[vs[1].(int)]
	}).(ServiceOutput)
}

type ServiceMapOutput struct{ *pulumi.OutputState }

func (ServiceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Service)(nil)).Elem()
}

func (o ServiceMapOutput) ToServiceMapOutput() ServiceMapOutput {
	return o
}

func (o ServiceMapOutput) ToServiceMapOutputWithContext(ctx context.Context) ServiceMapOutput {
	return o
}

func (o ServiceMapOutput) MapIndex(k pulumi.StringInput) ServiceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Service {
		return vs[0].(map[string]*Service)[vs[1].(string)]
	}).(ServiceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceInput)(nil)).Elem(), &Service{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceArrayInput)(nil)).Elem(), ServiceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceMapInput)(nil)).Elem(), ServiceMap{})
	pulumi.RegisterOutputType(ServiceOutput{})
	pulumi.RegisterOutputType(ServiceArrayOutput{})
	pulumi.RegisterOutputType(ServiceMapOutput{})
}
