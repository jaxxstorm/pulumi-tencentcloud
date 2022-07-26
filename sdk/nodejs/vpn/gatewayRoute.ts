// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class GatewayRoute extends pulumi.CustomResource {
    /**
     * Get an existing GatewayRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayRouteState, opts?: pulumi.CustomResourceOptions): GatewayRoute {
        return new GatewayRoute(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Vpn/gatewayRoute:GatewayRoute';

    /**
     * Returns true if the given object is an instance of GatewayRoute.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GatewayRoute {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GatewayRoute.__pulumiType;
    }

    /**
     * Create time.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * Destination IDC IP range.
     */
    public readonly destinationCidrBlock!: pulumi.Output<string>;
    /**
     * Instance ID of the next hop.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * Next hop type (type of the associated instance). Valid values: VPNCONN (VPN tunnel) and CCN (CCN instance).
     */
    public readonly instanceType!: pulumi.Output<string>;
    /**
     * Priority. Valid values: 0 and 100.
     */
    public readonly priority!: pulumi.Output<number>;
    /**
     * Route ID.
     */
    public /*out*/ readonly routeId!: pulumi.Output<string>;
    /**
     * Status. Valid values: ENABLE and DISABLE.
     */
    public readonly status!: pulumi.Output<string>;
    /**
     * Route type. Default value: Static.
     */
    public /*out*/ readonly type!: pulumi.Output<string>;
    /**
     * Update time.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;
    /**
     * VPN gateway ID.
     */
    public readonly vpnGatewayId!: pulumi.Output<string>;

    /**
     * Create a GatewayRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GatewayRouteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GatewayRouteArgs | GatewayRouteState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GatewayRouteState | undefined;
            resourceInputs["createTime"] = state ? state.createTime : undefined;
            resourceInputs["destinationCidrBlock"] = state ? state.destinationCidrBlock : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["instanceType"] = state ? state.instanceType : undefined;
            resourceInputs["priority"] = state ? state.priority : undefined;
            resourceInputs["routeId"] = state ? state.routeId : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["updateTime"] = state ? state.updateTime : undefined;
            resourceInputs["vpnGatewayId"] = state ? state.vpnGatewayId : undefined;
        } else {
            const args = argsOrState as GatewayRouteArgs | undefined;
            if ((!args || args.destinationCidrBlock === undefined) && !opts.urn) {
                throw new Error("Missing required property 'destinationCidrBlock'");
            }
            if ((!args || args.instanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceId'");
            }
            if ((!args || args.instanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceType'");
            }
            if ((!args || args.priority === undefined) && !opts.urn) {
                throw new Error("Missing required property 'priority'");
            }
            if ((!args || args.status === undefined) && !opts.urn) {
                throw new Error("Missing required property 'status'");
            }
            if ((!args || args.vpnGatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpnGatewayId'");
            }
            resourceInputs["destinationCidrBlock"] = args ? args.destinationCidrBlock : undefined;
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["instanceType"] = args ? args.instanceType : undefined;
            resourceInputs["priority"] = args ? args.priority : undefined;
            resourceInputs["status"] = args ? args.status : undefined;
            resourceInputs["vpnGatewayId"] = args ? args.vpnGatewayId : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["routeId"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GatewayRoute.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GatewayRoute resources.
 */
export interface GatewayRouteState {
    /**
     * Create time.
     */
    createTime?: pulumi.Input<string>;
    /**
     * Destination IDC IP range.
     */
    destinationCidrBlock?: pulumi.Input<string>;
    /**
     * Instance ID of the next hop.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * Next hop type (type of the associated instance). Valid values: VPNCONN (VPN tunnel) and CCN (CCN instance).
     */
    instanceType?: pulumi.Input<string>;
    /**
     * Priority. Valid values: 0 and 100.
     */
    priority?: pulumi.Input<number>;
    /**
     * Route ID.
     */
    routeId?: pulumi.Input<string>;
    /**
     * Status. Valid values: ENABLE and DISABLE.
     */
    status?: pulumi.Input<string>;
    /**
     * Route type. Default value: Static.
     */
    type?: pulumi.Input<string>;
    /**
     * Update time.
     */
    updateTime?: pulumi.Input<string>;
    /**
     * VPN gateway ID.
     */
    vpnGatewayId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GatewayRoute resource.
 */
export interface GatewayRouteArgs {
    /**
     * Destination IDC IP range.
     */
    destinationCidrBlock: pulumi.Input<string>;
    /**
     * Instance ID of the next hop.
     */
    instanceId: pulumi.Input<string>;
    /**
     * Next hop type (type of the associated instance). Valid values: VPNCONN (VPN tunnel) and CCN (CCN instance).
     */
    instanceType: pulumi.Input<string>;
    /**
     * Priority. Valid values: 0 and 100.
     */
    priority: pulumi.Input<number>;
    /**
     * Status. Valid values: ENABLE and DISABLE.
     */
    status: pulumi.Input<string>;
    /**
     * VPN gateway ID.
     */
    vpnGatewayId: pulumi.Input<string>;
}
