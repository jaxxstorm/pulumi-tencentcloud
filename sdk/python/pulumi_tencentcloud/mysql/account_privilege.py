# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AccountPrivilegeArgs', 'AccountPrivilege']

@pulumi.input_type
class AccountPrivilegeArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 database_names: pulumi.Input[Sequence[pulumi.Input[str]]],
                 mysql_id: pulumi.Input[str],
                 account_host: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AccountPrivilege resource.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_names: List of specified database name.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: Database permissions. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`,
               `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER
               ROUTINE`, `EVENT` and `TRIGGER``.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "database_names", database_names)
        pulumi.set(__self__, "mysql_id", mysql_id)
        if account_host is not None:
            pulumi.set(__self__, "account_host", account_host)
        if privileges is not None:
            pulumi.set(__self__, "privileges", privileges)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="databaseNames")
    def database_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of specified database name.
        """
        return pulumi.get(self, "database_names")

    @database_names.setter
    def database_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "database_names", value)

    @property
    @pulumi.getter(name="mysqlId")
    def mysql_id(self) -> pulumi.Input[str]:
        """
        Instance ID.
        """
        return pulumi.get(self, "mysql_id")

    @mysql_id.setter
    def mysql_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "mysql_id", value)

    @property
    @pulumi.getter(name="accountHost")
    def account_host(self) -> Optional[pulumi.Input[str]]:
        """
        Account host, default is `%`.
        """
        return pulumi.get(self, "account_host")

    @account_host.setter
    def account_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_host", value)

    @property
    @pulumi.getter
    def privileges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Database permissions. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`,
        `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER
        ROUTINE`, `EVENT` and `TRIGGER``.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "privileges", value)


@pulumi.input_type
class _AccountPrivilegeState:
    def __init__(__self__, *,
                 account_host: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 database_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mysql_id: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering AccountPrivilege resources.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_names: List of specified database name.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: Database permissions. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`,
               `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER
               ROUTINE`, `EVENT` and `TRIGGER``.
        """
        if account_host is not None:
            pulumi.set(__self__, "account_host", account_host)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if database_names is not None:
            pulumi.set(__self__, "database_names", database_names)
        if mysql_id is not None:
            pulumi.set(__self__, "mysql_id", mysql_id)
        if privileges is not None:
            pulumi.set(__self__, "privileges", privileges)

    @property
    @pulumi.getter(name="accountHost")
    def account_host(self) -> Optional[pulumi.Input[str]]:
        """
        Account host, default is `%`.
        """
        return pulumi.get(self, "account_host")

    @account_host.setter
    def account_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_host", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="databaseNames")
    def database_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of specified database name.
        """
        return pulumi.get(self, "database_names")

    @database_names.setter
    def database_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "database_names", value)

    @property
    @pulumi.getter(name="mysqlId")
    def mysql_id(self) -> Optional[pulumi.Input[str]]:
        """
        Instance ID.
        """
        return pulumi.get(self, "mysql_id")

    @mysql_id.setter
    def mysql_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mysql_id", value)

    @property
    @pulumi.getter
    def privileges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Database permissions. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`,
        `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER
        ROUTINE`, `EVENT` and `TRIGGER``.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "privileges", value)


class AccountPrivilege(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_host: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 database_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mysql_id: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a AccountPrivilege resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_names: List of specified database name.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: Database permissions. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`,
               `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER
               ROUTINE`, `EVENT` and `TRIGGER``.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountPrivilegeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AccountPrivilege resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AccountPrivilegeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountPrivilegeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_host: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 database_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mysql_id: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountPrivilegeArgs.__new__(AccountPrivilegeArgs)

            __props__.__dict__["account_host"] = account_host
            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if database_names is None and not opts.urn:
                raise TypeError("Missing required property 'database_names'")
            __props__.__dict__["database_names"] = database_names
            if mysql_id is None and not opts.urn:
                raise TypeError("Missing required property 'mysql_id'")
            __props__.__dict__["mysql_id"] = mysql_id
            __props__.__dict__["privileges"] = privileges
        super(AccountPrivilege, __self__).__init__(
            'tencentcloud:Mysql/accountPrivilege:AccountPrivilege',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_host: Optional[pulumi.Input[str]] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            database_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            mysql_id: Optional[pulumi.Input[str]] = None,
            privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AccountPrivilege':
        """
        Get an existing AccountPrivilege resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] database_names: List of specified database name.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: Database permissions. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`,
               `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER
               ROUTINE`, `EVENT` and `TRIGGER``.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountPrivilegeState.__new__(_AccountPrivilegeState)

        __props__.__dict__["account_host"] = account_host
        __props__.__dict__["account_name"] = account_name
        __props__.__dict__["database_names"] = database_names
        __props__.__dict__["mysql_id"] = mysql_id
        __props__.__dict__["privileges"] = privileges
        return AccountPrivilege(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountHost")
    def account_host(self) -> pulumi.Output[Optional[str]]:
        """
        Account host, default is `%`.
        """
        return pulumi.get(self, "account_host")

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="databaseNames")
    def database_names(self) -> pulumi.Output[Sequence[str]]:
        """
        List of specified database name.
        """
        return pulumi.get(self, "database_names")

    @property
    @pulumi.getter(name="mysqlId")
    def mysql_id(self) -> pulumi.Output[str]:
        """
        Instance ID.
        """
        return pulumi.get(self, "mysql_id")

    @property
    @pulumi.getter
    def privileges(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Database permissions. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`,
        `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER
        ROUTINE`, `EVENT` and `TRIGGER``.
        """
        return pulumi.get(self, "privileges")

