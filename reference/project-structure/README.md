# Project Structure — Layer B.1 Reference Pattern

> The **prescribed**, foundations-first project structure for SliceOps adopters. A Layer B.1 methodology artifact — deliberately **distinct** from the lightweight *publishing* layout of this spec repo (see note below).

## The prescribed structure (foundations-first)

SliceOps prescribes that an adopter's corpus is organized so context flows **foundations → decisions → architecture → specs → execution → insights** — the order in which an agent should absorb it and an auditor should trace it. This ordering **is** the context architecture (P12 Context Discipline): single-source and routable.

```
foundations/   vision, principles, glossary, invariants — the WHY
decisions/     DecisionRecords — the audit plane (P2/P1)
architecture/  how the pieces fit — derived from decisions
specs/         versioned contracts — derived from decisions
execution/     slices, slice-tracker, evidence — the HOW in motion
insights/      InsightRecords, LearningPatterns, postmortems — capture (P8)
```

Homologated 1:1 with engineering repos: the same skeleton governs a methodology corpus and a code repo, so agents move between them with one mental model.

## Why decision-first ordering

Decision-first (per the canonical principles): architecture, specs, plans, and execution are **consequences** of foundations + decisions, never the reverse. A reader or agent starts at the WHY (foundations + decisions), then the mechanics. Leading with "one slice = one PR" inverts the dependency.

## Distinct from this repo's publishing layout

This spec repo deliberately uses a **different, lightweight publishing layout** (`spec/`, `reference/`, `decisions/`, `examples/`, `governance/`) optimized for an OSS documentation site (precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs). The *prescribed* structure above is what adopters apply to their own corpora and products; the *publishing* layout is how this framework documents itself. The two differ on purpose — do not conflate them.

## Adopter note

Adopters MAY adapt folder names to their stack, but MUST preserve the foundations-first ordering and the single-source property (P12). The structure is a Layer B.1 reference pattern: copy, then specialize.
