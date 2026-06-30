# Measurement — Build-Complexity Profile + Build Velocity (Layer B.1)

Reproducible, git-derived measurement of **how hard** a build is and **how fast** it
was built — so a "complex *and* fast" claim is *shown*, not asserted. SliceOps IP
(Layer B.1); documentation CC BY 4.0, the reference script MIT.

This artifact is **ex-post measurement** of a shipped build/product. It is orthogonal to:

- [`../sizing/`](../sizing/) — sizes a *slice/session ex ante* (token-band, context-band) for cost and model viability;
- [`../model-triage/`](../model-triage/) — routes a *session* to a (model, execution-mode).

Different unit of analysis (product vs slice) and time orientation (retrospective vs
prospective). It does not replace them.

> **Naming (P12).** This construct is the **Build-Complexity Profile** — deliberately
> *not* the bare word "complexity", which is a reserved canonical term (Model-Triage
> axis #3, a model-selection input), nor "velocity" (P5, Block-level forecast
> recalibration). The folder is `measurement/`, not `velocity/`.

---

## 1. Build velocity — commit-active hours (a proxy)

Worked time is estimated by clustering commit timestamps into sessions; it is **never**
calendar time. It is a **proxy** — it reconstructs time *around commits* and is blind to
design/thinking time, pairing, and review; it over-counts regular-cadence histories and
under-counts think-heavy or AI-bulk work. State the proxy, and the bias direction, next
to any figure.

```
MAXGAP = 120 min   # a gap larger than this starts a new session
FIRST  = 45 min    # credited per session for work before its first commit
total = FIRST ; sessions = 1
for each consecutive pair (t[i-1], t[i]) in sorted commit times:
    gap = t[i] - t[i-1]
    total   += gap if gap <= MAXGAP else FIRST
    sessions += 0   if gap <= MAXGAP else 1
commit_active_hours = total / 3600
```

- **`MAXGAP` and `FIRST` are calibratable defaults, not axioms** — document any change, like `sizing/` documents its bands. `FIRST` dominates a standalone hours figure (report absolute hours as a band over `FIRST ∈ {0, 45}`), but cancels out of the per-point *ratio* (§4), which is robust to it.
- **Commit hygiene (required).** Exclude merge commits and automated commits (auto-sync crons, `*[bot]`, dependabot/renovate) from the clustering — they fabricate sessions. The reference script filters them; a raw `git log` does not.
- **Multi-repo** products **sum** hours (note the over-count: the per-session `FIRST` block is double-counted on days that touched several repos — report as an approximate sum).

## 2. Build-Complexity Profile — six axes, 0–4, anchored rubric

Size is not difficulty. Score each axis 0–4 from **observable, countable criteria**, so the
same repo scores the same twice. **Discard false positives** — matches only in docs,
comments, strings, or CI/validator regexes are not real. **Exclude generated code**
(`/Migrations/`, `*.Designer.cs`, `*ModelSnapshot.cs`, `*.g.dart`, `*.freezed.dart`,
build output, vendored clients).

| Axis | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **State** | no runtime persistence | local/config/in-memory, file-based | one DB, ≤10 entities, single store | >10 entities and/or multiple stores; relational integrity, indexing | partitioned/distributed, append-only/event-sourced, or strong cross-store consistency |
| **Concurrency** | synchronous | basic async/await, no background work | background workers / scheduled jobs, single node | queues + retries + partial-failure, or real-time, or backpressure/circuit-breakers | distributed coordination: locks, consensus, CQRS, cross-service eventual consistency |
| **Integrations** | none | exactly 1 | 2–3 | 4–6 | 7+ |
| **Trust** | none | untrusted input OR a runtime secret | auth/authz OR PII | auth + PII + regulated domain, OR payments | auth + PII + payments + regulated + runtime crypto/key management |
| **Intelligence** | none | isolated LLM/ML call, off the core path | LLM/ML in the per-request path, single model | multi-step LLM orchestration or agents (non-deterministic control) | multi-agent systems with autonomous decisioning in production |
| **Code** | no executable code | avg CCN <3 and <5% of fns over 10 | avg CCN 3–5, or 5–15% over 10 | avg CCN 5–8, or 15–30% over 10 | avg CCN >8, or >30% over 10 |

The **profile (the six values) is the primary artifact.** The composite (sum, 0–24) is an
**equal-weighted index** — equal weight and equal spacing are explicit assumptions, *not*
facts. Label it an index, never a measurement.

**Why 0–4 (not 0–10):** anchored ordinal scales are reliable to ~5–7 levels (Miller 7±2);
beyond that the extra levels cannot be anchored and become noise. 0–10 is false precision.

**Aggregation (multi-repo):** **max per axis** (a product is as hard as its hardest
surface). Do **not** feed the max-assembled composite into the per-point ratio (§4) — it
is an assembled ceiling no single repo exhibits; compute the ratio per-repo or off the
dominant repo's observed profile.

## 3. Code axis — cyclomatic complexity (tool-agnostic)

The Code axis is specified by its **metric**: **average cyclomatic complexity (CCN)** and
the **% of functions with CCN > 10**, mapped to the rubric thresholds. Any conforming CCN
tool may produce it; [`lizard`](https://github.com/terryyin/lizard) is one reference
implementation (`pip install lizard`). The metric is canonical; the tool is not (P11
Platform-Agnostic). Where the parser undercounts (it under-reads JSX/TSX and Dart), mark
the tool number unreliable and **score the axis by reading the densest logic by hand**
(parsers, serializers, state machines, schedulers).

## 4. Speed against difficulty — descriptive, not causal

Read velocity *against* the profile: **commit-active hours per complexity point**.

```
hours_per_point(build) = build.commit_active_hours / build.composite
ratio(build) = baseline.hours_per_point / build.hours_per_point
```

This is **descriptive and uncontrolled.** Matching builds on the composite controls only
*measured technical difficulty* — never era, team size, product maturity, scope-to-date,
accumulated tech-debt, or AI vs no-AI. **Do not phrase it as "N× faster *because of* the
framework"** — that is causal over-claim (a P6 exposure). Phrase it as *"commit-active
hours per complexity point, observed across builds (descriptive, uncontrolled)"*, prefer
**same-lifecycle-stage** comparisons (greenfield-to-v1 vs greenfield-to-v1), and order any
display by complexity descending (the strongest proof leads). The non-causal disclaimer
**travels with the number** wherever it is denormalized (P12 single-source).

### Baseline discipline (the baseline is adopter-specific, not canon)

The ratio requires a baseline. **Each adopter selects and *measures* their own
pre-framework system, re-scored with this same rubric.** SliceOps ships **no baseline
number** — a baseline baked into vendor-neutral canon would be non-reproducible for any
other adopter (P11). A baseline that is **estimated, not measured, invalidates every
ratio built on it** (INS-002 §6). Until an adopter's baseline is measured, ship the
profile and the hours; ship the ratio only marked *"baseline estimated — pending
re-measure"*, or not at all.

## 5. Honesty rules (enforced as gates, not prose)

1. Everything derived from git/code; reason over each signal — never trust a raw grep.
2. Generated code excluded from LOC and from the Code axis.
3. Automated/merge commits excluded from velocity clustering.
4. The composite is an **index**, not a measurement — say so wherever it appears.
5. The X-faster ratio is **descriptive, not causal**; its disclaimer travels with it.
6. The baseline must be **measured**, not estimated.
7. **Validity check:** the composite should correlate with commit-active hours across
   builds; if it does not, the axes or weights are wrong.

## 6. Reference tooling

[`measure.py`](measure.py) (MIT) is a read-only starter: it computes the git-derived
substrate (velocity with commit-hygiene, LOC, decisions, dates, and the Code axis via a
pluggable CCN tool) and emits the result skeleton. The five judgment axes (State,
Concurrency, Integrations, Trust, Intelligence) are scored from §2 against repo evidence —
they are not auto-derivable.

Recalibration of the rubric, the CCN thresholds, and the clustering constants hooks into
the existing **Quarterly Curation ritual (Consistency-Management Layer 6)** — no new
ritual.

## Relation to the principles

This is a **capability**, not a principle (Layer A stays at 12 — INS-005 over-promotion
guard). It operationalizes **P6 (Evidence-by-Construction)** and extends **P2 (Audit
Plane)** to the velocity claim itself; a `measurement` result (e.g. a venture's
`velocity.json`) is an evidence reference suitable for an **OutcomeRecord**.
