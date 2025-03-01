// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type GetSecretVersionsSecretVersionList struct {
	// The base64-encoded binary secret.
	SecretBinary string `pulumi:"secretBinary"`
	// The string text of secret.
	SecretString string `pulumi:"secretString"`
	// VersionId used to filter result.
	VersionId string `pulumi:"versionId"`
}

// GetSecretVersionsSecretVersionListInput is an input type that accepts GetSecretVersionsSecretVersionListArgs and GetSecretVersionsSecretVersionListOutput values.
// You can construct a concrete instance of `GetSecretVersionsSecretVersionListInput` via:
//
//          GetSecretVersionsSecretVersionListArgs{...}
type GetSecretVersionsSecretVersionListInput interface {
	pulumi.Input

	ToGetSecretVersionsSecretVersionListOutput() GetSecretVersionsSecretVersionListOutput
	ToGetSecretVersionsSecretVersionListOutputWithContext(context.Context) GetSecretVersionsSecretVersionListOutput
}

type GetSecretVersionsSecretVersionListArgs struct {
	// The base64-encoded binary secret.
	SecretBinary pulumi.StringInput `pulumi:"secretBinary"`
	// The string text of secret.
	SecretString pulumi.StringInput `pulumi:"secretString"`
	// VersionId used to filter result.
	VersionId pulumi.StringInput `pulumi:"versionId"`
}

func (GetSecretVersionsSecretVersionListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSecretVersionsSecretVersionList)(nil)).Elem()
}

func (i GetSecretVersionsSecretVersionListArgs) ToGetSecretVersionsSecretVersionListOutput() GetSecretVersionsSecretVersionListOutput {
	return i.ToGetSecretVersionsSecretVersionListOutputWithContext(context.Background())
}

func (i GetSecretVersionsSecretVersionListArgs) ToGetSecretVersionsSecretVersionListOutputWithContext(ctx context.Context) GetSecretVersionsSecretVersionListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetSecretVersionsSecretVersionListOutput)
}

// GetSecretVersionsSecretVersionListArrayInput is an input type that accepts GetSecretVersionsSecretVersionListArray and GetSecretVersionsSecretVersionListArrayOutput values.
// You can construct a concrete instance of `GetSecretVersionsSecretVersionListArrayInput` via:
//
//          GetSecretVersionsSecretVersionListArray{ GetSecretVersionsSecretVersionListArgs{...} }
type GetSecretVersionsSecretVersionListArrayInput interface {
	pulumi.Input

	ToGetSecretVersionsSecretVersionListArrayOutput() GetSecretVersionsSecretVersionListArrayOutput
	ToGetSecretVersionsSecretVersionListArrayOutputWithContext(context.Context) GetSecretVersionsSecretVersionListArrayOutput
}

type GetSecretVersionsSecretVersionListArray []GetSecretVersionsSecretVersionListInput

func (GetSecretVersionsSecretVersionListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetSecretVersionsSecretVersionList)(nil)).Elem()
}

func (i GetSecretVersionsSecretVersionListArray) ToGetSecretVersionsSecretVersionListArrayOutput() GetSecretVersionsSecretVersionListArrayOutput {
	return i.ToGetSecretVersionsSecretVersionListArrayOutputWithContext(context.Background())
}

func (i GetSecretVersionsSecretVersionListArray) ToGetSecretVersionsSecretVersionListArrayOutputWithContext(ctx context.Context) GetSecretVersionsSecretVersionListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetSecretVersionsSecretVersionListArrayOutput)
}

type GetSecretVersionsSecretVersionListOutput struct{ *pulumi.OutputState }

func (GetSecretVersionsSecretVersionListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSecretVersionsSecretVersionList)(nil)).Elem()
}

func (o GetSecretVersionsSecretVersionListOutput) ToGetSecretVersionsSecretVersionListOutput() GetSecretVersionsSecretVersionListOutput {
	return o
}

func (o GetSecretVersionsSecretVersionListOutput) ToGetSecretVersionsSecretVersionListOutputWithContext(ctx context.Context) GetSecretVersionsSecretVersionListOutput {
	return o
}

// The base64-encoded binary secret.
func (o GetSecretVersionsSecretVersionListOutput) SecretBinary() pulumi.StringOutput {
	return o.ApplyT(func(v GetSecretVersionsSecretVersionList) string { return v.SecretBinary }).(pulumi.StringOutput)
}

// The string text of secret.
func (o GetSecretVersionsSecretVersionListOutput) SecretString() pulumi.StringOutput {
	return o.ApplyT(func(v GetSecretVersionsSecretVersionList) string { return v.SecretString }).(pulumi.StringOutput)
}

// VersionId used to filter result.
func (o GetSecretVersionsSecretVersionListOutput) VersionId() pulumi.StringOutput {
	return o.ApplyT(func(v GetSecretVersionsSecretVersionList) string { return v.VersionId }).(pulumi.StringOutput)
}

type GetSecretVersionsSecretVersionListArrayOutput struct{ *pulumi.OutputState }

func (GetSecretVersionsSecretVersionListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetSecretVersionsSecretVersionList)(nil)).Elem()
}

func (o GetSecretVersionsSecretVersionListArrayOutput) ToGetSecretVersionsSecretVersionListArrayOutput() GetSecretVersionsSecretVersionListArrayOutput {
	return o
}

func (o GetSecretVersionsSecretVersionListArrayOutput) ToGetSecretVersionsSecretVersionListArrayOutputWithContext(ctx context.Context) GetSecretVersionsSecretVersionListArrayOutput {
	return o
}

func (o GetSecretVersionsSecretVersionListArrayOutput) Index(i pulumi.IntInput) GetSecretVersionsSecretVersionListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetSecretVersionsSecretVersionList {
		return vs[0].([]GetSecretVersionsSecretVersionList)[vs[1].(int)]
	}).(GetSecretVersionsSecretVersionListOutput)
}

type GetSecretsSecretList struct {
	// Create time of secret.
	CreateTime int `pulumi:"createTime"`
	// Uin of Creator.
	CreateUin int `pulumi:"createUin"`
	// Delete time of CMK.
	DeleteTime int `pulumi:"deleteTime"`
	// Description of secret.
	Description string `pulumi:"description"`
	// KMS keyId used to encrypt secret.
	KmsKeyId string `pulumi:"kmsKeyId"`
	// Secret name used to filter result.
	SecretName string `pulumi:"secretName"`
	// Status of secret.
	Status string `pulumi:"status"`
}

// GetSecretsSecretListInput is an input type that accepts GetSecretsSecretListArgs and GetSecretsSecretListOutput values.
// You can construct a concrete instance of `GetSecretsSecretListInput` via:
//
//          GetSecretsSecretListArgs{...}
type GetSecretsSecretListInput interface {
	pulumi.Input

	ToGetSecretsSecretListOutput() GetSecretsSecretListOutput
	ToGetSecretsSecretListOutputWithContext(context.Context) GetSecretsSecretListOutput
}

type GetSecretsSecretListArgs struct {
	// Create time of secret.
	CreateTime pulumi.IntInput `pulumi:"createTime"`
	// Uin of Creator.
	CreateUin pulumi.IntInput `pulumi:"createUin"`
	// Delete time of CMK.
	DeleteTime pulumi.IntInput `pulumi:"deleteTime"`
	// Description of secret.
	Description pulumi.StringInput `pulumi:"description"`
	// KMS keyId used to encrypt secret.
	KmsKeyId pulumi.StringInput `pulumi:"kmsKeyId"`
	// Secret name used to filter result.
	SecretName pulumi.StringInput `pulumi:"secretName"`
	// Status of secret.
	Status pulumi.StringInput `pulumi:"status"`
}

func (GetSecretsSecretListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSecretsSecretList)(nil)).Elem()
}

func (i GetSecretsSecretListArgs) ToGetSecretsSecretListOutput() GetSecretsSecretListOutput {
	return i.ToGetSecretsSecretListOutputWithContext(context.Background())
}

func (i GetSecretsSecretListArgs) ToGetSecretsSecretListOutputWithContext(ctx context.Context) GetSecretsSecretListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetSecretsSecretListOutput)
}

// GetSecretsSecretListArrayInput is an input type that accepts GetSecretsSecretListArray and GetSecretsSecretListArrayOutput values.
// You can construct a concrete instance of `GetSecretsSecretListArrayInput` via:
//
//          GetSecretsSecretListArray{ GetSecretsSecretListArgs{...} }
type GetSecretsSecretListArrayInput interface {
	pulumi.Input

	ToGetSecretsSecretListArrayOutput() GetSecretsSecretListArrayOutput
	ToGetSecretsSecretListArrayOutputWithContext(context.Context) GetSecretsSecretListArrayOutput
}

type GetSecretsSecretListArray []GetSecretsSecretListInput

func (GetSecretsSecretListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetSecretsSecretList)(nil)).Elem()
}

func (i GetSecretsSecretListArray) ToGetSecretsSecretListArrayOutput() GetSecretsSecretListArrayOutput {
	return i.ToGetSecretsSecretListArrayOutputWithContext(context.Background())
}

func (i GetSecretsSecretListArray) ToGetSecretsSecretListArrayOutputWithContext(ctx context.Context) GetSecretsSecretListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetSecretsSecretListArrayOutput)
}

type GetSecretsSecretListOutput struct{ *pulumi.OutputState }

func (GetSecretsSecretListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSecretsSecretList)(nil)).Elem()
}

func (o GetSecretsSecretListOutput) ToGetSecretsSecretListOutput() GetSecretsSecretListOutput {
	return o
}

func (o GetSecretsSecretListOutput) ToGetSecretsSecretListOutputWithContext(ctx context.Context) GetSecretsSecretListOutput {
	return o
}

// Create time of secret.
func (o GetSecretsSecretListOutput) CreateTime() pulumi.IntOutput {
	return o.ApplyT(func(v GetSecretsSecretList) int { return v.CreateTime }).(pulumi.IntOutput)
}

// Uin of Creator.
func (o GetSecretsSecretListOutput) CreateUin() pulumi.IntOutput {
	return o.ApplyT(func(v GetSecretsSecretList) int { return v.CreateUin }).(pulumi.IntOutput)
}

// Delete time of CMK.
func (o GetSecretsSecretListOutput) DeleteTime() pulumi.IntOutput {
	return o.ApplyT(func(v GetSecretsSecretList) int { return v.DeleteTime }).(pulumi.IntOutput)
}

// Description of secret.
func (o GetSecretsSecretListOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetSecretsSecretList) string { return v.Description }).(pulumi.StringOutput)
}

// KMS keyId used to encrypt secret.
func (o GetSecretsSecretListOutput) KmsKeyId() pulumi.StringOutput {
	return o.ApplyT(func(v GetSecretsSecretList) string { return v.KmsKeyId }).(pulumi.StringOutput)
}

// Secret name used to filter result.
func (o GetSecretsSecretListOutput) SecretName() pulumi.StringOutput {
	return o.ApplyT(func(v GetSecretsSecretList) string { return v.SecretName }).(pulumi.StringOutput)
}

// Status of secret.
func (o GetSecretsSecretListOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v GetSecretsSecretList) string { return v.Status }).(pulumi.StringOutput)
}

type GetSecretsSecretListArrayOutput struct{ *pulumi.OutputState }

func (GetSecretsSecretListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetSecretsSecretList)(nil)).Elem()
}

func (o GetSecretsSecretListArrayOutput) ToGetSecretsSecretListArrayOutput() GetSecretsSecretListArrayOutput {
	return o
}

func (o GetSecretsSecretListArrayOutput) ToGetSecretsSecretListArrayOutputWithContext(ctx context.Context) GetSecretsSecretListArrayOutput {
	return o
}

func (o GetSecretsSecretListArrayOutput) Index(i pulumi.IntInput) GetSecretsSecretListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetSecretsSecretList {
		return vs[0].([]GetSecretsSecretList)[vs[1].(int)]
	}).(GetSecretsSecretListOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GetSecretVersionsSecretVersionListInput)(nil)).Elem(), GetSecretVersionsSecretVersionListArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetSecretVersionsSecretVersionListArrayInput)(nil)).Elem(), GetSecretVersionsSecretVersionListArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetSecretsSecretListInput)(nil)).Elem(), GetSecretsSecretListArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetSecretsSecretListArrayInput)(nil)).Elem(), GetSecretsSecretListArray{})
	pulumi.RegisterOutputType(GetSecretVersionsSecretVersionListOutput{})
	pulumi.RegisterOutputType(GetSecretVersionsSecretVersionListArrayOutput{})
	pulumi.RegisterOutputType(GetSecretsSecretListOutput{})
	pulumi.RegisterOutputType(GetSecretsSecretListArrayOutput{})
}
