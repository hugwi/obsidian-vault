---
created: 2023-06-28 09:39
---
tags:: [[+Daily Notes]]

# Wednesday, June 28, 2023

<< [[2023-06-27-Tuesday|Yesterday]] | [[2023-06-29-Thursday|Tomorrow]] >>

---

# 🔥 Todo 
- [ ] Verify PII glossary terms work
	- [/] Fix casing when matching fields
	- [/]  Temporary tables should be excluded
	- [ ] When fixing the filtering of temporary tables I noticed an error. We're comparing string with dates. Seems to be related to latest change of int overflow.. 
- [ ] Add pii table reference in terraform 
- [ ] Sharded table need to have the same notation as datahub table_20120410 -> table. Need to change in domains/owners as well as when writing pii results.
- [ ] Answer Nicolas (and message him that I'm free now?)
- [ ] Prepare CV
- [ ] Backlog
	 - [ ] Need to make sure to create a run_id since we can't deduplicate otherwise
	- [ ] Missing from datahub but discovered in the unnesting v135-4542-pricing-cockpit-prod.ad_hoc.20230522_mw_BHT
	 - [x] Follow up with Pasha about the alp table duplication ✅ 2023-06-20
	- [ ] Fix logging so it's logging in the correct place scan.py line 227. The start time should probably be different.
	- [ ] Use chatpgpt to identify false positives

---

# 📝 Notes

PII Improvement meeting 

Exclude service account

Good morning again! ![🙂](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/smile/default/60_f.png?v=v82)

I tried to gave the additional parts some priorisation, and if this is okay, I would create also Stories for these. If you see other priorities, let me know. But, here - with highest priority on top and at the moment skipping some aspects from above, which I think have lower priority:

Speed Optimisation

- refactor: Scanner: Sending out Batch of fields to PubSub instead of full table reference (++) (just on top, as we pulled it to the sprint already)

Update on Detectors

- refactor: Exclusion of additional special names ("Best", ...) (++)
- refactor: Detector: Exclusion of Service Account Emails and special URLs (@sometext.html), potentially also "no-reply" and general - "kontakt, info, dpo, atencionalcliente, centrala... " - mms mail addresses) (++)
- refactor: Detector: Street Name detection (Special check for Mannheim ;-)) improvement (++)
- feat: Detector : Gather and cross check detection on Shop/Market address information (++)
- refactor: Field Name Detection even if fields are "empty" / missing (++)
- feat: Post-Filtering Hierarchy of Findings: If only country, if only phone number, ... vs. email, country + city + street (++)

External Requests

- Gathering informations from the scanner for IQI/Data Excellence Interviews (++)
- Additional Detectors as requested by Privacy (++)

Infra Updates

- Delta/Update logic if new fields (++)
- feat: Terraform: New GCP roles for developers instead of Owner/Editor (++)
- If not done already: Datahub deletion mechanism for wrongfully classified or removed fields (+)
- feat: Unnesting/Scanner: Sink for Logs (+)

Docs & Tests

- docs: Confluence: Update Documentation (++)
- feat: Tests: Prioritised intermediate Acceptance / Result tests (and potential other tests). next to unit tests and general clean code ideas. (++)

External Request

- PoC: Other source with existing Connector (=> Might render the current BQ based field name lookup irrelevant or at least bring it's quality down to some extent, if not adapted)(++)

Speed Optimisation

- feat/refactor: Unnesting potentially: Separation of Unnesting and Writing (+)

External Request

- Potential Dashboard (+) 

Update on Detectors

- Iso Country Abbreviations ("DE", "TR", ...) (+)
- Inclusion of Additional field names =>  generally more desk research on potential names
---
Fix alp_table_data to have dataset_default_expiration_time has nullable int.

Majority of columns is having "None"
"dataset_default_expiration_time": "None", "cnt": "63757"

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

