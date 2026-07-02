# decisions/ — DECs about the framework itself (recursive dogfooding)

SliceOps uses SliceOps to develop SliceOps. Decisions about the framework are recorded here as DecisionRecords, following the same audit-plane discipline (P2) and decision-integrity discipline (P1) the framework prescribes.

This is **process** dogfooding (the framework governs its own evolution), not **schema** dogfooding (this folder layout is not required to match an adopter's codebase layout).

## Lifecycle (ADR-style)

| Folder | Meaning |
|---|---|
| `accepted/` | Active, ratified decisions |
| `superseded/` | Replaced by a later decision (`superseded-by:` in frontmatter) |
| `deprecated/` | No longer applies (`replacement:` in frontmatter) |
| `rfcs/` | Proposed, under deliberation |

## Naming

`DR-YYYY-MM-DD-slug.md`

## Frontmatter discipline (Layer 1)

Every DEC carries: `conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check` (multi-line paragraph declaring relationship to existing corpus), plus supersession edges. Bidirectional cross-references are mandatory.

## What does NOT live here

Decisions about specific vendor runtimes (those live in vendor repos). Adopter-internal decisions (those live in the adopter's own brain).

## Status

Active. This folder holds the framework's **published** DecisionRecords — ratified decisions in `accepted/` and proposals under deliberation in `rfcs/`. The maintainers' fuller working corpus (drafts, internal analyses, runtime-adjacent decisions) remains private; the DECs published here are the go-public subset, sanitized per the IP boundary (see "What does NOT live here" above).
