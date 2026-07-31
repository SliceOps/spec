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
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0009-20260712-handoffs-as-a-contextpack-kind, DEC-0011-20260713-canonical-corpus-container-and-layout, DEC-P-0023-20260731-complete-decade-scaffold-supersedes-presence-activation]
topics: [context-discipline, corpus-integrity, folder-structure]
vocabulary-changes: ["_index.md (corpus index)", "reserved infrastructure names", "loading chain"]
consistency-check: |
  Originally drafted as a ContextPack kind inside the DEC-0008 conversation; the owner
  rejected that design (an entry point you must search for defeats itself) and this
  record fixes the corrected form: the index is corpus INFRASTRUCTURE with a reserved
  name, outside the entity catalog — the same class as .counters/ and the agent-context
  files. Materializes the routing mechanism the Context Router already specifies (the
  router is the mechanism; _index.md is its artifact). Formalizes the reserved
  infrastructure-name list that the universal grammar of DEC-0008_5 exempts. Split out
  as standalone per DEC-0008_9. No conflicts; ContextPack (DEC-0009) explicitly does NOT
  cover locating.
---

# DEC-0010 — The Corpus Index as Reserved-Name Infrastructure

> A SliceOps DecisionRecord about SliceOps itself. Ratified in the DEC-0008 conversation
> (2026-07-12); split out as an independent record per DEC-0008_9.

## Summary

Every corpus carries **`_index.md` at its root**: the map of where to look for what, so
no agent or human ever searches a corpus wholesale. The index is **not a
cognitive entity** — a pack *contains* context, an index *locates* it — so it lives in
the reserved-name infrastructure class (like `.counters/` and `CLAUDE.md`/`AGENTS.md`),
findable with **zero discovery cost** because its name and place never vary. Context
engineering is a first-class concern: the framework is optimized for agentic and human
work, and finding context cheaply is the foundation.

## Context

The original purpose of ContextPack included indexing — letting a language model know
where to look instead of reading everything. The first draft of this rule modeled the
index as a ContextPack kind; the owner rejected it: an agent would have to open
ContextPacks to find which are indexes, and **an entry point you must search for defeats
itself**. Meanwhile the practice already existed everywhere without a canonical home:
a wild `IndexCatalog` entity invented in one corpus, master-index pages in product
documentation, memory-index files. Evidence of a missing standard.

## Decision

1. **Reserved name, zero discovery**: `_index.md` at every corpus root. The underscore
   sorts it first in any listing. Large corpora MAY add per-folder `_index.md` files;
   the root index routes to them (recursive routing, zero discovery at every level).
2. **The loading chain**: agent-context file (thin, always loaded) → `_index.md` (small,
   says WHERE) → the exact files or ContextPacks needed. No agent reads a corpus wholesale.
3. **Content**: route tables — topic / entity / question pattern → exact paths or
   ContextPack ids to open. The index **points, never copies** (copies drift — P12,
   Context Discipline). It is the materialized routing table of the Context Router.
   An `index-template` ships with the spec templates.
4. **Enforcement**: the naming validator checks (a) the root `_index.md` exists in every
   homologated corpus, and (b) every route target resolves — a stale index is a build
   failure, not a suggestion.
5. **Reserved infrastructure names, formalized** (the universal grammar of DEC-0008_5
   governs *entity artifacts*; these are exempt and reserved): `README.md`,
   `CLAUDE.md`/`AGENTS.md`, `MEMORY.md`, `_organization.md`, `_index.md`, `*-ledger.md`,
   and the `.counters/` directory. The list lives in naming.md; anything else must be an
   entity artifact under the grammar.

## Alternatives considered

- **A — Index as a ContextPack kind**: rejected by the owner — discovery would require
  scanning packs; an entry point must be findable without search. Locating ≠ containing.
- **B — A dedicated Index entity (14th)**: rejected — locating is not a cognition; the
  catalog holds what a mind produces, and infrastructure already has its own class
  (`.counters/` precedent: operational state, no frontmatter, outside the catalog).
- **C — Reserved-name infrastructure file**: **selected** — zero-discovery by
  construction, one per corpus, recursive for scale, machine-enforceable freshness.

## Consequences

**Enables**: constant-cost context bootstrap in every corpus for every agent and human;
the Context Router gains its concrete artifact; token-budget discipline by construction.
**Constrains**: every homologated corpus must seed and maintain its root `_index.md`
(migration seeds it; the validator keeps it honest). **Costs**: index maintenance on
structural changes — bounded by the routes-resolve gate, which turns rot into a visible
failure instead of silent drift.

## Ratification note

Approved by the owner on 2026-07-12 in the DEC-0008 ratification conversation, **as the
correction** of the first draft (ContextPack kind) after the owner's objection. The
correction is part of the record: the rejected design is preserved under Alternatives —
the audit plane keeps its graveyard (DEC-0008_7).

## References

- [`DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — parent conversation; universal grammar and exemptions (DEC-0008_5), conventions (DEC-0008_7), clause rule (DEC-0008_9).
- [`DEC-0009-20260712-handoffs-as-a-contextpack-kind.md`](DEC-0009-20260712-handoffs-as-a-contextpack-kind.md) — ContextPack kinds (containing, not locating).
- `reference/context-router/` — the routing mechanism this record materializes.
