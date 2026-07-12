---
entity: DecisionRecord
status: approved
kind: constitutive          # proposed by this very DEC (Decision 3) — dogfooding
created: 2026-07-12
updated: 2026-07-12
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra   # ratified 2026-07-12 (P3)
sensitivity: public
originating_slice: null     # back-fill: framework design session with the owner, 2026-07-12
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-2026-07-10-spec-v1-2-0-naming-homologation, DEC-2026-05-12-three-layer-ip-boundary]
topics: [entity-catalog, vocabulary-discipline, corpus-integrity, foundational]
vocabulary-changes: ["Frame", "Conclusion", "Priority", "cognition cycle", "decision kind (constitutive/strategic/tactical)", "defines-goal", "serves-goal", "decided-by", "SLC (slice coordinate)", "handoff (ContextPack kind)", "brief (ContextPack kind)", "_index.md (corpus index — reserved-name infrastructure)", "reserved infrastructure names"]
consistency-check: |
  Extends DEC-2026-07-10-spec-v1-2-0-naming-homologation before its publication. The
  v1.2.0 cut exists only on an unmerged branch, so on approval the unpublished cut is
  re-issued as **v2.0.0** — per the repository's own versioning policy this is a major
  version: catalog entity renames, new required fields and the universal identifier
  grammar are breaking changes to the framework contract (a corpus valid under v1.x
  requires migration). One migration, not two; the ecosystem jumps v1.1.0 → v2.0.0. Preserves the 13-entity catalog of
  DEC-2026-05-12-three-layer-ip-boundary — no entity is added or removed; three are
  renamed for plain-language clarity (Frame, Conclusion, Priority) and DecisionRecord
  gains a kind axis with goal edges. Replaces naming.md §2 (dual ID schemes) with one
  universal grammar, superseding that section's rationale: the collision-avoidance that
  motivated date-based vault IDs is re-provided by mandatory counter discipline plus the
  counter-atomicity validator. The Slice ID format in the glossary (BL-XX.SEC-XX.SL-XXX)
  is replaced by the SLC coordinate (Decision 6). P5 (plans as derived views) is deliberately
  reaffirmed, not amended. No conflicts with licensing or the IP boundary.
---

# DEC-0008 — The Cognition Cycle and the Universal ID Scheme

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 — Audit Plane Discipline, P1 — Decision Integrity by Construction). This
> record is **born under the naming it proposes** (`DEC-P-NNNN-YYYYMMDD-slug`, number from
> the counter pre-flight of principle P9 — Shared-Resource Pre-flight: 7 prior decisions → 0008). If approved, it is renamed
> `DEC-0008-20260712-…` — same number, same date, new prefix (Decision 5.3).

## Summary

The catalog stops being a flat list and is presented as the **cognition cycle** — the
natural order in which anything gets built: philosophize → observe → conclude → decide →
aim → focus → act → record → learn again. Three entities are renamed to plain words
(Frame, Conclusion, Priority — names must not contain states or jargon). DecisionRecord
gains a **kind** axis (constitutive / strategic / tactical) whose truth is carried by
goal edges, closing the "what comes first, a decision or a goal?" question: *the strategic
decision creates the goal; the goal disciplines the tactical decisions that follow.* All
artifact IDs unify into **one grammar**: `PREFIX-NNNN-YYYYMMDD-slug`, including slices
(`SLC…SEC…BL…`); handoffs — the most-used coordination artifact — are standardized as a
ContextPack kind (Decision 9), and every corpus carries a reserved-name index
(`_index.md`) so agents know where to look without ever searching wholesale (Decision 10). These are breaking changes to the framework contract, so this ships as
**SliceOps v2.0.0** (the unpublished v1.2.0 cut is re-issued; v1.1.0 remains the last
published 1.x). SliceOps is a framework for building anything; software is its first
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

### Decision 1 — The catalog is presented on the cognition cycle

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

### Decision 2 — Three entities renamed to plain words (catalog stays 13)

| Was | Becomes | Prefix | Semantics preserved |
|---|---|---|---|
| CognitiveFramework | **Frame** | `FRAME-` | a mental model / lens; no collision with "framework" (the framework has frames) |
| LearningPattern | **Conclusion** | `CONC-` | lifecycle `candidate → canonical → retired` unchanged; **≥3 supporting insights remains the promotion rule to `canonical`** (empirical conclusions); single-chain reasoned conclusions may exist as `candidate` |
| ActivePriority | **Priority** | `PRI-` | state moves fully to `status:` (`open → in-progress → blocked → resolved`); an entity name must never contain a state |

### Decision 2.1 — The complete catalog as it will read (13 entities, definitions included)

Stable numbers are identifiers, never re-ordered; the **Cycle stage** column is the
teaching order of Decision 1. Lifecycle values live in `status:` — never in names (Decision 2's rule).

| # | Entity | Prefix | Definition — what one file of this entity holds | Cycle stage | Lifecycle (`status:`) |
|---|---|---|---|---|---|
| 01 | **DecisionRecord** | `DEC-` / `DEC-P-` / `DEC-D-` | A commitment: what was decided, by whom (`owner`/`approver`), why, which alternatives were weighed and discarded, with what consequences. Carries `kind: constitutive / strategic / tactical` and the goal edges (Decision 3). The audit plane's first-class artifact. | Decide — appears twice: after Conclude (strategic) and after Focus (tactical); constitutive decisions rewrite the Values ring | `pending → approved → deprecated` (state also in the prefix) |
| 02 | **InsightRecord** | `INS-` | One empirical observation, captured raw before it is rationalized — what surprised, what drifted, what a hunch says. Append-only and blameless: never edited to "correct", always answered with a newer insight. | Learn / Observe | `active → archived` |
| 03 | **OutcomeRecord** | `OUTC-` | What actually happened: shipped scope, forecast versus actual, evidence references. `kind: retrospective / postmortem / result` is mandatory. Closed outcomes are immutable; corrections append. | Record / Examine | `open → closed` |
| 04 | **Capability** | `CAP-` | An accrued competence — what an actor *can now do that it could not before* ("we know how to parse financial documents into structured records"). Described by sibling components `standard` (how the result must look), `runbook` (how it executes), `playbook` (what to do per situation) via `kind:`. | Act — accrues from repeated action | `emerging → established → deprecated` |
| 05 | **Goal** | `GOAL-` | A measurable objective with a stated `horizon` (now / quarter / year / multi-year) and a `measure`. REQUIRES `decided-by:` — the decision that created it (Decision 4). Vision is a multi-year Goal with a narrative body (Decision 7.1). | Aim | `proposed → active → achieved / abandoned` (abandonment requires rationale) |
| 06 | **Conclusion** *(was LearningPattern)* | `CONC-` | What we now believe: a generalization promoted from repeated insights (three or more supporting observations to become canonical) or reached by explicit reasoning (stays candidate until evidenced). Conclusions change beliefs; decisions change actions. | Conclude | `candidate → canonical → retired` |
| 07 | **Frame** *(was CognitiveFramework)* | `FRAME-` | A mental model or lens the corpus reasons with: glossaries, taxonomies, worldview documents, architectural frames. The framework has frames the way a body has cells. | Why — the worldview ring | `active → superseded` |
| 08 | **ContextPack** | `CP-` | Packaged, routable context for sessions, with `kind: pack / brief / handoff` (Decision 9) — pre-computed corpus context, topic briefs, and session handoffs. Packs **contain** context; **locating** it is the corpus index's job (`_index.md`, reserved-name infrastructure — Decision 10, not an entity). | Transversal infrastructure (feeds every stage) | `active → superseded` |
| 09 | **Priority** *(was ActivePriority)* | `PRI-` | A ranked commitment of focus: what is being worked now/next and in which order. REQUIRES `serves-goal:` and an integer `rank` unique within `(owner, horizon)` (Decision 4) — buckets do not order; ranks do. The name carries no state: `status:` does. | Focus | `open → in-progress → blocked / resolved` |
| 10 | **RelationshipContext** | `REL-` | The relationship fabric: people, organizations and entities, and how they relate — the edges that condition every other stage. | Transversal infrastructure | `active → archived` |
| 11 | **Preference** | `PREF-` | A stated taste or working choice (style, tooling, approach) — softer than a Value, still worth recording so agents stop re-asking. | Why — the worldview ring | `active → superseded` |
| 12 | **Value** | `VAL-` | A terminal criterion — what is cared about for its own sake; the base case where justification stops and `serves-value:` edges terminate. Constraint-shaped values ("we never do X") are values with teeth. | Why — the ring constitutive decisions rewrite | `active → superseded` |
| 13 | **Session** | `SESS-` | The unit of human–artificial-intelligence interaction: one conversation, identifiable and auditable, with model, cost and provenance recorded. The Slice is the development Session-Type: every slice is a session; not every session is a slice. | Act | `active → archive / delete` |
| — | *Slice coordinate* | `SLC[n]SEC[n]BL[n]` | Not an entity: the **work coordinate** (slice within section within block) used in branches, commits, trackers and `originating_slice:` (Decision 6). | Act — the address of action | not applicable |

### Decision 3 — DecisionRecord gains a kind axis; the edges carry the truth

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

### Decision 4 — The pyramid becomes mandatory (goal provenance and priority ordering)

- `Goal.decided-by: <DEC id>` — REQUIRED. Every goal traces to the decision that created
  it (mirror edge of `defines-goal`, bidirectional like `supersedes`/`superseded-by`).
  A goal without an originating decision is unaccountable ambition.
- `Priority.serves-goal: <GOAL id>` — REQUIRED. "Priority over what" is answerable only
  as an ordering of focus toward goals.
- `Priority.rank: <int>` — unique within scope `(owner, horizon)` — replaces the
  three-bucket `priority: high|medium|low` (buckets don't order; ranks do).
- Full provenance chain, machine-checkable end to end:
  `VAL → INS/CONC → DEC(strategic) → GOAL → PRI → DEC(tactical) → SESS/SLC → OUTC → INS ↺`

### Decision 5 — One universal ID grammar for all entity artifacts

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

### Decision 6 — The slice coordinate: `SLC`, letters as separators

```
SLC0012SEC03BL02          full coordinate (slice ∈ section ∈ block)
SLC0034                   simple form — SEC/BL optional (matches existing practice)
```

- Replaces `BL-XX.SEC-XX.SL-XXX`. **No dots** (git refs restrict dot sequences; dots in
  `.md` filenames confuse tooling). **No inner hyphens** (hyphen is the field separator
  of the universal grammar); the component letters are the separators.
- `SLC` leads — the slice is the framework's atomic unit and its namesake. Minimum
  widths: `SLC` 4 digits, `SEC`/`BL` 2 digits; all unbounded per Decision 5.1.
- In frontmatter: `originating_slice: SLC0012SEC03BL02`. In branches/commits/PR titles:
  the bare coordinate (git supplies dates). As a materialized file it joins the universal
  grammar: `SLC0012SEC03BL02-20260712-slug.md`.
- **Migration is forward-only for git history**: coordinates inside merged commit
  messages and historical refs are immutable history (same standing as `99-archive/`) —
  covered by the alias map. Trackers, ledgers, frontmatter, and living docs are rewritten.

### Decision 7 — Three conventions (no new entities)

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

### Decision 8 — Application (on approval): re-issue the unpublished cut as v2.0.0

**Version verdict — major, by the repository's own policy** ("breaking changes to the
framework contract lead to a new major"): renaming catalog entities changes the
inter-layer contract (the schema IS the contract), the new required fields fail
previously-valid documents, and the universal grammar renames every artifact file. A
minor number would misrepresent the migration cost to adopters; version honesty is part
of selling a standard.

Mechanics — the v1.2.0 branch was never pushed, so nothing public is rewritten:

1. `spec/v2.0.0/` → `spec/v2.0.0/` (directory re-cut; `latest` → `v2.0.0`); v1.0.0 and
   v1.1.0 remain frozen; **v1.2.0 is never published** (it existed only as a working cut —
   the changelog records [2.0.0] as the successor of [1.1.0]).
2. `naming.md`, glossary, entity catalog and templates rewritten from the Decision 2.1 table
   (single source); frontmatter schemas gain the Decision 3/Decision 4 fields; the decision template's
   heading becomes "Summary" (Decision 7.4).
3. The spec's own decisions are renumbered under the universal grammar (chronological per
   the counter pre-flight), and DEC-2026-07-10-spec-v1-2-0-naming-homologation receives an
   amendment annotation (its "v1.2.0" references read as "the cut re-issued as v2.0.0 by
   DEC-0008"); its slug is cleaned to `naming-homologation` in the same rename — a
   one-time liberty available only because the file was never published, recorded in the
   alias map.
4. Validator, hooks, and continuous-integration gates updated to the v2 rules; the
   migration re-runs **once** across the four SliceOps corpora with final rules, so
   Etapa 2 reaches the remaining corpora with one stable standard.
5. The Datta runtime enumeration rename (before general availability, "pre-GA") extends
   to Frame, Conclusion, Priority, plus the new fields (kind, defines-goal, serves-goal,
   decided-by, rank).
6. The evidence.v1 `decisionRefs` pattern is extended additively to accept the universal
   form (`DEC-0008-20260712-slug`); all previously accepted forms remain read-tolerated.

The canonical catalog table is Decision 2.1 (single source — naming.md and the entity catalog
are rewritten from it, never copied by hand). Retired additionally on approval: `LP-`,
`CF-`, `AP-`, `BL-XX.SEC-XX.SL-XXX`, `priority: high|medium|low`, and the "TL;DR"
template heading (Decision 7.4).

### Decision 9 — Handoffs standardized as a ContextPack kind (added at approval)

Requested by the owner in the ratification message: handoffs are among the most-used
coordination artifacts in practice (one vault's handoff counter alone reached 027), and
they were unstandardized — exactly the vacuum that turned ActivePriority into a catch-all.

A handoff is born in two situations (the owner's definition): **(a) the session's context
is exhausted** and the work must continue elsewhere, or **(b) a specific topic is spun
off** for another session to develop. Both are *packaged context prepared for another
session* — the literal definition of ContextPack. So, by the same discipline as Decision 3
(kinds, never new entities), ContextPack gains a kind axis:

```yaml
entity: ContextPack
kind: pack | brief | handoff              # all three CONTAIN context (locating it is
                                          # the corpus index's job — Decision 10)
from_session: <SESS id or session reference>   # handoff-specific
to: <owner | domain | SESS id> | null          # handoff-specific: who receives the work
reason: context-exhausted | spinoff            # handoff-specific: the two birth conditions
```

- **pack** — routed or pre-computed corpus context loaded at session start (brain-pack style).
- **brief** — context prepared to *start* a new topic or session.
- **handoff** — context prepared to *continue or spin off* in-flight work. Canonical body
  sections: state of work · done · pending · open questions · next steps · counter and
  resource state.
- Files follow the universal grammar (`CP-0028-20260712-slug.md`). Legacy `HANDOFF-NNN`
  identifiers migrate into the ContextPack counter (alias map covers them); handoff
  *ledgers* remain operational index files, not entities.
- Handoffs close the session-provenance loop: the emitting session records the handoff in
  its `outcome`; the receiving session loads it — `SESS-A → CP (handoff) → SESS-B` is
  fully auditable. The catalog stays at 13; a `handoff-template` ships with the templates.

### Decision 10 — The corpus index: reserved-name infrastructure (`_index.md`), not an entity

Added in the ratification conversation, correcting Decision 9's first draft: the index
was initially modeled as a ContextPack kind, and the owner rejected it — an agent would
have to open ContextPacks to discover which ones are indexes, and **an entry point you
must search for defeats itself**. The root distinction: a pack *contains* context; an
index *locates* it. Locating is not containing, so the index is not a cognitive entity
at all — it is **corpus infrastructure**, the same class as `.counters/` (which the
framework already keeps outside the catalog, without frontmatter).

1. **Reserved name, zero discovery**: every corpus carries **`_index.md` at its root**.
   Any agent or human finds it without searching, in every corpus, always — the same
   guarantee `CLAUDE.md`/`AGENTS.md` and `README.md` already give. The underscore sorts
   it first in any listing. Large corpora MAY add per-folder `_index.md` files; the root
   index routes to them (recursive routing, zero discovery at every level).
2. **The loading chain of context engineering**: agent-context file (thin, always
   loaded) → `_index.md` (small, says WHERE) → the exact files or ContextPacks needed.
   No agent reads a corpus wholesale; finding context cheaply is a first-class concern
   of the framework — it is optimized for agentic and human work.
3. **Content**: route tables — topic / entity / question pattern → exact paths or
   ContextPack ids to open. It **points, never copies** (copies drift — P12). It is the
   **materialized routing table of the Context Router**: the router is the mechanism,
   `_index.md` is its artifact. A template ships with the spec templates.
4. **Enforcement**: the validator checks (a) the root `_index.md` exists in every
   homologated corpus, (b) every route target resolves — a stale index is a build
   failure, not a suggestion.
5. **Reserved infrastructure names, formalized**: the universal grammar (Decision 5)
   governs *entity artifacts*; infrastructure files are exempt and their names are
   reserved: `README.md`, `CLAUDE.md`/`AGENTS.md`, `MEMORY.md`, `_organization.md`,
   `_index.md`, `*-ledger.md`, and the `.counters/` directory. This list lives in
   naming.md; anything else must be an entity artifact under the grammar.

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
  (Decision 7.1); the absence of Plan is a philosophical position to defend, not a gap (principle P5 — Stage as DAG-Derived View:
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

**Approved by the owner on 2026-07-12.** At approval the owner added the handoff
standardization, incorporated as Decision 9 in the same act. In the same ratification conversation the
owner (a) required internal section references written out in full ("Decision N", never
"DN"), and (b) raised the corpus-index requirement — first drafted as a ContextPack kind,
then **corrected on the owner's objection** (an entry point you must search for defeats
itself) into Decision 10: `_index.md` as reserved-name corpus infrastructure. All applied
before publication; the correction is kept visible here as the audit trail. Per its own Decision 5.3 the file was renamed
`DEC-P-0008-…` → `DEC-0008-…` (number and date stable, prefix carries the new state) and
all references were rewritten atomically (rule R5 — atomic lifecycle transitions).
Execution of Decision 8 (the v2.0.0 re-issue and single migration) begins immediately.

## References

- [`DEC-2026-07-10-spec-v1-2-0-naming-homologation.md`](DEC-2026-07-10-spec-v1-2-0-naming-homologation.md) — the homologation this extends (absorbed into the same unpublished cut).
- [`DEC-2026-05-12-three-layer-ip-boundary.md`](DEC-2026-05-12-three-layer-ip-boundary.md) — the 13-entity B.1 catalog this preserves (renames, no growth).
- [`../spec/v2.0.0/naming.md`](../spec/v2.0.0/naming.md) — §2 (dual ID schemes) superseded by Decision 5; the whole cut re-issues as `spec/v2.0.0/` per Decision 8.
- [`../spec/README.md`](../spec/README.md) — the versioning policy whose "breaking → major" rule Decision 8 applies.
- [`../reference/entity-catalog/`](../reference/entity-catalog/) — entries 05/06/07/09 and 01 amended per Decision 2–Decision 4.
- Principle P5 (Stage as DAG-Derived View) — reaffirmed by alternative E and Decision 7: plans are derived, never decreed.
