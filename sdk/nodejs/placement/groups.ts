// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function groups(args?: GroupsArgs, opts?: pulumi.InvokeOptions): Promise<GroupsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Placement/groups:Groups", {
        "name": args.name,
        "placementGroupId": args.placementGroupId,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking Groups.
 */
export interface GroupsArgs {
    name?: string;
    placementGroupId?: string;
    resultOutputFile?: string;
}

/**
 * A collection of values returned by Groups.
 */
export interface GroupsResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name?: string;
    readonly placementGroupId?: string;
    readonly placementGroupLists: outputs.Placement.GroupsPlacementGroupList[];
    readonly resultOutputFile?: string;
}

export function groupsOutput(args?: GroupsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GroupsResult> {
    return pulumi.output(args).apply(a => groups(a, opts))
}

/**
 * A collection of arguments for invoking Groups.
 */
export interface GroupsOutputArgs {
    name?: pulumi.Input<string>;
    placementGroupId?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
}
