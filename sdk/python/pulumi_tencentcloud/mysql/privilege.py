# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PrivilegeArgs', 'Privilege']

@pulumi.input_type
class PrivilegeArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 globals: pulumi.Input[Sequence[pulumi.Input[str]]],
                 mysql_id: pulumi.Input[str],
                 account_host: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]]] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]]] = None):
        """
        The set of arguments for constructing a Privilege resource.
        :param pulumi.Input[str] account_name: Account name.the forbidden value is:root,mysql.sys,tencentroot.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] globals: Global privileges. available values for Privileges:ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TEMPORARY
               TABLES,CREATE USER,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE,INDEX,INSERT,LOCK TABLES,PROCESS,REFERENCES,RELOAD,REPLICATION
               CLIENT,REPLICATION SLAVE,SELECT,SHOW DATABASES,SHOW VIEW,TRIGGER,UPDATE.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]] columns: Column privileges list.
        :param pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]] databases: Database privileges list.
        :param pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]] tables: Table privileges list.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "globals", globals)
        pulumi.set(__self__, "mysql_id", mysql_id)
        if account_host is not None:
            pulumi.set(__self__, "account_host", account_host)
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if databases is not None:
            pulumi.set(__self__, "databases", databases)
        if tables is not None:
            pulumi.set(__self__, "tables", tables)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Account name.the forbidden value is:root,mysql.sys,tencentroot.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def globals(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Global privileges. available values for Privileges:ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TEMPORARY
        TABLES,CREATE USER,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE,INDEX,INSERT,LOCK TABLES,PROCESS,REFERENCES,RELOAD,REPLICATION
        CLIENT,REPLICATION SLAVE,SELECT,SHOW DATABASES,SHOW VIEW,TRIGGER,UPDATE.
        """
        return pulumi.get(self, "globals")

    @globals.setter
    def globals(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "globals", value)

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
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]]]:
        """
        Column privileges list.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]]]:
        """
        Database privileges list.
        """
        return pulumi.get(self, "databases")

    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]]]):
        pulumi.set(self, "databases", value)

    @property
    @pulumi.getter
    def tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]]]:
        """
        Table privileges list.
        """
        return pulumi.get(self, "tables")

    @tables.setter
    def tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]]]):
        pulumi.set(self, "tables", value)


@pulumi.input_type
class _PrivilegeState:
    def __init__(__self__, *,
                 account_host: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]]] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]]] = None,
                 globals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mysql_id: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]]] = None):
        """
        Input properties used for looking up and filtering Privilege resources.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[str] account_name: Account name.the forbidden value is:root,mysql.sys,tencentroot.
        :param pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]] columns: Column privileges list.
        :param pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]] databases: Database privileges list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] globals: Global privileges. available values for Privileges:ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TEMPORARY
               TABLES,CREATE USER,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE,INDEX,INSERT,LOCK TABLES,PROCESS,REFERENCES,RELOAD,REPLICATION
               CLIENT,REPLICATION SLAVE,SELECT,SHOW DATABASES,SHOW VIEW,TRIGGER,UPDATE.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]] tables: Table privileges list.
        """
        if account_host is not None:
            pulumi.set(__self__, "account_host", account_host)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if databases is not None:
            pulumi.set(__self__, "databases", databases)
        if globals is not None:
            pulumi.set(__self__, "globals", globals)
        if mysql_id is not None:
            pulumi.set(__self__, "mysql_id", mysql_id)
        if tables is not None:
            pulumi.set(__self__, "tables", tables)

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
        Account name.the forbidden value is:root,mysql.sys,tencentroot.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]]]:
        """
        Column privileges list.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeColumnArgs']]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]]]:
        """
        Database privileges list.
        """
        return pulumi.get(self, "databases")

    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeDatabaseArgs']]]]):
        pulumi.set(self, "databases", value)

    @property
    @pulumi.getter
    def globals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Global privileges. available values for Privileges:ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TEMPORARY
        TABLES,CREATE USER,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE,INDEX,INSERT,LOCK TABLES,PROCESS,REFERENCES,RELOAD,REPLICATION
        CLIENT,REPLICATION SLAVE,SELECT,SHOW DATABASES,SHOW VIEW,TRIGGER,UPDATE.
        """
        return pulumi.get(self, "globals")

    @globals.setter
    def globals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "globals", value)

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
    def tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]]]:
        """
        Table privileges list.
        """
        return pulumi.get(self, "tables")

    @tables.setter
    def tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivilegeTableArgs']]]]):
        pulumi.set(self, "tables", value)


class Privilege(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_host: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeColumnArgs']]]]] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeDatabaseArgs']]]]] = None,
                 globals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mysql_id: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeTableArgs']]]]] = None,
                 __props__=None):
        """
        Create a Privilege resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[str] account_name: Account name.the forbidden value is:root,mysql.sys,tencentroot.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeColumnArgs']]]] columns: Column privileges list.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeDatabaseArgs']]]] databases: Database privileges list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] globals: Global privileges. available values for Privileges:ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TEMPORARY
               TABLES,CREATE USER,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE,INDEX,INSERT,LOCK TABLES,PROCESS,REFERENCES,RELOAD,REPLICATION
               CLIENT,REPLICATION SLAVE,SELECT,SHOW DATABASES,SHOW VIEW,TRIGGER,UPDATE.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeTableArgs']]]] tables: Table privileges list.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivilegeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Privilege resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PrivilegeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivilegeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_host: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeColumnArgs']]]]] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeDatabaseArgs']]]]] = None,
                 globals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mysql_id: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeTableArgs']]]]] = None,
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
            __props__ = PrivilegeArgs.__new__(PrivilegeArgs)

            __props__.__dict__["account_host"] = account_host
            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["columns"] = columns
            __props__.__dict__["databases"] = databases
            if globals is None and not opts.urn:
                raise TypeError("Missing required property 'globals'")
            __props__.__dict__["globals"] = globals
            if mysql_id is None and not opts.urn:
                raise TypeError("Missing required property 'mysql_id'")
            __props__.__dict__["mysql_id"] = mysql_id
            __props__.__dict__["tables"] = tables
        super(Privilege, __self__).__init__(
            'tencentcloud:Mysql/privilege:Privilege',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_host: Optional[pulumi.Input[str]] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeColumnArgs']]]]] = None,
            databases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeDatabaseArgs']]]]] = None,
            globals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            mysql_id: Optional[pulumi.Input[str]] = None,
            tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeTableArgs']]]]] = None) -> 'Privilege':
        """
        Get an existing Privilege resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_host: Account host, default is `%`.
        :param pulumi.Input[str] account_name: Account name.the forbidden value is:root,mysql.sys,tencentroot.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeColumnArgs']]]] columns: Column privileges list.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeDatabaseArgs']]]] databases: Database privileges list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] globals: Global privileges. available values for Privileges:ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TEMPORARY
               TABLES,CREATE USER,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE,INDEX,INSERT,LOCK TABLES,PROCESS,REFERENCES,RELOAD,REPLICATION
               CLIENT,REPLICATION SLAVE,SELECT,SHOW DATABASES,SHOW VIEW,TRIGGER,UPDATE.
        :param pulumi.Input[str] mysql_id: Instance ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivilegeTableArgs']]]] tables: Table privileges list.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivilegeState.__new__(_PrivilegeState)

        __props__.__dict__["account_host"] = account_host
        __props__.__dict__["account_name"] = account_name
        __props__.__dict__["columns"] = columns
        __props__.__dict__["databases"] = databases
        __props__.__dict__["globals"] = globals
        __props__.__dict__["mysql_id"] = mysql_id
        __props__.__dict__["tables"] = tables
        return Privilege(resource_name, opts=opts, __props__=__props__)

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
        Account name.the forbidden value is:root,mysql.sys,tencentroot.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter
    def columns(self) -> pulumi.Output[Optional[Sequence['outputs.PrivilegeColumn']]]:
        """
        Column privileges list.
        """
        return pulumi.get(self, "columns")

    @property
    @pulumi.getter
    def databases(self) -> pulumi.Output[Optional[Sequence['outputs.PrivilegeDatabase']]]:
        """
        Database privileges list.
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def globals(self) -> pulumi.Output[Sequence[str]]:
        """
        Global privileges. available values for Privileges:ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TEMPORARY
        TABLES,CREATE USER,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE,INDEX,INSERT,LOCK TABLES,PROCESS,REFERENCES,RELOAD,REPLICATION
        CLIENT,REPLICATION SLAVE,SELECT,SHOW DATABASES,SHOW VIEW,TRIGGER,UPDATE.
        """
        return pulumi.get(self, "globals")

    @property
    @pulumi.getter(name="mysqlId")
    def mysql_id(self) -> pulumi.Output[str]:
        """
        Instance ID.
        """
        return pulumi.get(self, "mysql_id")

    @property
    @pulumi.getter
    def tables(self) -> pulumi.Output[Optional[Sequence['outputs.PrivilegeTable']]]:
        """
        Table privileges list.
        """
        return pulumi.get(self, "tables")

