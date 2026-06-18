# Frontmatter Schemas — Layer B.1 (v1.0)

Canonical frontmatter schemas. SliceOps IP (Layer B.1). The **per-entity** field schemas live in the entity catalog (`../entity-catalog/`); this folder specifies the **cross-cutting** schema layers every entity shares.

## Files

- [`base-schema.md`](base-schema.md) — the common base fields every entity doc carries
- [`layer-1-consistency-fields.md`](layer-1-consistency-fields.md) — the mandatory consistency-management fields for DecisionRecords (Layer 1 frontmatter discipline)

## Vendor-neutral key

The canonical type key is `entity:` (value = entity name from the catalog). Runtimes MAY map this to a runtime-specific typed key; `entity:` is the portable, standalone, cross-adopter form (P11). Adopters keep `entity:` for interoperability.
