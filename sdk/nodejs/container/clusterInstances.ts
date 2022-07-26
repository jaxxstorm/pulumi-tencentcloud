// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function clusterInstances(args: ClusterInstancesArgs, opts?: pulumi.InvokeOptions): Promise<ClusterInstancesResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Container/clusterInstances:ClusterInstances", {
        "clusterId": args.clusterId,
        "limit": args.limit,
    }, opts);
}

/**
 * A collection of arguments for invoking ClusterInstances.
 */
export interface ClusterInstancesArgs {
    clusterId: string;
    limit?: number;
}

/**
 * A collection of values returned by ClusterInstances.
 */
export interface ClusterInstancesResult {
    readonly clusterId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly limit?: number;
    readonly nodes: outputs.Container.ClusterInstancesNode[];
    readonly totalCount: number;
}

export function clusterInstancesOutput(args: ClusterInstancesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ClusterInstancesResult> {
    return pulumi.output(args).apply(a => clusterInstances(a, opts))
}

/**
 * A collection of arguments for invoking ClusterInstances.
 */
export interface ClusterInstancesOutputArgs {
    clusterId: pulumi.Input<string>;
    limit?: pulumi.Input<number>;
}
