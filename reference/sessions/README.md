# Sessions — Layer B.1 (v1.0)

Canonical Session-Type taxonomy. Every human–AI interaction is a **Session** (cognitive entity #13, see `../entity-catalog/13-session.md`). This document specifies how Sessions are classified: 8 canonical Session-Types (level 1), Slice-Types (level 2, only when Session-Type=Slice), and 2 orthogonal axes (lifecycle and cross-cutting dimensions).

The taxonomy is **hierarchical, not flat** — earlier operational practice mixed levels (a 17-item flat list confused Session-Type with Slice-Type with sub-variants with lifecycle with cross-cutting axes). The canonical taxonomy separates them, which is what enables clean tagging, calibration by type, and audit-plane completeness.

---

## Axis 1 — Session-Type (8 canonical, vendor-neutral)

| Family | Session-Type | What it is |
|---|---|---|
| **Build** | **Slice** | Full end-to-end development → PR. Has Slice-Types (level 2). |
| **Build** | **Artifact** | A bounded output (script / template / config / doc). May be code, but NOT a complete slice. |
| **Ops** | **Support** | Incidents / care (internal or customer). Generic operations. |
| **Ops** | **Infra** | Infra / deploy / environment operations (connects to P11). |
| **Govern** | **Meta** | Governance: foundations, planning, framework or project decisions. |
| **Govern** | **Audit** | Verification / control / compliance — operationalizes P2. |
| **Learn** | **Learning** | Exploration / research / knowledge acquisition (feeds P7). |
| **Orchestrate** | **Orchestrate** | Coordinates other sessions; does not produce direct work output. **Full word per naming convention — replaces the abbreviated "COORD".** |

Each Session-Type is canonical and reserved (P10). Adopters add **sub-variants** (Layer C.2) for their stack/business, never new top-level Session-Types without a superseding decision.

---

## Axis 2 — Sub-Type (depends on Session-Type)

### Slice-Type (when Session-Type=Slice)

| Slice-Type | SemVer | Description |
|---|---|---|
| **Dev** | minor `vX.Y.0` | Feature work — new functional surface. |
| **Refactor** | patch `vX.Y.Z` | No functional change — structural improvement. |
| **Fix** | patch `vX.Y.Z` | Bug fix — restores intended behavior. |

SemVer already encodes part of the distinction; the Slice-Type makes it explicit and queryable. Adopters may add stack-specific Slice-Types (Layer C.2 — e.g., a banking adopter could add a `Regulatory` Slice-Type).

### Support-variant (when Session-Type=Support)

`Layer C.2` — adopter-defined sub-variants (e.g., "Support Multi" for multi-ticket→1-WI flows; "Support General" for sessions without an inbound ticket). The sub-variant depends on the adopter's ticketing system and is NOT part of the canonical SliceOps taxonomy.

---

## Orthogonal axis A — Lifecycle disposition

`active` | `archive` | `delete`

**NOT a Session-Type.** This is the lifecycle **state** of a session, not a kind of session. "Delete" is a disposition, not a category. A Meta session can be `archive`; a Slice session can be `active`. Lifecycle and Session-Type are orthogonal.

---

## Orthogonal axis B — Cross-cutting dimension

`security` | `compliance` | … (extensible per adopter)

**NOT a Session-Type.** A cross-cutting dimension **cuts across** types — a session can be a Slice-Fix with a security dimension, or an Audit session with a compliance dimension. "Security" is not a kind of session; it is an attribute that crosses kinds.

---

## Mapping legacy "flat 17" to canonical structure

Adopters or scripts that used an earlier flat categorization migrate as follows:

| Flat label | Canonical placement |
|---|---|
| SliceOps (BL-NN…) | Slice (Session-Type, level 1) |
| Dev, Refactor, Fix | Slice-Type (level 2) |
| Support | Support (Session-Type, level 1) |
| Support Multi, Support General | Support-variant (level 2) → Layer C.2 |
| Artifact | Artifact (Session-Type) |
| Documentation | Artifact sub-type (or its own Session-Type per adopter preference) |
| Infra | Infra (Session-Type) |
| COORD | **Orchestrate** (Session-Type) — full word per naming convention |
| Learning | Learning (Session-Type) |
| Audit | Audit (Session-Type) |
| Meta | Meta (Session-Type) |
| Security | Cross-cutting dimension (axis B) |
| Admin, Business | Layer C.2 (adopter-specific ops, not part of the canonical framework taxonomy) |
| Delete | Lifecycle disposition (axis A) |

Result: 17 flat labels become **8 canonical Session-Types, Slice-Types, and 2 orthogonal axes** — scalable and without level confusion.

---

## Why hierarchical (not flat)

A flat list cannot represent that:

- "Dev" is a sub-classification of Slice (level 2), not a sibling of Slice (level 1).
- "Security" is an attribute that cuts across types, not a sibling of Slice.
- "Delete" is a state, not a kind.
- "Admin" / "Business" are adopter ops, not part of the framework.

Mixing these in one list creates ambiguity ("what kind of session is a Security session?"), prevents clean tagging (the same session is two labels), and breaks calibration (DEV sessions and Meta sessions have very different sizing distributions; aggregating them blurs the bands).

The hierarchical taxonomy mirrors the same pattern used elsewhere in SliceOps (Layer A/B/C top-level with sub-numbering for new dimensions) — top-level stability and extensible sub-numbering, no renaming on growth.

---

## Adopter customization rules

Adopters **may**: use the 8 canonical types as-is (recommended — cross-adopter interoperability); add **Layer C.2 sub-variants** for their stack/business (e.g., Support Multi/General, banking-specific Slice-Types); add new cross-cutting **dimensions** to axis B.

Adopters **may not**: add new top-level Session-Types without a superseding decision (this would alter the canonical catalog); reuse a deprecated abbreviation (e.g., "COORD" for Orchestrate); claim SliceOps-compliance while conflicting canonical Session-Type semantics.

---

## Operational note — tagging & calibration

Sessions are tagged with their Session-Type at index time. **Calibration of token-band and context-band by Session-Type** (separately for Slice vs Meta vs Orchestrate vs …) is more useful than aggregate calibration: DEV slices skew small; Meta and Orchestrate sessions skew large. Adopters who tag by Session-Type can run the calibration script (see the SliceOps toolkit `calibration/`) per type to derive type-specific bands.
