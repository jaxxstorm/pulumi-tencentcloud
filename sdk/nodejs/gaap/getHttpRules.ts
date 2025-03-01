// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query forward rule of layer7 listeners.
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
 * const fooLayer7Listener = new tencentcloud.gaap.Layer7Listener("fooLayer7Listener", {
 *     protocol: "HTTP",
 *     port: 80,
 *     proxyId: fooProxy.id,
 * });
 * const fooRealserver = new tencentcloud.gaap.Realserver("fooRealserver", {ip: "1.1.1.1"});
 * const fooHttpRule = new tencentcloud.gaap.HttpRule("fooHttpRule", {
 *     listenerId: fooLayer7Listener.id,
 *     domain: "www.qq.com",
 *     path: "/",
 *     realserverType: "IP",
 *     healthCheck: true,
 *     realservers: [{
 *         id: fooRealserver.id,
 *         ip: fooRealserver.ip,
 *         port: 80,
 *     }],
 * });
 * const fooHttpRules = tencentcloud.Gaap.getHttpRulesOutput({
 *     listenerId: fooLayer7Listener.id,
 *     domain: fooHttpRule.domain,
 * });
 * ```
 */
export function getHttpRules(args: GetHttpRulesArgs, opts?: pulumi.InvokeOptions): Promise<GetHttpRulesResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Gaap/getHttpRules:getHttpRules", {
        "domain": args.domain,
        "forwardHost": args.forwardHost,
        "listenerId": args.listenerId,
        "path": args.path,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking getHttpRules.
 */
export interface GetHttpRulesArgs {
    /**
     * Forward domain of the layer7 listener to be queried.
     */
    domain?: string;
    /**
     * Requested host which is forwarded to the realserver by the listener to be queried.
     */
    forwardHost?: string;
    /**
     * ID of the layer7 listener to be queried.
     */
    listenerId: string;
    /**
     * Path of the forward rule to be queried.
     */
    path?: string;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
}

/**
 * A collection of values returned by getHttpRules.
 */
export interface GetHttpRulesResult {
    /**
     * Domain of the GAAP realserver.
     */
    readonly domain?: string;
    /**
     * Requested host which is forwarded to the realserver by the listener.
     */
    readonly forwardHost?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * ID of the layer7 listener.
     */
    readonly listenerId: string;
    /**
     * Path of the forward rule.
     */
    readonly path?: string;
    readonly resultOutputFile?: string;
    /**
     * An information list of forward rule of the layer7 listeners. Each element contains the following attributes:
     */
    readonly rules: outputs.Gaap.GetHttpRulesRule[];
}

export function getHttpRulesOutput(args: GetHttpRulesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetHttpRulesResult> {
    return pulumi.output(args).apply(a => getHttpRules(a, opts))
}

/**
 * A collection of arguments for invoking getHttpRules.
 */
export interface GetHttpRulesOutputArgs {
    /**
     * Forward domain of the layer7 listener to be queried.
     */
    domain?: pulumi.Input<string>;
    /**
     * Requested host which is forwarded to the realserver by the listener to be queried.
     */
    forwardHost?: pulumi.Input<string>;
    /**
     * ID of the layer7 listener to be queried.
     */
    listenerId: pulumi.Input<string>;
    /**
     * Path of the forward rule to be queried.
     */
    path?: pulumi.Input<string>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
}
