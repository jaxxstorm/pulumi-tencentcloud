// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function logs(args: LogsArgs, opts?: pulumi.InvokeOptions): Promise<LogsResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Scf/logs:Logs", {
        "endTime": args.endTime,
        "functionName": args.functionName,
        "invokeRequestId": args.invokeRequestId,
        "limit": args.limit,
        "namespace": args.namespace,
        "offset": args.offset,
        "order": args.order,
        "orderBy": args.orderBy,
        "resultOutputFile": args.resultOutputFile,
        "retCode": args.retCode,
        "startTime": args.startTime,
    }, opts);
}

/**
 * A collection of arguments for invoking Logs.
 */
export interface LogsArgs {
    endTime?: string;
    functionName: string;
    invokeRequestId?: string;
    limit?: number;
    namespace?: string;
    offset?: number;
    order?: string;
    orderBy?: string;
    resultOutputFile?: string;
    retCode?: string;
    startTime?: string;
}

/**
 * A collection of values returned by Logs.
 */
export interface LogsResult {
    readonly endTime?: string;
    readonly functionName: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly invokeRequestId?: string;
    readonly limit?: number;
    readonly logs: outputs.Scf.LogsLog[];
    readonly namespace?: string;
    readonly offset?: number;
    readonly order?: string;
    readonly orderBy?: string;
    readonly resultOutputFile?: string;
    readonly retCode?: string;
    readonly startTime?: string;
}

export function logsOutput(args: LogsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<LogsResult> {
    return pulumi.output(args).apply(a => logs(a, opts))
}

/**
 * A collection of arguments for invoking Logs.
 */
export interface LogsOutputArgs {
    endTime?: pulumi.Input<string>;
    functionName: pulumi.Input<string>;
    invokeRequestId?: pulumi.Input<string>;
    limit?: pulumi.Input<number>;
    namespace?: pulumi.Input<string>;
    offset?: pulumi.Input<number>;
    order?: pulumi.Input<string>;
    orderBy?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
    retCode?: pulumi.Input<string>;
    startTime?: pulumi.Input<string>;
}
