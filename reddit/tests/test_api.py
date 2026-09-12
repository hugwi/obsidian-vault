from pathlib import Path
"""Exercise the listing-flatten + morechildren expansion against fake API payloads."""
import importlib.util, sys
SYNC_PATH = str(Path(__file__).resolve().parent.parent / "sync.py")
spec = importlib.util.spec_from_file_location("sync", SYNC_PATH)
sync = importlib.util.module_from_spec(spec); spec.loader.exec_module(sync)

fails = []
def check(name, cond, extra=""):
    print(("  ok   " if cond else "  FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond: fails.append(name)

def t1(cid, parent, body, replies=None, score=1):
    d = {"id": cid, "parent_id": parent, "author": "u", "body": body, "score": score, "created_utc": 1752451200}
    d["replies"] = replies if replies is not None else ""
    return {"kind": "t1", "data": d}

def listing(children):
    return {"kind": "Listing", "data": {"children": children}}

print("== _walk_listing: nested replies flattened ==")
payload = listing([
    t1("a", "t3_p", "root a", listing([
        t1("b", "t1_a", "reply b", listing([t1("c", "t1_b", "reply c")])),
        {"kind": "more", "data": {"id": "m1", "parent_id": "t1_a", "children": ["x1", "x2"]}},
    ])),
    t1("d", "t3_p", "root d"),
])
flat, pending = {}, []
sync._walk_listing(payload, flat, pending)
check("flattens 4 comments", sorted(flat) == ["a","b","c","d"], sorted(flat))
check("collects 1 more node", len(pending) == 1 and pending[0]["children"] == ["x1","x2"])
check("empty replies string safe", flat["d"]["replies"] == "")

print("\n== dedupe on repeated ids ==")
sync._walk_listing(payload, flat, pending)
check("no duplicate comments", len(flat) == 4)

print("\n== full Reddit.comments() with mocked transport ==")
class FakeClient(sync.Reddit):
    def __init__(self):
        self.requests = []
    def request(self, path, params=None, post_data=None):
        self.requests.append((path, params, post_data))
        if path == "/comments/p":
            return [listing([]), listing([
                t1("a", "t3_p", "root a", listing([
                    {"kind": "more", "data": {"id": "m1", "parent_id": "t1_a", "children": ["b", "c"]}},
                ])),
                {"kind": "more", "data": {"id": "_", "parent_id": "t1_a", "children": []}},
            ])]
        if path == "/api/morechildren":
            return {"json": {"data": {"things": [
                t1("b", "t1_a", "expanded b"),
                t1("c", "t1_a", "expanded c", listing([t1("e", "t1_c", "nested under expanded")])),
            ]}}}
        if path.startswith("/comments/p/_/"):
            return [listing([]), listing([t1("f", "t1_a", "continue-thread comment")])]
        raise AssertionError(path)

fc = FakeClient()
result = fc.comments("p", max_more=20)
ids = sorted(c["id"] for c in result)
check("expands morechildren", "b" in ids and "c" in ids, ids)
check("expands nested reply inside morechildren", "e" in ids, ids)
check("handles continue-thread more", "f" in ids, ids)
check("all 5 comments", ids == ["a","b","c","e","f"], ids)
check("morechildren was POSTed with link_id", any(p == "/api/morechildren" and d and d["link_id"] == "t3_p" for p, _, d in fc.requests))
check("children joined by comma", any(d and d.get("children") == "b,c" for _, _, d in fc.requests))

print("\n== max_more cap is respected ==")
class BigClient(sync.Reddit):
    def __init__(self): self.n = 0
    def request(self, path, params=None, post_data=None):
        if path == "/comments/p":
            return [listing([]), listing([t1("a", "t3_p", "root")] + [
                {"kind": "more", "data": {"id": f"m{i}", "parent_id": "t1_a", "children": [f"x{i}"]}} for i in range(50)
            ])]
        self.n += 1
        return {"json": {"data": {"things": []}}}
bc = BigClient()
bc.comments("p", max_more=3)
check("stops at max_more requests", bc.n == 3, f"n={bc.n}")

print("\n== batching >100 children ==")
class BatchClient(sync.Reddit):
    def __init__(self): self.batches = []
    def request(self, path, params=None, post_data=None):
        if path == "/comments/p":
            kids = [f"k{i}" for i in range(250)]
            return [listing([]), listing([{"kind": "more", "data": {"id": "m", "parent_id": "t3_p", "children": kids}}])]
        self.batches.append(len(post_data["children"].split(",")))
        return {"json": {"data": {"things": []}}}
bcl = BatchClient()
bcl.comments("p", max_more=20)
check("splits into 100-max batches", bcl.batches == [100, 100, 50], str(bcl.batches))

print("\n== saved_posts pagination + type filter ==")
class PagedClient(sync.Reddit):
    username = "tester"
    def __init__(self): self.pages = 0
    def request(self, path, params=None, post_data=None):
        assert params["type"] == "links", params
        self.pages += 1
        if self.pages == 1:
            return {"data": {"children": [{"kind": "t3", "data": {"id": f"p{i}"}} for i in range(100)], "after": "t3_p99"}}
        if self.pages == 2:
            return {"data": {"children": [
                {"kind": "t3", "data": {"id": "p100"}},
                {"kind": "t1", "data": {"id": "comment-should-be-skipped"}},
            ], "after": None}}
        raise AssertionError("paged past the end")
pc = PagedClient()
got = list(pc.saved_posts())
check("paginates via after cursor", len(got) == 101, len(got))
check("filters out t1 saved comments", all(g["id"] != "comment-should-be-skipped" for g in got))
pc2 = PagedClient()
check("--limit stops early", len(list(pc2.saved_posts(limit=5))) == 5)

print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILURES: {fails}"))
sys.exit(1 if fails else 0)
