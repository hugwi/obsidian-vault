Migrating from kubeflow for Databricks
Devices wasn't in Databricks



A lot of issues with the subsriptions combined 
We start excluding subscriptions 
A lot of the time there is duplications

table_subscriptions_status

If customer has payments problem. 
Dunning subscriptions means it didn't cancel activated but was a payment problem. 

Another consumers should also do the same cleanup

Laura need to report sales. 

Sources: Devices to know if it were TM5 and TM6

Assigns the most recent device to customers

We just to have customer in one tier 
![[Pasted image 20240911102738.png]]

purchases log is takee to know when during trial the customer decide to buy the device

![[Pasted image 20240911103224.png]]
Converted before end of trial or at the same time. 

## Cancelleation 
problem with concellation 
We need to pull from a lot different sources 
We assume that there has been cancellation if there is a gap
Need to apply logic to status deltas for marcoss. 

We reun everyday the full history to get the device. 


Data issues: 
Start and end date was wrongly taken from Zuora 
Some logic needs to be changed on how they build Zuora

Use Cases:  

- Conversions 
- Retentions 
- Cancellations
- Churn 

Reporting: 
- Controlling take the figures from dashboards to do forecast for the next year. 

Might arise more question when looking at in app purchases


