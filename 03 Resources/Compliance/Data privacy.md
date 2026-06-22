
# ADR

https://vorwerkproducts.atlassian.net/wiki/spaces/NWOT/pages/871170218/WIP+ADR+analytics+10+Future+Targeting+Options+for+Digital+Marketing

# Build vs buy

https://www.piiano.com/blog/building-vs-buying-a-data-privacy-vault

1. **Strategic**: If you're going to build it, does this project align with the enterprise's core business objectives and long-term strategies?
2. **Total cost of ownership (TCO)**: When building a solution in-house, you need to consider the building aspect and maintenance costs (and focus) and compare them to the TCO of buying a product.
3. **Focus**: When building an in-house data privacy solution, organizations need to focus on a few crucial questions, such as:  
    - Can you afford to dedicate the resources required for such a project, and at what expense?  
    - Do you have the time and resources? When can you expect to get a fully functional system?
4. **Economies of scale**: Vendors that service many customers can allegedly distribute the maintenance and software operations costs across their clients. Thus, these economies of scale allow them to charge less for a service or product than you will achieve by building it yourself. You may consider asking yourself the following questions:  
    - Is there such a shelf product out there?  
    - Does it fit your needs in terms of functionality, scalability, performance, and playing well with your existing tech stack and various integrations?
5. **Competitiveness:** When building an in-house solution, do you have the needed compliance knowledge, experience, and expertise to build a better solution than the ones already out there on the market?
6. **Engineering complexity**:  
    - **Building security features like encryption and key management** or even just using an open-source encryption library requires expertise. It is a highly error-prone task and many fail to do it well.  
    - **Complexity of building a tokenization engine**: Building a tokenization engine is complicated. It has to be robust and secure and reduce privacy risks to data, requiring effort and expertise. It’s not just a mapping table. There’s so much more to it, like scopes, format-preserving tokens, convergence, uniqueness, determinism, rotations, etc.

Skyflow
![[Pasted image 20240614113034.png]]
8 months to build

https://www.skyflow.com/post/the-build-vs-buy-dilemma-the-real-cost-of-data-privacy
# Tips handling PII
## Always apply the 3 facts rule

It’s been said that with just 3 facts you can identify anyone in the world. This isn’t always the case, but you can certainly narrow the pool down tremendously with every fact you add. Consider the IP address example above.

# Always consider how datasets could be combined to allow for re-identification

# Always isolate environments that process PII

If you’ve ever watched [The Walking Dead](https://www.imdb.com/title/tt1520211/) you’ll know that as soon as a zombie enters the compound, it’s usually the end game for everyone inside. It’s similar with PII. Once you introduce PII into an environment, it’s hard to predict how your users will use that data, and more importantly where it will end up. As a result, you should always ensure that environments that process PII data are fully isolated from those that do not.

# Data Access

Attribute based access? 
Access linked to consent? 

https://www.immuta.com/blog/purpose-based-access-control/

## Are Purpose-Based and Policy-Based Access Control the Same?

There is another form of contemporary access control that is sometimes referred to as “PBAC”: [policy-based access control](https://www.immuta.com/blog/what-is-policy-based-access-control/). It’s important to clarify that, while often referred to by the same acronym, these two access control methods are **not the same**.

To reiterate the distinction between the two at the control enforcement level:

- **Policy-based access control** enforces policies on system users, letting these rules determine user access based on the role or attributes/characteristics of the individual.
- **Purpose-based access control** does not focus on individual users, and instead adds a contextual layer of specific data use purposes that determines whether access is granted or denied.

Ultimately, the term “policy-based” is becoming outdated in the face of the evolution of access control models. Since ABAC and its predecessor role-based access control (RBAC) are both policy-based, this terminology is broadened to the point of non-specificity. That is why we use PBAC to discuss access based on purpose, not policy. The policy-based access controls of yesterday are evolving alongside the data they govern and are incorporating more contextual information into access decisions, driving toward a future where purpose is vital

## How Does Purpose-Based Access Control Add Context in Practice?

Now that we understand what PBAC is (and what it’s not), we can examine how it works in practice.

Let’s imagine that you work for a data governance team at a [financial institution](https://www.immuta.com/solutions/financial-services/?_ga=2.19613054.738993641.1652104334-2097120534.1635515968&_gac=1.157879880.1649702598.CjwKCAjwo8-SBhAlEiwAopc9WyW-j9f0WP5Mc7Gb_C6MTMrsNRwCgjtcLwnzKbn0oweTVZCo-uk7GBoCTokQAvD_BwE). Much of the data you’re collecting from your customers, whether it be credit card numbers or bank account information, is extremely sensitive. This makes it all the more important that this data is kept safe from risk of leak or breach. Using ABAC to determine access will help determine which data users are able to see which information based on their given attributes. But what if an exception needs to be made to a global policy in order to enable data collaboration that would normally be restricted for certain users?

This is where having a purpose-based layer of access control is key. This user, who may not normally have access based on their attributes, could be assigned a specific purpose that alters their permissions. For instance, if they’re part of the organization’s legal team, they probably won’t typically have attribute-based access to credit card transaction data. But if a fraud case requires legal oversight and input, this user could be assigned a “fraud detection” purpose that (in a compliant fashion) grants them access to this information for this specific reason. This purpose could be rescinded after the case was closed, and the data would once again be hidden from this user.

# Data Acceptable Usage Policy

https://usercentrics.com/knowledge-hub/what-is-the-best-protection-method-for-sharing-pii/
Organizations need strong, clear policies to determine:

- what PII they need
- how they collect it
- how PII is stored, accessed, and shared
- if consent is needed to collect PII and how it is obtained
- who can access what PII and how
- what are the acceptable uses of PII
- how is unauthorized access or use of PII dealt with
- how is PII disposed of when no longer needed
- how often are audits and security reviews done and with what parameters
- who is responsible for PII security and use

Policies and procedures should cover both employee onboarding and offboarding as well as their authorizations while working for the organization. It is important to securely shut down access for accounts that are no longer needed, e.g. if an employee leaves the organization.
 
 https://medium.com/google-cloud/stop-worrying-about-bigquery-pii-how-to-automate-data-governance-at-scale-81abb3e47e0c

![[Pasted image 20240419151932.png]]

---
### **Data Security Governance**

One of the areas that screams out for centralization depending upon the corporate operating model is privacy, compliance, and security. This is what we refer to as data security governance. How this is implemented matters. This is because most enterprise data flows between corporate systems.

And while one could clearly start the process by governing domains, it is problematic when one takes an enterprise architecture perspective. What happens, for example, when customer data flows between Salesforce automation to customer support and financial systems? Clearly, the rules of the road need to operate consistently across different functional areas. Add to this compliance, which needs to be consistently managed across enterprise systems. There are clear penalties for doing it any other way.

However, there is good news. In the past, much of the difficulty concerning centralization was due to the need to manually manage data access system by system. Fortunately, new technologies make it possible to simultaneously discover risky data and implement a single policy and control for managing that data across the data estate — without coding. There is no penalty for centralization of privacy, compliance, or data security governance. This type of data governance is a lever of probability. Good governance reduces the probability of risk. It doesn’t eliminate it, but it goes a long way in mitigating. Bad governance or no governance is a formula for high risk.
# Anoynmization

Good articles mentioned misconception about PII
https://www.edps.europa.eu/system/files/2021-04/21-04-27_aepd-edps_anonymisation_en_5.pdf

![[Pasted image 20240520160318.png]]

Really good article on anonymization done incorrectly.
https://edps.europa.eu/system/files/2021-04/21-04-27_aepd-edps_anonymisation_en_5.pdf

Comparing the different solutions
https://www.databricks.com/blog/handling-right-be-forgotten-gdpr-and-ccpa-using-delta-live-tables-dlt
#right-to-be-forgotten
#databricks
## Data Anonymization Techniques

Data anonymization is the process of protecting private or [sensitive information](https://www.imperva.com/learn/data-security/sensitive-data/) by erasing or encrypting identifiers that connect an individual to stored data.

https://www.imperva.com/learn/data-security/anonymization/

- [**Data masking**](https://www.imperva.com/learn/data-security/data-masking/)—hiding data with altered values. You can create a mirror version of a database and apply modification techniques such as character shuffling, encryption, and word or character substitution. For example, you can replace a value character with a symbol such as “*” or “x”. Data masking makes reverse engineering or detection impossible.
- [**Pseudonymization**](https://www.imperva.com/learn/data-security/pseudonymization/)—a data management and de-identification method that replaces private identifiers with fake identifiers or pseudonyms, for example replacing the identifier “John Smith” with “Mark Spencer”. Pseudonymization preserves statistical accuracy and data integrity, allowing the modified data to be used for training, development, testing, and analytics while protecting [data privacy](https://www.imperva.com/learn/data-security/data-privacy/).
- **Generalization**—deliberately removes some of the data to make it less identifiable. Data can be modified into a set of ranges or a broad area with appropriate boundaries. You can remove the house number in an address, but make sure you don’t remove the road name. The purpose is to eliminate some of the identifiers while retaining a measure of data accuracy.
- **Data swapping**—also known as shuffling and permutation, a technique used to rearrange the dataset attribute values so they don’t correspond with the original records. Swapping attributes (columns) that contain identifiers values such as date of birth, for example, may have more impact on anonymization than membership type values.
- **Data perturbation**—modifies the original dataset slightly by applying techniques that round numbers and add random noise. The range of values needs to be in proportion to the perturbation. A small base may lead to weak anonymization while a large base can reduce the utility of the dataset. For example, you can use a base of 5 for rounding values like age or house number because it’s proportional to the original value. You can multiply a house number by 15 and the value may retain its credence. However, using higher bases like 15 can make the age values seem fake.
- **Synthetic data**—algorithmically manufactured information that has no connection to real events. Synthetic data is used to create artificial datasets instead of altering the original dataset or using it as is and risking privacy and security. The process involves creating statistical models based on patterns found in the original dataset. You can use standard deviations, medians, linear regression or other statistical techniques to generate the synthetic data.

![[Pasted image 20231213134832.png]]
###### Methods
- k-anonymization 
- tokenization
- encryption

**Needs to be confirmed by the DPO**

encryption wasn't considered compliant but random tokens were. Why is encryption less secure than tokenization? 

---

# Points to consider while choosing the tokenization provider

- Which industry do you work in, and does your company always experience data breaches or hacking attacks?
- Do you want to protect specific numbers, such as credit card numbers or account numbers (tokenization), or entire databases (encryption)?
- Do you think you could comply with your company’s data security policy more easily with which option? 
- Based on your budget, which option would be more feasible?
- What are the potential benefits of tokenization or encryption for your company based on your company size and customer base?

### Token Generation capabilities
- What data should be supported? Should it support token generation for JSON based requests.
- How many tokens should it be able to generate? 
-  Should be able to perform partial tokenization for e.g. for a given 16 digit credit card number just tokenize first 12 numbers and keep the last 4 digits real.
- Data residency requirement? 

# Tokenization

https://www.piiano.com/blog/how-to-protect-customers-secrets-in-your-saas-offering
![[Pasted image 20240620115800.png]]

## Pros
- Format preserving 
- Simplifies Data residency - Because vaulted tokens aren’t exploitable, they can be safely stored outside of the EU or Brazil without compromising the personal data of EU or Brazilian residents.
- Efficiently updating/deleting identifiers. Only need to update data in token vault and keep the token as is. 

## Cons
- Most optimal for structured data
- Can be harder for JSON data? 
- Single point of failure - If the vault (key?) is compromised all the actual values are exposed. 
- Data vault synchronization 
- Data backup?
# Encryption 

## Pros
- Scales independant of the volume since it's not reliant on the database
- Can anonymized unstructured, semi- and structured data.
- reduces the chances of data inconsistencies or synchronization issues between different centers or databases
- No data replication which reducing network traffic and latency. 
- Encryption is faster - The encryption process uses alghoritms to secure data, which [makes it faster](https://nira.com/tokenization-vs-encryption/). Tokenization takes _much_ longer because each character or number is changed into a random character.


## Cons
- Not format preserving
- Doesn't support data residency
- Doesn't comply with [[PCI Regulation]] 
- [More complex](https://www.piiano.com/blog/encryption-failure)
- Mathematical correlation that can be broken
-  Creating, protecting, and deploying encryption key can be hard. See [[Tokenization#Challenges with key management]]
- Given the high value of encryption keys, they are an appealing target for cyber thieves.  
- Doesn't simplify data residency


---

While the above are excellent guiding questions, we would recommend using both techniques together— tokenization and encryption—whenever possible. As both the methods are not mutually exclusive, you can employ them together to cover the other’s drawbacks and enhance your company‘s overall data security levels.

---
# [tokenization vs encryption](https://www.encryptionconsulting.com/education-center/encryption-vs-tokenization/)
Unlike encrypted data, tokenized data is undecipherable and irreversible because there is no mathematical relationship between the token and its original number. There is no key or algorithm, that can be used to derive the original data for a token. Instead, tokenization uses a database, called a token vault, which stores the relationship between the sensitive value and the token. The real data in the vault is then secured, often via encryption.

**Challenges with encryption**
- right algorithm
- chaining mode (block versus stream),
- use a strong random number generator 
- initialization vectors for key generation
- rotate keys
- Encryption algorithms are constant targets of cryptanalysis


- Biggest advantage of tokenization is to use production data in lower environments for testing.

The primary difference between tokenization and encryption is: with encryption the ciphertext is still mathematically connected to the original plaintext value. This means that if someone gets access to the key, either through brute force computation or by stealing it, they can retrieve all of the original data.

https://www.skyflow.com/post/demystifying-tokenization-what-every-engineer-should-know

Another point of concern when encrypting data for storage is the management of the decryption key. When data is encrypted, it is always going to be possible to decrypt the encrypted value with the corresponding decryption key. This makes the key rotation process very cumbersome because it requires that the data be fully decrypted with the original key and then re-encrypted with a new encryption key. Tokenization on the other hand allows access keys to be rotated on whatever frequency is specified by an agency’s security team without any additional operations being required on the previously-tokenized data.

### Vault Based
#### Concern
- Performance: Look up can become expensive if the list of mapped values grows over a period of time. More the number of mapping, the slower the lookup is.
- If the vault key is compromised, all the actual values are exposed.
- <mark style="background: #FF5582A6;">if the vault based tokenization server is hosted in various regions then it requires an expensive synchronization capability in order to keep it out of the loop of collision.</mark>  #tokenization-concern
- To provide a highly available and fault-tolerant platform for our vaulted customers, vaulted data must be replicated between data centers, which–in the event of a catastrophic outage–can result in a recovery point objective (RPO)/recovery time objective (RTO) of several minutes.

### Vault less

Vaultless tokenization, also known as format-preserving tokenization or deterministic tokenization, involves applying an algorithm to the sensitive data to generate a token that retains the same format and length as the original data. Unlike vault tokenization, vaultless tokenization does not rely on a centralized vault for storage.

The TokenEx vaultless tokenization algorithm is centered on a mode of format-preserving encryption (FPE).

[According to the official documentation of **Microsoft Presidio**, the change from **Format Preserving Encryption (FPE)** to **Advanced Encryption Standard (AES)** was introduced in **version 2** of the software](https://microsoft.github.io/presidio/presidio_V2/) [1](https://microsoft.github.io/presidio/presidio_V2/). [The change was made to improve the security of the software and to provide better support for encryption and decryption of sensitive data](https://microsoft.github.io/presidio/presidio_V2/) [1](https://microsoft.github.io/presidio/presidio_V2/).

[The **V1** version of Presidio, which used FPE, is still available for download](https://microsoft.github.io/presidio/presidio_V2/) [1](https://microsoft.github.io/presidio/presidio_V2/). [However, it is recommended to use the latest version of the software, which uses AES encryption](https://microsoft.github.io/presidio/presidio_V2/) [1](https://microsoft.github.io/presidio/presidio_V2/).

I hope this helps!

#### Strengths of Vaultless Tokenization:

- Reduced risk of a single point of failure: Since there is no centralized vaulted tokenization, the risk of a breach compromising all the sensitive data is minimized.
- **Simplified implementation: Vaultless tokenization can be implemented more easily than vaulted tokenization, as it does not require setting up and managing a centralized vault.?? Is this true**
- Retains data format: The format-preserving nature of vaultless tokenization makes it suitable for applications that require the original data format to be preserved, such as databases or legacy systems. One of the [benefits](https://www.linkedin.com/pulse/bigdata-gdpr-pii-anonymization-pseudonymisation-fpe-data-max-b%C3%B6reb%C3%A4ck/) with FPE is that you could use it to generate test data from production data in which would give you very good and quality data to use in test.
- With vaultless tokenization, there is no token vault to replicate, so RPO/RTO effectively drops to zero, increasing availability. Platform responsiveness also increases because there are no database reads or writes with vaultless tokenization. In a single API call, this improvement is negligible, but when processing a large batch file, the faster processing has a noticeable impact.
+ Ease of right to be forgotten
- Works for both structured and unstructured data, such as entire files in their entirety. 
+ **Vaultless Tokenization Doesn’t Simplify Data Residency**
- The encryption process uses alghoritms to secure data, which [makes it faster](https://nira.com/tokenization-vs-encryption/). Tokenization takes _much_ longer because each character or number is changed into a random character.
![[Pasted image 20231204181725.png]]
#### Right to be forgotten
**Imagine that you assign a unique encryption key to each Data Subject** (employee, customer, and so forth) and that you encrypt that person’s personal data in your databases with that unique and specific key. The time comes when must meet your obligations under Right of Erasure. Rather than go through every database table and storage server to delete the data, you could just delete the encryption key.

#### Weaknesses of Vaultless Tokenization:

**- Potentially weaker security: Without the added layer of encryption and storage in a secure vaulted tokenization, the risk of unauthorized access to sensitive data may be higher.**
- Limited search and analysis capabilities: Since the original data is not stored, performing operations like search or analysis on the tokenized data might be more challenging.
-  **Secure storage of keys:** Given the high value of encryption keys, they are an appealing target for cyber thieves, particularly when numerous keys are held in the same location. It is best practise to store keys in a [hardware security module (HSM)](https://www.jisasoftech.com/hsm-hardware-security-module/), which provides very strong physical and logical security protection and is often validated to the FIPS 140-2 security requirements for cryptographic modules.

https://www.skyflow.com/post/why-and-how-to-migrate-from-vaultless-tokenization-to-a-vault
##### Why Vaultless Tokenization is Actually Encryption (and Isn’t PCI Compliant)

Vaultless tokenization solutions may appear similar to vaulted tokenization on the surface, but they lack the essential security and compliance features that vaulted tokenization offers.

Returning to our example above, if a malicious actor discovers that the token “d7-4c-5734” corresponds to “John Doe”, that doesn’t impact the security of other sensitive data if “John Doe” and other customer names like “Mary Joe” and “Abby Smith” are stored in a vault. With vaulted tokenization, there’s no relationship between the plaintext data and its obfuscated form.

On the other hand, with vaultless tokenization (which is  a form of encryption), a malicious actor who discovers that  “d7-4c-5734” corresponds to “John Doe” can now decrypt the names of other customers from their tokens.

This is the reason that the [Payment Card Industry Data Security Standard (PCI DSS) doesn’t recognize vaultless tokenization](https://www.pcisecuritystandards.org/documents/Tokenization_Guidelines_Info_Supplement.pdf) as a secure method to protect PANs.

As they put it:

> ‍_Note that where token generation is based on a reversible encryption method (where the token is mathematically derived from the original PAN through the use of an encryption algorithm and cryptographic key), the resultant token is an encrypted PAN, and may be subject to PCI DSS considerations in addition to those included in this document. The PCI SSC is further evaluating how these considerations may impact PCI DSS scope for reversible, encryption-based tokens._  

**Vaulted tokenization that’s PCI DSS compliant relies on a secure token vault to store the mapping between sensitive data and tokens, so that tokens generated by this method cannot be "decrypted" to reveal the original data.**

####  Challenges with key management
https://info.townsendsecurity.com/gdpr-right-erasure-encryption-key-management
The hardest part of getting encryption right has to do with creating, protecting, and deploying encryption keys. It is probably the hardest part of getting an encryption strategy right - and there are a lot of ways to get key management wrong:

- Storing the unprotected encryption key with the protected data
- Using weak protection methods to secure encryption keys
- Storing the encryption key directly in application code
- Using a weak encryption key - a password is an example of a weak key
- Not using strong, industry standard methods of generating an encryption key
- Not providing separation of duties and dual control around key management

### Comparing Efficiency: Vault vs. Vaultless Tokenization

#### Evaluating the Efficiency of Vault Tokenization

Vault tokenization provides a secure method for storing and retrieving sensitive data. However, it can become less efficient as the volume of data increases. With more data to token and detokenize, the size of the vault database grows, leading to increased latency. and decreased performance.  
  
One way to address this issue is through intelligent data management techniques. This includes implementing data archiving and purging strategies to remove unnecessary or outdated data from the vault database. By regularly cleaning up the database, the overall size can be reduced, resulting in improved efficiency and performance.

Another approach is to employ data compression techniques. Compressing the vault database can significantly reduce its size without compromising security. This can be achieved through various compression algorithms that are designed to minimize storage requirements while maintaining data integrity.  
  
Additionally, optimizing the tokenization and detokenization processes can help enhance efficiency. This involves streamlining and fine-tuning the algorithms and procedures used for these operations to minimize computational overhead and latency. **Implementing caching #tokenization-cache mechanisms and utilizing indexing techniques can also improve the retrieval speed of tokenized data**. Furthermore, scaling the infrastructure supporting the vault system can enhance performance. This includes deploying additional servers or utilizing cloud-based solutions to distribute the workload across multiple instances. Load-balancing techniques can also be employed to evenly distribute requests and prevent any single point of failure.  
  
Overall, ensuring efficient vault tokenization with increasing data volumes requires a combination of smart data management practices, compression techniques, algorithm optimization, and infrastructure scaling. By implementing these strategies, organizations can maintain high-performance levels while securely storing and retrieving sensitive data.

#### Assessing the Efficiency of Vaultless Tokenization

Vaultless tokenization, in contrast, does not face the same scalability issues. Since it doesn’t rely on a database, **it remains equally efficient regardless of the data volume**. This absence of a database also means there’s no need for data replication between centers, further enhancing efficiency. and reducing the chances of data inconsistencies. Vaultless tokenization achieves this by generating unique tokenization explained for each sensitive data element, such as credit card numbers or social security numbers, on the fly, without the need for a centralized database to store and retrieve the tokens.  
  
Instead, the tokenization process is typically performed within the application itself, using encryption algorithms and secure key management systems. This enables each application or system to tokenize its own sensitive data independently without relying on a shared or centralized tokenization service.  
  
As a result, vaultless tokenization offers several advantages. Firstly, it eliminates the need for complex database infrastructure and maintenance, which can be costly and resource-intensive. This makes it easier and more cost-effective to implement tokenization across multiple systems or applications.  
  
Secondly, the absence of data replication between centers reduces network traffic and latency, improving overall system performance and responsiveness. This is particularly beneficial in distributed environments where data is stored across multiple locations or data centers.  
  
Furthermore, vaultless tokenization offers better scalability as it can handle increasing data volumes without impacting performance. Since there is no reliance on a centralized database, the tokenization process remains efficient regardless of the amount of data being tokenized. Lastly, without the need for data replication, vaultless tokenization also reduces the chances of data inconsistencies or synchronization issues between different centers or databases. Each application or system maintains its own tokens, ensuring data integrity and consistency within its own context. Overall, vaultless tokenization provides a scalable, efficient, and cost-effective solution for protecting sensitive data without the limitations and scalability challenges associated with traditional database-dependent tokenization approaches.

### Comparison
https://www.blockchain-council.org/blockchain/tokenization-vs-encryption/?utm_source=Affiliate&utm_medium=Rakuten&utm_campaign=2126220&utm_content=10&ranMID=43395&ranEAID=a1LgFw09t88&ranSiteID=a1LgFw09t88-paOk7zviFhyk7D9DxAsbjg

![[Pasted image 20231204182853.png]]

While the above are excellent guiding questions, we would recommend using both techniques together— tokenization and encryption—whenever possible. As both the methods are not mutually exclusive, you can employ them together to cover the other’s drawbacks and enhance your company‘s overall data security levels.

![[Pasted image 20231204183225.png]]

https://www.linkedin.com/pulse/tokenization-vs-encryption-suyash-chand/?trk=public_profile_article_view
![[Pasted image 20231205141642.png]]

**Encrypted data is not protected during use. How is tokenisation that?**

### Points to consider while choosing the tokenization provider

- Which industry do you work in, and does your company always experience data breaches or hacking attacks?
- Do you want to protect specific numbers, such as credit card numbers or account numbers (tokenization), or entire databases (encryption)?
- Do you think you could comply with your company’s data security policy more easily with which option? 
- Based on your budget, which option would be more feasible?
- What are the potential benefits of tokenization or encryption for your company based on your company size and customer base?

### Token Generation capabilities

- Should support bulk token generation for data bundled in CSV or batch so that round trip time between calling service and tokenization server can be reduced.
- Should support token generation for JSON based requests.
<mark style="background: #FF5582A6;">- It should be able to generate tokens for the different data types for e.g. alphanumeric, numeric, Date and boolean.</mark>
- <mark style="background: #FF5582A6;">It should be able to generate tokens for multibyte characters with accented characters (for e.g. [umlaut](http://www.disknet.com/indiana_biolab/ger004.htm) characters) by <mark style="background: #FF5582A6;">preserving</mark> appearance, length and delimiter.</mark>
- <mark style="background: #FF5582A6;">Some PII fields like surname can be two or three letters (for e.g. Yu or Lee), it should be able to generate tokens for those by either padding or some other mechanism. Reason being de-tokenization of two characters can be hacked.</mark>
-<mark style="background: #FF5582A6;"> Should support the prefix or suffix for an application to identify the multi region tokenized data so that it can be routed to the appropriate region for de-tokenization.</mark>
-<mark style="background: #FF5582A6;"> Should be able to perform partial tokenization for e.g. for a given 16 digit credit card number just tokenize first 12 numbers and keep the last 4 digits real.</mark>
-<mark style="background: #D2B3FFA6;"> Should be able to provide VaultLess tokenization service.</mark>
### Performance:

- Should be able to generate thousands of tokens fast and secured else this could become the biggest bottleneck.
- Should be able to handle the request coming in MBs and should provide the response faster.

###  Scalability:

- Should be scalable if the number of connections that performs tokenizations and not just by throwing a hardware to existing tokenization server farm.

### PCI and CCPA/GDPR compliant:

- Ensure provider understand PCI and GDPR compliance, security, and the risk.
---
you are perfectly right, there are many methods and different interpretations made by DPOs. For us encryption was not considered compliant by the DPO, but random tokens made the cut. Deleting the token in firestore makes it anonymous and is how we approach RTBF. Also, encryption often results in strings, we want to support more types.

Should keep the distribution?

![[Pasted image 20231116140035.png]]

![[Pasted image 20231116140124.png]]
#robert-sahlin
BigQuery GDPR compliance with serverless PII format preserving tokenization?  
  
As Data Platform Lead I don't do as much programming as I used to and hence I thought I would spend a day or two brushing up my Python and FastAPI skills by developing a service to de-identify and re-identify PII while supporting both stream and batch mode. The service is built on top of cloud run and firestore and the streaming mode is supported through a simple REST-API while the batch mode is implemented as a remote functions endpoint.  
  
The solution uses tokenization rather than encryption for a few reasons. It enables native data types, format preserving tokenization, no algorithm that can be broken, forgetting single fields/values, etc.  
  
The nice thing with keeping the token/value lookup in firestore is that you keep the pseudonymized data and the lookup completely separated with no duplication and it also works great with streaming patterns that is the most frequently used mode, but you can still re-identify data that isn't forgotten if you have to (ex. activation). I will however add a feature to publish created and deleted tokens on a pubsub to implement cdc of tokens in BigQuery if frequent and large scale re-identification is needed.  
  
I intend to open source the code when I've cleaned it up and documented it a bit and we appreciate contributions and feedback if you are interested. I will also write a longer post about the solution in my substack so please subscribe if you find it interesting (link in comments).

##### Right to be forgotten
Is it enough to just anonymize data?
https://www.linkedin.com/pulse/data-anonymization-right-forgotten-bill-tolson/

https://knowledge.technolutions.com/hc/en-us/articles/360058260631-GDPR-Right-to-Erasure-or-Right-to-be-Forgotten-Process-and-Considerations-
When a person requests to be forgotten, there are two options to fulfill the request: 

- Delete the record, including all associated identifiable data. 
- Anonymize the data by creating a record with pertinent (non-identifiable) data points to represent the forgotten individual, and then delete the record.

### [[Tokenization]]


### Differential privacy
[differential privavy][https://cloud.google.com/bigquery/docs/differential-privacy]

compliance with privacy laws.
data encryption


## Adrian Experience

Secured in a Data Lake 
You can have buckets and buckets policies. 
Could import data sources with sensitive information. 
Ownership was assigned to teams. Used OKTA. 
Only grant this team have access writing or reading. 
DBT - It's responsibility to write it to a place where only they have access. Product teams responsibility to not write it 

Built a solution with 
Schemas where you could specify with 

Tokenization 
Replaced it by token 
production database. 
mysql database with a lookup 

Prevent keeping users with plain text - own responsibility
Tokenization was done by ourself. 
Hard part for scalability? It was a issue but they figured out a way. 
Getting schemas was hard. What happened if type changes? 

---
#hm #data-privacy
Alla som har PII utbildas inom. PII. De behöver gå en kurs.  
Ledger: Har ett frågeformulär som de ska fråga för att veta vilka de ska man ge access till.  
Koppla varje request access till PII till era ropa entires (record of processing activity).  
Kopplar access till juridiskt dokument, där man samlar sina right of processing. En användare får klicka in vilket typ av access man behöver vilken anledning man har till access. Gäller bara för person data

--

# Netlight reference cases 

https://netlight.slack.com/archives/C04G2CJP6/p1727163871736139
`homomorphic encryption` `privacy`Hey all! ![:smile:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f604@2x.png)Long shot here - has anyone explored using homomorphic encryption techniques to pseudonomize user id:s but maintaining equality comparisons? The goal would be to encrypt sensitive data with somewhat low cardinality i.e social security numbers without ever exposing the raw ssn:s to the database while still maintaining referential integrity, especially when more rows are loaded with the same ssn incrementally over time.Most commonly if compliance requirements are a bit more relaxed salting & hashing is done but that still requires holding a lookup table of ssns/salts OR if not using salting, it is very easy to brute force try all SSN:s as the range of SSN:s is relatively small. The above would allow for not holding that lookup table internally


# Resources 
https://medium.com/@andrewpweaver/best-practices-for-handling-pii-data-6281be8c15ae