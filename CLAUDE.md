# CLAUDE.md — sliceops-spec

Agent context for sessions developing the SliceOps™ framework spec itself (recursive dogfooding: SliceOps uses SliceOps).

## What this repo is

The canonical, versioned SliceOps™ framework specification, Layer B reference patterns, and governance. Documentation under CC BY 4.0, code under MIT — ratified (`DR-2026-06-15-sliceops-license-ratification`; see `governance/IPR_POLICY.md`). Repo private pre-launch; goes public on founder approval (P3).

This is a **framework spec repo**, not a product-engineering brain. Structure is lightweight and industry-aligned (precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs), and grows into more folders only when explicit promotion criteria are met (P5 and P8 — structure emerges from need, not imposed top-down).

## Structure

```
spec/v1.0.0/     versioned canonical spec (principles, glossary, topics, ip-boundary)
reference/       Layer B patterns: entity-catalog, knowledge-categories, r-rules,
                 frontmatter-schemas, templates, workflows
decisions/       DECs about the framework itself (accepted/superseded/deprecated/rfcs)
examples/        reference implementations and adopter onboarding
governance/      roadmap, RFC process, maintainers, IPR
```

Root: `README` `DISCLOSURE` `CONTRIBUTING` `CODE_OF_CONDUCT` `GOVERNANCE` `CLAUDE` `TRADEMARK` `LICENSE` `LICENSE-CODE` `DCO`.

## Canonical core (read before editing spec content)

- **Layer A — 12 principles** (P1-P12): Slice Atomicity, Audit Plane Discipline, Stage as DAG-Derived View, Decision Integrity by Construction, Evidence-by-Construction, Security-by-Construction, Recursive Learning by Capture, Platform-Agnostic, Human-in-the-Loop Authority, Vocabulary Discipline, Infrastructure Continuity, Shared-Resource Pre-flight.
- **Taxonomy**: Layer A (Principles) / Layer B (B.1 Framework Artifacts and B.2 Universal Engineering Patterns) / Layer C (C.1 Vendor Runtimes and C.2 Adopter Stack Patterns). Top-level stable; sub-numbering extensible via DEC.
- **Cognitive entity #4 is `Capability`** (not "Skill"). "Skill" is reserved for the future vendor-neutral Agent-Skill concept.

## Hard rules for spec work

1. **IP boundary (critical)**: this repo is public-bound. NEVER include runtime-internal artifacts — internal decision IDs, slice IDs, internal filesystem paths, vendor product internals, customer data. The spec describes the framework abstractly. Reference runtimes are cited as architectural peers, never copied.
2. **One slice = one PR** (P4). Scope declared upfront.
3. **DEC discipline** (P2/P1): framework changes are DecisionRecords with Layer 1 frontmatter (`conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check`), a Layer 2 pre-merge checklist, and bidirectional cross-refs.
4. **Vocabulary is canon** (P12): no synonyms for canonical terms; new terms need a DEC; fix-on-touch drift.
5. **HITL** (P3): principle amendments need elevated human gate; never auto-merge critical decisions.
6. **Shared-resource pre-flight** (P9): before scaling parallel agent work, enumerate, cap, alert, and telemeter finite/serialized shared resources (CI minutes, counters, rate limits). Guardrails are bootstrap defaults, never retrofit. Re-scan real counter state before creating numbered artifacts (never trust a stale "counter currently at").

## Status

Skeleton, governance, and Layer B.1 reference content are in place. Bootstrap CI guardrails live in the SliceOps toolkit repo and as `.github/workflows/` here (recursive dogfooding).
