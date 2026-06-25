---
categories:
  - "[[Projects]]"
project: "[[PII]]"
created: 2026-06-23
---
Can we create a roadmap for the epics? 
Should we have any priority? 

#### Dependecies:
Data Models, Table & Dataset Names and places, and Labels from [ANASE-598](https://jira.media-saturn.com/browse/ANASE-598) are defined

Dependency! Architecture is planned and setup in alignment with [ANASE-600](https://jira.media-saturn.com/browse/ANASE-600)

---

### Add Prefilter 
- Field Name Prefilter is Setup and Included (reuse PoC Code)
- Type check excluding int & float from values (New)
- General value preparations, like lowering strings or removing special characters (Teradata is based on ETL and might not be that messy) (New)
- Pre Value Filterings (1) (abbreviations, colors, phrases, other special words) are added to BigQuery at dedicated dataset / tables (New)
- Pre Value Filterings (2) (abbreviations, colors, phrases, other special words) are added to BigQuery to prefilter the values (New)

### Regex
- Add existing emails (2) 1 day 
- Add phone (8) - 4 days 
- Person Names (3) - 
- Streets: (5)
	- Extract street names of 12 more countries and store them at a dedicated place for this lookup (New)
	-  Adapt the street name detection for 13 Countries, test and include it (reuse PoC code, remainder is New)
- Citites ()
	-  Extract city / municipality names of 13 countries and store them at a dedicated place for this lookup (New)
	- Implement, test and include City SQL based detection (Might be similar to street names) (New)
	- Implement, test and include Value Prefilter on Locations maybe at the WHERE clause of the city detection (See for phrases the LocationValueFilter class in filters.py) (New)

- Create consolidated output of scanning on column level, in alignment with [ANASE-598](https://jira.media-saturn.com/browse/ANASE-598) (New)
- Postfiler 
- Check Quality on Test Data (reusing old 6 tables or test data set)


Need our own interconnect project
If you know what to do it should be pretty fast? 
It's terraform best - need to make a PR to terraform team. 