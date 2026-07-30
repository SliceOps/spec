---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-30
updated: 2026-07-30
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # origin: maintainer questions surfacing a three-way layout contradiction, 2026-07-30
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0011-20260713-canonical-corpus-container-and-layout, DEC-P-0020-20260730-planning-gate-workflow-plan-template-completeness, DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme]
topics: [folder-structure, corpus-integrity, context-discipline, consistency-management, adopter, meta-framework]
vocabulary-changes: ["context architecture chain (clarified: a reading order, never a folder list)"]
consistency-check: |
  No principle is amended and no canonical layout is changed — DEC-0011 already decided the
  layout and this record makes the corpus say so consistently. Three loci currently answer
  "where does a thing live?" differently: P12's Implication states the chain
  `foundations → decisions → architecture → specs → plan → execution`;
  `reference/project-structure/README.md` prescribes six sibling folders
  (`foundations/ decisions/ architecture/ specs/ execution/ insights/`) with no plans location
  and no mention of `_sliceops`, `50-products` or `60-execution`; `naming.md` §7 and DEC-0011_2–_4
  prescribe the `_sliceops/` decade container, place architecture and specs together inside
  `50-products/<product>/`, and put plans in `60-execution/62-plans`. project-structure predates
  DEC-0011 and was never updated — it is the stale locus, and DEC-0011 the authority. The
  reconciliation is therefore a rewrite of one Layer B.1 reference artifact plus a clarification
  that P12's chain is a reading order rather than a folder list; both restate existing decisions
  and add none. Unblocks the dependency DEC-P-0020 named in its Consequences: a plan lives at
  `60-execution/62-plans/` (DEC-0011_4), so the plan template can state its location. The public
  quickstart is in application scope and is the most urgent locus: it teaches forms DEC-0008
  retired.
---

# DEC-P-0021 — Canonical layout reconciliation: one answer to "where does it live?"

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1, P2, P12).
> **Status: pending.** Constitutive: it settles which of three loci is normative about corpus
> layout, so it lands only with the human ratification P3 requires.

## Summary

Three places in the corpus answer "where does a thing live?" and they disagree. DEC-0011 already
decided the answer — a `_sliceops/` decade container with architecture and specs together inside
`50-products/<product>/` and plans in `60-execution/62-plans/` — but
`reference/project-structure/` still prescribes the pre-DEC-0011 layout, and P12's chain reads
like a folder list when it is a reading order. This record names DEC-0011 as the single
authority, rewrites the stale artifact, and clarifies the chain. It unblocks DEC-P-0020 clause 2
and puts three drifted surfaces into application scope, the public quickstart first.

## Context

**The three answers.**

| Locus | Says | Status |
|---|---|---|
| P12 Implication (Layer A) | `foundations → decisions → architecture → specs → plan → execution` | correct as a **reading order**; misreadable as a folder list |
| `reference/project-structure/` (Layer B.1) | six sibling folders: `foundations/ decisions/ architecture/ specs/ execution/ insights/` — no plans location | **stale**: predates DEC-0011, mentions neither `_sliceops`, nor `50-products`, nor `60-execution` |
| `naming.md` §7 + DEC-0011_2–_4 (Layer B.1) | `_sliceops/` decade container; architecture and specs **inside** `50-products/<product>/`; plans in `60-execution/62-plans/` | **authority** — later, and decided by record |

The contradiction is not subtle: project-structure makes `architecture/` and `specs/` top-level
peers, DEC-0011_3 makes them siblings *inside* a product, and neither mentions the other. A
reader who lands on project-structure builds the wrong corpus and never learns it.

**How it surfaced.** The maintainer, reading DEC-P-0017, asked why `architecture` was not part
of the product's specs — having previously settled the cognition cycle. Both halves of the
question were right: DEC-0011_3 does place architecture inside `50-products/` ("the complete
WHAT: definition + architecture + specs + reference"), and the cognition cycle (DEC-0008_1) is a
different map from P12's chain. The confusion was authored by the corpus, not by the reader.

**Two maps, routinely conflated.** The **cognition cycle** (DEC-0008_1) orders *entities* —
values → insights → conclusions → strategic decision → goal → priority → tactical decision →
action → capability. It answers "in what order is knowledge produced?" The **context
architecture chain** (P12) orders *dependency*: what must exist before what may be authored. It
answers "what may I write next?" Neither is a directory listing. The directory listing is
DEC-0011's decade container, and it is a third thing that *satisfies* both.

**Three drifted surfaces, found while verifying.**

1. **`reference/project-structure/`** — the stale prescription above.
2. **The public quickstart** (`SliceOps/quickstart`) — the day-1 onramp adopters clone. It ships
   `10-decisions/` with `accepted/` and `rfcs/` subfolders, and `70-execution/`. Every one of
   those is retired: decisions live at `30-decisions/` and are **flat** (DEC-0008_5), lifecycle
   is carried in the prefix not in folders, "RFC" is a retired term (a proposal is `DEC-P-`),
   and execution is `60-execution/`. Its evidence file names a slice `sl-001`, which is not a
   coordinate under `naming.md` §5. The onramp teaches what the framework retired.
3. **The SliceOps workspace itself** — four sibling repositories and no `_sliceops` container.
   In its place: `00-foundation/` holding `FND-001…FND-006` (a prefix absent from the canonical
   fourteen, under the three-digit counter form v2.0.0 retired) and a `30-context-packs/`
   containing one placeholder. DEC-0011_1 requires a git repository named `_sliceops`, sibling
   of the code repositories, for exactly this shape of workspace.

## Decision

**1. DEC-0011 is the single authority on layout.** Where any artifact disagrees with
`naming.md` §7 or DEC-0011_2–_4 about where something lives, the artifact is drifted and is
corrected on touch (P12). No new layout is introduced by this record.

**2. `reference/project-structure/` is rewritten to describe the decade container**, including
an explicit chain → decade mapping so a reader arriving from P12 lands correctly:

| Chain position (P12) | Decade (DEC-0011) |
|---|---|
| foundations | `00-context/` (`01-values`, `02-preferences`, `03-mental-models`) |
| decisions | `30-decisions/` (flat) |
| architecture | `50-products/<product>/architecture/` |
| specs (substrate specs, DEC-P-0017) | `50-products/<product>/specs/` |
| plan | `60-execution/62-plans/` (derived only, P5) |
| execution | `60-execution/` (`61-priorities`, `63-dags`, `64-fleet-agents`, `65-in-flight`) |
| insights | `10-insights/` → `20-conclusions/` |
| outcomes | `70-outcomes/` |

**3. P12's chain is a reading order, not a folder list (clarification, no amendment).** The
chain states **authoring dependency**: nothing downstream may be authored before what precedes
it exists. It has never been a directory prescription, and text that presents it as one is
drifted. The glossary entry for the chain gains this sentence at approval.

**4. A plan's location is settled.** `60-execution/62-plans/`, with its DAG in `63-dags/`, both
**derived only** (DEC-0011_4, P5) — computed from `depends_on` and re-rendered, never
hand-patched. **This unblocks DEC-P-0020 clause 2**, which could not state a definition of ready
without knowing where the artifact lives.

**5. Architecture and specs are siblings inside a product.** `50-products/<product>/` holds
`definition/`, `architecture/`, `specs/`, `reference/` (DEC-0011_3). They are never top-level
peers of `decisions/`. Restated normatively here because the artifact that contradicted it was
itself a Layer B.1 reference.

**6. Application scope, in order of exposure.** (a) The **quickstart** is rebuilt on the
container — highest urgency, because it is public, cloned on day 1, and currently teaches
retired forms. (b) The **SliceOps workspace** adopts `_sliceops` per DEC-0011_1, migrating
`00-foundation/` into `00-context/` under the canonical grammar. (c) `project-structure/` is
rewritten per clause 2 — **fix-on-touch, applied without waiting for ratification**, since it
corrects an artifact against an already-approved record.

## Alternatives considered

- **Change DEC-0011 to match project-structure** — rejected. project-structure is the older,
  less specific, undecided-by-record artifact; DEC-0011 carries eight clauses, a ratified human
  gate and downstream dependents. Reverting to six flat folders would also discard the zoom rule
  (DEC-0011_3) and the derived-only discipline (DEC-0011_4), both of which are load-bearing.
- **Delete `project-structure/` rather than rewrite it** — rejected. Adopters arrive at it from
  `reference/README.md` and from the P12 chain; deleting the landing page leaves the traffic
  with nowhere correct to go. A rewritten page that maps chain → decade is what a reader coming
  from P12 actually needs.
- **Amend P12's Implication to name the decades** — rejected under anti-over-promotion
  discipline and P11-adjacent reasoning: Layer A states the discipline, Layer B states the
  mechanism. Baking decade numbers into a principle would make an adopter's folder rename a
  principle amendment.
- **Fix only the quickstart, treat the rest as documentation debt** — rejected. The quickstart
  is the most *urgent* locus but not the *causal* one: it drifted because the layout had no
  single authority to conform to. Fixing the copy without naming the source reproduces the drift
  at the next surface.
- **Fold this into DEC-P-0020** — rejected. DEC-P-0020 is about *when* work is gated; this is
  about *where* artifacts live. Merging them would produce a record no future reader could cite
  precisely, and DEC-P-0020 already names this as a blocked dependency rather than absorbing it.

## Consequences

**Enables**: one answer to "where does it live", so a plan template can state a location and a
completeness validator can check one · adopters cloning the quickstart learn the canonical
layout instead of retired forms · the P12 chain stops being readable as a competing layout.

**Constrains**: every artifact describing layout must now conform to DEC-0011 or be corrected on
touch · the quickstart's git history will show a structural break; adopters who cloned the old
shape need a migration note in the alias map (`naming.md` §9).

**Costs**: a rewrite of `project-structure/` · a quickstart rebuild with its own PR in its own
repository · a workspace migration creating one new repository · an alias-map entry mapping the
quickstart's retired folders to their canonical decades.

**Recursive dogfooding, stated plainly**: this record exists because the framework's own
workspace and its own onramp do not follow the framework. Clause 6 is where that stops being
true. Until (a) and (b) land, "SliceOps uses SliceOps" is aspirational for the workspace and
false for the quickstart.

## References

- DEC-0011 clauses _1 (container and unit-of-work), _2 (canonical decades), _3
  (`50-products/` holds the complete what), _4 (`60-execution/` internals, derived-only)
- [`spec/latest/naming.md`](../spec/latest/naming.md) §7 (canonical container and layout),
  §9 (alias tables), §5 (slice coordinate)
- P12 Context Discipline, Implication "Foundations-first governed substrate" —
  [`spec/latest/principles.md`](../spec/latest/principles.md)
- DEC-0008_1 (the cognition cycle — the other map), DEC-0008_5 (flat decisions, prefix lifecycle,
  retired term "RFC")
- DEC-P-0020 — the blocked dependency clause 4 releases
- DEC-P-0017 — `substrate spec`, the artifact that lives at `50-products/<product>/specs/`
