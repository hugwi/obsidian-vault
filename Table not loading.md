---
categories:
  - "[[Projects]]"
project: "[[Datahub]]"
created: 2026-06-23
---
#datahub-issue 
**Problem**: Tables not loading in datahub-dev 
**Root cause**:  The issue arise when retrieving usage statistics about dataset, specifically topSqlQueries and seem to be coming from *ElasticSearch*. 

**Relevant logs**:
The  log describing this problem can be found in the datahub-gms [logs](https://console.cloud.google.com/logs/query;cursorTimestamp=2023-06-12T08:01:41.781520116Z;pinnedLogId=2023-06-12T08:01:41.781520116Z%2Fjyqt0qop4j56m9pm;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22mms-ana-anase-datahub-d-data%22%0Aresource.labels.location%3D%22europe-west4%22%0Aresource.labels.cluster_name%3D%22anase-datahub-cluster%22%0Aresource.labels.namespace_name%3D%22default%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Finstance%3D%22datahub%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Fname%3D%22datahub-gms%22%20severity%3E%3DDEFAULT%0Atimestamp%3D%222023-06-12T08:01:41.781520116Z%22%0AinsertId%3D%22jyqt0qop4j56m9pm%22?project=mms-ana-anase-datahub-d-data)  and looks like this
>Caused by: org.elasticsearch.ElasticsearchException: Elasticsearch exception [type=execution_exception, reason=execution_exception: java.lang.IllegalStateException: unexpected docvalues type NONE for field 'topSqlQueries' (expected one of [SORTED, SORTED_SET]). Re-index with correct docvalues type.]

This issue was first discovered at 2023-06-07 when tables were not loading. The issue got be narrowed down to Elasticserach failing by looking at the following [gms logs](https://console.cloud.google.com/logs/query;cursorTimestamp=2023-06-12T08:01:41.780768450Z;pinnedLogId=2023-06-12T08:01:41.781520116Z%2Fjyqt0qop4j56m9pm;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22mms-ana-anase-datahub-d-data%22%0Aresource.labels.location%3D%22europe-west4%22%0Aresource.labels.cluster_name%3D%22anase-datahub-cluster%22%0Aresource.labels.namespace_name%3D%22default%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Finstance%3D%22datahub%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Fname%3D%22datahub-gms%22%20severity%3E%3DDEFAULT%0Atimestamp%3D%222023-06-12T08:01:41.780768450Z%22%0AinsertId%3D%22786poi6eo5lznd6k%22?project=mms-ana-anase-datahub-d-data).

--- 
**Do no include**
Also have this [issue](https://console.cloud.google.com/logs/query;cursorTimestamp=2023-06-07T13:54:31.198676091Z;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22mms-ana-anase-datahub-d-data%22%0Aresource.labels.location%3D%22europe-west4%22%0Aresource.labels.cluster_name%3D%22anase-datahub-cluster%22%0Aresource.labels.namespace_name%3D%22default%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Finstance%3D%22datahub%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Fname%3D%22datahub-gms%22%20severity%3E%3DDEFAULT%0Atimestamp%3D%222023-06-07T13:54:31.198676091Z%22%0AinsertId%3D%2272czbcfpclxeae3t%22;timeRange=2023-06-07T11:00:00.000Z%2F2023-06-07T13:55:00.000Z?project=mms-ana-anase-datahub-d-data) 
>com.linkedin.r2.RemoteInvocationException: com.linkedin.data.template.RequiredFieldNotPresentException: Field "value" is required but it is not present
---

TODO: Check if this should be kept
Ingestion proposal at 12:31:37 seem to kicked of a lot of [post](https://console.cloud.google.com/logs/query;cursorTimestamp=2023-06-07T12:41:37.519855866Z;pinnedLogId=2023-06-07T12:41:37.519855866Z%2Fa1yfz87geq01nxov;query=resource.type%3D%22k8s_container%22%0Aresource.labels.project_id%3D%22mms-ana-anase-datahub-d-data%22%0Aresource.labels.location%3D%22europe-west4%22%0Aresource.labels.cluster_name%3D%22anase-datahub-cluster%22%0Aresource.labels.namespace_name%3D%22default%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Finstance%3D%22datahub%22%0Alabels.k8s-pod%2Fapp_kubernetes_io%2Fname%3D%22datahub-gms%22%20severity%3E%3DDEFAULT%0Atimestamp%3D%222023-06-07T12:41:37.519855866Z%22%0AinsertId%3D%22a1yfz87geq01nxov%22;timeRange=2023-06-07T06:17:12Z%2F2023-06-07T10:18:00.000000001Z?project=mms-ana-anase-datahub-d-data)to elastic search indexes.

**Similar issue in Datahub**
A similar [issue](https://datahubspace.slack.com/archives/C029A3M079U/p1683949129461639) also is mentioned in the Datahub slack channel where Hyejin Yoon (Acryl) points out that this might be an issue on their side.   

>   Hey, I found the cause. Some of my top_sql_queries’s length is over 32766, so elasticsearch failed to bulk. After I fixed to top_sql_queries’s length under 32766, everything works well.

The hypothesis was that the problem could be caused by too long strings [top_sql_queries](https://datahubspace.slack.com/archives/C029A3M079U/p1683903419165439) (Elasticsearch has a limitation on fields being longer than 32766), but it was rejected since they patched this problem by making sure that the total length of the topSqlQueries never exceed 20000 characters.

**Update 12:30** - I'm able to limit the problem to ElasticSearch having problem to query topSqlQueries due to NONE field. Need to figure out however why this has happened. 

We used acryl-datahub-0.10.3.1. See [https://console.cloud.google.com/cloud-build/builds;region=global/ffc0b343-c662-4582-98e6-683063c86b55;step=1?project=mms-ana-anase-datahub-d-data](https://console.cloud.google.com/cloud-build/builds;region=global/ffc0b343-c662-4582-98e6-683063c86b55;step=1?project=mms-ana-anase-datahub-d-data "https://console.cloud.google.com/cloud-build/builds;region=global/ffc0b343-c662-4582-98e6-683063c86b55;step=1?project=mms-ana-anase-datahub-d-data"). Might have some incompatibility issue-

**Solution**

Using Elasticvue the *dataset_datasetusagestatisticsaspect_v1*  was deleted and recreated by redeploying datahub.  

When doing so our build failed because a one of the values.yaml had an indention problem. We research that for quite some time an ultimately also find that there was a open fix for this issue but it deployment doesn't seemed to have propagated yet so we needed to manually upgrade datahub. The fix should have propagated now though.

However we noticed that we were missing the schema cp-schema-registry and noticed that it seemed to have been removed and changed to a internal implementation. It seems like they have been wanting to remove that for a while but it's unclear if it's already removed. 

Removing prerequisites-cp-schema-registry.
```YAML
topics:
			metadata_change_event_name: "MetadataChangeEvent_v4"
			failed_metadata_change_event_name: "FailedMetadataChangeEvent_v4"
			metadata_audit_event_name: "MetadataAuditEvent_v4"
			datahub_usage_event_name: "DataHubUsageEvent_v1"
			metadata_change_proposal_topic_name: "MetadataChangeProposal_v1"
			failed_metadata_change_proposal_topic_name: "FailedMetadataChangeProposal_v1"
			metadata_change_log_versioned_topic_name: "MetadataChangeLog_Versioned_v1"
			metadata_change_log_timeseries_topic_name: "MetadataChangeLog_Timeseries_v1"
			platform_event_topic_name: "PlatformEvent_v1"
			datahub_upgrade_history_topic_name: "DataHubUpgradeHistory_v1"
		## For AWS MSK set this to a number larger than 1
		# partitions: 3
		# replicationFactor: 3
		schemaregistry:
			# GMS Implementation - `url` configured based on component context
			type: INTERNAL
			# Confluent Kafka Implementation
			# type: KAFKA
			# url: "http://prerequisites-cp-schema-registry:8081"

			# Glue Implementation - `url` not applicable
			# type: AWS_GLUE
			# glue:
			#   region: us-east-1
			#   registry: datahub
```


Still getting problem with  datahub-datahub-system-update-job 
>ERROR StatusLogger Log4j2 could not find a logging implementation. Please add log4j-core to the classpath. Using SimpleLogger to log to the console.

We need to specify helm version. They added new updates to the latest version. They added a health check created a health check to an endpoint that didn't exist in helm version 0.10.2. The chart version wasn't compatible with the application version which always took the latest.   
For version 10.4 cp-schema-registry is not needed. Changed to type kafka. 

resgistry is maintained in datahub and not in prerequisistes. 

**Observation**
This table has no queries! https://datahub.mediamarktsaturn.com/dataset/urn:li:dataset:(urn:li:dataPlatform:bigquery,mms-tra-latest-tables-d-0000.data_share_dev.v_amt_campaign_cluster,DEV)/Queries?is_lineage_mode=false


Probable cause of Elasticsearch not loading 

https://datahubspace.slack.com/archives/C029A3M079U/p1684219641287839?thread_ts=1683903419.165439&cid=C029A3M079U

o

