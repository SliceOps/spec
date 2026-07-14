# MentalModel — Layer B.1 Cognitive Entity

> A mental model or lens the corpus reasons with. **Mapped principle: universal.** Canonical filename prefix: `MM-` (see `../../spec/v2.0.1/naming.md`).

> **Naming**: this entity was **CognitiveFramework** before v2.0.0, briefly **Frame** during the v2.0.0 design (clause DEC-0008_2), and takes its final name **MentalModel** by clause DEC-0012_1 — self-explanatory to any audience, no collision with "framework". The `CF-` and `FRAME-` prefixes are retired.

## Purpose

Holds the reference structures thinking happens *through*: glossaries, taxonomies, worldview documents, architectural lenses, evaluation grids — the instruments you pick per problem (first principles, inversion, the vital few) and apply deliberately. MentalModels live in the **Why ring** of the cognition cycle (clause DEC-0008_1) together with Values and Preferences — they condition every downstream stage without being stages themselves. Constitutive decisions are the only path that rewrites this ring.

## Frontmatter schema

```yaml
entity: MentalModel
status: active | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
version: <SemVer>
supersedes: [<MM id>...]
superseded-by: <MM id> | null
related-decs: [<DEC id>...]      # decisions that approved/amended this mental model
topics: [<canonical topic>...]
```

## Lifecycle states

`active` → `superseded`. Minor changes (additions, clarifications) bump `updated` and `version` in place. Major restructure → a new versioned MentalModel that `supersedes` the prior (bidirectional). Living document by design.

## Usage example (generic)

```
MM-0003-20260514-canonical-glossary-pointer.md
  entity: MentalModel
  status: active
  version: 2.0.0
  related-decs: [DEC-0012-…]
  topics: [vocabulary-discipline, meta-framework]
Body: purpose · what this mental model is FOR · the lens itself (or the pointer to the norm).
```

## Cross-reference patterns

- Approved/amended by → `related-decs`.
- Points to the norm, never copies it (P12 — a MentalModel that mirrors a canonical document is drift waiting to happen; make it a pointer).
- Supersession → bidirectional `supersedes`/`superseded-by`.

## Anti-patterns

- A MentalModel that copies a canonical source instead of pointing to it (the glossary-mirror failure).
- Editing a superseded MentalModel (frozen audit trail).
- The `CF-`/`FRAME-` prefixes or the names "CognitiveFramework"/"Frame" (retired — clauses DEC-0008_2, DEC-0012_1).
