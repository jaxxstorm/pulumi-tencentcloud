// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package tke

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AuthAttachment struct {
	pulumi.CustomResourceState

	// If set to `true`, the rbac rule will be created automatically which allow anonymous user to access
	// '/.well-known/openid-configuration' and '/openid/v1/jwks'.
	AutoCreateDiscoveryAnonymousAuth pulumi.BoolPtrOutput `pulumi:"autoCreateDiscoveryAnonymousAuth"`
	// ID of clusters.
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// Specify service-account-issuer.
	Issuer pulumi.StringOutput `pulumi:"issuer"`
	// Specify service-account-jwks-uri.
	JwksUri pulumi.StringPtrOutput `pulumi:"jwksUri"`
}

// NewAuthAttachment registers a new resource with the given unique name, arguments, and options.
func NewAuthAttachment(ctx *pulumi.Context,
	name string, args *AuthAttachmentArgs, opts ...pulumi.ResourceOption) (*AuthAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.Issuer == nil {
		return nil, errors.New("invalid value for required argument 'Issuer'")
	}
	var resource AuthAttachment
	err := ctx.RegisterResource("tencentcloud:Tke/authAttachment:AuthAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAuthAttachment gets an existing AuthAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAuthAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AuthAttachmentState, opts ...pulumi.ResourceOption) (*AuthAttachment, error) {
	var resource AuthAttachment
	err := ctx.ReadResource("tencentcloud:Tke/authAttachment:AuthAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AuthAttachment resources.
type authAttachmentState struct {
	// If set to `true`, the rbac rule will be created automatically which allow anonymous user to access
	// '/.well-known/openid-configuration' and '/openid/v1/jwks'.
	AutoCreateDiscoveryAnonymousAuth *bool `pulumi:"autoCreateDiscoveryAnonymousAuth"`
	// ID of clusters.
	ClusterId *string `pulumi:"clusterId"`
	// Specify service-account-issuer.
	Issuer *string `pulumi:"issuer"`
	// Specify service-account-jwks-uri.
	JwksUri *string `pulumi:"jwksUri"`
}

type AuthAttachmentState struct {
	// If set to `true`, the rbac rule will be created automatically which allow anonymous user to access
	// '/.well-known/openid-configuration' and '/openid/v1/jwks'.
	AutoCreateDiscoveryAnonymousAuth pulumi.BoolPtrInput
	// ID of clusters.
	ClusterId pulumi.StringPtrInput
	// Specify service-account-issuer.
	Issuer pulumi.StringPtrInput
	// Specify service-account-jwks-uri.
	JwksUri pulumi.StringPtrInput
}

func (AuthAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*authAttachmentState)(nil)).Elem()
}

type authAttachmentArgs struct {
	// If set to `true`, the rbac rule will be created automatically which allow anonymous user to access
	// '/.well-known/openid-configuration' and '/openid/v1/jwks'.
	AutoCreateDiscoveryAnonymousAuth *bool `pulumi:"autoCreateDiscoveryAnonymousAuth"`
	// ID of clusters.
	ClusterId string `pulumi:"clusterId"`
	// Specify service-account-issuer.
	Issuer string `pulumi:"issuer"`
	// Specify service-account-jwks-uri.
	JwksUri *string `pulumi:"jwksUri"`
}

// The set of arguments for constructing a AuthAttachment resource.
type AuthAttachmentArgs struct {
	// If set to `true`, the rbac rule will be created automatically which allow anonymous user to access
	// '/.well-known/openid-configuration' and '/openid/v1/jwks'.
	AutoCreateDiscoveryAnonymousAuth pulumi.BoolPtrInput
	// ID of clusters.
	ClusterId pulumi.StringInput
	// Specify service-account-issuer.
	Issuer pulumi.StringInput
	// Specify service-account-jwks-uri.
	JwksUri pulumi.StringPtrInput
}

func (AuthAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*authAttachmentArgs)(nil)).Elem()
}

type AuthAttachmentInput interface {
	pulumi.Input

	ToAuthAttachmentOutput() AuthAttachmentOutput
	ToAuthAttachmentOutputWithContext(ctx context.Context) AuthAttachmentOutput
}

func (*AuthAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**AuthAttachment)(nil)).Elem()
}

func (i *AuthAttachment) ToAuthAttachmentOutput() AuthAttachmentOutput {
	return i.ToAuthAttachmentOutputWithContext(context.Background())
}

func (i *AuthAttachment) ToAuthAttachmentOutputWithContext(ctx context.Context) AuthAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuthAttachmentOutput)
}

// AuthAttachmentArrayInput is an input type that accepts AuthAttachmentArray and AuthAttachmentArrayOutput values.
// You can construct a concrete instance of `AuthAttachmentArrayInput` via:
//
//          AuthAttachmentArray{ AuthAttachmentArgs{...} }
type AuthAttachmentArrayInput interface {
	pulumi.Input

	ToAuthAttachmentArrayOutput() AuthAttachmentArrayOutput
	ToAuthAttachmentArrayOutputWithContext(context.Context) AuthAttachmentArrayOutput
}

type AuthAttachmentArray []AuthAttachmentInput

func (AuthAttachmentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AuthAttachment)(nil)).Elem()
}

func (i AuthAttachmentArray) ToAuthAttachmentArrayOutput() AuthAttachmentArrayOutput {
	return i.ToAuthAttachmentArrayOutputWithContext(context.Background())
}

func (i AuthAttachmentArray) ToAuthAttachmentArrayOutputWithContext(ctx context.Context) AuthAttachmentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuthAttachmentArrayOutput)
}

// AuthAttachmentMapInput is an input type that accepts AuthAttachmentMap and AuthAttachmentMapOutput values.
// You can construct a concrete instance of `AuthAttachmentMapInput` via:
//
//          AuthAttachmentMap{ "key": AuthAttachmentArgs{...} }
type AuthAttachmentMapInput interface {
	pulumi.Input

	ToAuthAttachmentMapOutput() AuthAttachmentMapOutput
	ToAuthAttachmentMapOutputWithContext(context.Context) AuthAttachmentMapOutput
}

type AuthAttachmentMap map[string]AuthAttachmentInput

func (AuthAttachmentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AuthAttachment)(nil)).Elem()
}

func (i AuthAttachmentMap) ToAuthAttachmentMapOutput() AuthAttachmentMapOutput {
	return i.ToAuthAttachmentMapOutputWithContext(context.Background())
}

func (i AuthAttachmentMap) ToAuthAttachmentMapOutputWithContext(ctx context.Context) AuthAttachmentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuthAttachmentMapOutput)
}

type AuthAttachmentOutput struct{ *pulumi.OutputState }

func (AuthAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AuthAttachment)(nil)).Elem()
}

func (o AuthAttachmentOutput) ToAuthAttachmentOutput() AuthAttachmentOutput {
	return o
}

func (o AuthAttachmentOutput) ToAuthAttachmentOutputWithContext(ctx context.Context) AuthAttachmentOutput {
	return o
}

// If set to `true`, the rbac rule will be created automatically which allow anonymous user to access
// '/.well-known/openid-configuration' and '/openid/v1/jwks'.
func (o AuthAttachmentOutput) AutoCreateDiscoveryAnonymousAuth() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *AuthAttachment) pulumi.BoolPtrOutput { return v.AutoCreateDiscoveryAnonymousAuth }).(pulumi.BoolPtrOutput)
}

// ID of clusters.
func (o AuthAttachmentOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *AuthAttachment) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// Specify service-account-issuer.
func (o AuthAttachmentOutput) Issuer() pulumi.StringOutput {
	return o.ApplyT(func(v *AuthAttachment) pulumi.StringOutput { return v.Issuer }).(pulumi.StringOutput)
}

// Specify service-account-jwks-uri.
func (o AuthAttachmentOutput) JwksUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AuthAttachment) pulumi.StringPtrOutput { return v.JwksUri }).(pulumi.StringPtrOutput)
}

type AuthAttachmentArrayOutput struct{ *pulumi.OutputState }

func (AuthAttachmentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AuthAttachment)(nil)).Elem()
}

func (o AuthAttachmentArrayOutput) ToAuthAttachmentArrayOutput() AuthAttachmentArrayOutput {
	return o
}

func (o AuthAttachmentArrayOutput) ToAuthAttachmentArrayOutputWithContext(ctx context.Context) AuthAttachmentArrayOutput {
	return o
}

func (o AuthAttachmentArrayOutput) Index(i pulumi.IntInput) AuthAttachmentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AuthAttachment {
		return vs[0].([]*AuthAttachment)[vs[1].(int)]
	}).(AuthAttachmentOutput)
}

type AuthAttachmentMapOutput struct{ *pulumi.OutputState }

func (AuthAttachmentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AuthAttachment)(nil)).Elem()
}

func (o AuthAttachmentMapOutput) ToAuthAttachmentMapOutput() AuthAttachmentMapOutput {
	return o
}

func (o AuthAttachmentMapOutput) ToAuthAttachmentMapOutputWithContext(ctx context.Context) AuthAttachmentMapOutput {
	return o
}

func (o AuthAttachmentMapOutput) MapIndex(k pulumi.StringInput) AuthAttachmentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AuthAttachment {
		return vs[0].(map[string]*AuthAttachment)[vs[1].(string)]
	}).(AuthAttachmentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AuthAttachmentInput)(nil)).Elem(), &AuthAttachment{})
	pulumi.RegisterInputType(reflect.TypeOf((*AuthAttachmentArrayInput)(nil)).Elem(), AuthAttachmentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AuthAttachmentMapInput)(nil)).Elem(), AuthAttachmentMap{})
	pulumi.RegisterOutputType(AuthAttachmentOutput{})
	pulumi.RegisterOutputType(AuthAttachmentArrayOutput{})
	pulumi.RegisterOutputType(AuthAttachmentMapOutput{})
}
