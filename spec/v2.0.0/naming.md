# SliceOps™ Canonical Naming — v2.0.0

The canonical naming standard for SliceOps artifacts: **one concept = one name = one prefix, across every layer**. This document is the **single normative source** for artifact naming; every other document (reference patterns, adopter corpora, vendor docs) points here and never copies the tables (copies drift — P12 Context Discipline).

Introduced in v1.2.0 by `DEC-2026-07-10-spec-v1-2-0-naming-homologation` (see `../../decisions/`).

---

## 1. Canonical prefix per entity

Every Layer B.1 cognitive entity has exactly **one** canonical filename prefix. The prefix and the entity name are identical in every store — engineering repos, knowledge vaults, runtime exports.

| # | Entity (Layer B.1) | Prefix | Retired aliases (prohibited) |
|---|---|---|---|
| 1 | DecisionRecord | `DEC-` · `DEC-P-` · `DEC-D-` (lifecycle, §3) | `DR-`, the term "RFC" |
| 2 | InsightRecord | `INS-` | `IN-`, `IR-` |
| 3 | OutcomeRecord | `OUTC-` (`kind:` — §6) | `OC-`, `BR-` |
| 4 | Capability | `CAP-` (components — §5) | `SKILL-`, `RUN-`, `REF-` |
| 5 | Goal | `GOAL-` | — |
| 6 | LearningPattern | `LP-` | `REF-` (patterns misuse) |
| 7 | CognitiveFramework | `CF-` | — |
| 8 | ContextPack | `CP-` | — |
| 9 | ActivePriority | `AP-` | — |
| 10 | RelationshipContext | `REL-` | — |
| 11 | Preference | `PREF-` | — |
| 12 | Value | `VAL-` | — |
| 13 | Session | `SESS-` | — |

`REF-` is retired as a prefix entirely: it was a catch-all hiding three distinct entities (coding standards → `CAP-`, patterns → `LP-`, third-party integrations → vendor connector entities). A prefix that maps to more than one entity is the anti-pattern this standard exists to prevent.

## 2. ID schemes: local per store, prefix global

The **prefix is global; the ID scheme is local** to the store type:

| Store type | ID scheme | Example |
|---|---|---|
| Engineering repos / corpora with `.counters` | sequential `NNN` (counter discipline, Layer B.1) | `DEC-041-slug.md`, `INS-013-slug.md` |
| Knowledge vaults (date-natural corpora) | `YYYY-MM-DD` (date + slug carries uniqueness) | `DEC-2026-07-10-slug.md`, `CF-2026-05-14-slug.md` |

Both schemes are canonical. What is **not** allowed: changing the prefix or the entity name per store. `DEC-041` (repo) and `DEC-2026-07-10-slug` (vault) are the same entity with the same prefix under two ID schemes.

## 3. DecisionRecord lifecycle — carried in the prefix

The lifecycle state of a decision is visible in its filename:

| Prefix | State | `status:` frontmatter |
|---|---|---|
| `DEC-` | approved (in force) | `approved` |
| `DEC-P-` | pending (proposed, under deliberation) | `pending` |
| `DEC-D-` | deprecated / superseded (requires `superseded-by:` when superseded) | `deprecated` |

**Flat `decisions/` folder.** Because the prefix carries the state, lifecycle folders (`rfcs/`, `accepted/`, `superseded/`, `deprecated/`) are retired: every decisions folder is **flat**. A state change renames the file (`DEC-P-…` → `DEC-…`) and rewrites all references in the same atomic change (R5).

**The term "RFC" is retired** from the SliceOps vocabulary (confusing: it named both a process and a folder and collided with IETF usage). A proposal is a **pending DecisionRecord** (`DEC-P-`). The governance process formerly called "RFC process" is the **proposal process** (`governance/PROPOSAL-PROCESS.md`).

### `status:` values and read tolerance

Canonical DecisionRecord `status:` values are exactly `pending` / `approved` / `deprecated`. Legacy values `proposed`, `ratified`, `superseded` (and adopter variants such as `active` / `accepted` on decision artifacts) are **read-tolerated**: a conforming parser MAY map them (`proposed`→`pending`, `ratified`/`active`/`accepted`→`approved`, `superseded`→`deprecated`) when reading archives or third-party corpora, but a conforming validator MUST reject them on write in a homologated corpus.

The `approver:` field (optional since v1.1.0 — the human who approved, P3) is unchanged; its recommendation now reads "recommended on `status: approved`".

## 4. Immutable archives

`99-archive/` folders (R10 immutability) are **never renamed**. Historical names inside archives are covered by each corpus's **alias map** (old → new), emitted by the migration tooling. Everything outside archives is renamed retroactively — homologation is total, not forward-only.

## 5. Capability model: one entity, components by `kind:`

**Capability is the capacity** — the WHAT ("we know how to parse financial PDFs into structured databases"). It is the mother entity. Three **component kinds** describe it (siblings of each other, never nested):

| `kind:` | Answers |
|---|---|
| `standard` | how the result must look (acceptance shape) |
| `runbook` | how it is executed, step by step |
| `playbook` | what to do depending on the situation |

Implementation: a **small** capability is one `CAP-` file with sections; a **large** one is a `CAP-` mother file plus component files carrying `capability: <mother-slug>` and `kind: standard|runbook|playbook` in frontmatter. The catalog does **not** grow — Capability remains one entity (#4).

**"Skill" stays reserved** for the executable agent artifact (execution plane, Agent-Skills style). It is not a catalog entity. Knowledge plane (Capability: what the org can do) and execution plane (Skill: what an agent runs) remain distinct.

## 6. OutcomeRecord `kind:`

Every OutcomeRecord declares `kind: retrospective | postmortem | result`. Block Retrospectives are OutcomeRecords with `kind: retrospective` (the former standalone `BR-` prefix is retired into this).

## 7. Alias table — pre-v1.2.0 → v1.2.0 migration

Scheme-level renames a migrating corpus applies (per-file alias maps are emitted per corpus by the migration tooling):

| Pre-v1.2.0 (or wild) | v1.2.0 canonical | Rule |
|---|---|---|
| `DR-<id>` | `DEC-<id>` / `DEC-P-<id>` / `DEC-D-<id>` (by state) | lifecycle in prefix |
| `decisions/rfcs/<file>` | `decisions/DEC-P-<file>` | flatten |
| `decisions/accepted/<file>` | `decisions/DEC-<file>` | flatten |
| `decisions/superseded|deprecated/<file>` | `decisions/DEC-D-<file>` | flatten |
| `IN-<id>`, `IR-<id>` | `INS-<id>` | one Insight prefix |
| `OC-<id>`, `BR-<id>` | `OUTC-<id>` (+ `kind:`) | one Outcome prefix |
| `SKILL-<id>`, `RUN-<id>` | `CAP-<id>` | one Capability prefix |
| `REF-<id>` (coding standards) | `CAP-<id>` | REF- split |
| `REF-<id>` (patterns) | `LP-<id>` | REF- split |
| `status: proposed/ratified/superseded` | `pending/approved/deprecated` | status homologation |
| term "RFC" | "pending DecisionRecord" / `DEC-P-` | vocabulary retirement |

## 8. Implementation aliases (vendor runtimes)

Known Layer C.1 runtime names that map to canonical B.1 entities. Runtimes migrating to the canonical names use this table; the **canonical name always wins** in shared/portable form (P11):

| Runtime name (implementation alias) | Canonical B.1 entity |
|---|---|
| AgentContextPack | ContextPack |
| AgentSkill | Capability |
| GoalObjective | Goal |
| ValuePrinciple | Value |
| AgentPreference | Preference |

Runtime-**proprietary** entities (entities whose meaning depends on that runtime to operate) are NOT in the canonical catalog and are not renamed by this standard — they follow the vendor-extension mechanism in [`ip-boundary.md`](ip-boundary.md) (Layer C).

## 9. Enforcement

The standard self-imposes at the point of write (published-not-enforced is the failure mode this section closes):

1. **Norm without copies** — naming lives only here; other docs link.
2. **Agent context** — each corpus's agent-context file (`AGENTS.md` / `CLAUDE.md`) carries a short NAMING block pointing here.
3. **Write hook** — the toolkit **naming validator** runs as an agent pre-write hook and blocks non-homologated names, indicating the correct one.
4. **CI gate + sweeper** — the same validator runs as a merge gate in repos with CI and as a periodic sweep over vaults without CI.

Reference implementation: `sliceops-toolkit/templates/naming-validator/`.
