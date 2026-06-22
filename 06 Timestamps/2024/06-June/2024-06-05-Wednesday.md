---
created: 2024-06-05 09:18
---
tags:: [[+Daily Notes]]

# Wednesday, June 05, 2024

<< [[2024-06-04-Tuesday|Yesterday]] | [[2024-06-06-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Vorwerk
	- [ ] Need to add checks to see that we're not caching calls to udf
	- [ ] What happens if we create the token at the same time as we reuse it? I suppose we only create one since we're deduplicating?
	- [ ] Prepare material for setting up meeting with vendors. What do we need to know? Ask Yevgen
	- [ ] Follow up with DPO
	- [ ] Check with V if we need to have serial number. Othwerise we might skio the conversatoin for how to hadnle it
		- [ ] Look into column and row level security
	- [ ] Make an example for determinsitc tokens
	- [ ] Show PIIano sandbox
- [ ] Waiting
- [ ] Netlight 
	- [ ] Write about data meeetup on Tuesday
	- [ ] Write feedback Karolin
	- [x] Kolla möte med Gustav mentor ✅ 2024-06-04
	- [ ] Delete AWS databricks resources
- [ ] DATA PRIVACY considerations 
	- [ ] RTBF across systems
	- [ ] Can we keep a deletion log for RTBF
	- [ ] Need to create a seggregation for use cases. What if you only can have access to part of the tokens although they're in the same column group? Do we need to add isolation? 
	- [ ] Pii in unity catalog - Create a [warning](https://medium.com/@andrewpweaver/identifying-and-tagging-pii-data-with-unity-catalog-870522f25730)
- [ ] Personal
 - [ ] Backlog
	 - [ ] Keep in mind to replace with token and not delete
	- [ ] What happens if a value for a customer is updated? How should it behave?
		- [ ] Data access concepts
		- How is PII accessed? Do we need to have more fine grained access rules? 
	- [ ] Compare synchronization vs isolation
	- [ ] Write about data governance initiative - check with Michael
	- [ ] What happens if we have id from different sources
	- [ ] Watch [gen ai talk](https://netlight365beta-my.sharepoint.com/personal/raku_netlight_com/_layouts/15/stream.aspx?id=%2Fpersonal%2Fraku%5Fnetlight%5Fcom%2FDocuments%2FRecordings%2FArchitecting%20LLM%2Dpowered%20applications%5F%20A%20practical%20guide%2D20231207%5F180207%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview&ga=1)

---

# 📝 Notes
- 

Needed for first join
- token scope = "email"
- Deterministic = True

Needed for generation
- token scope = "email"
- Deterministic = True
- pii type = email
- anonymizer = uuid()



--- 
#bartosz

10-20 k records

#prolongation
We have one data model in Datahub is being the same model since we created Datahub. Based on the previous systems that managed subscriptions. We migrated subscriptions in Cookiedoo whih intrpduced different ocnccepts memebership subscroptions orders and cookiedoo business model changes different sub tiers different prices. The way we manage the journey, which trial, when they convert to the to another sub. We're facing data quality issues from the way we're sourcing data. Wanted external view, collection of data, modelling the data. Someone that has clean view of it and don't want bias model. Review the pipelines and suggest outcome. See what's feasible. Different way of ingesting the data 

Ask if it's problem if it comes from Germany. 
Development team is based Germany. 
Worst case it can be in Yevgen. 


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

