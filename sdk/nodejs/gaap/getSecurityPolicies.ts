// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to query security policies of GAAP proxy.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const fooProxy = new tencentcloud.gaap.Proxy("fooProxy", {
 *     bandwidth: 10,
 *     concurrent: 2,
 *     accessRegion: "SouthChina",
 *     realserverRegion: "NorthChina",
 * });
 * const fooSecurityPolicy = new tencentcloud.gaap.SecurityPolicy("fooSecurityPolicy", {
 *     proxyId: fooProxy.id,
 *     action: "ACCEPT",
 * });
 * const fooSecurityPolicies = tencentcloud.Gaap.getSecurityPoliciesOutput({
 *     id: fooSecurityPolicy.id,
 * });
 * ```
 */
export function getSecurityPolicies(args: GetSecurityPoliciesArgs, opts?: pulumi.InvokeOptions): Promise<GetSecurityPoliciesResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Gaap/getSecurityPolicies:getSecurityPolicies", {
        "id": args.id,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking getSecurityPolicies.
 */
export interface GetSecurityPoliciesArgs {
    /**
     * ID of the security policy to be queried.
     */
    id: string;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
}

/**
 * A collection of values returned by getSecurityPolicies.
 */
export interface GetSecurityPoliciesResult {
    /**
     * Default policy.
     */
    readonly action: string;
    readonly id: string;
    /**
     * ID of the GAAP proxy.
     */
    readonly proxyId: string;
    readonly resultOutputFile?: string;
    /**
     * Status of the security policy.
     */
    readonly status: string;
}

export function getSecurityPoliciesOutput(args: GetSecurityPoliciesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSecurityPoliciesResult> {
    return pulumi.output(args).apply(a => getSecurityPolicies(a, opts))
}

/**
 * A collection of arguments for invoking getSecurityPolicies.
 */
export interface GetSecurityPoliciesOutputArgs {
    /**
     * ID of the security policy to be queried.
     */
    id: pulumi.Input<string>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
}
