## VNet peering

VNet peering enables you to seamlessly connect Azure [virtual networks](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview). Once peered, the VNets appear as one, for connectivity purposes. The traffic between virtual machines in the peered virtual networks is routed through the Microsoft backbone infrastructure, much like traffic is routed between virtual machines in the same VNet, through _private_ IP addresses only.

## VPN gateways

A VPN gateway is a specific type of VNet gateway that is used to send traffic between an Azure virtual network and an on-premises location over the public internet. You can also use a VPN gateway to send traffic between VNets. Each VNet can have only one VPN gateway.

### Which is best for you?

While we offer two ways to connect VNets, based on your specific scenario and needs, you might want to pick one over the other.



**VPN Gateways** provide a limited bandwidth connection and is useful in scenarios where encryption is needed, but bandwidth restrictions are tolerable. In these scenarios, customers are also not as latency-sensitive.


## Private link vs VPN 
https://community.appian.com/discussions/f/integrations/21691/privatelink-vs-vpn-tunnel

AWS PrivateLink and VPN tunnels both provide secure connectivity between a customer's network and an AWS VPC (Virtual Private Cloud)

However, there can be some advantages of using PrivateLink over VPN tunnels

  
**Performance:** As PrivateLink does not require data to traverse the public internet (traffic never leaves the AWS network), it can provide faster and more consistent performance compared to VPN tunnels.

**Simplified setup:** Setting up a VPN connection can be complex, requiring the configuration of multiple components such as tunnels, gateways, and route tables. PrivateLink, on the other hand, provides a simpler setup as it only requires the creation of an interface endpoint in the VPC and an endpoint service in the customer's network.

**Cost-effective:** PrivateLink pricing is based on the number of requests made to the endpoint service, whereas VPN tunnels are charged based on data transferred over the connection. For customers with large amounts of data transferred, PrivateLink can be a more cost-effective option.

## Expressroute vs Private Link

**On-premises and peered networks**: Access services running in Azure from on-premises over ExpressRoute private peering, VPN tunnels, and peered virtual networks using private endpoints. There's no need to configure ExpressRoute Microsoft peering or traverse the internet to reach the service. Private Link provides a secure way to migrate workloads to Azure.

https://www.youtube.com/watch?v=i3byrLaJiiM

# Connectivity to other cloud providers

![[Pasted image 20231207142423.png]]