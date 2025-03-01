// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Tcaplus
{
    /// <summary>
    /// Use this resource to create TcaplusDB table.
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
    ///         var test = new Tencentcloud.Tcaplus.Cluster("test", new Tencentcloud.Tcaplus.ClusterArgs
    ///         {
    ///             IdlType = "PROTO",
    ///             ClusterName = "tf_tcaplus_cluster_test",
    ///             VpcId = "vpc-7k6gzox6",
    ///             SubnetId = "subnet-akwgvfa3",
    ///             Password = "1qaA2k1wgvfa3ZZZ",
    ///             OldPasswordExpireLast = 3600,
    ///         });
    ///         var tablegroup = new Tencentcloud.Tcaplus.Tablegroup("tablegroup", new Tencentcloud.Tcaplus.TablegroupArgs
    ///         {
    ///             ClusterId = test.Id,
    ///             TablegroupName = "tf_test_group_name",
    ///         });
    ///         var main = new Tencentcloud.Tcaplus.Idl("main", new Tencentcloud.Tcaplus.IdlArgs
    ///         {
    ///             ClusterId = test.Id,
    ///             TablegroupId = tablegroup.Id,
    ///             FileName = "tf_idl_test_2",
    ///             FileType = "PROTO",
    ///             FileExtType = "proto",
    ///             FileContent = @"    syntax = ""proto2"";
    ///     package myTcaplusTable;
    ///     import ""tcaplusservice.optionv1.proto"";
    ///     message tb_online {
    ///        option(tcaplusservice.tcaplus_primary_key) = ""uin,name,region"";
    ///         required int64 uin = 1;
    ///         required string name = 2;
    ///         required int32 region = 3;
    ///         required int32 gamesvrid = 4;
    ///         optional int32 logintime = 5 [default = 1];
    ///         repeated int64 lockid = 6 [packed = true];
    ///         optional bool is_available = 7 [default = false];
    ///         optional pay_info pay = 8;
    ///     }
    /// 
    ///     message pay_info {
    ///         required int64 pay_id = 1;
    ///         optional uint64 total_money = 2;
    ///         optional uint64 pay_times = 3;
    ///         optional pay_auth_info auth = 4;
    ///         message pay_auth_info {
    ///             required string pay_keys = 1;
    ///             optional int64 update_time = 2;
    ///         }
    ///     }
    /// ",
    ///         });
    ///         var table = new Tencentcloud.Tcaplus.Table("table", new Tencentcloud.Tcaplus.TableArgs
    ///         {
    ///             ClusterId = test.Id,
    ///             TablegroupId = tablegroup.Id,
    ///             TableName = "tb_online",
    ///             TableType = "GENERIC",
    ///             Description = "test",
    ///             IdlId = main.Id,
    ///             TableIdlType = "PROTO",
    ///             ReservedReadCu = 1000,
    ///             ReservedWriteCu = 20,
    ///             ReservedVolume = 1,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Tcaplus/table:Table")]
    public partial class Table : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of the TcaplusDB cluster to which the table belongs.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// Create time of the TcaplusDB table.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Description of the TcaplusDB table.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Error messages for creating TcaplusDB table.
        /// </summary>
        [Output("error")]
        public Output<string> Error { get; private set; } = null!;

        /// <summary>
        /// ID of the IDL File.
        /// </summary>
        [Output("idlId")]
        public Output<string> IdlId { get; private set; } = null!;

        /// <summary>
        /// Reserved read capacity units of the TcaplusDB table.
        /// </summary>
        [Output("reservedReadCu")]
        public Output<int> ReservedReadCu { get; private set; } = null!;

        /// <summary>
        /// Reserved storage capacity of the TcaplusDB table (unit: GB).
        /// </summary>
        [Output("reservedVolume")]
        public Output<int> ReservedVolume { get; private set; } = null!;

        /// <summary>
        /// Reserved write capacity units of the TcaplusDB table.
        /// </summary>
        [Output("reservedWriteCu")]
        public Output<int> ReservedWriteCu { get; private set; } = null!;

        /// <summary>
        /// Status of the TcaplusDB table.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// IDL type of the TcaplusDB table. Valid values: `PROTO` and `TDR`.
        /// </summary>
        [Output("tableIdlType")]
        public Output<string> TableIdlType { get; private set; } = null!;

        /// <summary>
        /// Name of the TcaplusDB table.
        /// </summary>
        [Output("tableName")]
        public Output<string> TableName { get; private set; } = null!;

        /// <summary>
        /// Size of the TcaplusDB table.
        /// </summary>
        [Output("tableSize")]
        public Output<int> TableSize { get; private set; } = null!;

        /// <summary>
        /// Type of the TcaplusDB table. Valid values are `GENERIC` and `LIST`.
        /// </summary>
        [Output("tableType")]
        public Output<string> TableType { get; private set; } = null!;

        /// <summary>
        /// ID of the table group to which the table belongs.
        /// </summary>
        [Output("tablegroupId")]
        public Output<string> TablegroupId { get; private set; } = null!;


        /// <summary>
        /// Create a Table resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Table(string name, TableArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Tcaplus/table:Table", name, args ?? new TableArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Table(string name, Input<string> id, TableState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Tcaplus/table:Table", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Table resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Table Get(string name, Input<string> id, TableState? state = null, CustomResourceOptions? options = null)
        {
            return new Table(name, id, state, options);
        }
    }

    public sealed class TableArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the TcaplusDB cluster to which the table belongs.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Description of the TcaplusDB table.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// ID of the IDL File.
        /// </summary>
        [Input("idlId", required: true)]
        public Input<string> IdlId { get; set; } = null!;

        /// <summary>
        /// Reserved read capacity units of the TcaplusDB table.
        /// </summary>
        [Input("reservedReadCu", required: true)]
        public Input<int> ReservedReadCu { get; set; } = null!;

        /// <summary>
        /// Reserved storage capacity of the TcaplusDB table (unit: GB).
        /// </summary>
        [Input("reservedVolume", required: true)]
        public Input<int> ReservedVolume { get; set; } = null!;

        /// <summary>
        /// Reserved write capacity units of the TcaplusDB table.
        /// </summary>
        [Input("reservedWriteCu", required: true)]
        public Input<int> ReservedWriteCu { get; set; } = null!;

        /// <summary>
        /// IDL type of the TcaplusDB table. Valid values: `PROTO` and `TDR`.
        /// </summary>
        [Input("tableIdlType", required: true)]
        public Input<string> TableIdlType { get; set; } = null!;

        /// <summary>
        /// Name of the TcaplusDB table.
        /// </summary>
        [Input("tableName", required: true)]
        public Input<string> TableName { get; set; } = null!;

        /// <summary>
        /// Type of the TcaplusDB table. Valid values are `GENERIC` and `LIST`.
        /// </summary>
        [Input("tableType", required: true)]
        public Input<string> TableType { get; set; } = null!;

        /// <summary>
        /// ID of the table group to which the table belongs.
        /// </summary>
        [Input("tablegroupId", required: true)]
        public Input<string> TablegroupId { get; set; } = null!;

        public TableArgs()
        {
        }
    }

    public sealed class TableState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the TcaplusDB cluster to which the table belongs.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// Create time of the TcaplusDB table.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// Description of the TcaplusDB table.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Error messages for creating TcaplusDB table.
        /// </summary>
        [Input("error")]
        public Input<string>? Error { get; set; }

        /// <summary>
        /// ID of the IDL File.
        /// </summary>
        [Input("idlId")]
        public Input<string>? IdlId { get; set; }

        /// <summary>
        /// Reserved read capacity units of the TcaplusDB table.
        /// </summary>
        [Input("reservedReadCu")]
        public Input<int>? ReservedReadCu { get; set; }

        /// <summary>
        /// Reserved storage capacity of the TcaplusDB table (unit: GB).
        /// </summary>
        [Input("reservedVolume")]
        public Input<int>? ReservedVolume { get; set; }

        /// <summary>
        /// Reserved write capacity units of the TcaplusDB table.
        /// </summary>
        [Input("reservedWriteCu")]
        public Input<int>? ReservedWriteCu { get; set; }

        /// <summary>
        /// Status of the TcaplusDB table.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// IDL type of the TcaplusDB table. Valid values: `PROTO` and `TDR`.
        /// </summary>
        [Input("tableIdlType")]
        public Input<string>? TableIdlType { get; set; }

        /// <summary>
        /// Name of the TcaplusDB table.
        /// </summary>
        [Input("tableName")]
        public Input<string>? TableName { get; set; }

        /// <summary>
        /// Size of the TcaplusDB table.
        /// </summary>
        [Input("tableSize")]
        public Input<int>? TableSize { get; set; }

        /// <summary>
        /// Type of the TcaplusDB table. Valid values are `GENERIC` and `LIST`.
        /// </summary>
        [Input("tableType")]
        public Input<string>? TableType { get; set; }

        /// <summary>
        /// ID of the table group to which the table belongs.
        /// </summary>
        [Input("tablegroupId")]
        public Input<string>? TablegroupId { get; set; }

        public TableState()
        {
        }
    }
}
