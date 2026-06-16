# Context Router — Layer B.1 (v1.0)

A Layer B.1 artifact: routes context **selectively** to each slice/session — instead of loading the whole corpus, activates only the relevant **context-experts**. SliceOps IP, CC BY 4.0. Vendor-neutral.

The Context Router is the **consumption** side of context efficiency. Its complement, the **production** side (synthesis efficiency), is documented as an axis of Model Triage (see `../model-triage/`).

---

## Why both sides

The need for context tends to infinity (a serious operator's corpus only grows; richer context is not a defect — it is the reality of mature work). The question is not "how do I reduce my context needs" but "how do I use context well." Two sides:

| Side | What it optimizes | Mechanism |
|---|---|---|
| **Consumption** | How much context is *loaded* per session | **Context Router** (this doc) |
| **Production** | How *densely* context is *created* | **Synthesis efficiency** (`../model-triage/`) |

Production is the upstream cause of future consumption: verbose creation today inflates tomorrow's footprint. P7 corollary: a dense corpus is good training data; a verbose corpus is compounding debt.

---

## Scope honesty

SliceOps does **not** control the model's internal attention architecture (MoE / sparse attention / KV-cache compression are internal to the transformer). The Context Router adopts the **principle** of selective activation — the analog of a gating network — at the **orchestration** level: which context the agent receives, not how the model attends internally.

| Internal architecture analog | Context Router (orchestration) |
|---|---|
| Gating network → top-k experts per token | Router → context-experts relevant to the session (by topic / dependency) |
| Sparse parameter activation | Sparse working set: only the hot context of the current turn |
| Compressed key-value cache | Coordinators load summaries; handoffs transfer contracts |
| Top-k sparse attention | Pruning of stale context between phases |

The principle (selective activation) is universal. The mechanism is orchestrational, not architectural.

---

## Three mechanisms

### 1. Context routing

Per session, **select context-experts**. A **context-expert** is a specialized context module — a cluster of DECs, entities, or code modules grouped by topic or dependency — that can be activated selectively. The ContextPack (entity #8) evolves from a static bundle to a **routed/dynamic** selection: at session start, the router picks the experts relevant to the declared scope, instead of loading the full corpus.

Routing inputs (typical):
- The declared scope of the session (Session-Type, slice-id, declared topics).
- Cross-references in already-loaded entities (transitive expansion).
- Adopter-specific routing rules (Layer C.2).

### 2. Context compression

Coordinators (Orchestrate sessions) load **summaries**, not full contexts. Handoffs (across the DAG) transfer **contracts** (interfaces, accepted criteria, decision references) — not full upstream contexts. A spec/decision/test triplet often replaces a full prior session.

### 3. Sparse working set

Only the **hot** context of the current turn lives in the working set. Prune cold context between phases of a session — the discussion of a decision that has been ratified does not need to stay loaded for the implementation phase that follows. Pruning is explicit and routable (the router can re-load on demand).

---

## Existing primitives (proto-routers)

SliceOps already has several primitives that act as partial routers:

- **ContextPack (entity #8)** — currently static; evolves to routed under this artifact.
- **Brain-pack injection** — routes by repo / workspace (partial: not by topic).
- **Coordinator summaries** — informal compression in Orchestrate sessions.
- **Topic taxonomy** — already supports routing by theme (a routing primitive).

The Context Router is the **coherent pattern** that unifies them — it does not replace; it composes.

---

## Connection to Model Triage and sizing

- **Context-band** (see `../sizing/`) **measures** peak footprint. The Context Router **reduces** it.
- A smaller footprint **expands the feasible set** of Model Triage (more slices fit in smaller windows, so more local / cheaper / private models become viable). This is the direct contribution to **compliance-by-construction**: routing shrinks footprint enough that sensitive work fits in local-mode models.

---

## Why this matters compounding

Routing tightens consumption today; synthesis efficiency keeps tomorrow's corpus from inflating; both compound. P7 reads the corpus as training data — the denser and the better-routed it is, the more leverage each future session has. The two-sided treatment is what makes context efficiency a tractable engineering problem instead of an unbounded one.

---

## Adopter implementation note

The router pattern is vendor-neutral. Concrete implementations (the routing rules, the expert clusters, the integration with a specific agent platform's session-start hook) are **Layer C.2** — adopter-defined. The SliceOps toolkit hosts reference instantiations; adopters extend with stack-specific rules.
