# CognitiveFramework — Layer B.1 Cognitive Entity

> Mental models and reference structures for reasoning and decision-making. **Mapped principle: universal.**

## Purpose

A reusable mental model or reference structure that other entities consult — e.g., the canonical glossary, the topic taxonomy, a decision rubric. CognitiveFrameworks are *living reference substrate*: not a decision (DEC), not an observation (InsightRecord), but the shared scaffolding reasoning is performed against.

## Frontmatter schema

```yaml
entity: CognitiveFramework
status: active | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
version: <SemVer>
supersedes: [<CF id>...]
superseded-by: <CF id> | null
related-decs: [<DEC id>...]      # DECs that ratified/amended this framework
topics: [<canonical topic>...]
```

## Lifecycle states

`active` → `superseded`. Minor changes (additions, clarifications) bump `updated` and `version` patch/minor in place. Major restructure → a new versioned CF that `supersedes` the prior (bidirectional). Living document by design.

## Usage example (generic)

```
CF-canonical-glossary.md
  entity: CognitiveFramework
  status: active
  version: 1.0.0
  related-decs: [DR-...-consistency-management]
  topics: [vocabulary-discipline, meta-framework]
Body: purpose · per-item structure · the items · maintenance.
```

## Cross-reference patterns

- Ratified/amended by → `related-decs`.
- Consulted by → DECs (via `topics`/`vocabulary-changes`), Layer 1 frontmatter discipline.
- Versioned evolution → `supersedes`/`superseded-by`.

## Anti-patterns

- Encoding a decision as a CognitiveFramework to bypass the audit plane (decisions are DECs — P2).
- Major restructure done in place without a superseding versioned CF (loses audit trail).
- A CognitiveFramework no entity references (orphan scaffolding).
