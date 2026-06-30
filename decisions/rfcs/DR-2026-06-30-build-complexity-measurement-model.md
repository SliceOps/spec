---
entity: DecisionRecord
status: proposed
created: 2026-06-30
updated: 2026-06-30
owner: Andrés Ramírez Sierra
sensitivity: public
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: []
topics: [evidence-categories, audit-plane, meta-framework, layer-b-framework-artifact]
vocabulary-changes:
  - "Build-Complexity Profile (new canonical term — a six-axis 0-4 product-difficulty profile, composite as an equal-weighted index /24). Chosen deliberately OFF the bare word 'complexity', which remains reserved for the Model-Triage axis #3 (a model-selection input)."
  - "Build velocity / commit-active hours (proxy) — session-clustered commit time. Distinct from 'velocity' reserved by P5 (Block-level forecast recalibration); the artifact folder is measurement/, not velocity/."
consistency-check: "Introduces a new Layer B.1 reference artifact (reference/measurement/) for ex-post build measurement — orthogonal to sizing/ (ex-ante slice sizing) and model-triage/ (session routing). Operationalizes P6 (Evidence-by-Construction) and extends P2 (Audit Plane); NOT a new principle (Layer A stays at 12 — INS-005 guard). Resolves two live P12 term collisions by naming (Build-Complexity Profile vs Model-Triage 'complexity'; measurement/ vs P5 'velocity'). related-decs left empty pending ratification, when reciprocal links to the principles/sizing/model-triage records are wired bidirectionally (RFC-PROCESS step 5). No conflicts."
---

# DR-2026-06-30 — Build-Complexity Profile + Build-Velocity Measurement Model (RFC)

> RFC (proposed). Originates in andres.co (`DEC-019` / `INS-002`, SL-009), which built
> and dogfooded the model while shipping the `/velocity` proof page and explicitly
> proposed its elevation into SliceOps. This record proposes adopting it as canon.

## Decision (proposed)

Adopt the build-velocity + Build-Complexity Profile model as a new **Layer B.1**
reference artifact at [`reference/measurement/`](../../reference/measurement/) —
documentation CC BY 4.0, the reference script MIT. It is the framework's instrument for
showing **speed against measured difficulty**, both reconstructable from git.

**Canonical (universal):** the six-axis 0–4 anchored rubric; the session-clustering
algorithm with `MAXGAP`/`FIRST` as declared calibratable defaults; the max-per-axis /
sum-of-hours aggregation rule; the Code axis specified by its **metric** (cyclomatic
complexity), naming a CCN tool as a reference, not *the* tool (P11); the honesty rules
enforced as gates; a vendor-neutral read-only script.

**Adopter-specific (out of canon):** the X-faster **baseline** — each adopter selects and
*measures* their own pre-framework system with this rubric. SliceOps ships no baseline
number.

**Not a principle.** Layer A stays at 12 (INS-005). At most a one-line pointer is added to
**P6**'s Implication list at ratification; no Statement/Rationale text is edited. A
`measurement` result is an evidence reference suitable for an **OutcomeRecord**.

## Adoption gates (evidence required before the headline ships)

1. **Re-measure the baseline.** Any X-faster ratio rests on a *measured* baseline, not an
   estimate (INS-002 §6). Until measured, ship the profile + hours; ship the ratio only
   marked "baseline estimated — pending re-measure", or not at all.
2. **Descriptive, not causal.** Frame the ratio as "commit-active hours per complexity
   point, observed (descriptive, uncontrolled)"; prefer same-lifecycle-stage comparisons;
   the non-causal disclaimer travels with the number wherever denormalized (P12).
3. **Rename + hygiene landed.** "Build-Complexity Profile" (off reserved "complexity");
   `measurement/` (off reserved "velocity"); `worked_hours` → "commit-active hours
   (proxy)" with stated bias direction; automated/merge commits excluded from clustering.

## Alternatives considered

- **Promote to a 13th principle** — rejected (INS-005 over-promotion; a build with no
  velocity number is still SliceOps; it is a capability, not constitutive).
- **Place under `sizing/`** — rejected (conflates ex-ante slice sizing with ex-post build
  measurement; different unit and time orientation).
- **Ship the Insttantt baseline as canon** — rejected (a personal datapoint baked into
  vendor-neutral canon is non-reproducible for other adopters; P11). It ships only as a
  linked adopter worked example.
- **Single T1–T3 tier / LOC-as-complexity / 0–10 scale / composite-as-measurement** —
  rejected upstream in `DEC-019` (unanchored, volume-not-difficulty, false precision,
  index-not-measurement).

## Consequences

- **Enables**: a reproducible, defensible "complex *and* fast" claim — P6 made an
  instrument, P2 extended to the velocity claim, the strongest answer to the
  "marking your own homework" objection (reproducible-from-git).
- **Constrains**: every venture measured with the same rubric/params; the baseline must be
  measured per adopter; new ratio claims carry the non-causal disclaimer.
- **Costs**: re-measuring the baseline; manual Code-axis read where the CCN tool
  undercounts (JSX/TSX/Dart).

## Reconciliation with the prospective decision-dimensions contribution

A separate, not-yet-merged contribution adds a **prospective** decision-analysis scheme
(universal decision dimensions + materiality, used to *decide* before building). This model
is its **retrospective** complement (*measure* the result). They are bookends of one slice
lifecycle: **decide → build → measure**. When both land, anchor them to **one shared
dimension catalog** via a single reconciling DEC so the second does not fork the
vocabulary (~5 of 6 axes share dimension names at different scales). Two axes —
**Intelligence** and **Integrations** — have no prospective home and should be added to the
shared catalog deliberately. This RFC is **not blocked** on that contribution (it is not in
canon today).

## On ratification

Assign this slice its `SL-NN` from the SliceOps development slice ledger; wire
`related-decs` bidirectionally to the referenced principle/sizing/model-triage records;
add the one-line P6 pointer; and mark andres.co `DEC-019` / `INS-002` **superseded-by**
this record (supersession explicit, never silent — P1/P2).

## References

- andres.co `DEC-019` (build-velocity + complexity measure) and `INS-002` (the full model
  + the measurement prompt) — the origin and dogfooded prior art.
- [`../../reference/measurement/`](../../reference/measurement/) — the proposed artifact.
- Orthogonal siblings: [`../../reference/sizing/`](../../reference/sizing/),
  [`../../reference/model-triage/`](../../reference/model-triage/).
