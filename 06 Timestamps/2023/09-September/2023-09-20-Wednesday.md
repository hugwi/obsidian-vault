---
created: 2023-09-20 13:09
---
tags:: [[+Daily Notes]]

# Wednesday, September 20, 2023

<< [[2023-09-19-Tuesday|Yesterday]] | [[2023-09-21-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [x] Read Thorstens PR ✅ 2023-09-20
	- [x] Update requirements ✅ 2023-09-20
	- [x] New filter words? ✅ 2023-09-20
- [x] Book Meeting with Lea ✅ 2023-09-20

- [ ] Create data validation
	- ~~Complete documentation for data validation~ 
	 - [x] Add real phone numbers to test validation set ✅ 2023-09-20
	- [ ]  Open PR to create data validation set
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

#setuptools #vulnerability
Yeah, that's true. I don't think we need to upgrade this since we doesn't use this package though and it's a _Inefficient Regular Expression Complexity_ which consumes excessive CPU cycles.

So if that would be used for validating for example emails that could be a problem. However since we're not using setuptools I think we don't need to update it and should rather ignore the report. 

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

