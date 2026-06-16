# Base Frontmatter Schema — Layer B.1

Every SliceOps entity document carries this common base. Entity-specific fields are added per the entity catalog (`../entity-catalog/<NN>-<entity>.md`).

```yaml
entity: <EntityName>          # canonical type key (vendor-neutral); value from the catalog
status: <lifecycle state>      # valid states are entity-specific (see catalog)
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>     # single accountable human/team/agent (R3)
sensitivity: public | internal | restricted | sensitive   # R11
```

## Field semantics

| Field | Rule | Notes |
|---|---|---|
| `entity` | R3 | Must be a canonical entity name (entity catalog) or an adopter-declared extension |
| `status` | R3, R5 | Lifecycle state; transitions are atomic (R5) |
| `created` / `updated` | R3 | `updated` bumps on every semantic touch (P10 fix-on-touch) |
| `owner` | R3 | Single accountable party; not an AI handle (P9 — humans accountable) |
| `sensitivity` | R11 | From the canonical set; adopters may restrict the allowed subset by audience policy |

## Notes

- The base is intentionally minimal. Entity catalog specs add the typed fields each entity needs (e.g., DecisionRecord adds supersession and Layer 1 fields; InsightRecord adds append-only cross-refs).
- Runtimes may add runtime-specific fields under their own IP, but the base and catalog fields must remain present and portable (P8).
- A document missing required base fields fails R3.
