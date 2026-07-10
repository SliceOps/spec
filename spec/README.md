# spec/ — Versioned canonical framework spec

The authoritative SliceOps™ framework specification, versioned with SemVer.

- `v1.2.0/` — **current version** — naming homologation: canonical prefix per entity (`naming.md`), DEC lifecycle in the prefix (`DEC-`/`DEC-P-`/`DEC-D-`), flat `decisions/` folders, "RFC" term retired, Capability component model, OutcomeRecord `kind:`
- `v1.1.0/` — evidence.v1 canonical record format, P3 author ≠ approver (`approver` field) (frozen — retained for audit)
- `v1.0.0/` — first published spec version (frozen — retained for audit)
- `latest` → symlink to the current version (`v1.2.0`)

## What lives here

| Document | Purpose |
|---|---|
| `principles.md` | The 12 canonical principles (Layer A) — non-negotiable framework core |
| `glossary.md` | Canonical vocabulary (P12 substrate) |
| `naming.md` | Canonical naming — one entity = one prefix; ID schemes; alias tables (since v1.2.0) |
| `topics.md` | Canonical topic taxonomy |
| `ip-boundary.md` | Layer A/B/C three-layer IP boundary and sub-numbering taxonomy |
| `framework-not-methodology.md` | Why SliceOps is a framework, not a "methodology" |

## What does NOT live here

Working drafts (those live in `decisions/` as pending `DEC-P-` records), adopter-specific customizations (those live in the adopter's own brain), vendor runtime implementation details.

## Versioning

SemVer. A new `vX.Y.Z/` directory is created for any major/minor; prior versions are retained frozen for audit. Content changes to a released version are prohibited — evolve via a new version directory governed by a DecisionRecord in `../decisions/`.
