# decisions/ — DECs about the framework itself (recursive dogfooding)

SliceOps uses SliceOps to develop SliceOps. Decisions about the framework are recorded here as DecisionRecords, following the same audit-plane discipline (P2) and decision-integrity discipline (P1) the framework prescribes.

This is **process** dogfooding (the framework governs its own evolution), not **schema** dogfooding (this folder layout is not required to match an adopter's codebase layout).

## Lifecycle — in the prefix, folder flat

This folder is **flat** (no lifecycle subfolders): the filename prefix carries the state, per [`spec/v1.2.0/naming.md`](../spec/v1.2.0/naming.md) §3.

| Prefix | State | `status:` |
|---|---|---|
| `DEC-` | approved (in force) | `approved` |
| `DEC-P-` | pending, under deliberation (the proposal — see `../governance/PROPOSAL-PROCESS.md`) | `pending` |
| `DEC-D-` | deprecated / superseded (`superseded-by:` set when superseded) | `deprecated` |

A state change **renames the file** (`DEC-P-…` → `DEC-…` → `DEC-D-…`) and rewrites all references in the same atomic change (R5). The optional `approver:` field records the approving human (P3).

## Naming

`DEC-YYYY-MM-DD-slug.md` (date-based ID scheme — this corpus has no counter; date + slug carries uniqueness).

## Frontmatter discipline (Layer 1)

Every DEC carries: `conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check` (multi-line paragraph declaring relationship to existing corpus), plus supersession edges. Bidirectional cross-references are mandatory.

## What does NOT live here

Decisions about specific vendor runtimes (those live in vendor repos). Adopter-internal decisions (those live in the adopter's own brain).

## Status

Active. This folder holds the framework's **published** DecisionRecords — approved decisions (`DEC-`) and proposals under deliberation (`DEC-P-`), flat. The maintainers' fuller working corpus (drafts, internal analyses, runtime-adjacent decisions) remains private; the DECs published here are the go-public subset, sanitized per the IP boundary (see "What does NOT live here" above).
