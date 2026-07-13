# Entity Catalog — Layer B.1 (v2.0)

The canonical SliceOps™ cognitive entity catalog: **13 universal entities**, presented on the **cognition cycle** — the natural order in which anything gets built. SliceOps IP, shared across vendors (documentation under CC BY 4.0 — ratified, see `../../governance/IPR_POLICY.md`). Governed by [`DEC-0008`](../../decisions/DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md); this README is rewritten from clause DEC-0008.2.1 (the single-source table) and never edited independently of it.

These 13 entities are **vendor-neutral and runtime-independent** — each carries meaning standalone in markdown. Runtimes may extend the catalog with runtime-specific entities under their own IP; such extensions are NOT part of this canonical catalog (P11 — Platform-Agnostic; see `../../spec/v2.0.0/ip-boundary.md`).

## The cognition cycle

The catalog numbers are stable identifiers (never re-ordered); the **cycle** below is the teaching and reading order. It applies to building anything — software is the first instantiation:

```
        VALUES (VAL- / PREF-) · FRAME-            ← the WHY; constitutive decisions
            │ philosophize                          rewrite this ring (elevated gate)
            ▼
        INSIGHTS (INS-) ──≥3──▶ CONCLUSIONS (CONC-)
            │                        │
            ▼                        ▼
   ┌── DEC · kind: strategic ── defines-goal ──┐
   │        │                                   │
   │        ▼                                   │
   │    GOAL (GOAL-, decided-by ▲)              │
   │        │                                   │
   │        ▼                                   │
   │    PRIORITY (PRI-, serves-goal ▲, rank)    │
   │        │                                   │
   │        ▼                                   │
   │    DEC · kind: tactical ── serves-goal     │
   │        │                                   │
   │        ▼                                   │
   │    ACTION (SESS- / SLC…) ──accrues──▶ CAP- │
   │        │                                   │
   │        ▼                                   │
   └─── OUTCOME (OUTC-) ──examine──▶ INS- ──────┘   ↺ P8
```

DecisionRecord appears **twice** by design — one entity, two moments (strategic decisions create goals; tactical decisions select means within them). `REL-` and `CP-` are not stages: they are transversal infrastructure feeding every box. Locating context is the job of the corpus index `_index.md` (reserved-name infrastructure, [`DEC-0010`](../../decisions/DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md) — not an entity).

**The whole cycle runs ON the audit plane** — auditing is not a stage, it is the property every stage has by construction: every box leaves evidence (P6 — Evidence-by-Construction, machine-validatable as evidence.v1), every arrow is traceable (P2 — Audit Plane Discipline: provenance, append-only, supersession edges), machine gates verify at write and merge time (hooks, continuous-integration validators, the corpus sweeper), and the human examination cadence is first-class (the **Audit** Session-Type, Block Retrospectives as `OUTC-` `kind: retrospective` with the Cross-DEC Consistency Check, and quarterly curation). The Record stage is where a cycle *examines itself*; the plane is what makes the examination possible at every point.

## The 13 entities

Every entity has exactly **one canonical filename prefix** under the universal grammar `PREFIX-NNNN-YYYYMMDD-slug.md` — normative source: [`spec/v2.0.0/naming.md`](../../spec/v2.0.0/naming.md).

| # | Entity | Prefix | Holds | Cycle stage |
|---|---|---|---|---|
| 01 | [DecisionRecord](01-decision-record.md) | `DEC-` / `DEC-P-` / `DEC-D-` | A commitment: what was decided, by whom, why, with which alternatives — with `kind: constitutive / strategic / tactical` and goal edges | Decide (two moments) |
| 02 | [InsightRecord](02-insight-record.md) | `INS-` | One empirical observation, captured raw, append-only, blameless | Learn / Observe |
| 03 | [OutcomeRecord](03-outcome-record.md) | `OUTC-` | What actually happened (`kind: retrospective / postmortem / result` mandatory) | Record / Examine |
| 04 | [Capability](04-capability.md) | `CAP-` | An accrued competence; components `standard`/`runbook`/`playbook` via `kind:` | Act (accrual) |
| 05 | [Goal](05-goal.md) | `GOAL-` | A measurable objective with horizon and `decided-by:` provenance | Aim |
| 06 | [Conclusion](06-conclusion.md) | `CONC-` | What we now believe (≥3 insights to become canonical) — *was LearningPattern* | Conclude |
| 07 | [Frame](07-frame.md) | `FRAME-` | A mental model or lens — *was CognitiveFramework* | Why ring |
| 08 | [ContextPack](08-context-pack.md) | `CP-` | Packaged context: `kind: pack / brief / handoff` ([`DEC-0009`](../../decisions/DEC-0009-20260712-handoffs-as-a-contextpack-kind.md)) | Transversal |
| 09 | [Priority](09-priority.md) | `PRI-` | A ranked commitment of focus (`serves-goal:` + `rank:` mandatory) — *was ActivePriority* | Focus |
| 10 | [RelationshipContext](10-relationship-context.md) | `REL-` | Relationships among people, organizations and entities | Transversal |
| 11 | [Preference](11-preference.md) | `PREF-` | A stated taste or working choice | Why ring |
| 12 | [Value](12-value.md) | `VAL-` | A terminal criterion — where justification stops | Why ring |
| 13 | [Session](13-session.md) | `SESS-` | The unit of human–artificial-intelligence interaction; the Slice is the development Session-Type | Act |

> **Note on "Skill"**: entity 04 is **Capability**. The term **"Skill"** remains **reserved** for the executable agent artifact (execution plane) and must NOT be used for this entity.

## Per-spec structure

Each entity spec contains: purpose and mapped principles · frontmatter schema · lifecycle states · usage example · cross-reference patterns · anti-patterns.

## Canonical frontmatter key

The vendor-neutral canonical type key is `entity:` (value = the entity name). Runtimes MAY map this to a runtime-specific typed key; `entity:` is the portable, standalone form (P11). Adopters keep `entity:` for cross-adopter interoperability.

## Naming

Catalog spec files here: `NN-kebab-name.md` (number = stable identifier; ordering/navigation only). **Artifact instances** follow the universal grammar with per-corpus counters and the `.counters/` discipline — normative rules, retired aliases and reserved infrastructure names in [`spec/v2.0.0/naming.md`](../../spec/v2.0.0/naming.md).

## Adopter rules

Adopters **may**: use the catalog as-is (recommended — preserves interop); add adopter-specific entities (in their own corpus, not here); fork with renames/extensions (requires attribution and documenting in adopter DECs). Adopters **may not**: remove canonical entities and still claim SliceOps-compliance; conflict canonical entity semantics.
