---
categories:
  - "[[Resources]]"
domain: engineering
title: "Change Data Capture (CDC)"
source: "https://medium.com/@venkatkarthick15/change-data-capture-cdc-3a076c9bdaa3"
author: "Venkatakrishnan"
published: 2023-08-02
created: 2023-11-29
description: "Change Data Capture (CDC) is a design pattern used in modern data architectures"
tags:
  - to-process
  - data-engineering
---

Change Data Capture (CDC) is a design pattern used in modern data architectures to detect and track changes in data. This process helps synchronize the changes from the source system to a target system, such as data warehouses, data lakes, or other databases.


Change Data Capture (CDC) is employed to detect and respond to changes within data sources. There are two primary strategies for capturing changes, push-based and pull-based with various mechanisms within each category.


![](https://miro.medium.com/v2/resize:fit:681/1*JfSRChB7nYR3omfcJKViAg.png)Image by the author 
Below, we explore both, offering examples and considering the challenges that might be encountered.


# Pull-Based Mechanisms


## **Row Versioning**


Row versioning is a technique used to detect changes within a data record, especially in a database.


## How It Works:


1. **Version Column:** A specific column, usually named something like “version” is added to each record in the database table. This column stores an integer that represents the version of the record.
2. **Incrementing the Version:** Every time a change is made to the record, the version number is incremented by 1. This could include any modification like adding, updating, or deleting data.
3. **Target System Processing:** The target system maintains a reference table that stores the last known version for each record. It periodically checks for rows with a version number greater than the stored value, captures these records, and reflects the changes in its system.
4. **Update Reference Table:** The reference table must be updated to reflect the new version numbers for the records processed.


## Example:


Let’s consider a customer database with the following record:


If the customer updates their email, the database record would change to:


## Challenges:


* **Complexity:** Requires careful tracking of each record’s version number.
* **Overhead:** Maintaining the reference table adds extra storage and processing overhead.
* **Concurrency:** Concurrent updates to the same record must be handled to prevent conflicts in version numbers.