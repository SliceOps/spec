---
entity: DecisionRecord
status: ratified
created: 2026-05-14
updated: 2026-06-22
owner: Andrés Ramírez Sierra
sensitivity: public
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DR-2026-05-12-three-layer-ip-boundary]
topics: [folder-structure, meta-framework, layer-b-framework-artifact]
vocabulary-changes: []
consistency-check: "Records the publishing layout of this repo (5 folders + 7 root files) and its folder-promotion criteria; preserves the Layer B.1 frame from DR-2026-05-12-three-layer-ip-boundary (folder structure is framework IP); deliberately distinct from the prescribed adopter project structure in reference/project-structure/. No conflicts."
---

# DR-2026-05-14 — Spec Repo Publishing Layout

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 Audit Plane, P1 Decision Integrity). This record publishes the decision; the supporting industry survey and analysis are maintained internally.

## TL;DR

This repository publishes itself with a **lightweight, industry-aligned layout — 5 top-level folders + 7 root files** — and grows folders only when explicit promotion criteria are met. This is **distinct on purpose** from the foundations-first project structure the framework *prescribes* to adopters (see [`reference/project-structure/`](../../reference/project-structure/)): dogfooding is of the *process*, not of the *physical schema*.

## Decision

The canonical publishing layout of this spec repository is:

```
spec/        ← versioned canonical framework spec (spec/vX.Y.Z/)
reference/   ← reusable patterns, templates, schemas (Layer B.1 + B.2)
decisions/   ← DECs about the framework itself (accepted/superseded/deprecated/rfcs)
examples/    ← reference implementations + adopter onboarding samples
governance/  ← roadmap, RFC process, maintainers, IPR policy
+ 7 root files: README, LICENSE, LICENSE-CODE, DISCLOSURE, CONTRIBUTING,
  CODE_OF_CONDUCT, GOVERNANCE (plus the thin agent-context pointer)
```

**Folder-promotion criteria.** Additional folders (e.g. `operations/`, `architecture/`, `plan/`) are added only by an explicit DEC, when a real usage signal is present (for example: ≥3 InsightRecords accumulated, ≥1 LearningPattern emerged, or a roadmap that outgrows `governance/ROADMAP.md`). Structure is **derived from need, not imposed top-down** — P5 (Stage as DAG-Derived View) and P8 (Recursive Learning by Capture) applied at the folder-structure level.

**Process dogfooding, not schema dogfooding.** The repo uses the framework to develop itself — slices (P4), DECs in `decisions/` (P1/P2), evidence and security gates in CI (P6/P7), human authority on merge (P3). It does **not** force its publishing layout to match the structure adopters apply to their own corpora. (Precedent: a kernel is developed with itself, but its source tree is organized for kernel work, not to mirror its users' projects.)

## Alternatives considered

- **A — A heavyweight, product-engineering corpus layout (~11 folders)**: rejected — over-engineered for an initial spec corpus, adds adoption friction versus the industry baseline, and presupposes tooling and scale not yet present; it would impose structure top-down, against the spirit of P5.
- **B — A fully flat layout (single spec file or numbered flat docs)**: rejected — too coarse for a framework with clear sub-domains (reference patterns, governance, decisions are first-class) and it loses the recursive-dogfooding affordance of a `decisions/` folder.
- **C — Hybrid lightweight initial + explicit grow-into criteria**: **selected** — convergent with the OpenAPI / JSON Schema / Diátaxis / Spec Kit / PEPs precedent, keeps the audit plane (`decisions/`) first-class, and stays future-proof without committing structure ahead of need.

## Consequences

**Enables**: immediate, low-friction scaffolding; a layout recognizable to contributors familiar with major spec projects; simpler initial tooling surface. **Constrains**: no silent folder creation — additions require a DEC and an empirical trigger. **Costs**: contributors expecting a heavyweight corpus layout need the distinction (publishing layout ≠ prescribed adopter structure) documented, which the agent-context file and `reference/project-structure/` carry.

## References

- [`DR-2026-05-12-three-layer-ip-boundary.md`](DR-2026-05-12-three-layer-ip-boundary.md) — the Layer B.1 frame (folder structure is framework IP).
- [`reference/project-structure/`](../../reference/project-structure/) — the *prescribed* foundations-first adopter structure, deliberately distinct from this publishing layout.
- Industry precedent: OpenAPI Specification, JSON Schema, Diátaxis, GitHub Spec Kit, the Twelve-Factor App, PEPs.
