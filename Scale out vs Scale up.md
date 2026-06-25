---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
https://community.databricks.com/t5/data-engineering/sequential-vs-concurrency-optimization-questions-from-query/td-p/36696

Scaling in Databricks involves two aspects: vertical scaling (scale up) and horizontal scaling (scale out).

1. Vertical Scaling (Scale Up):
    
    - If your queries are running sequentially, meaning one query at a time, and you want to improve performance for a single query, you can scale up the cluster by increasing the size of the nodes.
    - For example, you can upgrade from a smaller instance type (e.g., 2x small) to a larger instance type (e.g., 4x large) to allocate more resources to the query. This can improve query execution time for individual queries.
2. Horizontal Scaling (Scale Out):
    
    - If your queries are running concurrently or there are multiple users running queries simultaneously, scaling out is a better approach. Scaling out involves adding more clusters to distribute the workload.
    - Instead of increasing the size of a single cluster, you can create multiple clusters and configure them to handle the workload in parallel.
    - Databricks provides features like Auto Scaling, which can automatically adjust the number of clusters based on workload demand. This helps ensure resources are efficiently allocated to handle the workload.

To summarize:

- Sequential queries: Scale up by increasing the size of the cluster to allocate more resources for better performance.
- Concurrent queries or multiple users: Scale out by adding more clusters to distribute the workload and enable parallel processing.

Keep in mind that the decision to scale up or scale out depends on the specific requirements of your workload, the complexity of your queries, and the concurrency level. It's essential to monitor and analyze the performance of your queries to determine the optimal scaling strategy.

Additionally, when it comes to SQL endpoints, scaling the range refers to adjusting the number of concurrent queries allowed. This can be useful when you have many users running queries simultaneously and need to ensure sufficient resources are available.

It's also worth noting that scaling alone might not be the only solution for improving performance. Optimizing your queries, leveraging query tuning techniques, and utilizing appropriate caching mechanisms can also significantly enhance query execution in Databricks.