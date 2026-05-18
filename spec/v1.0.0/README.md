# SliceOps™ Specification v1.0.0

**Status: drafting in progress.** This is the first canonical spec version. Documents below are being ported from canonical sources; this README is the table of contents.

## Table of contents (planned)

1. `principles.md` — The 12 canonical principles (Capa A): P1 Slice Atomicity, P2 Audit Plane Discipline, P3 Stage as DAG-Derived View, P4 Decision Integrity by Construction, P5 Evidence-by-Construction, P6 Security-by-Construction, P7 Recursive Learning by Capture, P8 Platform-Agnostic, P9 Human-in-the-Loop Authority, P10 Vocabulary Discipline, P11 Infrastructure Continuity, P12 Shared-Resource Pre-flight.
2. `glossary.md` — Canonical vocabulary. Every canonical term has a single canonical meaning (P10).
3. `topics.md` — Canonical topic taxonomy for corpus indexing.
4. `ip-boundary.md` — Capa A (Principles) / Capa B (Reference Patterns: B.1 Methodology Artifacts + B.2 Universal Engineering Patterns) / Capa C (Implementations: C.1 Vendor Runtimes + C.2 Adopter Stack Patterns). Top-level layers stable; sub-numbering extensible.

## Versioning

SemVer. Breaking changes to the methodology contract → new major. Backward-compatible additions → minor. Clarifications/typos → patch. A new `vX.Y.Z/` directory is created for any major/minor; the prior version is retained for audit.
