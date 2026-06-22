
# Format preserving encryption

https://www.techtarget.com/searchsecurity/tip/Format-preserving-encryption-use-cases-benefits-alternative

**Format preserving encryption is to short to not be reverse engineered**
![[Pasted image 20231201103752.png]]

In these cases, there is simply not enough entropy to create a secure output that cannot be reverse-engineered. In SP 800-38G, the domain size for FF1 and FF3 was required to be at least 100 and recommended to be at least 1,000,000. In the revision, the domain size is required to be 1,000,000. Organizations considering FPE must ensure potential products and services adhere to the updated requirements.


# Implemtation of encryption keys

**Centralized vs distributed vs both?**

https://www.linkedin.com/pulse/8-best-practices-cryptographic-key-management-jisa-softech/?trk=pulse-article_more-articles_related-content-card

## Key Rotation: No Decryption/Re-Encryption
The expiration/change of encryption keys is a major issue that arises in businesses that deal with large databases.
##  Secure storage of keys:
Given the high value of encryption keys, they are an appealing target for cyber thieves, particularly when numerous keys are held in the same location
It is best practise to store keys in a [hardware security module (HSM)](https://www.jisasoftech.com/hsm-hardware-security-module/),
## Backup your encryption keys on a regular basis
If you lose an encryption key, you’re unlikely to be able to recover anything that was encrypted with it.

# Encryption levels
## Data encryption at rest is useless in the cloud

Misunderstanding the value of encryption for data at rest in _cloud_ environments is a big problem. When you need to protect data and not just check the box for security compliance’s sake, data encryption at rest has to be judged differently and therefore understood first. Data encryption at rest doesn’t help protect your customer data because it’s unlikely that anybody will steal the hard drive storing the data from an Amazon data center.

So why do we do it? Because it's old baggage and a part of security standards today.

But, by contrast, encryption of data at rest is of huge value for mobile phones. If stolen, encrypting data at rest makes it incredibly hard to obtain the plaintext data (photos, texts, etc.).

### Data encryption at rest vs application-level encryption

Encryption at rest is effectively broken, as it _automatically decrypts_ data for an application's read (query) requests. So, when an attacker manages to get inside your network and connect to the database, this protection mechanism fails as it allows them to read the data. This attack against databases is probably the most common, and that’s unacceptable. 

Application-level security addresses this weakness. In this case, the attacker gets encrypted data when they read from the database. However, they can’t decipher it because they don’t have access to the keys held by the application or a vault. If they want access to the keys, they must break into the application, raising the bar.