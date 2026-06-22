---
title: "Connect to dbt Core"
source: "https://docs.databricks.com/en/partners/prep/dbt.html"
author: "databricks.com"
published: 2023-10-31
created: 2023-11-16
description: "Learn how to connect your Databricks workspace to dbt Core, an open-source"
tags:
  - to-process
  - data-engineering
---

This article covers dbt Core, a version of dbt for your local development machine that interacts with Databricks SQL warehouses and Databricks clusters within your Databricks workspaces. To use the hosted version of dbt (called *dbt Cloud*) instead, or to use Partner Connect to quickly create a SQL warehouse within your workspace and then connect it to dbt Cloud, see [Connect to dbt Cloud](https://docs.databricks.com/en/partners/prep/dbt-cloud.html).


dbt (data build tool) is a development environment that enables data analysts and data engineers to transform data by simply writing select statements. dbt handles turning these select statements into tables and views. dbt compiles your code into raw SQL and then runs that code on the specified database in Databricks. dbt supports collaborative coding patterns and best practices such as version control, documentation, modularity, and more.


dbt does not extract or load data. dbt focuses on the transformation step only, using a “transform after load” architecture. dbt assumes that you already have a copy of your data in your database.


This article focuses on using dbt Core. dbt Core enables you to write dbt code in the text editor or IDE of your choice on your local development machine and then run dbt from the command line. dbt Core includes the dbt Command Line Interface (CLI). The [dbt CLI](https://docs.getdbt.com/dbt-cli/cli-overview) is free to use and [open source](https://github.com/dbt-labs/dbt).


A hosted version of dbt called dbt Cloud is also available. dbt Cloud comes equipped with turnkey support for scheduling jobs, CI/CD, serving documentation, monitoring and alerting, and an integrated development environment (IDE). For more information, see [Connect to dbt Cloud](https://docs.databricks.com/en/partners/prep/dbt-cloud.html). The dbt Cloud Developer plan provides one free developer seat; Team and Enterprise paid plans are also available. For more information, see [dbt Pricing](https://www.getdbt.com/pricing/) on the dbt website.


Because dbt Core and dbt Cloud can use hosted git repositories (for example, on GitHub, GitLab or BitBucket), you can use dbt Core to create a dbt project and then make it available to your dbt Cloud users. For more information, see [Creating a dbt project](https://docs.getdbt.com/docs/building-a-dbt-project/projects#creating-a-dbt-project) and [Using an existing project](https://docs.getdbt.com/docs/building-a-dbt-project/projects#using-an-existing-project) on the dbt website.


For a general overview of dbt, watch the following YouTube video (26 minutes).


Some content could not be imported from the original document. [View content ↗](https://www.youtube.com/embed/zoHoIGE6tPc?rel=0) 


## Requirements


Before you install dbt Core, you must install the following on your local development machine:


* A utility for creating Python virtual environments (such as [pipenv](https://docs.python-guide.org/dev/virtualenvs/))


You also need one of the following to authenticate:


* dbt enabled as an OAuth application in your account (recommended). This is enabled by default.

 (Optional) To use a custom IdP for dbt login, see [Set up SSO in your Databricks account console](https://docs.databricks.com/en/administration-guide/account-settings-e2/single-sign-on/index.html).
* A personal access token

 As a security best practice when you authenticate with automated tools, systems, scripts, and apps, Databricks recommends that you use OAuth tokens or personal access tokens belonging to [service principals](https://docs.databricks.com/en/administration-guide/users-groups/service-principals.html) instead of workspace users. To create tokens for service principals, see [Manage tokens for a service principal](https://docs.databricks.com/en/administration-guide/users-groups/service-principals.html#personal-access-tokens).


## Step 1: Create and activate a Python virtual environment


In this step, you use `pipenv` to create a *[Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/)*. We recommend using a Python virtual environment as it isolates package versions and code dependencies to that specific environment, regardless of the package versions and code dependencies within other environments. This helps reduce unexpected package version mismatches and code dependency collisions.


1. In this empty directory, create a file named `Pipfile` with the following content. This *[Pipfile](https://realpython.com/pipenv-guide/#the-pipfile)* instructs `pipenv` to use Python version 3.8.6. If you use a different version, replace `3.8.6` with your version number.

 
```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
dbt-databricks = "*"

[requires]
python_version = "3.8.6"

```
 The preceding line `dbt-databricks = "*"` instructs `pipenv` to use the latest version of the `dbt-databricks` package. In production scenarios, you should replace `*` with the specific version of the package that you want to use. See [dbt-databricks Release history](https://pypi.org/project/dbt-databricks/#history) on the Python Package Index (PyPI) website.
2. Create a Python virtual environment in this directory by running `pipenv` and specifying the Python version to use. This command specifies Python version 3.8.6. If you use a different version, replace `3.8.6` with your version number:

 
```
pipenv --python 3.8.6

```
3. Install the dbt Databricks adapter by running `pipenv` with the `install` option. This installs the packages in your `Pipfile`, which includes the dbt Databricks adapter package, `dbt-databricks`, from PyPI. The dbt Databricks adapter package automatically installs dbt Core and other dependencies.

 If your local development machine uses any of the following operating systems, you must complete additional steps first: CentOS, MacOS, Ubuntu, Debian, and Windows. See the “Does my operating system have prerequisites” section of [Use pip to install dbt](https://docs.getdbt.com/dbt-cli/install/pip) on the dbt Labs website.
4. Activate this virtual environment by running `pipenv shell`. To confirm the activation, the terminal displays `(dbt_demo)` before the prompt. The virtual environment begins using the specified version of Python and isolates all package versions and code dependencies within this new environment.

 To deactivate this virtual environment, run `exit`. `(dbt_demo)` disappears from before the prompt. If you run `python --version` or `pip list` with this virtual environment deactivated, you might see a different version of Python, a different list of available packages or package versions, or both.
5. Confirm that your virtual environment is running the expected version of Python by running `python` with the `--version` option.

 If an unexpected version of Python displays, make sure you have activated your virtual environment by running `pipenv shell`.
6. Confirm that your virtual environment is running the expected versions of dbt and the dbt Databricks adapter by running `dbt` with the `--version` option.

 If an unexpected version of dbt or the dbt Databricks adapter displays, make sure you have activated your virtual environment by running `pipenv shell`. If an unexpected version still displays, try installing dbt or the dbt Databricks adapter again after you activate your virtual environment.


## Step 2: Create a dbt project and specify and test connection settings


In this step, you create a dbt *project*, which is a collection of related directories and files that are required to use dbt. You then configure your connection *profiles*, which contain connection settings to a Databricks [cluster](https://docs.databricks.com/en/clusters/configure.html), a [SQL warehouse](https://docs.databricks.com/en/sql/admin/create-sql-warehouse.html), or both. To increase security, dbt projects and profiles are stored in separate locations by default.


Tip


You can connect to an existing cluster or SQL warehouse, or you can create a new one.


* An existing cluster or SQL warehouse can be efficient for multiple dbt projects, for using dbt in a team, or for development use cases.
* A new cluster or SQL warehouse allows you to run a single dbt project in isolation for production use cases, as well as leverage automatic termination to save costs when that dbt project is not running.


Use Databricks to create a new cluster or SQL warehouse, and then reference the newly-created or existing cluster or SQL warehouse from your dbt profile.


1. When you are prompted to choose a `databricks` or `spark` database, enter the number that corresponds to `databricks`.
2. When prompted for a `host` value, do the following:


	* For a cluster, enter the **Server Hostname** value from the [Advanced Options, JDBC/ODBC](https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#connection-details-cluster) tab for your Databricks cluster.
	* For a SQL warehouse, enter the **Server Hostname** value from the [Connection Details](https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#connection-details-sql-warehouse) tab for your SQL warehouse.
3. When prompted for an `http_path` value, do the following:


	* For a cluster, enter the **HTTP Path** value from the [Advanced Options, JDBC/ODBC](https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#connection-details-cluster) tab for your Databricks cluster.
	* For a SQL warehouse, enter the **HTTP Path** value from the [Connection Details](https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#connection-details-sql-warehouse) tab for your SQL warehouse.
4. To choose an authentication type, enter the number that corresponds with `use oauth` (recommended) or `use access token`.
5. If you chose `use access token` for your authentication type, enter the value of your Databricks [personal access token](https://docs.databricks.com/api/workspace/tokenmanagement).

 As a security best practice when you authenticate with automated tools, systems, scripts, and apps, Databricks recommends that you use OAuth tokens or personal access tokens belonging to [service principals](https://docs.databricks.com/en/administration-guide/users-groups/service-principals.html) instead of workspace users. To create tokens for service principals, see [Manage tokens for a service principal](https://docs.databricks.com/en/administration-guide/users-groups/service-principals.html#personal-access-tokens).
6. When prompted for the `desired Unity Catalog option` value, enter the number that corresponds with `use Unity Catalog` or `not use Unity Catalog`.
7. If you chose to use Unity Catalog, enter the desired value for `catalog` when prompted.
8. Enter the desired values for `schema` and `threads` when prompted.
9. dbt writes your entries to a `profiles.yml` file. The location of this file is listed in the output of the `dbt init` command. You can also list this location later by running the `dbt debug --config-dir` command. You can open this file now to examine and verify its contents.

 If you chose `use oauth` for your authentication type, add your machine-to-machine (M2M) or user-to-machine (U2M) authentication profile to `profiles.yml`.

 The following is an example `profiles.yml` file with the profile `aws-oauth-u2m` specified. Specifying `aws-oauth-u2m` for `target` sets the U2M profile as the default run profile used by dbt.

 
```
databricks_demo:
outputs:
   azure-oauth-u2m:
      catalog: uc_demos
      host: "xxx.cloud.databricks.com"
      http_path: "/sql/1.0/warehouses/9196548d010cf14d"
      schema: databricks_demo
      threads: 1
      type: databricks
      auth_type: oauth
target: aws-oauth-u2m

```
 Databricks does not recommend specifying secrets in `profiles.yml` directly. Instead, set the client ID and client secret as environment variables.
10. Confirm that the connection details are correct by running the `dbt debug` command.

 If you chose `use oauth` for your authentication type, you’re prompted to sign in with your identity provider.

 You should see output similar to the following:

 
```
...
Configuration:
  profiles.yml file [OK found and valid]
  dbt_project.yml file [OK found and valid]

Required dependencies:
  - git [OK found]

Connection:
  ...
  Connection test: OK connection ok

```