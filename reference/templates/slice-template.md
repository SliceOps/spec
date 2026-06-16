<!--
Slice template (Layer B.1) — one chat = one PR = one atomic vertical slice (P1).
Use as the PR description / slice scope declaration. Replace all <…>.
-->

# Slice: <BL-XX.SEC-XX.SL-XXX> — <short title>

**Token band**: <XS | S | M | L | XL>  ·  **Depends on**: [<slice id>...]  ·  **Block**: <BL-XX>

## Scope (declared upfront — P1)

<One paragraph: the single end-to-end outcome this slice delivers. One architectural concern. If it spans more, split.>

**In scope**: <bullets>
**Out of scope**: <bullets — deferred to which future slice>

## Acceptance criteria (executable preferred — preferred convention)

<Declared upfront. Each criterion is testable. Together they define what makes this slice "done".

Executable form (preferred): an acceptance test (or small test suite) that codifies the criteria. The test pass IS the evidence-gate that closes the slice (P5). One artifact bridges scope (start) ↔ evidence (end).

Prose form (override permitted): a numbered list of testable statements. Maps to evidence in the Evidence plan below.>

- [ ] AC-1 — <criterion>
- [ ] AC-2 — <criterion>
- [ ] AC-3 — <criterion>

## Decisions produced (P2/P4)

- DR-YYYY-MM-DD-<slug> — <one line> (or "none")

## Evidence plan (P5/P6)

- [ ] Functional: <tests>
- [ ] Quality: <lint/format/coverage threshold>
- [ ] Security: <SAST / secrets scan / dependency check> (P6)
- [ ] Decision: DEC(s) and InsightRecord(s) above
- [ ] Provenance: slice id in branch, commits, PR title

## Infrastructure (P11, if touched)

- [ ] IaC/DB/env changes are in this slice with rollback plan — or N/A

## Shared-resource pre-flight (P12, if scaling parallelism)

- [ ] Finite/serialized resources enumerated, cap and alert verified — or N/A

## HITL (P9)

- [ ] Human approval gate identified (merge owner)

## Anti-pattern self-check

- [ ] Not a catch-all PR · single concern · scope ≤ ~2× forecast · evidence not deferred
