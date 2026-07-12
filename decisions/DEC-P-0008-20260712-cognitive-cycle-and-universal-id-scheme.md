---
entity: DecisionRecord
status: pending
kind: constitutive          # proposed by this very DEC (D3) — dogfooding
created: 2026-07-12
updated: 2026-07-12
owner: Andrés Ramírez Sierra
approver: null              # set on approval (P3)
sensitivity: public
originating_slice: null     # back-fill: framework design session with the owner, 2026-07-12
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-2026-07-10-spec-v1-2-0-naming-homologation, DEC-2026-05-12-three-layer-ip-boundary]
topics: [entity-catalog, vocabulary-discipline, corpus-integrity, foundational]
vocabulary-changes: ["Frame", "Conclusion", "Priority", "cognition cycle", "decision kind (constitutive/strategic/tactical)", "defines-goal", "serves-goal", "decided-by", "SLC (slice coordinate)"]
consistency-check: |
  Extends DEC-2026-07-10-spec-v1-2-0-naming-homologation before its publication: the
  v1.2.0 cut exists only on an unmerged branch, so on approval this proposal is absorbed
  into the same cut (one migration, not two). Preserves the 13-entity catalog of
  DEC-2026-05-12-three-layer-ip-boundary — no entity is added or removed; three are
  renamed for plain-language clarity (Frame, Conclusion, Priority) and DecisionRecord
  gains a kind axis with goal edges. Replaces naming.md §2 (dual ID schemes) with one
  universal grammar, superseding that section's rationale: the collision-avoidance that
  motivated date-based vault IDs is re-provided by mandatory counter discipline plus the
  counter-atomicity validator. The Slice ID format in the glossary (BL-XX.SEC-XX.SL-XXX)
  is replaced by the SLC coordinate (D6). P5 (plans as derived views) is deliberately
  reaffirmed, not amended. No conflicts with licensing or the IP boundary.
---

# DEC-P-0008 — The Cognition Cycle and the Universal ID Scheme

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 — Audit Plane Discipline, P1 — Decision Integrity by Construction). This
> record is **born under the naming it proposes** (`DEC-P-NNNN-YYYYMMDD-slug`, number from
> the counter pre-flight of principle P9 — Shared-Resource Pre-flight: 7 prior decisions → 0008). If approved, it is renamed
> `DEC-0008-20260712-…` — same number, same date, new prefix (D5.3).

## Summary

The catalog stops being a flat list and is presented as the **cognition cycle** — the
natural order in which anything gets built: philosophize → observe → conclude → decide →
aim → focus → act → record → learn again. Three entities are renamed to plain words
(Frame, Conclusion, Priority — names must not contain states or jargon). DecisionRecord
gains a **kind** axis (constitutive / strategic / tactical) whose truth is carried by
goal edges, closing the "what comes first, a decision or a goal?" question: *the strategic
decision creates the goal; the goal disciplines the tactical decisions that follow.* All
artifact IDs unify into **one grammar**: `PREFIX-NNNN-YYYYMMDD-slug`, including slices
(`SLC…SEC…BL…`). SliceOps is a framework for building anything; software is its first
instantiation.

## Context

The v1.2.0 naming homologation fixed *prefixes*; using it surfaced deeper ontology debt,
confirmed by a full-ecosystem census (2026-07-12):

- **Goal: 0 instances across all 10 corpora** — every `goals/` folder empty — while
  ActivePriority overflowed with 13 files of which only 3 are actual priorities (the rest:
  handoffs, briefs, checklists, drafts). The pyramid was inverted: the urgent was tracked
  without the important that would justify it. "Priority over *what*?" had no answer.
- **ActivePriority carries a state in its name** — an "ActivePriority" with
  `status: resolved` is a self-contradiction, the same defect the v1.2.0 lifecycle-in-prefix
  work removed from decisions (state lived in `accepted/` folders). Same principle, same fix.
- **Two ID schemes** (counter-based repos, date-based vaults) confused the owner of the
  standard himself — a standard that needs a footnote to explain its own filenames fails
  its purpose.
- **LearningPattern** is accurate but opaque; the framework must be understandable in
  plain words. What the entity holds are **conclusions**.
- The dotted Slice ID (`BL-XX.SEC-XX.SL-XXX`) is fragile in exactly the places it lives:
  git refs restrict dot sequences, and dots inside `.md` filenames confuse tooling.

The philosophical grounding (each stage of the cycle is a region one tradition
specialized in — teleology at Aim, empiricism at Observe, falsificationism at Conclude,
existentialism at Decide, stoicism at Values and Focus, dialectics at the supersession
chain) is recorded in the owner's design session notes, maintained internally. The
framework's contribution is not inventing the stages; it is making the whole cycle
**auditable, file-based, and enforced at the point of write**.

## Decision

### D1 — The catalog is presented on the cognition cycle

Catalog numbers 01–13 remain stable identifiers (never re-ordered, same discipline as
knowledge-category numbers). The *teaching and reading order* becomes the cycle:

```
        VALUES (VAL- / PREF-) · FRAME-            ← the WHY; constitutive DECs
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

`REL-` and `CP-` are not stages: they are transversal infrastructure (relationships and
packaged context feed every box). DecisionRecord appears **twice** by design — one entity,
two moments, like water appearing as vapor and rain in the water cycle.

### D2 — Three entities renamed to plain words (catalog stays 13)

| Was | Becomes | Prefix | Semantics preserved |
|---|---|---|---|
| CognitiveFramework | **Frame** | `FRAME-` | a mental model / lens; no collision with "framework" (the framework has frames) |
| LearningPattern | **Conclusion** | `CONC-` | lifecycle `candidate → canonical → retired` unchanged; **≥3 supporting insights remains the promotion rule to `canonical`** (empirical conclusions); single-chain reasoned conclusions may exist as `candidate` |
| ActivePriority | **Priority** | `PRI-` | state moves fully to `status:` (`open → in-progress → blocked → resolved`); an entity name must never contain a state |

### D2.1 — The complete catalog as it will read (13 entities, definitions included)

Stable numbers are identifiers, never re-ordered; the **Cycle stage** column is the
teaching order of D1. Lifecycle values live in `status:` — never in names (D2's rule).

| # | Entity | Prefix | Definition — what one file of this entity holds | Cycle stage | Lifecycle (`status:`) |
|---|---|---|---|---|---|
| 01 | **DecisionRecord** | `DEC-` / `DEC-P-` / `DEC-D-` | A commitment: what was decided, by whom (`owner`/`approver`), why, which alternatives were weighed and discarded, with what consequences. Carries `kind: constitutive / strategic / tactical` and the goal edges (D3). The audit plane's first-class artifact. | Decide — appears twice: after Conclude (strategic) and after Focus (tactical); constitutive decisions rewrite the Values ring | `pending → approved → deprecated` (state also in the prefix) |
| 02 | **InsightRecord** | `INS-` | One empirical observation, captured raw before it is rationalized — what surprised, what drifted, what a hunch says. Append-only and blameless: never edited to "correct", always answered with a newer insight. | Learn / Observe | `active → archived` |
| 03 | **OutcomeRecord** | `OUTC-` | What actually happened: shipped scope, forecast versus actual, evidence references. `kind: retrospective / postmortem / result` is mandatory. Closed outcomes are immutable; corrections append. | Record / Examine | `open → closed` |
| 04 | **Capability** | `CAP-` | An accrued competence — what an actor *can now do that it could not before* ("we know how to parse financial documents into structured records"). Described by sibling components `standard` (how the result must look), `runbook` (how it executes), `playbook` (what to do per situation) via `kind:`. | Act — accrues from repeated action | `emerging → established → deprecated` |
| 05 | **Goal** | `GOAL-` | A measurable objective with a stated `horizon` (now / quarter / year / multi-year) and a `measure`. REQUIRES `decided-by:` — the decision that created it (D4). Vision is a multi-year Goal with a narrative body (D7.1). | Aim | `proposed → active → achieved / abandoned` (abandonment requires rationale) |
| 06 | **Conclusion** *(was LearningPattern)* | `CONC-` | What we now believe: a generalization promoted from repeated insights (three or more supporting observations to become canonical) or reached by explicit reasoning (stays candidate until evidenced). Conclusions change beliefs; decisions change actions. | Conclude | `candidate → canonical → retired` |
| 07 | **Frame** *(was CognitiveFramework)* | `FRAME-` | A mental model or lens the corpus reasons with: glossaries, taxonomies, worldview documents, architectural frames. The framework has frames the way a body has cells. | Why — the worldview ring | `active → superseded` |
| 08 | **ContextPack** | `CP-` | Packaged, routable context loaded at session start — the portable bundle that lets any agent begin already knowing. Briefs prepared for another session belong here. | Transversal infrastructure (feeds every stage) | `active → superseded` |
| 09 | **Priority** *(was ActivePriority)* | `PRI-` | A ranked commitment of focus: what is being worked now/next and in which order. REQUIRES `serves-goal:` and an integer `rank` unique within `(owner, horizon)` (D4) — buckets do not order; ranks do. The name carries no state: `status:` does. | Focus | `open → in-progress → blocked / resolved` |
| 10 | **RelationshipContext** | `REL-` | The relationship fabric: people, organizations and entities, and how they relate — the edges that condition every other stage. | Transversal infrastructure | `active → archived` |
| 11 | **Preference** | `PREF-` | A stated taste or working choice (style, tooling, approach) — softer than a Value, still worth recording so agents stop re-asking. | Why — the worldview ring | `active → superseded` |
| 12 | **Value** | `VAL-` | A terminal criterion — what is cared about for its own sake; the base case where justification stops and `serves-value:` edges terminate. Constraint-shaped values ("we never do X") are values with teeth. | Why — the ring constitutive decisions rewrite | `active → superseded` |
| 13 | **Session** | `SESS-` | The unit of human–artificial-intelligence interaction: one conversation, identifiable and auditable, with model, cost and provenance recorded. The Slice is the development Session-Type: every slice is a session; not every session is a slice. | Act | `active → archive / delete` |
| — | *Slice coordinate* | `SLC[n]SEC[n]BL[n]` | Not an entity: the **work coordinate** (slice within section within block) used in branches, commits, trackers and `originating_slice:` (D6). | Act — the address of action | not applicable |

### D3 — DecisionRecord gains a kind axis; the edges carry the truth

```yaml
kind: constitutive | strategic | tactical
defines-goal: [<GOAL id>…]   # REQUIRED when strategic — the decision creates/kills/reframes goals
serves-goal: <GOAL id>       # REQUIRED when tactical — the decision selects means within a goal
serves-value: <VAL id>       # the recursion's base case: strategic decisions with no goal above
```

- **Constitutive** decisions change the rules of the system itself (principles, naming,
  licensing, governance — rules about rules). They REQUIRE `approver:` and the elevated
  human-in-the-loop gate (P3 — Human-in-the-Loop Authority), now machine-checkable.
- **Strategic** decisions change the goal tree. **Tactical** decisions move within it.
  Operational test: *does this decision change the goal tree, or move inside it?*
- The boundary is **fractal, not binary**: a decision may carry both edges (tactical
  toward its parent goal, strategic toward the sub-goals it creates). Strategic at level
  n is tactical at level n+1. This is why kinds are one entity, not three (a split would
  break the single audit plane, the supersession graph, and turn every borderline case
  into a filing debate).
- Validator coherence rules: `strategic` without `defines-goal` → error; `tactical`
  without `serves-goal` → error; `constitutive` with `status: approved` and no
  `approver` → error.

### D4 — The pyramid becomes mandatory (goal provenance and priority ordering)

- `Goal.decided-by: <DEC id>` — REQUIRED. Every goal traces to the decision that created
  it (mirror edge of `defines-goal`, bidirectional like `supersedes`/`superseded-by`).
  A goal without an originating decision is unaccountable ambition.
- `Priority.serves-goal: <GOAL id>` — REQUIRED. "Priority over what" is answerable only
  as an ordering of focus toward goals.
- `Priority.rank: <int>` — unique within scope `(owner, horizon)` — replaces the
  three-bucket `priority: high|medium|low` (buckets don't order; ranks do).
- Full provenance chain, machine-checkable end to end:
  `VAL → INS/CONC → DEC(strategic) → GOAL → PRI → DEC(tactical) → SESS/SLC → OUTC → INS ↺`

### D5 — One universal ID grammar for all entity artifacts

```
PREFIX-NNNN-YYYYMMDD-slug-in-kebab-case.md
```

1. **`NNNN`** — per-corpus, per-entity counter; **minimum 4 digits, zero-padded,
   unbounded** (`\d{4,}`: …9999 → 10000 → …). Counters are finite/serialized shared
   resources: every corpus REQUIRES the `.counters/` discipline (P9 pre-flight: re-scan
   the real max before claiming) and the counter-atomicity validator detects collisions.
2. **`YYYYMMDD`** — the creation date, compact (no dashes), immutable. Migration derives
   it from frontmatter `created:`, falling back to first git commit date. The compact
   form makes new names visually distinct from legacy date-based names during migration.
3. **Number and date are stable across the lifecycle**: `DEC-P-0008-…` → approval →
   `DEC-0008-…`. One counter per entity, shared across lifecycle prefixes (a new
   `DEC-0008` colliding with an existing `DEC-D-0008` is a detected error).
4. **Slug**: kebab-case, lowercase only (case-insensitive-filesystem safety, web-address
   convention, shell and pattern-matching safety — formalizes the existing corpus convention).
5. Short citations (`DEC-0008`) are unambiguous **within** a corpus; cross-corpus
   citations carry corpus context or the full filename.
6. Scope: the 13 catalog entities' artifact files. Replaces naming.md §2's dual scheme.

### D6 — The slice coordinate: `SLC`, letters as separators

```
SLC0012SEC03BL02          full coordinate (slice ∈ section ∈ block)
SLC0034                   simple form — SEC/BL optional (matches existing practice)
```

- Replaces `BL-XX.SEC-XX.SL-XXX`. **No dots** (git refs restrict dot sequences; dots in
  `.md` filenames confuse tooling). **No inner hyphens** (hyphen is the field separator
  of the universal grammar); the component letters are the separators.
- `SLC` leads — the slice is the framework's atomic unit and its namesake. Minimum
  widths: `SLC` 4 digits, `SEC`/`BL` 2 digits; all unbounded per D5.1.
- In frontmatter: `originating_slice: SLC0012SEC03BL02`. In branches/commits/PR titles:
  the bare coordinate (git supplies dates). As a materialized file it joins the universal
  grammar: `SLC0012SEC03BL02-20260712-slug.md`.
- **Migration is forward-only for git history**: coordinates inside merged commit
  messages and historical refs are immutable history (same standing as `99-archive/`) —
  covered by the alias map. Trackers, ledgers, frontmatter, and living docs are rewritten.

### D7 — Three conventions (no new entities)

1. **Vision** lives as `GOAL-` with `horizon: multi-year` and a narrative body (the
   misfiled manifesto drafts were the evidence of this missing home). If it proves
   cramped ≥3 times, that evidence may justify promotion (P8 — Recursive Learning by Capture) — not before.
2. **Intuition** enters the system as `INS-` with low verification — the framework's job
   is to capture hunches before they are rationalized, not to exclude them.
3. **The graveyard is part of the audit plane**: strategic and constitutive decisions
   record what was considered and *discarded* (strategy is also what you choose not to
   do). Already structurally present in "Alternatives considered"; now stated as intent.
4. **Plain language in documents**: acronyms and initialisms are defined at first use in
   every artifact, and headings prefer plain words — the decision template's "TL;DR"
   heading (internet shorthand for *Too Long; Didn't Read*) becomes **"Summary"**. A
   standard sold on clarity does not gate its own documents behind jargon.

### D8 — Application (on approval)

Absorbed into the **unpublished v1.2.0 cut** (the branch has never been pushed): naming.md
§1–§3 rewritten (new table below), glossary/catalog/templates/validator updated, and the
migration re-run **once** across the SliceOps corpora with the final rules — so Etapa 2
reaches the other corpora with one stable standard. The Datta runtime enumeration rename (before general
availability, "pre-GA") extends to Frame, Conclusion, Priority. If the owner prefers a separate version
cut instead of absorption, this ships as v1.3.0 with identical content.

The canonical catalog table is D2.1 (single source — naming.md and the entity catalog
are rewritten from it, never copied by hand). Retired additionally on approval: `LP-`,
`CF-`, `AP-`, `BL-XX.SEC-XX.SL-XXX`, `priority: high|medium|low`, and the "TL;DR"
template heading (D7.4).

## Alternatives considered

- **A — Split DecisionRecord into Strategic/Tactical entities**: rejected — the audit
  plane's power is uniformity (one lifecycle, one supersession graph, one validator);
  the boundary is fractal, so a split turns every real decision into a filing debate.
  Kinds + edges give the distinction machine-checkable truth without the split.
- **B — Keep the dual ID scheme** (counters in repos, dates in vaults): rejected by the
  owner — a standard whose own filenames need a footnote is failing at being simple. The
  collision risk that motivated date-based vault IDs is re-covered by mandatory counter
  discipline + the counter-atomicity gate. Uniformity is worth the discipline cost.
- **C — Fixed-width counters (exactly 4 digits)**: rejected — a ceiling breaks at scale
  (one corpus reached ~800 decisions in four months). Unpadded free-width: rejected —
  breaks lexicographic listing immediately. **Minimum-width, unbounded** takes both wins.
- **D — Keep the dotted slice ID, or hyphenate the composite**: rejected — dots are
  fragile in git refs and `.md` names; inner hyphens would collide with the universal
  grammar's field separator. Letter-anchored components are self-separating and regex-clean.
- **E — Add Vision/Plan/Product entities**: rejected — Vision maps to multi-year Goals
  (D7.1); the absence of Plan is a philosophical position to defend, not a gap (principle P5 — Stage as DAG-Derived View:
  stages and plans are *derived views* of the dependency graph, never imperative artifacts);
  Product is a corpus artifact, not a cognition. The catalog stays at 13.

## Consequences

**Enables**: a standard explainable in one breath (one grammar, plain-word entities, a
cycle anyone can draw); machine-checkable strategy discipline (no goal without a deciding
DEC, no priority without a goal, no strategic decision without the goal it creates);
`SliceOps` branding carried by its own atomic unit (`SLC`). **Constrains**: every corpus
runs counter discipline (`.counters/` + P9 pre-flight + collision gate); constitutive
decisions cannot ship without a named approver. **Costs**: one full re-rename of the
just-migrated SliceOps corpora *before* publication (single migration, branches never
pushed); Datta enum rename widened by three; slice-ID history in git remains under the
old format (alias map covers it).

## Ratification note

Pending the owner's approval. On approval: set `approver:`, rename this file
`DEC-P-0008-…` → `DEC-0008-…`, rewrite references atomically (rule R5 — atomic lifecycle transitions), and execute D8.

## References

- [`DEC-2026-07-10-spec-v1-2-0-naming-homologation.md`](DEC-2026-07-10-spec-v1-2-0-naming-homologation.md) — the homologation this extends (absorbed into the same unpublished cut).
- [`DEC-2026-05-12-three-layer-ip-boundary.md`](DEC-2026-05-12-three-layer-ip-boundary.md) — the 13-entity B.1 catalog this preserves (renames, no growth).
- [`../spec/v1.2.0/naming.md`](../spec/v1.2.0/naming.md) — §2 (dual ID schemes) superseded by D5; tables rewritten per D8.
- [`../reference/entity-catalog/`](../reference/entity-catalog/) — entries 05/06/07/09 and 01 amended per D2–D4.
- Principle P5 (Stage as DAG-Derived View) — reaffirmed by alternative E and D7: plans are derived, never decreed.
