---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
Need to add namespace and download crds manually
Then add a dependency to the charts that needs to add it to ingress.
$ kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.6.3/cert-manager.crds.yaml

Getting W0417 21:30:36.327353   39357 warnings.go:70] unknown field "spec.secretName"


# These commands seem to work
 5457  helm repo add jetstack https://charts.jetstack.io
 5458  kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.0/cert-manager.crds.yaml
 5459  helm upgrade --install cert-manager jetstack/cert-manager --namespace cert-manager --version v1.8.0 -f manifests/cert-manager-values.yaml
 5460  helm upgrade --install cert-manager jetstack/cert-manager --namespace cert-manager --version v1.8.0 -f
 5461  helm upgrade --install cert-manager jetstack/cert-manager --namespace cert-manager --version v1.8.0
 5462  vim
 5463  helm upgrade elain-bff ./charts/elain-bff/ -f charts/elain-bff/values-dev.yaml
 5464  helm install elain-bff ./charts/elain-bff/ -f charts/elain-bff/values-dev.yaml
 5465  kubectl describe clusterissuer letsencrypt-staging
 5466  kubectl get certificate
 5467  kubectl describe certificate letsencrypt-staging-account-key3  -n cert-manager
 5468  kubectl describe certificate letsencrypt-staging-account-key3
 5469  kubectl get ingress
 5470  kubectl describe ingress
