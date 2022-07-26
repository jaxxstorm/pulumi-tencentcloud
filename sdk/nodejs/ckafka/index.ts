// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./acl";
export * from "./acls";
export * from "./instance";
export * from "./topic";
export * from "./topics";
export * from "./user";
export * from "./users";

// Import resources to register:
import { Acl } from "./acl";
import { Instance } from "./instance";
import { Topic } from "./topic";
import { User } from "./user";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Ckafka/acl:Acl":
                return new Acl(name, <any>undefined, { urn })
            case "tencentcloud:Ckafka/instance:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "tencentcloud:Ckafka/topic:Topic":
                return new Topic(name, <any>undefined, { urn })
            case "tencentcloud:Ckafka/user:User":
                return new User(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Ckafka/acl", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Ckafka/instance", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Ckafka/topic", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Ckafka/user", _module)
