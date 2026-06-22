---
created: 2024-05-22 10:43
---
tags:: [[+Daily Notes]]

# Wednesday, May 22, 2024

<< [[2024-05-21-Tuesday|Yesterday]] | [[2024-05-23-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Vorwerk
	- [ ] Upload time reporting in Documents to Julian
	- [x] Write to Benedikt and see how loading testing can be performed ✅ 2024-05-22
		- [ ] Waiting
	- [x] Finalize DPO document ✅ 2024-05-22
	- [ ] Write feedback
	- [ ] Book recurring meeting Yevgen
		- [ ] Inform Yevgen about vacation
	- [ ] Book meeting Yevgen Mathias MDM
- [ ] DATA PRIVACY considerations 
	- [ ] RTBF across systems
	- [ ] Can we keep a deletion log for RTBF
	- [ ] Need to create a seggregation for use cases. What if you only can have access to part of the tokens although they're in the same column group? Do we need to add isolation? 
	- [ ] Pii in unity catalog - Create a [warning](https://medium.com/@andrewpweaver/identifying-and-tagging-pii-data-with-unity-catalog-870522f25730)
- [ ] Netlight 
	- [ ] Delete AWS databricks resources
	- [ ] Skriv till Laruenz DC Abdel och snacka om fortsatt format
	 - [ ] 2. Förebered LAF - Who to request feedback from and who to write to. 
	 - [ ] Skriv feedback Karolin!
	- [ ] Follow up with Josefin wellness
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
- [ ] Thoughts
	- [ ] Can we do quality checks too see that CDC works. For isntance hashnig a table?

---

# 📝 Notes


#scrapyard
Data Portability 

Tokenization supports data portability by providing a mechanism to represent sensitive data in a standardized and transferable format. Since tokens serve as references to the original data, users can easily transfer their data. By accurately tagging PII, we can facilitate seamless data exchange and interoperability while safeguarding user privacy and adhering to data protection regulations.

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

