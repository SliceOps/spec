# Sizing — Bidimensional Slice/Session Sizing (Layer B.1)

A slice or session is sized on **two orthogonal axes** — never conflated into a single composite. SliceOps IP (Layer B.1); CC BY 4.0.

| Axis | Measures | Unit | Governs |
|---|---|---|---|
| **Token-band** | Throughput of the slice/session | **billed-equivalent** tokens | Cost (P12), forecast |
| **Context-band** | Peak context footprint (input and cache in the largest single turn) | tokens | **Model viability** (primary filter of Model Triage) |

A slice can be XL-token / S-context (lots of output, small working set) or S-token / XL-context (little output, must load a large codebase). They are independent.

---

## Token-band — throughput, in billed-equivalent

**Unit is critical**: throughput is measured as `input + cache_creation × 1.25 + cache_read × 0.1 + output`, NOT total-with-cache (which inflates by ~5×). Fixing the unit prevents measurement drift (the failure mode formalized in the corpus as "denormalized count drift"). The bands below are calibrated against billed-equivalent.

| Band | Range (billed-equivalent) |
|---|---|
| XS | < 2M |
| S | 2–5M |
| M | 5–10M |
| L | 10–20M |
| XL | > 20M (red flag) |

Token-band governs cost (P12) and forecast. It is the throughput band — independent of how much context the model had to *carry* per turn.

---

## Context-band — peak footprint, model-viability filter

`max` across turns of `input_tokens + cache_creation_input_tokens + cache_read_input_tokens` — the maximum context loaded in the largest single turn of the session. Anchored to real model windows and the empirical distribution:

| Band | Range (peak footprint) |
|---|---|
| XS | < 32K |
| S | 32–128K |
| M | 128–200K |
| L | 200–512K |
| XL | > 512K |

Context-band governs **viability** of a model: a model whose context window is smaller than the slice's footprint cannot run the slice, no matter its cost or speed. This is why context-band is the **primary filter** in Model Triage (see `../model-triage/`) — it sets the feasible set first, before any other axis applies.

---

## Calibration discipline

The bands are **calibrated against real data and the vigent model landscape, NOT axiomatic**. Three rules:

1. **Reproducible** — a versioned deterministic script parses a real session corpus (`.jsonl`) → peak-footprint and billed-equivalent throughput → percentiles → bands. NOT ad-hoc per calibration. Materializes Determinism-over-Regeneration (the script is written once and reused). Reference implementation: the SliceOps toolkit `calibration/`.
2. **Quarterly cadence** — recalibration hooks into the Quarterly Curation Ritual (Layer 6 of the consistency-management mechanism). Not a new ritual; a Layer 6 item.
3. **Versioned** — each calibration records `date, script-version, dataset (N sessions, corpus), model landscape, percentiles, resulting bands`. Drift over time is auditable. The historical record is the **band-calibration-register** (lives alongside the script).

### Why recalibrate

Model context windows and capability change. Frontier-class windows have grown from 200K → 1M → … ; local models are climbing from 8K → 32K → 128K. Static bands age silently. Quarterly recalibration keeps the triage aligned with the real landscape.

### Baseline v1 (2026-06-15) — model landscape

The first calibration anchored the bands against this landscape (recorded for audit; recalibration is triggered when this changes materially):

- **Frontier long-context**: ~1M (the calibration model class) and ~1M+ peers.
- **Claude-class**: ~200K.
- **GPT-class**: ~128K.
- **Local-medium**: ~32K (Qwen/Llama mainstream).
- **Local-small**: ~8K.

When local-medium reaches mainstream 128K, or frontier crosses ~2M, **recalibrate context-band**.

---

## Why bidimensional

A single composite size axis conflates throughput and footprint and fails honestly:

- A local model with a small window may have **plenty** of throughput capacity but cannot fit the slice's footprint, so it fails on **viability**, not cost.
- A frontier model may have ample window but the slice still costs a lot, so it fails on **cost**, not viability.

Cost and viability are different failure modes; they need different bands. P1 already named "context window finita" in its rationale; only the throughput (cost) had been operationalized as token-band. Context-band closes the missing axis.

---

## Sizing in the Session record

Both bands are recorded on the Session entity (#13) as `token_band` and `context_band`. Together with `model_used`, `execution_mode`, and `triage_rationale` they form the auditable provenance of "why this model was chosen for this work" — the audit-plane (P2) extended to the model-selection decision.
