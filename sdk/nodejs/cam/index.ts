// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./group";
export * from "./groupMembership";
export * from "./groupMemberships";
export * from "./groupPolicyAttachment";
export * from "./groupPolicyAttachments";
export * from "./groups";
export * from "./oidcsso";
export * from "./policies";
export * from "./policy";
export * from "./role";
export * from "./rolePolicyAttachment";
export * from "./rolePolicyAttachments";
export * from "./roleSSO";
export * from "./roles";
export * from "./samlprovider";
export * from "./samlproviders";
export * from "./user";
export * from "./userPolicyAttachment";
export * from "./userPolicyAttachments";
export * from "./users";

// Import resources to register:
import { Group } from "./group";
import { GroupMembership } from "./groupMembership";
import { GroupPolicyAttachment } from "./groupPolicyAttachment";
import { OIDCSSO } from "./oidcsso";
import { Policy } from "./policy";
import { Role } from "./role";
import { RolePolicyAttachment } from "./rolePolicyAttachment";
import { RoleSSO } from "./roleSSO";
import { SAMLProvider } from "./samlprovider";
import { User } from "./user";
import { UserPolicyAttachment } from "./userPolicyAttachment";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Cam/group:Group":
                return new Group(name, <any>undefined, { urn })
            case "tencentcloud:Cam/groupMembership:GroupMembership":
                return new GroupMembership(name, <any>undefined, { urn })
            case "tencentcloud:Cam/groupPolicyAttachment:GroupPolicyAttachment":
                return new GroupPolicyAttachment(name, <any>undefined, { urn })
            case "tencentcloud:Cam/oIDCSSO:OIDCSSO":
                return new OIDCSSO(name, <any>undefined, { urn })
            case "tencentcloud:Cam/policy:Policy":
                return new Policy(name, <any>undefined, { urn })
            case "tencentcloud:Cam/role:Role":
                return new Role(name, <any>undefined, { urn })
            case "tencentcloud:Cam/rolePolicyAttachment:RolePolicyAttachment":
                return new RolePolicyAttachment(name, <any>undefined, { urn })
            case "tencentcloud:Cam/roleSSO:RoleSSO":
                return new RoleSSO(name, <any>undefined, { urn })
            case "tencentcloud:Cam/sAMLProvider:SAMLProvider":
                return new SAMLProvider(name, <any>undefined, { urn })
            case "tencentcloud:Cam/user:User":
                return new User(name, <any>undefined, { urn })
            case "tencentcloud:Cam/userPolicyAttachment:UserPolicyAttachment":
                return new UserPolicyAttachment(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/group", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/groupMembership", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/groupPolicyAttachment", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/oIDCSSO", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/policy", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/role", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/rolePolicyAttachment", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/roleSSO", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/sAMLProvider", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/user", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cam/userPolicyAttachment", _module)
