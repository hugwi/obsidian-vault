---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

Retrieeve the usagestats of a dataset (currently crashingo)
```python

import requests
import json
import os

DATAHUB_TOKEN = os.getenv("DATHAUB_TOKEN")

endpoint = f"https://datahub-dev.mediamarktsaturn.com/api/graphql"
headers = {"Authorization": f"Bearer {DATAHUB_TOKEN}"}

query = """query {
  search(input: { type: DATASET, query: "*", start: 0, count: 10 }) {
    start
    count
    total
    searchResults {
      entity {
         urn
         type
         ...on Dataset {
            name
            usageStats {
                buckets {
                    metrics {
                    topSqlQueries
                    }
                }
                aggregations {
                    totalSqlQueries
                }
            }
         }
      }
    }
  }
}"""

r = requests.post(endpoint, json={"query": query}, headers=headers)
if r.status_code == 200:
    print(json.dumps(r.json(), indent=2))
else:
    raise Exception(f"Query failed to run with a {r.status_code}.")
```