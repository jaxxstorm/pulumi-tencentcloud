// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function userPolicyAttachments(args?: UserPolicyAttachmentsArgs, opts?: pulumi.InvokeOptions): Promise<UserPolicyAttachmentsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Cam/userPolicyAttachments:UserPolicyAttachments", {
        "createMode": args.createMode,
        "policyId": args.policyId,
        "policyType": args.policyType,
        "resultOutputFile": args.resultOutputFile,
        "userId": args.userId,
        "userName": args.userName,
    }, opts);
}

/**
 * A collection of arguments for invoking UserPolicyAttachments.
 */
export interface UserPolicyAttachmentsArgs {
    createMode?: number;
    policyId?: string;
    policyType?: string;
    resultOutputFile?: string;
    /**
     * @deprecated It has been deprecated from version 1.59.6. Use `user_name` instead.
     */
    userId?: string;
    userName?: string;
}

/**
 * A collection of values returned by UserPolicyAttachments.
 */
export interface UserPolicyAttachmentsResult {
    readonly createMode?: number;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly policyId?: string;
    readonly policyType?: string;
    readonly resultOutputFile?: string;
    /**
     * @deprecated It has been deprecated from version 1.59.6. Use `user_name` instead.
     */
    readonly userId?: string;
    readonly userName?: string;
    readonly userPolicyAttachmentLists: outputs.Cam.UserPolicyAttachmentsUserPolicyAttachmentList[];
}

export function userPolicyAttachmentsOutput(args?: UserPolicyAttachmentsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<UserPolicyAttachmentsResult> {
    return pulumi.output(args).apply(a => userPolicyAttachments(a, opts))
}

/**
 * A collection of arguments for invoking UserPolicyAttachments.
 */
export interface UserPolicyAttachmentsOutputArgs {
    createMode?: pulumi.Input<number>;
    policyId?: pulumi.Input<string>;
    policyType?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
    /**
     * @deprecated It has been deprecated from version 1.59.6. Use `user_name` instead.
     */
    userId?: pulumi.Input<string>;
    userName?: pulumi.Input<string>;
}
