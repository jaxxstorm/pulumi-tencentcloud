// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Provides a resource to create a CLB attachment.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const foo = new tencentcloud.Clb.Attachment("foo", {
 *     clbId: "lb-k2zjp9lv",
 *     listenerId: "lbl-hh141sn9",
 *     ruleId: "loc-4xxr2cy7",
 *     targets: [{
 *         instanceId: "ins-1flbqyp8",
 *         port: 80,
 *         weight: 10,
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * CLB attachment can be imported using the id, e.g.
 *
 * ```sh
 *  $ pulumi import tencentcloud:Clb/attachment:Attachment foo loc-4xxr2cy7#lbl-hh141sn9#lb-7a0t6zqb
 * ```
 */
export class Attachment extends pulumi.CustomResource {
    /**
     * Get an existing Attachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AttachmentState, opts?: pulumi.CustomResourceOptions): Attachment {
        return new Attachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Clb/attachment:Attachment';

    /**
     * Returns true if the given object is an instance of Attachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Attachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Attachment.__pulumiType;
    }

    /**
     * ID of the CLB.
     */
    public readonly clbId!: pulumi.Output<string>;
    /**
     * ID of the CLB listener.
     */
    public readonly listenerId!: pulumi.Output<string>;
    /**
     * Type of protocol within the listener.
     */
    public /*out*/ readonly protocolType!: pulumi.Output<string>;
    /**
     * ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
     */
    public readonly ruleId!: pulumi.Output<string | undefined>;
    /**
     * Information of the backends to be attached.
     */
    public readonly targets!: pulumi.Output<outputs.Clb.AttachmentTarget[]>;

    /**
     * Create a Attachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AttachmentArgs | AttachmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AttachmentState | undefined;
            resourceInputs["clbId"] = state ? state.clbId : undefined;
            resourceInputs["listenerId"] = state ? state.listenerId : undefined;
            resourceInputs["protocolType"] = state ? state.protocolType : undefined;
            resourceInputs["ruleId"] = state ? state.ruleId : undefined;
            resourceInputs["targets"] = state ? state.targets : undefined;
        } else {
            const args = argsOrState as AttachmentArgs | undefined;
            if ((!args || args.clbId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clbId'");
            }
            if ((!args || args.listenerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'listenerId'");
            }
            if ((!args || args.targets === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targets'");
            }
            resourceInputs["clbId"] = args ? args.clbId : undefined;
            resourceInputs["listenerId"] = args ? args.listenerId : undefined;
            resourceInputs["ruleId"] = args ? args.ruleId : undefined;
            resourceInputs["targets"] = args ? args.targets : undefined;
            resourceInputs["protocolType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Attachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Attachment resources.
 */
export interface AttachmentState {
    /**
     * ID of the CLB.
     */
    clbId?: pulumi.Input<string>;
    /**
     * ID of the CLB listener.
     */
    listenerId?: pulumi.Input<string>;
    /**
     * Type of protocol within the listener.
     */
    protocolType?: pulumi.Input<string>;
    /**
     * ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
     */
    ruleId?: pulumi.Input<string>;
    /**
     * Information of the backends to be attached.
     */
    targets?: pulumi.Input<pulumi.Input<inputs.Clb.AttachmentTarget>[]>;
}

/**
 * The set of arguments for constructing a Attachment resource.
 */
export interface AttachmentArgs {
    /**
     * ID of the CLB.
     */
    clbId: pulumi.Input<string>;
    /**
     * ID of the CLB listener.
     */
    listenerId: pulumi.Input<string>;
    /**
     * ID of the CLB listener rule. Only supports listeners of `HTTPS` and `HTTP` protocol.
     */
    ruleId?: pulumi.Input<string>;
    /**
     * Information of the backends to be attached.
     */
    targets: pulumi.Input<pulumi.Input<inputs.Clb.AttachmentTarget>[]>;
}
