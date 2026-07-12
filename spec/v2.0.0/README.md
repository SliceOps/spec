# SliceOps™ Specification v1.2.0

The canonical SliceOps™ framework specification, version 1.2.0.

**What's new in v1.2.0 — naming homologation** (governed by `DEC-2026-07-10-spec-v1-2-0-naming-homologation`): canonical prefix per entity ([`naming.md`](naming.md)), DecisionRecord lifecycle carried in the prefix (`DEC-` / `DEC-P-` / `DEC-D-`) with flat `decisions/` folders and `status: pending|approved|deprecated`, the term "RFC" retired, Capability component model (`standard`/`runbook`/`playbook` via `kind:`), OutcomeRecord `kind:`, and the migration alias tables. Backward-compatible addition (SemVer minor): entity names and catalog semantics are unchanged; pre-v1.2.0 names are read-tolerated and mapped by the alias tables. The v1.1.0 additions (evidence.v1, `approver` field, measurement artifact) are carried forward unchanged.

## Table of contents

1. **[principles.md](principles.md)** — The 12 canonical principles (Layer A): P4 Slice Atomicity, P2 Audit Plane Discipline, P5 Stage as DAG-Derived View, P1 Decision Integrity by Construction, P6 Evidence-by-Construction, P7 Security-by-Construction, P8 Recursive Learning by Capture, P11 Platform-Agnostic, P3 Human-in-the-Loop Authority, P12 Context Discipline, P10 Infrastructure Continuity, P9 Shared-Resource Pre-flight. Non-negotiable.
2. **[glossary.md](glossary.md)** — Canonical vocabulary. Every canonical term has one canonical meaning (P12).
3. **[naming.md](naming.md)** — Canonical naming: one entity = one prefix; ID schemes per store; DEC lifecycle prefixes; alias tables. *New in v1.2.0.*
4. **[topics.md](topics.md)** — Canonical topic taxonomy for corpus indexing (Layer 1 frontmatter discipline).
5. **[ip-boundary.md](ip-boundary.md)** — Layer A (Principles) / Layer B (B.1 Framework Artifacts and B.2 Universal Engineering Patterns) / Layer C (C.1 Vendor Runtimes and C.2 Adopter Stack Patterns). Top-level layers stable; sub-numbering extensible.
6. **[framework-not-methodology.md](framework-not-methodology.md)** — why SliceOps is a framework, not a "methodology".

## Status

Core spec documents present. The 13-entity catalog, 27 knowledge categories, R1–R14 templates, frontmatter schemas, file templates, agent-skill concept, B.2 patterns, evidence.v1, measurement, and Layer 3 validator specs are materialized in `../../reference/`. Sizing (token-band plus context-band), Model Triage, Context Router, and the development-model characterization are documented alongside.

Licensing is ratified (`DEC-2026-06-15-sliceops-license-ratification`): the spec text is licensed **CC BY 4.0** (`../../LICENSE`) and code/templates **MIT** (`../../LICENSE-CODE`). See `../../governance/IPR_POLICY.md` and `../../DISCLOSURE.md`. The repository is public.

## Versioning

SemVer. Breaking changes to the framework contract lead to a new major. Backward-compatible additions lead to a minor. Clarifications/typos lead to a patch. A new `vX.Y.Z/` directory is created for any major/minor; prior versions (`../v1.1.0/`, `../v1.0.0/`) are retained frozen for audit. `latest →` symlink points at the current version.
