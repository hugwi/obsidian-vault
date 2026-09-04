---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-09-04
---

# Server operations — memory and swap on rtx-3090

The host running the OpenCode telemetry stack: 30 GiB RAM, 8 GiB swap
(`/swap.img` file, zswap disabled, swappiness 60 → 10). Box also runs model
containers (Qwen3-4B, gemma-12b, vocis voice worker) and several coding-agent
sessions, so memory is routinely near-full by design. Knowing *what is actually
dangerous* here is the difference between an actionable alert and nightly noise.

## The core lesson

**A full swap file is not the problem. A full swap file with little free RAM is.**
Cold pages parked on swap cost nothing while RAM is plentiful — a fault just
reads the page back in. The OOM killer only reaps when a fault cannot be served
from RAM at all. So the alert condition is the *pair*, not either alone:

- swap usage crossing ~95% **AND** MemAvailable < ~15% → genuine OOM territory.
- swap at 80–90% with 10+ GiB RAM available → parked cold pages, fine. Do nothing.

## Alert configuration (ai-telemetry repo)

`~/ai-telemetry/prometheus-rules/host-resources.yml`, rule `HostSwapPressure`:

```yaml
expr: (1 - node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes) > 0.95
      and node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes < 0.15
for: 10m
```

Reload without restart: validate with `promtool` inside the container, then hit
the lifecycle endpoint:

```bash
docker exec prometheus sh -c 'promtool check rules /etc/prometheus/rules/*.yml'
curl -s -X POST localhost:9090/-/reload
```

`HostMemoryPressure` (MemAvailable < 10%) is the earlier warning; the swap rule
is the critical follow-on. Do not loosen the swap rule back to a single high
percentage — that is exactly what produced false "panic" pages.

## Diagnosis quickstart

```bash
free -h                              # 30Gi RAM / 8Gi swap
vmstat 1 5                           # si/so ≈ 0 while idle = parked, not thrashing
cat /proc/sys/vm/swappiness          # 60 → lowered to 10 (below)
```

Host `ps` lies about swap on this box: `/proc/<pid>/status` `Swap:` reads zero
for swapped containers, and the biggest host user (`t3code.service`) shows ~94 MB
RSS while holding 3+ GiB on swap. Attribute swap truthfully via cgroups:

```bash
# per-container:
docker inspect -f '{{.Name}}' <cid>; cat "/sys/fs/cgroup$(cat /proc/<pid>/cgroup | cut -d/ -f2-)/memory.swap.current"

# host services (systemd):
find /sys/fs/cgroup/user.slice -name memory.swap.current \
  -exec sh -c 'v=$(cat "$1"); [ "$v" -gt 0 ] && printf "%9d $1\n" "$v"' _ {} \; | sort -rn
```

Known swap consumers (measured 2026-09-04): `t3code.service` ≈ 3.3 GiB (cold,
idle), `llm-models-brain-cpu-1` (Qwen3-4B) ≈ 1.3 GiB, `omnigent-voice-worker-1`
(vocis) ≈ 1.0 GiB, `llm-models-gemma-12b` ≈ 0.24 GiB.

## Tuning choices and non-choices

- **Keep the 8 GiB swap.** It is genuinely used (6+ GiB parked) and model
  containers burst. Shrinking to 4 GiB raises OOM odds right when the workload
  spikes

  and a resize is downtime (`swapoff` writes it all back into RAM first).
- **Lowered `swappiness` 60 → 10** (2026-09-04) so the kernel stops parking idle
  process pages so eagerly — that eager parking is what filled swap with cold
  t3/opencode pages and drove the old 80% alert. Persistent via
  `/etc/sysctl.d/99-low-swappiness.conf`.
- If swap is full of *cold* pages and you want headroom back, restart the
  biggest idle holder rather than touching swap size — `systemctl restart
  t3code` frees ~3 GiB of swap instantly. Caveat: that bridge may carry the
  very session doing the restart.

## Related

- OmniGent / Vocis tailnet exposure and the gateway stack: see the ai-telemetry
  repo `ARCHITECTURE.md` and the OpenCode Telemetry notes.