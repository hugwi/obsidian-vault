
# Questions 
- [ ] Is TLS enough for data in transit? - **End-to-end TLS encryption** from client to server to storage account

TODO: 

[Delta sharing][https://www.youtube.com/watch?v=EP5kmhP5t1I]
![[Pasted image 20231117150653.png]]

https://learn.microsoft.com/en-us/azure/databricks/data-sharing/

### Are egress costs high?

Delta Sharing within a region incurs no egress cost.

Delta Sharing is the only solution that enables cross-cloud and cross-region sharing without data replication, which is why it can incur egress charges.

To learn about how to reduce egress charges, talk to your Databricks account team.


### Security


The security of the sharing connection—including all identity verification, authentication, and auditing—is managed entirely through Delta Sharing and the Databricks platform. Another advantage is the ability to share Databricks notebook files.

https://www.databricks.com/blog/2022/08/01/security-best-practices-for-delta-sharing.html

It's important to note that [Delta Sharing](https://www.databricks.com/product/delta-sharing) has been built from the ground up with security in mind, allowing you to leverage the following features out of the box whether you use the [open source version](https://delta.io/sharing/) or its [managed equivalent](https://www.databricks.com/product/delta-sharing):

- **End-to-end TLS encryption** from client to server to storage account
- **Short lived credentials** such as pre-signed URLs are used to access the data
- **Easily govern, track, and audit access** to your shared data sets via [Unity Catalog](https://www.databricks.com/product/unity-catalog)

The best practices that we'll share as part of this blog are additive, allowing customers to align the appropriate security controls to their risk profile and the sensitivity of their data

#### Isn’t it insecure to use pre-signed URLs?

Delta Sharing uses pre-signed URLs to provide temporary access to a file in object storage. They are only given to recipients that already have access to the shared data. They are secure because they are short-lived and don’t expand the level of access beyond what recipients have already been granted.

#### Best practices

##### Securing token (Not need for databricks to databricks sharing)
https://learn.microsoft.com/en-gb/azure/databricks/data-sharing/#modify-the-recipient-token-lifetime
If you prefer not to use tokens to manage access to recipient shares, you should use [Databricks-to-Databricks sharing](https://learn.microsoft.com/en-gb/azure/databricks/data-sharing/share-data-databricks) or contact your Databricks account team for alternatives.

#### Consider the right level of granularity for Shares, Recipients & Partitions
In the [managed version](https://www.databricks.com/product/delta-sharing), each share can contain one or more tables and can be associated with one or more recipients, using fine-grained controls to manage who or how the multiple data sets are accessed.. This allows us to provide fine-grained access to multiple data sets in a way that would be much harder to achieve using [open source](https://delta.io/sharing/) alone.

#### Configure IP Access Lists
By default, all that is required to access your shares is a valid Delta Sharing Credential File

Configure Delta Sharing IP access lists (see the docs for [AWS](https://docs.databricks.com/data-sharing/delta-sharing/access_list.html), [Azure](https://docs.microsoft.com/en-gb/azure/databricks/data-sharing/delta-sharing/access_list)) to restrict recipient access to trusted IP addresses, for example, the public IP of your corporate VPN.

####  Configure network restrictions on the storage account(s)

Once a delta sharing request has been successfully authenticated by the sharing server, an array of short-lived credentials are generated and returned to the client. The client then uses these URLs to request the relevant files directly from the cloud provider. This design means that the transfer can happen in parallel at massive bandwidth, without streaming the results through the server. It also means that from a security perspective, you're likely to want to implement similar network restrictions on the storage account to the delta sharing recipient itself - there's no point in protecting the share at the recipient level, if the data itself is hosted in a storage account that can be accessed by anyone and from anywhere.

On Azure, Databricks recommends using [Managed Identities](https://docs.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/azure-managed-identities) (currently in Public Preview) to access the underlying Storage Account on behalf of [Unity Catalog](https://www.databricks.com/product/unity-catalog). Customers can then configure [Storage firewalls to restrict all other access](https://docs.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/azure-managed-identities#recommended-configure-trusted-access-to-azure-storage-based-on-your-managed-identity) to the trusted private endpoints, virtual networks or public IP ranges that delta sharing clients may use to access the data. Please reach out to your Databricks representative for more information.

- When using the managed version, the pre-signed URLs are generated by [Unity Catalog](https://www.databricks.com/product/unity-catalog), and therefore you will need to allow access from the [Databricks Control Plane NAT IP for your region](https://docs.databricks.com/administration-guide/cloud-configurations/aws/customer-managed-vpc.html#required-ips-and-storage-buckets).
- It's likely that one or more Databricks workspaces will also require access to the data, and therefore you should allow access from the relevant VPC IDs if the underlying S3 bucket is in the same region and you're using VPC Endpoints to connect to S3 or the public IP address that the data plane traffic resolves to (for example via a NAT Gateway).
- To avoid losing connectivity from within your corporate network, Databricks recommends always allowing access from at least one known and trusted IP address, such as the public IP of your corporate VPN. This is because Deny conditions apply even within the AWS console.

#### Restriction on network for bucket

![[Pasted image 20231130121416.png]]

#### Restriction for IAM role

![[Pasted image 20231130121439.png]]

The reason being is that as we have seen, [Unity Catalog](https://www.databricks.com/product/unity-catalog) provides fine grained access to your data in a way that is not possible with the coarse grained permissions provided by AWS IAM/S3. Therefore, if someone were able to access the S3 bucket directly they might be able to bypass those fine grained permissions and access more of the data than you had intended.

#### Audit logging (Probably later iteration)
- Which of my Delta Shares are the most popular?
- Are Delta Sharing Recipients being created without IP access list restrictions being applied?
- Who is trying to gain unauthorized access to my data products, and what queries are they trying to run?
- Are Delta Sharing Recipients being created with IP access list restrictions which are outside of my trusted IP address range?
- Are attempts to access my Delta Shares failing IP access list restrictions?
- Are attempts to access my Delta Shares repeatedly failing authentication?

#### Configure logging on the storage account(s) (Probably later iteration)

In  addition to enforcing network-level restrictions on the underlying storage account(s), you're likely going to want to monitor whether anyone is trying to bypass them. As such, Databricks recommends:

- Setting up [S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) on AWS as well as the appropriate monitoring and alerting around it
- Setting up [Diagnostic logging](https://docs.microsoft.com/en-us/azure/storage/blobs/monitor-blob-storage?tabs=azure-portal) on Azure, as well as the appropriate monitoring and alerting around it


### Networking 

https://medium.com/@alyssonmarquesdesouza/designing-a-multi-cloud-data-platform-with-databricks-24be057ac360

There are two main options for establishing this connectivity:

**1. Internet based**
Object Storage services can be configured to allow internet-based access to the data they store. In this approach, the clusters running in Cloud Provider 1 will resolve the storage endpoint URL to its public IP address and access the endpoint over the internet.

**2. Private connectivity**
A second option is to enable private connectivity by leveraging services such as Private Link to enable access to object storage over a Private IP address.

--- 
### Limitations 

- Tabular data must be in the [Delta table format](https://docs.databricks.com/en/delta/index.html). You can easily convert Parquet tables to Delta—and back again. See [CONVERT TO DELTA](https://docs.databricks.com/en/sql/language-manual/delta-convert-to-delta.html).
    
- View sharing is supported only in Databricks-to-Databricks sharing. Shareable views must be defined on Delta tables or other shareable views. For details, see (for providers) [Add views to a share](https://docs.databricks.com/en/data-sharing/create-share.html#views) and (for consumers) [Read shared views](https://docs.databricks.com/en/data-sharing/read-data-databricks.html#views).
    
- There are limits on the number of files in metadata allowed for a shared table. To learn more, see [Resource limit exceeded errors](https://docs.databricks.com/en/data-sharing/troubleshooting.html#resource-limits).
    
- Schemas named `information_schema` cannot be imported into a Unity Catalog metastore, because that schema name is reserved in Unity Catalog.
    
- [Table constraints](https://docs.databricks.com/en/tables/constraints.html) (primary and foreign key constraints) are not available in shared tables.
