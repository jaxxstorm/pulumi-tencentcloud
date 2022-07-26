// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function idls(args: IdlsArgs, opts?: pulumi.InvokeOptions): Promise<IdlsResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Tcaplus/idls:Idls", {
        "clusterId": args.clusterId,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking Idls.
 */
export interface IdlsArgs {
    clusterId: string;
    resultOutputFile?: string;
}

/**
 * A collection of values returned by Idls.
 */
export interface IdlsResult {
    readonly clusterId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly lists: outputs.Tcaplus.IdlsList[];
    readonly resultOutputFile?: string;
}

export function idlsOutput(args: IdlsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<IdlsResult> {
    return pulumi.output(args).apply(a => idls(a, opts))
}

/**
 * A collection of arguments for invoking Idls.
 */
export interface IdlsOutputArgs {
    clusterId: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
}
