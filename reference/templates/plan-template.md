<!--
Plan template (Layer B.1) — the twelfth canonical template, mandated by DEC-0020 clause 2.
Lives at 60-execution/62-plans/ (DEC-0011_4). DERIVED, never hand-patched: the plan is
rendered from the slice source (depends_on) and re-rendered when that source changes (P5).
The DAG at 63-dags/ is derived from the same source, never authored alongside.
Flow and gate: ../workflows/planning.md. Replace all <…>.
-->

# Plan: <product or capability> — <short title>

**Derived from**: <the slice source file this plan renders from>  ·  **Rendered**: <YYYY-MM-DD>
·  **Spec pin**: <spec version>

> Do not hand-edit this file. Change the source and re-render (P5). A plan edited in place has
> stopped being a derived view and become an unauditable commitment.

## Definition of ready

Every box must hold before any slice in this plan executes. This is the **plan gate** — the
pre-execution counterpart of P6's evidence gate. Unchecked boxes block execution, not revision.

- [ ] **Derivation** — every slice cites the `substrate spec` it decomposes (DEC-0017 clause 2).
      A slice that cannot carries **asserted** scope, not derived scope, and is listed under
      *Asserted scope* below rather than quietly included.
- [ ] **Field completeness** — every slice carries every field of
      [`slice-template.md`](slice-template.md): coordinate, token-band, context-band,
      sensitivity, execution mode, depends-on, derives-from, scope, acceptance criteria,
      evidence plan, decisions produced, HITL, P9, P10. Absent is a defect; explicit "N/A —
      <reason>" is a declaration.
- [ ] **Coordinates** — blocks and sections assigned under `naming.md` §5
      (`SLC[n][a]SEC[n|A]BL[n]`). The dotted form is retired.
- [ ] **Dependencies derivable** — `depends_on` is complete enough that the DAG computes. If the
      DAG needs a manual edge, the declaration is wrong.
- [ ] **Blocked work visible** — externally blocked slices appear **marked blocked**, never
      omitted. A block stops what depends on it, not its wave.
- [ ] **Sensitivity routed** — any slice touching real data declares sensitivity and the
      resulting execution locality (P7 + model triage). Compliance by construction.
- [ ] **No silent truncation** — if coverage is bounded (top-N, sampling, deferred areas), say
      what was left out and why.

**Gate status**: <READY | BLOCKED — list the failing conditions>

## Substrate spec coverage

Every spec this plan decomposes, and its state. A plan may not decompose a spec that does not
exist (see `../workflows/planning.md` stage 1).

| Substrate spec | Version | Slices derived from it |
|---|---|---|
| `<spec-slug>` | `<v0.1.0>` | `<SLC…>`, `<SLC…>` |

## Blocks and sections

| Block | Section | Covers |
|---|---|---|
| `BL01` | `SEC01` | <one architectural concern> |

## Slices

One row per slice. The full declaration lives in each slice's own document; this is the index.

| Coordinate | Slice | Tok | Ctx | Sens. | Exec | Derives from | Depends on | HITL | State |
|---|---|---|---|---|---|---|---|---|---|
| `SLC0001SEC01BL01` | <title> | `<M>` | `<M>` | `<internal>` | `<plan>` | `<spec-slug>` | — | `<owner>` | ready |

**Legend** — Tok/Ctx: token-band and context-band, orthogonal (`../sizing/`). Sens.: sensitivity,
which drives execution locality (`../model-triage/`). State: `ready` · `blocked` · `in-flight` ·
`merged`.

## Asserted scope

Slices whose scope is **not** derived from a substrate spec. Empty is the healthy state; a
non-empty list is a declared risk, not a hidden one.

| Coordinate | Why no spec | What would close it |
|---|---|---|

## Blocked

| Coordinate | Blocked by | External? | Unblocks when |
|---|---|---|---|

## Waves (derived — do not author)

A wave is the DAG's answer to "what is executable now", recomputed as dependencies clear. It is
**not** a sprint, carries no commitment, and is never assigned by hand (P5).

| Wave | In parallel | Slices |
|---|---|---|
| 1 | <n> | `<SLC…>` |

## Health signals

- **Sub-slice rate**: <n>/<total> coordinates carry a sub-slice suffix. At planning time **0 is
  correct** — the suffix records what execution discovers, not what the plan foresees
  (DEC-0014_4). A rate that climbs, especially into plannable work rather than tooling and
  cleanup, means slices are cut too coarse.
- **Asserted-scope rate**: <n>/<total>. Should trend to zero as specs land.

## Re-render

```
<the command that regenerates this file and the DAG from source>
```

Changing a dependency in the source and re-running must reproduce this plan and
`63-dags/` exactly. Determinism is the property that makes a derived plan auditable
(Determinism-over-Regeneration, Layer B.2).
