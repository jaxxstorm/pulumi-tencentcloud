// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kubernetes

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "tencentcloud:Kubernetes/addonAttachment:AddonAttachment":
		r = &AddonAttachment{}
	case "tencentcloud:Kubernetes/asScalingGroup:AsScalingGroup":
		r = &AsScalingGroup{}
	case "tencentcloud:Kubernetes/authAttachment:AuthAttachment":
		r = &AuthAttachment{}
	case "tencentcloud:Kubernetes/cluster:Cluster":
		r = &Cluster{}
	case "tencentcloud:Kubernetes/clusterAttachment:ClusterAttachment":
		r = &ClusterAttachment{}
	case "tencentcloud:Kubernetes/clusterEndpoint:ClusterEndpoint":
		r = &ClusterEndpoint{}
	case "tencentcloud:Kubernetes/nodePool:NodePool":
		r = &NodePool{}
	case "tencentcloud:Kubernetes/scaleWorker:ScaleWorker":
		r = &ScaleWorker{}
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
		"Kubernetes/addonAttachment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Kubernetes/asScalingGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Kubernetes/authAttachment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Kubernetes/cluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Kubernetes/clusterAttachment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Kubernetes/clusterEndpoint",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Kubernetes/nodePool",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Kubernetes/scaleWorker",
		&module{version},
	)
}
