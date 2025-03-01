// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./accessGroup";
export * from "./accessRule";
export * from "./fileSystem";
export * from "./getAccessGroups";
export * from "./getAccessRules";
export * from "./getFileSystems";

// Import resources to register:
import { AccessGroup } from "./accessGroup";
import { AccessRule } from "./accessRule";
import { FileSystem } from "./fileSystem";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Cfs/accessGroup:AccessGroup":
                return new AccessGroup(name, <any>undefined, { urn })
            case "tencentcloud:Cfs/accessRule:AccessRule":
                return new AccessRule(name, <any>undefined, { urn })
            case "tencentcloud:Cfs/fileSystem:FileSystem":
                return new FileSystem(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Cfs/accessGroup", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cfs/accessRule", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cfs/fileSystem", _module)
