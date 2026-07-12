# File Templates — Layer B.1 (v2.0)

Copy-to-start file skeletons. SliceOps IP (Layer B.1); documentation under CC BY 4.0, templates usable under MIT (ratified — see `../../governance/IPR_POLICY.md`).

All templates are born homologated: universal grammar `PREFIX-NNNN-YYYYMMDD-slug.md`, canonical prefixes and frontmatter per [`spec/v2.0.0/naming.md`](../../spec/v2.0.0/naming.md) — claim numbers with the toolkit's `claim_id.py`.

## Files

- [`slice-template.md`](slice-template.md) — a slice scope/PR-description skeleton (P4)
- [`dec-template.md`](dec-template.md) — a DecisionRecord skeleton with Layer 1 fields (lifecycle in the prefix: `DEC-P-` → `DEC-` → `DEC-D-`; flat `decisions/`; optional `approver`, P3)
- [`insight-record-template.md`](insight-record-template.md) — an InsightRecord skeleton (append-only, P8)
- [`capability-template.md`](capability-template.md) — a Capability skeleton with the component model (`standard`/`runbook`/`playbook` via `kind:`)
- [`outcome-record-template.md`](outcome-record-template.md) — an OutcomeRecord skeleton with mandatory `kind:` (retrospective/postmortem/result)
- [`goal-template.md`](goal-template.md) — a Goal skeleton with mandatory `decided-by:` provenance (vision = multi-year horizon)
- [`priority-template.md`](priority-template.md) — a Priority skeleton with mandatory `serves-goal:` + integer `rank`
- [`handoff-template.md`](handoff-template.md) — a ContextPack `kind: handoff` skeleton (DEC-0009: state of work, pending, open questions, counter state)
- [`index-template.md`](index-template.md) — the reserved-name corpus index `_index.md` (DEC-0010: routes that must resolve; not an entity)

Templates for the remaining entities follow the per-entity schemas in `../entity-catalog/`. Adopters may extend these with stack-specific sections (Layer C.2) but must preserve the canonical fields for cross-adopter interoperability.
