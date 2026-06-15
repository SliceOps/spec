# SliceOps™ Specification v1.0.0

The canonical SliceOps™ methodology specification, version 1.0.0.

## Table of contents

1. **[principles.md](principles.md)** — The 12 canonical principles (Capa A): P1 Slice Atomicity, P2 Audit Plane Discipline, P3 Stage as DAG-Derived View, P4 Decision Integrity by Construction, P5 Evidence-by-Construction, P6 Security-by-Construction, P7 Recursive Learning by Capture, P8 Platform-Agnostic, P9 Human-in-the-Loop Authority, P10 Vocabulary Discipline, P11 Infrastructure Continuity, P12 Shared-Resource Pre-flight. Non-negotiable.
2. **[glossary.md](glossary.md)** — Canonical vocabulary. Every canonical term has one canonical meaning (P10).
3. **[topics.md](topics.md)** — Canonical topic taxonomy for corpus indexing (Layer 1 frontmatter discipline).
4. **[ip-boundary.md](ip-boundary.md)** — Capa A (Principles) / Capa B (B.1 Methodology Artifacts + B.2 Universal Engineering Patterns) / Capa C (C.1 Vendor Runtimes + C.2 Adopter Stack Patterns). Top-level layers stable; sub-numbering extensible.

## Status

Core spec documents present. The 13-entity catalog, 27 knowledge categories, R1–R14 templates, frontmatter schemas, file templates, agent-skill concept, B.2 patterns, and Layer 3 validator specs are materialized in `../../reference/`. Sizing (token-band + context-band), Model Triage, Context Router, and the development-model characterization are documented alongside.

Licensing pending IP/Legal ratification — no `LICENSE` file yet by design (see `../../governance/IPR_POLICY.md`, `../../DISCLOSURE.md`). Repository private until scaffolding complete.

## Versioning

SemVer. Breaking changes to the methodology contract → new major. Backward-compatible additions → minor. Clarifications/typos → patch. A new `vX.Y.Z/` directory is created for any major/minor; the prior version is retained for audit. `latest →` symlink added at first public release.
