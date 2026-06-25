---
categories:
  - "[[Daily]]"
created: 2023-07-26 11:19
---
tags:: [[+Daily Notes]]

# Wednesday, July 26, 2023

<< [[2023-07-25-Tuesday|Yesterday]] | [[2023-07-27-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
 - [ ] Fix shards - Fix review comments
	 - [<] First PR for domains and data owners in Review
	 - [x] PR for adding PII ✅ 2023-07-21
			- [ ] Write Summary from Sebastian
- [ ] Format with black
	- [/] [  ] Pull request for push-ingestion
	- [ ] Pull request for bigstaging - depend on open PR
	- [ ] Pull request for PII Thorsten
	- [ ] Review Thorstens PR
- [ ] Long processing time
	- [ ] Lower the amount of time we retry pulling since its adds up quite quickly.
 - [ ] Read Thorstens PR:  Field Name Filter type update https://github.com/MediaMarktSaturn/ANASE-pii-detector/pull/40
- [ ] Backlog
- [ ] Format all repos (see if branching works)
- [x] Update repos for with black Monday (@2023-07-24 09:20)
- [x] Follow up on way of identifying shards google team (@2023-07-31 09:20)
	- [ ] Check elasticsearch performance
	- [ ] Field information is empty. 
	- [ ] React on logs?
	- [ ] Prepare CV
	- [ ] Add pii table reference in terraform 
	 - [ ] Need to make sure to create a run_id since we can't deduplicate otherwise
	- [ ] Missing from datahub but discovered in the unnesting v135-4542-pricing-cockpit-prod.ad_hoc.20230522_mw_BHT
	 - [x] Follow up with Pasha about the alp table duplication ✅ 2023-06-20
	- [ ] Fix logging so it's logging in the correct place scan.py line 227. The start time should probably be different.
	- [ ] Use chatpgpt to identify false positives

---

# 📝 Notes

**Planning** 
Jan asking why we have so much unused tables. 

We have 5.2 PB which cost 87.565 euro per month 5.2 PB, cost is 0.02 dollar per GiB.

We don't have hard deadlines Dieter said to Thorsten when he asked what should be included for instance the IBAN detector.

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

