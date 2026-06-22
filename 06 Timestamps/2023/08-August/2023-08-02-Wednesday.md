---
created: 2023-08-02 10:16
---
tags:: [[+Daily Notes]]

# Wednesday, August 02, 2023

<< [[2023-08-01-Tuesday|Yesterday]] | [[2023-08-03-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] PII names list need to be fixes since it has LOCAL RUN and will be read incorrectly by detector
- [ ] Follow up on security fix for sqlparse. Seems like they need to propagate it in the next release. 
- [ ] Fix spacy loading time
- [ ] Check borgstad answer regarding datahub
- [ ] Backlog
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

**Refinement** 

#neo4j
We have another node pool for neo4j. Doesn't seems so according to neo4j. 
Do we see some bottlenecks? 
How is the cpu when loading lineage? Xuelei has already optimized some when loading.

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

