---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-30
updated: 2026-07-30
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # origin: a downstream adopter-session misread, 2026-07-30 (see Context)
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0015-20260716-p1-statement-provenance-axis-clarity]
topics: [vocabulary-discipline, context-discipline, slice-workflow, corpus-integrity, meta-framework]
vocabulary-changes: ["substrate spec (new canonical term)", "slice spec-anchor (new canonical term; nominalizes the existing spec-anchoring entry)", "spec (canonical term becomes ambiguous alone — must be qualified)"]
consistency-check: |
  Additive vocabulary, no principle amended. The canonical noun `spec` currently denotes two
  distinct artifacts at two distinct layers, and the corpus never separates them: the
  pre-plan product/architecture specification that P12's context architecture places between
  `architecture` and `plan` (principles.md, P12 Implication — "foundations → decisions →
  architecture → specs → plan → execution"), and the per-slice scope declaration P4 names as
  the first element of a slice ("spec, decision, code, tests, evidence, merge"), materialized
  in reference/templates/slice-template.md as Scope + Acceptance criteria. This record names
  them `substrate spec` and `slice spec-anchor` and makes bare `spec` a term that must be
  qualified. Nothing is renamed or retired: `spec-anchored` / `spec-anchoring` (glossary) stand
  unchanged and gain a noun form; `spec-driven` and `specless` remain prohibited aliases with
  their existing reasons. P4, P8 and P12 keep their statements verbatim — the record adds a
  reading rule over them, not a new obligation. Because it introduces canonical terms, P12
  requires the glossary to carry them; released versions are immutable, so the glossary entries
  land in the next MINOR (v2.2.0, in preparation) at approval time, not in v2.1.0. The
  companion fix to AGENTS.md is fix-on-touch drift repair (P12) against an already-canonical
  source and does not depend on this record's approval.
---

# DEC-P-0017 — Spec-level vocabulary: `substrate spec` and `slice spec-anchor`

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1, P2, P8).
> **Status: pending.** Constitutive: it amends the canonical vocabulary, so it lands only with
> the human ratification P3 requires (`approver:` set on approval).

## Summary

The canonical noun **`spec`** silently denotes two different artifacts at two different layers,
and no canonical term separates them. An adopter session, reading the corpus correctly at every
individual step, concluded that a build plan may be derived without product-level
specifications — citing P8 and the "not spec-driven-first" characterization as authority. The
misread is a corpus defect, not a reading error. This record introduces **`substrate spec`**
(pre-plan, product/architecture level) and **`slice spec-anchor`** (per-slice scope declaration,
P4), states the derivation rule between them, and fixes the scope of "not spec-driven-first" to
sovereignty and mutability — never to existence or timing.

## Context

**The incident.** In an adopter session that produced an 18-slice, 6-wave plan, the agent was
asked whether all product specs were in place. It answered *"No — and they should not be"*,
justified by: (a) *"SliceOps is explicitly not spec-driven-first"*; (b) P8 — you learn by
executing; (c) the specs of waves 2 and 3 are *"deliverables of their own slices"*. It then
declared the plan ready to execute. Waves 2–6 had no product-level definition to derive scope
from.

**Why the corpus produced that answer.** Four compounding causes, each verifiable:

1. **Drift in the agent-facing restatement.** [`AGENTS.md`](../AGENTS.md) §Decision-first reads
   *"a decision-driven framework, **not a spec-first one**"*. The normative source says
   `not spec-driven-**first**` and explicitly permits the opposite of what AGENTS.md asserts:
   *"An adopter can be **spec-first AND SliceOps-compliant**"*
   ([`reference/development-model/README.md`](../reference/development-model/README.md) §2).
   One word — `driven` — separates rejecting the spec's *sovereignty* from rejecting its
   *timing*. AGENTS.md is the first file an agent loads and the one it weights most. This is
   denormalized-reference drift, the failure mode P12 names in its own Rationale.
2. **Asymmetric salience.** The negation is an H2 heading, restated three times in
   `development-model/README.md` (§ title, §1 title, §"Why NOT"). Every qualification lives in
   a low-salience position: the `Aliases prohibited:` field of two glossary entries
   (`"specless" (also incorrect — specs are anchors)`), one Implication bullet of P12 (the last
   of twelve), and §2–§3 of a document whose §1 already appears to answer the question. P12
   mandates **routed, partial** context loading — so partial reads are guaranteed by design.
   Any qualification that survives only a full read is structurally unreachable.
3. **No propagation to the operational layer.** Neither `spec-driven` nor `spec-anchored`
   occurs anywhere in the toolkit, quickstart, foundation or context-pack layers. An adopter
   session has the negation available and the correction unavailable.
4. **The missing distinction (root cause).** P12's context architecture places `specs` *before*
   `plan`; P4 places a `spec` *inside* the slice. Both are called `spec`. Collapsing them is
   not a misreading of the corpus — it is a faithful reading of a corpus that uses one word for
   two things.

**Prior art in this corpus.** DEC-0015 closed a structurally identical failure: a canonical
statement that was correct but readable in a second, wrong way. The remedy there was
clarification of the statement, not amendment of the principle. Same remedy applies here.

## Decision

**1. Two canonical terms replace the bare noun.**

- **`substrate spec`** — the product/architecture-level specification that occupies the `specs`
  position in P12's governed substrate (`foundations → decisions → architecture → specs → plan
  → execution`). It is the artifact a **plan** derives from: it fixes intended outcome, scope
  boundary, acceptance criteria and interface contracts at product granularity. It is versioned
  and revisable; revision is captured as a decision (P8). It is **not** immutable and **not**
  the source of truth — the corpus of decisions and merged evidence remains sovereign
  (`development-model/README.md` §1 stands unchanged).
- **`slice spec-anchor`** — the per-slice scope declaration named by P4 as the slice's first
  element, materialized as the **Scope** and **Acceptance criteria** sections of
  `reference/templates/slice-template.md`. It anchors one slice against drift and, in the
  preferred acceptance-first convention, bridges scope to evidence-gate. This nominalizes the
  existing `spec-anchored` / `spec-anchoring` glossary entries; those entries are unchanged.

Bare **`spec`** remains a canonical term but is **ambiguous alone**: normative text must qualify
it as `substrate spec` or `slice spec-anchor`. Ambiguous bare use is fix-on-touch drift.

**2. Derivation rule (normative).** A plan — any slice decomposition or DAG — **derives from**
substrate specs. Every slice's `slice spec-anchor` must be traceable to the substrate spec whose
scope it decomposes. A slice whose scope cannot cite one carries **asserted** scope, not
**derived** scope, and must be declared as such in the plan. Producing a plan whose slices have
no substrate spec to derive from is an anti-pattern of P12 (context assumed rather than
authored), not an application of P8.

**3. Scope of "not spec-driven-first" (clarification, no amendment).** The characterization
rejects exactly two properties: the spec's **sovereignty** (that it is the source of truth) and
its **immutability** (that divergence is a bug). It does **not** reject the spec's existence,
its authorship ahead of the plan, or its completeness at product granularity. The prohibited
alias `specless` already encodes this; the prohibition is hereby elevated from a glossary
metadata field to a normative clause.

**4. Scope of P8 in this context (clarification, no amendment).** P8 grants a **licence to
revise** a substrate spec under capture — the decision recording *why it changed* being the
valuable artifact. P8 grants no **dispensation from authoring** one. Citing P8 to justify an
absent substrate spec inverts the principle: with no spec, there is no divergence to capture,
and P8's loop has no input.

**5. Propagation (binding on approval).** The two terms land in the glossary of the next MINOR
(v2.2.0), and `spec-anchored` gains a cross-reference to both. `reference/development-model/`
§1 gains an explicit statement of clause 3. The slice template's Scope section names the
substrate spec it derives from. `AGENTS.md` §Decision-first is corrected independently of this
record (see *Consequences*).

## Alternatives considered

- **Do nothing; fix the adopter's session prompt** — rejected. Three of the four causes are
  corpus defects present on every branch. A prompt-level fix repairs one session and leaves the
  next N sessions to rediscover the same trap. P8's own doctrine points the remedy at the
  artifact, not the instance.
- **Fix only `AGENTS.md` (cause 1), no vocabulary change** — rejected as insufficient, though it
  is necessary and lands regardless. Correcting `not a spec-first one` removes the false premise
  but leaves causes 2 and 4: `spec` still names two layers, and the negation still outranks its
  qualifications in retrieval salience. The misread reproduces without the drifted sentence.
- **Amend P4 or P8 to carry the distinction** — rejected. Anti-over-promotion discipline: this
  is Layer B vocabulary, not a thirteenth principle, and neither statement is wrong. DEC-0015
  set the precedent — clarify the reading, do not amend the statement.
- **Rename the negation to "not spec-sovereign"** — rejected for now. It would raise salience of
  the correct meaning at the source, but `spec-driven-first` is established positioning
  vocabulary with external reach (site copy, competitive framing), and retiring it costs more
  than qualifying it. Re-evaluable if the misread recurs after this record lands.
- **Terms `product spec` / `slice spec`** — rejected. `product` imports a term the framework does
  not otherwise define and reads as inapplicable to non-product corpora; `slice spec` is one
  character from bare `spec` and would not survive skim-reading. `substrate` is already
  canonical P12 vocabulary ("one governed substrate"), and `spec-anchor` is already canonical
  in adjectival form — both terms are derived from the corpus rather than imported into it.

## Consequences

**Enables**: a plan can be audited for derivation, not just for structure — "which substrate
spec does this slice decompose?" becomes an answerable, gateable question · adopters get an
unambiguous answer to "must I define the product before planning?" (yes, at substrate level) ·
the acceptance-first convention gains its missing upper half: acceptance criteria at product
granularity, not only at slice granularity.

**Constrains**: normative text may no longer use bare `spec` · plans containing slices with
asserted scope must say so explicitly · the glossary must carry both terms before the next
release is cut.

**Costs**: one MINOR version of glossary churn (v2.2.0, already in preparation) · a fix-on-touch
sweep of bare `spec` across normative text · re-issue of any adopter plan built on the
"specs are deliverables of their own slices" reading — including the 18-slice plan that
originated this record.

**Independent of this record**: the `AGENTS.md` §Decision-first correction is drift repair
against an already-canonical source (`development-model/README.md` §2, unchanged since v1.0.0).
It requires no ratification and lands with this branch. It is reported here because the drift is
this record's Context, not because approval gates it.

**Observed while gathering evidence, not decided here** (each needs its own record): the spec
repo carries three divergent lines (`main` @ DEC-0015, `release/v2.1.0` @ DEC-P-0014,
`fix/topic-taxonomy-naming-and-back-edges` @ DEC-P-0016); `DEC-0014` exists as two files with
different dates, slugs and lifecycle states across two of them; `.counters/dec.txt` reads `0015`
on `main` and `0016` on the third line. The counter was reconciled to the real corpus maximum
(`0016`) before this record claimed `0017`, per DEC-0008_5 rule 1 and P9 — the tool re-scans one
worktree and cannot see across branches, which is a gap in the mechanized pre-flight worth its
own record.

## References

- P4 (Slice Atomicity), P8 (Recursive Learning by Capture), P12 (Context Discipline) —
  [`spec/v2.1.0/principles.md`](../spec/v2.1.0/principles.md)
- `spec-anchored`, `development model`, prohibited aliases `spec-driven` / `specless` —
  [`spec/v2.1.0/glossary.md`](../spec/v2.1.0/glossary.md)
- Development model, §1 characterization and §2 style-agnosticism —
  [`reference/development-model/README.md`](../reference/development-model/README.md)
- Slice template, Scope and Acceptance criteria sections —
  [`reference/templates/slice-template.md`](../reference/templates/slice-template.md)
- DEC-0015 — precedent: clarify a correct-but-misreadable canonical statement without amending it
- DEC-0008_5 — counter discipline invoked for the `0017` claim
