// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class GatewayCcnRouteInstance extends pulumi.CustomResource {
    /**
     * Get an existing GatewayCcnRouteInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayCcnRouteInstanceState, opts?: pulumi.CustomResourceOptions): GatewayCcnRouteInstance {
        return new GatewayCcnRouteInstance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Dc/gatewayCcnRouteInstance:GatewayCcnRouteInstance';

    /**
     * Returns true if the given object is an instance of GatewayCcnRouteInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GatewayCcnRouteInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GatewayCcnRouteInstance.__pulumiType;
    }

    /**
     * As path list of the BGP.
     */
    public /*out*/ readonly asPaths!: pulumi.Output<string[]>;
    /**
     * A network address segment of IDC.
     */
    public readonly cidrBlock!: pulumi.Output<string>;
    /**
     * ID of the DCG.
     */
    public readonly dcgId!: pulumi.Output<string>;

    /**
     * Create a GatewayCcnRouteInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GatewayCcnRouteInstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GatewayCcnRouteInstanceArgs | GatewayCcnRouteInstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GatewayCcnRouteInstanceState | undefined;
            resourceInputs["asPaths"] = state ? state.asPaths : undefined;
            resourceInputs["cidrBlock"] = state ? state.cidrBlock : undefined;
            resourceInputs["dcgId"] = state ? state.dcgId : undefined;
        } else {
            const args = argsOrState as GatewayCcnRouteInstanceArgs | undefined;
            if ((!args || args.cidrBlock === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cidrBlock'");
            }
            if ((!args || args.dcgId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dcgId'");
            }
            resourceInputs["cidrBlock"] = args ? args.cidrBlock : undefined;
            resourceInputs["dcgId"] = args ? args.dcgId : undefined;
            resourceInputs["asPaths"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GatewayCcnRouteInstance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GatewayCcnRouteInstance resources.
 */
export interface GatewayCcnRouteInstanceState {
    /**
     * As path list of the BGP.
     */
    asPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A network address segment of IDC.
     */
    cidrBlock?: pulumi.Input<string>;
    /**
     * ID of the DCG.
     */
    dcgId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GatewayCcnRouteInstance resource.
 */
export interface GatewayCcnRouteInstanceArgs {
    /**
     * A network address segment of IDC.
     */
    cidrBlock: pulumi.Input<string>;
    /**
     * ID of the DCG.
     */
    dcgId: pulumi.Input<string>;
}
