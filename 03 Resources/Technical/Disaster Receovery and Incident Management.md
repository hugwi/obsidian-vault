### Articles
https://www.databricks.com/wp-content/uploads/2022/04/disaster-recovery-impact-assesment.pdf

Can we use delta lake time travel to get deleted data
```
Important

Table versions accessible with time travel are determined by a combination of the retention threshold for transaction log files and the frequency and specified retention for `VACUUM` operations. If you run `VACUUM` daily with the default values, 7 days of data is available for time travel.
```

# Disaster Recovery

Disaster recovery can be triggered by many different scenarios. It can be triggered by an unexpected break. Some core functionality may be down, including the cloud network, cloud storage, or another core service

A disaster is an unexpected problem resulting in a slowdown, interruption, or network outage in an IT system. Outages come in many forms, including the following examples:

- An earthquake or fire
- Technology failures
- System incompatibilities
- Simple human error 
- Intentional unauthorized access by third parties



Points to consider: 
- Regional Failover 
- Restoring daa

Disaster recovery might be more than just having a backup dependent on how long time it may take to restore

![[Pasted image 20241204161523.png]]

https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html
![[Pasted image 20241204161305.png]]
## Recovery point objective (RPO)

## Data Replication

## Recovery time objective

## Typical recovery workflow[](https://docs.databricks.com/en/admin/disaster-recovery.html#typical-recovery-workflow "Permalink to this headline")

# Backup 

## Backup time 
https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html

![[Pasted image 20241204164434.png]]

## Backup Plan 
[Create backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)
## Compare S3 backup types
https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html#compare-s3-backup-types

- Continuous backups only
- Periodic (snapshot) backups only, scheduled or on-demand
- Continuous backups combined with periodic/snapshot backups


# Incident handling 

What happens if the service is down? 