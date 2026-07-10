# File Templates — Layer B.1 (v1.2)

Copy-to-start file skeletons. SliceOps IP (Layer B.1); documentation under CC BY 4.0, templates usable under MIT (ratified — see `../../governance/IPR_POLICY.md`).

All templates are born homologated: canonical prefixes and frontmatter per [`spec/v1.2.0/naming.md`](../../spec/v1.2.0/naming.md).

## Files

- [`slice-template.md`](slice-template.md) — a slice scope/PR-description skeleton (P4)
- [`dec-template.md`](dec-template.md) — a DecisionRecord skeleton with Layer 1 fields (lifecycle in the prefix: `DEC-P-` → `DEC-` → `DEC-D-`; flat `decisions/`; optional `approver`, P3)
- [`insight-record-template.md`](insight-record-template.md) — an InsightRecord skeleton (append-only, P8)
- [`capability-template.md`](capability-template.md) — a Capability skeleton with the component model (`standard`/`runbook`/`playbook` via `kind:`)
- [`outcome-record-template.md`](outcome-record-template.md) — an OutcomeRecord skeleton with mandatory `kind:` (retrospective/postmortem/result)

Templates for the remaining entities follow the per-entity schemas in `../entity-catalog/`. Adopters may extend these with stack-specific sections (Layer C.2) but must preserve the canonical fields for cross-adopter interoperability.
