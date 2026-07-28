---
entity: DecisionRecord
status: approved
kind: constitutive
created: 2026-07-13
updated: 2026-07-13
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
originating_slice: null   # back-fill: layout-design conversation, 2026-07-12/13
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0009-20260712-handoffs-as-a-contextpack-kind, DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure, DEC-0012-20260713-catalog-amendments-mental-model-and-policy]
topics: [folder-structure, corpus-integrity, context-discipline, naming, adopter]
vocabulary-changes: ["_sliceops (container)", "unit of work", "canonical decade / free decade", "presence activation", "sliceops.json (adoption manifest)", "_agents.md", "_policies.md", "_metrics/", "_meta/", "fleet agents"]
consistency-check: |
  DEC-0008 fixed WHAT artifacts are called (one concept = one name = one grammar); this
  record fixes WHERE they live — the same drift disease at the folder level, evidenced by
  sibling engineering corpora sharing concepts under different numbers. Storage follows
  the cognition cycle of DEC-0008_1; the cycle remains SCHEMA and this record is STORAGE
  (folder placement never alters entity semantics or edges). Extends the reserved-name
  list of DEC-0010_5 with the underscore family. Clause .4 operationalizes P5 (plans and
  dependency graphs as derived artifacts only). Clause .5 houses the id counters as P9
  telemetry. Clause .7 preserves P11 (the file corpus as the portable canonical
  serialization) and P12 (points-never-copies routing). Vendor runtime applications of
  this layout are Layer C and live in vendor corpora, not in this spec. Relies on
  DEC-0012 for the MentalModel folder name and the Policy records behind `_policies.md`.
  No conflicts.
---

# DEC-0011 — The Canonical Corpus Container and Layout (`_sliceops/`)

> A SliceOps DecisionRecord about SliceOps itself. Designed and ratified iteratively with
> the owner across working drafts (2026-07-12/13); approved 2026-07-13 (born `DEC-P-0011`,
> renamed on approval — the prefix carries the state). Clause identifiers per DEC-0008_9.

## Summary

One reserved, visible container — **`_sliceops/`** — at the root of every unit of work
marks that the unit runs the framework, the way `.git` marks a git repository but
**visible**: underscore, not dot, so it sorts first and adoption can be seen. Inside,
folders are numbered in **cognition-cycle order**, so a plain directory listing teaches
the framework. Storage speaks one vocabulary; products project their own surfaces over
it. The record defines: the unit-of-work rule (directory / repository / pointer), the
canonical decades with presence activation, the complete WHAT under `50-products/`, the
`60-execution/` internals, the reserved underscore family, the adoption manifest, and
the relation between runtimes, surfaces and the file serialization.

## Context

The naming homologation (DEC-0008) cured one-concept-many-names for artifacts. Folder
layouts still carried the same disease: sibling engineering corpora shared a numbered
profile yet drifted — one corpus renumbered the same concepts differently; insights were
stored at the end of the listing; goals and priorities had no folder at all; three
folders mixed entities of different natures. Meanwhile adoption needs a detection
convention: something a tool or a person can find at any project root and know "this
runs SliceOps". This record was designed against the real corpora and ratified clause by
clause with the owner; the temporary working drafts are superseded by this record.

## Decision (clauses)

### DEC-0011_1 — The container and the unit-of-work rule

`_sliceops` is ALWAYS the container at the root of the unit of work; only its physical
form varies with the unit:

| Unit of work | Form of `_sliceops` |
|---|---|
| A single repository (a mono-repo product) | a **directory** `_sliceops/` at the repo root |
| A multi-repo product workspace | a **git repository named `_sliceops`**, sibling of the code repositories — it replaces the former "-engineering" repository |
| A code repository inside a workspace | a **pointer**: minimal `sliceops.json` (`{"ref": "../_sliceops", "remote": "<url>"}`) plus the root agent-context file pointing at the container |

Detection is identical in all three cases. **One product = one corpus** (one set of
counters); code repositories never carry a container of their own. The **local** name is
what detects; the remote repository name is free (a host organization admits one
repository per name — the remote may be `<product>-sliceops`, cloned locally as
`_sliceops`). Directory and repository forms are isomorphic: consolidating or splitting
repos moves the container unchanged.

### DEC-0011_2 — Canonical decades, presence-activated

```
_sliceops/
  sliceops.json          adoption manifest (clause .6)
  _index.md              locates (DEC-0010)
  _agents.md             behaves — corpus behavior contract (clause .5)
  _policies.md           regulates — DERIVED from 07-policies (DEC-0012_3)
  _metrics/              measures (clause .5)
  _meta/                 maintains (clause .5)
  00-context/
    01-values/           VAL-
    02-preferences/      PREF-
    03-mental-models/    MM-   (DEC-0012_1)
    04-context-packs/    CP-   (pack | brief | handoff — DEC-0009)
    05-relations/        REL-
    06-capabilities/     CAP-  (accrues in Act, consumed as context)
    07-policies/         POL-  (DEC-0012_2)
    10-custom-context/   the adopter's free context space beyond the framework
  10-insights/           INS-
  20-conclusions/        CONC-
  30-decisions/          DEC- / DEC-P- / DEC-D-   (flat; the prefix carries state)
  40-goals/              GOAL-
  50-products/           the complete WHAT (clause .3)
  60-execution/          the HOW (clause .4)
  70-outcomes/           OUTC-
  99-archive/            immutable (R10); resolved via alias maps in _meta/
```

Rules: the canonical decades are **00, 10, 20, 30, 40, 50, 60, 70, 99** and their
semantics are reserved forever — a decade present can only mean what this record says.
Decades **80 and 90 are free** adopter/vendor space, declared in the manifest. Inside
`00-context/`, slots 01–07 are canonical, **08–09 remain reserved to the framework**,
and the adopter's space is always 10. **Presence activates**: a corpus materializes only
the decades its work needs; the validator validates what exists. Numbers are stable
identifiers; the listing order is the cycle's teaching order.

### DEC-0011_3 — `50-products/` holds the COMPLETE what

Per product, `50-products/<product>/` contains `definition/` (product definition,
manifesto), `architecture/`, `specs/` (versioned contracts), and `reference/`.
Architecture and contracts ARE the what at increasing precision — not construction
residue — so the folder narrative completes: context → insights → conclusions →
decisions → goals → **the what** → the how → outcomes. Zoom rule: an
organization-level corpus MAY hold the what at portfolio zoom (which products exist and
why) and **point, never copy**, at each product corpus's `50-products/` (construction
zoom). Same reserved semantics, different zoom per corpus.

### DEC-0011_4 — `60-execution/` internals

`61-priorities/` (PRI-) · `62-plans/` and `63-dags/` hold **derived artifacts only** —
per P5 the plan is computed from the slice dependency graph (`depends_on` metadata made
explicit) and re-rendered when sources change, never hand-patched; hand-written strategy
is a `DEC-` or a `GOAL-` · `64-fleet-agents/` — one file per executing agent
(description + full configuration); the FLEET, distinct from `_agents.md` (the corpus
behavior contract) · `65-in-flight/` — live sessions, slice ledgers, `SLC` coordinates.

Boundary: the framework reserves the **folders and the derived-only discipline** — that
you prioritize, that plans are computed from the dependency graph, that slices follow the
slice rules (all already public in P5 and DEC-0008_6). The **machinery** that produces
and runs them — planning pipelines, the format of fleet-agent definitions, orchestration —
is vendor Layer C: contents beyond the canonical frontmatter are adopter/vendor-defined
and specified in their own corpora.

### DEC-0011_5 — The reserved underscore family

Extends the reserved infrastructure names of DEC-0010_5. Each carries one verb:

| Reserved | Verb | Contents |
|---|---|---|
| `_index.md` | locates | the corpus map (DEC-0010) |
| `_agents.md` | behaves | the behavior contract for any agent working the corpus; the root `CLAUDE.md`/`AGENTS.md` remain as thin pointers (harnesses look at the root) |
| `_policies.md` | regulates | DERIVED summary of the active Policy records (DEC-0012_3) |
| `_metrics/` | measures | id `counters/` (P9 telemetry of a finite shared resource), the cost ledger across its dimensions, the metrics manifest, sizing-band calibration, measurement results |
| `_meta/` | maintains | dated migration operations, alias maps (the archive resolves old names against them), one-off maintenance mandates |

Numbers are cognition; underscores are infrastructure. Nothing normative lives in
`_meta/` — norms live in decisions and the spec; `_meta/` is the corpus's works log.

### DEC-0011_6 — The adoption manifest `sliceops.json`

Container form:

```json
{
  "spec": "<spec version>",
  "corpus": "engineering | organization",
  "vendor": "<vendor id or none>",
  "extensions": { "<free slot or layer>": "<claimant>" }
}
```

Pointer form (code repositories): `{"ref": "<local path>", "remote": "<url>"}`.

Vendors MAY define additional corpus types for their own runtime products (Layer C —
declared here, specified in their own corpora). Three functions: **detection** (any tool
knows the project runs SliceOps), **version pin** (validators validate against the
declared spec), **extension declaration** (which free slots and vendor layers exist — a
verifiable conformance claim). Written by scaffolding and migrations; read by validators
and runtimes; never a hand-maintained document surface.

### DEC-0011_7 — Surfaces, runtimes and the file serialization

On disk there is ONE vocabulary — this record's. Products name their **surfaces**
freely: a console-type product may render its own sections over the corpus; any Layer C
runtime maps the folders to whatever its users see. Runtime storage may be a database:
the file corpus is the **canonical interchange serialization**, and the universal
grammar (DEC-0008_5) makes filename ↔ primary-key conversion bijective — a compliant
runtime must always be able to materialize the file corpus, round-trip, without loss
(exports, agent workspaces, sync, integrations). `00-context/10-custom-context/` MAY
route (points-never-copies, DEC-0010) to an external, vendor-defined data layer; such
layers are entirely the vendor's intellectual property — the framework reserves only the
route.

### DEC-0011_8 — Application

The former engineering profile (`00-foundation` … `80-operations`, including its
renumbered variants) is **retired**. Existing corpora migrate at their next homologation
stage: entities to their cycle folders; the technical corpus into `50-products/`; the
three mixed folders (foundation, reference, operations) split by entity nature —
patterns to conclusions, runbooks and standards to capabilities, operating rules to
policies, insights and retrospectives to their decades; archives untouched (R10) with
alias maps in `_meta/`. This record folds into spec v2.0.0 (never published — no
compatibility debt). Templates for the container ship with the spec; the naming
validator gains container checks (manifest present and coherent, reserved decade
semantics, index routes resolve).

## Alternatives considered

- **A — Keep per-repo numbered profiles**: rejected — proven drift; sibling corpora held
  the same concepts under different numbers, and the cycle's early stages had no home.
- **B — Hidden dotfile `.sliceops`**: rejected — invisible by default kills
  adoption-by-seeing; the underscore is visible, sorts first, and is already the
  infrastructure convention.
- **C — Technical docs (architecture/specs/reference) as container siblings**: rejected
  by the owner — they are the WHAT itself; leaving them outside splits the product's
  truth across the container boundary. Recorded correction.
- **D — A container per code repository**: rejected — fragments counters and decisions;
  one product = one corpus, code repos point home.

## Consequences

**Enables**: detection and scaffolding across adopting projects; a directory listing that teaches
the cycle; a single migration path (directory ↔ repository isomorphism); Layer C
runtimes interoperate through the shared serialization. **Constrains**: every corpus
migrates once, staged per homologation plan; validators, scaffolds and runtime parsers
update their paths. **Costs**: multi-repo continuous integration needs a container
checkout step (the pointer's `remote` field feeds it); host-organization repo naming
needs the local-name convention; changes spanning cognition and code remain two
commits — traced by slice evidence (commit hash + coordinate), the standard multi-repo
cost, not introduced here.

## Ratification note

Designed and ratified iteratively with the owner (2026-07-12/13) across seven working
drafts, with the owner's corrections preserved where they re-founded the design — most
notably the complete-WHAT rule of clause .3, rejecting the technical-siblings draft
(Alternative C). The drafts are superseded by this record; the audit plane keeps its
graveyard (DEC-0008_7). **Approved by the owner on 2026-07-13** after two boundary
adjustments requested in review: the clause .4 machinery boundary (framework keeps the
folders and the derived-only discipline; the producing machinery is vendor Layer C) and
the removal of runtime-domain content from this record entirely.

## References

- [`DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — the cycle (schema this storage follows), universal grammar and exemptions, conventions, clause rule.
- [`DEC-0009-20260712-handoffs-as-a-contextpack-kind.md`](DEC-0009-20260712-handoffs-as-a-contextpack-kind.md) — ContextPack kinds.
- [`DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md`](DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md) — the index; reserved-name class extended by clause .5.
- [`DEC-0012-20260713-catalog-amendments-mental-model-and-policy.md`](DEC-0012-20260713-catalog-amendments-mental-model-and-policy.md) — MentalModel and Policy, which clauses .2 and .5 rely on.
- `spec/v2.0.0/principles.md` — P5 (clause .4), P9 (clause .5), P11/P12 (clause .7).
