// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function proxies(args?: ProxiesArgs, opts?: pulumi.InvokeOptions): Promise<ProxiesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Gaap/proxies:Proxies", {
        "accessRegion": args.accessRegion,
        "ids": args.ids,
        "projectId": args.projectId,
        "realserverRegion": args.realserverRegion,
        "resultOutputFile": args.resultOutputFile,
        "tags": args.tags,
    }, opts);
}

/**
 * A collection of arguments for invoking Proxies.
 */
export interface ProxiesArgs {
    accessRegion?: string;
    ids?: string[];
    projectId?: number;
    realserverRegion?: string;
    resultOutputFile?: string;
    tags?: {[key: string]: any};
}

/**
 * A collection of values returned by Proxies.
 */
export interface ProxiesResult {
    readonly accessRegion?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly ids?: string[];
    readonly projectId?: number;
    readonly proxies: outputs.Gaap.ProxiesProxy[];
    readonly realserverRegion?: string;
    readonly resultOutputFile?: string;
    readonly tags?: {[key: string]: any};
}

export function proxiesOutput(args?: ProxiesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ProxiesResult> {
    return pulumi.output(args).apply(a => proxies(a, opts))
}

/**
 * A collection of arguments for invoking Proxies.
 */
export interface ProxiesOutputArgs {
    accessRegion?: pulumi.Input<string>;
    ids?: pulumi.Input<pulumi.Input<string>[]>;
    projectId?: pulumi.Input<number>;
    realserverRegion?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
    tags?: pulumi.Input<{[key: string]: any}>;
}
