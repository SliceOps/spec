# Frame — Layer B.1 Cognitive Entity

> A mental model or lens the corpus reasons with. **Mapped principle: universal.** Canonical filename prefix: `FRAME-` (see `../../spec/v2.0.0/naming.md`).

> **Naming**: this entity was **CognitiveFramework** before v2.0.0 (renamed by clause DEC-0008.2). No collision with "framework": the framework has frames the way a body has cells. The `CF-` prefix is retired.

## Purpose

Holds the reference structures thinking happens *through*: glossaries, taxonomies, worldview documents, architectural lenses, evaluation grids. Frames live in the **Why ring** of the cognition cycle (clause DEC-0008.1) together with Values and Preferences — they condition every downstream stage without being stages themselves. Constitutive decisions are the only path that rewrites this ring.

## Frontmatter schema

```yaml
entity: Frame
status: active | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
version: <SemVer>
supersedes: [<FRAME id>...]
superseded-by: <FRAME id> | null
related-decs: [<DEC id>...]      # decisions that approved/amended this frame
topics: [<canonical topic>...]
```

## Lifecycle states

`active` → `superseded`. Minor changes (additions, clarifications) bump `updated` and `version` in place. Major restructure → a new versioned Frame that `supersedes` the prior (bidirectional). Living document by design.

## Usage example (generic)

```
FRAME-0003-20260514-canonical-glossary-pointer.md
  entity: Frame
  status: active
  version: 2.0.0
  related-decs: [DEC-0008-…]
  topics: [vocabulary-discipline, meta-framework]
Body: purpose · what this frame is FOR · the lens itself (or the pointer to the norm).
```

## Cross-reference patterns

- Approved/amended by → `related-decs`.
- Points to the norm, never copies it (P12 — a Frame that mirrors a canonical document is drift waiting to happen; make it a pointer).
- Supersession → bidirectional `supersedes`/`superseded-by`.

## Anti-patterns

- A Frame that copies a canonical source instead of pointing to it (the glossary-mirror failure).
- Editing a superseded Frame (frozen audit trail).
- The `CF-` prefix or the name "CognitiveFramework" (retired — clause DEC-0008.2).
