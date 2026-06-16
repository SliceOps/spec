# Model Triage — Layer B.1 (v1.0)

A Layer B.1 artifact: routes each slice/session to a **(model, execution-mode)** recommendation according to five axes, in filter order. Recommends; the human disposes (P9). The choice is recorded on the Session record as auditable provenance (P2 — the audit plane extended to the model-selection decision).

SliceOps IP, CC BY 4.0. Vendor-neutral.

---

## The five axes (in filter order)

```
1. context-band  → PRIMARY FILTER: which models have window ≥ footprint? (hard restriction)
2. sensitivity   → locality: can the work leave to an external API or must it stay local? (P6)
   ── feasible set bounded ──
3. complexity    → reasoning tier (token-band + slice-type → which capability tier?)
4. latency       → speed need
5. cost          → economic tier (P12)
                 → recommendation
```

Plus a **synthesis efficiency** axis (see below) used when the slice is context-producing.

### Why context-band is primary

A model whose window is smaller than the slice's footprint cannot run the slice — full stop. No amount of speed or low cost recovers from a context overflow. Context-band sets the feasible set first; all other axes refine within it. Empirically the dominant restriction: in the baseline calibration, the majority of real sessions exceed a 200K window — a smaller local model is infeasible for most work even before cost or speed enters the conversation.

### Sensitivity → locality (P6)

If the work touches restricted/sensitive data (per the `sensitivity` field on the Session), the triage filters to **local** execution modes only — never to an external API, regardless of cost or speed advantages. This is compliance-by-construction for regulated work.

### Complexity, latency, cost

Within the feasible set:
- **Complexity** = token-band + Slice-Type (Dev vs Refactor vs Fix vs adopter-specific) → reasoning capability tier.
- **Latency** = how fast a human needs the response (interactive vs background batch).
- **Cost** = the economic tier within the feasible set (P12 — cheapest adequate model wins; see also the LLM-Inference-Cost-Economy B.2 sub-pattern).

---

## Execution-modes

How the slice is executed against the chosen model:

| Mode | Where the model runs | Typical use |
|---|---|---|
| `frontier-API` | A frontier model accessed via an external API | High-complexity, non-sensitive work |
| `local-via-API` | A locally-hosted model exposed via API (e.g., local server) | Sensitive work that requires local capability |
| `account-with-plan` | A subscription whose cost is already paid (flat-rate plan) | Bulk work where marginal cost is zero |
| `local-in-IDE` | A local model integrated directly into the IDE | Lightweight inline assist, full locality |

The execution mode is recorded on the Session as `execution_mode` for audit.

---

## Synthesis efficiency — the producing axis

An additional Model Triage axis: the **semantic density** with which a model creates context (information preserved per output token). Two practical consequences:

### context-consuming vs context-producing slices

| Orientation | What dominates | Triage prioritizes |
|---|---|---|
| **context-consuming** | Reading (analysis over existing code/corpus) | Window size (axis 1) |
| **context-producing** | Writing (specs/docs/code/refactor) | Synthesis efficiency (this axis) |
| **mixed** | Both, balanced | Both — favor a model that scores well on both |

A model optimal for consuming is not necessarily optimal for producing. Calibrate per model.

### Measuring synthesis efficiency

A calibrable model attribute. **Proxy**: given the same fixed acceptance criteria, count the output tokens required for the artifact to pass the gate. Lower tokens = denser synthesis. Calibrate per model at the same Quarterly Curation cadence as the bands.

**Caveat**: density ≠ blind terseness. The optimum is maximum density that still passes the acceptance gate (P5) and remains auditable (P2). Code-golf extremes are anti-patterns.

---

## Where it differentiates

Closed and opaque competitors hard-code a model or route invisibly between a small set. SliceOps's triage is **explicit and auditable** — Wedge A (audit plane) applied to the model-selection decision. The sensitivity → locality axis makes it **compliance-by-construction** for regulated work: sensitive slices are routed to local execution by policy, never to an external API by accident.

---

## Conflict surfacing (P9 HITL)

When axes conflict — e.g., an XL-context slice (needs a large window) that is high-sensitivity (cannot leave) — the triage **surfaces the tension** rather than silently picking. The human decides: split the slice to lower the footprint, use a local long-context model, or accept the risk (with a rationale recorded). Surfacing > guessing.

---

## What is recorded on the Session

For audit, every triaged session carries:

- `model_used` — the identifier of the chosen model.
- `execution_mode` — one of the four canonical modes.
- `triage_rationale` — a one-line statement of which axis decided it (e.g., "context-band drove it: footprint > 200K → frontier long-context required").
- `context_orientation` — `consuming` | `producing` | `mixed`.

Nobody else audits *why* a model was chosen for a piece of work. SliceOps does.
