// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./alarmPolicy";
export * from "./bindingReceiver";
export * from "./getBindingObjects";
export * from "./getData";
export * from "./getPolicyConditions";
export * from "./getPolicyGroups";
export * from "./getProductEvent";
export * from "./getProductNamespace";
export * from "./policyBindingObject";
export * from "./tmpAlertRule";
export * from "./tmpCvmAgent";
export * from "./tmpExporterIntegration";
export * from "./tmpInstance";
export * from "./tmpRecordingRule";
export * from "./tmpScrapeJob";
export * from "./tmpTkeAlertPolicy";
export * from "./tmpTkeTemplate";

// Import resources to register:
import { AlarmPolicy } from "./alarmPolicy";
import { BindingReceiver } from "./bindingReceiver";
import { PolicyBindingObject } from "./policyBindingObject";
import { TmpAlertRule } from "./tmpAlertRule";
import { TmpCvmAgent } from "./tmpCvmAgent";
import { TmpExporterIntegration } from "./tmpExporterIntegration";
import { TmpInstance } from "./tmpInstance";
import { TmpRecordingRule } from "./tmpRecordingRule";
import { TmpScrapeJob } from "./tmpScrapeJob";
import { TmpTkeAlertPolicy } from "./tmpTkeAlertPolicy";
import { TmpTkeTemplate } from "./tmpTkeTemplate";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Monitor/alarmPolicy:AlarmPolicy":
                return new AlarmPolicy(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/bindingReceiver:BindingReceiver":
                return new BindingReceiver(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/policyBindingObject:PolicyBindingObject":
                return new PolicyBindingObject(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpAlertRule:TmpAlertRule":
                return new TmpAlertRule(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpCvmAgent:TmpCvmAgent":
                return new TmpCvmAgent(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpExporterIntegration:TmpExporterIntegration":
                return new TmpExporterIntegration(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpInstance:TmpInstance":
                return new TmpInstance(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpRecordingRule:TmpRecordingRule":
                return new TmpRecordingRule(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpScrapeJob:TmpScrapeJob":
                return new TmpScrapeJob(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpTkeAlertPolicy:TmpTkeAlertPolicy":
                return new TmpTkeAlertPolicy(name, <any>undefined, { urn })
            case "tencentcloud:Monitor/tmpTkeTemplate:TmpTkeTemplate":
                return new TmpTkeTemplate(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/alarmPolicy", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/bindingReceiver", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/policyBindingObject", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpAlertRule", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpCvmAgent", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpExporterIntegration", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpInstance", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpRecordingRule", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpScrapeJob", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpTkeAlertPolicy", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Monitor/tmpTkeTemplate", _module)
