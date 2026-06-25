import os, re, csv, sys
import numpy as np
D = "Readwise/Full Document Contents/Articles"
TMP = os.environ.get("TMPDIR", "/tmp").rstrip("/")

# tag vocabulary: tag -> rich description sentence (drives zero-shot matching).
# Includes CROSS-CUTTING tags (cost, tokens, metrics, quality, security) so an
# article can carry several.
TAGS = {
 "harness-engineering":"agent harness engineering: the loop, scaffolding and infrastructure that makes an autonomous coding agent reliable and controllable",
 "context-engineering":"context engineering: managing the LLM context window, what tokens to include, compaction, progressive disclosure",
 "claude-md":"writing and structuring CLAUDE.md / AGENTS.md instruction files for coding agents",
 "token-efficiency":"reducing token consumption, fewer tokens, smaller context, token-efficient pipelines",
 "cost-optimization":"reducing AI and API cost, cheaper inference, lowering the price of coding tools",
 "code-intelligence":"codebase indexing, semantic code retrieval, code knowledge graphs so the agent reads only what matters",
 "agent-memory":"persistent memory for coding agents, remembering context across sessions",
 "agent-skills":"reusable agent skills and plugins, skill libraries, skill packages for Claude Code",
 "spec-driven-dev":"spec-driven development and AIDLC: writing PRDs and specs first, BMAD, QRSPI, spec-kit, Kiro, structured plans",
 "multi-agent":"multi-agent orchestration, multiple agents or sub-agents collaborating on a task",
 "alt-agents":"alternative coding agents and IDEs: Pi, OpenClaw, OpenCode, Codex, Cursor, Copilot comparisons",
 "claude-code-ops":"operating Claude Code: sessions, permissions, slash commands, remote use, CLI, daily workflow",
 "agent-git":"git for agents: worktrees, parallel branches, stacked pull requests, devcontainers",
 "agent-testing":"automated testing with agents: end-to-end, Playwright, generating test coverage",
 "evals":"evaluating LLMs and agent skills, eval frameworks, benchmarks",
 "code-quality":"code quality and readability, linters as guardrails, preventing bad or unreadable AI-generated code",
 "code-review":"AI code review, automated review loops, review checklists, catching production incidents",
 "dora-metrics":"DORA metrics and engineering delivery performance, developer productivity dashboards, code-drift metrics",
 "observability":"dashboards, monitoring and auditability of agent or coding sessions",
 "comprehension-debt":"the human bottleneck: comprehension debt, attention, understanding AI-written code, technical debt of agentic coding",
 "mcp":"Model Context Protocol, MCP servers, letting agents take action through tools",
 "browser-automation":"browser automation and computer use for AI agents, Chrome DevTools, web UI automation",
 "voice-ai":"voice AI agents, speech-to-speech, voice coding assistants",
 "media-generation":"generating videos, slides and presentations with AI, Remotion",
 "local-llm":"running local LLMs, GPUs, VRAM, Ollama, quantization, self-hosting models, hardware",
 "llm-fundamentals":"large language model fundamentals, deterministic vs non-deterministic behavior, model overviews",
 "web-security":"web and prompt security, sanitizing input, injection attacks, MCP security",
 "frontend-webapp":"frontend engineering, native-feel web apps, PWAs, performance, HTTP streaming",
 "ux-ui-design":"UI and UX design, building beautiful interfaces, buttons, design systems and design skills",
 "ddd":"domain-driven design, bounded contexts, aggregates, ubiquitous language",
 "clean-architecture":"clean and hexagonal architecture, layering, dependency rules, folder structure",
 "software-patterns":"software design patterns, coupling metrics, refactoring, code katas, test-driven development",
 "data-engineering":"data engineering, data mesh, dbt, change data capture, event sourcing",
 "mdm-governance":"master data management, data governance, data democratization",
 "startup":"startups and founders, pitch decks, fundraising, YC, equity, moats",
 "product-management":"product management, customer interviews, user stories, epics, agile estimation, requirements",
 "ai-industry":"AI industry analysis: the AI bubble, AI economics, hype, executive strategy, opinion pieces",
 "pkm-obsidian":"personal knowledge management, Obsidian, second brain, note-taking systems",
 "productivity":"personal productivity systems, task management, inbox zero",
 "health":"health and medicine, arthritis, joints, regenerative medicine, climbing injuries",
 "real-estate":"real estate, selling a home, brokers, mäklare",
 "non-content":"a login page, sign-in wall, error page, empty placeholder or non-article fragment",
}

def clean_title(fn): return re.sub(r'^#\s*','',os.path.splitext(fn)[0]).strip()
def extract(t):
    m=re.search(r'- Summary:\s*(.+)',t); summ=m.group(1).strip() if m else ""
    fd=re.split(r'##\s*Full Document',t,maxsplit=1); body=fd[1] if len(fd)>1 else t
    body=re.sub(r'```.*?```',' ',body,flags=re.S); body=re.sub(r'!\[.*?\]\(.*?\)',' ',body)
    body=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',body); body=re.sub(r'https?://\S+',' ',body)
    body=re.sub(r'\[\[.*?\]\]',' ',body); body=re.sub(r'[#>*`|]',' ',body); body=re.sub(r'\s+',' ',body).strip()
    return summ,body

titles,docs,files=[],[],[]
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".md"): continue
    dt=clean_title(fn); summ,body=extract(open(os.path.join(D,fn),encoding="utf-8",errors="ignore").read())
    titles.append(dt); files.append(os.path.splitext(fn)[0])
    docs.append(". ".join([dt,dt,summ,summ,body[:2000]]).strip(". ") or dt)
print("docs:",len(docs),"tags:",len(TAGS),flush=True)

from sentence_transformers import SentenceTransformer
m=SentenceTransformer("all-MiniLM-L6-v2")
tag_names=list(TAGS)
TE=m.encode([TAGS[t] for t in tag_names],normalize_embeddings=True)
DE=m.encode(docs,normalize_embeddings=True,show_progress_bar=True,batch_size=32)
S=DE@TE.T   # cosine sims [docs x tags]

def assign(row):
    order=np.argsort(-row); top=row[order[0]]
    out=[]
    for j in order:
        if len(out)>=5: break
        if row[j]>=0.30 or row[j]>=top-0.05:
            out.append((tag_names[j],round(float(row[j]),3)))
        else: break
    return out

assigns=[assign(S[i]) for i in range(len(docs))]

# calibration: show the two articles the user named
print("\n=== CALIBRATION ===")
for needle in ["middlewarehqmiddleware","dirac-rundirac"]:
    for i,t in enumerate(titles):
        if needle.lower() in t.lower().replace(" ",""):
            print(f"\n{t[:70]}")
            for tag,sc in assigns[i]: print(f"    {sc}  {tag}")
# distribution
from collections import Counter
nt=Counter(len(a) for a in assigns); tc=Counter(t for a in assigns for t,_ in a)
print("\ntags-per-article dist:",dict(sorted(nt.items())))
print("\ntop tags:")
for t,c in tc.most_common(20): print(f"  {c:3} {t}")

with open(os.path.join(TMP,"multilabel.csv"),"w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh); w.writerow(["title","file","tags"])
    for i in range(len(docs)):
        w.writerow([titles[i],files[i]," ".join(t for t,_ in assigns[i])])
print("\nsaved ->",os.path.join(TMP,"multilabel.csv"))
