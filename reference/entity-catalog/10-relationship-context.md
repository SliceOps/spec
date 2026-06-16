# RelationshipContext — Layer B.1 Cognitive Entity

> Cross-references between entities, people, or orgs. **Mapped principle: universal.**

## Purpose

Makes a relationship a first-class, queryable artifact rather than an implicit link buried in prose — "entity X depends on Y", "person A owns domain B", "org C adopts framework D". RelationshipContext is the connective tissue that lets the corpus be traversed as a graph (supporting audit-plane reachability, P2/P4) without coupling to any runtime's graph engine (P8).

## Frontmatter schema

```yaml
entity: RelationshipContext
status: active | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
subject: <entity id | actor>
predicate: depends-on | owns | adopts | supersedes | relates-to | blocks
object: <entity id | actor>
directional: true | false
```

## Lifecycle states

`active` → `archived` (the relationship no longer holds; archived, not deleted, to preserve historical graph state for audit).

## Usage example (generic)

```
REL-022-team-owns-auth-domain.md
  entity: RelationshipContext
  status: active
  subject: platform-team
  predicate: owns
  object: domain:auth
  directional: true
Body: nature of the relationship · since when · evidence.
```

## Cross-reference patterns

- Edges between any two entities/actors (`subject` → `predicate` → `object`).
- Complements (does not replace) typed frontmatter edges like `supersedes`/`depends_on` — use RelationshipContext for relationships that are not already a first-class typed field.
- Archived edges retained → historical graph reconstruction.

## Anti-patterns

- Duplicating a typed edge that already exists in frontmatter (e.g., re-encoding `supersedes` as a RelationshipContext) — redundant, drift risk.
- Deleting instead of archiving (loses historical graph state).
- Free-text relationship with no canonical `predicate` (defeats queryability).
- Using it to encode a decision (decisions are DECs — P2).
