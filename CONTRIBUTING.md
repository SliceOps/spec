# Contributing to SliceOps™

> **Status: contribution terms ratified 2026-06-15** (`DR-2026-06-15-sliceops-license-ratification`). This repository is private pre-launch; external pull requests are accepted once it goes public (P3 — founder approval).

Thank you for your interest in contributing to SliceOps™. This page is the **practical guide** to contributing. The binding legal terms — license scope, trademark separation, and the contribution license — live in [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md).

By opening a pull request you agree to both of the following:

1. **Contribution license — Inbound = Outbound.** Your contribution is licensed under the same license as the file you change: CC BY 4.0 for documentation, MIT for code. Contributing grants no trademark rights. Full terms: [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md).
2. **Developer Certificate of Origin (DCO).** You certify that you have the right to submit the contribution, by signing off your commits (below).

## Developer Certificate of Origin

SliceOps uses the **Developer Certificate of Origin 1.1** — full text in [`DCO`](DCO) — instead of a Contributor License Agreement. It is lightweight: there is nothing separate to sign, you simply certify each commit.

Sign off every commit with `-s`:

```
git commit -s -m "Your message"
```

This appends a line certifying the DCO:

```
Signed-off-by: Your Name <your.email@example.com>
```

Use a real name and email — anonymous contributions cannot be accepted. Every commit in a pull request must be signed off, and a DCO check enforces it. No Contributor License Agreement (CLA) is required for v1.

## Git workflow

Standard fork-and-pull-request flow:

1. **Fork** the repository and **clone** your fork.
2. **Branch** off `main` with a descriptive name (e.g. `feat/<short-slug>` or `fix/<short-slug>`); if the change maps to a slice, align the branch to the slice ID (P4 — Slice Atomicity).
3. **Commit** in atomic steps, each **signed off** (`git commit -s`) per the DCO above. Write clear messages in the imperative mood, explaining the *why*.
4. **Keep the pull request atomic** — one slice = one PR (P4). Rebase on the latest `main` before opening it.
5. **Push** to your fork and **open a pull request** against `main`. Fill the description with the scope declaration (and the produced DEC list, if any).
6. **CI must be green** and a maintainer must approve before merge (P3 — Human-in-the-Loop Authority). Address review feedback with follow-up signed-off commits.

Squash-merge keeps `main` history linear; the pull-request description is preserved as the audit trail.

## The process

### 1. One slice = one PR

Contributions follow SliceOps's own discipline (P4 — Slice Atomicity). One atomic, vertical change per pull request, scope declared upfront.

### 2. Changes to the framework go through the RFC process

Any change to a principle, reference pattern, or canonical vocabulary is a DecisionRecord. See [`governance/RFC-PROCESS.md`](governance/RFC-PROCESS.md). Decisions are recorded with full audit-plane discipline (P2): context, alternatives considered, rationale, consequences, supersession chain.

### 3. Frontmatter and consistency discipline

DECs carry Layer 1 frontmatter (`conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check`). The Layer 2 pre-merge checklist is mandatory. (These "Layer 1 / Layer 2" labels are the consistency-management layers, distinct from the A/B/C IP layers.)

### 4. Context discipline (P12)

The corpus is the agents' shared context, so keep it single-source and coherent. Canonical terms have canonical meanings (the vocabulary facet) — do not introduce synonyms for "slice", "DEC", and the like; new canonical terms require a DEC. Do not duplicate a fact across files (it drifts) — point to its single source.

### 5. Human authority (P3)

AI-assisted contributions are welcome but treated as untrusted until human-reviewed. Maintainer approval is required before merge; critical decisions are never auto-merged.

### 6. Shared-resource pre-flight (P9)

Before scaling any parallelism lever (for example, many parallel contributor agents), enumerate, cap, alert, and telemeter the finite or serialized shared resources it consumes (CI minutes, counters, rate limits).

## Code of conduct

All participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
