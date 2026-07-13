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

`pending` → `approved` → `deprecated`. **The state is carried in the filename prefix**: `DEC-P-` (pending) → `DEC-` (approved) → `DEC-D-` (deprecated/superseded). Supersession requires a bidirectional edge (new DEC `supersedes`; old DEC `superseded-by`) and the old record becomes `DEC-D-` with `status: deprecated`. The supersession graph must be acyclic. DECs are append-only — never deleted, never silently rewritten. A state change renames the file and rewrites all references in the same atomic change (R5); decisions folders are **flat** (no `rfcs/`/`accepted/`/`superseded/` subfolders — see `../../spec/v2.0.0/naming.md` §3).

Legacy status values (`proposed`/`ratified`/`superseded`) are read-tolerated when parsing archives or non-homologated corpora, and prohibited on write.

Approval is a human act (P3 — Human-in-the-Loop Authority): the optional `approver` field records the human who approved the DEC, and is recommended once `status: approved`. `approver` MAY equal `owner` in single-maintainer contexts — the point is recording *who* approved, making self-approval explicit and auditable instead of implicit.

## Kind axis and goal edges (clause DEC-0008.3)

```yaml
kind: constitutive | strategic | tactical
defines-goal: [<GOAL id>…]   # REQUIRED when strategic — the decision creates/kills/reframes goals
serves-goal: <GOAL id>       # REQUIRED when tactical — the decision selects means within a goal
serves-value: <VAL id>       # the recursion's base case: strategic decisions with no goal above
```

**Constitutive** decisions change the rules of the system itself (principles, naming, licensing, governance) and REQUIRE `approver:` under the elevated human-in-the-loop gate. **Strategic** decisions change the goal tree; **tactical** decisions move within it. Operational test: *does this decision change the goal tree, or move inside it?* The boundary is fractal — a record may carry both edges (tactical toward its parent goal, strategic toward the sub-goals it creates); strategic at level n is tactical at level n+1. `kind:` is mandatory for records created on or after 2026-07-13; earlier records are back-filled fix-on-touch.

## Clause identifiers (clause DEC-0008.9)

Resolutions inside a record are **clauses**, cited `DEC-NNNN.n` — never "Decision n" bare. Clause identifiers are valid supersession targets (`supersedes: [DEC-0008.3]`). The independence test decides clause versus standalone record: *could you reject this part and approve the rest without breaking the design?* No → clause; yes → its own record.

## Usage example (generic)

```
DEC-NNNN-YYYYMMDD-<decision-slug>.md      (universal grammar — spec/v2.0.0/naming.md)
  entity: DecisionRecord
  status: approved
  originating_slice: SLC<n>SEC<n>BL<n>
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
- The `DR-` prefix or the term "RFC" (retired — see `../../spec/v2.0.0/naming.md`).
- Lifecycle subfolders (`rfcs/`, `accepted/`, `superseded/`) — the prefix carries the state; folders stay flat.
- Prefix/status mismatch (e.g., a `DEC-P-` file with `status: approved`).
