# Changelog

All notable changes to the SliceOps™ framework specification are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) per the Versioning policy in [`spec/v1.1.0/README.md`](spec/v1.1.0/README.md).

## [Unreleased]

### Pending ratification — spec v2.2.0 ([`DEC-0016`](decisions/DEC-0016-20260728-topic-taxonomy-naming-and-off-taxonomy-cleanup.md))

Prepared, **not ratified**: the material below is staged so that approval is a rename and a status flip, not a second authoring pass. It moves to a released `## [2.2.0]` section on ratification, or is reverted with the record on rejection.

- **Canonical topic `naming`** (clause DEC-0016_1) under `meta-framework`, covering the identifier standard of `naming.md` — universal grammar, entity prefixes, slice coordinate, clause identifiers, reserved names, alias tables. Closes a gap the v2 re-founding left: `topics.md` is byte-identical from v1.1.0 through v2.1.0 and therefore predates `DEC-0008`, which created the universal grammar — leaving the identifier standard as the only canonical spec document with no topic, while `meta-framework` named "naming" in its own scope without carrying an entry for it. Four approved constitutive records (`DEC-0011`, `DEC-0012`, `DEC-0013`, `DEC-0014`) had independently tagged themselves `naming`; they become conformant with no edit. Backwards-compatible minor — no `topics:` value valid under v2.1.0 becomes invalid. `spec/v2.2.0/` cut with `topics.md` as its only changed document; `spec/v2.1.0/` and earlier retained frozen; `spec/latest` → `v2.2.0`, with the `spec/README.md` version index and the root `_index.md` routes updated.

### Pending ratification — corpus reconciliation ([`DEC-P-0018`](decisions/DEC-P-0018-20260730-duplicate-decision-number-reconciliation.md), [`DEC-P-0019`](decisions/DEC-P-0019-20260730-counter-tooling-branch-and-worktree-blindness.md))

Prepared, **not ratified**. No spec version is cut: no published document changes, and no corpus artifact's conformance moves.

- **One number, one artifact — the forked `DEC-0014` reconciled** (clause DEC-0018_1). Counter value 0014 addressed two different DecisionRecords on two branches: `DEC-0014-20260715-…` (approved, `main`) and `DEC-P-0014-20260728-…` (pending, `release/v2.1.0`), violating DEC-0008_5 rule 3. They are not two decisions — they are two independent authorings of **one** decision, stating the same four clauses with the same normative content. The 2026-07-15 record is canonical (first claim; merged history, two published spec versions and three later decisions cite it; it is ratified). The 2026-07-28 record is **withdrawn, not renumbered** — a second number for one decision would break DEC-0008_5 rule 5's guarantee that a short citation is unambiguous within a corpus.
- **Withdrawal absorbs, never discards** (clause DEC-0018_2) — the withdrawn draft's unique material is grafted into the canonical record before it stops being a live artifact. `DEC-0014` gains its real provenance (a Layer C.1 implementation handoff of 2026-07-15, DEC-0009 `kind: handoff`) and a corrected evidence figure — **75 of 229 distinct coordinates, 33%**, replacing the handoff's ~40% (91/230), which double-counted the 15 coordinates hitting both gaps and included one malformed identifier (P6). Non-normative material only: no clause text changed. The draft's one normative addition — a revisit condition on the sub-slicing-rate threshold — is deliberately **not** grafted and is recorded in DEC-0018_2 for separate raising. General rule fixed: one decision on two numbers → withdraw; two decisions on one number → renumber the later claim.
- **`main` named the integration line; `release/v2.1.0` retired by salvage** (clause DEC-0018_3). Both `fix/` branches are already merged — `fix/spec-level-vocabulary-and-agents-drift` has a zero-byte content diff, `fix/topic-taxonomy-naming-and-back-edges` is strictly behind. `release/v2.1.0` is **not** merged: its content is a second preparation of a version already published from `main`, and merging it would regress `spec/latest` from v2.2.0 to v2.1.0, delete `spec/v2.2.0/` and reinstate the withdrawn draft. Reconciled by an itemized salvage table instead.
- **The claimed-id set spans refs; the corpus boundary stops at nested checkouts** ([`DEC-P-0019`](decisions/DEC-P-0019-20260730-counter-tooling-branch-and-worktree-blindness.md), clauses DEC-0019_1 and DEC-0019_2) — the two tools enforcing counter discipline both mistake one working tree for the corpus, failing in opposite directions. `claim_id.py` **under-reports**: `scan_real_max()` is an `os.walk()` that cannot see a branch, and `.counters/dec.txt` forks with the branch, so both inputs go stale together — which is how 0014 was issued thirteen days after it was spent. `validators.py`'s counter-atomicity check **over-reports**: it descends into `.claude/worktrees/`, finding every record twice. Claims and validation walks now read git refs, with an announced filesystem fallback where git is unavailable; the nested-checkout boundary moves to module level so every walk shares it.
- **CI/local gate parity** (clause DEC-0019_3) — a check that returns different verdicts in continuous integration and locally on the same corpus state is a defect in the check. This one did: all nine checks pass on CI's clean tree while the same command in a maintainer's worktree reports **17 collisions, all false and none real** (15 when first diagnosed — the count tracks corpus size, so it only grows). The published gate stayed green for the thirteen days the corpus carried a duplicate number, and the one true collision was cross-branch and therefore invisible to a filesystem walk at any exclusion setting.

### Fixed

- **Pre-write hook re-vendored from the toolkit** (clause DEC-0018_3, salvaged from `release/v2.1.0`) — `.claude/hooks/naming_validator.py` had drifted **155 lines** from the toolkit upstream it is a copy of, and still cited clause identifiers in the dotted form (`DEC-0008.5`) that [`DEC-0013`](decisions/DEC-0013-20260713-clause-identifier-separator-underscore.md) retired in favour of the underscore — a pre-write gate emitting the notation the corpus forbids. Now upstream plus an 8-line column-0 guard (only top-level YAML keys are read as catalog signals, so a vendor's indented `*-entity-mapping:` block is not mistaken for one). That guard is owed back to `sliceops-toolkit` as a declared follow-up: a vendored fix that never travels home is the same drift, one level up.
- **Bidirectional cross-references restored** — nine `related-decs` edges were declared one-way, failing the repository's own `[cross-references-bidirectional]` gate: `DEC-0008` had no back-edge from `DEC-0011`/`DEC-0012`/`DEC-0013`/`DEC-0014`/`DEC-0015`, `DEC-0009` and `DEC-0010` none from `DEC-0011`, `DEC-0013` none from `DEC-0014`, `DEC-0014` none from `DEC-0015`. `related-decs` is symmetric, and `governance/PROPOSAL-PROCESS.md` step 3 makes reciprocation a Layer 2 pre-merge requirement. Edge addition only — no decision content changed.
- **Three off-taxonomy topic values corrected** (recorded as clause DEC-0016_2) — mislabels of concepts the taxonomy already carried, resolved to their canonical entries per P12 fix-on-touch rather than by growing the taxonomy: `DEC-0011` `adoption` → `adopter`; `DEC-0012` `glossary` → `vocabulary-discipline`; `DEC-0012` `enforcement` → `r-rules`.
- **CI topic-taxonomy pin unstuck** (clause DEC-0016_3) — `.github/workflows/ci.yml` pinned `spec/v2.0.0/topics.md` through the v2.0.1 and v2.1.0 cuts. Harmless only because the file happened to be identical across them, but it silently decoupled the published gate from the published spec. The pin now tracks the current version and moves with every cut.

## [2.1.0] — 2026-07-15

Slice-coordinate grammar extension, raised by the maintainer after using the SLC coordinate against real corpora — plus the sub-slice established as a first-class concept and a clarity refinement of P1's statement. **Backwards-compatible minor** — every slice coordinate valid under v2.0.1 stays valid, and no corpus artifact becomes non-conformant — the first minor of the v2 line. `spec/v2.1.0/` created; `spec/v2.0.1/`, `spec/v2.0.0/`, `spec/v1.1.0/` and `spec/v1.0.0/` retained frozen for audit; `spec/latest` → `v2.1.0`.

### Added

- **The sub-slice as a first-class concept** ([`DEC-0014`](decisions/DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md), clause DEC-0014_4): a sub-slice is emergent granularity discovered *in execution* after its parent's coordinate was spent (the plan commits to structure; execution discovers the leaves) — reserved for emergent work bound to a parent, with foreseeable batches planned as numbered siblings. Its **rate** is a health signal for planning altitude, kept observable as a sweeper metric, never a hard gate (P9). Stated in `principles.md` P4 (atomicity under emergence) and P5 (the plan is a hypothesis), mirrored in the glossary (`Sub-slice`, `Sub-slice rate`), with a pointer from `naming.md` §5.
- **Sub-slice suffix on the slice coordinate** ([`DEC-0014`](decisions/DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md), clause DEC-0014_1, amending DEC-0008_6): an *optional one-letter lowercase* suffix after the slice number (`SLC0010b`) marks a slice that split off an existing one mid-implementation without renumbering its neighbours — restoring the `[a-z]` tail the legacy dotted `BL-NN[.SEC-NN].SL-NNN[a-z]` already carried (its absence from the SLC coordinate was a regression against that precedent; the evidence `sliceId` pattern kept the suffix on its dotted side).
- **Alphabetic section codes** (clause DEC-0014_2): a `SEC` code may be all-uppercase-letters (`SECDOC`, `SECAPI`) as well as all-digits (`SEC03`), each code *pure* (digits xor letters, never mixed — `SECA1` is invalid). The single normative constraint: an alphabetic code **must not contain the substring `BL`** (the one parse-ambiguity source against the block qualifier), rejected at write time — e.g. `SECTABLE`. The block qualifier `BL` stays **numeric**.
- New canonical examples in `naming.md` §5 and the glossary: `SLC0010b`, `SLC0010bSECAPIBL02`, `SLC0001bSEC21BL06`, `SLC0034SECDOC` (alongside the unchanged `SLC0012SEC03BL02`, `SLC0034`). The coordinate grammar is now `SLC\d{4,}[a-z]?(SEC(\d{2,}|[A-Z]{2,}))?(BL\d{2,})?`.

### Changed

- **Dotted-recognizer retirement made pin-governed** (clause DEC-0014_3): the retirement of the dotted coordinate (DEC-0008_6) binds a corpus only once it adopts a spec version ≥2.0.1; a corpus whose `sliceops.json` still pins 2.0.0 is not in violation and migrates when it raises its pin.
- **Legacy dotted recognizer widened** to see the sub-slice and alphabetic-section forms in old coordinates (previously invisible to migration tooling): `^BL-?\d+\.SEC-?(\d+|[A-Z]+)\.SL-?\d+[a-z]?$`.
- Naming validator (`.claude/hooks/naming_validator.py`): `SLC_COORD`, `SLC_FILENAME` and `SLC_LEGACY_DOTTED` updated to the extended grammars, plus a write-time check rejecting the substring `BL` inside an alphabetic section code (both the filename and `originating_slice:` frontmatter forms).
- evidence.v1 `sliceId` pattern (`reference/evidence/evidence.v1.schema.json`) extended on **both** sides — the SLC coordinate gains the sub-slice suffix and alphabetic section codes; the dotted alternative gains the alphabetic section (it already carried the `[a-z]` suffix). Additive: every previously accepted `sliceId` stays valid.
- **P1 statement refined onto the provenance axis** ([`DEC-0015`](decisions/DEC-0015-20260716-p1-statement-provenance-axis-clarity.md), under the P3 gate): P1's statement now leads with the **session** that produced a decision (the slice being its DEV special case) and names the two axes the word "slice" was straddling — the **provenance** axis (P1: *where* a decision was produced) versus the **dependency** axis (the cognition cycle: decisions precede the plans and slices that are their consequence). Wording, not substance: the twelve-principle set, P1's anchoring/back-link/out-of-band rules, and every corpus artifact's conformance are unchanged. The provenance bullet now cites the SLC coordinate (§5) instead of the retired dotted format.
- `spec/latest` → `v2.1.0`; the version index in `spec/README.md` and the root `_index.md` routes updated to v2.1.0.

## [2.0.1] — 2026-07-13

Clause-citation separator amendment, raised by the owner reviewing the published v2.0.0.

### Changed

- **Clause identifiers are cited `DEC-NNNN_n`** (sub-clauses `DEC-NNNN_n_m`) — underscore, not dot ([`DEC-0013`](decisions/DEC-0013-20260713-clause-identifier-separator-underscore.md), superseding the notation of DEC-0008_9): dots are fragile wherever an identifier may materialize as a filename, the same rationale that retired the dotted slice coordinate. Living corpora swept; `spec/v2.0.1/` cut (v2.0.0 frozen keeps its dotted citations — DEC-0013 is their alias note); validator messages updated.

## [2.0.0] — 2026-07-13

The cognition cycle and the universal identifier scheme. Governed by [`decisions/DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md`](decisions/DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) (with [`DEC-0009`](decisions/DEC-0009-20260712-handoffs-as-a-contextpack-kind.md) and [`DEC-0010`](decisions/DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md)), absorbing the total naming homologation of [`DEC-0007`](decisions/DEC-0007-20260710-spec-v1-2-0-naming-homologation.md) — the v1.2.0 cut those changes were first drafted into was **never published**; it re-issues here as a major version because catalog renames, new required fields and the universal grammar are breaking changes to the framework contract. `spec/v2.0.0/` created; `spec/v1.1.0/` and `spec/v1.0.0/` retained frozen for audit.

### Added (v2.0.0 scope — the cognition cycle)

- **The catalog presented on the cognition cycle** (clause DEC-0008_1): philosophize → observe → conclude → decide (strategic) → aim → focus → decide (tactical) → act → record → learn again. Stable numbers; DecisionRecord appears at two moments by design.
- **Universal identifier grammar** (clause DEC-0008_5): `PREFIX-NNNN-YYYYMMDD-slug.md` for every entity artifact in every store — counters minimum 4 digits, unbounded, per corpus per entity, lifecycle-stable; compact immutable creation date; kebab-case slugs. Mechanized by the toolkit's `claim_id.py`.
- **Decision kind axis + goal edges** (clause DEC-0008_3): `kind: constitutive | strategic | tactical`; `defines-goal` / `serves-goal` / `serves-value`; machine-checkable coherence. **Clause identifiers** `DEC-NNNN_n` with the independence test (clause DEC-0008_9).
- **The pyramid, mandatory** (clause DEC-0008_4): `Goal.decided-by`, `Priority.serves-goal` + integer `rank` (buckets retired).
- **Slice coordinate** `SLC[n]SEC[n]BL[n]` (clause DEC-0008_6) — letters as separators; dotted `BL-XX.SEC-XX.SL-XXX` retired (git-reference and filename safety).
- **Handoffs standardized** as ContextPack `kind: handoff` ([`DEC-0009`](decisions/DEC-0009-20260712-handoffs-as-a-contextpack-kind.md)): the two birth conditions (context-exhausted, spinoff), canonical body sections, session-provenance loop.
- **The corpus index** `_index.md` as reserved-name infrastructure ([`DEC-0010`](decisions/DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md)): mandatory at every corpus root, zero-discovery, points-never-copies, routes must resolve; reserved infrastructure names formalized.
- Plain-language rule (clause DEC-0008_7): acronyms defined at first use; template heading "TL;DR" → "Summary".
- **The canonical corpus container and layout** `_sliceops/` ([`DEC-0011`](decisions/DEC-0011-20260713-canonical-corpus-container-and-layout.md)): the unit-of-work rule (directory / repository named `_sliceops` / pointer manifest), cycle-ordered decades with reserved semantics and presence activation, the complete WHAT under `50-products/`, the reserved underscore family (`_agents.md` · `_policies.md` derived · `_metrics/` · `_meta/`), the adoption manifest `sliceops.json`; the former "-engineering" numbered profile retired.
- **Catalog amendments** ([`DEC-0012`](decisions/DEC-0012-20260713-catalog-amendments-mental-model-and-policy.md)): the entity's final name **MentalModel** (`MM-`), and **Policy** (`POL-`) as the fourteenth canonical entity — operating rules with `scope` / `enforced-by` / `severity`, `_policies.md` demoted to a derived summary. New templates: `policy-template.md`, `sliceops-json-template.md`.

### Changed (v2.0.0 scope)

- **Three entities renamed to plain words** (clause DEC-0008_2): CognitiveFramework → **MentalModel** (`MM-`; interim design name "Frame"/`FRAME-` also retired — clause DEC-0012_1), LearningPattern → **Conclusion** (`CONC-`), ActivePriority → **Priority** (`PRI-`) — semantics preserved; old names become implementation aliases; `LP-`/`CF-`/`FRAME-`/`AP-` retired.
- Entity catalog, glossary and naming.md rewritten from the single-source table (clause DEC-0008_2_1).

### Added (absorbed naming homologation, first drafted as v1.2.0 — never published)

### Added

- **Canonical naming standard** ([`spec/v2.0.0/naming.md`](spec/v2.0.0/naming.md)) — the single normative source for artifact naming: canonical prefix per entity (14-entity table since DEC-0012), the universal identifier grammar (the interim per-store ID schemes were retired by DEC-0008_5 within this same release), DecisionRecord lifecycle in the prefix (`DEC-` / `DEC-P-` / `DEC-D-` with `status: pending|approved|deprecated`), flat `decisions/` folders, migration alias tables (pre-v1.2.0 → v1.2.0) and vendor implementation-alias table.
- Glossary entries: *Naming (canonical prefixes)*, *OutcomeRecord* (with mandatory `kind: retrospective|postmortem|result`), *Capability components (standard/runbook/playbook)*, *RFC (retired term)*.
- Capability **component model** (`reference/entity-catalog/04-capability.md`): `standard`/`runbook`/`playbook` as sibling components via `kind:` + `capability:` back-reference — the catalog does not grow.
- Templates born homologated: [`capability-template.md`](reference/templates/capability-template.md), [`outcome-record-template.md`](reference/templates/outcome-record-template.md); `dec-template.md` rewritten to the lifecycle-prefix form.
- Naming enforcement (spec `naming.md` §9): CI **naming-validator merge gate** (`.github/workflows/ci.yml`, fetched from the toolkit) + pre-write agent hook (`.claude/settings.json` → `.claude/hooks/naming_validator.py`). Reference implementation: `sliceops-toolkit/templates/naming-validator/`.
- Layer B.1 measurement artifact ([`reference/measurement/`](reference/measurement/)): Build-Complexity Profile (six axes, 0–4, composite index /24) + build-velocity (commit-active hours, session-clustered) — ex-post product measurement, orthogonal to `sizing/` (ex-ante) and `model-triage/` (session routing). Approved in [`decisions/DEC-0004-20260630-build-complexity-measurement-model.md`](decisions/DEC-0004-20260630-build-complexity-measurement-model.md) (proposed 2026-06-30, founder-approved 2026-07-02).

### Changed

- **The term "RFC" is retired**; a proposal is a pending DecisionRecord (`DEC-P-`). `governance/RFC-PROCESS.md` → [`governance/PROPOSAL-PROCESS.md`](governance/PROPOSAL-PROCESS.md).
- **`decisions/` flattened** (this repo, dogfooding): `accepted/` files renamed `DR-*` → `DEC-*` with `status: approved`; lifecycle subfolders retired; every reference rewritten in the same change (R5). The publishing-layout DEC carries the amendment annotation.
- DecisionRecord `status` enum homologated to `pending|approved|deprecated` (legacy `proposed`/`ratified`/`superseded` read-tolerated, write-prohibited); `approver` recommendation now reads "on `status: approved`".
- evidence.v1 reference patterns brought to the universal grammar: `sliceId` accepts the `SLC` coordinate and `decisionRef` the `PREFIX-NNNN-YYYYMMDD-slug` form (pre-v2 forms read-tolerated for immutable history) — fold-in of clauses DEC-0008_5/.6; golden examples updated.
- Living references updated from `spec/v1.1.0/` to `spec/v2.0.0/` (root README, `reference/`, CI taxonomy path); `spec/latest` → `v2.0.0`. Historical documents keep their original version links.
- `spec/README.md` version index brought up to date (was still describing v1.0.0 as current — stale-copy fix).
- ip-boundary licensing note: the stale "No `LICENSE` file is published…" line (pre-dating the 2026-06-15 license ratification) now states the published CC BY 4.0 + MIT reality. No licensing terms changed.

## [1.1.0] — 2026-07-02

P3 author ≠ approver ratified, evidence.v1 canonical, and the version cut: `spec/v1.1.0/` created, `spec/v1.0.0/` retained for audit.

### Added

- Canonical **evidence.v1** record format (`reference/evidence/`) — the framework's audit-plane evidence record, upstreamed as Layer B.1: JSON Schema draft 2020-12 (`$id` `https://sliceops.org/schemas/evidence/evidence.v1.schema.json`), prose spec (`evidence-v1.md`: P6/P7 category mapping, vendor `extensions` boundary, signing/verification guidance — no embedded signature field in v1), and golden examples (2 valid, 3 invalid). Ratified in [`decisions/DEC-0006-20260702-evidence-v1-canonical-schema.md`](decisions/DEC-0006-20260702-evidence-v1-canonical-schema.md) — the first spec DR to carry the `approver` field. The glossary entry lands in this release (`spec/v1.1.0/glossary.md`).
- `CHANGELOG.md` (this file).
- Optional `approver` field in the DecisionRecord frontmatter reference schemas (`reference/templates/dec-template.md`, `reference/entity-catalog/01-decision-record.md`, `reference/frontmatter-schemas/base-schema.md`) — records the human who ratified a DEC (P3 human gate).
- RFC [`decisions/DEC-0005-20260702-author-approver-separation.md`](decisions/DEC-0005-20260702-author-approver-separation.md) — proposes formalizing author ≠ approver as a P3 implication (ratified in this release — see Changed).
- `spec/v1.1.0/` version directory per the versioning policy (`spec/v1.0.0/` retained for audit), plus the `spec/latest` symlink the policy prescribed at first public release.
- Glossary (`spec/v1.1.0/glossary.md`): `evidence.v1` entry, plus a canonical-record-format cross-reference in the Evidence-by-Construction entry.

### Changed

- **P3 (Human-in-the-Loop Authority) gains a ratified implication** — author ≠ approver: the DEC schema records the ratifying human in `approver`; in projects with more than one maintainer, `approver` MUST differ from `owner`; single-maintainer projects MUST record self-ratification explicitly (`approver` == `owner`). Ratified by the founder on 2026-07-02, with the wording tightened at ratification to the field-level, machine-checkable form (see the DEC's Ratification note). The RFC moved `decisions/rfcs/` → `decisions/accepted/` with `status: ratified`.
- Living references updated from `spec/v1.0.0/` to `spec/v1.1.0/` (root README, `reference/`, CI taxonomy path); historical documents keep their original version links, which remain valid because v1.0.0 is retained.

### Fixed

- Stale pre-publication copy: the licensing/visibility note in `spec/v1.0.0/README.md` (LICENSE and LICENSE-CODE exist; the repository is public), the status notes in `decisions/README.md` and `examples/README.md`, and the P12 name in the spec table of contents (canonical: Context Discipline).

## [1.0.0] — 2026-06-22

First public release — the open framework and audit plane for AI-first software engineering. Multi-agent teams ship auditable software, not vibe code.

### Added

- Canonical spec (`spec/v1.0.0/`): the 12 canonical principles (Layer A) in Why→How→What order (`principles.md`), glossary, canonical topic taxonomy, and the three-layer IP boundary.
- Layer B reference: entity catalog (thirteen entities), R-rules, frontmatter schemas, file templates, sessions, sizing, model-triage, context-router, development-model, patterns, and project-structure.
- Governance: roadmap, RFC process, IPR policy, code of conduct, DCO, plus sanitized public DecisionRecords.
- Licensing: documentation **CC BY 4.0**, code **MIT** (`DEC-0003-20260615-sliceops-license-ratification`).
- Recursive dogfooding CI: the repo runs the consistency validators it publishes on every pull request, on a protected `main`.

Decision-first and platform-agnostic — runs on any text-based AI agent plus git, no specific runtime required (P11). SliceOps™ trademark pending (EUIPO #019381071) — see `TRADEMARK.md`.

[Unreleased]: https://github.com/SliceOps/spec/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/SliceOps/spec/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/SliceOps/spec/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/SliceOps/spec/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/SliceOps/spec/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/SliceOps/spec/releases/tag/v1.0.0
