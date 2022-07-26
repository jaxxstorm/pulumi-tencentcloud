// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./cluster";
export * from "./clusterCredential";
export * from "./clusters";
export * from "./containerInstance";

// Import resources to register:
import { Cluster } from "./cluster";
import { ContainerInstance } from "./containerInstance";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Eks/cluster:Cluster":
                return new Cluster(name, <any>undefined, { urn })
            case "tencentcloud:Eks/containerInstance:ContainerInstance":
                return new ContainerInstance(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Eks/cluster", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Eks/containerInstance", _module)
