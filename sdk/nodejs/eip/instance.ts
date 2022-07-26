// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class Instance extends pulumi.CustomResource {
    /**
     * Get an existing Instance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState, opts?: pulumi.CustomResourceOptions): Instance {
        return new Instance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Eip/instance:Instance';

    /**
     * Returns true if the given object is an instance of Instance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Instance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Instance.__pulumiType;
    }

    /**
     * The zone of anycast. Valid value: `ANYCAST_ZONE_GLOBAL` and `ANYCAST_ZONE_OVERSEAS`.
     */
    public readonly anycastZone!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether the anycast eip can be associated to a CLB.
     *
     * @deprecated It has been deprecated from version 1.27.0.
     */
    public readonly applicableForClb!: pulumi.Output<boolean | undefined>;
    /**
     * The charge type of eip. Valid value: `BANDWIDTH_PACKAGE`, `BANDWIDTH_POSTPAID_BY_HOUR` and `TRAFFIC_POSTPAID_BY_HOUR`.
     */
    public readonly internetChargeType!: pulumi.Output<string | undefined>;
    /**
     * The bandwidth limit of EIP, unit is Mbps.
     */
    public readonly internetMaxBandwidthOut!: pulumi.Output<number | undefined>;
    /**
     * Internet service provider of eip. Valid value: `BGP`, `CMCC`, `CTCC` and `CUCC`.
     */
    public readonly internetServiceProvider!: pulumi.Output<string | undefined>;
    /**
     * The name of eip.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The elastic IP address.
     */
    public /*out*/ readonly publicIp!: pulumi.Output<string>;
    /**
     * The EIP current status.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * The tags of eip.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The type of eip. Valid value: `EIP` and `AnycastEIP` and `HighQualityEIP`. Default is `EIP`.
     */
    public readonly type!: pulumi.Output<string | undefined>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: InstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceArgs | InstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as InstanceState | undefined;
            resourceInputs["anycastZone"] = state ? state.anycastZone : undefined;
            resourceInputs["applicableForClb"] = state ? state.applicableForClb : undefined;
            resourceInputs["internetChargeType"] = state ? state.internetChargeType : undefined;
            resourceInputs["internetMaxBandwidthOut"] = state ? state.internetMaxBandwidthOut : undefined;
            resourceInputs["internetServiceProvider"] = state ? state.internetServiceProvider : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["publicIp"] = state ? state.publicIp : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as InstanceArgs | undefined;
            resourceInputs["anycastZone"] = args ? args.anycastZone : undefined;
            resourceInputs["applicableForClb"] = args ? args.applicableForClb : undefined;
            resourceInputs["internetChargeType"] = args ? args.internetChargeType : undefined;
            resourceInputs["internetMaxBandwidthOut"] = args ? args.internetMaxBandwidthOut : undefined;
            resourceInputs["internetServiceProvider"] = args ? args.internetServiceProvider : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["publicIp"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Instance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Instance resources.
 */
export interface InstanceState {
    /**
     * The zone of anycast. Valid value: `ANYCAST_ZONE_GLOBAL` and `ANYCAST_ZONE_OVERSEAS`.
     */
    anycastZone?: pulumi.Input<string>;
    /**
     * Indicates whether the anycast eip can be associated to a CLB.
     *
     * @deprecated It has been deprecated from version 1.27.0.
     */
    applicableForClb?: pulumi.Input<boolean>;
    /**
     * The charge type of eip. Valid value: `BANDWIDTH_PACKAGE`, `BANDWIDTH_POSTPAID_BY_HOUR` and `TRAFFIC_POSTPAID_BY_HOUR`.
     */
    internetChargeType?: pulumi.Input<string>;
    /**
     * The bandwidth limit of EIP, unit is Mbps.
     */
    internetMaxBandwidthOut?: pulumi.Input<number>;
    /**
     * Internet service provider of eip. Valid value: `BGP`, `CMCC`, `CTCC` and `CUCC`.
     */
    internetServiceProvider?: pulumi.Input<string>;
    /**
     * The name of eip.
     */
    name?: pulumi.Input<string>;
    /**
     * The elastic IP address.
     */
    publicIp?: pulumi.Input<string>;
    /**
     * The EIP current status.
     */
    status?: pulumi.Input<string>;
    /**
     * The tags of eip.
     */
    tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The type of eip. Valid value: `EIP` and `AnycastEIP` and `HighQualityEIP`. Default is `EIP`.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * The zone of anycast. Valid value: `ANYCAST_ZONE_GLOBAL` and `ANYCAST_ZONE_OVERSEAS`.
     */
    anycastZone?: pulumi.Input<string>;
    /**
     * Indicates whether the anycast eip can be associated to a CLB.
     *
     * @deprecated It has been deprecated from version 1.27.0.
     */
    applicableForClb?: pulumi.Input<boolean>;
    /**
     * The charge type of eip. Valid value: `BANDWIDTH_PACKAGE`, `BANDWIDTH_POSTPAID_BY_HOUR` and `TRAFFIC_POSTPAID_BY_HOUR`.
     */
    internetChargeType?: pulumi.Input<string>;
    /**
     * The bandwidth limit of EIP, unit is Mbps.
     */
    internetMaxBandwidthOut?: pulumi.Input<number>;
    /**
     * Internet service provider of eip. Valid value: `BGP`, `CMCC`, `CTCC` and `CUCC`.
     */
    internetServiceProvider?: pulumi.Input<string>;
    /**
     * The name of eip.
     */
    name?: pulumi.Input<string>;
    /**
     * The tags of eip.
     */
    tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The type of eip. Valid value: `EIP` and `AnycastEIP` and `HighQualityEIP`. Default is `EIP`.
     */
    type?: pulumi.Input<string>;
}
