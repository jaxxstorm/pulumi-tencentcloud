// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ha

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "tencentcloud:Ha/haVip:HaVip":
		r = &HaVip{}
	case "tencentcloud:Ha/vipEipAttachment:VipEipAttachment":
		r = &VipEipAttachment{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := tencentcloud.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Ha/haVip",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Ha/vipEipAttachment",
		&module{version},
	)
}
