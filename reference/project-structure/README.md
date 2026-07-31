# Project Structure — Layer B.1 Reference Pattern

> The **prescribed** corpus structure for SliceOps adopters: the `_sliceops/` container and its
> canonical decades. Normative source: [`naming.md`](../../spec/latest/naming.md) §7 and
> DEC-0011 (clauses _1–_8); reconciled by DEC-0021. Deliberately **distinct** from the
> lightweight *publishing* layout of this spec repo — see the note at the end.

## The container

One reserved, visible container — **`_sliceops/`** — at the root of the unit of work. Its
physical form varies; its position never does (DEC-0011_1):

| Unit of work | Form of `_sliceops` |
|---|---|
| A single repository (mono-repo product) | a **directory** `_sliceops/` at the repo root |
| A multi-repo product workspace | a **git repository named `_sliceops`**, sibling of the code repositories |
| A code repository inside a workspace | a **pointer**: minimal `sliceops.json` (`{"ref": "../_sliceops", "remote": "<url>"}`) plus the root agent-context file pointing at the container |

One product = one corpus = one set of counters. Directory and repository forms are isomorphic:
consolidating or splitting changes the form, never the semantics.

## The decades

Numbered in cognition-cycle order, semantics **reserved forever**. The scaffold is
**complete, always**: every corpus materializes all nine, whether or not it uses them
(DEC-0023, superseding DEC-0011_2's presence activation).

```
_sliceops/
  sliceops.json · _index.md · _agents.md · _policies.md (derived) · _metrics/ · _meta/
  00-context/    01-values 02-preferences 03-mental-models 04-context-packs
                 05-relations 06-capabilities 07-policies 10-custom-context
                 (08–09 reserved to the framework)
  10-insights/   20-conclusions/   30-decisions/ (flat)   40-goals/
  50-products/   the complete WHAT: definition + architecture + specs + reference
  60-execution/  61-priorities 62-plans 63-dags (derived only, P5)
                 64-fleet-agents 65-in-flight
  70-outcomes/   99-archive/ (immutable, R10)
```

Decades **80 and 90** are free adopter/vendor space and stay opt-in: they are created only
when declared in the manifest's `extensions`.

**Each decade carries a `README.md`** saying what belongs there, which prefixes it holds, and any
rule that is easy to get wrong there. That is what makes the scaffold useful: an empty folder
alone is silent, and the point is to read a corpus's gaps from its tree. **An empty decade is a
declared gap, not a defect** — no corpus is required to fill one, and the framework reports
emptiness rather than punishing it.

### Two rules that are easy to get wrong

- **`30-decisions/` is flat.** No `accepted/`, no `rfcs/`, no lifecycle subfolders — the
  lifecycle lives in the prefix (`DEC-P-` pending · `DEC-` approved · `DEC-D-` deprecated), and
  a state change renames the file and rewrites references atomically. "RFC" is a retired term: a
  proposal is a pending DecisionRecord.
- **`62-plans/` and `63-dags/` are derived only.** Per P5 the plan is computed from the slice
  dependency graph (`depends_on`) and re-rendered when sources change — never hand-patched.
  Hand-written strategy is a `DEC-` or a `GOAL-`, not a plan file.

## Where the chain lands

P12 states the context architecture as a chain: **foundations → decisions → architecture →
specs → plan → execution**. That chain is a **reading and authoring order** — nothing downstream
may be authored before what precedes it exists — and *not* a folder list (DEC-0021 clause 3).
It maps onto the decades like this:

| Chain position | Lives in |
|---|---|
| foundations | `00-context/` — `01-values`, `02-preferences`, `03-mental-models` |
| decisions | `30-decisions/` (flat) |
| architecture | `50-products/<product>/architecture/` |
| specs (substrate specs) | `50-products/<product>/specs/` |
| plan | `60-execution/62-plans/` (derived) |
| execution | `60-execution/` — `61-priorities`, `63-dags`, `64-fleet-agents`, `65-in-flight` |
| insights | `10-insights/`, promoted to `20-conclusions/` at ≥3 observations (P8) |
| outcomes | `70-outcomes/` |

**Architecture and specs are siblings inside a product** (DEC-0011_3), never top-level peers of
`decisions/`. Architecture and contracts *are* the WHAT at increasing precision — not
construction residue — so the folder narrative completes: context → insights → conclusions →
decisions → goals → **the what** → the how → outcomes.

**Zoom rule**: an organization-level corpus MAY hold the WHAT at portfolio zoom (which products
exist and why) and **point, never copy**, at each product corpus's `50-products/` (construction
zoom). Same reserved semantics, different zoom per corpus.

## Why decision-first ordering

Architecture, specs, plans and execution are **consequences** of foundations and decisions, never
the reverse. A reader or agent starts at the WHY (foundations + decisions), then the mechanics.
Leading with "one slice = one PR" inverts the dependency.

Note this is the *authoring* order. It is not the cognition cycle (DEC-0008_1), which orders
*entities* — values → insights → conclusions → strategic decision → goal → priority → tactical
decision → action → capability. Two different maps; the decade numbering satisfies both.

## Distinct from this repo's publishing layout

This spec repo deliberately uses a **different, lightweight publishing layout** (`spec/`,
`reference/`, `decisions/`, `examples/`, `governance/`) optimized for an OSS documentation site
(precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs) — recorded in DEC-0002. The
*prescribed* structure above is what adopters apply to their own corpora and products; the
*publishing* layout is how this framework documents itself. The two differ on purpose — do not
conflate them.

## Adopter note

Adopters MAY use decades 80/90 for their own space and MAY specialize what a decade contains,
but MUST preserve the reserved decade semantics, the flat `30-decisions/`, the derived-only
discipline of `62-plans/`/`63-dags/`, and the single-source property (P12). The structure is a
Layer B.1 reference pattern: adopt, then specialize.
