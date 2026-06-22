
MD5 or SHA is not the concern. Hashes can be used for pseudonymization. The problem is that the hash would need to be salted (or peppered) so that data from other sources could not be used to identify the person.

My email is the same everywhere. A hash of it would also be the same. So that means that, in this case, the hash and my email become synonymous. Just like a username and the legal name of a person if paired. If you use a hash in this case, you actually gain nothing in terms of GDPR.

Hashing with a salt (or pepper) makes de-anonymising nearly impossible without knowing the added value. The salt (or pepper) almost becomes the token, in this case.

As always, check with your DPO.


https://security.stackexchange.com/questions/202022/hashing-email-addresses-for-gdpr-compliance

The problem with hashing emails is that they are usually short and easy to brute-force.

If you use a salt, by definition it is a public "key", so you do not add anything in terms of protection. Because GDPR includes yourself being unable to trace back your customers, you are the defendant and the attacker here, so any pepper or password is of little use against yourself.

The real problem is brute-force. I am no expert in security but the solution we are currently considering for our own issue which is similar to yours is the following: for each user email, apply a hashing algorithm N times, where N is a random number between Min and Max. When looking up in your database, take the email provided by your user and hash it Min-times, then lookup, then hash again, then lookup, etc until you either have a match or reach Max-times.

The advantage of having N varying for each database entry is that a brute-force attack would need to try hashing Max-times for every single combination they try, whilst if you have the combination, you are likely to get a lookup hit after only (Max-Min)/2 hash iterations. So on average, you make the attacker's life harder than yours. That's assuming your database lookups are faster than each hashing iteration.

Some further food for thoughts:

1. Use a [time consuming](https://crypto.stackexchange.com/questions/24/what-makes-a-hash-function-good-for-password-hashing) hashing algorithm
2. Use a [good salt](https://crypto.stackexchange.com/questions/44976/how-do-i-create-an-effective-salt) (long and random)
3. Consider having the salt changing for each iteration: `salt(n) = f(salt(n-1))`
4. Consider having the salt evolving between each iteration: `salt(n) = f(salt(n-1), hash(n-1))`
5. Do not store `N`, by the way.

# Peppar 

https://en.wikipedia.org/wiki/Pepper_(cryptography)
In [cryptography](https://en.wikipedia.org/wiki/Cryptography "Cryptography"), a **pepper** is a secret added to an input such as a [password](https://en.wikipedia.org/wiki/Password "Password") during [hashing](https://en.wikipedia.org/wiki/Hash_function "Hash function") with a [cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function "Cryptographic hash function"). This value differs from a [salt](https://en.wikipedia.org/wiki/Salt_(cryptography) "Salt (cryptography)") in that it is not stored alongside a password hash, but rather the pepper is kept separate in some other medium, such as a Hardware Security Module.[[1]](https://en.wikipedia.org/wiki/Pepper_(cryptography)#cite_note-1) Note that the [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology "National Institute of Standards and Technology") refers to this value as a **secret key** rather than a **pepper**. A pepper is similar in concept to a [salt](https://en.wikipedia.org/wiki/Salt_(cryptography) "Salt (cryptography)") or an [encryption key](https://en.wikipedia.org/wiki/Key_(cryptography) "Key (cryptography)"). It is like a salt in that it is a randomized value that is added to a password hash, and it is similar to an encryption key in that it should be kept secret.

https://news.ycombinator.com/item?id=24379120

A pepper is essentially a secret encryption key (it's a long secret string that's added to the password and the salt to ensure more entropy). With cloud key management services (e.g. both AWS and GCP have a KMS), I think it's more beneficial to just _encrypt the hash_ before putting it in your database. Process looks like this:

Upon password creation:

1. Generate hash as hash of password + salt.

2. Encrypt the hash with a public key from KMS (you can store the public key in your server code).

3. In your database store the encrypted hash, the salt, plus some "key ID" that identifies which KMS public key you used (this is so you can rotate keys later).

Upon user login to verify the password:

1. Retrieve the user's encrypted password hash, salt and KMS key ID from the database.

2. Make a call to KMS to decrypt the hash (KMS internally stores the corresponding private key but never lets you access it).

3. Then hash the password the user entered + salt and compare it to the decrypted hash to see if there is a match.

Benefits of this are:

1. If an attacker steals your database, they can't decrypt any of the passwords or the password hashes.

2. KMS _never_ exposes the private key of the async key pair, so you know this won't get exposed either. The only way to decrypt something is to make an API call to KMS.

3. Thus, the only valid attack really is if the attacker is able to gain the same access privileges as your server. But even then they _still_ need to call KMS one-at-a-time to decrypt hashes, and all of those KMS calls are logged in an audit trail, so it should be much easier to see if you have anomalous calls to KMS. There is a huge benefit here in that it is impossible to do bulk decryption without a giant audit trail.


https://medium.com/@berto168/salt-pepper-spice-up-your-hash-b48328caa2af

Enter the cryptographic hash function that can scramble our data, a process referred to as hashing. Hashing involves taking in a string of data, running it through a mathematical algorithm, and outputting a slew of jumbled data that looks nothing like our original input. Our server will then store this hashed password and link it to the corresponding username. This hash function is referred to as a “one-way function” because it is infeasible to revert the process.

It is important to note though that with the same hashing algorithm (and there are a few out there), the hashed output of the same string will be the same. This is how the server verifies that we have indeed provided the correct password. Because it has stored the hashed password it can run the hash algorithm on our input and compared to two hashed results.

Hackers can use this to their advantage by creating a list of **passwords derived from common terms** and checking each password at high rates to find the right combination (**dictionary attack**). The hackers can take this a step further if they know the hashing algorithm used to produce the hashed passwords. They can take their dictionary and **pre-hash all of the passwords creating a new “rainbow table” for their attacks**. Now all they need to do is check to see if any of the hashes of the rainbow table match with any of the hashed passwords in the database and they have our password.

![[Pasted image 20231214113555.png]]

However, the main difference is that while **salt is stored with the hashed value**, the **pepper value is hidden away from the hashed value**. This adds the additional benefit that the pepper is not known to the attacker.

Although pepper may seem like just more security, it is not as commonly utilized as a salt. Accepted hashing algorithms such as PBKDF2 and bcrypt were designed to derive keys with salts only.

Because hashes are a one-way function, the rotation of the pepper key creates an additional problem.

A password hashed with a pepper relies on that original pepper in order to be validated. This precludes the rotation of the pepper key, a big security flaw! For now salt-seasoned hash is the way to go.

https://info.townsendsecurity.com/bid/50817/Data-Protection-Hashes-and-Salting
If you do use a salt value with a hash, you have to take care to **protect the salt value from loss**. You should take as much care about protecting the salt value as you take with encryption keys. If someone knows the salt value you’ve lost your advantage. Also, you should be sure to use a salt value that is large enough to provide good security. A 128-bit salt value is adequate for most business applications.


## Hashing UUID

A UUID's hash value is **a 64 bit representation of that number**. Obviously we're losing information in the hash function. So it could well be possible for two UUIDs to hash to the same value. Or consider a rudimentary string hash that simply sums the value of each character in a string

## Probability of collision and impact

https://stackoverflow.com/questions/16352202/is-it-wrong-to-use-a-hash-for-a-unique-id
How horrible would it be if two ended up the same? Murphy's Law applies - if a million to one, or even a 100,000:1 chance is acceptable, then go right ahead! The real chance is much, much smaller - but if your system will explode if it happens then your design flaw must be addressed first. Then proceed with confidence.

Here is a question/answer of what the probabilities really are: [Probability of SHA1 Collisions](https://stackoverflow.com/questions/1867191/probability-of-sha1-collisions)