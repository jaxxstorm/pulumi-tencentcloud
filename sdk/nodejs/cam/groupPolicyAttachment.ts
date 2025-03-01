// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a resource to create a CAM group policy attachment.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const foo = new tencentcloud.cam.GroupPolicyAttachment("foo", {
 *     groupId: tencentcloud_cam_group.foo.id,
 *     policyId: tencentcloud_cam_policy.foo.id,
 * });
 * ```
 *
 * ## Import
 *
 * CAM group policy attachment can be imported using the id, e.g.
 *
 * ```sh
 *  $ pulumi import tencentcloud:Cam/groupPolicyAttachment:GroupPolicyAttachment foo 12515263#26800353
 * ```
 */
export class GroupPolicyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing GroupPolicyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupPolicyAttachmentState, opts?: pulumi.CustomResourceOptions): GroupPolicyAttachment {
        return new GroupPolicyAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Cam/groupPolicyAttachment:GroupPolicyAttachment';

    /**
     * Returns true if the given object is an instance of GroupPolicyAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GroupPolicyAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GroupPolicyAttachment.__pulumiType;
    }

    /**
     * Mode of Creation of the CAM group policy attachment. `1` means the cam policy attachment is created by production, and the others indicate syntax strategy ways.
     */
    public /*out*/ readonly createMode!: pulumi.Output<number>;
    /**
     * Create time of the CAM group policy attachment.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * ID of the attached CAM group.
     */
    public readonly groupId!: pulumi.Output<string>;
    /**
     * ID of the policy.
     */
    public readonly policyId!: pulumi.Output<string>;
    /**
     * Name of the policy.
     */
    public /*out*/ readonly policyName!: pulumi.Output<string>;
    /**
     * Type of the policy strategy. 'Group' means customer strategy and 'QCS' means preset strategy.
     */
    public /*out*/ readonly policyType!: pulumi.Output<string>;

    /**
     * Create a GroupPolicyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupPolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupPolicyAttachmentArgs | GroupPolicyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupPolicyAttachmentState | undefined;
            resourceInputs["createMode"] = state ? state.createMode : undefined;
            resourceInputs["createTime"] = state ? state.createTime : undefined;
            resourceInputs["groupId"] = state ? state.groupId : undefined;
            resourceInputs["policyId"] = state ? state.policyId : undefined;
            resourceInputs["policyName"] = state ? state.policyName : undefined;
            resourceInputs["policyType"] = state ? state.policyType : undefined;
        } else {
            const args = argsOrState as GroupPolicyAttachmentArgs | undefined;
            if ((!args || args.groupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupId'");
            }
            if ((!args || args.policyId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policyId'");
            }
            resourceInputs["groupId"] = args ? args.groupId : undefined;
            resourceInputs["policyId"] = args ? args.policyId : undefined;
            resourceInputs["createMode"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["policyName"] = undefined /*out*/;
            resourceInputs["policyType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GroupPolicyAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GroupPolicyAttachment resources.
 */
export interface GroupPolicyAttachmentState {
    /**
     * Mode of Creation of the CAM group policy attachment. `1` means the cam policy attachment is created by production, and the others indicate syntax strategy ways.
     */
    createMode?: pulumi.Input<number>;
    /**
     * Create time of the CAM group policy attachment.
     */
    createTime?: pulumi.Input<string>;
    /**
     * ID of the attached CAM group.
     */
    groupId?: pulumi.Input<string>;
    /**
     * ID of the policy.
     */
    policyId?: pulumi.Input<string>;
    /**
     * Name of the policy.
     */
    policyName?: pulumi.Input<string>;
    /**
     * Type of the policy strategy. 'Group' means customer strategy and 'QCS' means preset strategy.
     */
    policyType?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GroupPolicyAttachment resource.
 */
export interface GroupPolicyAttachmentArgs {
    /**
     * ID of the attached CAM group.
     */
    groupId: pulumi.Input<string>;
    /**
     * ID of the policy.
     */
    policyId: pulumi.Input<string>;
}
