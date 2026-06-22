---
created: 2023-09-13 10:07
---
tags:: [[+Daily Notes]]

# Wednesday, September 13, 2023

<< [[2023-09-12-Tuesday|Yesterday]] | [[2023-09-14-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Create data validation
- [x] Prepare a demo of Data vajlidation and remote functions ✅ 2023-09-14
After lunch 
- [ ] Plan for when to swim in isar. 
- [ ] Answer Nicolas regarding Swsscom
- [ ] Backlog
	- [ ] Netlight
		- [ ] Follow up on gcp certifications document
	 - [ ] PII
		- [ ] Add task for location
		- [!] Add task for automatically running the validation on a PR
		- [!] Need to add higher confidence but for instance looking at how many of one mail is occurring
		 - [ ] Don't have any context to what part in a findings that was PII
		- [ ] Could pubsub messges be trunacated due to size.  Some messages or columns were truncated due to size. To pull the full message, see this documentation
		- [ ] Add pii table reference in terraform 
	 - [ ] Datahub
		- [ ] Write Summary from Sebastian
		- [ ] React on logs?
		 - [ ] Need to make sure to create a run_id since we can't deduplicate otherwise
		- [ ] Use chatpgpt to identify false positives
- [ ] Question:
	 - [ ] How is the pubsub messages consumed. Can they consume more although porcessing a callback. Can the load be uneven so only one batch job consume the last messages.


---

# 📝 Notes
- 

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

