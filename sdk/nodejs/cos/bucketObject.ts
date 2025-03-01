// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a COS object resource to put an object(content or file) to the bucket.
 *
 * ## Example Usage
 *
 * Uploading a file to a bucket
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const myobject = new tencentcloud.Cos.BucketObject("myobject", {
 *     bucket: "mycos-1258798060",
 *     key: "new_object_key",
 *     source: "path/to/file",
 * });
 * ```
 *
 * Uploading a content to a bucket
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const mycos = new tencentcloud.cos.Bucket("mycos", {
 *     bucket: "mycos-1258798060",
 *     acl: "public-read",
 * });
 * const myobject = new tencentcloud.cos.BucketObject("myobject", {
 *     bucket: mycos.bucket,
 *     key: "new_object_key",
 *     content: "the content that you want to upload.",
 * });
 * ```
 */
export class BucketObject extends pulumi.CustomResource {
    /**
     * Get an existing BucketObject resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketObjectState, opts?: pulumi.CustomResourceOptions): BucketObject {
        return new BucketObject(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Cos/bucketObject:BucketObject';

    /**
     * Returns true if the given object is an instance of BucketObject.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BucketObject {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BucketObject.__pulumiType;
    }

    /**
     * The canned ACL to apply. Available values include `private`, `public-read`, and `public-read-write`. Defaults to `private`.
     */
    public readonly acl!: pulumi.Output<string | undefined>;
    /**
     * The name of a bucket to use. Bucket format should be [custom name]-[appid], for example `mycos-1258798060`.
     */
    public readonly bucket!: pulumi.Output<string>;
    /**
     * Specifies caching behavior along the request/reply chain. For further details, RFC2616 can be referred.
     */
    public readonly cacheControl!: pulumi.Output<string>;
    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
     */
    public readonly content!: pulumi.Output<string | undefined>;
    /**
     * Specifies presentational information for the object.
     */
    public readonly contentDisposition!: pulumi.Output<string | undefined>;
    /**
     * Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
     */
    public readonly contentEncoding!: pulumi.Output<string | undefined>;
    /**
     * A standard MIME type describing the format of the object data.
     */
    public readonly contentType!: pulumi.Output<string>;
    /**
     * The ETag generated for the object (an MD5 sum of the object content).
     */
    public readonly etag!: pulumi.Output<string>;
    /**
     * The name of the object once it is in the bucket.
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * The path to the source file being uploaded to the bucket.
     */
    public readonly source!: pulumi.Output<string | undefined>;
    /**
     * Object storage type, Available values include `STANDARD`, `STANDARD_IA` and `ARCHIVE`.
     */
    public readonly storageClass!: pulumi.Output<string>;
    /**
     * Tag of the object.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a BucketObject resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BucketObjectArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BucketObjectArgs | BucketObjectState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BucketObjectState | undefined;
            resourceInputs["acl"] = state ? state.acl : undefined;
            resourceInputs["bucket"] = state ? state.bucket : undefined;
            resourceInputs["cacheControl"] = state ? state.cacheControl : undefined;
            resourceInputs["content"] = state ? state.content : undefined;
            resourceInputs["contentDisposition"] = state ? state.contentDisposition : undefined;
            resourceInputs["contentEncoding"] = state ? state.contentEncoding : undefined;
            resourceInputs["contentType"] = state ? state.contentType : undefined;
            resourceInputs["etag"] = state ? state.etag : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
            resourceInputs["storageClass"] = state ? state.storageClass : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as BucketObjectArgs | undefined;
            if ((!args || args.bucket === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bucket'");
            }
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            resourceInputs["acl"] = args ? args.acl : undefined;
            resourceInputs["bucket"] = args ? args.bucket : undefined;
            resourceInputs["cacheControl"] = args ? args.cacheControl : undefined;
            resourceInputs["content"] = args ? args.content : undefined;
            resourceInputs["contentDisposition"] = args ? args.contentDisposition : undefined;
            resourceInputs["contentEncoding"] = args ? args.contentEncoding : undefined;
            resourceInputs["contentType"] = args ? args.contentType : undefined;
            resourceInputs["etag"] = args ? args.etag : undefined;
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["storageClass"] = args ? args.storageClass : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(BucketObject.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BucketObject resources.
 */
export interface BucketObjectState {
    /**
     * The canned ACL to apply. Available values include `private`, `public-read`, and `public-read-write`. Defaults to `private`.
     */
    acl?: pulumi.Input<string>;
    /**
     * The name of a bucket to use. Bucket format should be [custom name]-[appid], for example `mycos-1258798060`.
     */
    bucket?: pulumi.Input<string>;
    /**
     * Specifies caching behavior along the request/reply chain. For further details, RFC2616 can be referred.
     */
    cacheControl?: pulumi.Input<string>;
    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
     */
    content?: pulumi.Input<string>;
    /**
     * Specifies presentational information for the object.
     */
    contentDisposition?: pulumi.Input<string>;
    /**
     * Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
     */
    contentEncoding?: pulumi.Input<string>;
    /**
     * A standard MIME type describing the format of the object data.
     */
    contentType?: pulumi.Input<string>;
    /**
     * The ETag generated for the object (an MD5 sum of the object content).
     */
    etag?: pulumi.Input<string>;
    /**
     * The name of the object once it is in the bucket.
     */
    key?: pulumi.Input<string>;
    /**
     * The path to the source file being uploaded to the bucket.
     */
    source?: pulumi.Input<string>;
    /**
     * Object storage type, Available values include `STANDARD`, `STANDARD_IA` and `ARCHIVE`.
     */
    storageClass?: pulumi.Input<string>;
    /**
     * Tag of the object.
     */
    tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a BucketObject resource.
 */
export interface BucketObjectArgs {
    /**
     * The canned ACL to apply. Available values include `private`, `public-read`, and `public-read-write`. Defaults to `private`.
     */
    acl?: pulumi.Input<string>;
    /**
     * The name of a bucket to use. Bucket format should be [custom name]-[appid], for example `mycos-1258798060`.
     */
    bucket: pulumi.Input<string>;
    /**
     * Specifies caching behavior along the request/reply chain. For further details, RFC2616 can be referred.
     */
    cacheControl?: pulumi.Input<string>;
    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
     */
    content?: pulumi.Input<string>;
    /**
     * Specifies presentational information for the object.
     */
    contentDisposition?: pulumi.Input<string>;
    /**
     * Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
     */
    contentEncoding?: pulumi.Input<string>;
    /**
     * A standard MIME type describing the format of the object data.
     */
    contentType?: pulumi.Input<string>;
    /**
     * The ETag generated for the object (an MD5 sum of the object content).
     */
    etag?: pulumi.Input<string>;
    /**
     * The name of the object once it is in the bucket.
     */
    key: pulumi.Input<string>;
    /**
     * The path to the source file being uploaded to the bucket.
     */
    source?: pulumi.Input<string>;
    /**
     * Object storage type, Available values include `STANDARD`, `STANDARD_IA` and `ARCHIVE`.
     */
    storageClass?: pulumi.Input<string>;
    /**
     * Tag of the object.
     */
    tags?: pulumi.Input<{[key: string]: any}>;
}
