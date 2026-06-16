# Entity Catalog — Layer B.1 (v1.0)

The canonical SliceOps™ cognitive entity catalog: **13 universal entities**. SliceOps IP, shared across vendors (documentation under CC BY 4.0; final terms pending IP/Legal — see `../../governance/IPR_POLICY.md`).

These 13 entities are **vendor-neutral and runtime-independent** — each carries meaning standalone in markdown. Runtimes may extend the catalog with runtime-specific entities under their own IP; such extensions are NOT part of this canonical catalog (P8 — Platform-Agnostic; see `../../spec/v1.0.0/ip-boundary.md`).

## The 13 entities

| # | Entity | Purpose | Mapped principle |
|---|---|---|---|
| 1 | [DecisionRecord](01-decision-record.md) | Architectural/strategic decisions with lifecycle, supersession, rationale | P2, P4 |
| 2 | [InsightRecord](02-insight-record.md) | Empirical observations from slices; raw material for LearningPatterns | P7 |
| 3 | [OutcomeRecord](03-outcome-record.md) | Tracked outcomes of slices/blocks — what shipped, what worked | P5 |
| 4 | [Capability](04-capability.md) | Capabilities accrued by individuals/agents/teams | P7 |
| 5 | [Goal](05-goal.md) | Forward-looking objectives at various time horizons | universal |
| 6 | [LearningPattern](06-learning-pattern.md) | Patterns observed ≥3 times across InsightRecords | P7 |
| 7 | [CognitiveFramework](07-cognitive-framework.md) | Mental models for reasoning and decision-making | universal |
| 8 | [ContextPack](08-context-pack.md) | Pre-computed bundles loaded at session start (evolves to *routed* per Context Router) | P8 |
| 9 | [ActivePriority](09-active-priority.md) | Current priorities tracked with status and ownership | universal |
| 10 | [RelationshipContext](10-relationship-context.md) | Cross-references between entities/people/orgs | universal |
| 11 | [Preference](11-preference.md) | Stated preferences (style, tooling, approach) | universal |
| 12 | [Value](12-value.md) | Core values guiding decisions | P9 |
| 13 | [Session](13-session.md) | The unit of human–AI interaction; the Slice is the DEV Session-Type | P2, P4, P5 |

> **Note on "Skill"**: entity #4 is **Capability** ("capabilities accrued"). The term **"Skill"** is **reserved** for the future *Agent-Skill* concept (a vendor-neutral procedural pack) and must NOT be used for this entity.

## Per-spec structure

Each entity spec contains:

1. **Purpose** — what the entity is for and mapped principle(s)
2. **Frontmatter schema** — the canonical YAML fields (vendor-neutral)
3. **Lifecycle states** — valid status values and transitions
4. **Usage example** — a generic, vendor-neutral example
5. **Cross-reference patterns** — how it links to other entities
6. **Anti-patterns** — explicitly prohibited usage

## Canonical frontmatter key

The vendor-neutral canonical type key is `entity:` (value = the entity name, e.g., `entity: DecisionRecord`). Runtimes MAY map this to a runtime-specific typed key, but the canonical, portable, standalone form is `entity:`. Adopters keep `entity:` for cross-adopter interoperability.

## Naming

`NN-kebab-name.md` (number = catalog order). The number is for ordering/navigation only; the canonical identifier is the entity name.

## Adopter rules

Adopters **may**: use the catalog as-is (recommended — preserves interop); add adopter-specific entities (in their own brain, not here); fork with renames/extensions (requires attribution and documenting in adopter DECs). Adopters **may not**: remove canonical entities and still claim SliceOps-compliance; conflict canonical entity semantics.
