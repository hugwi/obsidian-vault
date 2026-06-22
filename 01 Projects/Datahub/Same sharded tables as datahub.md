
These odd examples show up like shards but are also displaye as shards in bigquery. 
`v105-3606-for.odbc.27_07_2023_20_48_25_93890304`
`mms-marketing-analytics.temp.ema_20210209_MMPL_AS_KrupsCoffeeMachine_pmai_20230728`


TODO: 
- [ ] Follow up 

seems like that in 
Seems a bit off. Shouldn't it be hits or customdimensions? 
https://datahub-dev.mediamarktsaturn.com/dataset/urn:li:dataset:(urn:li:dataPlatform:bigquery,v400-3663-ga-onlineplatform.196462391.ga_sessions_intraday,PROD)/Schema?is_lineage_mode=false&schemaFilter=

{"uuid": "ba904a3c-77db-49b0-ad8e-e322d6534c15", "context_id": null, "version": 1, "environment": "prod", "created_at": "2023-07-13T09:51:43.230176+00:00", "type": "Batch", "operation": "update", "props": {"glossary_identifier": "PIIMLService", "table_identifier": "v400-3663-ga-onlineplatform.196462391.ga_sessions_intraday", "type": "glossary_term_to_dataset", "field_name": "hits[].customdimensions[].value"}}


Query to get all the tables that are incorrectly labelled shards

```SQL

SELECT CONCAT(project_id, ".", dataset, ".", table_name) table_ref,

COUNT(*) OVER(),

FROM `mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data` WHERE TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")

AND REGEXP_CONTAINS(table_name, r"_\d{8}$")

AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$")

QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1
```


We can see that most incorrectly labelled shards stem from the project odbc who use this format for tables v105-3606-for.odbc.07_07_2023_10_10_33_44480400 where 44480400  isn't a date but 8 digits with a leading underscore. 

![[Pasted image 20230713164918.png]]

Query attached
```SQL
WITH
shards AS (
SELECT
project_id,
dataset,
table_schema
FROM
`mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data`
WHERE TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")
AND REGEXP_CONTAINS(table_name, r"_\d{8}$")
AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$") QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1 )
SELECT
project_id,
dataset
-- ,table_schema,
,COUNT(*) cnt
FROM
shards
GROUP BY
project_id,
dataset
-- , table_schema
ORDER BY
cnt DESC
LIMIT
1000
```

 If you uncomment the table_schema you can see that quite a few actually share schema (thus in theory could be referred to as shard). BUT THEY HAVE DIFFERENT TABLE BASE.

All shards with same table base still have different schema (seems like they just add 6 random digits at the end). For example although these tables 
`v105-3606-for.odbc.29_06_2023_08_00_10_37614384`
`v105-3606-for.odbc.29_06_2023_08_00_10_37937536`
have same base  
`v105-3606-for.odbc.29_06_2023_08_00_10`  
they still have completely different schema. Datahub however will treat them as one shard. 

If we alter the query slightly to extract table_base 

```SQL
WITH

shards AS (

SELECT

project_id,

dataset,

table_schema,

REGEXP_EXTRACT(table_name, r"^(.+?)_\d{8}$") as table_base

FROM

`mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data`

WHERE

TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")

AND REGEXP_CONTAINS(table_name, r"_\d{8}$")

AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$") QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1 )

SELECT

project_id,

dataset

,table_base

-- ,table_schema,

,COUNT(*) cnt

FROM

shards

GROUP BY

project_id,

dataset

,table_base

-- , table_schema

ORDER BY

cnt DESC

LIMIT

1000
```

Now we can see that most of this tables have different table base. So each of these tables will be treated as its own base. 

![[Pasted image 20230713171039.png]]


 We have 1498 tables that are missclassified but since some of them are shards and we take the schema into consideration we have 191 missclassified shards. 

```SQL
WITH

shards AS (

SELECT

project_id,

dataset,

table_schema

FROM

`mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data`

WHERE TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")

AND REGEXP_CONTAINS(table_name, r"_\d{8}$")

AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$") QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1 )

SELECT

project_id,

dataset

,table_schema

,COUNT(*) cnt

FROM

shards

GROUP BY

project_id,

dataset

, table_schema

ORDER BY

cnt DESC

LIMIT

1000
```


TLDR: 
- We have 1498 but in reality more like 191 incorrectly labelled shards.
- We can have tables with the same "table base" but completely different schemas. Datahub will treat them incorrectly as one if they add a random 8 digit number.
- If tables with the same prefix is ingested into Datahub only one of them (the one with the highest 8 digit) will be displayed in Datahub. However this situation is very rare and I believe it only happens when they have tables with the same table base in the same project. So project1.dataset1.table_11111111 wouldn't clash with project2.dataset1.table_11111111. 
- If we want to properly label all dataset we probably need to raise this too Datahub.  

Solution 1: Only match dates for PII scanner
Pro:
- All tables are scanned 
Cons: 
- Can't tag PII table correctly cause we have different notation.  
- We scan extra shards. Sometime tables are shards although they have different prefix. 

Solution 2: Same notation of datahub
Pros: 
- Same notation as dathahub (but we miss dataset with same table_base but different schema)
Cons:
- We miss some datasets

Solution 3: Solution 1 + open a PR to Datahub.
Cons: 
	- We still could have wrong PII glossary term sent to wrong table. 

Shards with different base could have same schema. -> we might scan to many and have more tables than we should since they have different name. Shit in shit out?

All shards with same table base still have different schema (seems like they just add 6 random digits at the end). For example although this table have same  
`v105-3606-for.odbc.29_06_2023_08_00_10` 
For instance these have same base but different shard in the end
`29_06_2023_08_00_10_37614384`
`29_06_2023_08_00_10_37937536`

-> if we treat each table base as one shard we're omitting some tables (currently it will only take `37937536` and not `37614384` )

Probably a thing that we should raise to Datahub. 


Fix: 
test with dataset `v135-5683-g-a.01_temp_fs_jg_new.ga_sessions_temp_pseud`

v135-5683-g-a.01_temp_fs_jg_new.ga_sessions_temp_pseud_92488497

Use dataplex api to fetch the fully qualified tables name 
Then use entries lookup to fetch the latest

![[Pasted image 20230717172332.png]]

![[Pasted image 20230717172750.png]]

{  
"scope": {  
   "includeProjectIds": [  
     "media-saturn-digital-analytics"  
   ]  
},  
"query": "name: media-saturn-digital-analytics.92513812"  
}


Sharded table pattern is set to deprecated in this commit. No explanation why though.
commit commit 4572c96d6085abb6f0030fe69ffee4b85f9d02e4
Author: Tamas Nemeth <treff7es@gmail.com>
Date:   Tue Aug 30 07:33:24 2022 +0200

    feat(ingestion): bigquery - Bigquery beta connector - first cut (#5663)


Author: Tamas Nemeth <treff7es@gmail.com>
Date:   Tue Aug 30 07:33:24 2022 +0200

    feat(ingestion): bigquery - Bigquery beta connector - first cut (#5663)

how can we make something that work for both pii and domains? 



TODO: 
- [ ] Follow up 

seems like that in 
Seems a bit off. Shouldn't it be hits or customdimensions? 
https://datahub-dev.mediamarktsaturn.com/dataset/urn:li:dataset:(urn:li:dataPlatform:bigquery,v400-3663-ga-onlineplatform.196462391.ga_sessions_intraday,PROD)/Schema?is_lineage_mode=false&schemaFilter=

{"uuid": "ba904a3c-77db-49b0-ad8e-e322d6534c15", "context_id": null, "version": 1, "environment": "prod", "created_at": "2023-07-13T09:51:43.230176+00:00", "type": "Batch", "operation": "update", "props": {"glossary_identifier": "PIIMLService", "table_identifier": "v400-3663-ga-onlineplatform.196462391.ga_sessions_intraday", "type": "glossary_term_to_dataset", "field_name": "hits[].customdimensions[].value"}}


Query to get all the tables that are incorrectly labelled shards

```SQL

SELECT CONCAT(project_id, ".", dataset, ".", table_name) table_ref,

COUNT(*) OVER(),

FROM `mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data` WHERE TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")

AND REGEXP_CONTAINS(table_name, r"_\d{8}$")

AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$")

QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1
```


We can see that most incorrectly labelled shards stem from the project odbc who use this format for tables v105-3606-for.odbc.07_07_2023_10_10_33_44480400 where 44480400  isn't a date but 8 digits with a leading underscore. 

![[Pasted image 20230713164918.png]]

Query attached
```SQL
WITH
shards AS (
SELECT
project_id,
dataset,
table_schema
FROM
`mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data`
WHERE TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")
AND REGEXP_CONTAINS(table_name, r"_\d{8}$")
AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$") QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1 )
SELECT
project_id,
dataset
-- ,table_schema,
,COUNT(*) cnt
FROM
shards
GROUP BY
project_id,
dataset
-- , table_schema
ORDER BY
cnt DESC
LIMIT
1000
```

 If you uncomment the table_schema you can see that quite a few actually share schema (thus in theory could be referred to as shard). BUT THEY HAVE DIFFERENT TABLE BASE.

All shards with same table base still have different schema (seems like they just add 6 random digits at the end). For example although these tables 
`v105-3606-for.odbc.29_06_2023_08_00_10_37614384`
`v105-3606-for.odbc.29_06_2023_08_00_10_37937536`
have same base  
`v105-3606-for.odbc.29_06_2023_08_00_10`  
they still have completely different schema. Datahub however will treat them as one shard. 

If we alter the query slightly to extract table_base 

```SQL
WITH

shards AS (

SELECT

project_id,

dataset,

table_schema,

REGEXP_EXTRACT(table_name, r"^(.+?)_\d{8}$") as table_base

FROM

`mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data`

WHERE

TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")

AND REGEXP_CONTAINS(table_name, r"_\d{8}$")

AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$") QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1 )

SELECT

project_id,

dataset

,table_base

-- ,table_schema,

,COUNT(*) cnt

FROM

shards

GROUP BY

project_id,

dataset

,table_base

-- , table_schema

ORDER BY

cnt DESC

LIMIT

1000
```

Now we can see that most of this tables have different table base. So each of these tables will be treated as its own base. 

![[Pasted image 20230713171039.png]]


 We have 1498 tables that are missclassified but since some of them are shards and we take the schema into consideration we have 191 missclassified shards. 

```SQL
WITH

shards AS (

SELECT

project_id,

dataset,

table_schema

FROM

`mms-dac-monitoring-bq-d-data.alp_data.t_alp_table_data`

WHERE TIMESTAMP_TRUNC(publishing_timestamp, DAY) > TIMESTAMP("2023-03-01")

AND REGEXP_CONTAINS(table_name, r"_\d{8}$")

AND NOT REGEXP_CONTAINS(table_name, r"_\d{4}(0[1-9]|1[0,1,2])(0[1-9]|[12][0-9]|3[01])$") QUALIFY ROW_NUMBER() OVER(PARTITION BY project_id, dataset, table_name ORDER BY publishing_timestamp DESC) = 1 )

SELECT

project_id,

dataset

,table_schema

,COUNT(*) cnt

FROM

shards

GROUP BY

project_id,

dataset

, table_schema

ORDER BY

cnt DESC

LIMIT

1000
```


TLDR: 
- We have 1498 but in reality more like 191 incorrectly labelled shards.
- We can have tables with the same "table base" but completely different schemas. Datahub will treat them incorrectly as one if they add a random 8 digit number.
- If tables with the same prefix is ingested into Datahub only one of them (the one with the highest 8 digit) will be displayed in Datahub. However this situation is very rare and I believe it only happens when they have tables with the same table base in the same project. So project1.dataset1.table_11111111 wouldn't clash with project2.dataset1.table_11111111. 
- If we want to properly label all dataset we probably need to raise this too Datahub.  

Solution 1: Only match dates for PII scanner
Pro:
- All tables are scanned 
Cons: 
- Can't tag PII table correctly cause we have different notation.  
- We scan extra shards. Sometime tables are shards although they have different prefix. 

Solution 2: Same notation of datahub
Pros: 
- Same notation as dathahub (but we miss dataset with same table_base but different schema)
Cons:
- We miss some datasets

Solution 3: Solution 1 + open a PR to Datahub.
Cons: 
	- We still could have wrong PII glossary term sent to wrong table. 

Shards with different base could have same schema. -> we might scan to many and have more tables than we should since they have different name. Shit in shit out?

All shards with same table base still have different schema (seems like they just add 6 random digits at the end). For example although this table have same  
`v105-3606-for.odbc.29_06_2023_08_00_10` 
For instance these have same base but different shard in the end
`29_06_2023_08_00_10_37614384`
`29_06_2023_08_00_10_37937536`

-> if we treat each table base as one shard we're omitting some tables (currently it will only take `37937536` and not `37614384` )

Probably a thing that we should raise to Datahub. 


Fix: 
test with dataset `v135-5683-g-a.01_temp_fs_jg_new.ga_sessions_temp_pseud`

v135-5683-g-a.01_temp_fs_jg_new.ga_sessions_temp_pseud_92488497

Use dataplex api to fetch the fully qualified tables name 
Then use entries lookup to fetch the latest

![[Pasted image 20230717172332.png]]

![[Pasted image 20230717172750.png]]

{  
"scope": {  
   "includeProjectIds": [  
     "media-saturn-digital-analytics"  
   ]  
},  
"query": "name: media-saturn-digital-analytics.92513812"  
}


Sharded table pattern is set to deprecated in this commit. No explanation why though.
commit commit 4572c96d6085abb6f0030fe69ffee4b85f9d02e4
Author: Tamas Nemeth <treff7es@gmail.com>
Date:   Tue Aug 30 07:33:24 2022 +0200

    feat(ingestion): bigquery - Bigquery beta connector - first cut (#5663)


Author: Tamas Nemeth <treff7es@gmail.com>
Date:   Tue Aug 30 07:33:24 2022 +0200

    feat(ingestion): bigquery - Bigquery beta connector - first cut (#5663)

