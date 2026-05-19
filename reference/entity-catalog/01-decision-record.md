# DecisionRecord — Capa B.1 Cognitive Entity

> Architectural/strategic decisions with lifecycle, supersession, and rationale. **Mapped principles: P2 (Audit Plane Discipline), P4 (Decision Integrity by Construction).**

## Purpose

The first-class artifact of the audit plane. Every architectural or strategic decision is recorded as a DecisionRecord (DEC) so that *what was decided, by whom, why, with which alternatives, and with what supersession chain* is auditable. DECs are the substrate that makes P2's "audit the decision plane" real.

## Frontmatter schema

```yaml
entity: DecisionRecord
status: proposed | ratified | superseded | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
originating_slice: <BL-XX.SEC-XX.SL-XXX>   # P4 provenance; null only for back-fill
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

`proposed` → `ratified` → (`superseded` | `deprecated`). `superseded` requires a bidirectional edge (new DEC `supersedes`; old DEC `superseded-by`). The supersession graph must be acyclic. DECs are append-only — never deleted, never silently rewritten.

## Usage example (generic)

```
DR-YYYY-MM-DD-<decision-slug>.md
  entity: DecisionRecord
  status: ratified
  originating_slice: BL-XX.SEC-XX.SL-XXX
  supersedes: [DR-YYYY-MM-DD-<prior-decision-slug>]
  topics: [<canonical topic>...]
  consistency-check: |
    Supersedes the prior decision. States what is preserved
    and what changes vs the existing corpus.
```

Body sections: Context · Decision · Alternatives considered · Consequences · References.

## Cross-reference patterns

- Produced by a slice → `originating_slice` (P4).
- Supersedes/superseded-by → other DecisionRecords (bidirectional).
- Evidence trail → links InsightRecords, OutcomeRecords produced alongside.
- R-rule amendments → cite a LearningPattern as evidence.

## Anti-patterns

- DEC created post-hoc to justify already-merged code.
- DEC contradicting a prior DEC without explicit supersession.
- DEC without "alternatives considered" (false-binary thinking).
- DEC with no `originating_slice` and no back-fill flag (violates P4).
- Decisions left in chat/email/meeting notes without a subsequent DEC.
