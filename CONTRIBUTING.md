# Contributing to SliceOps™

> **Status: external contributions are not yet open.** The contribution license is pending an IP/Legal ratification (see `governance/IPR_POLICY.md`). This repository is currently private during scaffolding.

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

Conduct expectations: see `CODE_OF_CONDUCT.md`.
