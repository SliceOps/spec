# Governance

SliceOps™ is a founder-stewarded open methodology. This document is the top-level overview; detailed governance lives in `governance/`.

## Stewardship

Authored and maintained by Andrés Ramírez Sierra. Trademark + copyright held personally (pre-incorporation; planned SliceOps LLC; eventual foundation governance — precedent: Linux/Torvalds, Python/PSF).

## Decision-making

- **Capa A (Principles)** — the 12 canonical principles. Amendments require a ratified DEC superseding the canonical principles DEC, under an elevated human-in-the-loop gate (P9). Non-negotiable: an implementation violating any principle is not SliceOps-compliant.
- **Capa B (Reference Patterns)** — B.1 Methodology Artifacts + B.2 Universal Engineering Patterns. Changes via ratified DEC.
- **Capa C (Implementations)** — vendor runtimes (C.1) + adopter stack patterns (C.2). Owned by vendors/adopters, not by SliceOps.

Top-level layers (A/B/C) are stable; sub-numbering (B.1, B.2, C.1, C.2, …) is extensible via DEC without renaming parents.

## Process

- Changes follow `governance/RFC-PROCESS.md`.
- Consistency is managed by a 6-layer mechanism (frontmatter discipline → pre-merge checklist → CI validators → reconciliation → block retrospective → quarterly curation).
- Decisions are recorded and traceable (audit plane, P2). Decisions emerge from slices (P4).

## Pointers

- `governance/MAINTAINERS.md` — authority + how it is exercised
- `governance/RFC-PROCESS.md` — proposal → ratification flow
- `governance/IPR_POLICY.md` — IP + contribution licensing (pending ratification)
- `DISCLOSURE.md` — SliceOps / reference-runtime relationship
