

# Dataform 

https://medium.com/dataform/switching-to-a-better-data-warehouse-naming-convention-20c95535e8f3

# Databricks

https://docs.databricks.com/en/data-governance/unity-catalog/best-practices.html

Catalogs represent a logical grouping of schemas, usually bounded by data access requirements. Catalogs often mirror organizational units or software development lifecycle scopes. You may choose, for example, to have a catalog for production data and a catalog for development data, or a catalog for non-customer data and one for sensitive customer data.

If the catalog is the primary unit of data isolation in the Databricks data governance model, the _workspace_ is the primary environment for working with data assets. Metastore admins and catalog owners can manage access to catalogs independently of workspaces, or they can bind catalogs to specific workspaces to ensure that certain kinds of data are processed only in those workspaces. You might want separate production and development workspaces, for example, or a separate workspace for processing personal data.

By default, access permissions for a securable object are inherited by the children of that object, with catalogs at the top of the hierarchy. This makes it easier to set up default access rules for your data and to specify different rules at each level of the hierarchy only where you need them.