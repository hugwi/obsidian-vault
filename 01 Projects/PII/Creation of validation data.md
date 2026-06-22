

- Create synthesized data
- Create snapshots of real data
- Need to be able to run on all but only for one pii type


Takes a long time to go through all the data and create tests for false positives

Questions: 
How to handle shop in domain, top level and username? 
master is ecxluded but shouldn't be
mm.com shouldn't be excluded for instance office@hellsklamm.com is PII
Don't think notify should be excluded
abuse and NO are valid emails


emails from 
Include in emails
.html'
- [x] '.gserviceaccount.com' 
 'noreply@newsletter.mediamarktsaturn.com'
 'd{3, }@es.mm.com' 
 'ios@d{1, 5}.d{1, 5}.d{1, 5}.d{1,10}'
 'android@d{1,5}.d{1,5}.d{1,5}.d{1,10}'
 'datenschutz@mediamarktsaturn.com'
 'events@mediamarktsaturn.com'
 'info@mediamarktsaturn.com'
 'jobs@mediamarktsaturn.com'
 'msits.so.spm@mediamarktsaturn.com'
 'modernworkplace@mediamarktsaturn.com'
 'sustainability@mediamarktsaturn.com'
 '.info@mediamarkt.be'
 '.webshop@mediamarkt.be'
 'kontakt@mediamarkt.de'
'kundenservice@mediamarkt.at'
'kundendienst@mediamarkt.ch'
'atencioncliente@mediamarkt.es'
'mmstopshop@mediamarkt.hu'
'^mm[a-z]{1,25}@mediamarkt.hu' when should we ignore this ?
'dummy@mediaworld.it'
'servizioclientimediaworld@mediaworld.it'
'contact@mediamarkt.nl'
'noreply@mediamarkt.nl'
'musterihizmetleri@mediamarkt.com.tr'
'musteri.hizmetleri@mediamarkt.com.tr'



#### How do we maintain the tables?  

We keep snapshot of original data (maybe not all) and then the rest can be created on demand. 

We could have both CTEs and real tables depend on if we use Dataform.
In Dataform it's simple to create tables per user so they don't conflict with each other. 

~~Can we use 
```
FOR SYSTEM_TIME AS OF JOB_START_TIMESTAMP
```
to maintain snapshots? 

#### Preventing data drift
We need to make sure that our performance doesn't worsen because unintentional data drift. This could for example be that one of the real tables that we're querying updates their data. To avoid this we need to create a export of the data and an additional snapshot to prevent us from data loss. 


#### Potential additional real data source

```
v1354451-olm-histo.thor_customer_order_historization.customer_order_thor_raw_data_v2
v135-6228-datafoundation.olm.data
xpay-histo.thor_payment_historization.data
v1354451-olm-histo.thor_customer_order_historization.customer_order_thor_raw_data_v2
```

`cos-histo.thor_cos_v3_prod_historization.data_cluster`
`feed-composition-prod.export_temp.temp_outlet_MM_20230523_02_12_19_MEDIAES` email

https://huggingface.co/datasets/beki/privy

#### Is verifying data easy enough?

We need to add the code for verifying the output data. Can of course be done automatically by Dataform. 

### TODO 

- [ ] Is verifying data easy enough?
- [ ] NEED TO ADD PII FOR DIFFERENT FORMATS
- [ ] Create snapshots of real data
- [ ] We need to have different input and output table. The first one need to be same as sampled data and the output must be the expected output
- [x] Decrease permissions for service account ✅ 2023-09-13
example
{"country":"DE","THOR_DATAFLOW_TIMESTAMP":"2023-03-12T17:22:15.389Z","source_system":{"channel":"MOBILE","id":"","type":"XCC"},"kind":"CUSTOMER_ORDER","created_at":"2015-09-23T18:41:49Z","language":"DE","billing_address":{"address_components":[{"firstname":"Lena","salutation":"MS","type":"addressee_...
}


We want to distinguish between test for extracting email and test for if a email has pii. 

In one case we only need to test if it extract email or not. In the other we should verify if a column has pii or not! In that case we might need to have check for the number of percentage of PII for example. 


---

#### Data validation documentation 

Different cases of testing:
- The one that's like a unit test which will be smaller and quick to iterate on. These can be for a specific pii_type for example  
- Bigger one that's more like an end to end test for the entire PII scanning which will be on column level (can also be for row level maybe?) 

We'll have one script which created the validation data



---
#### Formats 

**Error messages** 
Error while importing: [{'index': 992, 'errors': [{'reason': 'invalid', 'location': 'date_of_l

**Long list**
[0.03455032149460496, 0.011270248640891906,.... ]

**Json**  
{"busObId": "934ec7a1701c451ce57f2c43bfbbe2e46fe4843f81"}

**html** 
```
<Track><trackNo>1</trackNo><title>1. Präludium ( 1. Akt)</title><artist></artist> <Track><trackNo>1</trackNo><title>1. Präludium ( 1. Akt)</title><artist></artist><playPeriod>223</playPeriod><mediaUrl>http:
```

**yaml** 
```
openapi: 3.0.0  
info:  
title: customers  
description: Cloud-CCR Customers (B2C) API  
# Never forget to update the version in README.md
```

**schemas** 
from mms-ssr-dev.table_similarity_score.t_alp_table_data_20230331 and mms-dac-monitoring-bq-d-data.alp_data.t_pii_input_data

```
SchemaField('id', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('kind',
```

List from table similarty containing list


**Number** 
```
2458536----2553022----2555091----2555001----2555307----2458746----2298095----2554401----2458441----2555750----2555613----2295595----2556667
```
table: feed-composition-prod.data_quality.debug_online_delta_MEDIADE

**Bytes** 
```
b'{\x00"\x00s\x00a\x00l\x00e\x00s\x00l\x00i\x00n\x00e\x00"\x00:\x00"\x00M\x00e\x00d\x00
```

**Uknown format**
Table: at-tableau-dev.metadata_staging.reporting_metadata
format:
```
avg basket value per member to (selected period to compare),# avg baskets per member all mem to (target month pre month),# avg baskets per member all mem to (target month pre year),# avg baskets per member to (selected period to compare),# avg baskets per member to (target month pre month),# avg baskets per member to (target month pre
```

table: v105-3114-sales-assistant-hist.06_analytics_co.co_data

format:
```
WAITING_STOCK>AWAITING_STOCK>AWAITING_STOCK>BACKORDERED>AWAITING_STOCK>BACKORDERED>AWAITING_STOCK>BACKORDER
```

----
#### Questions

- Should we maintain is detection for emails containing äåö 
- Should we include Dataform? Can we skip taking a decision on that for now until Dieter comes back.  
- Quite often we have fake emails but they usually occurs in columns with PII data. 
- How much data can we process everytime? 


## Creation of validation set

The validation set consist of two types of PII data:

- PII data such as email and phone number
- Non PII data

To avoid false positives, predict that a certain value is PII when in reality it isn't, we need to include not only PII data but also data that isn't PII.

Furthermore the PII data is comprised of both manually created PII data as well as real PII data. The manually created data is important to create to ensure that PII can be detected for a lot of different formats of data (json, html, body text) and variations of a certain PII type.

  

  

![Creation of validation set](https://confluence.media-saturn.com/download/attachments/465082949/Blank%20Diagram%20-%20QfYgcSsWD-u_%20-%20Page%201.png?version=1&modificationDate=1694781711898&api=v2 "Creation of validation set")

  

The dataset will be continously be updated as new edge cases are discovered.

## Validating PII classifications

When a validation set has been created it can iteratively be used to validate that any change to the PII scanning logic doesn't create new incorrect classifcations. Each time a PII scan is run, the second step will be to validate its predictions with the PII validation set which contains the expected output of the scan. Similar to evaluating expected outcome of a function in a unit test, the result of the scanner should match the expected outcome defined in the validation set.

![](https://confluence.media-saturn.com/download/attachments/465082949/Blank%20Diagram%20-%20QfYgcSsWD-u_%20-%20Page%201%283%29.png?version=1&modificationDate=1694782484943&api=v2)

  

If the result isn't matching the validation set the difference is presented otherwise the result will be empty.  

  

**False positives**: In this case we're incorrectly classifying a value which isn't PII as PII. This can for example be predicting a invalid emails such as username@.com as an email.  
  
**False negatives:** In this case we fail to classify a value which is PII, for example classifying the valid phone number 0046730520561 as a phone number.

**No misclassifications:** All PII was correctly classified and no data is presented during evaluation (since there were no incorrect classifcations)  
  

![](https://confluence.media-saturn.com/download/attachments/465082949/Blank%20Diagram%20-%20QfYgcSsWD-u_%20-%20Page%201%282%29.png?version=1&modificationDate=1694782484737&api=v2)

## Unit test and end to end tests of PII scanner

  
To ensure the quality of the PII scanning service both unit test and end to end test are performed.

### Unit test

The unit tests are the first validation of the PII classifications. In order to enable quick iterations on the transformations, the tests should be a smaller subset of the validation dataset mosly existing of manually created data.

### End-to-end Test

An end-to-end test should also be performed for all PII types and the full validation dataset to include real data and is a more extensive test. This test will be performed as a last evaluation when PRs are opened.

  

![](https://confluence.media-saturn.com/download/attachments/465082949/Blank%20Diagram%20-%20QfYgcSsWD-u_%20-%20Page%201%286%29.png?version=1&modificationDate=1694796719894&api=v2)





#### Test Data vs Validation Data

Who should be responsible for creating the labelled PII data? 

If external, do we have resources for that and where should they get the data? 
How much extra time does that have? 

What's our biggest problem at the moment preventing us to use the detections? 

If false positives?  Is creating the test dataset the way to go? How much time will it take? What deadline do we have? 
