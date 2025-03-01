// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a resource to create a VPN customer gateway.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const foo = new tencentcloud.Vpn.CustomerGateway("foo", {
 *     publicIpAddress: "1.1.1.1",
 *     tags: {
 *         tag: "test",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * VPN customer gateway can be imported using the id, e.g.
 *
 * ```sh
 *  $ pulumi import tencentcloud:Vpn/customerGateway:CustomerGateway foo cgw-xfqag
 * ```
 */
export class CustomerGateway extends pulumi.CustomResource {
    /**
     * Get an existing CustomerGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomerGatewayState, opts?: pulumi.CustomResourceOptions): CustomerGateway {
        return new CustomerGateway(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Vpn/customerGateway:CustomerGateway';

    /**
     * Returns true if the given object is an instance of CustomerGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomerGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomerGateway.__pulumiType;
    }

    /**
     * Create time of the customer gateway.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * Name of the customer gateway. The length of character is limited to 1-60.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Public IP of the customer gateway.
     */
    public readonly publicIpAddress!: pulumi.Output<string>;
    /**
     * A list of tags used to associate different resources.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a CustomerGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomerGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CustomerGatewayArgs | CustomerGatewayState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CustomerGatewayState | undefined;
            resourceInputs["createTime"] = state ? state.createTime : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["publicIpAddress"] = state ? state.publicIpAddress : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as CustomerGatewayArgs | undefined;
            if ((!args || args.publicIpAddress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'publicIpAddress'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["publicIpAddress"] = args ? args.publicIpAddress : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CustomerGateway.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CustomerGateway resources.
 */
export interface CustomerGatewayState {
    /**
     * Create time of the customer gateway.
     */
    createTime?: pulumi.Input<string>;
    /**
     * Name of the customer gateway. The length of character is limited to 1-60.
     */
    name?: pulumi.Input<string>;
    /**
     * Public IP of the customer gateway.
     */
    publicIpAddress?: pulumi.Input<string>;
    /**
     * A list of tags used to associate different resources.
     */
    tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a CustomerGateway resource.
 */
export interface CustomerGatewayArgs {
    /**
     * Name of the customer gateway. The length of character is limited to 1-60.
     */
    name?: pulumi.Input<string>;
    /**
     * Public IP of the customer gateway.
     */
    publicIpAddress: pulumi.Input<string>;
    /**
     * A list of tags used to associate different resources.
     */
    tags?: pulumi.Input<{[key: string]: any}>;
}
