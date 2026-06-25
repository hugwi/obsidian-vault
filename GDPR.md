---
categories:
  - "[[Resources]]"
domain: compliance
created: 2026-06-23
---
# What data is PII and sensitive? 

Here are some examples of common personal data:  
- name,  
- address,  
- phone number,  
- email address,  
- IP address,  
- photos.  
  
Personal data can also be indirect. Here are some examples:  
- gender,  
- competences,  
- employment information,  
- education information,  
- written reviews.  
  
Finally, some personal data is sensitive, such as:  
- biometric data,  
- racial or ethnic origin,  
- sexual orientation,  
- religion,  
- medical information,  
- political opinions,  
- union membership.

# Anonymization rules

# Questions
- If you don't have consent for more that legitimate interest can you still store the data anonymized? 


https://www.gdprsummary.com/anonymization-and-gdpr/
Data anonymization is defined in an **ISO standard (ISO 29100:2011)** as:

> _“Process by which [personally identifiable information](https://www.gdprsummary.com/gdpr-definitions/personally-identifiable-information/) (PII) is irreversibly altered in such a way that a PII principal can no longer be identified directly or indirectly, either by the PII [controller](https://www.gdprsummary.com/gdpr-definitions/controller/) alone or in collaboration with any other party”_

**Official defintion**
The principles of data protection should therefore not apply to anonymous information, namely, information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the [data subject](https://www.gdprsummary.com/gdpr-definitions/data-subject/) is not or no longer identifiable

## Anonymization techniques
The first type of technique is **Randomisation** and this technique is build on the alteration of the data. The purpose is to cut the link between the individual and the data, without losing the value the controller has of the data. Therefore, this type of technique may be good to use when you do not need precise information for the processing. **Noise addition, permutation and differential privacy are techniques** that fall within the family of randomization techniques.

The second type is **Generalisation**, and the purpose of this technique is to reduce the granularity of data. Which will have the effect that you disclose lesser data regarding the data subject. By using this type of technique, it is less likely that an individual can be singled out. This technique can only work if you store multiple data subjects data together. For example, a database storing the ages of data subjects can be altered so only the band of ages the data subjects fall under is recorded (e.g. 18-25; 25-35; 35-45; etc.). Therefore, you would not be able to identify any of the specific data subjects. This technique will only work if you store so many **different persons in the database that it is impossible to single people out under each category.** The family of generalisation techniques include the techniques of aggregation and K-anonymity and L-diversity/T-closeness.

The last technique is **Masking** and this often works as a supplement to different anonymisation techniques. This technique builds on removing any obvious personal identifiers form the data. This could, for example, be a name, images and addresses. This technique will often not be enough for the data to be anonym. Therefore, often you need to use this technique together with one of the other techniques.
https://medium.com/golden-data/austrian-data-protection-authority-the-erasure-of-personal-data-is-also-possible-through-4e61b882e4ad

In its decision of 5 December 2018 ([DSB-D123.270/0009-DSB/2018](https://www.ris.bka.gv.at/Dokumente/Dsk/DSBT_20181205_DSB_D123_270_0009_DSB_2018_00/DSBT_20181205_DSB_D123_270_0009_DSB_2018_00.html), German), the Austrian Data Protection Authority (DPA) decided on an extremely relevant practical issue for the application of the GDPR. Is it sufficient for the erasure of personal data (and thus for the fulfillment of a data subject’s right to erasure under Article 17 (1) GDPR) for such data to be anonymized? The DPA’s assessment: the anonymization of personal data can in principle be a possible measure of deletion within the meaning of the GDPR.

The DPA rightly points out at the outset that the binding part of the GDPR does not define the term "anonymization". Only recital 26 GDPR mentions (but does not define) this and states that the GDPR does not apply to anonymized data, i.e. information "which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable."


Subsequently, the DPA deals with the definition of the term "processing" (Art. 4 №2 GDPR), in which, however, no definition of the term "erasure of personal data" (as used in Art. 17 (1) GDPR) can be found.

However, according to Art. 4 №2 GDPR, the DPA considers erasure and destruction to be alternative forms of processing ("erasure or destruction") which are not necessarily identical.

Consequently, deletion does not necessarily require final destruction. This clarification by the DPA is already the first important statement of the decision. Erasure does not mean that data must actually be destroyed.

In the opinion of the DPA, the controller is entitled to make a selection of the measures (i.e. the manner in which the data will be erased).

The removal of the personal reference ("anonymization") of personal data can thus in principle be a possible means of erasure within the meaning of Art. 4 №2 GDPR in conjunction with Art. 17 (1) GDPR.

However, in my opinion, the DPA rightly demands, that it must be ensured that neither the controller himself nor a third party can restore a personal reference without disproportionate effort. When such a disproportionate effort can be assumed is, of course, always an individual question in the end. Only if the controller aggregates the data on one level, so that no individual information can be identified, the resulting database, in the opinion of the DPA, can be described as anonymous (i.e. without personal reference) (in this regard, the DPA also refers to Statement 5/2014 by the former Art. 29 Data Protection Working Party).

In the present case, in the opinion of the DPA, the company has "partly destroyed (i.e. without "leaving" anonymous data), partly "erased" by removing the personal reference to the complainant.

In the opinion of the DPA, this combination of destruction and removal of the personal reference (also by replacing it with dummy data) is sufficient to be able to assume erasure in the sense of the GDPR.

In the end, the DPA refers to another important aspect: hypothetical developments, in particular, the further development of the technology, do not have to change anything about the result. The complainant argued that "the data could be "de-anonymized"" at a later stage. In the view of the DPA, erasure occurs when the processing and use of a data subject's personal data are no longer possible. The fact that a reconstruction (e.g. by using new technical aids) proves possible at any time does not make the erasure insufficient. Complete irreversibility is therefore not necessary, regardless of the means used.

---
https://edps.europa.eu/system/files/2021-04/21-04-27_aepd-edps_anonymisation_en_5.pdf

A robust anonymisation process aims to
reduce the re-identification risk below
a certain threshold. Such threshold will
depend on several factors such as the
existing mitigation controls (none in the
context of public disclosure), the impact
on individuals’ privacy in the event of re-
identification, the motives and the capacity
of an attacker to re-identify the data1 

**Data minimisation Principle**: 
The “data minimisation” principle requires
the controller to determine if it is necessary
to process personal data in order to fulfil a
particular purpose, or if that purpose can
also be achieved with anonymous data


https://www.gdprsummary.com/anonymization-and-gdpr/

Processing personal data for the purpose to anonymize the data is still processing that must have a [legal basis](https://www.gdprsummary.com/gdpr-definitions/legal-basis/) under [Article 6](https://www.gdprsummary.com/gdpr-definitions/article-6/). The anonymization process is what is known as “further processing”. As such the new processing must be compliant with the principle of purpose limitation.


### Legitimate interest
https://www.gdprsummary.com/gdpr-definitions/legitimate-interest/
An example of an area where legitimate interest most often are used to motivate the processing is when the [personal data](https://www.gdprsummary.com/gdpr-definitions/personal-data/) are being processed for certain marketing purposes, internal security and fraud prevention, administration of staff etc.

It is worth to note that public authorities can not use legitimate interest for processing that is carried out in the performance of their tasks.

Most often, the legal basis of the controller’s/[processor](https://www.gdprsummary.com/gdpr-definitions/processor/)’s fulfiling contract or [legitimate interest](https://www.gdprsummary.com/gdpr-definitions/legitimate-interest/) will apply, if the principles of collection, purpose, [retention](https://www.gdprsummary.com/gdpr-definitions/retention/) have been complied with.

https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/when-can-we-rely-on-legitimate-interests/#legitimate_appropriate

Legitimate interests is the most flexible of the six lawful bases. It is not focused on a particular purpose and therefore gives you more scope to potentially rely on it in many different circumstances.

It may be the most appropriate basis when:

- the processing is not required by law but is of a clear benefit to you or others;
- there’s a limited privacy impact on the individual;
- the individual should reasonably expect you to use their data in that way; and
- you cannot, or do not want to, give the individual full upfront control (ie consent) or bother them with disruptive consent requests when they are unlikely to object to the processing.

There may also be occasions when you have a compelling justification for the processing which may mean that a more intrusive impact on the individual can be warranted. However in such cases you need to ensure that you can demonstrate that any impact is justified.

The legitimate interests basis is likely to be most useful where there is either a minimal impact on the individual, or else a compelling justification for the processing.

## Can we use it as the default basis for all of our processing?

No. Although legitimate interests is a flexible concept and will often be relevant, it does not apply to everything and you are not be able to use it as the default basis for all your processing.

None of the lawful bases take precedence over the others, and you should always use the one that is most appropriate to the circumstances having considered the purpose of the processing.

You should carefully consider whether legitimate interests is the appropriate lawful basis for the particular processing operation. You should not look to rely on it simply because it may initially seem easier to apply than other lawful bases. It is not always the easiest option, and in fact places more responsibility on you to justify your processing and any impact on individuals. In effect, it requires a risk assessment based on the specific context and circumstances to demonstrate that processing is appropriate.


# Pseudoanonymization vs Anonymization

In their new analysis, the difference between anonymization and pseudonymization lays in the likelihood of reidentifiability — whether it’s possible to derive personal information from deidentified data. As study after study has demonstrated, however, it’s pretty much impossible to perfectly anonymize data, meaning some possibility of reidentification often remains. So how should organizations determine what is likely?

Here the WP enumerated three specific reidentification risks:

- **Singling out** — the ability to locate an individual's record within a data set.
- **Linkability** — the ability to link two records pertaining to the same individual or group of individuals.
- **Inference** — the ability to confidently guess or estimate values using other information.

So far, so good. The problem emerged, however, when the WP went on to suggest both aggregation and destruction of the raw data were also needed to achieve anonymization:

“It is critical to understand that when a data controller does not delete the original (identifiable) data at event-level, and the data controller hands over part of this dataset (for example after removal or masking of identifiable data), the resulting dataset is still personal data. Only if the data controller would aggregate the data to a level where the individual events are no longer identifiable, the resulting dataset can be qualified as anonymous.”

In other words, only by aggregating data into group statistics and permanently deleting the original data could organizations have full confidence their data was anonymized and therefore outside the scope of data protection regulations in the EU.

#### **Give up and embrace pseudonymization**

The first option is to give up on the project of anonymizing data entirely and simply consider all deidentified data as pseudonymized. While pseudonymized data does not fall outside the scope of EU data protections because reidentification is still possible, the compliance burden on pseudonymous data can be significantly lighter — assuming the processing purpose is legitimate, a legal basis is established (or the secondary purpose is considered to be compatible with the initial purpose) and the data controller is not in a position to identify individuals (making most individual rights virtually nonexistent, except the rights to information and to object).

A risk-based approach implies adopting an attacker-centric definition of anonymization, which appears compatible with the legal test. Indeed, the legal test will focus upon an assessment of the reidentification means reasonably likely to be used by the controller or another person, i.e, an attacker. In order to anticipate attackers’ behavior, deidentification experts rely upon risk models to guide them in their selection of data and context controls.

https://www.linkedin.com/pulse/anonymisation-now-house-cards-magali-feys/
With the elevation of Pseudonymisation to an outcome, to achieve GDPR-compliant Pseudonymisation it has become necessary to protect not only direct identifiers but also indirect identifiers and attributes. In addition, instead of being applied only to individual fields, GDPR-defined Pseudonymisation, in combination with the GDPR definition for Personal Data,[[vii]](http://#_edn7) now requires that the outcome must apply to a data set as a whole (the entire collection of direct identifiers, indirect identifiers, and attributes), and consideration must be given to the degree of protection applied to all elements in a data set. Finally, the foregoing must be accomplished while still preserving the data’s utility for its intended use.

As a result, pre-GDPR approaches (using a static token on a direct identifier, which unfortunately is still widely and incorrectly referred to as “pseudonymisation”) will rarely, if ever, meet the heightened GDPR requirements of Pseudonymisation. This also means that old approaches known as “pseudonymisation” will not be sufficient to meet the new heightened requirements under EU law.

**Protecting against singling out attacks**: Paragraph 85 of the EDPB Schrems II Recommendations requires protection against "singling out" of a data subject in a larger group effectively making the use of either k-anonymity or aggregation mandatory.

- ggregation mandatory.
- **Dynamism**: complying with the requirements in Paragraphs 79, 85, 86, 87 and 88 of the EDPB Schrems II Recommendations to protect against the use of information from different datasets to re-identify data subjects necessitates the use of different replacement tokens for differing purposes at different times (i.e., dynamism) to prevent re-identification by leveraging correlations among data sets without needing access to the “additional information held separately” by the EU data controller (see [MosaicEffect.com](https://www.mosaiceffect.com));

Anonymization techniques and pre-GDPR forms of tokenization (sometimes referred to as pseudonymization) are ineffective in today’s data-driven world. These factors combine to enable unauthorized re-identification of individuals via the Mosaic Effect. The Mosaic Effect occurs when a person is indirectly identifiable via linkage attacks because some datasets can be combined with other datasets known to relate to the same individual, enabling the individual to be distinguished from others.Go

> _“Data Controllers may not be aware that the GDPR encourages the use of pseudonymisation. I think that there are more than 16 occurrences of pseudonymisation in the GDPR. And they are not aware that Pseudonymisation helps to reduce the risks associated with processing data and can help relax some GDPR obligations.”_[_**[ix]**_](http://#_edn9)

I don't think we should compare data protection measures such as anonymization and pseudonymization.  
In fact, these measures are complementary and above all address very different risks and use cases.  
It’s important to note that under GDPR, pseudonymized data is still considered personal data.   
In addition, pseudonymization, cited in the GDPR must meet the good practices described by the EDBP by the end of 2021 (Thanks to [Fabrice Pariente](https://www.linkedin.com/in/ACoAAAEYrZ0BPTv6rN7KRAhCIITdLQKz99igmR8) for the reminder).  
  
On the other hand, to be robust anonymization must take into account the three risks of data re-identification listed by the G29 group : singling out, linkability and Inference.  
  
Solutions must meet specifications and ensure that they are state-of-the-art both for anonymization et pseudonymization according use cases and business needs.

An example of an area where legitimate interest most often are used to motivate the processing is when the [personal data](https://www.gdprsummary.com/gdpr-definitions/personal-data/) are being processed for certain marketing purposes, internal security and fraud prevention, administration of staff etc.



#gdpr
#pseudonymization
https://gdpr-info.eu/recitals/no-26/
1The principles of data protection should apply to any information concerning an identified or identifiable natural person. 2Personal data which have undergone pseudonymisation, which could be attributed to a natural person by the use of additional information should be considered to be information on an identifiable natural person. 3To determine whether a natural person is identifiable, account should be taken of all the means reasonably likely to be used, such as singling out, either by the controller or by another person to identify the natural person directly or indirectly. 4To ascertain whether means are reasonably likely to be used to identify the natural person, account should be taken of all objective factors, such as the costs of and the amount of time required for identification, taking into consideration the available technology at the time of the processing and technological developments. 5The principles of data protection should therefore not apply to anonymous information, namely information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable. 6This Regulation does not therefore concern the processing of such anonymous information, including for statistical or research purposes.