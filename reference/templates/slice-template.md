<!--
Slice template (Layer B.1) — one chat = one PR = one atomic vertical slice (P4).
Use as the PR description / slice scope declaration. Replace all <…>.
-->

# Slice: <SLC0001SEC01BL01> — <short title>

**Token band**: <XS | S | M | L | XL>  ·  **Context band**: <XS | S | M | L | XL>  ·  **Sensitivity**: <public | internal | restricted | sensitive>  ·  **Execution mode**: <account-with-plan | local-via-API | …>  ·  **Depends on**: [<slice id>...]  ·  **Derives from**: <substrate spec>

<!--
Every field above is declared, not inferred. Where each is defined:

- **Coordinate** `SLC[n][a]SEC[n|A]BL[n]` — slice ∈ section ∈ block, letters as separators.
  Normative grammar: `../../spec/latest/naming.md` §5. The dotted `BL-XX.SEC-XX.SL-XXX` form
  is RETIRED (DEC-0014). The optional one-letter sub-slice suffix records a leaf that emerged
  during execution — never planned upfront (P5).
- **Bands** — `../sizing/`. Token-band measures throughput (billed-equivalent); context-band
  measures peak context footprint. They are ORTHOGONAL: context-band is the primary filter,
  because a window smaller than the slice's footprint cannot run it at any price (P4).
- **Sensitivity and execution mode** — `../model-triage/`. Axis 2 is sensitivity → locality:
  a slice handling real PII during execution runs local, never against an external API,
  regardless of cost or speed. That is compliance by construction (P7), not an optimization.
- **Derives from** — the substrate spec this slice decomposes (DEC-0017 clause 2). A slice
  that cannot cite one carries ASSERTED scope, not derived scope, and must say so here.
-->


## Scope (declared upfront — P4)

<One paragraph: the single end-to-end outcome this slice delivers. One architectural concern. If it spans more, split.>

**In scope**: <bullets>
**Out of scope**: <bullets — deferred to which future slice>

## Acceptance criteria (executable preferred — preferred convention)

<Declared upfront. Each criterion is testable. Together they define what makes this slice "done".

Executable form (preferred): an acceptance test (or small test suite) that codifies the criteria. The test pass IS the evidence-gate that closes the slice (P6). One artifact bridges scope (start) ↔ evidence (end).

Prose form (override permitted): a numbered list of testable statements. Maps to evidence in the Evidence plan below.>

- [ ] AC-1 — <criterion>
- [ ] AC-2 — <criterion>
- [ ] AC-3 — <criterion>

## Decisions produced (P2/P1)

- DEC-NNNN-YYYYMMDD-<slug> — <one line> (or "none")

## Evidence plan (P6/P7)

- [ ] Functional: <tests>
- [ ] Quality: <lint/format/coverage threshold>
- [ ] Security: <SAST / secrets scan / dependency check> (P7)
- [ ] Decision: DEC(s) and InsightRecord(s) above
- [ ] Provenance: slice id in branch, commits, PR title

## Infrastructure (P10, if touched)

- [ ] IaC/DB/env changes are in this slice with rollback plan — or N/A

## Shared-resource pre-flight (P9, if scaling parallelism)

- [ ] Finite/serialized resources enumerated, cap and alert verified — or N/A

## HITL (P3)

- [ ] Human approval gate identified (merge owner)

## Anti-pattern self-check

- [ ] Not a catch-all PR · single concern · scope ≤ ~2× forecast · evidence not deferred
