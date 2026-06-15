# reference/ — Capa B reference patterns + templates + schemas

Vendor-agnostic, stack-agnostic reference material that materializes the canonical principles. SliceOps IP under CC BY 4.0 (documentation) + MIT (code templates / workflow exemplars).

## Sub-folders

| Folder | Content | Capa |
|---|---|---|
| `entity-catalog/` | 13 canonical cognitive entity specs (DecisionRecord, InsightRecord, OutcomeRecord, Capability, Goal, LearningPattern, CognitiveFramework, ContextPack, ActivePriority, RelationshipContext, Preference, Value, **Session**) — each with frontmatter schema + lifecycle + generic examples + anti-patterns | B.1 |
| `sessions/` | Session-Type taxonomy (8 canonical Session-Types + Slice-Types level 2 + 2 orthogonal axes) — hierarchical, replaces earlier flat 17-label practice | B.1 |
| `sizing/` | Bidimensional sizing: **token-band** (throughput, billed-equivalent) + **context-band** (peak footprint, model-viability filter) + calibration discipline | B.1 |
| `model-triage/` | Model Triage artifact: 5 axes (context-band primary filter → sensitivity → complexity → latency → cost) + execution-modes + synthesis efficiency + consuming/producing distinction | B.1 |
| `context-router/` | Context Router: selective routing of context-experts (consumption side) — pairs with synthesis efficiency in Model Triage (production side) | B.1 |
| `knowledge-categories/` | 27 canonical knowledge categories (reference taxonomy v1.0) | B.1 |
| `r-rules/` | R1–R14 starter templates (regex vendor-agnostic, adopter-instantiable) | B.1 |
| `frontmatter-schemas/` | Abstract frontmatter schemas (DEC, InsightRecord, LearningPattern, CognitiveFramework) including Layer 1 consistency-management fields | B.1 |
| `templates/` | File templates (slice, DEC, InsightRecord) | B.1 |
| `agent-skill/` | Agent-Skill concept spec (vendor-neutral procedural-pack concept; distinct from the Capability cognitive entity) | B.1 |
| `patterns/` | Capa B.2 Universal Engineering Patterns — reaffirmed industry-canonical + SliceOps-formalized (Determinism-over-Regeneration, CI/Pipeline Cost Economy) | B.2 |
| `workflows/` | CI workflow exemplars (full reference implementation lives in the SliceOps toolkit repo) | B.2 |

## Status

Capa B.1 reference core drafted: entity-catalog, knowledge-categories, r-rules, frontmatter-schemas, templates, agent-skill, patterns. `workflows/` exemplars + adopter onboarding are remaining.

## Note on "Skill" vs "Capability"

Cognitive entity #4 is **Capability** ("capabilities accrued by individuals/agents/teams"). The term **"Skill"** is **reserved** for the future *Agent-Skill* concept (a vendor-neutral procedural pack: description + instructions + deterministic tools + composability + recursive improvement + invocation control). Do not use "Skill" for the cognitive entity.
