# SliceOps™ Specification v2.2.0

The canonical SliceOps™ framework specification, version 2.2.0.

**What's new in v2.2.0 (topic taxonomy, DEC-0016) over v2.1.0** — a **backwards-compatible minor**: [`topics.md`](topics.md) gains the canonical topic **`naming`** under `meta-framework`, covering the identifier standard of [`naming.md`](naming.md) — the universal grammar, entity prefixes, the slice coordinate, clause identifiers, reserved names and the alias tables. It closes a gap left by the v2 re-founding: the taxonomy predates `DEC-0008`, so the identifier standard it created was the only canonical spec document with no topic of its own, and `meta-framework` named "naming" in its own scope without carrying an entry for it. Purely additive — every `topics:` value valid in v2.1.0 stays valid, and no other entry is renamed, merged, split or removed. The scope text draws the line the taxonomy needs to keep: `naming` is the *identifier* axis, `vocabulary-discipline` is term canonicity in prose, `hierarchical-taxonomy` is the Layer A/B/C layer names.

**Carried forward from v2.1.0 (slice-coordinate grammar, DEC-0014) over v2.0.1** — a **backwards-compatible minor**, the first minor of the v2 line: the **slice coordinate** (`naming.md` §5) gains an **optional one-letter lowercase sub-slice suffix** (`SLC0010b` — restoring the `[a-z]` tail the legacy dotted form carried) and **alphabetic section codes** alongside numeric ones (`SLC0034SECDOC`), each section code *pure* (all digits or all uppercase letters) and, when alphabetic, forbidden from containing the substring `BL`; the block qualifier `BL` stays numeric. The grammar becomes `SLC\d{4,}[a-z]?(SEC(\d{2,}|[A-Z]{2,}))?(BL\d{2,})?`. Every coordinate valid in v2.0.1 stays valid. Retirement of the dotted recognizer binds a corpus only from spec ≥2.0.1 (corpora pinned to 2.0.0 migrate when they raise the pin — DEC-0014_3). The legacy dotted recognizer is widened in step so migration tooling can see the sub-slice and alphabetic-section forms in old coordinates.

**Carried forward from v2.0.0 — the cognition cycle and the universal identifier scheme** (governed by `DEC-0008`, with `DEC-0009`–`DEC-0013`; absorbs the naming homologation of `DEC-0007`, whose v1.2.0 cut was never published): the catalog presented on the cognition cycle; three entities renamed to plain words (**MentalModel**, **Conclusion**, **Priority**); the universal grammar `PREFIX-NNNN-YYYYMMDD-slug.md` for every artifact in every store; the decision kind axis with goal edges and clause identifiers `DEC-NNNN_n` (underscore separator, DEC-0013); the mandatory pyramid (`Goal.decided-by`, `Priority.serves-goal` + `rank`); handoffs as a ContextPack kind; the reserved-name corpus index `_index.md`; the canonical corpus container `_sliceops/` and layout (DEC-0011); and the Policy entity with the MentalModel final name (fourteen entities, DEC-0012). Pre-v2 names are read-tolerated and mapped by the alias tables in [`naming.md`](naming.md) §9. The v1.1.0 additions (evidence.v1, `approver` field, measurement artifact) are carried forward unchanged.

## Table of contents

1. **[principles.md](principles.md)** — The 12 canonical principles (Layer A): P4 Slice Atomicity, P2 Audit Plane Discipline, P5 Stage as DAG-Derived View, P1 Decision Integrity by Construction, P6 Evidence-by-Construction, P7 Security-by-Construction, P8 Recursive Learning by Capture, P11 Platform-Agnostic, P3 Human-in-the-Loop Authority, P12 Context Discipline, P10 Infrastructure Continuity, P9 Shared-Resource Pre-flight. Non-negotiable.
2. **[glossary.md](glossary.md)** — Canonical vocabulary. Every canonical term has one canonical meaning (P12).
3. **[naming.md](naming.md)** — Canonical naming: one entity = one prefix; ID schemes per store; DEC lifecycle prefixes; alias tables. *New in v1.2.0.*
4. **[topics.md](topics.md)** — Canonical topic taxonomy for corpus indexing (Layer 1 frontmatter discipline).
5. **[ip-boundary.md](ip-boundary.md)** — Layer A (Principles) / Layer B (B.1 Framework Artifacts and B.2 Universal Engineering Patterns) / Layer C (C.1 Vendor Runtimes and C.2 Adopter Stack Patterns). Top-level layers stable; sub-numbering extensible.
6. **[framework-not-methodology.md](framework-not-methodology.md)** — why SliceOps is a framework, not a "methodology".

## Status

Core spec documents present. The 14-entity catalog, the R-rule starter templates, frontmatter schemas, file templates, agent-skill concept, B.2 patterns, evidence.v1, measurement, and Layer 3 validator specs are materialized in `../../reference/`. Sizing (token-band plus context-band), Model Triage, Context Router, and the development-model characterization are documented alongside.

Licensing is ratified (`DEC-0003-20260615-sliceops-license-ratification`): the spec text is licensed **CC BY 4.0** (`../../LICENSE`) and code/templates **MIT** (`../../LICENSE-CODE`). See `../../governance/IPR_POLICY.md` and `../../DISCLOSURE.md`. The repository is public.

## Versioning

SemVer. Breaking changes to the framework contract lead to a new major. Backward-compatible additions lead to a minor. Clarifications/typos lead to a patch. A new `vX.Y.Z/` directory is created for any major/minor; prior versions (`../v2.1.0/`, `../v2.0.1/`, `../v2.0.0/`, `../v1.1.0/`, `../v1.0.0/`) are retained frozen for audit; v1.2.0 was a working cut that never published (re-issued as v2.0.0). This v2.2.0 is a backwards-compatible minor over v2.1.0 (the `naming` topic added to the taxonomy by DEC-0016). `latest →` symlink points at the current version.
