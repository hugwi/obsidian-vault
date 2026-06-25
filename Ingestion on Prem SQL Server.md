---
categories:
  - "[[Projects]]"
project: "[[PII]]"
created: 2026-06-23
---


## [[Ingestion Patterns]]
CDC, full load, incremental 
## Questions
What kind of data do we need? Only the latest or historical changes. This will affect which process we use. For CDC for instance then we need to have a process for historical records as well. 


### CDC 
https://learn.microsoft.com/en-us/azure/data-factory/tutorial-incremental-copy-multiple-tables-portal

# [[Ingestion tools]]



## Networking
---
### Resources 
[How managed virtual network makes it easier](https://medium.com/@shunderpooch/taking-the-pain-out-of-networking-with-managed-virtual-networks-for-azure-synapse-and-azure-data-94e4ae589463)

---

### Managed network 

This eventually got even easier, as [**Private Links**](https://azure.microsoft.com/en-us/services/private-link/) became available on numerous Azure and partner services. I**nstead of the customers having to VNet Inject to reach a resource securely**, they could limit its connections to just the “[**Private Endpoint**](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview)” deployed in their network- a dedicated network interface for resources in the customer’s network to connect with a PaaS service- reducing the general overhead of managing a service wholly VNet Injected and all the layers of compute configuration required to make this work.

For private link need to pay for private endpoint and ingress and egress traffic. Also expressroute gatwaway. 

## Which is best for you?

# Networking Databricks (Probably don't need to b)

<mark style="background: #FF5582A6;">TO CONNECT TO ON PREM A VNET ALSO NEEDS TO BE CREATED!</mark>

## Optional configuration steps
### [Route Azure Databricks traffic using a virtual appliance or firewall](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/on-prem-network#--option-route-azure-databricks-traffic-using-a-virtual-appliance-or-firewall)
### Option: Configure custom DNS

### Option: Route Azure Databricks traffic using a virtual appliance or firewall

Microsoft recommends use of Azure Private Link and private endpoints for secure and private access to services hosted on the Azure platform. Azure Private Link provisions a network interface into a virtual network of your choosing for Azure services such as Azure Storage or Azure SQL. For more information, see [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) and [What is a private endpoint?](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview).

## Vnet injection for Databricks

https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/on-prem-network
![[Pasted image 20231129184400.png]]

https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-inject
The default deployment of Azure Databricks is a fully managed service on Azure: all compute plane resources, including a [VNet](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) that all clusters will be associated with, are deployed to a locked resource group. If you require network customization, however, you can deploy Azure Databricks compute plane resources in your own virtual network (sometimes called _VNet injection_), enabling you to:

- Connect Azure Databricks to other Azure services (such as Azure Storage) in a more secure manner using [service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview) or [private endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints).
- Connect to [on-premises data sources](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/on-prem-network) for use with Azure Databricks, taking advantage of [user-defined routes](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/udr).
- Connect Azure Databricks to a [network virtual appliance](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/on-prem-network#route-via-firewall) to inspect all outbound traffic and take actions according to allow and deny rules, by using [user-defined routes](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/udr).
- Configure Azure Databricks to use [custom DNS](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/on-prem-network#vnet-custom-dns).
- Configure [network security group (NSG) rules](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group) to specify egress traffic restrictions.
- Deploy Azure Databricks clusters in your existing VNet.

Deploying Azure Databricks compute plane resources to your own VNet also lets you take advantage of flexible CIDR ranges (anywhere between `/16`-`/24` for the VNet and up to `/26` for the subnets).


## Secure Azure service access from on-premises
<mark style="background: #CACFD9A6;">https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview#secure-azure-services-to-virtual-networks
</mark> **Shouldn't use service endpoints**

By default, Azure service resources secured to virtual networks aren't reachable from on-premises networks. If you want to allow traffic from on-premises, you must also allow public (typically, NAT) IP addresses from your on-premises or ExpressRoute. You can add these IP addresses through the IP firewall configuration for Azure service resources.

ExpressRoute: If you're using [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction?toc=/azure/virtual-network/toc.json) for public peering or Microsoft peering from your premises, you'll need to identify the NAT IP addresses that you're using. For public peering, each ExpressRoute circuit uses two NAT IP addresses, by default, applied to Azure service traffic when the traffic enters the Microsoft Azure network backbone. For Microsoft peering, the NAT IP addresses are either customer provided or provided by the service provider. To allow access to your service resources, you must allow these public IP addresses in the resource IP firewall setting. To find your public peering ExpressRoute circuit IP addresses, [open a support ticket with ExpressRoute](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/overview) via the Azure portal. For more information about NAT for ExpressRoute public and Microsoft peering, see [ExpressRoute NAT requirements](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-nat?toc=/azure/virtual-network/toc.json#nat-requirements-for-azure-public-peering).




# Meeting notes

## 1 December

On premise SQL server

The data that we share. 
Emarsys connectoin sql server
Data out of our system with middleware 

Create a users that has access toschemas and table? 
Date when the data was loaded? Always a column? 

Topology of data 
N3 level: 
3rd level for reporting? 
Raw data? 

Service request in service now to create azure data factory? 
Make a proposal. 
Micheal was working on. Databricks is suggestion. 
Connection to local server
Italian we need to connect to a local server?

7 systems getting data from us. 
Emarsys would be the first system to directly connected to us.
We create views to extract ystem for other systems.
Can data directly from the table. 
Use field last changed as a watermark
Issue with deleted records. In case of SAP we can identify deleted record. Other system that doesn't have it. We have to go through some logic. We upload 6 months data 
Some case problem when dele. If physical deleted we can't assign users for a transatiction that was table.
GDPR. 
We need to eastablish data lineage for many different system. 
Normally data is not manulaly deleted but automated.
The next delta will be scrambled. Databricks will be scrambled.   


https://ashy-wave-0b2f86d03.azurestaticapps.net/p/part-2-how-to-choose-the-right-adf-or-synapse-integration-runtime-for-a-secure-network-topology/