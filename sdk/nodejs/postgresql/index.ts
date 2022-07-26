// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./instance";
export * from "./instances";
export * from "./readonlyAttachment";
export * from "./readonlyGroup";
export * from "./readonlyInstance";
export * from "./specinfos";
export * from "./xlogs";

// Import resources to register:
import { Instance } from "./instance";
import { ReadonlyAttachment } from "./readonlyAttachment";
import { ReadonlyGroup } from "./readonlyGroup";
import { ReadonlyInstance } from "./readonlyInstance";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Postgresql/instance:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "tencentcloud:Postgresql/readonlyAttachment:ReadonlyAttachment":
                return new ReadonlyAttachment(name, <any>undefined, { urn })
            case "tencentcloud:Postgresql/readonlyGroup:ReadonlyGroup":
                return new ReadonlyGroup(name, <any>undefined, { urn })
            case "tencentcloud:Postgresql/readonlyInstance:ReadonlyInstance":
                return new ReadonlyInstance(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Postgresql/instance", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Postgresql/readonlyAttachment", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Postgresql/readonlyGroup", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Postgresql/readonlyInstance", _module)
