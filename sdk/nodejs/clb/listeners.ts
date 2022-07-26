// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function listeners(args: ListenersArgs, opts?: pulumi.InvokeOptions): Promise<ListenersResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Clb/listeners:Listeners", {
        "clbId": args.clbId,
        "listenerId": args.listenerId,
        "port": args.port,
        "protocol": args.protocol,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking Listeners.
 */
export interface ListenersArgs {
    clbId: string;
    listenerId?: string;
    port?: number;
    protocol?: string;
    resultOutputFile?: string;
}

/**
 * A collection of values returned by Listeners.
 */
export interface ListenersResult {
    readonly clbId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly listenerId?: string;
    readonly listenerLists: outputs.Clb.ListenersListenerList[];
    readonly port?: number;
    readonly protocol?: string;
    readonly resultOutputFile?: string;
}

export function listenersOutput(args: ListenersOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ListenersResult> {
    return pulumi.output(args).apply(a => listeners(a, opts))
}

/**
 * A collection of arguments for invoking Listeners.
 */
export interface ListenersOutputArgs {
    clbId: pulumi.Input<string>;
    listenerId?: pulumi.Input<string>;
    port?: pulumi.Input<number>;
    protocol?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
}
