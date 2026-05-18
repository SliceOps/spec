# CLAUDE.md — sliceops-spec

Agent context for sessions developing the SliceOps™ methodology spec itself (recursive dogfooding: SliceOps uses SliceOps).

## What this repo is

The canonical, versioned SliceOps™ methodology specification + Capa B reference patterns + governance. Documentation under CC BY 4.0, code templates under MIT (final terms pending IP/Legal ratification — no `LICENSE` file yet; repo private until then).

This is a **methodology spec repo**, not a product-engineering brain. Structure is lightweight and industry-aligned (precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs), and grows into more folders only when explicit promotion criteria are met (P3 + P7 — structure emerges from need, not imposed top-down).

## Structure

```
spec/v1.0.0/     versioned canonical spec (principles, glossary, topics, ip-boundary)
reference/       Capa B patterns: entity-catalog, knowledge-categories, r-rules,
                 frontmatter-schemas, templates, workflows
decisions/       DECs about the framework itself (accepted/superseded/deprecated/rfcs)
examples/        reference implementations + adopter onboarding
governance/      roadmap, RFC process, maintainers, IPR
```

Root: `README` `DISCLOSURE` `CONTRIBUTING` `CODE_OF_CONDUCT` `GOVERNANCE` `CLAUDE` (+ `LICENSE` once ratified).

## Canonical core (read before editing spec content)

- **Capa A — 12 principles** (P1-P12): Slice Atomicity, Audit Plane Discipline, Stage as DAG-Derived View, Decision Integrity by Construction, Evidence-by-Construction, Security-by-Construction, Recursive Learning by Capture, Platform-Agnostic, Human-in-the-Loop Authority, Vocabulary Discipline, Infrastructure Continuity, Shared-Resource Pre-flight.
- **Taxonomy**: Capa A (Principles) / Capa B (B.1 Methodology Artifacts + B.2 Universal Engineering Patterns) / Capa C (C.1 Vendor Runtimes + C.2 Adopter Stack Patterns). Top-level stable; sub-numbering extensible via DEC.
- **Cognitive entity #4 is `Capability`** (not "Skill"). "Skill" is reserved for the future vendor-neutral Agent-Skill concept.

## Hard rules for spec work

1. **IP boundary (critical)**: this repo is public-bound. NEVER include runtime-internal artifacts — internal decision IDs, slice IDs, internal filesystem paths, vendor product internals, customer data. The spec describes the methodology abstractly. Reference runtimes are cited as architectural peers, never copied.
2. **One slice = one PR** (P1). Scope declared upfront.
3. **DEC discipline** (P2/P4): methodology changes are DecisionRecords with Layer 1 frontmatter (`conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check`) + Layer 2 pre-merge checklist + bidirectional cross-refs.
4. **Vocabulary is canon** (P10): no synonyms for canonical terms; new terms need a DEC; fix-on-touch drift.
5. **HITL** (P9): principle amendments need elevated human gate; never auto-merge critical decisions.
6. **Shared-resource pre-flight** (P12): before scaling parallel agent work, enumerate + cap + alert + telemeter finite/serialized shared resources (CI minutes, counters, rate limits). Guardrails are bootstrap defaults, never retrofit. Re-scan real counter state before creating numbered artifacts (never trust a stale "counter currently at").

## Status

Scaffolding in progress. Folders are placeholders; Capa B.1 content drafting is the next batch. Bootstrap CI guardrails live in the SliceOps toolkit repo and as `.github/workflows/` here (recursive dogfooding).
