---
categories:
  - "[[Projects]]"
project: "[[Datahub]]"
created: 2026-06-23
---

My basic understanding of snowflake is that you can define custom roles and have certain table/schema privileges assigned to that role (or even [assign other roles to a role](https://docs.snowflake.com/en/user-guide/security-access-control-overview.html)).  
We want to enable an access model for for self-service,  where a user should be able to request access to a dataset (one or multiple tables) and also possibly combine data from different datasets in their analysis.  

- If we create one role per dataset and give the analyst that role, I assume that the analyst will only be able to access the data by explicitly selecting that role in Snowflake and not be able to combine with other datasets requiring other roles, correct?
- If we instead have a generic Analyst role, and grant access to more and more tables based on access requests, other analysts will get the same access without needing it.

Have you done anything similar with Snowflake? How have you defined your roles / access model?

4 replies

---

![](https://ca.slack-edge.com/T0252T2EC-U01P6PMKAJK-63c21d17db84-48)

Julius Neudecker![:palm_tree:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-large/1f334.png)  [1 year ago](https://netlight.slack.com/archives/C04G2CJP6/p1666281283460369?thread_ts=1666279175.091579&cid=C04G2CJP6)  

The answer is _compound roles_: with the option **GRANT ROLE** ([https://docs.snowflake.com/en/sql-reference/sql/grant-role.html](https://docs.snowflake.com/en/sql-reference/sql/grant-role.html)) you can create a hierarchy of different roles. In your particular example, you would create a role for every single table or view (like described in your first scenario) and grant that role to an aggregate role, which in turn is granted to the user. Then, a user can enable the _use secondary roles_ flag to make sure that all roles are being considered in the background if necessary for masking or filter policies.**One caveat though**: this works fine for _select_-statements but has a side effect if you actually create or alter datasets. In that case - under the assumption that every select-role for a certain dataset has also the equivalent write-privilege - the owner of any altered or created dataset will be the role, which the user has currently selected upon executing (most likely the compound role).EDIT: although the simplest answer would be to create a single role for every table or view, I wouldn't recommend it and instread try to carve up the data landscape into different parts - thus vastly reducing _role-verbosity_. (edited) 

![](https://ca.slack-edge.com/T0252T2EC-U5VBZJERJ-fa49abcd09d7-48)

Tuukka Järvinen  [1 year ago](https://netlight.slack.com/archives/C04G2CJP6/p1666334021552239?thread_ts=1666279175.091579&cid=C04G2CJP6)  

We use the same things that Julius mentioned, the hierarchy of different roles and the [use secondary roles](https://docs.snowflake.com/en/sql-reference/sql/use-secondary-roles.html) is what we have in place as well. Our granularity is mostly on the schema level and grants are managed by dbt ![:dbt:](https://emoji.slack-edge.com/T0252T2EC/dbt/659542a2ae264d46.png)Furthermore, our first step towards self-service is by propagating AD groups to Snowflake such as FINANCE_READER group which then has read access to all finance-related schemas in Snowflake. User can make a request to join that AD group and then gets access when the request is approved.


[Role Inheritance](https://docs.snowflake.com/en/user-guide/security-access-control-overview#label-role-hierarchy-and-privilege-inheritance)

![[Pasted image 20240412134313.png]]


https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/sql_permissions
![[Pasted image 20240412142115.png]]


https://discourse.getdbt.com/t/how-do-you-manage-snowflake-privileges/1397

Thank you for starting this convo. We had a similar experience where we learned a lot about Snowflake along the way (that’s just being nice to ourselves ![:smiley:](https://emoji.discourse-cdn.com/twitter/smiley.png?v=9 ":smiley:") )

Given this is a big topic and I’m no expert, I will just comment on your first bullet point. We think about this a bit differently. Albeit, most other things you say definitely rings true for us too.

We think about the creation/ownership of objects by schema across databsaes as well. So we have a role for general purpose loading into the RAW schemas and another role for transformation which is what dbt uses to create the objects in the STG and MART schemas.

We did this because we wanted dbt to have as little privileges as possible given we wanted as many people from the business to use dbt as possible.

This is actually similar to the design you linked. But I guess the main point is, we found it useful to have a higher privileged role “Loader” to be able to perform operations across databases. Then have a lower privilege role, “Transformer” that could own and create objects within that database.

This allows the Loader role to be much more powerful which gives a lot of flexibility upstream in the pipeline given all the various options of how data can be loaded into Snowflake.


## Role inheritance over Composition [link](https://community.snowflake.com/s/article/snowflake-rbac-security-prefers-role-inheritance-to-role-composition)

The Role-based Access Control (RBAC) model adopted in Snowflake prefers role inheritance to role composition when roles are granted to users.
In combination with single role activation, this model makes separating duties easier and more accurate to implement, and violations easier to detect.

### Clear example 
Another scenario could be where there is no natural dominance between Roles A and B, and yet a user needs to use both roles simultaneously. A new composite role must be created, such as AB. While this model may be viewed as undesirable, and leads to increasing the number of roles required in the system, the benefit is that such composition (and thus lack of separation of duties) is explicit in the role hierarchy and easy to detect during privilege review.


## Inheritance model [Databricks](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#inheritance-model "Permalink to this headline")

Securable objects in Unity Catalog are hierarchical and privileges are inherited downward. The highest level object that privileges are inherited from is the catalog. This means that granting a privilege on a catalog or schema automatically grants the privilege to all current and future objects within the catalog or schema. Privileges that are granted on a Unity Catalog metastore are not inherited.


https://www.linkedin.com/advice/3/how-can-you-secure-your-data-warehouse-role-based
At the data store level of the data warehouse, roles should map interfaces to subject areas, not any more granular e.g. self-service analytics for sales data, whereas only prefab operational reports. RBAC for personas should be defined at the interface level. Ad-hoc interfaces are never governed well and ensuring understandability and fitness for purpose is a nightmare. Using the interface as the deepest layer of RBAC implementation enables efficient governance and can improve trust in data through understandability.



# Shift to ABAC model
![[Pasted image 20240614093331.png]]

![[Pasted image 20240614093407.png]]

![[Pasted image 20240614093609.png]]