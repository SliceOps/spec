# DecisionRecord — Layer B.1 Cognitive Entity

> Architectural/strategic decisions with lifecycle, supersession, and rationale. **Mapped principles: P2 (Audit Plane Discipline), P1 (Decision Integrity by Construction).**

## Purpose

The first-class artifact of the audit plane. Every architectural or strategic decision is recorded as a DecisionRecord (DEC) so that *what was decided, by whom, why, with which alternatives, and with what supersession chain* is auditable. DECs are the substrate that makes P2's "audit the decision plane" real.

## Frontmatter schema

```yaml
entity: DecisionRecord
status: pending | approved | deprecated   # legacy proposed/ratified/superseded read-tolerated, prohibited on write
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
approver: <approving human> | null           # optional; recommended on status: approved (P3)
sensitivity: public | internal | restricted | sensitive
originating_slice: <BL-XX.SEC-XX.SL-XXX>   # P1 provenance; null only for back-fill
supersedes: [<DEC id>...]
superseded-by: <DEC id> | null
conflicts-with: [<DEC id>...]               # Layer 1; non-empty → body resolution paragraph
related-decs: [<DEC id>...]                  # topically adjacent
topics: [<canonical topic>...]               # from the topic taxonomy
vocabulary-changes: [<term>...]              # triggers glossary update
consistency-check: |                          # Layer 1 mandatory paragraph
  How this DEC relates to the existing corpus.
```

## Lifecycle states

`pending` → `approved` → `deprecated`. **The state is carried in the filename prefix**: `DEC-P-` (pending) → `DEC-` (approved) → `DEC-D-` (deprecated/superseded). Supersession requires a bidirectional edge (new DEC `supersedes`; old DEC `superseded-by`) and the old record becomes `DEC-D-` with `status: deprecated`. The supersession graph must be acyclic. DECs are append-only — never deleted, never silently rewritten. A state change renames the file and rewrites all references in the same atomic change (R5); decisions folders are **flat** (no `rfcs/`/`accepted/`/`superseded/` subfolders — see `../../spec/v1.2.0/naming.md` §3).

Legacy status values (`proposed`/`ratified`/`superseded`) are read-tolerated when parsing archives or non-homologated corpora, and prohibited on write.

Approval is a human act (P3 — Human-in-the-Loop Authority): the optional `approver` field records the human who approved the DEC, and is recommended once `status: approved`. `approver` MAY equal `owner` in single-maintainer contexts — the point is recording *who* approved, making self-approval explicit and auditable instead of implicit.

## Usage example (generic)

```
DEC-YYYY-MM-DD-<decision-slug>.md      (date-based, vaults · DEC-NNN-<slug>.md counter-based repos)
  entity: DecisionRecord
  status: approved
  originating_slice: BL-XX.SEC-XX.SL-XXX
  supersedes: [DEC-D-YYYY-MM-DD-<prior-decision-slug>]
  topics: [<canonical topic>...]
  consistency-check: |
    Supersedes the prior decision. States what is preserved
    and what changes vs the existing corpus.
```

Body sections: Context · Decision · Alternatives considered · Consequences · References.

## Cross-reference patterns

- Produced by a slice → `originating_slice` (P1).
- Supersedes/superseded-by → other DecisionRecords (bidirectional).
- Evidence trail → links InsightRecords, OutcomeRecords produced alongside.
- R-rule amendments → cite a LearningPattern as evidence.

## Anti-patterns

- DEC created post-hoc to justify already-merged code.
- DEC contradicting a prior DEC without explicit supersession.
- DEC without "alternatives considered" (false-binary thinking).
- DEC with no `originating_slice` and no back-fill flag (violates P1).
- Decisions left in chat/email/meeting notes without a subsequent DEC.
- The `DR-` prefix or the term "RFC" (retired — see `../../spec/v1.2.0/naming.md`).
- Lifecycle subfolders (`rfcs/`, `accepted/`, `superseded/`) — the prefix carries the state; folders stay flat.
- Prefix/status mismatch (e.g., a `DEC-P-` file with `status: approved`).
