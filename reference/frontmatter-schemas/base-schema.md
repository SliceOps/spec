# Base Frontmatter Schema — Layer B.1

Every SliceOps entity document carries this common base. Entity-specific fields are added per the entity catalog (`../entity-catalog/<NN>-<entity>.md`).

```yaml
entity: <EntityName>          # canonical type key (vendor-neutral); value from the catalog
status: <lifecycle state>      # valid states are entity-specific (see catalog)
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>     # single accountable human/team/agent (R3)
approver: <approving human>    # OPTIONAL — the human who approved (P3 gate); recommended on status: approved
sensitivity: public | internal | restricted | sensitive   # R11
```

## Field semantics

| Field | Rule | Notes |
|---|---|---|
| `entity` | R3 | Must be a canonical entity name (entity catalog) or an adopter-declared extension |
| `status` | R3, R5 | Lifecycle state; transitions are atomic (R5) |
| `created` / `updated` | R3 | `updated` bumps on every semantic touch (P12 fix-on-touch) |
| `owner` | R3 | Single accountable party; not an AI handle (P3 — humans accountable) |
| `approver` | optional | The human who approved the document (P3 human gate); not an AI handle. Recommended on `status: approved`. MAY equal `owner` in single-maintainer contexts — the point is recording *who* approved, making self-approval explicit and auditable instead of implicit |
| `sensitivity` | R11 | From the canonical set; adopters may restrict the allowed subset by audience policy |

## Canonical enums and required edges (v2.0.0)

Normative source: [`spec/v2.0.0/naming.md`](../../spec/v2.0.0/naming.md). What the naming validator enforces on write:

| Entity | Field | Canonical values / rule | Read tolerance (write-prohibited) |
|---|---|---|---|
| DecisionRecord | `status` | `pending` / `approved` / `deprecated` (must match the `DEC-P-`/`DEC-`/`DEC-D-` prefix) | `proposed`→pending · `ratified`/`active`/`accepted`→approved · `superseded`→deprecated |
| DecisionRecord | `kind` | `constitutive` / `strategic` / `tactical` — strategic requires `defines-goal:`, tactical requires `serves-goal:`, constitutive requires `approver:` (mandatory for records created ≥ 2026-07-13) | earlier records back-filled fix-on-touch |
| OutcomeRecord | `kind` | `retrospective` / `postmortem` / `result` (mandatory) | — |
| Capability (component files) | `kind` + `capability` | `standard` / `runbook` / `playbook`, with `capability: <mother-slug>` | — |
| Goal | `decided-by` | REQUIRED — the decision that created the goal | — |
| Priority | `serves-goal` + `rank` | REQUIRED — goal edge + integer rank unique within (owner, horizon) | `priority: high\|medium\|low` retired |
| ContextPack | `kind` | `pack` / `brief` / `handoff` (handoff: `reason: context-exhausted\|spinoff`) | — |
| Policy | `scope` | REQUIRED — `environment` / `agent` / `corpus` / `session` (vendors MAY extend the values in their own runtimes, Layer C) | — |
| Policy | `severity` + `enforced-by` + `status` | `block` / `warn` · enforcement surfaces (`hook`/`validator`/`runtime`/`human`) · `active` / `deprecated`; the corpus `_policies.md` is DERIVED from active records (DEC-0012.3) | — |

## Notes

- The base is intentionally minimal. Entity catalog specs add the typed fields each entity needs (e.g., DecisionRecord adds supersession and Layer 1 fields; InsightRecord adds append-only cross-refs).
- Runtimes may add runtime-specific fields under their own IP, but the base and catalog fields must remain present and portable (P11).
- A document missing required base fields fails R3.
