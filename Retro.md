---
categories:
  - "[[Areas]]"
domain: career
created: 2026-06-23
---
Think we blame each other too much 

```
DataHub prod should be back working again for ingestion ![🚚](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/truck/default/60_f.png?v=v14)
We found two issues:

- The DataHub ingestion config for some reason missed the entry statefulIngestionCapable=true. We cannot find the reason since it is hardcoded into the source code. Sebastian and I did a redeployment of DataHub and now it is fixed. Ingestions should be able to run through again. ![⚒️](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/2692_hammerandpick/default/60_f.png?v=v10)
- The redeployment was not smoothly done since someone triggered [this deployment](https://console.cloud.google.com/cloud-build/builds;region=global/718a2547-5e6c-4193-b262-95c492e5944c?project=mms-ana-anase-datahub-p-data "https://console.cloud.google.com/cloud-build/builds;region=global/718a2547-5e6c-4193-b262-95c492e5944c?project=mms-ana-anase-datahub-p-data") yesterday, which failed since it missed the correct Helm chart version and enablement of cp-helm-charts. It caused DataHub prod to be left in a unclear state. Although it is not too hard to fix, in the future we should be more mindful when running any deployments in prod (e.g. should at least communicate it to the team upfront) ![🙂](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/smile/default/60_f.png?v=v82)

```

I think we comment to much on formatting on PR. 

- A lot of comments on formatting make one miss important changes -> suggestion to have editorconfig
	- One line change could make changes to 50 lines
	- If we have different formatting they might back and fourth
- Clear roadmap a bit hard to prioritise what we need to get done in a sprint and our new "feature". 
- Have meetings in the afternoon (morning is more productive)
- How do we handles updates to security conflicts? Do we need to verify that it doesn't break anything. 



We've needed to work on the same task