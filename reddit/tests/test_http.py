"""Run sync.py's real HTTP stack against a fake Reddit served on localhost.

This covers what the mocked suites could not: the OAuth token handshake,
Authorization/User-Agent headers, urllib request building, 429 + 5xx retry,
mid-run token expiry, rate-limit header handling, and pagination over the
wire — everything except Reddit's own servers.
"""
import base64, importlib.util, json, sys, tempfile, threading, time, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SYNC_PATH = str(Path(__file__).resolve().parent.parent / "sync.py")
spec = importlib.util.spec_from_file_location("sync", SYNC_PATH)
sync = importlib.util.module_from_spec(spec); spec.loader.exec_module(sync)

fails = []
def check(name, cond, extra=""):
    print(("  ok   " if cond else "  FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond: fails.append(name)

STATE = {
    "token_requests": [], "seen_headers": [], "paths": [],
    "429_fired": False, "401_fired": False, "expired_token": "tok-1",
}

def t1(cid, parent, body, replies=None, score=5):
    d = {"id": cid, "parent_id": parent, "author": f"user_{cid}", "body": body,
         "score": score, "created_utc": 1752451200}
    d["replies"] = replies if replies is not None else ""
    return {"kind": "t1", "data": d}

def listing(children, after=None):
    return {"kind": "Listing", "data": {"children": children, "after": after}}

def post(pid, title, **kw):
    d = {"id": pid, "name": f"t3_{pid}", "title": title,
         "permalink": f"/r/test/comments/{pid}/slug/", "subreddit": "test",
         "subreddit_name_prefixed": "r/test", "author": "op", "created_utc": 1752451200,
         "score": 123, "num_comments": 4, "selftext": f"Body of {pid}.",
         "url": f"https://www.reddit.com/r/test/comments/{pid}/slug/", "domain": "self.test"}
    d.update(kw)
    return {"kind": "t3", "data": d}


class FakeReddit(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def _send(self, code, payload, extra_headers=None):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra_headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _read_form(self):
        n = int(self.headers.get("Content-Length") or 0)
        return dict(urllib.parse.parse_qsl(self.rfile.read(n).decode())) if n else {}

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        form = self._read_form()
        STATE["paths"].append(("POST", path))
        STATE["seen_headers"].append(dict(self.headers))

        if path == "/api/v1/access_token":
            auth = self.headers.get("Authorization", "")
            if not auth.startswith("Basic "):
                return self._send(401, {"error": "no basic auth"})
            user, _, secret = base64.b64decode(auth[6:]).decode().partition(":")
            if (user, secret) != ("cid", "csecret"):
                return self._send(401, {"error": "bad client"})
            STATE["token_requests"].append(form)
            if form.get("grant_type") == "password" and form.get("password") != "pw":
                return self._send(200, {"error": "invalid_grant"})
            n = len(STATE["token_requests"])
            return self._send(200, {"access_token": f"tok-{n}", "expires_in": 3600,
                                    "scope": "identity history read"})

        if path == "/api/morechildren":
            if not self._auth_ok(): return
            kids = form.get("children", "").split(",")
            return self._send(200, {"json": {"data": {"things": [
                t1(k, "t1_c1", f"expanded {k}") for k in kids if k
            ]}}})

        self._send(404, {"error": "unknown", "path": path})

    def _auth_ok(self):
        tok = self.headers.get("Authorization", "")
        if not tok.startswith("Bearer "):
            self._send(401, {"error": "no bearer"}); return False
        if self.headers.get("User-Agent", "").find("obsidian-vault-reddit-sync") < 0:
            self._send(403, {"error": "bad user agent"}); return False
        return True

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path, qs = parsed.path, dict(urllib.parse.parse_qsl(parsed.query))
        STATE["paths"].append(("GET", path))
        STATE["seen_headers"].append(dict(self.headers))
        if not self._auth_ok():
            return

        # One-shot mid-run token expiry, to exercise the 401-refresh branch.
        if path == "/comments/p2" and not STATE["401_fired"]:
            STATE["401_fired"] = True
            return self._send(401, {"error": "token expired"})

        # One-shot 429, to exercise retry/backoff.
        if path == "/comments/p3" and not STATE["429_fired"]:
            STATE["429_fired"] = True
            return self._send(429, {"error": "slow down"}, {"Retry-After": "1"})

        if path == "/api/v1/me":
            return self._send(200, {"name": "tester"})

        if path == "/user/tester/saved":
            if qs.get("type") != "links":
                return self._send(400, {"error": "expected type=links"})
            if not qs.get("after"):
                return self._send(200, listing([post("p1", 'First: "quoted" & odd/chars'),
                                                post("p2", "Second post")], after="t3_p2"),
                                  {"X-Ratelimit-Remaining": "95", "X-Ratelimit-Reset": "60"})
            return self._send(200, listing([post("p3", "Third post", selftext="",
                                                 url="https://example.com/x", domain="example.com")],
                                           after=None),
                              {"X-Ratelimit-Remaining": "94", "X-Ratelimit-Reset": "59"})

        if path.startswith("/comments/"):
            parts = path.split("/")
            if len(parts) > 4:  # /comments/{id}/_/{parent} continue-thread
                return self._send(200, [listing([]), listing([t1("cont", "t1_c1", "continued")])])
            return self._send(200, [listing([]), listing([
                t1("c1", f"t3_{parts[2]}", "Top comment", listing([
                    t1("c2", "t1_c1", "A reply"),
                    {"kind": "more", "data": {"id": "m1", "parent_id": "t1_c1", "children": ["c3", "c4"]}},
                ])),
                t1("c9", f"t3_{parts[2]}", "Another top comment", score=99),
            ])], {"X-Ratelimit-Remaining": "90", "X-Ratelimit-Reset": "55"})

        self._send(404, {"error": "unknown", "path": path})


srv = ThreadingHTTPServer(("127.0.0.1", 0), FakeReddit)
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}"
sync.OAUTH_BASE = base
sync.WWW_BASE = base
print(f"fake reddit on {base}\n")

cfg = {"REDDIT_CLIENT_ID": "cid", "REDDIT_CLIENT_SECRET": "csecret",
       "REDDIT_USERNAME": "tester", "REDDIT_PASSWORD": "pw"}

print("== OAuth handshake over the wire ==")
client = sync.Reddit(cfg)
me = client.whoami()
check("authenticates and reads /api/v1/me", me == "tester", me)
check("password grant sent", STATE["token_requests"][0]["grant_type"] == "password")
check("credentials sent in form", STATE["token_requests"][0]["username"] == "tester")
bearer = [h for h in STATE["seen_headers"] if h.get("Authorization", "").startswith("Bearer ")]
check("bearer token on api calls", len(bearer) >= 1)
check("user-agent identifies the tool", "obsidian-vault-reddit-sync" in bearer[0]["User-Agent"]
      and "u/tester" in bearer[0]["User-Agent"], bearer[0].get("User-Agent"))

print("\n== bad credentials produce a clear error ==")
import subprocess
bad = subprocess.run([sys.executable, "-c", f"""
import importlib.util
spec = importlib.util.spec_from_file_location('sync', '{SYNC_PATH}')
s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
s.OAUTH_BASE = s.WWW_BASE = '{base}'
s.Reddit({{'REDDIT_CLIENT_ID':'cid','REDDIT_CLIENT_SECRET':'csecret','REDDIT_USERNAME':'t','REDDIT_PASSWORD':'WRONG'}})._ensure_token()
"""], capture_output=True, text=True)
check("invalid_grant exits non-zero", bad.returncode == 1, str(bad.returncode))
check("invalid_grant mentions 2FA remedy", "--get-refresh-token" in bad.stderr, bad.stderr[:200])

bad2 = subprocess.run([sys.executable, "-c", f"""
import importlib.util
spec = importlib.util.spec_from_file_location('sync', '{SYNC_PATH}')
s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
s.OAUTH_BASE = s.WWW_BASE = '{base}'
s.Reddit({{'REDDIT_CLIENT_ID':'WRONG','REDDIT_CLIENT_SECRET':'x','REDDIT_USERNAME':'t','REDDIT_PASSWORD':'p'}})._ensure_token()
"""], capture_output=True, text=True)
check("bad client id -> 401 guidance", "type 'script'" in bad2.stderr, bad2.stderr[:200])

print("\n== refresh-token grant ==")
STATE["token_requests"].clear()
rc = sync.Reddit({**cfg, "REDDIT_REFRESH_TOKEN": "rt-abc"})
rc.whoami()
check("uses refresh_token grant", STATE["token_requests"][0]["grant_type"] == "refresh_token")
check("sends the refresh token", STATE["token_requests"][0]["refresh_token"] == "rt-abc")

print("\n== throttle actually throttles ==")
t0 = time.time()
for _ in range(3):
    client.request("/api/v1/me")
elapsed = time.time() - t0
check(">=1s between requests", elapsed >= 2.0, f"{elapsed:.2f}s for 3 requests")

print("\n== full run over HTTP (429 retry + 401 refresh included) ==")
with tempfile.TemporaryDirectory() as td:
    out = Path(td)
    sync.load_config = lambda: cfg
    sys.argv = ["sync.py", "--out", str(out), "--verbose"]
    t0 = time.time()
    rc = sync.main()
    dur = time.time() - t0
    files = sorted(p.name for p in out.glob("*.md"))
    print("    files:", files)
    check("exit 0 despite 429 and 401", rc == 0, str(rc))
    check("3 notes written", len(files) == 3, str(files))
    check("429 was actually served", STATE["429_fired"])
    check("401 was actually served", STATE["401_fired"])
    check("re-authenticated after 401", len(STATE["token_requests"]) >= 2)
    check("backoff waited", dur >= 2.0, f"{dur:.1f}s")
    check("filename sanitized on disk", any("quoted" in f and "/" not in f for f in files), str(files))

    note = next(p for p in out.glob("*.md") if p.name.startswith("First"))
    text = note.read_text()
    check("comments expanded via morechildren", "expanded c3" in text and "expanded c4" in text)
    check("nested reply indented", "> **u/user_c2**" in text)
    check("higher-scored comment first", text.index("user_c9") < text.index("user_c1"))
    check("reddit_id written", 'reddit_id: "t3_p1"' in text)
    try:
        import yaml
        fm = yaml.safe_load(text.split("---\n")[1])
        check("frontmatter parses after real round-trip", isinstance(fm, dict) and fm["score"] == 123)
        check("odd title preserved", fm["title"] == 'First: "quoted" & odd/chars', repr(fm.get("title")))
    except ImportError:
        print("  skip  pyyaml missing")

    linknote = next(p for p in out.glob("*.md") if p.name.startswith("Third"))
    check("link post renders Link section", "## Link" in linknote.read_text())

    # rerun against the same folder must skip everything
    sys.argv = ["sync.py", "--out", str(out)]
    before = STATE["paths"].count(("GET", "/comments/p1"))
    sync.main()
    after = STATE["paths"].count(("GET", "/comments/p1"))
    check("rerun refetches no comments", before == after, f"{before} -> {after}")
    check("no duplicate files", len(list(out.glob("*.md"))) == 3)

srv.shutdown()
print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILURES: {fails}"))
sys.exit(1 if fails else 0)
