// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to API gateway attach access key to usage plan.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const key = new tencentcloud.apigateway.ApiKey("key", {
 *     secretName: "my_api_key",
 *     status: "on",
 * });
 * const plan = new tencentcloud.apigateway.UsagePlan("plan", {
 *     usagePlanName: "my_plan",
 *     usagePlanDesc: "nice plan",
 *     maxRequestNum: 100,
 *     maxRequestNumPreSec: 10,
 * });
 * const attach = new tencentcloud.apigateway.ApiKeyAttachment("attach", {
 *     apiKeyId: key.id,
 *     usagePlanId: plan.id,
 * });
 * ```
 *
 * ## Import
 *
 * API gateway attach access key can be imported using the id, e.g.
 *
 * ```sh
 *  $ pulumi import tencentcloud:ApiGateway/apiKeyAttachment:ApiKeyAttachment attach AKID110b8Rmuw7t0fP1N8bi809n327023Is7xN8f#usagePlan-gyeafpab
 * ```
 */
export class ApiKeyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing ApiKeyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApiKeyAttachmentState, opts?: pulumi.CustomResourceOptions): ApiKeyAttachment {
        return new ApiKeyAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:ApiGateway/apiKeyAttachment:ApiKeyAttachment';

    /**
     * Returns true if the given object is an instance of ApiKeyAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApiKeyAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApiKeyAttachment.__pulumiType;
    }

    /**
     * ID of API key.
     */
    public readonly apiKeyId!: pulumi.Output<string>;
    /**
     * ID of the usage plan.
     */
    public readonly usagePlanId!: pulumi.Output<string>;

    /**
     * Create a ApiKeyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApiKeyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApiKeyAttachmentArgs | ApiKeyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ApiKeyAttachmentState | undefined;
            resourceInputs["apiKeyId"] = state ? state.apiKeyId : undefined;
            resourceInputs["usagePlanId"] = state ? state.usagePlanId : undefined;
        } else {
            const args = argsOrState as ApiKeyAttachmentArgs | undefined;
            if ((!args || args.apiKeyId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiKeyId'");
            }
            if ((!args || args.usagePlanId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'usagePlanId'");
            }
            resourceInputs["apiKeyId"] = args ? args.apiKeyId : undefined;
            resourceInputs["usagePlanId"] = args ? args.usagePlanId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ApiKeyAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApiKeyAttachment resources.
 */
export interface ApiKeyAttachmentState {
    /**
     * ID of API key.
     */
    apiKeyId?: pulumi.Input<string>;
    /**
     * ID of the usage plan.
     */
    usagePlanId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApiKeyAttachment resource.
 */
export interface ApiKeyAttachmentArgs {
    /**
     * ID of API key.
     */
    apiKeyId: pulumi.Input<string>;
    /**
     * ID of the usage plan.
     */
    usagePlanId: pulumi.Input<string>;
}
