// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package tcr

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this resource to create tcr instance.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Tcr"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Tcr.NewInstance(ctx, "foo", &Tcr.InstanceArgs{
// 			InstanceType: pulumi.String("basic"),
// 			Tags: pulumi.AnyMap{
// 				"test": pulumi.Any("tf"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// Using public network access whitelist
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Tcr"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Tcr"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Tcr.NewInstance(ctx, "foo", &Tcr.InstanceArgs{
// 			InstanceType:        pulumi.String("basic"),
// 			OpenPublicOperation: pulumi.Bool(true),
// 			SecurityPolicies: tcr.InstanceSecurityPolicyArray{
// 				&tcr.InstanceSecurityPolicyArgs{
// 					CidrBlock: pulumi.String("10.0.0.1/24"),
// 				},
// 				&tcr.InstanceSecurityPolicyArgs{
// 					CidrBlock: pulumi.String("192.168.1.1"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// tcr instance can be imported using the id, e.g.
//
// ```sh
//  $ pulumi import tencentcloud:Tcr/instance:Instance foo cls-cda1iex1
// ```
type Instance struct {
	pulumi.CustomResourceState

	// Indicate to delete the COS bucket which is auto-created with the instance or not.
	DeleteBucket pulumi.BoolPtrOutput `pulumi:"deleteBucket"`
	// TCR types. Valid values are: `standard`, `basic`, `premium`.
	InstanceType pulumi.StringOutput `pulumi:"instanceType"`
	// Internal address for access of the TCR instance.
	InternalEndPoint pulumi.StringOutput `pulumi:"internalEndPoint"`
	// Name of the TCR instance.
	Name pulumi.StringOutput `pulumi:"name"`
	// Control public network access.
	OpenPublicOperation pulumi.BoolPtrOutput `pulumi:"openPublicOperation"`
	// Public address for access of the TCR instance.
	PublicDomain pulumi.StringOutput `pulumi:"publicDomain"`
	// Status of the TCR instance public network access.
	PublicStatus pulumi.StringOutput `pulumi:"publicStatus"`
	// Public network access allowlist policies of the TCR instance. Only available when `openPublicOperation` is `true`.
	SecurityPolicies InstanceSecurityPolicyArrayOutput `pulumi:"securityPolicies"`
	// Status of the TCR instance.
	Status pulumi.StringOutput `pulumi:"status"`
	// The available tags within this TCR instance.
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceType == nil {
		return nil, errors.New("invalid value for required argument 'InstanceType'")
	}
	var resource Instance
	err := ctx.RegisterResource("tencentcloud:Tcr/instance:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("tencentcloud:Tcr/instance:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
	// Indicate to delete the COS bucket which is auto-created with the instance or not.
	DeleteBucket *bool `pulumi:"deleteBucket"`
	// TCR types. Valid values are: `standard`, `basic`, `premium`.
	InstanceType *string `pulumi:"instanceType"`
	// Internal address for access of the TCR instance.
	InternalEndPoint *string `pulumi:"internalEndPoint"`
	// Name of the TCR instance.
	Name *string `pulumi:"name"`
	// Control public network access.
	OpenPublicOperation *bool `pulumi:"openPublicOperation"`
	// Public address for access of the TCR instance.
	PublicDomain *string `pulumi:"publicDomain"`
	// Status of the TCR instance public network access.
	PublicStatus *string `pulumi:"publicStatus"`
	// Public network access allowlist policies of the TCR instance. Only available when `openPublicOperation` is `true`.
	SecurityPolicies []InstanceSecurityPolicy `pulumi:"securityPolicies"`
	// Status of the TCR instance.
	Status *string `pulumi:"status"`
	// The available tags within this TCR instance.
	Tags map[string]interface{} `pulumi:"tags"`
}

type InstanceState struct {
	// Indicate to delete the COS bucket which is auto-created with the instance or not.
	DeleteBucket pulumi.BoolPtrInput
	// TCR types. Valid values are: `standard`, `basic`, `premium`.
	InstanceType pulumi.StringPtrInput
	// Internal address for access of the TCR instance.
	InternalEndPoint pulumi.StringPtrInput
	// Name of the TCR instance.
	Name pulumi.StringPtrInput
	// Control public network access.
	OpenPublicOperation pulumi.BoolPtrInput
	// Public address for access of the TCR instance.
	PublicDomain pulumi.StringPtrInput
	// Status of the TCR instance public network access.
	PublicStatus pulumi.StringPtrInput
	// Public network access allowlist policies of the TCR instance. Only available when `openPublicOperation` is `true`.
	SecurityPolicies InstanceSecurityPolicyArrayInput
	// Status of the TCR instance.
	Status pulumi.StringPtrInput
	// The available tags within this TCR instance.
	Tags pulumi.MapInput
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// Indicate to delete the COS bucket which is auto-created with the instance or not.
	DeleteBucket *bool `pulumi:"deleteBucket"`
	// TCR types. Valid values are: `standard`, `basic`, `premium`.
	InstanceType string `pulumi:"instanceType"`
	// Name of the TCR instance.
	Name *string `pulumi:"name"`
	// Control public network access.
	OpenPublicOperation *bool `pulumi:"openPublicOperation"`
	// Public network access allowlist policies of the TCR instance. Only available when `openPublicOperation` is `true`.
	SecurityPolicies []InstanceSecurityPolicy `pulumi:"securityPolicies"`
	// The available tags within this TCR instance.
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// Indicate to delete the COS bucket which is auto-created with the instance or not.
	DeleteBucket pulumi.BoolPtrInput
	// TCR types. Valid values are: `standard`, `basic`, `premium`.
	InstanceType pulumi.StringInput
	// Name of the TCR instance.
	Name pulumi.StringPtrInput
	// Control public network access.
	OpenPublicOperation pulumi.BoolPtrInput
	// Public network access allowlist policies of the TCR instance. Only available when `openPublicOperation` is `true`.
	SecurityPolicies InstanceSecurityPolicyArrayInput
	// The available tags within this TCR instance.
	Tags pulumi.MapInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}

type InstanceInput interface {
	pulumi.Input

	ToInstanceOutput() InstanceOutput
	ToInstanceOutputWithContext(ctx context.Context) InstanceOutput
}

func (*Instance) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (i *Instance) ToInstanceOutput() InstanceOutput {
	return i.ToInstanceOutputWithContext(context.Background())
}

func (i *Instance) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceOutput)
}

// InstanceArrayInput is an input type that accepts InstanceArray and InstanceArrayOutput values.
// You can construct a concrete instance of `InstanceArrayInput` via:
//
//          InstanceArray{ InstanceArgs{...} }
type InstanceArrayInput interface {
	pulumi.Input

	ToInstanceArrayOutput() InstanceArrayOutput
	ToInstanceArrayOutputWithContext(context.Context) InstanceArrayOutput
}

type InstanceArray []InstanceInput

func (InstanceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Instance)(nil)).Elem()
}

func (i InstanceArray) ToInstanceArrayOutput() InstanceArrayOutput {
	return i.ToInstanceArrayOutputWithContext(context.Background())
}

func (i InstanceArray) ToInstanceArrayOutputWithContext(ctx context.Context) InstanceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceArrayOutput)
}

// InstanceMapInput is an input type that accepts InstanceMap and InstanceMapOutput values.
// You can construct a concrete instance of `InstanceMapInput` via:
//
//          InstanceMap{ "key": InstanceArgs{...} }
type InstanceMapInput interface {
	pulumi.Input

	ToInstanceMapOutput() InstanceMapOutput
	ToInstanceMapOutputWithContext(context.Context) InstanceMapOutput
}

type InstanceMap map[string]InstanceInput

func (InstanceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Instance)(nil)).Elem()
}

func (i InstanceMap) ToInstanceMapOutput() InstanceMapOutput {
	return i.ToInstanceMapOutputWithContext(context.Background())
}

func (i InstanceMap) ToInstanceMapOutputWithContext(ctx context.Context) InstanceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceMapOutput)
}

type InstanceOutput struct{ *pulumi.OutputState }

func (InstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (o InstanceOutput) ToInstanceOutput() InstanceOutput {
	return o
}

func (o InstanceOutput) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return o
}

// Indicate to delete the COS bucket which is auto-created with the instance or not.
func (o InstanceOutput) DeleteBucket() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.BoolPtrOutput { return v.DeleteBucket }).(pulumi.BoolPtrOutput)
}

// TCR types. Valid values are: `standard`, `basic`, `premium`.
func (o InstanceOutput) InstanceType() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.InstanceType }).(pulumi.StringOutput)
}

// Internal address for access of the TCR instance.
func (o InstanceOutput) InternalEndPoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.InternalEndPoint }).(pulumi.StringOutput)
}

// Name of the TCR instance.
func (o InstanceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Control public network access.
func (o InstanceOutput) OpenPublicOperation() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.BoolPtrOutput { return v.OpenPublicOperation }).(pulumi.BoolPtrOutput)
}

// Public address for access of the TCR instance.
func (o InstanceOutput) PublicDomain() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.PublicDomain }).(pulumi.StringOutput)
}

// Status of the TCR instance public network access.
func (o InstanceOutput) PublicStatus() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.PublicStatus }).(pulumi.StringOutput)
}

// Public network access allowlist policies of the TCR instance. Only available when `openPublicOperation` is `true`.
func (o InstanceOutput) SecurityPolicies() InstanceSecurityPolicyArrayOutput {
	return o.ApplyT(func(v *Instance) InstanceSecurityPolicyArrayOutput { return v.SecurityPolicies }).(InstanceSecurityPolicyArrayOutput)
}

// Status of the TCR instance.
func (o InstanceOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// The available tags within this TCR instance.
func (o InstanceOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v *Instance) pulumi.MapOutput { return v.Tags }).(pulumi.MapOutput)
}

type InstanceArrayOutput struct{ *pulumi.OutputState }

func (InstanceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Instance)(nil)).Elem()
}

func (o InstanceArrayOutput) ToInstanceArrayOutput() InstanceArrayOutput {
	return o
}

func (o InstanceArrayOutput) ToInstanceArrayOutputWithContext(ctx context.Context) InstanceArrayOutput {
	return o
}

func (o InstanceArrayOutput) Index(i pulumi.IntInput) InstanceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Instance {
		return vs[0].([]*Instance)[vs[1].(int)]
	}).(InstanceOutput)
}

type InstanceMapOutput struct{ *pulumi.OutputState }

func (InstanceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Instance)(nil)).Elem()
}

func (o InstanceMapOutput) ToInstanceMapOutput() InstanceMapOutput {
	return o
}

func (o InstanceMapOutput) ToInstanceMapOutputWithContext(ctx context.Context) InstanceMapOutput {
	return o
}

func (o InstanceMapOutput) MapIndex(k pulumi.StringInput) InstanceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Instance {
		return vs[0].(map[string]*Instance)[vs[1].(string)]
	}).(InstanceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceInput)(nil)).Elem(), &Instance{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceArrayInput)(nil)).Elem(), InstanceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceMapInput)(nil)).Elem(), InstanceMap{})
	pulumi.RegisterOutputType(InstanceOutput{})
	pulumi.RegisterOutputType(InstanceArrayOutput{})
	pulumi.RegisterOutputType(InstanceMapOutput{})
}
