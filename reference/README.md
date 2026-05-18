# reference/ — Capa B reference patterns + templates + schemas

Vendor-agnostic, stack-agnostic reference material that materializes the canonical principles. SliceOps IP under CC BY 4.0 (documentation) + MIT (code templates / workflow exemplars).

## Sub-folders

| Folder | Content | Capa |
|---|---|---|
| `entity-catalog/` | 12 canonical cognitive entity specs (DecisionRecord, InsightRecord, OutcomeRecord, Capability, Goal, LearningPattern, CognitiveFramework, ContextPack, ActivePriority, RelationshipContext, Preference, Value) — each with frontmatter schema + lifecycle + generic examples + anti-patterns | B.1 |
| `knowledge-categories/` | 27 canonical knowledge categories (reference taxonomy v1.0) | B.1 |
| `r-rules/` | R1–R14 starter templates (regex vendor-agnostic, adopter-instantiable) | B.1 |
| `frontmatter-schemas/` | Abstract frontmatter schemas (DEC, InsightRecord, LearningPattern, CognitiveFramework) including Layer 1 consistency-management fields | B.1 |
| `templates/` | File templates (slice, DEC, InsightRecord, etc.) | B.1 |
| `workflows/` | CI workflow exemplars (full reference implementation lives in the SliceOps toolkit repo) | B.2 |

## Status

Scaffolding in progress. Sub-folders are placeholders; Capa B.1 content drafting is the next work batch.

## Note on "Skill" vs "Capability"

Cognitive entity #4 is **Capability** ("capabilities accrued by individuals/agents/teams"). The term **"Skill"** is **reserved** for the future *Agent-Skill* concept (a vendor-neutral procedural pack: description + instructions + deterministic tools + composability + recursive improvement + invocation control). Do not use "Skill" for the cognitive entity.
