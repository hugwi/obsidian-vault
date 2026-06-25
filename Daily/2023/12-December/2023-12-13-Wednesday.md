---
categories:
  - "[[Daily]]"
created: 2023-12-13 09:43
---
tags:: [[+Daily Notes]]

# Wednesday, December 13, 2023

<< [[2023-12-12-Tuesday|Yesterday]] | [[2023-12-14-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Vw
	 - [ ] Book meeting with Pietro tomorrow
- [ ] Netlight 
	 - [ ] Reach out to Klarna to setup a meeting - Gunnar Tångring
	 - [ ] Remove myself from the Munich group
- [ ] Next day
	- [ ] Ask Benedikt about clarification how the ticket relates to the deletion of DCID since I'm missing context
 - [ ] Backlog
	- [ ] Sketch Ingestion flow
	- [ ] Remove administrator role
	- [ ] WAITING - Check if CDC is disadvantagous if data is updated daily.
	- [ ] Create a data and dumplings website
	- [ ] Write about data governance initiative
	- [ ] See how a role for reading CDC can be setup.
	- [ ] Watch [gen ai talk](https://netlight365beta-my.sharepoint.com/personal/raku_netlight_com/_layouts/15/stream.aspx?id=%2Fpersonal%2Fraku%5Fnetlight%5Fcom%2FDocuments%2FRecordings%2FArchitecting%20LLM%2Dpowered%20applications%5F%20A%20practical%20guide%2D20231207%5F180207%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview&ga=1)
- [ ] Thoughts
	- [ ] Can we do quality checks too see that CDC works. For isntance hashnig a table?

---

# 📝 Notes

Hi Pietro! 
I hope you're doing well and thanks for the introduction to how data could be ingested from on prem to Azure. 

I have some additional questions about the ingestion which we briefly touched upon last time: 
- What would be the process for us to setup a connection to on prem and ingest data? 
- You mentioned that data get scrambled, what's meant by this and how does this affect us down stream? 
- How are deleted records propagated? 
- The proposed solution to ingest data seems to be by using a watermark that you create? Have you also used CDC in the past or is this the preferred choice to ingest data? 

If you have time this week or next week to discuss these topics that would be super helpful.  


## Meeting Data privacy

**Legimitate Interest**

Opt in if we got consent - we can unanonymize the data.
The data should 

Personalised if consent is given 
Legitimate interest don't need consent. 
Consent opt in 
Second is anonymized way.  Product improvements. 

**Error handling**  - Can access all the data without filter - legimitate interest 
**Recommender** - Can use data from the device, what a person cooked do give recommendation. Can only access the data for user with consent. Mapping table. Personalisation id if the user gets consent. 

**Considerations:** 
How do we identify. How many customer are affacted by a an error or wifi strength. We need to have that data anonymized. This is behavioural data, but does it need to be forwarded? 

Might want to do monitoring and full journeys of customers?
Need a linkable id. Need to be anonymized but it can't link to cookiedoo customer. DCID is the link if we have consent. 

Want to have analytics even if they don't have consent. 

Legitimate interest you can upload that to the server. It will be complex on the device. If all data is classified to legitimate interest. If not we only use it for analytical use cases. 

In the past we only had collection if we had consent. If you remove the consent you remove the data we remove the mapping. Now it's mixed but only use it on personalization level. Still want linkability. 

google analytcis and usagebox was not linked. 
Explore if it possible to see full journey while still being compliant. Access only if it has consent. 

DCID identifies the customer. What they did on device and analytics. 

Tokenization is easier, which subscription do they need 
DCID to the email.
Create governance 

We need to see if the vault can be synchronized.  

---
### Notes created today
```dataview
LIST  
WHERE file.cday = this.file.day  
SORT file.time asc  
```

### Notes last touched today
```dataview
LIST  
WHERE file.mday = this.file.day  
SORT file.mtime asc  
```

