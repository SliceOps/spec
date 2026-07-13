# ContextPack — Layer B.1 Cognitive Entity

> Pre-computed context bundles loaded at slice/session start. **Mapped principle: P11 (Platform-Agnostic).**

## Purpose

A curated, pre-assembled bundle of the context an agent needs to start a slice without re-deriving it — relevant DECs, applicable patterns, glossary subset, prior outcomes. ContextPacks make SliceOps portable across platforms (P11): the bundle is plain files, readable by any text-based agent, independent of any runtime's retrieval features.

## Frontmatter schema

```yaml
entity: ContextPack
status: active | stale | archived
kind: pack | brief | handoff           # DEC-0009 — all three CONTAIN context
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
scope: <topic | block | role | onboarding>
includes: [<entity id | path>...]      # what the pack bundles
regenerated-from: <source descriptor>   # how to rebuild deterministically (kind: pack)
# handoff-specific (DEC-0009):
from_session: <SESS id or session reference>
to: <owner | domain | SESS id> | null
reason: context-exhausted | spinoff     # the two birth conditions of a handoff
```

**Kinds** ([`DEC-0009`](../../decisions/DEC-0009-20260712-handoffs-as-a-contextpack-kind.md)): **pack** — routed or pre-computed corpus context loaded at session start; **brief** — context prepared to *start* a new topic or session; **handoff** — context prepared to *continue or spin off* in-flight work (canonical body: state of work · done · pending · open questions · next steps · counter and resource state), closing the session-provenance loop `SESS-A → CP (handoff) → SESS-B`.

Packs **contain** context; **locating** it is the corpus index's job — `_index.md`, reserved-name infrastructure, not an entity ([`DEC-0010`](../../decisions/DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md)).

## Lifecycle states

`active` → `stale` (sources changed; needs regeneration) → `archived` or back to `active` after rebuild. ContextPacks are **regenerated deterministically** from sources (Determinism-over-Regeneration, B.2) — not hand-maintained drift.

## Usage example (generic)

```
CP-01-entity-catalog.md
  entity: ContextPack
  status: active
  scope: topic
  includes: [reference/entity-catalog/*, spec/v2.0.0/glossary.md#cognitive-entity]
  regenerated-from: build-context-packs script over reference/ and spec/
Body: when to load · contents summary · regeneration command.
```

## Cross-reference patterns

- Bundles → `includes` (entities/paths).
- Loaded by → slices/sessions at start (context-pack injection mechanism).
- Rebuilt by → a deterministic generator (B.2 Determinism-over-Regeneration).

## Anti-patterns

- Hand-editing a ContextPack instead of regenerating from sources (drift; violates determinism).
- Stale pack served as active (sources moved; pack not regenerated).
- Pack so large it defeats its purpose (curate, don't dump).
- Adopter-specific context placed in a shared spec pack (belongs in the adopter's own corpus).
