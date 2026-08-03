# Handoff — Reddit saved posts → vault sync

**Branch:** `claude/reddit-articles-vault-sync-7l4hny` · **Commit:** `2919522` · **Date:** 2026-08-03
**Status:** code complete and tested; **the import has not been run yet**

---

## The ask

Pull all saved Reddit posts into the vault, and make it run recurrently.

## What was decided

| Question | Choice |
|---|---|
| How to reach Reddit | OAuth API, "script" app (works unattended) |
| Where the schedule runs | Locally, launchd/cron |
| Note contents | Post **plus the full comment tree** |

## What is done

`.reddit-sync/` — zero-dependency Python 3.9+, stdlib only:

| File | Purpose |
|---|---|
| `sync.py` | The sync tool (~700 lines) |
| `.env.example` | Credential template; real `.env` is gitignored |
| `run.sh` | Scheduled-run wrapper — logging + rotation at 2000 lines |
| `com.obsidian.reddit-sync.plist` | launchd job, daily 07:30 |
| `README.md` | Setup, scheduling, flags, limits |

Behaviour: authenticates (password grant, or refresh-token grant if 2FA), pages
the saved listing filtered to link posts, fetches each post's comments and
expands collapsed `more` branches, renders a note into `Clippings/`. Throttled
to ~60 req/min with retry/backoff on 429 and 5xx. Dedupes on the `reddit_id`
frontmatter property, so reruns only fetch new saves.

Note shape follows `CLAUDE.md`: `categories: "[[Clippings]]"`, blank `rating:`
and `action:` so imports surface as untriaged in `Clippings.base`, plus
`platform: reddit`, `subreddit`, `score`, `reddit_id`. Body is the post text
(or outbound link) then comments, nested as blockquotes to 6 levels.

## What is NOT done — the one remaining step

**No saved posts have been imported.** The work was done in a cloud container
where Reddit is blocked by network policy (`CONNECT tunnel failed, 403` for
both `reddit.com` and `oauth.reddit.com`) and where the account credentials
are not available. The import must run wherever the vault lives:

```bash
cd /path/to/vault/.reddit-sync
cp .env.example .env && $EDITOR .env   # app from reddit.com/prefs/apps, type: script
chmod 600 .env
./sync.py --dry-run --limit 5          # verify the note format first
./sync.py                              # full import
```

Expect roughly 10–30 minutes for a few hundred posts — the throttle dominates.

Then schedule it: edit both `VAULT_PATH` placeholders in the plist, copy to
`~/Library/LaunchAgents/`, `launchctl load`, and `launchctl start` once to
confirm. Cron alternative is in `README.md`.

If 2FA is on the account, password login cannot work unattended — run
`./sync.py --get-refresh-token` first and put the token in `.env`.

## Verification

60 assertions across two offline suites, all passing. Covered: filename
sanitization (illegal characters, truncation, unicode, collisions), YAML
escaping round-tripped through a real parser, comment-tree nesting and score
ordering, orphaned comments, the 6-level nesting cap, `more` expansion
including "continue this thread", 100-item batching, `max_more` capping,
listing pagination and the `t1` filter, and an end-to-end run against a mocked
API covering fresh sync, rerun-skips-existing, `--update`, and `--dry-run`.

**Only the live network calls are unverified** — auth handshake, real listing
and comment payloads. That is the risk surface for the first real run. If
something breaks there it will most likely be an auth error, and `sync.py`
prints a specific message for 401 and `invalid_grant`.

## Open items

1. **The ~1000 cap.** Reddit's listing API exposes only roughly the 1000 most
   recent saved items; older saves are unreachable by any API. If the import
   count comes in below what you expect, the full history needs a data export
   from <https://www.reddit.com/settings/data-request> (`saved_posts.csv` has
   every permalink) and a backfill mode reading that CSV. Not built.
2. **Saved comments are skipped** — the listing is filtered to link posts.
3. **Two deliberate deviations** from the existing 443 clippings, either of
   which can be reverted in `render_note()`:
   - `title:` is written only when the filename had to be truncated (100 char
     cap) or sanitized, per `CLAUDE.md`'s "no redundant title" rule. Existing
     clippings all carry `title:`.
   - `author:` is plain text `u/name`, not a `[[wikilink]]` — hundreds of
     redditors would otherwise become unresolved links, and they are not
     People notes in `References/`.
4. **Unsaving on Reddit does not remove the note.** Import is one-way.

## Notes for whoever picks this up

- Credentials must never be committed. The vault auto-commits ("vault backup"
  commits), so `.gitignore` covers `.reddit-sync/.env`, `*.log`, and
  `__pycache__/`. Verified with `git check-ignore`.
- `.reddit-sync/` is dot-prefixed on purpose, matching `.multilabel.py` and
  `.cluster_work/`, so Obsidian does not index it as notes. Do not move it to
  `Templates/Scripts/` — that folder is for `dv.view()` JavaScript, which must
  be in an indexed folder for the opposite reason.
- The pre-existing `Templates/Web Clipper/reddit-summary.json` clipper is
  unrelated and untouched, but note it still writes to `Inbox/Articles` with
  `title:`/`status:`/`tags: clip/discussion` — it predates the flat
  property-driven restructure and is now inconsistent with `CLAUDE.md`.
  Worth fixing separately.
