---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
Profiling improvements 

- Lower counter for max empty pulled messages. If we have 600 jobs it will take 300 hours. Of course this will be done in parallel, but in compute hours. 
- Move initialization 
- Scan fewer rows for columns that are long 
- Splitting large string to smaller batches 

Thoughts:
- Will breaking up super long strings into chunks make it faster?
- 
**TODO**:
- Run one batch job for one super long value and measure that. 
- Profile the memory


https://realpython.com/python-profiling/

Because a **deterministic profiler** monitors all the function calls across your application, it has considerable overhead and produces a lot of noise in the report. Moreover, this overhead isn’t uniform because it depends on the number of actual function calls, leading to inaccurate and distorted results.

In contrast, a **statistical profiler** will filter out insignificant calls that don’t affect the overall performance, and its overhead is uniform and adjustable. Depending on your sampling rate, functions that return quickly may not even show up in the report.

pyinstrument
```python
25.455 <module>  app/scanner/src/scan.py:1
├─ 23.186 scan_pii_data_and_write_to_table  app/scanner/src/scan.py:159
│  ├─ 17.451 ManagedBigQueryClient.execute_query  app/shared/src/storage_io/bigquery_client_factory.py:27
│  │  ├─ 13.083 Client.query  google/cloud/bigquery/client.py:3266
│  │  │     [303 frames hidden]  google, requests, urllib3, http, sock...
│  │  │        12.848 _SSLSocket.read  None
│  │  └─ 4.367 Retry.result  google/cloud/bigquery/job/query.py:1390
│  │        [492 frames hidden]  google, requests, urllib3, http, sock...
│  ├─ 3.954 scan_data  app/scanner/src/scan.py:275
│  │  └─ 3.636 RowIterator._page_iter  google/api_core/page_iterator.py:232
│  │        [269 frames hidden]  google, requests, urllib3, http, sock...
│  ├─ 0.879 BigQueryClientFactory.get_client  app/shared/src/storage_io/bigquery_client_factory.py:138
│  │  └─ 0.879 Client.__init__  google/cloud/bigquery/client.py:234
│  │        [33 frames hidden]  google, subprocess, <built-in>, json
│  └─ 0.729 DetectorFacade.__init__  app/scanner/src/detectors.py:317
│     └─ 0.729 SpacyDetector.__init__  app/scanner/src/detectors.py:283
│        └─ 0.729 load  spacy/__init__.py:30
│              [1002 frames hidden]  spacy, en_core_web_sm, catalogue, imp...
├─ 1.664 <module>  app/scanner/src/detectors.py:1
│  └─ 1.662 <module>  spacy/__init__.py:1
│        [3133 frames hidden]  spacy, thinc, torch, sympy, <built-in...
└─ 0.481 <module>  google/cloud/bigquery/__init__.py:1
      [1737 frames hidden]  google, tqdm, IPython, jedi, <built-i...

To view this report with different options, run:
    pyinstrument --load-prev 2023-07-18T11-06-56 [options]


```

**PySpy** 

```
sudo -E py-spy record -o profile.svg -- python app/scanner/src/scan.py
```

**Flamegraph**
/Users/hugo/Work/pii/pii-detector-branches/pr/refactor_anase_446_anase_454/profile.svg?x=11&y=164


See all the jobs
```SQL

SELECT
start_time
FROM
`region-eu.INFORMATION_SCHEMA.JOBS`, UNNEST(referenced_tables) as r
where DATE(start_time) BETWEEN "2023-06-05" AND "2023-06-08"

```
We queried for 
76,385524645888 TB
Took only 1.5 h however


Running on 200 tables
```python
  _     ._   __/__   _ _  _  _ _/_   Recorded: 13:35:51  Samples:  22343
 /_//_/// /_\ / //_// / //_'/ //     Duration: 2932.305  CPU time: 27.085
/   _/                      v4.5.0

Program: cloud_batch_launcher.py -o instrument_profile.out

2290.486 <module>  cloud_batch_launcher.py:1
└─ 2288.234 run  cloud_batch_launcher.py:7
   └─ 2288.234 PubSubPullSubscriber.pull  app/shared/src/pubsub/subscriber.py:31
      ├─ 2248.016 process_worker_event  app/scanner/process_message_to_scan.py:32
      │  └─ 2247.709 scan_pii_data_and_write_to_table  app/scanner/src/scan.py:159
      │     ├─ 2180.835 ManagedBigQueryClient.execute_query  app/shared/src/storage_io/bigquery_client_factory.py:27
      │     │  ├─ 2151.524 Client.query  google/cloud/bigquery/client.py:3266
      │     │  │     [1140 frames hidden]  google, requests, urllib3, http, sock...
      │     │  │        2141.648 _SSLSocket.read  None
      │     │  └─ 29.305 Retry.result  google/cloud/bigquery/job/query.py:1390
      │     │        [1331 frames hidden]  google, requests, urllib3, http, sock...
      │     └─ 32.890 scan_data  app/scanner/src/scan.py:275
      │        └─ 30.568 RowIterator._page_iter  google/api_core/page_iterator.py:232
      │              [1063 frames hidden]  google, requests, urllib3, http, sock...
      └─ 23.743 SubscriberClient.pull  google/pubsub_v1/services/subscriber/client.py:1366
            [134 frames hidden]  google, grpc, proto, <built-in>, thre...

To view this report with different options, run:
    pyinstrument --load-prev 2023-07-24T13-35-51 [options]
```

```python
Thread 0x1FABDDE00 (idle): "MainThread"
    read (ssl.py:1129)
    recv_into (ssl.py:1273)
    readinto (socket.py:705)
    _read_status (http/client.py:278)
    begin (http/client.py:317)
    getresponse (http/client.py:1368)
    _make_request (urllib3/connectionpool.py:445)
    urlopen (urllib3/connectionpool.py:703)
    send (requests/adapters.py:500)
    send (requests/sessions.py:701)
    request (requests/sessions.py:587)
    request (auth/transport/requests.py:549)
    _do_request (_http/__init__.py:379)
    _make_request (_http/__init__.py:341)
    api_request (_http/__init__.py:482)
    retry_target (api_core/retry.py:191)
    retry_wrapped_func (api_core/retry.py:349)
    _call_api (bigquery/client.py:813)
    _begin (bigquery/job/base.py:693)
    _begin (bigquery/job/query.py:1306)
    do_query (bigquery/_job_helpers.py:91)
    query_jobs_insert (bigquery/_job_helpers.py:114)
    query (bigquery/client.py:3403)
    execute_query (bigquery_client_factory.py:44)
    scan_pii_data_and_write_to_table (scan.py:209)
    process_worker_event (process_message_to_scan.py:34)
    pull (subscriber.py:61)
    run (cloud_batch_launcher.py:23)
    <module> (cloud_batch_launcher.py:34)
    _run_code (runpy.py:86)
    _run_module_code (runpy.py:96)
    run_path (runpy.py:269)
    <module> (<string>:1)
    main (pyinstrument/__main__.py:327)
    <module> (pyinstrument:8)

```


https://stackoverflow.com/questions/132058/showing-the-stack-trace-from-a-running-python-application

Pulling empty data takes 18 seconds
0.5 hours per batch job to shutdown. 
If we have 600 jobs it will take 300 hours. Of course this will be done in parallel. 

Of course we have a timeout from pull for 600 seconds? But that's only the request for pulling down messages


Stuck on 
Almost all the time is spent in the ValueFilter process_value filter. 



- Profiling  
- Scan fewer rows for columns that are long 
- Splitting large string to smaller batches 

### Profiling investigation outcome  

#### Classes reinitialised  
Classes initialised in low level functions, reinitialized for any new pubsub message which adds up to TODO ADD NUMBER.  Get some numbers on how long each initialisation takes 

Move bigquery client, detectors and reading of file to beginning of cloud_batch job. 
**

#### Number of queries executing
Get numbers on how many queries we run, how many tables we're querying and how much data. 

#### Exclude audit log access
This content can for example contain select statements.  
audit_log.cloudaudit_googleapis_com_data_access

Examples of long strings

**Error messages** 
Error while importing: [{'index': 992, 'errors': [{'reason': 'invalid', 'location': 'date_of_l

**Long list**
[0.03455032149460496, 0.011270248640891906,.... ]

**Json**  
{"busObId": "934ec7a1701c451ce57f2c43bfbbe2e46fe4843f81"}

**html** 
```
<Track><trackNo>1</trackNo><title>1. Präludium ( 1. Akt)</title><artist></artist> <Track><trackNo>1</trackNo><title>1. Präludium ( 1. Akt)</title><artist></artist><playPeriod>223</playPeriod><mediaUrl>http:
```

**yaml** 
```
openapi: 3.0.0  
info:  
title: customers  
description: Cloud-CCR Customers (B2C) API  
# Never forget to update the version in README.md
```

**schemas** 
from mms-ssr-dev.table_similarity_score.t_alp_table_data_20230331 and mms-dac-monitoring-bq-d-data.alp_data.t_pii_input_data

```
SchemaField('id', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('kind',
```

List from table similarty containing list


**Number** 
```
2458536----2553022----2555091----2555001----2555307----2458746----2298095----2554401----2458441----2555750----2555613----2295595----2556667
```
table: feed-composition-prod.data_quality.debug_online_delta_MEDIADE

**Bytes** 
```
b'{\x00"\x00s\x00a\x00l\x00e\x00s\x00l\x00i\x00n\x00e\x00"\x00:\x00"\x00M\x00e\x00d\x00
```

**Uknown format**
Table: at-tableau-dev.metadata_staging.reporting_metadata
format:
```
avg basket value per member to (selected period to compare),# avg baskets per member all mem to (target month pre month),# avg baskets per member all mem to (target month pre year),# avg baskets per member to (selected period to compare),# avg baskets per member to (target month pre month),# avg baskets per member to (target month pre
```

table: v105-3114-sales-assistant-hist.06_analytics_co.co_data

format:
```
WAITING_STOCK>AWAITING_STOCK>AWAITING_STOCK>BACKORDERED>AWAITING_STOCK>BACKORDERED>AWAITING_STOCK>BACKORDER
```

#### Descriptions of items


#### Project with long content
Distribution of project with content_value > 10,000 

```SQL
WITH tmp as ( SELECT * FROM `mms-ana-anase-dataclf-d.dctable_data.analytics_tables_sample`
WHERE LENGTH(sample_content_value) > 10000
QUALIFY ROW_NUMBER() OVER(PARTITION BY full_table_reference, sample_content_variable_reference) = 1
)
SELECT SPLIT(full_table_reference, ".")[0] dataset, COUNT(*) cnt from tmp
GROUP BY dataset
ORDER BY cnt DESC
```

feed-composition-prod got way more than any other project and most come from tempory exports. 

![[Pasted image 20230726152132.png]]

Distribution of different types of data in strings. 
![[Pasted image 20230726153847.png]]

We need to consider how the string actually look like. Depending on if there are a lot of spaces or not it will take a lot of time. 

Number of unique fields 1344350
Fields 29728


E2 machines 

![[Pasted image 20230727174437.png]]

batch job 

Mem | cpu | type
---
1.95 GB|2 vCPU|e2-standard-4|


Took 79.32128882408142

to can the following 

```SQL
SELECT sample_content_variable_reference, sample_content_value FROM `mms-ana-==anase==-dataclf-d.dctable_data.analytics_tables_sample` WHERE full_table_reference = "sales-product-histo.thor_sales_product_v2_historization_dev.errors" and sample_content_variable_reference = "DATA" AND LENGTH(sample_content_value) > 100000 LIMIT 1
```


Running for 1000000 records took 2734 seconds.  
```

{"severity": "INFO", "message": "MMS-INFO: query is \n        SELECT\n          sample_content_variable_reference,\n          sample_content_value\n        FROM\n          `mms-ana-anase-dataclf-d.dctable_data.analytics_tables_sample` \n        WHERE LENGTH(sample_content_value) > 1000000 \n        LIMIT 1\n    ", "trace_id": null}
Function scan_data(<google.cloud.bigquery.table.RowIterator object at 0x1352cf3a0>, <app.scanner.src.detectors.DetectorFacade object at 0x13539ead0>, <app.scanner.src.scan.PiiResultPreparer object at 0x13539f970>) {} Took 2732.9028 seconds
{"severity": "INFO", "message": "MMS-INFO: Scanned table mms-marketing-analytics.temp.sales_loyalty field dummy finished in 2734.3147311210632 seconds.", "trace_id": null}
```
