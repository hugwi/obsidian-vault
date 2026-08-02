---
type: inspiration
title: Remote video test
categories:
  - "[[Clippings]]"
domain: design
source_url: https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/
platform: commondatastorage.googleapis.com
thumbnail_url: https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/images/BigBuckBunny.jpg
media_url: https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4
saved_at: 2026-08-02
created: 2026-08-02
source: web-clipper
rating: 
action: review
tags:
  - inspiration
  - web-design
  - ui
  - ux
---

# Remote video test

```dataviewjs
await dv.view("Templates/Scripts/remote-video");
```

[Open original source](https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/)

## Notes

- Happy path: `media_url` is a direct MP4, so the renderer shows the thumbnail plus a
  **Load video** button and only attaches the source after the button is pressed.

## Why I saved this

- Verifies the remote-video renderer end to end without writing any MP4 into the vault.
