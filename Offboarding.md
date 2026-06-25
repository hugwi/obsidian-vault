---
categories:
  - "[[Areas]]"
domain: career
created: 2026-06-23
---



Limitations: 

To be aware of: 

- What's the implication of having the same value for two different PII column with the same PII type. -> They have the same toke
- [ ] Users that needs the package don't get automatic updates but need to manually update


Open Questions: 
- [ ] When dropping duplicates before merging could we have an edge case where we're not updating pi values.  
- [ ] What should the prefix for the different PIIColumns be
- [ ] Make sure that concurrent merges doesn't fail. Add a retry mechanism
- [ ] Should we use the poetry.lock file or not with poetry. Since it's not used when building a .whl file it might not be needed

- [ ] Optimization: Add partition


- [ ] TODO
	- [ ] at 514 we're doing a coalesce to return the token data if it's null. Add documentation on that.
	- [ ] When detokenizing and we have forgotten a user. We still have the tokenized data but can't deanonymize. How does this affect end consumers. Add a comment on why we coalesce. 
	- [ ] Add a note that we have a concurrent append exception that seems to be due to instability of Databricks. FML. 
	- [ ] 



Meaningful: Experience so far. This is what I've would do differently. Thing that would have been 


Solving the concurrent append:
https://docs.databricks.com/en/optimizations/isolation-level.html


Thoughts: 
- How can we involve them more? 
- Hard time getting them to attend


How should detokenize work if we deleted the token? 

Feedback  

- How can we involve them more?  
- Hard time getting them to attend


General impression is that Vorwerk is organisationally well structured and have a lot of good processes ingrained into the Vorwerk's working culture. For instance putting emphasise on ADR. 

One of the challenge during the project has been that a lot of decision needs to be made about the handling of personal data which needs input from a variety of people. 



Worked in an organised way
autonomous way 
gathering demand requriement
bulding a plan 
getting buy in 
start implementation 
attentive and listening
