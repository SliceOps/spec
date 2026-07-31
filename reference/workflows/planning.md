# Planning Workflow — substrate specs → plan → slices → DAG (Layer B.1)

> The canonical flow from intent to an executable plan, and the **plan gate** that closes it.
> Mandated by DEC-0020 clause 1. Companion artifacts: [`../templates/plan-template.md`](../templates/plan-template.md)
> and [`../templates/slice-template.md`](../templates/slice-template.md).

SliceOps gates the **slice** at merge (P6, Evidence-by-Construction). This workflow is the
other gate — the one **before** execution. Its rule is the same in spirit: a stage may not
begin until the stage before it exists.

```
foundations + decisions  →  substrate specs  →  PLAN  →  slices  →  DAG (derived)
                                              ▲                      │
                                              └──── plan gate ────────┘
```

---

## Stage 1 — Substrate specs

**Produces**: one `substrate spec` per capability being built, in
`50-products/<product>/specs/` (DEC-0017; location per DEC-0011_3).

A substrate spec fixes, at product granularity: intended outcome, scope boundary, acceptance
criteria, and interface contracts with adjacent capabilities. It is versioned (`v0.3.0`), never
numbered — identity is by version, not by counter (DEC-0017).

**Entry condition**: the decisions the spec implements exist. Architecture, specs and plans are
consequences of foundations and decisions, never the reverse (P12).

**Exit condition**: every capability the plan will decompose has a spec. **Not every spec the
product will ever need** — only those the plan is about to cut into slices. Specs for later
waves are legitimate future work; what is illegitimate is planning a wave whose specs do not
exist.

> **The failure this stage prevents.** An agent produced an 18-slice plan from 4 of 9 substrate
> specs, citing P8 ("you learn by executing") as authority. P8 licenses **revising** a spec under
> capture; it never licenses **not authoring** one. With no spec there is no divergence to
> capture, and P8's loop has no input.

## Stage 2 — The plan

**Produces**: one plan in `60-execution/62-plans/` (DEC-0011_4), from the
[plan template](../templates/plan-template.md).

The plan decomposes substrate specs into slices and declares dependencies. It states
**structure**, deliberately coarser than reality — detail that changes no decision is waste
(P5).

**Entry condition**: stage 1's exit condition holds.

**Exit condition**: the **plan gate** below passes.

### Altitude is not completeness

P5 governs a plan's **altitude**: the plan commits to structure and execution discovers the
leaves; a sub-slice is the notation for a leaf that emerged late. P5 does **not** govern
**completeness**: a slice that is declared is declared in full.

|  | Complete | Partial |
|---|---|---|
| **Coarse** | ✅ the intended state | ❌ defect |
| **Fine** | acceptable, often waste | ❌ defect |

Coarse-but-complete is correct. Both partial cells are defects, and neither is licensed by P5
(DEC-0020 clause 5).

## Stage 3 — Slices

**Produces**: one [slice declaration](../templates/slice-template.md) per unit of work, each
carrying its full field set — coordinate, bands, sensitivity, execution mode, dependencies,
**derives-from**, scope, acceptance criteria, evidence plan, HITL, P9/P10.

**Entry condition**: the plan passed the gate.

**Exit condition**: each slice cites the substrate spec it decomposes. A slice that cannot
carries **asserted** scope, not **derived** scope, and the plan says so explicitly (DEC-0017
clause 2).

## Stage 4 — The DAG

**Produces**: `60-execution/63-dags/`, **derived only** (P5, DEC-0011_4).

The DAG is computed from the slices' `depends_on` and re-rendered when the source changes. It
is never hand-authored and never hand-patched. A stage is "what is mergeable now given
dependencies" — a computed view, not a commitment.

**Exit condition**: the DAG regenerates from source without manual edits. If it does not, the
dependencies are wrong, not the renderer.

---

## The plan gate

A plan is **ready** when every condition holds. This is the enumerated form of the definition of
ready in the plan template; the completeness validator (DEC-0020 clause 4) checks it
mechanically.

- [ ] **Derivation** — every slice cites the substrate spec it decomposes, or is explicitly
      marked as carrying asserted scope.
- [ ] **Field completeness** — every slice carries every field the slice template declares.
      Absent is a defect; "N/A" with a reason is a declaration.
- [ ] **Coordinates** — blocks and sections assigned under `naming.md` §5. No dotted form.
- [ ] **Dependencies** — declared such that the DAG is *derivable*, not authored.
- [ ] **Blocked work is visible** — externally blocked slices appear in the plan **marked as
      blocked**, never omitted. A blocked slice does not stop its wave; only what depends on it.
- [ ] **Sensitivity routed** — any slice touching real data declares its sensitivity and
      resulting execution locality (P7, model triage). This is compliance by construction, not
      an optimization.
- [ ] **No silent truncation** — if the plan bounds coverage, it says what was left out.

**A failed gate blocks execution of the plan's slices, not the plan's revision.** Fix the plan
and re-run; the gate is a checkpoint, not a punishment.

## What this workflow is not

- **Not spec-driven-first.** The spec anchors; it is not sovereign, and it is not immutable.
  When it and reality diverge, that is a recorded decision, not a bug (development model §1).
- **Not a waterfall.** The stages gate *authoring dependency*, not calendar phases. Wave 2's
  specs may be written while wave 1 executes; what may not happen is planning wave 2 without
  them.
- **Not a commitment device.** A stage is derived (P5). "We committed to N slices this stage"
  is the anti-pattern.
