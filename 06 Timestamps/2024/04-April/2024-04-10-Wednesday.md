---
created: 2024-04-10 11:30
---
tags:: [[+Daily Notes]]

# Wednesday, April 10, 2024

<< [[2024-04-09-Tuesday|Yesterday]] | [[2024-04-11-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Vorwerk
	- [ ] Sign NDA
	- [ ] Create access pattern for different data roles
	- [ ] Load testing
	- [x] Create a PII columns class ✅ 2024-04-11
	 - [ ] 2. Förebered LAF - Who to request feedback from and who to write to. 
- [ ] Netlight 
	- [x] 1. Book meeting with scout24 forwarded ✅ 2024-04-10
	- [ ]  Waiting for answer for Scout24
- [ ] Personal
 - [ ] Backlog
	- [ ] Skriv till Mathias för att fråga om tisdagen! Waiting resposne
	- [ ] Compare build vs buy
	- [ ] What happens if a value for a customer is updated? How should it behave?
	- [ ] Data access concepts
		- How is PII accessed? Do we need to have more fine grained access rules? 
	- [ ] Compare synchronization vs isolation
	- [ ] Write about data governance initiative - check with Michael
	- [ ] What happens if we have id from different sources
	- [ ] Watch [gen ai talk](https://netlight365beta-my.sharepoint.com/personal/raku_netlight_com/_layouts/15/stream.aspx?id=%2Fpersonal%2Fraku%5Fnetlight%5Fcom%2FDocuments%2FRecordings%2FArchitecting%20LLM%2Dpowered%20applications%5F%20A%20practical%20guide%2D20231207%5F180207%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview&ga=1)
- [ ] Thoughts
	- [ ] Can we do quality checks too see that CDC works. For isntance hashnig a table?

---

# 📝 Notes


{"pii_type": "entity_type", "type": "integer", "pii_policy": ["location/id"]}


    pii_columns = PIIColumnCollection(pii_columns=[PIIColumn(name="user_id",pii_type="ENTITY_IDENTIFIER"),PIIColumn(name="first_name",pii_type="FIRST_NAME")])


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

