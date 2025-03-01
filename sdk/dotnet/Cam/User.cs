// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cam
{
    /// <summary>
    /// Provides a resource to manage CAM user.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Tencentcloud = Pulumi.Tencentcloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var foo = new Tencentcloud.Cam.User("foo", new Tencentcloud.Cam.UserArgs
    ///         {
    ///             ConsoleLogin = true,
    ///             CountryCode = "86",
    ///             Email = "hello@test.com",
    ///             ForceDelete = true,
    ///             NeedResetPassword = true,
    ///             Password = "Gail@1234",
    ///             PhoneNum = "12345678910",
    ///             Remark = "test",
    ///             Tags = 
    ///             {
    ///                 { "test", "tf-cam-user" },
    ///             },
    ///             UseApi = true,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// CAM user can be imported using the user name, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Cam/user:User foo cam-user-test
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Cam/user:User")]
    public partial class User : Pulumi.CustomResource
    {
        /// <summary>
        /// Indicate whether the CAM user can login to the web console or not.
        /// </summary>
        [Output("consoleLogin")]
        public Output<bool?> ConsoleLogin { get; private set; } = null!;

        /// <summary>
        /// Country code of the phone number, for example: '86'.
        /// </summary>
        [Output("countryCode")]
        public Output<string> CountryCode { get; private set; } = null!;

        /// <summary>
        /// Email of the CAM user.
        /// </summary>
        [Output("email")]
        public Output<string?> Email { get; private set; } = null!;

        /// <summary>
        /// Indicate whether to force deletes the CAM user. If set false, the API secret key will be checked and failed when exists; otherwise the user will be deleted directly. Default is false.
        /// </summary>
        [Output("forceDelete")]
        public Output<bool?> ForceDelete { get; private set; } = null!;

        /// <summary>
        /// Name of the CAM user.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Indicate whether the CAM user need to reset the password when first logins.
        /// </summary>
        [Output("needResetPassword")]
        public Output<bool?> NeedResetPassword { get; private set; } = null!;

        /// <summary>
        /// The password of the CAM user. Password should be at least 8 characters and no more than 32 characters, includes uppercase letters, lowercase letters, numbers and special characters. Only required when `console_login` is true. If not set, a random password will be automatically generated.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// Phone number of the CAM user.
        /// </summary>
        [Output("phoneNum")]
        public Output<string?> PhoneNum { get; private set; } = null!;

        /// <summary>
        /// Remark of the CAM user.
        /// </summary>
        [Output("remark")]
        public Output<string?> Remark { get; private set; } = null!;

        /// <summary>
        /// Secret ID of the CAM user.
        /// </summary>
        [Output("secretId")]
        public Output<string> SecretId { get; private set; } = null!;

        /// <summary>
        /// Secret key of the CAM user.
        /// </summary>
        [Output("secretKey")]
        public Output<string> SecretKey { get; private set; } = null!;

        /// <summary>
        /// A list of tags used to associate different resources.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// ID of the CAM user.
        /// </summary>
        [Output("uid")]
        public Output<int> Uid { get; private set; } = null!;

        /// <summary>
        /// Uin of the CAM User.
        /// </summary>
        [Output("uin")]
        public Output<int> Uin { get; private set; } = null!;

        /// <summary>
        /// Indicate whether to generate the API secret key or not.
        /// </summary>
        [Output("useApi")]
        public Output<bool?> UseApi { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs? args = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Cam/user:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private User(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Cam/user:User", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing User resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static User Get(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
        {
            return new User(name, id, state, options);
        }
    }

    public sealed class UserArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicate whether the CAM user can login to the web console or not.
        /// </summary>
        [Input("consoleLogin")]
        public Input<bool>? ConsoleLogin { get; set; }

        /// <summary>
        /// Country code of the phone number, for example: '86'.
        /// </summary>
        [Input("countryCode")]
        public Input<string>? CountryCode { get; set; }

        /// <summary>
        /// Email of the CAM user.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Indicate whether to force deletes the CAM user. If set false, the API secret key will be checked and failed when exists; otherwise the user will be deleted directly. Default is false.
        /// </summary>
        [Input("forceDelete")]
        public Input<bool>? ForceDelete { get; set; }

        /// <summary>
        /// Name of the CAM user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Indicate whether the CAM user need to reset the password when first logins.
        /// </summary>
        [Input("needResetPassword")]
        public Input<bool>? NeedResetPassword { get; set; }

        /// <summary>
        /// The password of the CAM user. Password should be at least 8 characters and no more than 32 characters, includes uppercase letters, lowercase letters, numbers and special characters. Only required when `console_login` is true. If not set, a random password will be automatically generated.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// Phone number of the CAM user.
        /// </summary>
        [Input("phoneNum")]
        public Input<string>? PhoneNum { get; set; }

        /// <summary>
        /// Remark of the CAM user.
        /// </summary>
        [Input("remark")]
        public Input<string>? Remark { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A list of tags used to associate different resources.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Indicate whether to generate the API secret key or not.
        /// </summary>
        [Input("useApi")]
        public Input<bool>? UseApi { get; set; }

        public UserArgs()
        {
        }
    }

    public sealed class UserState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicate whether the CAM user can login to the web console or not.
        /// </summary>
        [Input("consoleLogin")]
        public Input<bool>? ConsoleLogin { get; set; }

        /// <summary>
        /// Country code of the phone number, for example: '86'.
        /// </summary>
        [Input("countryCode")]
        public Input<string>? CountryCode { get; set; }

        /// <summary>
        /// Email of the CAM user.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Indicate whether to force deletes the CAM user. If set false, the API secret key will be checked and failed when exists; otherwise the user will be deleted directly. Default is false.
        /// </summary>
        [Input("forceDelete")]
        public Input<bool>? ForceDelete { get; set; }

        /// <summary>
        /// Name of the CAM user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Indicate whether the CAM user need to reset the password when first logins.
        /// </summary>
        [Input("needResetPassword")]
        public Input<bool>? NeedResetPassword { get; set; }

        /// <summary>
        /// The password of the CAM user. Password should be at least 8 characters and no more than 32 characters, includes uppercase letters, lowercase letters, numbers and special characters. Only required when `console_login` is true. If not set, a random password will be automatically generated.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// Phone number of the CAM user.
        /// </summary>
        [Input("phoneNum")]
        public Input<string>? PhoneNum { get; set; }

        /// <summary>
        /// Remark of the CAM user.
        /// </summary>
        [Input("remark")]
        public Input<string>? Remark { get; set; }

        /// <summary>
        /// Secret ID of the CAM user.
        /// </summary>
        [Input("secretId")]
        public Input<string>? SecretId { get; set; }

        /// <summary>
        /// Secret key of the CAM user.
        /// </summary>
        [Input("secretKey")]
        public Input<string>? SecretKey { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A list of tags used to associate different resources.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// ID of the CAM user.
        /// </summary>
        [Input("uid")]
        public Input<int>? Uid { get; set; }

        /// <summary>
        /// Uin of the CAM User.
        /// </summary>
        [Input("uin")]
        public Input<int>? Uin { get; set; }

        /// <summary>
        /// Indicate whether to generate the API secret key or not.
        /// </summary>
        [Input("useApi")]
        public Input<bool>? UseApi { get; set; }

        public UserState()
        {
        }
    }
}
