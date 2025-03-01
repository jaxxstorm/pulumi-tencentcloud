// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query detailed information of HA VIP EIP attachments
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const foo = pulumi.output(tencentcloud.Ha.getVipEipAttachments({
 *     addressIp: "1.1.1.1",
 *     havipId: "havip-kjqwe4ba",
 * }));
 * ```
 */
export function getVipEipAttachments(args: GetVipEipAttachmentsArgs, opts?: pulumi.InvokeOptions): Promise<GetVipEipAttachmentsResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Ha/getVipEipAttachments:getVipEipAttachments", {
        "addressIp": args.addressIp,
        "havipId": args.havipId,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking getVipEipAttachments.
 */
export interface GetVipEipAttachmentsArgs {
    /**
     * Public IP address of EIP to be queried.
     */
    addressIp?: string;
    /**
     * ID of the attached HA VIP to be queried.
     */
    havipId: string;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
}

/**
 * A collection of values returned by getVipEipAttachments.
 */
export interface GetVipEipAttachmentsResult {
    /**
     * Public IP address of EIP.
     */
    readonly addressIp?: string;
    /**
     * A list of HA VIP EIP attachments. Each element contains the following attributes:
     */
    readonly haVipEipAttachmentLists: outputs.Ha.GetVipEipAttachmentsHaVipEipAttachmentList[];
    /**
     * ID of the attached HA VIP.
     */
    readonly havipId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly resultOutputFile?: string;
}

export function getVipEipAttachmentsOutput(args: GetVipEipAttachmentsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVipEipAttachmentsResult> {
    return pulumi.output(args).apply(a => getVipEipAttachments(a, opts))
}

/**
 * A collection of arguments for invoking getVipEipAttachments.
 */
export interface GetVipEipAttachmentsOutputArgs {
    /**
     * Public IP address of EIP to be queried.
     */
    addressIp?: pulumi.Input<string>;
    /**
     * ID of the attached HA VIP to be queried.
     */
    havipId: pulumi.Input<string>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
}
