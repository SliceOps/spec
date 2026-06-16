# ContextPack — Layer B.1 Cognitive Entity

> Pre-computed context bundles loaded at slice/session start. **Mapped principle: P8 (Platform-Agnostic).**

## Purpose

A curated, pre-assembled bundle of the context an agent needs to start a slice without re-deriving it — relevant DECs, applicable patterns, glossary subset, prior outcomes. ContextPacks make SliceOps portable across platforms (P8): the bundle is plain files, readable by any text-based agent, independent of any runtime's retrieval features.

## Frontmatter schema

```yaml
entity: ContextPack
status: active | stale | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
scope: <topic | block | role | onboarding>
includes: [<entity id | path>...]      # what the pack bundles
regenerated-from: <source descriptor>   # how to rebuild deterministically
```

## Lifecycle states

`active` → `stale` (sources changed; needs regeneration) → `archived` or back to `active` after rebuild. ContextPacks are **regenerated deterministically** from sources (Determinism-over-Regeneration, B.2) — not hand-maintained drift.

## Usage example (generic)

```
CP-01-entity-catalog.md
  entity: ContextPack
  status: active
  scope: topic
  includes: [reference/entity-catalog/*, spec/v1.0.0/glossary.md#cognitive-entity]
  regenerated-from: build-context-packs script over reference/ + spec/
Body: when to load · contents summary · regeneration command.
```

## Cross-reference patterns

- Bundles → `includes` (entities/paths).
- Loaded by → slices/sessions at start (brain-pack injection mechanism).
- Rebuilt by → a deterministic generator (B.2 Determinism-over-Regeneration).

## Anti-patterns

- Hand-editing a ContextPack instead of regenerating from sources (drift; violates determinism).
- Stale pack served as active (sources moved; pack not regenerated).
- Pack so large it defeats its purpose (curate, don't dump).
- Adopter-specific context placed in a shared spec pack (belongs in the adopter's own brain).
