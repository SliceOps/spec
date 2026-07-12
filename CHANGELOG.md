# Changelog

All notable changes to the SliceOps™ framework specification are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) per the Versioning policy in [`spec/v1.1.0/README.md`](spec/v1.1.0/README.md).

## [Unreleased]

## [1.2.0] — 2026-07-10

Total naming homologation: one entity = one prefix in every layer and every store, the DecisionRecord lifecycle carried in the filename prefix, and the enforcement that makes the standard self-impose at the point of write. Governed by [`decisions/DEC-2026-07-10-spec-v1-2-0-naming-homologation.md`](decisions/DEC-2026-07-10-spec-v1-2-0-naming-homologation.md). `spec/v2.0.0/` created; `spec/v1.1.0/` retained for audit.

### Added

- **Canonical naming standard** ([`spec/v2.0.0/naming.md`](spec/v2.0.0/naming.md)) — the single normative source for artifact naming: canonical prefix per entity (13-entity table), per-store ID schemes (`NNN` counter-based / `YYYY-MM-DD` date-based), DecisionRecord lifecycle in the prefix (`DEC-` / `DEC-P-` / `DEC-D-` with `status: pending|approved|deprecated`), flat `decisions/` folders, migration alias tables (pre-v1.2.0 → v1.2.0) and vendor implementation-alias table.
- Glossary entries: *Naming (canonical prefixes)*, *OutcomeRecord* (with mandatory `kind: retrospective|postmortem|result`), *Capability components (standard/runbook/playbook)*, *RFC (retired term)*.
- Capability **component model** (`reference/entity-catalog/04-capability.md`): `standard`/`runbook`/`playbook` as sibling components via `kind:` + `capability:` back-reference — the catalog does not grow.
- Templates born homologated: [`capability-template.md`](reference/templates/capability-template.md), [`outcome-record-template.md`](reference/templates/outcome-record-template.md); `dec-template.md` rewritten to the lifecycle-prefix form.
- Naming enforcement (spec `naming.md` §9): CI **naming-validator merge gate** (`.github/workflows/ci.yml`, fetched from the toolkit) + pre-write agent hook (`.claude/settings.json` → `.claude/hooks/naming_validator.py`). Reference implementation: `sliceops-toolkit/templates/naming-validator/`.
- Layer B.1 measurement artifact ([`reference/measurement/`](reference/measurement/)): Build-Complexity Profile (six axes, 0–4, composite index /24) + build-velocity (commit-active hours, session-clustered) — ex-post product measurement, orthogonal to `sizing/` (ex-ante) and `model-triage/` (session routing). Approved in [`decisions/DEC-2026-06-30-build-complexity-measurement-model.md`](decisions/DEC-2026-06-30-build-complexity-measurement-model.md) (proposed 2026-06-30, founder-approved 2026-07-02).

### Changed

- **The term "RFC" is retired**; a proposal is a pending DecisionRecord (`DEC-P-`). `governance/RFC-PROCESS.md` → [`governance/PROPOSAL-PROCESS.md`](governance/PROPOSAL-PROCESS.md).
- **`decisions/` flattened** (this repo, dogfooding): `accepted/` files renamed `DR-*` → `DEC-*` with `status: approved`; lifecycle subfolders retired; every reference rewritten in the same change (R5). The publishing-layout DEC carries the amendment annotation.
- DecisionRecord `status` enum homologated to `pending|approved|deprecated` (legacy `proposed`/`ratified`/`superseded` read-tolerated, write-prohibited); `approver` recommendation now reads "on `status: approved`".
- Living references updated from `spec/v1.1.0/` to `spec/v2.0.0/` (root README, `reference/`, CI taxonomy path); `spec/latest` → `v1.2.0`. Historical documents keep their original version links.
- `spec/README.md` version index brought up to date (was still describing v1.0.0 as current — stale-copy fix).
- ip-boundary licensing note: the stale "No `LICENSE` file is published…" line (pre-dating the 2026-06-15 license ratification) now states the published CC BY 4.0 + MIT reality. No licensing terms changed.

## [1.1.0] — 2026-07-02

P3 author ≠ approver ratified, evidence.v1 canonical, and the version cut: `spec/v1.1.0/` created, `spec/v1.0.0/` retained for audit.

### Added

- Canonical **evidence.v1** record format (`reference/evidence/`) — the framework's audit-plane evidence record, upstreamed as Layer B.1: JSON Schema draft 2020-12 (`$id` `https://sliceops.org/schemas/evidence/evidence.v1.schema.json`), prose spec (`evidence-v1.md`: P6/P7 category mapping, vendor `extensions` boundary, signing/verification guidance — no embedded signature field in v1), and golden examples (2 valid, 3 invalid). Ratified in [`decisions/DEC-2026-07-02-evidence-v1-canonical-schema.md`](decisions/DEC-2026-07-02-evidence-v1-canonical-schema.md) — the first spec DR to carry the `approver` field. The glossary entry lands in this release (`spec/v1.1.0/glossary.md`).
- `CHANGELOG.md` (this file).
- Optional `approver` field in the DecisionRecord frontmatter reference schemas (`reference/templates/dec-template.md`, `reference/entity-catalog/01-decision-record.md`, `reference/frontmatter-schemas/base-schema.md`) — records the human who ratified a DEC (P3 human gate).
- RFC [`decisions/DEC-2026-07-02-author-approver-separation.md`](decisions/DEC-2026-07-02-author-approver-separation.md) — proposes formalizing author ≠ approver as a P3 implication (ratified in this release — see Changed).
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
- Layer B reference: entity catalog (13 entities), R-rules, frontmatter schemas, file templates, sessions, sizing, model-triage, context-router, development-model, patterns, and project-structure.
- Governance: roadmap, RFC process, IPR policy, code of conduct, DCO, plus sanitized public DecisionRecords.
- Licensing: documentation **CC BY 4.0**, code **MIT** (`DEC-2026-06-15-sliceops-license-ratification`).
- Recursive dogfooding CI: the repo runs the consistency validators it publishes on every pull request, on a protected `main`.

Decision-first and platform-agnostic — runs on any text-based AI agent plus git, no specific runtime required (P11). SliceOps™ trademark pending (EUIPO #019381071) — see `TRADEMARK.md`.

[Unreleased]: https://github.com/SliceOps/spec/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/SliceOps/spec/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/SliceOps/spec/releases/tag/v1.0.0
