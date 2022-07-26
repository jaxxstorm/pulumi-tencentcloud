// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function namespaces(args?: NamespacesArgs, opts?: pulumi.InvokeOptions): Promise<NamespacesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Scf/namespaces:Namespaces", {
        "description": args.description,
        "namespace": args.namespace,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking Namespaces.
 */
export interface NamespacesArgs {
    description?: string;
    namespace?: string;
    resultOutputFile?: string;
}

/**
 * A collection of values returned by Namespaces.
 */
export interface NamespacesResult {
    readonly description?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly namespace?: string;
    readonly namespaces: outputs.Scf.NamespacesNamespace[];
    readonly resultOutputFile?: string;
}

export function namespacesOutput(args?: NamespacesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<NamespacesResult> {
    return pulumi.output(args).apply(a => namespaces(a, opts))
}

/**
 * A collection of arguments for invoking Namespaces.
 */
export interface NamespacesOutputArgs {
    description?: pulumi.Input<string>;
    namespace?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
}
