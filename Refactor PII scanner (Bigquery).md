---
categories:
  - "[[Projects]]"
project: "[[PII]]"
created: 2026-06-23
---
#bigquery
#pii


# Roadmap

## Validation set 

Can't be used like a machine learning dataset since it works in different way. 
In machine learning you have labelled data where you usually can't predict all data correctly so you're trying to find the best "cut off"  and it's based on multiple features. We don't have multiple features (technically only one) and we don't have labelled data. 

- We don't have labelled data 
- Our prediction is as good as the test data we create (like creating a unit test)
- Should it be one column or mulitple? For example if we have it in a bucket instead. 
### Creating validation dataset 

Previous way of validating the predictions was to label one column and measure the accuracy by looking at if we was able to predict that column. The drawback with this is that if we find only one value we will label it correctly although we might still label other rows in that column incorrectly. We should rather look at each sample within a column we want to test.  

The dataset consist of different variations of the pii type which should be tested. It's rather the variations than the amount of data that is important. For example rather have two different variations of phone like +41 22 730 5989 and (+41) 22 730 5989 rather than 100 examples similar to one of them. 

We can however use some of the email and phone numbers that are already in the customer data like in `v1354451-olm-histo.thor_customer_order_historization.customer_order_thor_raw_data_v2`.


### Updating dataset
- The dataset is extended each time we find a false positives to decrease number of false positives.
- The dataset is extended each time we miss PII that should be captured

### Continuous validation of the PII scanner

The PII scanner is automatically validated each time a PR is created and evaluate the PII scanner. The scanner should predict the expected outcome defined in the validation dataset.
Rather than calculating accuracy we define a test that should capture all pii data we defined in the validation dataset and not capture the data that is in the non-pii validation set

## Replacing the current implementation with SQL
### Reason for replacing the current logic 
 - Faster to iterate  
 - Correctness? 

---
### Bigquery Regex

Are there any limitations with the regex? There are no lookahead and lookbehind
Would need to see if there are 

For instance if one would like to exclude info then it can be added to the regular expression  like  `(?i)(?!info@)`, which is a negative lookahead assertion that checks if the email address does not start with "info@". If it does start with "info@", the regex will fail to match the email address. Otherwise, it will proceed to match the rest of the email address as before.

However this is not possible since BQ use [re2](https://github.com/google/re2/wiki/Syntax) regex which is a strictly linear regular expression.  

---


### Included in the new POC

#### Included fields
First Name , Last Name , email addresses , phone nr 
location? 
Should first and last name be included? 

#### Quality of predictions
What's the expectation of the prediction for each field? A lot of time was spent refining the predictions? 
Can we scope some part down to for example only detecting german phone number? German addresses?   

#### Reading each field or an entire row
We loose context when reading just one column

Should the methods be compared? 
+ What are the outcome of changing? Should it be a proof of concept?

#### Need to be moved to the new scanner (some can probably be moved)
**Filters** 
- field_names.csv
- colors.csv
- words.csv
- phrases.csv
- abbreviations.csv

#### Additional info

Need to have a good way of working together.
Focus on one PII type and see how fast you can get on the results. 

Can start on email addresses cause they work quite well. How fast can we iterate it on. 
Phone number: Can try to do all.  





#### Email extraction


#### Indentification 

Still https is incorrectly classified as PII aso_search[].screenshots[].full: 
```
https://is4-ssl.mzstatic.com/image/thumb/PurpleSource125/v4/da/55/2c/da552c0e-431d-581b-dd84-2d6704de2880/ef49255e-fa42-477f-808f-69670e344df5_Walkthrough@2x.jpg/1242x2688.png
```

`autoreply+33360@appfollow.io` - should this be classified? 


Should we exclude or not? `notify.on.marketplace.spec.511543986.e2e@mail.co`
This have notify, marketplace and e2e which we all exclude: 


We detect data which has PII that is example data. customer@e2e.test.com

Should we exclude
`da-concepts-dev.monitoring_dev.cloudaudit_googleapis_com_data_access`

False positive  `product.features_aggregated`
Information about products. Need to refine the regex - MP@L4.1
Ja----Unterstützte Videoformate->MPEG-4.10 H.264/AVC (MP@L4.1, HP@L4.0), MPEG-4.2 SP/ASP (z. B. Xvid bis simple@L3)----Fingerprintsensor->Ja----Touchpad->Ja mit Fingerprint-Sensor----Speicherkartenformat->Micro-SDHC----Speicherkartenformat->Micro-SDXC----Speicherkartenformat->Micro-SD----Kartenleser->Ja----Kensington Lock Vorrichtung->Ja----Betriebssystem->Windows 10 Home in S Modus----Tastaturbelegung->QWERTZ----

Some emails are not valid. Could use a python package to verifty email
This package seems to be good to validate email `pip install email-validator`

CAN USE REMOTE FUNCTIONS to validate email or to check if emails contain customer information. 

Correct should classify ip addreses `android@101.0.4951.41`

```python
EmailSyntaxError: The part after the @-sign is not valid. It is not within a valid top-level domain.

In [40]: inp = "android@101.0.4951.41"

```


This is valid email address but not valid domain? `1119@es.mm.com`

HTML
`www.mediamarkt.gr/el/product/_russell-hobbs-cook@home-multi-cooker-21850-1161944.html`

`mediamarkt.pl/check_email?email=...@gmail.com` 


When adding remote function to validate valid emails 1665 out of 4592 0.36 % is invalid emails. 

Valid characters of email: 
https://www.jochentopf.com/email/chars.html

/ and = are actually valid, but one might opt for something easier since for example = often is used by some mailing list servers to generate special addresses for detecting bounces.
/check_email?email=...@op.pl

Is this PII? `mms-ism-staging-d-ddev.dev_staging_itsm_cherwell.t_raw_changerequest`
#### Phone extraction 

We consider it a high confidence when it has either moible, phone, contact, kontakt, tel, value close to where we find the phone. 

```
`WHERE`
  `phone` `IS` `TRUE`
  `AND` `(` `ABS``(pos_phone_extracted - pos_mobile) >= 15`
    `OR` `ABS``(pos_phone_extracted - pos_phone) >= 15`
    `OR` `ABS``(pos_phone_extracted - pos_contact) >= 15`
    `OR` `ABS``(pos_phone_extracted - pos_kontakt) >= 15`
    `OR` `ABS``(pos_phone_extracted - pos_tel) >= 15`
    `OR` `ABS``(pos_phone_extracted - pos_value) >= 15 )`
  `AND` `( pos_mobile > 0`
    `OR` `pos_phone > 0`
    `OR` `pos_contact > 0`
    `OR` `pos_kontakt > 0`
    `OR` `pos_tel > 0 )`
```


When testing Dieter's Regex
649985278 out of 1,007,508,894 false classifications

--- 
#### Confidence base predictions


Combine how many percentage is PII, if any PII information is contained in the schema.

It seems that it can contain PII still. For instance we only have 3 samples of biib-analytics.BDI.returns_january but it has a lot of  PII! It's also shown in the schema though.  Some small tables have email but  is then also called something with email
#### Observations

- It seems like if we have tables with a high percentage of PII it's likey is PII. 
- We sometimes filter fake data which is often an indication of PII in prod table
For instance marketplace.420c8b14-a0d6-467a-b2ac-8d044effb6a8.e2e@mail.com and notify.on.marketplace.spec.511543581.e2e@mail.com, and e2e.test@...com are all fake emails but they're indicating that the production table is PII. Should there be rule on dev vs prod tables?  The same with no@e.mail for `DLVRY_CUST_EMAIL` table `e200-5304-biib-dataform-prod.sources.tbl_voucher_es_pt`.


From: (Debitoren-Postfach) debitoren@proreserv.de Sehr geehrte Damen und Herren, zu der im Betreff genannten Rechnung erhalten Sie anbei die aktuelle Mahnung sowie den dazugehörigen Vorgang. Betrifft Ihre Case Nummer 1018558. Wir bitten um zeitnahe Bearbeitung. Für etwaige Rückfragen stehen wir I...



## Check names of fields like
email
description
employee 
cust


Interesting article using machine learning but also clustering PII https://medium.com/cape-ai-stories/case-study-using-machine-learning-to-classify-personally-identifiable-data-fields-6b9c5b0743e7


Generate fake data with faker 
```
The following code is an example of how to generate custom PII by using Faker, and shows the data generation process for custom PIIs. The generated custom PIIs can be used to create a sentence that includes all of the relevant information. Then, you can use this sentence to fine-tune the model.
```
https://developer.ibm.com/tutorials/pii-extraction-using-fine-tuned-models/

--- 
#### Next steps 
- Add confidence to classifications
	- Combine how many percentage is PII, if any PII information is contained in the schema.
	- (Optional: Can check if there are one value occurring multiple times (then it's probably test)
- Check if it has low PII, what does that mean? 
- Can we use the size of the table as a confidence computation? Maybe if it's really small it doesn't contain PII? 
	- It seems that it can contain PII still. For instance we only have 3 samples of biib-analytics.BDI.returns_january but it has a lot of  PII! It's also shown in the schema though.  Some small tables have email but  is then also called something with email
- Should we exclude mms account? 
- We can probably say that even it has any PII, like phone, email, customer, it's more likely that it contain any PII. Question is which step we'll do it. 
- Can use vertex AI for spacy to detect person data and invoke it from BigQuery.


###### 19 Sept
By validate_emails we can reduce the lower confidence emails from 791 columns to 117. We can see that for medium and high confidence the valid emails are higher.  

![[Pasted image 20230919161539.png]]


It takes 3 min 24 sec to go through 183.37 GB so that's feasible imo.