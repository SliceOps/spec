# AGENTS.md — sliceops-spec

Agent context for sessions developing the SliceOps™ framework spec itself (recursive dogfooding: SliceOps uses SliceOps). Vendor-neutral; tool-specific files (e.g. `CLAUDE.md`) are thin pointers to this file (P11 Platform-Agnostic).

## Decision-first

SliceOps is a **decision-driven framework**, not a spec-first one. Architecture, specs, plans, and execution are **consequences** of foundations and decisions — never the reverse. Read and write in that order: **foundations → decisions → architecture → specs → execution → insights**. Do not lead with "one slice = one PR"; lead with the WHY (the decisions) and let the mechanics follow.

## What this repo is

The canonical, versioned SliceOps™ framework specification, Layer B reference patterns, and governance. Documentation under CC BY 4.0, code under MIT — ratified (`DR-2026-06-15-sliceops-license-ratification`; see `governance/IPR_POLICY.md`). Public repository; changes land via pull requests with maintainer approval (P3 — Human-in-the-Loop Authority).

The repo's own **publishing layout** is lightweight and industry-aligned (precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs), growing folders only when explicit promotion criteria are met — the decision is recorded in [`decisions/accepted/DR-2026-05-14-spec-repo-publishing-layout.md`](decisions/accepted/DR-2026-05-14-spec-repo-publishing-layout.md). This is deliberately **distinct** from the foundations-first project structure the framework *prescribes* to adopters — see `reference/project-structure/`.

## Canonical core (read before editing spec content)

- **Layer A — 12 principles (P1-P12)**, in Why → How → What order:
  - **WHY (P1-P3)**: P1 Decision Integrity by Construction, P2 Audit Plane Discipline, P3 Human-in-the-Loop Authority.
  - **HOW (P4-P10)**: P4 Slice Atomicity, P5 Stage as DAG-Derived View, P6 Evidence-by-Construction, P7 Security-by-Construction, P8 Recursive Learning by Capture, P9 Shared-Resource Pre-flight, P10 Infrastructure Continuity.
  - **WHAT (P11-P12)**: P11 Platform-Agnostic, P12 Context Discipline.
- **Taxonomy**: Layer A (Principles) / Layer B (B.1 Framework Artifacts + B.2 Universal Engineering Patterns) / Layer C (C.1 Vendor Runtimes + C.2 Adopter Stack Patterns). Top-level stable; sub-numbering extensible via DEC.
- **Cognitive entity #4 is `Capability`** (not "Skill"). "Skill" is reserved for the future vendor-neutral Agent-Skill concept.

## Hard rules for spec work (foundations → decisions → execution)

1. **IP boundary (critical)**: this repo is public-bound. NEVER include runtime-internal artifacts — internal decision IDs, slice IDs, internal filesystem paths, vendor product internals, customer data. The spec describes the framework abstractly. Reference runtimes are cited as architectural peers, never copied.
2. **DEC discipline first** (P1/P2): framework changes are DecisionRecords with Layer 1 frontmatter (`conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check`), a Layer 2 pre-merge checklist, and bidirectional cross-references. Decisions precede mechanics.
3. **Human authority** (P3): principle amendments need an elevated human gate; never auto-merge critical decisions.
4. **Atomic slices** (P4): one slice = one PR, scope declared upfront — the DEV mechanism, not the starting point.
5. **Context discipline** (P12): single source of truth per fact; no synonyms for canonical terms; new terms need a DEC; fix-on-touch drift; route context, do not dump the whole corpus.
6. **Shared-resource pre-flight** (P9): before scaling parallel agent work, enumerate, cap, alert, and telemeter finite/serialized shared resources (CI minutes, counters, rate limits). Guardrails are bootstrap defaults, never retrofit. Re-scan real counter state before creating numbered artifacts (never trust a stale "counter currently at").

## Status

Skeleton, governance, and Layer B.1 reference content are in place. Bootstrap CI guardrails live in the SliceOps toolkit repo and as `.github/workflows/` here (recursive dogfooding).
