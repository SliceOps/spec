# Contributing to SliceOps™

> **Status: contribution license ratified 2026-06-15** (`DR-2026-06-15-sliceops-license-ratification`). Contributions are **Inbound = Outbound** (see §7). This repository is private pre-launch; external PRs are accepted once it goes public (P9 — founder approval).

Once contributions open, the process is:

## 1. One slice = one PR

Contributions follow SliceOps's own discipline (P1 — Slice Atomicity). One atomic, vertical change per pull request, scope declared upfront.

## 2. Changes to the methodology go through the RFC process

Any change to a principle, reference pattern, or canonical vocabulary is a DecisionRecord. See `governance/RFC-PROCESS.md`. Decisions are recorded with full audit-plane discipline (P2): context, alternatives considered, rationale, consequences, supersession chain.

## 3. Frontmatter + consistency discipline

DECs carry Layer 1 frontmatter (`conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check`). The Layer 2 pre-merge checklist is mandatory.

## 4. Vocabulary is canon (P10)

Canonical terms have canonical meanings. Do not introduce synonyms for "slice", "DEC", etc. New canonical terms require a DEC.

## 5. Human authority (P9)

AI-assisted contributions are welcome but treated as untrusted until human-reviewed. Maintainer approval is required before merge; critical decisions are never auto-merged.

## 6. Shared-resource pre-flight (P12)

Before scaling any parallelism lever (e.g., many parallel contributor agents), enumerate + cap + alert + telemeter the finite/serialized shared resources it consumes (CI minutes, counters, rate limits).

## 7. Contribution license — Inbound = Outbound

By opening a pull request, you license your contribution under the same license that governs the file you are changing:

- **Documentation** (prose, spec, governance, decisions, examples, READMEs) → [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
- **Code** (templates, workflows, schemas, validators, CI) → [MIT License](LICENSE-CODE), as declared by each file's `SPDX-License-Identifier: MIT` header (or the disambiguation rule in [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md) when no header is present).

No Contributor License Agreement (CLA) is required for v1 — the Inbound = Outbound posture is sufficient. **Trademark is not part of this license:** contributing grants no rights in the "SliceOps™" mark, which remains personal IP governed by [`TRADEMARK.md`](TRADEMARK.md). Full policy: [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md).

Conduct expectations: see `CODE_OF_CONDUCT.md`.
