// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function customerGateways(args?: CustomerGatewaysArgs, opts?: pulumi.InvokeOptions): Promise<CustomerGatewaysResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Vpn/customerGateways:CustomerGateways", {
        "id": args.id,
        "name": args.name,
        "publicIpAddress": args.publicIpAddress,
        "resultOutputFile": args.resultOutputFile,
        "tags": args.tags,
    }, opts);
}

/**
 * A collection of arguments for invoking CustomerGateways.
 */
export interface CustomerGatewaysArgs {
    id?: string;
    name?: string;
    publicIpAddress?: string;
    resultOutputFile?: string;
    tags?: {[key: string]: any};
}

/**
 * A collection of values returned by CustomerGateways.
 */
export interface CustomerGatewaysResult {
    readonly gatewayLists: outputs.Vpn.CustomerGatewaysGatewayList[];
    readonly id?: string;
    readonly name?: string;
    readonly publicIpAddress?: string;
    readonly resultOutputFile?: string;
    readonly tags?: {[key: string]: any};
}

export function customerGatewaysOutput(args?: CustomerGatewaysOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<CustomerGatewaysResult> {
    return pulumi.output(args).apply(a => customerGateways(a, opts))
}

/**
 * A collection of arguments for invoking CustomerGateways.
 */
export interface CustomerGatewaysOutputArgs {
    id?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    publicIpAddress?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
    tags?: pulumi.Input<{[key: string]: any}>;
}
