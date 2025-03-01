// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query detailed instance information of Ckafka
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const foo = pulumi.output(tencentcloud.Ckafka.getInstances({
 *     instanceIds: ["ckafka-vv7wpvae"],
 * }));
 * ```
 */
export function getInstances(args?: GetInstancesArgs, opts?: pulumi.InvokeOptions): Promise<GetInstancesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Ckafka/getInstances:getInstances", {
        "filters": args.filters,
        "instanceIds": args.instanceIds,
        "limit": args.limit,
        "offset": args.offset,
        "resultOutputFile": args.resultOutputFile,
        "searchWord": args.searchWord,
        "statuses": args.statuses,
        "tagKey": args.tagKey,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstances.
 */
export interface GetInstancesArgs {
    /**
     * Filter. filter.name supports ('Ip', 'VpcId', 'SubNetId', 'InstanceType','InstanceId'), filter.values can pass up to 10 values.
     */
    filters?: inputs.Ckafka.GetInstancesFilter[];
    /**
     * Filter by instance ID.
     */
    instanceIds?: string[];
    /**
     * The number of pages, default is `10`.
     */
    limit?: number;
    /**
     * The page start offset, default is `0`.
     */
    offset?: number;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
    /**
     * Filter by instance name, support fuzzy query.
     */
    searchWord?: string;
    /**
     * (Filter Criteria) The status of the instance. 0: Create, 1: Run, 2: Delete, do not fill the default return all.
     */
    statuses?: number[];
    /**
     * Matches the tag key value.
     */
    tagKey?: string;
}

/**
 * A collection of values returned by getInstances.
 */
export interface GetInstancesResult {
    readonly filters?: outputs.Ckafka.GetInstancesFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly instanceIds?: string[];
    /**
     * A list of ckafka users. Each element contains the following attributes:
     */
    readonly instanceLists: outputs.Ckafka.GetInstancesInstanceList[];
    readonly limit?: number;
    readonly offset?: number;
    readonly resultOutputFile?: string;
    readonly searchWord?: string;
    /**
     * The status of the instance. 0: Created, 1: Running, 2: Delete: 5 Quarantined, -1 Creation failed.
     */
    readonly statuses?: number[];
    /**
     * Tag Key.
     */
    readonly tagKey?: string;
}

export function getInstancesOutput(args?: GetInstancesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstancesResult> {
    return pulumi.output(args).apply(a => getInstances(a, opts))
}

/**
 * A collection of arguments for invoking getInstances.
 */
export interface GetInstancesOutputArgs {
    /**
     * Filter. filter.name supports ('Ip', 'VpcId', 'SubNetId', 'InstanceType','InstanceId'), filter.values can pass up to 10 values.
     */
    filters?: pulumi.Input<pulumi.Input<inputs.Ckafka.GetInstancesFilterArgs>[]>;
    /**
     * Filter by instance ID.
     */
    instanceIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The number of pages, default is `10`.
     */
    limit?: pulumi.Input<number>;
    /**
     * The page start offset, default is `0`.
     */
    offset?: pulumi.Input<number>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
    /**
     * Filter by instance name, support fuzzy query.
     */
    searchWord?: pulumi.Input<string>;
    /**
     * (Filter Criteria) The status of the instance. 0: Create, 1: Run, 2: Delete, do not fill the default return all.
     */
    statuses?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Matches the tag key value.
     */
    tagKey?: pulumi.Input<string>;
}
