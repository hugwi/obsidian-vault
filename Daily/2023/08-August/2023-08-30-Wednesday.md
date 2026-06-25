---
categories:
  - "[[Daily]]"
created: 2023-08-30 09:02
---
tags:: [[+Daily Notes]]

# Wednesday, August 30, 2023

<< [[2023-08-29-Tuesday|Yesterday]] | [[2023-08-31-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [?] pii scanner need to infer environment variables correctly - Open PR! 
	- NEED TO ADD SCAN_OUTPUT_INFO_TABLE_REFERENCE AND SAMPLE_RUN_INFO as well to terraform
- [?] Add environment variables to terraform! Open PR! ✅ 2023-08-30
- [ ] Bigstaging need to infer environment variables correctly
	- NEED TO ADD SCAN_OUTPUT_INFO_TABLE_REFERENCE AND SAMPLE_RUN_INFO as well to terraform
 - [ ] Read post filter PR
- [ ] Answer Kristoffer Advent - after lunch or in time
 - [ ] Don't have any context to what part in a findings that was PII

- [ ] Backlog
	- [ ] Investigate pubsub subscriber not pulling all messages 
		- Add some logging and debugger
		 - Same problem for deployed version? 
	- [ ] Add task_count and parallelism as environment variables
	- [ ] Write Summary from Sebastian
	- [ ] Missing from datahub but discovered in the unnesting v135-4542-pricing-cockpit-prod.ad_hoc.20230522_mw_BHT
	- [ ] Fix logging so it's logging in the correct place scan.py line 227. The start time should probably be different.
	- [ ] Follow up on gcp certifications document
	- [ ] Field information is empty. 
	- [ ] React on logs?
	- [ ] Add pii table reference in terraform 
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

