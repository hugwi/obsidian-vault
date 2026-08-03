# Reddit saved posts → Clippings

Pulls your saved Reddit posts into `Clippings/` as one note per post, with the
full comment tree, using the vault's normal frontmatter conventions. Re-running
is cheap: posts already synced are skipped, so this is safe on a schedule.

Python 3.9+ standard library only — nothing to `pip install`.

There are two ways to run it. **Export mode needs no Reddit app and no
credentials** — start there if app creation is a hassle.

| | API mode (default) | Export mode (`--from-export`) |
|---|---|---|
| Reddit app | required | **none** |
| Credentials | required | **none** |
| History reachable | ~1000 most recent saves | **everything** |
| Can run unattended | yes | no (manual export each time) |
| Speed | ~1 post/sec | ~1 post/3sec |

The usual setup is both: export mode once to backfill everything, then API
mode on a schedule to keep up with new saves.

## Export mode — no app, no credentials

1. Request your data at <https://www.reddit.com/settings/data-request>
   (choose GDPR or CCPA; the archive arrives by email, usually within a day).
2. Unzip it and find `saved_posts.csv`.
3. Run:

```bash
./sync.py --from-export ~/Downloads/export/saved_posts.csv --dry-run --limit 5
./sync.py --from-export ~/Downloads/export/saved_posts.csv
```

This reads Reddit's public JSON endpoints, which need no authentication. It
is deliberately slow — unauthenticated requests are rate limited hard, so it
waits 3 seconds between posts (`--interval` to change, at your own risk).
2000 saved posts is about 100 minutes. Leave it running.

It also accepts a plain file of thread URLs, one per line, if you would
rather hand-pick.

## API mode setup

**1. Create a Reddit app** at <https://www.reddit.com/prefs/apps> →
*create another app…*

> If that page no longer offers app creation, try
> <https://old.reddit.com/prefs/apps/>, which still shows the
> "create another app…" button. Reddit's newer **Devvit** developer platform
> is for apps that run *on* Reddit and cannot issue script credentials — it
> is not what this needs. If you cannot create an app at all, use export mode
> above; it does everything except run unattended.

- type: **script**
- redirect uri: `http://localhost:8080`

The client id is the string shown under the app name; the secret is labelled
*secret*.

**2. Fill in credentials**

```bash
cd /path/to/vault/.reddit-sync
cp .env.example .env
$EDITOR .env
chmod 600 .env
```

`.env` is gitignored — the vault auto-commits, so keep credentials only there.

**If 2FA is enabled** on your Reddit account, password login cannot work
unattended. Run `./sync.py --get-refresh-token` once, follow the prompts, put
the resulting `REDDIT_REFRESH_TOKEN` in `.env`, and remove `REDDIT_PASSWORD`.

**3. Try it**

```bash
./sync.py --dry-run --limit 5   # writes nothing, shows what it would do
./sync.py --limit 5             # write 5 notes for real
./sync.py                       # full sync
```

The first full run takes a while: each post costs at least one request for the
post plus one or more for comments, deliberately throttled to ~60 requests/min
to stay under Reddit's limit. A few hundred saved posts means roughly 10–30
minutes. Later runs only touch new saves.

## Scheduling

### launchd (macOS, recommended)

```bash
# edit the file first: replace both VAULT_PATH occurrences with your real path
cp com.obsidian.reddit-sync.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.obsidian.reddit-sync.plist
launchctl start com.obsidian.reddit-sync   # run once now to verify
```

Runs daily at 07:30. Output goes to `sync.log` in this folder.

To remove it:
`launchctl unload ~/Library/LaunchAgents/com.obsidian.reddit-sync.plist`

### cron (Linux, or if you prefer it)

```cron
30 7 * * * /bin/bash /path/to/vault/.reddit-sync/run.sh
```

`run.sh` handles the working directory, appends to `sync.log`, and trims that
log at 2000 lines.

## What a note looks like

```yaml
---
categories:
  - "[[Clippings]]"
source: "https://www.reddit.com/r/ClaudeAI/comments/abc123/..."
author: "u/someone"
published: 2026-07-14
created: 2026-08-03
rating:
action:
description: "First ~200 characters of the post body…"
type: discussion
platform: reddit
subreddit: "r/ClaudeAI"
score: 412
reddit_id: "t3_abc123"
tags:
  - "clippings"
  - "reddit"
---
```

Then the post body (or the outbound link, for link posts) and the comment
tree, with replies nested as blockquotes up to 6 levels deep.

`rating:` and `action:` are left blank on purpose — they are your triage
fields, so `Clippings.base` surfaces new imports as untriaged.

Notes match the vault conventions in `CLAUDE.md`:

- `title:` is omitted when the filename already is the full title, and only
  written when the title had to be truncated (filenames cap at 100 characters)
  or contained characters illegal in a filename.
- `author:` is plain text `u/name`, not a `[[wikilink]]` — hundreds of
  redditors would otherwise become unresolved links, and they are not People
  notes in `References/`.

## Options

| Flag | Effect |
|---|---|
| `--dry-run` | Report what would change, write nothing |
| `--limit N` | Only the N most recently saved posts |
| `--update` | Rewrite notes for posts already synced (refreshes scores/comments) |
| `--no-comments` | Post body only, much faster |
| `--max-more N` | Cap extra requests per post for expanding collapsed comment branches (default 20) |
| `--from-export CSV` | Backfill from a data-export `saved_posts.csv` — no app or credentials needed |
| `--interval S` | Seconds between requests in export mode (default 3.0) |
| `--out DIR` | Write somewhere other than `Clippings/` |
| `--verbose` | Log skips and token activity |

## Tests

```bash
./tests/run.sh
```

112 assertions, no credentials or network required — `tests/test_http.py`
serves a fake Reddit on localhost and drives the real HTTP stack against it
(OAuth grants, headers, throttle, 429 backoff, mid-run token expiry,
pagination), and `test_export.py` does the same for the unauthenticated
export path. Takes about 30 seconds, most of it the deliberate throttle and
backoff waits. Worth running after any edit to `sync.py`.

## Known limits

- **~1000 saved items in API mode.** Reddit's listing API exposes only
  roughly your 1000 most recent saved items. Use `--from-export` for the rest;
  the data export has every permalink and export mode has no cap.
- **Saved comments are skipped.** The listing is filtered to link posts
  (`type=links`). Saved *comments* are not imported.
- **Very large threads.** `--max-more` caps how hard the script works to
  expand "load more comments" branches. When it runs out it says so in the log
  rather than silently dropping them; raise the cap for those posts.
- **Deleted/removed content** appears as `[deleted]` / `_[removed]_`, which is
  all the API returns.
- Unsaving a post on Reddit does not delete the note here — imports are
  one-way by design.
