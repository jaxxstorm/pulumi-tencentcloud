// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export class ScalingConfig extends pulumi.CustomResource {
    /**
     * Get an existing ScalingConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScalingConfigState, opts?: pulumi.CustomResourceOptions): ScalingConfig {
        return new ScalingConfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:As/scalingConfig:ScalingConfig';

    /**
     * Returns true if the given object is an instance of ScalingConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ScalingConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ScalingConfig.__pulumiType;
    }

    /**
     * CAM role name authorized to access.
     */
    public readonly camRoleName!: pulumi.Output<string | undefined>;
    /**
     * Name of a launch configuration.
     */
    public readonly configurationName!: pulumi.Output<string>;
    /**
     * The time when the launch configuration was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * Configurations of data disk.
     */
    public readonly dataDisks!: pulumi.Output<outputs.As.ScalingConfigDataDisk[] | undefined>;
    /**
     * Policy of cloud disk type. Valid values: `ORIGINAL` and `AUTOMATIC`. Default is `ORIGINAL`.
     */
    public readonly diskTypePolicy!: pulumi.Output<string | undefined>;
    /**
     * To specify whether to enable cloud monitor service. Default is `TRUE`.
     */
    public readonly enhancedMonitorService!: pulumi.Output<boolean | undefined>;
    /**
     * To specify whether to enable cloud security service. Default is `TRUE`.
     */
    public readonly enhancedSecurityService!: pulumi.Output<boolean | undefined>;
    /**
     * An available image ID for a cvm instance.
     */
    public readonly imageId!: pulumi.Output<string>;
    /**
     * Charge type of instance. Valid values are `PREPAID`, `POSTPAID_BY_HOUR`, `SPOTPAID`. The default is `POSTPAID_BY_HOUR`.
     * NOTE: `SPOTPAID` instance must set `spot_instance_type` and `spot_max_price` at the same time.
     */
    public readonly instanceChargeType!: pulumi.Output<string | undefined>;
    /**
     * The tenancy (in month) of the prepaid instance, NOTE: it only works when instance_charge_type is set to `PREPAID`. Valid
     * values are `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`.
     */
    public readonly instanceChargeTypePrepaidPeriod!: pulumi.Output<number | undefined>;
    /**
     * Auto renewal flag. Valid values: `NOTIFY_AND_AUTO_RENEW`: notify upon expiration and renew automatically,
     * `NOTIFY_AND_MANUAL_RENEW`: notify upon expiration but do not renew automatically, `DISABLE_NOTIFY_AND_MANUAL_RENEW`:
     * neither notify upon expiration nor renew automatically. Default value: `NOTIFY_AND_MANUAL_RENEW`. If this parameter is
     * specified as `NOTIFY_AND_AUTO_RENEW`, the instance will be automatically renewed on a monthly basis if the account
     * balance is sufficient. NOTE: it only works when instance_charge_type is set to `PREPAID`.
     */
    public readonly instanceChargeTypePrepaidRenewFlag!: pulumi.Output<string>;
    /**
     * Settings of CVM instance names.
     */
    public readonly instanceNameSettings!: pulumi.Output<outputs.As.ScalingConfigInstanceNameSettings | undefined>;
    /**
     * A list of tags used to associate different resources.
     */
    public readonly instanceTags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * Specified types of CVM instances.
     */
    public readonly instanceTypes!: pulumi.Output<string[]>;
    /**
     * Charge types for network traffic. Valid values: `BANDWIDTH_PREPAID`, `TRAFFIC_POSTPAID_BY_HOUR`,
     * `TRAFFIC_POSTPAID_BY_HOUR` and `BANDWIDTH_PACKAGE`.
     */
    public readonly internetChargeType!: pulumi.Output<string | undefined>;
    /**
     * Max bandwidth of Internet access in Mbps. Default is `0`.
     */
    public readonly internetMaxBandwidthOut!: pulumi.Output<number | undefined>;
    /**
     * Specify whether to keep original settings of a CVM image. And it can't be used with password or key_ids together.
     */
    public readonly keepImageLogin!: pulumi.Output<boolean | undefined>;
    /**
     * ID list of keys.
     */
    public readonly keyIds!: pulumi.Output<string[] | undefined>;
    /**
     * Password to access.
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * Specifys to which project the configuration belongs.
     */
    public readonly projectId!: pulumi.Output<number | undefined>;
    /**
     * Specify whether to assign an Internet IP address.
     */
    public readonly publicIpAssigned!: pulumi.Output<boolean | undefined>;
    /**
     * Security groups to which a CVM instance belongs.
     */
    public readonly securityGroupIds!: pulumi.Output<string[] | undefined>;
    /**
     * Type of spot instance, only support `one-time` now. Note: it only works when instance_charge_type is set to `SPOTPAID`.
     */
    public readonly spotInstanceType!: pulumi.Output<string | undefined>;
    /**
     * Max price of a spot instance, is the format of decimal string, for example "0.50". Note: it only works when
     * instance_charge_type is set to `SPOTPAID`.
     */
    public readonly spotMaxPrice!: pulumi.Output<string | undefined>;
    /**
     * Current statues of a launch configuration.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * Volume of system disk in GB. Default is `50`.
     */
    public readonly systemDiskSize!: pulumi.Output<number | undefined>;
    /**
     * Type of a CVM disk. Valid values: `CLOUD_PREMIUM` and `CLOUD_SSD`. Default is `CLOUD_PREMIUM`. valid when
     * disk_type_policy is ORIGINAL.
     */
    public readonly systemDiskType!: pulumi.Output<string | undefined>;
    /**
     * ase64-encoded User Data text, the length limit is 16KB.
     */
    public readonly userData!: pulumi.Output<string | undefined>;

    /**
     * Create a ScalingConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ScalingConfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ScalingConfigArgs | ScalingConfigState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ScalingConfigState | undefined;
            resourceInputs["camRoleName"] = state ? state.camRoleName : undefined;
            resourceInputs["configurationName"] = state ? state.configurationName : undefined;
            resourceInputs["createTime"] = state ? state.createTime : undefined;
            resourceInputs["dataDisks"] = state ? state.dataDisks : undefined;
            resourceInputs["diskTypePolicy"] = state ? state.diskTypePolicy : undefined;
            resourceInputs["enhancedMonitorService"] = state ? state.enhancedMonitorService : undefined;
            resourceInputs["enhancedSecurityService"] = state ? state.enhancedSecurityService : undefined;
            resourceInputs["imageId"] = state ? state.imageId : undefined;
            resourceInputs["instanceChargeType"] = state ? state.instanceChargeType : undefined;
            resourceInputs["instanceChargeTypePrepaidPeriod"] = state ? state.instanceChargeTypePrepaidPeriod : undefined;
            resourceInputs["instanceChargeTypePrepaidRenewFlag"] = state ? state.instanceChargeTypePrepaidRenewFlag : undefined;
            resourceInputs["instanceNameSettings"] = state ? state.instanceNameSettings : undefined;
            resourceInputs["instanceTags"] = state ? state.instanceTags : undefined;
            resourceInputs["instanceTypes"] = state ? state.instanceTypes : undefined;
            resourceInputs["internetChargeType"] = state ? state.internetChargeType : undefined;
            resourceInputs["internetMaxBandwidthOut"] = state ? state.internetMaxBandwidthOut : undefined;
            resourceInputs["keepImageLogin"] = state ? state.keepImageLogin : undefined;
            resourceInputs["keyIds"] = state ? state.keyIds : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["publicIpAssigned"] = state ? state.publicIpAssigned : undefined;
            resourceInputs["securityGroupIds"] = state ? state.securityGroupIds : undefined;
            resourceInputs["spotInstanceType"] = state ? state.spotInstanceType : undefined;
            resourceInputs["spotMaxPrice"] = state ? state.spotMaxPrice : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["systemDiskSize"] = state ? state.systemDiskSize : undefined;
            resourceInputs["systemDiskType"] = state ? state.systemDiskType : undefined;
            resourceInputs["userData"] = state ? state.userData : undefined;
        } else {
            const args = argsOrState as ScalingConfigArgs | undefined;
            if ((!args || args.configurationName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'configurationName'");
            }
            if ((!args || args.imageId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'imageId'");
            }
            if ((!args || args.instanceTypes === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceTypes'");
            }
            resourceInputs["camRoleName"] = args ? args.camRoleName : undefined;
            resourceInputs["configurationName"] = args ? args.configurationName : undefined;
            resourceInputs["dataDisks"] = args ? args.dataDisks : undefined;
            resourceInputs["diskTypePolicy"] = args ? args.diskTypePolicy : undefined;
            resourceInputs["enhancedMonitorService"] = args ? args.enhancedMonitorService : undefined;
            resourceInputs["enhancedSecurityService"] = args ? args.enhancedSecurityService : undefined;
            resourceInputs["imageId"] = args ? args.imageId : undefined;
            resourceInputs["instanceChargeType"] = args ? args.instanceChargeType : undefined;
            resourceInputs["instanceChargeTypePrepaidPeriod"] = args ? args.instanceChargeTypePrepaidPeriod : undefined;
            resourceInputs["instanceChargeTypePrepaidRenewFlag"] = args ? args.instanceChargeTypePrepaidRenewFlag : undefined;
            resourceInputs["instanceNameSettings"] = args ? args.instanceNameSettings : undefined;
            resourceInputs["instanceTags"] = args ? args.instanceTags : undefined;
            resourceInputs["instanceTypes"] = args ? args.instanceTypes : undefined;
            resourceInputs["internetChargeType"] = args ? args.internetChargeType : undefined;
            resourceInputs["internetMaxBandwidthOut"] = args ? args.internetMaxBandwidthOut : undefined;
            resourceInputs["keepImageLogin"] = args ? args.keepImageLogin : undefined;
            resourceInputs["keyIds"] = args ? args.keyIds : undefined;
            resourceInputs["password"] = args ? args.password : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["publicIpAssigned"] = args ? args.publicIpAssigned : undefined;
            resourceInputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            resourceInputs["spotInstanceType"] = args ? args.spotInstanceType : undefined;
            resourceInputs["spotMaxPrice"] = args ? args.spotMaxPrice : undefined;
            resourceInputs["systemDiskSize"] = args ? args.systemDiskSize : undefined;
            resourceInputs["systemDiskType"] = args ? args.systemDiskType : undefined;
            resourceInputs["userData"] = args ? args.userData : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ScalingConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ScalingConfig resources.
 */
export interface ScalingConfigState {
    /**
     * CAM role name authorized to access.
     */
    camRoleName?: pulumi.Input<string>;
    /**
     * Name of a launch configuration.
     */
    configurationName?: pulumi.Input<string>;
    /**
     * The time when the launch configuration was created.
     */
    createTime?: pulumi.Input<string>;
    /**
     * Configurations of data disk.
     */
    dataDisks?: pulumi.Input<pulumi.Input<inputs.As.ScalingConfigDataDisk>[]>;
    /**
     * Policy of cloud disk type. Valid values: `ORIGINAL` and `AUTOMATIC`. Default is `ORIGINAL`.
     */
    diskTypePolicy?: pulumi.Input<string>;
    /**
     * To specify whether to enable cloud monitor service. Default is `TRUE`.
     */
    enhancedMonitorService?: pulumi.Input<boolean>;
    /**
     * To specify whether to enable cloud security service. Default is `TRUE`.
     */
    enhancedSecurityService?: pulumi.Input<boolean>;
    /**
     * An available image ID for a cvm instance.
     */
    imageId?: pulumi.Input<string>;
    /**
     * Charge type of instance. Valid values are `PREPAID`, `POSTPAID_BY_HOUR`, `SPOTPAID`. The default is `POSTPAID_BY_HOUR`.
     * NOTE: `SPOTPAID` instance must set `spot_instance_type` and `spot_max_price` at the same time.
     */
    instanceChargeType?: pulumi.Input<string>;
    /**
     * The tenancy (in month) of the prepaid instance, NOTE: it only works when instance_charge_type is set to `PREPAID`. Valid
     * values are `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`.
     */
    instanceChargeTypePrepaidPeriod?: pulumi.Input<number>;
    /**
     * Auto renewal flag. Valid values: `NOTIFY_AND_AUTO_RENEW`: notify upon expiration and renew automatically,
     * `NOTIFY_AND_MANUAL_RENEW`: notify upon expiration but do not renew automatically, `DISABLE_NOTIFY_AND_MANUAL_RENEW`:
     * neither notify upon expiration nor renew automatically. Default value: `NOTIFY_AND_MANUAL_RENEW`. If this parameter is
     * specified as `NOTIFY_AND_AUTO_RENEW`, the instance will be automatically renewed on a monthly basis if the account
     * balance is sufficient. NOTE: it only works when instance_charge_type is set to `PREPAID`.
     */
    instanceChargeTypePrepaidRenewFlag?: pulumi.Input<string>;
    /**
     * Settings of CVM instance names.
     */
    instanceNameSettings?: pulumi.Input<inputs.As.ScalingConfigInstanceNameSettings>;
    /**
     * A list of tags used to associate different resources.
     */
    instanceTags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Specified types of CVM instances.
     */
    instanceTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Charge types for network traffic. Valid values: `BANDWIDTH_PREPAID`, `TRAFFIC_POSTPAID_BY_HOUR`,
     * `TRAFFIC_POSTPAID_BY_HOUR` and `BANDWIDTH_PACKAGE`.
     */
    internetChargeType?: pulumi.Input<string>;
    /**
     * Max bandwidth of Internet access in Mbps. Default is `0`.
     */
    internetMaxBandwidthOut?: pulumi.Input<number>;
    /**
     * Specify whether to keep original settings of a CVM image. And it can't be used with password or key_ids together.
     */
    keepImageLogin?: pulumi.Input<boolean>;
    /**
     * ID list of keys.
     */
    keyIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Password to access.
     */
    password?: pulumi.Input<string>;
    /**
     * Specifys to which project the configuration belongs.
     */
    projectId?: pulumi.Input<number>;
    /**
     * Specify whether to assign an Internet IP address.
     */
    publicIpAssigned?: pulumi.Input<boolean>;
    /**
     * Security groups to which a CVM instance belongs.
     */
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Type of spot instance, only support `one-time` now. Note: it only works when instance_charge_type is set to `SPOTPAID`.
     */
    spotInstanceType?: pulumi.Input<string>;
    /**
     * Max price of a spot instance, is the format of decimal string, for example "0.50". Note: it only works when
     * instance_charge_type is set to `SPOTPAID`.
     */
    spotMaxPrice?: pulumi.Input<string>;
    /**
     * Current statues of a launch configuration.
     */
    status?: pulumi.Input<string>;
    /**
     * Volume of system disk in GB. Default is `50`.
     */
    systemDiskSize?: pulumi.Input<number>;
    /**
     * Type of a CVM disk. Valid values: `CLOUD_PREMIUM` and `CLOUD_SSD`. Default is `CLOUD_PREMIUM`. valid when
     * disk_type_policy is ORIGINAL.
     */
    systemDiskType?: pulumi.Input<string>;
    /**
     * ase64-encoded User Data text, the length limit is 16KB.
     */
    userData?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ScalingConfig resource.
 */
export interface ScalingConfigArgs {
    /**
     * CAM role name authorized to access.
     */
    camRoleName?: pulumi.Input<string>;
    /**
     * Name of a launch configuration.
     */
    configurationName: pulumi.Input<string>;
    /**
     * Configurations of data disk.
     */
    dataDisks?: pulumi.Input<pulumi.Input<inputs.As.ScalingConfigDataDisk>[]>;
    /**
     * Policy of cloud disk type. Valid values: `ORIGINAL` and `AUTOMATIC`. Default is `ORIGINAL`.
     */
    diskTypePolicy?: pulumi.Input<string>;
    /**
     * To specify whether to enable cloud monitor service. Default is `TRUE`.
     */
    enhancedMonitorService?: pulumi.Input<boolean>;
    /**
     * To specify whether to enable cloud security service. Default is `TRUE`.
     */
    enhancedSecurityService?: pulumi.Input<boolean>;
    /**
     * An available image ID for a cvm instance.
     */
    imageId: pulumi.Input<string>;
    /**
     * Charge type of instance. Valid values are `PREPAID`, `POSTPAID_BY_HOUR`, `SPOTPAID`. The default is `POSTPAID_BY_HOUR`.
     * NOTE: `SPOTPAID` instance must set `spot_instance_type` and `spot_max_price` at the same time.
     */
    instanceChargeType?: pulumi.Input<string>;
    /**
     * The tenancy (in month) of the prepaid instance, NOTE: it only works when instance_charge_type is set to `PREPAID`. Valid
     * values are `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`.
     */
    instanceChargeTypePrepaidPeriod?: pulumi.Input<number>;
    /**
     * Auto renewal flag. Valid values: `NOTIFY_AND_AUTO_RENEW`: notify upon expiration and renew automatically,
     * `NOTIFY_AND_MANUAL_RENEW`: notify upon expiration but do not renew automatically, `DISABLE_NOTIFY_AND_MANUAL_RENEW`:
     * neither notify upon expiration nor renew automatically. Default value: `NOTIFY_AND_MANUAL_RENEW`. If this parameter is
     * specified as `NOTIFY_AND_AUTO_RENEW`, the instance will be automatically renewed on a monthly basis if the account
     * balance is sufficient. NOTE: it only works when instance_charge_type is set to `PREPAID`.
     */
    instanceChargeTypePrepaidRenewFlag?: pulumi.Input<string>;
    /**
     * Settings of CVM instance names.
     */
    instanceNameSettings?: pulumi.Input<inputs.As.ScalingConfigInstanceNameSettings>;
    /**
     * A list of tags used to associate different resources.
     */
    instanceTags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Specified types of CVM instances.
     */
    instanceTypes: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Charge types for network traffic. Valid values: `BANDWIDTH_PREPAID`, `TRAFFIC_POSTPAID_BY_HOUR`,
     * `TRAFFIC_POSTPAID_BY_HOUR` and `BANDWIDTH_PACKAGE`.
     */
    internetChargeType?: pulumi.Input<string>;
    /**
     * Max bandwidth of Internet access in Mbps. Default is `0`.
     */
    internetMaxBandwidthOut?: pulumi.Input<number>;
    /**
     * Specify whether to keep original settings of a CVM image. And it can't be used with password or key_ids together.
     */
    keepImageLogin?: pulumi.Input<boolean>;
    /**
     * ID list of keys.
     */
    keyIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Password to access.
     */
    password?: pulumi.Input<string>;
    /**
     * Specifys to which project the configuration belongs.
     */
    projectId?: pulumi.Input<number>;
    /**
     * Specify whether to assign an Internet IP address.
     */
    publicIpAssigned?: pulumi.Input<boolean>;
    /**
     * Security groups to which a CVM instance belongs.
     */
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Type of spot instance, only support `one-time` now. Note: it only works when instance_charge_type is set to `SPOTPAID`.
     */
    spotInstanceType?: pulumi.Input<string>;
    /**
     * Max price of a spot instance, is the format of decimal string, for example "0.50". Note: it only works when
     * instance_charge_type is set to `SPOTPAID`.
     */
    spotMaxPrice?: pulumi.Input<string>;
    /**
     * Volume of system disk in GB. Default is `50`.
     */
    systemDiskSize?: pulumi.Input<number>;
    /**
     * Type of a CVM disk. Valid values: `CLOUD_PREMIUM` and `CLOUD_SSD`. Default is `CLOUD_PREMIUM`. valid when
     * disk_type_policy is ORIGINAL.
     */
    systemDiskType?: pulumi.Input<string>;
    /**
     * ase64-encoded User Data text, the length limit is 16KB.
     */
    userData?: pulumi.Input<string>;
}
