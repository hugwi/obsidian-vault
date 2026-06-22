---
created: 2023-07-05 09:08
---
tags:: [[+Daily Notes]]

# Wednesday, July 05, 2023

<< [[2023-07-04-Tuesday|Yesterday]] | [[2023-07-06-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [x] Remind Dieter about the MMS event ✅ 2023-07-05
 - [ ] Fix shards - Sharded table need to have the same notation as datahub table_20120410 -> table. Need to change in domains/owners as well as when writing pii results.
- [ ] Add pii table reference in terraform 
- [ ] Field information is empty. 
- [ ] Create a task for improving processing time


After lunch
- [x] Register for the mms event (@2023-07-05 13:10)
- [ ] Connect with Pradeep on linkedin and ask how everything is going and if he'd like to schedule a meeting with MMS
- [x] Meeting with Jonas (@2023-06-06 09:13) ✅ 2023-07-05

- [ ] Backlog
	- [ ] React on logs?
	- [ ] Create a prod project for alp table
	- [ ] Prepare CV
	 - [ ] Need to make sure to create a run_id since we can't deduplicate otherwise
	- [ ] Missing from datahub but discovered in the unnesting v135-4542-pricing-cockpit-prod.ad_hoc.20230522_mw_BHT
	 - [x] Follow up with Pasha about the alp table duplication ✅ 2023-06-20
	- [ ] Fix logging so it's logging in the correct place scan.py line 227. The start time should probably be different.
	- [ ] Use chatpgpt to identify false positives

---

# 📝 Notes

**Refinement** #refinement

- Create run_id since we can't deduplicate otherwise for sampling table and pii
- Discovery: How to easier validate our ingestion? Especially aspects like domain, owners. Should we react if that number drops significantly for example? 
- Can we ensure that the run time has been decreased? 
- Create test/prod table for alp? 


#issue-sharded-table
For every row that coming from a shards we query once again. Then we update 

Change SHARDED_TABLE_REGEX to be the same as Datahub use. 

This way we will have the same representation of shards as they have as
well as this regex also retrieves the 


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

