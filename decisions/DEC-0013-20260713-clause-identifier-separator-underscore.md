---
entity: DecisionRecord
status: approved
kind: constitutive
created: 2026-07-13
updated: 2026-07-13
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
originating_slice: null   # owner review of the published v2.0.0, 2026-07-13
supersedes: [DEC-0008_9]
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections, DEC-0016-20260728-topic-taxonomy-naming-and-off-taxonomy-cleanup]
topics: [naming, meta-framework]
vocabulary-changes: ["clause identifier DEC-NNNN_n (was DEC-NNNN.n)"]
consistency-check: |
  Amends the citation NOTATION of DEC-0008_9 only — the clause mechanism itself
  (sub-resolutions as supersession targets, the independence test) is unchanged, and no
  filename changes: clause identifiers are citations, never filenames. Applies the same
  rationale DEC-0008_6 used to retire the dotted slice coordinate (dots are fragile
  wherever an identifier may someday materialize as a filename or pass through
  extension-splitting tooling) to the one remaining dotted identifier in the standard.
  Published v2.0.0 hours earlier makes this the cheapest possible moment; per the
  versioning policy (released versions are immutable) the change ships as spec v2.0.1.
  Frozen zones (spec/v1.x, spec/v2.0.0, 99-archive folders, git history) keep the dotted
  citations they were published with — this record is their alias note.
---

# DEC-0013 — Clause Identifier Separator: Underscore

> A SliceOps DecisionRecord about SliceOps itself. Raised and ratified by the owner on
> 2026-07-13 while reviewing the published v2.0.0.

## Summary

Clause identifiers are cited **`DEC-NNNN_n`** (sub-clauses `DEC-NNNN_n_m`) — underscore,
not dot. Rationale, in the owner's words: if a clause identifier ever ends up naming a
file, a dot invites extension-splitting breakage; the standard already retired dots from
the slice coordinate for exactly this fragility (DEC-0008_6). One separator philosophy,
everywhere: hyphens separate grammar fields, underscores mark infrastructure and
sub-identifiers, dots belong to file extensions only.

## Decision

1. The canonical citation form of a clause is `DEC-NNNN_n` (e.g. `DEC-0008_5`);
   sub-sub-clauses chain the underscore (`DEC-0008_2_1`). Valid everywhere a clause is
   cited: prose, frontmatter edges (`supersedes: [DEC-0008_3]`), validator messages.
2. Everything else in DEC-0008_9 stands: clauses are supersession targets; the
   independence test decides clause versus standalone record.
3. Living corpora are swept to the new notation in one pass; frozen zones keep the
   dotted form and resolve against this record.
4. Ships as **spec v2.0.1** (new version directory per the versioning policy; v2.0.0
   remains frozen for audit).

## Alternatives considered

- **Keep the dot**: rejected by the owner — inconsistent with the standard's own
  letters-over-dots rationale (DEC-0008_6) and a latent filename hazard.
- **Hyphen** (`DEC-0008-5`): rejected — the hyphen is the universal grammar's field
  separator; a clause citation would become ambiguous against real filenames.

## Consequences

**Enables**: filename-safe, tool-safe clause citations; one separator philosophy.
**Constrains**: a one-time sweep of living documents and validator messages; v2.0.1 cut.
**Costs**: dotted citations persist in the published v2.0.0 snapshot and git history —
covered by clause 3 (alias note), zero runtime breakage (citations, not filenames).
