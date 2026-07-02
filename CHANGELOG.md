# Changelog

All notable changes to the SliceOps™ framework specification are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) per the Versioning policy in [`spec/v1.0.0/README.md`](spec/v1.0.0/README.md).

## [Unreleased]

### Added

- Canonical **evidence.v1** record format (`reference/evidence/`) — the framework's audit-plane evidence record, upstreamed as Layer B.1: JSON Schema draft 2020-12 (`$id` `https://sliceops.org/schemas/evidence/evidence.v1.schema.json`), prose spec (`evidence-v1.md`: P6/P7 category mapping, vendor `extensions` boundary, signing/verification guidance — no embedded signature field in v1), and golden examples (2 valid, 3 invalid). Ratified in [`decisions/accepted/DR-2026-07-02-evidence-v1-canonical-schema.md`](decisions/accepted/DR-2026-07-02-evidence-v1-canonical-schema.md) — the first spec DR to carry the `approver` field. Glossary entry for `evidence.v1` is deferred to the next spec minor version.
- `CHANGELOG.md` (this file).
- Optional `approver` field in the DecisionRecord frontmatter reference schemas (`reference/templates/dec-template.md`, `reference/entity-catalog/01-decision-record.md`, `reference/frontmatter-schemas/base-schema.md`) — records the human who ratified a DEC (P3 human gate).
- RFC [`decisions/rfcs/DR-2026-07-02-author-approver-separation.md`](decisions/rfcs/DR-2026-07-02-author-approver-separation.md) — proposes formalizing author ≠ approver as a P3 implication.

### Fixed

- Stale pre-publication copy: the licensing/visibility note in `spec/v1.0.0/README.md` (LICENSE and LICENSE-CODE exist; the repository is public), the status notes in `decisions/README.md` and `examples/README.md`, and the P12 name in the spec table of contents (canonical: Context Discipline).

## [1.0.0] — 2026-06-22

First public release — the open framework and audit plane for AI-first software engineering. Multi-agent teams ship auditable software, not vibe code.

### Added

- Canonical spec (`spec/v1.0.0/`): the 12 canonical principles (Layer A) in Why→How→What order (`principles.md`), glossary, canonical topic taxonomy, and the three-layer IP boundary.
- Layer B reference: entity catalog (13 entities), R-rules, frontmatter schemas, file templates, sessions, sizing, model-triage, context-router, development-model, patterns, and project-structure.
- Governance: roadmap, RFC process, IPR policy, code of conduct, DCO, plus sanitized public DecisionRecords.
- Licensing: documentation **CC BY 4.0**, code **MIT** (`DR-2026-06-15-sliceops-license-ratification`).
- Recursive dogfooding CI: the repo runs the consistency validators it publishes on every pull request, on a protected `main`.

Decision-first and platform-agnostic — runs on any text-based AI agent plus git, no specific runtime required (P11). SliceOps™ trademark pending (EUIPO #019381071) — see `TRADEMARK.md`.

[Unreleased]: https://github.com/SliceOps/spec/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/SliceOps/spec/releases/tag/v1.0.0
