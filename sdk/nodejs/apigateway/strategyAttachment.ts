// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to create IP strategy attachment of API gateway.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const serviceService = new tencentcloud.apigateway.Service("serviceService", {
 *     serviceName: "niceservice",
 *     protocol: "http&https",
 *     serviceDesc: "your nice service",
 *     netTypes: [
 *         "INNER",
 *         "OUTER",
 *     ],
 *     ipVersion: "IPv4",
 * });
 * const testIpStrategy = new tencentcloud.apigateway.IpStrategy("testIpStrategy", {
 *     serviceId: serviceService.id,
 *     strategyName: "tf_test",
 *     strategyType: "BLACK",
 *     strategyData: "9.9.9.9",
 * });
 * const api = new tencentcloud.apigateway.Api("api", {
 *     serviceId: serviceService.id,
 *     apiName: "hello_update",
 *     apiDesc: "my hello api update",
 *     authType: "SECRET",
 *     protocol: "HTTP",
 *     enableCors: true,
 *     requestConfigPath: "/user/info",
 *     requestConfigMethod: "POST",
 *     requestParameters: [{
 *         name: "email",
 *         position: "QUERY",
 *         type: "string",
 *         desc: "your email please?",
 *         defaultValue: "tom@qq.com",
 *         required: true,
 *     }],
 *     serviceConfigType: "HTTP",
 *     serviceConfigTimeout: 10,
 *     serviceConfigUrl: "http://www.tencent.com",
 *     serviceConfigPath: "/user",
 *     serviceConfigMethod: "POST",
 *     responseType: "XML",
 *     responseSuccessExample: "<note>success</note>",
 *     responseFailExample: "<note>fail</note>",
 *     responseErrorCodes: [{
 *         code: 10,
 *         msg: "system error",
 *         desc: "system error code",
 *         convertedCode: -10,
 *         needConvert: true,
 *     }],
 * });
 * const serviceServiceRelease = new tencentcloud.apigateway.ServiceRelease("serviceServiceRelease", {
 *     serviceId: serviceService.id,
 *     environmentName: "release",
 *     releaseDesc: "test service release",
 * });
 * const testStrategyAttachment = new tencentcloud.apigateway.StrategyAttachment("testStrategyAttachment", {
 *     serviceId: serviceServiceRelease.serviceId,
 *     strategyId: testIpStrategy.strategyId,
 *     environmentName: "release",
 *     bindApiId: api.id,
 * });
 * ```
 *
 * ## Import
 *
 * IP strategy attachment of API gateway can be imported using the id, e.g.
 *
 * ```sh
 *  $ pulumi import tencentcloud:ApiGateway/strategyAttachment:StrategyAttachment test service-pk2r6bcc#IPStrategy-4kz2ljfi#api-h3wc5r0s#release
 * ```
 */
export class StrategyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing StrategyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StrategyAttachmentState, opts?: pulumi.CustomResourceOptions): StrategyAttachment {
        return new StrategyAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:ApiGateway/strategyAttachment:StrategyAttachment';

    /**
     * Returns true if the given object is an instance of StrategyAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StrategyAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StrategyAttachment.__pulumiType;
    }

    /**
     * The API that needs to be bound.
     */
    public readonly bindApiId!: pulumi.Output<string>;
    /**
     * The environment of the strategy association. Valid values: `test`, `release`, `prepub`.
     */
    public readonly environmentName!: pulumi.Output<string>;
    /**
     * The ID of the API gateway service.
     */
    public readonly serviceId!: pulumi.Output<string>;
    /**
     * The ID of the API gateway strategy.
     */
    public readonly strategyId!: pulumi.Output<string>;

    /**
     * Create a StrategyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StrategyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StrategyAttachmentArgs | StrategyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as StrategyAttachmentState | undefined;
            resourceInputs["bindApiId"] = state ? state.bindApiId : undefined;
            resourceInputs["environmentName"] = state ? state.environmentName : undefined;
            resourceInputs["serviceId"] = state ? state.serviceId : undefined;
            resourceInputs["strategyId"] = state ? state.strategyId : undefined;
        } else {
            const args = argsOrState as StrategyAttachmentArgs | undefined;
            if ((!args || args.bindApiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bindApiId'");
            }
            if ((!args || args.environmentName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'environmentName'");
            }
            if ((!args || args.serviceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceId'");
            }
            if ((!args || args.strategyId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'strategyId'");
            }
            resourceInputs["bindApiId"] = args ? args.bindApiId : undefined;
            resourceInputs["environmentName"] = args ? args.environmentName : undefined;
            resourceInputs["serviceId"] = args ? args.serviceId : undefined;
            resourceInputs["strategyId"] = args ? args.strategyId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(StrategyAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering StrategyAttachment resources.
 */
export interface StrategyAttachmentState {
    /**
     * The API that needs to be bound.
     */
    bindApiId?: pulumi.Input<string>;
    /**
     * The environment of the strategy association. Valid values: `test`, `release`, `prepub`.
     */
    environmentName?: pulumi.Input<string>;
    /**
     * The ID of the API gateway service.
     */
    serviceId?: pulumi.Input<string>;
    /**
     * The ID of the API gateway strategy.
     */
    strategyId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a StrategyAttachment resource.
 */
export interface StrategyAttachmentArgs {
    /**
     * The API that needs to be bound.
     */
    bindApiId: pulumi.Input<string>;
    /**
     * The environment of the strategy association. Valid values: `test`, `release`, `prepub`.
     */
    environmentName: pulumi.Input<string>;
    /**
     * The ID of the API gateway service.
     */
    serviceId: pulumi.Input<string>;
    /**
     * The ID of the API gateway strategy.
     */
    strategyId: pulumi.Input<string>;
}
