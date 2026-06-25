---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

Set up Databricks 
![[Pasted image 20240708134237.png]]

ContactL: Astrid, Lars Kristian, Lars Martin Kleppe, Moritz

# Questions
- How to configure pools?
- How to configure clusters? Which configuration do you use? 
- How to setup access to dataset that goes across environment? Do you even want this? Don't think so? 




### Snowflake vs Databricks
#snowflake-vs-databricks

Johan Westlund  [8 months ago](https://netlight.slack.com/archives/C04G2CJP6/p1677053677712359?thread_ts=1676986310.537649&cid=C04G2CJP6)  

Yes, we started on Azure Databricks using it for a large portion of our pipe: lake stuff, warehouse and science. Scope and team was quite small. During my time there we switched to SF for the model part and was very happy with the switch - it was a lot more performant for our sql-based (dbt) transformations and freed up developer time that was spent dealing with clusters and other spark stuff. A bit more expensive but it was worth it for us. Also, PBI integration to Databricks was not good (this was 2 years ago, things might have changed)  
 We still kept databricks around for lake and science, but since I left the team 1 year ago they are now using SF for lake, Azure ML for science.  
My 5 cents is that databricks needs more skill to manage effectively, but very versatile. If the skill or time to invest is there, Databricks might be a good option, but it was not in our case


# Databricks in Azure 

## Setup 

+ Setup Virtual Network 
- (Optional) Create a new resource group were Databricks can be deployed in. 
+ Inject Databricks in the Virtual Network
- **Assign users to admin** in account settings. 
 - [SCIM sync](https://learn.microsoft.com/en-gb/azure/databricks/administration-guide/users-groups/scim/)
	 - [identity federation](https://learn.microsoft.com/en-gb/azure/databricks/administration-guide/users-groups/#enable-identity-federation)
 - Create private endpoint to access data in storage account securely.  
+ Setup setting for Azure storage
- Make sure to create a [Azure Data Lake Storage Gen2](https://learn.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account)
- Crete a Unity Catalog
- Configure [managed identity to connect to Azure storage](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/azure-managed-identities) 
	1. Create managed identity
	2. Create access connector 
	3. Deploy custom template  
	4. Grant identity access to storage account
	5. Grant the managed identity access to file events. 
	6. Grant the Azure Databricks access to configure file events on your behalf. 
	7. Use a managed identity to access the Unity Catalog root storage account
			
	 


You can create a data flow in ADF which source is an inline dataset reading by CDC and a sink being a delta table where you need to specify the bucket where data is stored. 

You can also setup an azure connector but to do that you need more permission for the unity catalog.  

Read delta table via 

```python

#setup reading for storage account. Probably not needed if you have the connector setup
spark.conf.set(
"fs.azure.account.key."+storage_account_name+".blob.core.windows.net",
storage_account_access_key)


from delta.tables import *

from pyspark.sql.functions import *

deltaTableUsers = DeltaTable.forName(spark, "users")

# I only get it working with path but it would be interesting to see if one can get it working with table name instead.
deltaTableUsersUpdates = DeltaTable.forPath(spark,"wasbs://raw@hugo.blob.core.windows.net/users/")

dfUpdates = deltaTableUsersUpdates.toDF()

dfUpdates.show()

# Merge tables together
(deltaTableUsers.alias('users')

.merge(dfUpdates.alias('updates'), "users.id = updates.id")
.whenMatchedUpdateAll()
.whenNotMatchedInsertAll()
.whenNotMatchedBySourceDelete()
.execute()
)
```

# Databrick Organization

## Hub and spoke 
https://www.databricks.com/blog/building-data-mesh-based-databricks-lakehouse-part-2

https://www.youtube.com/watch?v=bpehnBe1fCs

![[Pasted image 20231213160557.png]]

## Unity Catalog

https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/best-practices


![[Pasted image 20231128142550.png]]

![[Pasted image 20231213160111.png]]

![[Pasted image 20231218122852.png]]
### Thoughts
- **How do you request usage to a dataset?**  
- Do they have domains? Would you setup users within certain groups? 


## Auditing for governance 
- What are the most popular data assets across my organization?
https://www.databricks.com/blog/2020/06/02/monitor-your-databricks-workspace-with-audit-logs.html
https://www.databricks.com/blog/2022/05/02/monitoring-your-databricks-lakehouse-platform-with-audit-logs.html

![[Pasted image 20231129112021.png]]

![[Pasted image 20231129112036.png]]

![[Pasted image 20231129112053.png]]

### Data quality

#### Expectations 
What expectations to we have for the golden records? 
https://learn.microsoft.com/en-us/azure/databricks/delta-live-tables/expectations

### Observability
https://learn.microsoft.com/en-us/azure/databricks/delta-live-tables/observability


### Networking 

![[Pasted image 20231129183344.png]]

Microsoft recommends use of Azure Private Link and private endpoints for secure and private access to services hosted on the Azure platform. Azure Private Link provisions a network interface into a virtual network of your choosing for Azure services such as Azure Storage or Azure SQL. For more information, see [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) and [What is a private endpoint?](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview).

Good explanation https://www.youtube.com/watch?v=bPNkXwRFsek


## [Administration cheat sheet](https://learn.microsoft.com/en-us/azure/databricks/cheat-sheet/administration) 


### Security best practices

https://cms.databricks.com/sites/default/files/2023-03/Azure-Databricks-Security-Best-Practices-and-Threat-Model.pdf

#### Most deployments
#### Highly-secure deployments



---

[Using dbx](https://medium.com/d-one/how-to-streamline-data-pipelines-in-databricks-with-dbx-7c92e8ab1d2e)
# Move into correct place
# ![[Pasted image 20231211115310.png]]


---

## Tests

https://docs.databricks.com/en/notebooks/best-practices.html

## Best practices 

https://github.com/databricks/notebook-best-practices/blob/main/notebooks/run_unit_tests.py
---


# Bugs

```
Job aborted due to stage failure: Task 14 in stage 184.0 failed 4 times, most recent failure: Lost task 14.3 in stage 184.0 (TID 2984) (10.179.0.5 executor 0): org.apache.spark.SparkRuntimeException: [UDF_ERROR.INTERNAL_] Execution of function generate_uuid() failed == Error == Environment directory not found at /local_disk0/.ephemeral_nfs/envs/pythonEnv-f99cde87-5953-45a1-a0cf-0695797b84e7, cause: java.nio.file.NoSuchFileException: /local_disk0/.ephemeral_nfs/envs/pythonEnv-f99cde87-5953-45a1-a0cf-0695797b84e7, missing path: /local_disk0/.ephemeral_nfs/envs/pythonEnv-f99cde87-5953-45a1-a0cf-0695797b84e7 == Stacktrace ==
```

According to 
https://kb.databricks.com/en_US/libraries/apache-spark-jobs-fail-with-environment-directory-not-found-error
issues between communication between cluster driver and worker. 

**Resolution**: For now limit it to one driver node.


29 Feb
All of a sudden got this error which seems to be coming from a notebook error.
![[Pasted image 20240229142821.png]]


## 20 Mars issue 

```
E                   delta.connect.exceptions.ConcurrentAppendException: Files were added to the root of the table by a concurrent update. Please try the operation again.
E                   Conflicting commit: {"timestamp":1710859844174,"operation":"CREATE OR REPLACE TABLE AS SELECT","operationParameters":{"partitionBy":[],"description":null,"isManaged":true,"properties":{"delta.enableDeletionVectors":"true"},"statsOnLoad":false},"readVersion":840,"isolationLevel":"WriteSerializable","isBlindAppend":false,"operationMetrics":{"numFiles":"1","numOutputRows":"4","numOutputBytes":"1546","conflictDetectionTimeMs":"22"},"tags":{"restoresDeletedRows":"false"},"engineInfo":"Databricks-Runtime/14.3.x-cpu-ml-scala2.12","txnId":"daea204e-6ac6-4739-8827-a7fe4ddd1501"}
E                   Refer to https://docs.microsoft.com/azure/databricks/delta/concurrency-control for more details.
```

## Resolution 
## [Avoid conflicts using partitioning and disjoint command conditions](https://docs.delta.io/latest/concurrency-control.html#id3)

In all cases marked “can conflict”, whether the two operations will conflict depends on whether they operate on the same set of files. You can make the two sets of files disjoint by partitioning the table by the same columns as those used in the conditions of the operations. For example, the two commands `UPDATE table WHERE date > '2010-01-01' ...` and `DELETE table WHERE date < '2010-01-01'` will conflict if the table is not partitioned by date, as both can attempt to modify the same set of files. Partitioning the table by `date` will avoid the conflict. Hence, partitioning a table according to the conditions commonly used on the command can reduce conflicts significantly. However, partitioning a table by a column that has high cardinality can lead to other performance issues due to large number of subdirectories.

## [](https://docs.delta.io/latest/concurrency-control.html#id4)

https://docs.delta.io/latest/concurrency-control.html

![[Pasted image 20240320175049.png]]

---

## 3 April

```
E                   delta.connect.exceptions.ConcurrentDeleteReadException: This transaction attempted to read one or more files that were deleted (for example part-00144-c0813bf8-1740-4bad-bdff-031ad7109914-c000.snappy.parquet in the root of the table) by a concurrent update. Please try the operation again.
E                   Conflicting commit: {"timestamp":1712148547565,"operation":"CREATE OR REPLACE TABLE AS SELECT","operationParameters":{"partitionBy":[],"description":null,"isManaged":true,"properties":{"delta.enableDeletionVectors":"true"},"statsOnLoad":false},"readVersion":1644,"isolationLevel":"WriteSerializable","isBlindAppend":false,"operationMetrics":{"numFiles":"0","numOutputRows":"0","numOutputBytes":"0"},"tags":{"restoresDeletedRows":"false"},"engineInfo":"Databricks-Runtime/14.3.x-cpu-ml-scala2.12","txnId":"0a5e709f-04dc-4b35-8cc1-6596af35df46"}
E                   Refer to https://docs.microsoft.com/azure/databricks/delta/concurrency-control for more details.
```

```
E                   delta.connect.exceptions.ConcurrentAppendException: Files were added to the root of the table by a concurrent update. Please try the operation again.
E                   Conflicting commit: {"timestamp":1712148722269,"operation":"MERGE","operationParameters":{"predicate":["((id#191844 = user_id) AND (new_token#192017 = token#191847))"],"matchedPredicates":[],"statsOnLoad":false,"notMatchedBySourcePredicates":[],"notMatchedPredicates":[{"actionType":"insert"}]},"readVersion":1662,"isolationLevel":"WriteSerializable","isBlindAppend":false,"operationMetrics":{"numTargetRowsCopied":"0","numTargetRowsDeleted":"0","numTargetFilesAdded":"2","numTargetBytesAdded":"2512","numTargetBytesRemoved":"0","numTargetDeletionVectorsAdded":"0","numTargetRowsMatchedUpdated":"0","executionTimeMs":"38582","numTargetRowsInserted":"2","conflictDetectionTimeMs":"28","numTargetRowsMatchedDeleted":"0","numTargetDeletionVectorsUpdated":"0","scanTimeMs":"0","numTargetRowsUpdated":"0","numOutputRows":"2","numTargetDeletionVectorsRemoved":"0","numTargetRowsNotMatchedBySourceUpdated":"0","numTargetChangeFilesAdded":"0","numSourceRows":"2","numTargetFilesRemoved":"0","numTargetRowsNotMatchedBySourceDeleted":"0","rewriteTimeMs":"35947"},"tags":{"noRowsCopied":"true","delta.rowTracking.preserved":"false","restoresDeletedRows":"false"},"engineInfo":"Databricks-Runtime/14.3.x-cpu-ml-scala2.12","txnId":"b1569fe9-13bf-4e9e-b272-2c917f4a3087"}
E                   Refer to https://docs.microsoft.com/azure/databricks/delta/concurrency-control for more details.
```

	Library installation attempted on the driver node of cluster 0229-125840-c8nlz2bz and failed. Please refer to the following error message to fix the library or contact Databricks support. Error Code: DRIVER_LIBRARY_INSTALLATION_FAILURE. Error Message: org.apache.spark.SparkException: Process List(/bin/su, libraries, -c, bash /local_disk0/.ephemeral_nfs/cluster_libraries/python/python_start_clusterwide.sh /local_disk0/.ephemeral_nfs/cluster_libraries/python/bin/pip install --upgrade /local_disk0/tmp/addedFileeacd47c7d97c465faa90e5f0688accc5954826978916162580/pseudoanonymization-0.0.2-py3-none-any (1).whl --disable-pip-version-check) exited with code 2. sh: 1: Syntax error: "(" unexpected
	