// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to create postgresql readonly attachment.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const attach = new tencentcloud.postgresql.ReadonlyAttachment("attach", {
 *     dbInstanceId: tencentcloud_postgresql_readonly_instance.foo.id,
 *     readOnlyGroupId: tencentcloud_postgresql_readonly_group.group.id,
 * });
 * ```
 */
export class ReadonlyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing ReadonlyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ReadonlyAttachmentState, opts?: pulumi.CustomResourceOptions): ReadonlyAttachment {
        return new ReadonlyAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Postgresql/readonlyAttachment:ReadonlyAttachment';

    /**
     * Returns true if the given object is an instance of ReadonlyAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ReadonlyAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ReadonlyAttachment.__pulumiType;
    }

    /**
     * Read only instance ID.
     */
    public readonly dbInstanceId!: pulumi.Output<string>;
    /**
     * Read only group ID.
     */
    public readonly readOnlyGroupId!: pulumi.Output<string>;

    /**
     * Create a ReadonlyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ReadonlyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ReadonlyAttachmentArgs | ReadonlyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ReadonlyAttachmentState | undefined;
            resourceInputs["dbInstanceId"] = state ? state.dbInstanceId : undefined;
            resourceInputs["readOnlyGroupId"] = state ? state.readOnlyGroupId : undefined;
        } else {
            const args = argsOrState as ReadonlyAttachmentArgs | undefined;
            if ((!args || args.dbInstanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbInstanceId'");
            }
            if ((!args || args.readOnlyGroupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'readOnlyGroupId'");
            }
            resourceInputs["dbInstanceId"] = args ? args.dbInstanceId : undefined;
            resourceInputs["readOnlyGroupId"] = args ? args.readOnlyGroupId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ReadonlyAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ReadonlyAttachment resources.
 */
export interface ReadonlyAttachmentState {
    /**
     * Read only instance ID.
     */
    dbInstanceId?: pulumi.Input<string>;
    /**
     * Read only group ID.
     */
    readOnlyGroupId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ReadonlyAttachment resource.
 */
export interface ReadonlyAttachmentArgs {
    /**
     * Read only instance ID.
     */
    dbInstanceId: pulumi.Input<string>;
    /**
     * Read only group ID.
     */
    readOnlyGroupId: pulumi.Input<string>;
}
