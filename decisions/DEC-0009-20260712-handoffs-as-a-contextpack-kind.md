---
entity: DecisionRecord
status: approved
kind: constitutive
created: 2026-07-12
updated: 2026-07-12
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
originating_slice: null   # back-fill: ratification conversation of DEC-0008, 2026-07-12
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure]
topics: [entity-catalog, vocabulary-discipline, session-management]
vocabulary-changes: ["pack (ContextPack kind)", "brief (ContextPack kind)", "handoff (ContextPack kind)"]
consistency-check: |
  Originally drafted as a clause of DEC-0008 and split out as a standalone DecisionRecord
  by that record's own clause rule (DEC-0008.9 independence test: separately requested,
  separately supersedable). Extends ContextPack (catalog entity 08) with a kind axis —
  the catalog does not grow, matching the kind pattern of DEC-0008.3 (decision kinds) and
  the v1.2.0-era Capability components. Locating context is explicitly NOT this record's
  scope: that is the corpus index, DEC-0010. No conflicts.
---

# DEC-0009 — Handoffs as a ContextPack Kind

> A SliceOps DecisionRecord about SliceOps itself. Ratified in the DEC-0008 conversation
> (2026-07-12); split out as an independent record per DEC-0008.9.

## Summary

Handoffs — the most-used coordination artifact in practice — are standardized as a
**ContextPack kind**. A handoff is born in exactly two situations (the owner's
definition): the session's **context is exhausted**, or a **topic is spun off** for
another session. Both are packaged context prepared for another session — the literal
definition of ContextPack. The catalog stays at 13.

## Context

Handoffs were among the highest-volume coordination artifacts in the maintainers'
corpora, yet they had no canonical definition — the same vacuum that turned the former
ActivePriority into a catch-all (DEC-0008 context). Unstandardized coordination
artifacts are where naming discipline goes to die.

## Decision

```yaml
entity: ContextPack
kind: pack | brief | handoff              # all three CONTAIN context; locating it is
                                          # the corpus index's job (DEC-0010)
from_session: <SESS id or session reference>   # handoff-specific
to: <owner | domain | SESS id> | null          # handoff-specific: who receives the work
reason: context-exhausted | spinoff            # handoff-specific: the two birth conditions
```

- **pack** — routed or pre-computed corpus context loaded at session start.
- **brief** — context prepared to *start* a new topic or session.
- **handoff** — context prepared to *continue or spin off* in-flight work. Canonical body
  sections: state of work · done · pending · open questions · next steps · counter and
  resource state.
- Files follow the universal grammar of DEC-0008.5 (`CP-0028-20260712-slug.md`). Legacy
  `HANDOFF-NNN` identifiers migrate into the ContextPack counter (alias maps cover them);
  handoff *ledgers* remain reserved-name operational files (`*-ledger.md`, DEC-0010.5).
- Handoffs close the session-provenance loop: the emitting session records the handoff in
  its `outcome`; the receiving session loads it — `SESS-A → CP (handoff) → SESS-B` is
  fully auditable. A `handoff-template` ships with the spec templates.

## Alternatives considered

- **A — A dedicated Handoff entity (14th)**: rejected — a handoff is packaged context by
  nature; the catalog-stability discipline (kinds, never new entities) already ratified
  in DEC-0008.3 applies directly.
- **B — Keep handoffs unstandardized (folk practice)**: rejected — the highest-volume
  coordination artifact cannot be the least defined one; the ActivePriority catch-all was
  the direct cost of exactly this vacuum.

## Consequences

**Enables**: uniform handoffs across every corpus and machine; auditable session-to-session
continuity; agents that always know a handoff's shape. **Constrains**: handoffs are
ContextPacks — they carry `CP-` ids under the universal grammar, not ad-hoc names.
**Costs**: migrating legacy `HANDOFF-NNN` identifiers (one-time, alias-mapped).

## Ratification note

Approved by the owner on 2026-07-12 in the DEC-0008 ratification conversation. Drafted
first as clause "Decision 9" of DEC-0008; split into this standalone record when
DEC-0008.9 formalized the clause-versus-record test (this resolution was separately
requested and is separately supersedable).

## References

- [`DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — parent conversation; kind pattern (DEC-0008.3), universal grammar (DEC-0008.5), clause rule (DEC-0008.9).
- [`DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md`](DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md) — locating context (out of this record's scope).
