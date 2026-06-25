---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-troubleshoot

Get the existing namespaces in Kubernetes cluster. What namespace is your app running in? Is AGIC watching that namespace? Refer to the [Multiple Namespace Support](https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-multiple-namespace-support#enable-multiple-namespace-support) documentation on how to properly configure observed namespaces.

The AGIC pod should be in the `default` namespace (see column `NAMESPACE`). A healthy pod would have `Running` in the `STATUS` column. There should be at least one AGIC pod.





