---
categories:
  - "[[Daily]]"
created: 2023-09-27 10:14
---
tags:: [[+Daily Notes]]

# Wednesday, September 27, 2023

<< [[2023-09-26-Tuesday|Yesterday]] | [[2023-09-28-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Hash out the details of validation/test dataset
- [ ] Output table
	- [ ] Define which fields should be excluded
		 - [ ] Should probably have confidence
	- [ ] First sketch on how the output table with look like
- [ ] Open PRs
	- [ ] Finalize the PR for emails regex
		- [x] Fix emails so we can see subset of them ✅ 2023-09-21
		- [x] Clean up Code and save as queries ✅ 2023-09-21
		- [ ] Document the changes for email
- [ ] prepare planning meeting for scope framework
	- [x] Meeting with Renee at 14 ✅ 2023-09-22
	- [x] Asked in Netlight ✅ 2023-09-21
- [ ] Netlight
	- [ ] Follow up on data-n-dumplings
	 - [ ] Fill in bahncard skovid
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
			- [ ] Suggest way of giving data access
			- [ ] Write Summary from Sebastian
		- [ ] React on logs?
		 - [ ] Need to make sure to create a run_id since we can't deduplicate otherwise
		- [ ] Use chatpgpt to identify false positives
- [ ] Question:
	 - [ ] How is the pubsub messages consumed. Can they consume more although porcessing a callback. Can the load be uneven so only one batch job consume the last messages.

---

# 📝 Notes

All tables can be copied
Scanner running on BigQuery approach
Want a mapping if cust is mentioned in the table name or description. Might get extended support so we don't need to do this mapping. 
Would be good to have the glossary term and a list and potential example to check on list. 
We need interconnect to connect to it
multiple tables - bring every table to bq as the same table. 

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

