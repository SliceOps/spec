# Corpus index — SliceOps spec repository

Reserved-name corpus index (DEC-0010): where to look for what. Points, never
copies. Load this before searching anything.

| Looking for | Go to |
|---|---|
| The 12 principles (Layer A) | `spec/v2.1.0/principles.md` |
| Canonical naming — prefixes, universal grammar, container layout, aliases | `spec/v2.1.0/naming.md` |
| Canonical vocabulary | `spec/v2.1.0/glossary.md` |
| Topic taxonomy | `spec/v2.1.0/topics.md` |
| Layer A/B/C IP boundary | `spec/v2.1.0/ip-boundary.md` |
| Version index (which spec version is current) | `spec/README.md` |
| The 14-entity catalog | `reference/entity-catalog/README.md` |
| Frontmatter schemas | `reference/frontmatter-schemas/base-schema.md` |
| File templates (DEC, Goal, Priority, Policy, index, manifest…) | `reference/templates/README.md` |
| Evidence record format (evidence.v1) | `reference/evidence/` |
| Measurement (Build-Complexity Profile, velocity) | `reference/measurement/` |
| Context routing mechanism | `reference/context-router/README.md` |
| Framework decisions (why each rule exists) | `decisions/` (flat; `DEC-NNNN-…`) |
| How to propose a change | `governance/PROPOSAL-PROCESS.md` |
| Licensing / IPR | `governance/IPR_POLICY.md` |
| Release history | `CHANGELOG.md` |
| Agent working rules for this repo | `AGENTS.md` |
| Old names (pre-v2) | `_meta/homologacion-v2/alias-map-spec.md` |

Maintenance: routes must resolve — the naming validator's continuous-integration
gate fails on a stale index (DEC-0010_4).
