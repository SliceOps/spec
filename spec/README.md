# spec/ — Versioned canonical framework spec

The authoritative SliceOps™ framework specification, versioned with SemVer.

- `v2.0.1/` — **current version** — clause citations `DEC-NNNN_n` (underscore separator, DEC-0013; the only change vs v2.0.0)
- `v2.0.0/` — the v2 re-founding — the cognition cycle + the universal identifier grammar (`PREFIX-NNNN-YYYYMMDD-slug`), MentalModel/Conclusion/Priority renames, the Policy entity (fourteen-entity catalog, DEC-0012), the canonical corpus container `_sliceops/` and layout (DEC-0011), decision kind axis + clause identifiers, mandatory pyramid, `SLC` slice coordinate, handoffs as ContextPack kind, reserved-name `_index.md` (absorbs the never-published v1.2.0 naming homologation)
- `v1.1.0/` — evidence.v1 canonical record format, P3 author ≠ approver (`approver` field) (frozen — retained for audit)
- `v1.0.0/` — first published spec version (frozen — retained for audit)
- `latest` → symlink to the current version (`v2.0.1`)

## What lives here

| Document | Purpose |
|---|---|
| `principles.md` | The 12 canonical principles (Layer A) — non-negotiable framework core |
| `glossary.md` | Canonical vocabulary (P12 substrate) |
| `naming.md` | Canonical naming — one entity = one prefix = one grammar; alias tables (normative since v2.0.0) |
| `topics.md` | Canonical topic taxonomy |
| `ip-boundary.md` | Layer A/B/C three-layer IP boundary and sub-numbering taxonomy |
| `framework-not-methodology.md` | Why SliceOps is a framework, not a "methodology" |

## What does NOT live here

Working drafts (those live in `decisions/` as pending `DEC-P-` records), adopter-specific customizations (those live in the adopter's own corpus), vendor runtime implementation details.

## Versioning

SemVer. A new `vX.Y.Z/` directory is created for any major/minor; prior versions are retained frozen for audit. Content changes to a released version are prohibited — evolve via a new version directory governed by a DecisionRecord in `../decisions/`.
