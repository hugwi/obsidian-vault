---
categories:
  - "[[Resources]]"
domain: compliance
created: 2026-06-23
---
**Related:** [[PCI Regulation]] · [[Data Governance Netlight]] · [[Projects/PII/PII Scanner|PII Scanner]] · [[GDPR]] · [[MOC-Data-Governance|Data Governance MOC]]

# Vorwerk

# Thoughts

- Easier to anonymize everything and control access with rules for the tokenized table. Otherwise you need to update the data dependent on consent. 

Before uploading data to AWS the Thermomix device checks the user consent status with Profile SCS. If no consent has been given, no
data will be uploaded.

The **userDeviceId** is an opaque key generated once one user on one device opts-in to the UsageBox consent. 

The userDeviceId is stored in the Facade /customer-devices SCS alongside the DCID

Once a user opts-out of the UsageBox consent, the userDeviceId is dropped from the Facade /customer-devices SCS, but not in the
UsageBox - as the link back to the user is broken

Once a user opts back into the UsageBox consent, a new userDeviceId is generated, that is different from the user's previous one, so his
past data cannot be linked back to his recent one.

## DCID 
Around 800 users a week approach the Service Desk with the request to have their account deleted. As of today not all sub-systems in
Cookidoo are aware of those requests and ergo also do not delete any data in their systems.
It has been decided that any data set that contains e.g. the dcid has to be anonymised or deleted once such a request comes in.

## Process for deletion
On a monthly basis, the Service Management will provide a consolidated list of all user since the last ticket that want their account
respectively data being deleted.

This process will be run once every 90 days. This will allow the DataHub to stay compliant while being as cost-efficient as possible.


https://vorwerkholding.sharepoint.com/teams/DatabricksEval/Shared%20Documents/General/Confluence%20Exports/NWOT-Data%20in%20UsageBox-Pipeline-061223-202019.pdf?CT=1702030115544&OR=ItemsView
Personal Data Access
Has anyone access to the PERSONAL DATA fields who is located outside of the EU? Are the members of the team accessing the data from
outside the EU? -> yes

**Is this the case now or not?**
There is however the strong veto of both Recommender and Insights team to keep those events
for longer than DataHub would have liked. In case this becomes a very costly operation, we will investigate how to cross-charge that to
those teams.

## New requirement
<mark style="background: #D2B3FFA6;">What does this mean? </mark>

https://vorwerkholding.sharepoint.com/teams/DatabricksEval/Shared%20Documents/General/Confluence%20Exports/DS360+_+UsageBox+Kickoff+(28.+_+29.11.).pdf?CT=1702030101019&OR=ItemsView
Messages not linked to use-cases allowed by legitimate interest only if customer did
give personalization consent (New requirement)
o The difference with the current concept is that data points cannot be persisted and
used without consent. Either there is the legitimate interest basis, or
personalization consent from the user.
o That means that those events need to be filtered out before being persisted in the
“Usage data table” if customer did not give personalization consent
o Those events can be persisted in the “Usage data table” with personalization id if
customer the customer gave personalization consent


## Re-Build TM6 UsageBox
<mark style="background: #D2B3FFA6;">How will this affect the "forget" process? Shouldn't all be anonymized?    
</mark>
• One file for Legitimate Interest
- Implement a second upload for the legitimate interest data
• One file for Personalisation
- Re-use the existing mechanism of the consent-mechanism on the device,
including the userDeviceId mechanism