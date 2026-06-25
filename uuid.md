---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

https://medium.com/weekly-webtips/should-you-use-uuid-fee0765dad2c

# So what’s the catch?

Ok, there is ONE catch. And it’s not a small one: performance.

First, the size. Storing a 36 characters string is not as efficient as storing a 4 or 8-byte integer. I hear that MySQL 8 and MongoDB offer the possibility to store UUIDs in a compact binary format, that would occupy only 16 bytes, which is significantly better.

Second, the speed. In a database, entries are indexed in order. This is very convenient for auto-incremented values since every new row is then inserted after the last one. And this is how light-speed search is achieved when done on the primary key. But when using UUID, inserted rows will usually not be after the last one. This is slower because the database engine has to browse the entire database to make the insert. And it has some side effects on the database file structure.

# Make your choice

So, is UUID for you? Should you use it?

If your database is or will eventually be distributed, like in the case of a local-first application, or simply if your NoSQL database is scaling up and divided upon multiple servers, I’d say that you have an almost non-choice: Use UUID! Just know that there are some things that you can do to improve performance. I encourage you to look into the different versions of the UUID standard.

For every other case, don’t bother.

This article is based on my latest readings on the subject. Here is a sample of the more enlightening articles I’ve read on UUID. May they provide you with some more details.

- [https://www.percona.com/blog/2014/12/19/store-uuid-optimized-way/](https://www.percona.com/blog/2014/12/19/store-uuid-optimized-way/)
- [https://generate-uuid.com/when-why-use-uuid-guid](https://generate-uuid.com/when-why-use-uuid-guid)
- [http://www.debuggable.com/posts/why-uuids:48c906cc-7a6c-4f22-9e20-6ffd4834cda3](http://www.debuggable.com/posts/why-uuids:48c906cc-7a6c-4f22-9e20-6ffd4834cda3)


https://medium.com/@saurabhk1593/uuid-and-its-use-in-distributed-systems-cfc16bd227c8


Advantages:

There are several advantages of using UUIDs:

 Uniqueness: UUIDs are designed to be globally unique, which means that it is highly unlikely that two UUIDs will be the same. This makes them ideal for identifying objects in distributed systems, where multiple systems may need to access the same data.
 Randomness: Version 4 UUIDs are generated using random numbers, which makes them difficult to predict. This makes them more secure than sequential identifiers, which can be easily guessed or enumerated.
 Scalability: Because UUIDs are globally unique, they can be generated independently by different systems, which makes them ideal for use in distributed systems that require high scalability.
 No central authority: UUIDs do not require a central authority or server to generate them. This means that they can be generated locally and used immediately without having to contact a central authority.
 Easy to generate: UUIDs are relatively easy to generate, which makes them convenient to use in a variety of applications.
 Persistence: UUIDs can be used as unique identifiers for objects that are stored in a database or file system, which makes it easy to retrieve them later.
 Standardized: UUIDs are standardized by the Open Software Foundation (OSF) and the Internet Engineering Task Force (IETF), which means that they are widely recognized and supported by different systems and programming languages.

**How to partition using UUID ?**

Yes, it is possible to use UUIDs as a key for data partitioning in distributed systems.

UUIDs are designed to be globally unique, which makes them ideal for identifying data objects in a distributed system. In a partitioned database or file system, data is typically divided into multiple partitions or shards, each of which is stored on a separate node or server. The goal of data partitioning is to distribute data evenly across the system to achieve better scalability, availability, and performance.

UUIDs can be used as keys for data partitioning by mapping each UUID to a specific partition. One common approach is to use a consistent hashing algorithm, which takes the UUID as input and maps it to a specific partition based on the hash value. This ensures that UUIDs are evenly distributed across the partitions, and that each partition contains a roughly equal number of UUIDs.

Using UUIDs for data partitioning has several benefits.

1. First, because UUIDs are globally unique, they ensure that data objects are evenly distributed across the system, which helps to prevent hotspots and balance the workload.
2. Second, UUIDs are relatively easy to generate and can be used as primary keys for database tables, which makes it easy to link related data objects across partitions.
3. Finally, because UUIDs are independent of the underlying system or network, they can be used to partition data across different types of systems and networks, which makes them highly flexible.Go

**Example:**

Suppose you have a database with a large number of customer records, and you want to partition the data across multiple nodes for better scalability and performance. To do this, you could use a consistent hashing algorithm to map each customer record to a specific partition based on the UUID.

Here’s how this might work in practice:

1. Generate a UUID for each customer record. This can be done using a UUID generator library, which will create a unique UUID for each record.
2. Use a consistent hashing algorithm, such as MD5 or SHA-1, to map each UUID to a specific partition. This algorithm will take the UUID as input and output a hash value, which can be used to determine the partition.
3. Divide the partitions across multiple nodes or servers. Each node will be responsible for storing the customer records that are mapped to its partition.