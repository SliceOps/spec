# Changelog

All notable changes to the SliceOps™ framework specification are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) per the Versioning policy in [`spec/v1.1.0/README.md`](spec/v1.1.0/README.md).

## [Unreleased]

## [2.1.0] — 2026-07-15

Slice-coordinate grammar extension, raised by the maintainer after using the SLC coordinate against real corpora. **Backwards-compatible minor** — every slice coordinate valid under v2.0.1 stays valid — the first minor of the v2 line. `spec/v2.1.0/` created; `spec/v2.0.1/`, `spec/v2.0.0/`, `spec/v1.1.0/` and `spec/v1.0.0/` retained frozen for audit; `spec/latest` → `v2.1.0`.

### Added

- **Sub-slice suffix on the slice coordinate** ([`DEC-0014`](decisions/DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md), clause DEC-0014_1, amending DEC-0008_6): an *optional one-letter lowercase* suffix after the slice number (`SLC0010b`) marks a slice that split off an existing one mid-implementation without renumbering its neighbours — restoring the `[a-z]` tail the legacy dotted `BL-NN[.SEC-NN].SL-NNN[a-z]` already carried (its absence from the SLC coordinate was a regression against that precedent; the evidence `sliceId` pattern kept the suffix on its dotted side).
- **Alphabetic section codes** (clause DEC-0014_2): a `SEC` code may be all-uppercase-letters (`SECDOC`, `SECAPI`) as well as all-digits (`SEC03`), each code *pure* (digits xor letters, never mixed — `SECA1` is invalid). The single normative constraint: an alphabetic code **must not contain the substring `BL`** (the one parse-ambiguity source against the block qualifier), rejected at write time — e.g. `SECTABLE`. The block qualifier `BL` stays **numeric**.
- New canonical examples in `naming.md` §5 and the glossary: `SLC0010b`, `SLC0010bSECAPIBL02`, `SLC0001bSEC21BL06`, `SLC0034SECDOC` (alongside the unchanged `SLC0012SEC03BL02`, `SLC0034`). The coordinate grammar is now `SLC\d{4,}[a-z]?(SEC(\d{2,}|[A-Z]{2,}))?(BL\d{2,})?`.

### Changed

- **Dotted-recognizer retirement made pin-governed** (clause DEC-0014_3): the retirement of the dotted coordinate (DEC-0008_6) binds a corpus only once it adopts a spec version ≥2.0.1; a corpus whose `sliceops.json` still pins 2.0.0 is not in violation and migrates when it raises its pin.
- **Legacy dotted recognizer widened** to see the sub-slice and alphabetic-section forms in old coordinates (previously invisible to migration tooling): `^BL-?\d+\.SEC-?(\d+|[A-Z]+)\.SL-?\d+[a-z]?$`.
- Naming validator (`.claude/hooks/naming_validator.py`): `SLC_COORD`, `SLC_FILENAME` and `SLC_LEGACY_DOTTED` updated to the extended grammars, plus a write-time check rejecting the substring `BL` inside an alphabetic section code (both the filename and `originating_slice:` frontmatter forms).
- evidence.v1 `sliceId` pattern (`reference/evidence/evidence.v1.schema.json`) extended on **both** sides — the SLC coordinate gains the sub-slice suffix and alphabetic section codes; the dotted alternative gains the alphabetic section (it already carried the `[a-z]` suffix). Additive: every previously accepted `sliceId` stays valid.
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
