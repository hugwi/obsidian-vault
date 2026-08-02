---
created: 2026-08-02
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - youtube
  - video
  - transcript
  - workflow
---

# YouTube Archive

Download saved YouTube videos into the vault and get a **timestamped transcript** as a
normal note you can search, link and quote. Two paths, same note shape:

| Path | Gets the video file | Gets a transcript | Use when |
|---|---|---|---|
| `youtube_archive.py` (below) | ✅ into `Attachments/Videos/` | ✅ captions, or Whisper | You want to keep the video |
| **YouTube - Summary** Web Clipper | ❌ | ✅ scraped from the page | You're already in the browser |

Both write to `Clippings/` with `type: video` — browse them in
`Clippings.base` → **🎬 Videos**, or [[Clippings]].

## One-time setup

```bash
brew install yt-dlp ffmpeg          # macOS; or: pipx install yt-dlp
```

`ffmpeg` is what merges YouTube's separate video and audio streams — without it you get
audio-only or low-resolution files. Optional, for videos with captions disabled:

```bash
pipx install openai-whisper         # then pass --whisper
```

## Usage

The script lives at `Templates/Scripts/youtube-archive/youtube_archive.py` and finds the
vault by its own location, so it works from anywhere:

```bash
cd ~/path/to/vault/Templates/Scripts/youtube-archive

# one video
./youtube_archive.py "https://www.youtube.com/watch?v=VIDEO_ID"

# your Watch Later — needs cookies from a logged-in browser
./youtube_archive.py --cookies-from-browser chrome WL

# liked videos, 10 most recent, transcripts only (no media)
./youtube_archive.py --cookies-from-browser chrome --no-media --limit 10 LL

# any playlist
./youtube_archive.py "https://www.youtube.com/playlist?list=PL..."
```

`WL` = Watch Later, `LL` = Liked videos. Both are private, so they need
`--cookies-from-browser chrome|firefox|safari|brave|edge` (Safari and Chrome may ask for
keychain access the first time). Public and unlisted playlists need no cookies.

### Options worth knowing

| Flag | Effect |
|---|---|
| `--no-media` | Note + transcript only, nothing downloaded. Cheapest way to make a video searchable. |
| `--audio-only` | Keep an `.m4a` instead of the video — a fraction of the size, still playable in Obsidian. |
| `--max-height 720` | Cap resolution (default 1080). |
| `--whisper [model]` | Transcribe locally when the video has no captions (`base`, `small`, `medium`…). Slow, offline, no API key. |
| `--limit N` | Take only the first N of a playlist. |
| `--force` | Re-download and overwrite an existing note (rebuilds a Web Clipper note into a full archive note). |
| `--dry-run` | List what would be archived. |
| `--lang "de.*,de"` | Non-English captions. |

Re-runs are **idempotent**: a video whose note already exists is skipped, so pointing the
script at Watch Later on a schedule only ever picks up what's new.

## What you get

```
Attachments/Videos/Title (VIDEO_ID).mp4        ← the video (git-ignored, Syncthing-synced)
Clippings/Title (VIDEO_ID).md                  ← the note (committed)
```

The note carries `type: video`, `channel`, `duration`, `published`, `url`, `video_id`,
`media`, `transcript_source`, plus the usual `categories: "[[Clippings]]"`, `rating:` and
`action:` triage props. The body is the embedded player, chapters, description, and the
transcript broken into ~45-second paragraphs, each stamped with a link back into the
video:

```markdown
**[12:34](https://youtu.be/VIDEO_ID?t=754)** the words spoken at that point …
```

Clicking a timestamp opens YouTube at that second — handy when the transcript is enough to
find the moment but you want to watch it.

Captions are preferred over auto-captions, which are cleaned up on the way in: the
scrolling duplicate lines and per-word `<c>` timing tags YouTube emits are stripped.
`transcript_source` records which you got — `captions`, `whisper`, `web-clipper` or `none`.

## Media stays out of git

`Attachments/Videos/` is in `.gitignore` (along with `*.mp4`, `*.mkv`, `*.webm`, `*.m4a`)
so the repo stays small — **notes and transcripts are committed, video files are not**.
The files still travel between your machines over Syncthing like the rest of
`Attachments/`. A fresh `git clone` gets every transcript and a broken embed where the
video would be; re-run the script to refill it.

Keeping a lot of these? `--audio-only` or `--no-media` is usually the right default —
the transcript is what makes the video useful to the vault, and it's ~50 KB against a
video's ~500 MB.

## Keeping it topped up

There's no scheduler wired up. If you want one, a `launchd` job or a cron line is enough:

```bash
0 8 * * *  cd ~/path/to/vault/Templates/Scripts/youtube-archive && \
           ./youtube_archive.py --cookies-from-browser chrome --no-media WL
```

Cookies expire when you log out of YouTube; if a run suddenly returns nothing for `WL`,
that's usually why.

## Troubleshooting

- **`ERROR: Sign in to confirm you're not a bot`** — pass `--cookies-from-browser`, or wait
  a bit; YouTube rate-limits unauthenticated bulk requests.
- **No transcript** (`transcript_source: none`) — the video has captions disabled. Re-run
  with `--whisper` (needs the media, so not with `--no-media`).
- **Video won't play in Obsidian** — it's probably `.webm`; Obsidian plays `.mp4`/`.m4a`
  reliably. Make sure `ffmpeg` is installed so yt-dlp can remux to mp4.
- **yt-dlp suddenly failing on everything** — YouTube changed something; `brew upgrade
  yt-dlp` (it ships fixes constantly).

## Related

- [[Clippings]] · `Clippings.base` → **🎬 Videos**
- Web Clipper templates: `Templates/Web Clipper/README.md`
- Remote-only media (design inspiration, nothing downloaded): [[Inspiration]]
