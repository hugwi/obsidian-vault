"""Cover the no-credentials modes: --from-export and --from-feed.

Runs sync.py's real HTTP stack against a fake www.reddit.com on localhost, with
no credentials configured anywhere — the point of this mode.
"""
import importlib.util, json, sys, tempfile, threading, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SYNC_PATH = str(Path(__file__).resolve().parent.parent / "sync.py")
spec = importlib.util.spec_from_file_location("sync", SYNC_PATH)
sync = importlib.util.module_from_spec(spec); spec.loader.exec_module(sync)

fails = []
def check(name, cond, extra=""):
    print(("  ok   " if cond else "  FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond: fails.append(name)

print("== read_export: Reddit's saved_posts.csv ==")
with tempfile.TemporaryDirectory() as td:
    d = Path(td)

    official = d / "saved_posts.csv"
    official.write_text(
        "id,permalink\n"
        "abc123,https://www.reddit.com/r/ClaudeAI/comments/abc123/some_title/\n"
        "def456,https://www.reddit.com/r/obsidianmd/comments/def456/another/\n",
        encoding="utf-8")
    check("parses official export", sync.read_export(official) == ["abc123", "def456"],
          str(sync.read_export(official)))

    perma_only = d / "perma.csv"
    perma_only.write_text(
        "permalink\nhttps://www.reddit.com/r/x/comments/aaa111/t/\n"
        "https://old.reddit.com/r/y/comments/bbb222/t/\n", encoding="utf-8")
    check("permalink-only export", sync.read_export(perma_only) == ["aaa111", "bbb222"],
          str(sync.read_export(perma_only)))

    headerless = d / "urls.txt"
    headerless.write_text(
        "https://www.reddit.com/r/x/comments/ccc333/t/\n"
        "https://www.reddit.com/r/y/comments/ddd444/t/\n", encoding="utf-8")
    check("headerless list of URLs", sync.read_export(headerless) == ["ccc333", "ddd444"],
          str(sync.read_export(headerless)))

    dupes = d / "dupes.csv"
    dupes.write_text("id,permalink\nabc123,x\nabc123,y\nt3_abc123,z\n", encoding="utf-8")
    check("dedupes, strips t3_ prefix", sync.read_export(dupes) == ["abc123"],
          str(sync.read_export(dupes)))

    bom = d / "bom.csv"
    bom.write_bytes("﻿id,permalink\nabc123,x\n".encode("utf-8"))
    check("tolerates BOM", sync.read_export(bom) == ["abc123"], str(sync.read_export(bom)))

    # failure modes exit cleanly rather than tracebacking
    import subprocess
    def run_expect_fail(body, name):
        f = d / name
        f.write_text(body, encoding="utf-8")
        r = subprocess.run([sys.executable, "-c",
            f"import importlib.util;s=importlib.util.spec_from_file_location('s',r'{SYNC_PATH}');"
            f"m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
            f"m.read_export(m.Path(r'{f}'))"], capture_output=True, text=True)
        return r
    r = run_expect_fail("nothing,useful\nfoo,bar\n", "junk.csv")
    check("junk csv exits with guidance", r.returncode == 1 and "saved_posts.csv" in r.stderr,
          r.stderr[:150])
    r = run_expect_fail("", "empty.csv")
    check("empty csv exits cleanly", r.returncode == 1 and "empty" in r.stderr, r.stderr[:150])
    r = subprocess.run([sys.executable, "-c",
        f"import importlib.util;s=importlib.util.spec_from_file_location('s',r'{SYNC_PATH}');"
        f"m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
        f"m.read_export(m.Path(r'{d}/nope.csv'))"], capture_output=True, text=True)
    check("missing file exits cleanly", r.returncode == 1 and "not found" in r.stderr, r.stderr[:150])

print("\n== unauthenticated fetch over HTTP ==")
SEEN = {"paths": [], "headers": []}

def t1(cid, parent, body):
    return {"kind": "t1", "data": {"id": cid, "parent_id": parent, "author": f"u_{cid}",
                                   "body": body, "score": 3, "created_utc": 1752451200,
                                   "replies": ""}}

class FakeWww(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        p = urllib.parse.urlparse(self.path)
        SEEN["paths"].append(p.path)
        SEEN["headers"].append(dict(self.headers))
        if "Authorization" in self.headers:
            return self._send(400, {"error": "anon mode must not send auth"})
        if not p.path.endswith(".json"):
            return self._send(404, {"error": "www requires a .json suffix"})
        pid = p.path.split("/")[2].removesuffix(".json")
        if pid == "gone99":
            return self._send(200, [{"kind": "Listing", "data": {"children": []}},
                                    {"kind": "Listing", "data": {"children": []}}])
        post = {"kind": "t3", "data": {
            "id": pid, "name": f"t3_{pid}", "title": f"Export post {pid}",
            "permalink": f"/r/test/comments/{pid}/slug/", "subreddit": "test",
            "subreddit_name_prefixed": "r/test", "author": "op", "created_utc": 1752451200,
            "score": 77, "num_comments": 2, "selftext": f"Body {pid}.",
            "url": f"https://www.reddit.com/r/test/comments/{pid}/slug/", "domain": "self.test"}}
        return self._send(200, [
            {"kind": "Listing", "data": {"children": [post]}},
            {"kind": "Listing", "data": {"children": [
                t1("k1", f"t3_{pid}", "a comment"), t1("k2", f"t3_{pid}", "another")]}}])
    def _send(self, code, payload):
        b = json.dumps(payload).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

srv = ThreadingHTTPServer(("127.0.0.1", 0), FakeWww)
threading.Thread(target=srv.serve_forever, daemon=True).start()
sync.WWW_BASE = f"http://127.0.0.1:{srv.server_address[1]}"
print(f"fake www.reddit.com on {sync.WWW_BASE}\n")

client = sync.AnonReddit(interval=0.05)
client.base = sync.WWW_BASE
post, comments = client.thread("abc123", max_more=5)
check("fetches post without credentials", post and post["id"] == "abc123", str(post)[:80])
check("fetches comments", len(comments) == 2, str(len(comments)))
check("appends .json for www", SEEN["paths"][0] == "/comments/abc123.json", SEEN["paths"][0])
check("sends no Authorization header", all("Authorization" not in h for h in SEEN["headers"]))
check("still identifies itself", "obsidian-vault-reddit-sync" in SEEN["headers"][0]["User-Agent"])
check("missing post returns None", client.thread("gone99", max_more=0)[0] is None)

print("\n== end-to-end --from-export, zero credentials ==")
with tempfile.TemporaryDirectory() as td:
    d = Path(td); out = d / "Clippings"; out.mkdir()
    csvf = d / "saved_posts.csv"
    csvf.write_text("id,permalink\n"
                    "abc123,https://www.reddit.com/r/test/comments/abc123/a/\n"
                    "def456,https://www.reddit.com/r/test/comments/def456/b/\n"
                    "gone99,https://www.reddit.com/r/test/comments/gone99/c/\n", encoding="utf-8")

    sync.load_config = lambda: {}          # nothing configured at all
    sync.ANON_REQUEST_INTERVAL = 0.05
    orig_anon = sync.AnonReddit
    def fast_anon(verbose=False, interval=0.05):
        c = orig_anon(verbose=verbose, interval=0.05); c.base = sync.WWW_BASE; return c
    sync.AnonReddit = fast_anon

    sys.argv = ["sync.py", "--from-export", str(csvf), "--out", str(out), "--interval", "0.05"]
    rc = sync.main()
    files = sorted(p.name for p in out.glob("*.md"))
    print("    files:", files)
    check("runs with no credentials configured", rc == 1, f"rc={rc} (1 expected: gone99 fails)")
    check("2 good posts written", len(files) == 2, str(files))
    check("deleted post did not abort the run", "Export post def456.md" in files, str(files))

    text = (out / "Export post abc123.md").read_text()
    check("normal frontmatter", 'reddit_id: "t3_abc123"' in text and 'categories:' in text)
    check("comments included", "a comment" in text and "another" in text)

    sys.argv = ["sync.py", "--from-export", str(csvf), "--out", str(out), "--interval", "0.05"]
    n_before = len(SEEN["paths"])
    sync.main()
    check("rerun skips already-synced", len(SEEN["paths"]) - n_before <= 1, "refetched too much")
    check("no duplicate files", len(list(out.glob("*.md"))) == 2)

    with tempfile.TemporaryDirectory() as td2:
        sys.argv = ["sync.py", "--from-export", str(csvf), "--out", td2, "--dry-run",
                    "--limit", "1", "--interval", "0.05"]
        sync.main()
        check("--dry-run + --limit honoured", len(list(Path(td2).glob("*.md"))) == 0)


print("\n== --from-feed: private RSS, no app, unattended ==")
ATOM = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>saved</title>
  <entry><title>One</title>
    <link href="https://www.reddit.com/r/test/comments/abc123/one/" /></entry>
  <entry><title>Two</title>
    <link href="https://www.reddit.com/r/test/comments/def456/two/" /></entry>
  <entry><title>Dupe of one</title>
    <link href="https://www.reddit.com/r/test/comments/abc123/one/" /></entry>
</feed>"""

FEED = {"served": [], "status": 200, "body": ATOM}

class FeedSrv(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        FEED["served"].append(self.path)
        b = FEED["body"].encode()
        self.send_response(FEED["status"])
        self.send_header("Content-Type", "application/atom+xml")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

fsrv = ThreadingHTTPServer(("127.0.0.1", 0), FeedSrv)
threading.Thread(target=fsrv.serve_forever, daemon=True).start()
feed_url = f"http://127.0.0.1:{fsrv.server_address[1]}/saved.rss?feed=TOKEN&user=me"

# fetch_feed_ids sanity-checks that the url mentions reddit.com; satisfy that
# for the local fake server without weakening the check itself.
feed_url_ok = feed_url + "&host=reddit.com"
ids = sync.fetch_feed_ids(feed_url_ok)
check("parses atom feed", ids == ["abc123", "def456"], str(ids))
check("dedupes repeated entries", len(ids) == 2)
check("adds limit=100", "limit=100" in FEED["served"][0], FEED["served"][0])

import subprocess
r = subprocess.run([sys.executable, "-c",
    f"import importlib.util;s=importlib.util.spec_from_file_location('s',r'{SYNC_PATH}');"
    f"m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
    f"m.fetch_feed_ids('https://example.com/feed.rss')"], capture_output=True, text=True)
check("rejects non-reddit url", r.returncode == 1 and "does not look like" in r.stderr, r.stderr[:120])

FEED["body"] = "<feed xmlns='http://www.w3.org/2005/Atom'><title>empty</title></feed>"
r = subprocess.run([sys.executable, "-c",
    f"import importlib.util;s=importlib.util.spec_from_file_location('s',r'{SYNC_PATH}');"
    f"m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
    f"m.fetch_feed_ids('{feed_url_ok}')"], capture_output=True, text=True)
check("empty feed exits with guidance", r.returncode == 1 and "prefs/feeds" in r.stderr, r.stderr[:150])

FEED["status"] = 403
r = subprocess.run([sys.executable, "-c",
    f"import importlib.util;s=importlib.util.spec_from_file_location('s',r'{SYNC_PATH}');"
    f"m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
    f"m.fetch_feed_ids('{feed_url_ok}')"], capture_output=True, text=True)
check("403 tells you the token is stale", r.returncode == 1 and "expired" in r.stderr, r.stderr[:150])
FEED["status"] = 200
FEED["body"] = ATOM

print("\n== end-to-end --from-feed ==")
with tempfile.TemporaryDirectory() as td:
    out = Path(td)
    sync.load_config = lambda: {"REDDIT_SAVED_FEED": feed_url_ok}
    sys.argv = ["sync.py", "--from-feed", "--out", str(out), "--interval", "0.05"]
    rc = sync.main()
    files = sorted(p.name for p in out.glob("*.md"))
    check("feed run needs no credentials", rc == 0, f"rc={rc}")
    check("writes a note per feed entry", len(files) == 2, str(files))
    n = len(FEED["served"])
    sync.main()
    check("rerun skips already-synced", len(list(out.glob("*.md"))) == 2)
    check("feed refetched, posts not", len(FEED["served"]) == n + 1)

    sys.argv = ["sync.py", "--from-feed", feed_url_ok, "--out", str(out), "--interval", "0.05"]
    sync.main()
    check("explicit url overrides .env", len(list(out.glob("*.md"))) == 2)

fsrv.shutdown()

srv.shutdown()
print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILURES: {fails}"))
sys.exit(1 if fails else 0)
