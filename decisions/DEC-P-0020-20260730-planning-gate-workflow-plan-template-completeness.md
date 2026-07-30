---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-30
updated: 2026-07-30
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # origin: a downstream adopter-session incident, 2026-07-30 (see Context)
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-P-0017-20260730-spec-level-vocabulary-substrate-and-anchor, DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections, DEC-0011-20260713-canonical-corpus-container-and-layout]
topics: [slice-workflow, layer-b-framework-artifact, meta-framework, consistency-management, evidence-categories]
vocabulary-changes: ["plan gate (new canonical term)", "definition of ready (new canonical term, scoped to the plan)"]
consistency-check: |
  Additive Layer B.1 artifacts plus one new gate; no Layer A principle is amended and no
  existing artifact is retired. SliceOps mechanizes conformance at exactly one moment —
  merge (P6 Evidence-by-Construction, the CI validators, the naming validator) — and has
  nothing at plan time: `reference/workflows/` is empty but for `.gitkeep`, there is no plan
  template among the eleven in `reference/templates/`, `reference/templates/slice-template.md`
  never mentions model-triage, context-band or sensitivity, and none of the ten checks in the
  consistency validators inspects a slice or a plan. This record adds the missing plan-time
  artifacts and names the gate. P5 keeps its statement verbatim — the clarification in clause 5
  distinguishes the *altitude* of a plan (deliberately coarse, correct) from its *completeness*
  (every declared slice carries every declared field), which P5 never conflated but a partial
  reader can. P6's scope is unchanged: the plan gate is a second gate, not a widening of the
  evidence gate. Two new canonical terms therefore land in the glossary at approval, in the
  next MINOR. BLOCKED DEPENDENCY: clause 2 must state where a plan file lives, and the corpus
  currently answers that in two incompatible ways — `reference/project-structure/README.md`
  prescribes sibling `architecture/` and `specs/` folders with no plans location, while
  naming.md §7 (DEC-0011) places architecture and specs together inside `50-products/` and
  plans in `60-execution/62-plans`. project-structure predates DEC-0011 and was never
  updated; it mentions neither `_sliceops`, nor `50-products`, nor `60-execution`. That drift
  needs its own record and is named in Consequences, not resolved here.
---

# DEC-P-0020 — The plan gate: planning workflow, plan template, slice-template routing, completeness validator

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1, P2, P8).
> **Status: pending.** Constitutive: it adds a mandatory gate to the framework contract, so it
> lands only with the human ratification P3 requires (`approver:` set on approval).

## Summary

SliceOps gates the **slice** and never gates the **plan**. Every mechanized check in the
framework — CI validators, naming validator, evidence schema — fires at or after merge, when
code already exists. An incomplete plan fails against nothing. This record adds the four
missing plan-time artifacts (a planning workflow, a plan template, routing pointers in the
slice template, a completeness validator) and names the result the **plan gate**: the
pre-execution counterpart of P6's evidence gate.

## Context

**The incident.** In an adopter session, the agent produced a plan and its DAG, then was asked
whether the product specs were complete. They were not: **4 of 9**. It wrote the missing five,
then two more surfaced — 9 of 9 — and regenerated plan and DAG. Asked next to show the plan as
a table with blocks, sections and slice sizes, it checked again and found it had **5 of the 13
elements** SliceOps defines for a slice: no sections in the coordinate, no evidence plan, no
model triage, no HITL, no P9/P10 declarations. It completed them, correctly, in one pass.

Twice, complete work was one prompt away — and the prompt had to come from the human.

**What the corpus offered the agent.** Four verifiable gaps:

1. **`reference/workflows/` is empty** — `.gitkeep` and nothing else. The framework reserved a
   folder for its workflows and never wrote one. The act being performed — substrate specs →
   plan → slice decomposition → DAG — is documented nowhere.
2. **No plan template.** `reference/templates/` holds eleven: capability, dec, goal, handoff,
   index, insight-record, outcome-record, policy, priority, **slice**, sliceops-json. The slice
   has a canonical shape; the plan has none. "Is the plan complete?" is therefore not a
   checkable question — there is nothing to check it against.
3. **The slice template does not route to what a slice needs.** `slice-template.md` carries
   eight sections and zero occurrences of `model-triage`, `context-band` or `sensitivity`. The
   model-triage axes live in `reference/model-triage/`, the bands in `reference/sizing/`, the
   coordinate grammar in `naming.md` §5, and P3/P9/P10 in `principles.md`. The thirteen
   elements of a slice are distributed across at least five files and enumerated in none. The
   count itself is unverifiable — which is the finding, not an aside.
4. **No validator inspects a slice or a plan.** The ten consistency checks are
   frontmatter-schema, no-orphan-decs, cross-references-bidirectional, topic-tags,
   counter-atomicity, principle-count-coherence, entity-count-coherence, band-unit, llm-ci-cost
   and evidence-schema. Every one operates on the decision corpus or on the framework's
   self-coherence. None looks at the unit of work.

**The reading that licensed it.** P5 states, correctly, that *"the plan is a hypothesis;
execution discovers the leaves… detail that changes no decision is waste."* That is a claim
about **altitude** — how finely to cut slices. A partial reader applies it to **completeness** —
which fields a declared slice carries. P5 licenses not enumerating the leaves; it does not
license omitting the HITL, the model triage or the evidence plan of the slices already
enumerated.

**This is the second instance of one pattern.** DEC-P-0017 records the first: a true statement
about one axis (the spec's sovereignty) read as permission on another (the spec's existence).
Here: a true statement about one axis (planning altitude) read as permission on another (field
completeness). Same shape, different principle. Under P8 a third instance promotes this to a
LearningPattern; it is named here so the third is recognized when it arrives.

## Decision

**1. The planning workflow is written.** `reference/workflows/` gains the canonical flow from
substrate specs (DEC-P-0017) to plan to slice decomposition to derived DAG (P5), stating at
each step what must exist before the next may begin. The folder stops being a declared gap.

**2. A plan template joins the canonical eleven.** `reference/templates/plan-template.md`, with
an explicit **definition of ready**: the enumerated conditions a plan satisfies before any slice
in it may execute. At minimum — every slice cites the substrate spec it decomposes
(DEC-P-0017 clause 2); every slice carries the full declared field set of clause 3; blocks and
sections are assigned under `naming.md` §5; dependencies are declared so the DAG is derivable
rather than authored (P5); externally blocked slices are marked as blocked rather than omitted.

**3. The slice template routes to every element a slice declares.** `slice-template.md` gains
explicit pointers to `reference/model-triage/` (both axes, context-band primary and sensitivity
→ locality) and `reference/sizing/` (token-band, context-band), and names the coordinate's
section component. The template stops assuming the reader already knows which sibling folders
exist. **This clause is fix-on-touch drift repair (P12) and does not depend on ratification.**

**4. A completeness validator enforces the gate.** The consistency validators gain a check that
reads a plan and its slices and fails on missing declared fields, on a slice that cites no
substrate spec, and on a DAG that does not derive from the declared dependencies. It is the
first mechanized check that fires **before** code exists.

**5. Scope of P5 (clarification, no amendment).** P5 governs the **altitude** of a plan: the
plan commits to structure, execution discovers the leaves, and a sub-slice is the notation for a
leaf that emerged late. P5 does not govern **completeness**: a slice that is declared is
declared in full. Coarse-but-complete is the intended state; fine-but-partial and
coarse-and-partial are both defects. The sub-slice rate remains the health signal for altitude
(DEC-0014_4) and is not evidence about completeness in either direction.

## Alternatives considered

- **Fix only the slice template (clause 3)** — rejected as insufficient, though it is the
  cheapest clause and lands regardless. It closes the routing gap that made the agent guess
  which folders to open, but leaves the plan itself shapeless and unchecked. The first failure
  in the incident — 4 of 9 substrate specs — happened before any slice template was consulted.
- **Document only, no validator (clauses 1–3, drop 4)** — rejected. The framework's own
  evidence is that documentation the reader must know to seek does not reach a partial reader;
  that is the entire finding of DEC-P-0017. A gate that is prose is a reminder; a gate that runs
  is a gate. P6's authority comes from executing, not from being written down.
- **Extend P6 to cover plan time instead of adding a second gate** — rejected. P6 is
  Evidence-by-Construction: evidence *closes* a unit of work. A plan produces no evidence; it
  produces a commitment. Overloading P6 would blur the one binary it makes auditable. Two named
  gates at two moments is the honest model.
- **Promote plan completeness to a thirteenth principle** — rejected under anti-over-promotion
  discipline. Nothing here is a new axiom: clause 5 clarifies P5, clause 4 mechanizes P12's
  "context authored, not assumed", clause 2 operationalizes DEC-P-0017. Layer B.1 artifacts and
  one gate, no Layer A change.
- **Wait for the layout drift to be resolved first** — rejected as sequencing. Clauses 1, 3, 4
  and 5 are independent of where a plan file lives. Only clause 2 needs the answer, and it can
  state the definition of ready while citing DEC-0011 as the location authority and flagging
  project-structure as the stale sibling.

## Consequences

**Enables**: "is this plan ready to execute?" becomes a mechanized question rather than a
matter of whether the human thought to ask · the thirteen elements of a slice become
enumerable in one place for the first time · plan-time defects surface before token spend on
execution, which is the cheapest moment to find them (P9 economics).

**Constrains**: a plan that fails the definition of ready blocks execution of its slices ·
adopters carrying informal plans must formalize them to pass the new check · the slice
template grows, against the pressure to keep templates short.

**Costs**: one new reference folder, one new template, one validator with its tests · a glossary
MINOR for `plan gate` and `definition of ready` · re-issue of adopter plans that predate the
gate.

**Blocked dependency, named not resolved**: clause 2 must say where a plan lives, and the corpus
answers twice, incompatibly. `reference/project-structure/README.md` prescribes
`foundations/ decisions/ architecture/ specs/ execution/ insights/` — sibling `architecture/`
and `specs/`, no plans location, and no mention of `_sliceops`, `50-products` or `60-execution`.
`naming.md` §7 (DEC-0011, later) places architecture and specs **together** inside
`50-products/` ("the complete WHAT: definition + architecture + specs + reference") and plans in
`60-execution/62-plans`. A third variant exists in the P12 Implication chain, which includes
`plan` where project-structure omits it. project-structure is the stale document and DEC-0011
the authority, but the correction is a separate constitutive record with its own cross-reference
impact — it is not folded in here. Until it lands, clause 2 cites DEC-0011.

**Observed, not decided here**: the framework's own workspace does not follow DEC-0011. Where a
multi-repo product workspace requires a git repository named `_sliceops` as sibling of the code
repositories, the SliceOps workspace carries loose `00-foundation/` (files prefixed `FND-`, a
prefix absent from the canonical grammar, under the retired three-digit counter form) and a
`30-context-packs/` holding one placeholder. Recursive dogfooding is a stated property of this
project; this is where it is not yet true.

## References

- P5 (Stage as DAG-Derived View), P6 (Evidence-by-Construction), P9, P12 —
  [`spec/v2.1.0/principles.md`](../spec/v2.1.0/principles.md)
- `reference/templates/slice-template.md` — the eight declared sections
- `reference/model-triage/`, `reference/sizing/` — the axes and bands clause 3 routes to
- `reference/workflows/` — the empty folder clause 1 fills
- `naming.md` §5 (slice coordinate), §7 (canonical container and layout, DEC-0011)
- DEC-P-0017 — the first instance of the axis-confusion pattern; clause 2 depends on its
  substrate-spec derivation rule
- DEC-0014_4 — sub-slice rate as the altitude health signal referenced by clause 5
