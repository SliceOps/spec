# SliceOps™

> The open methodology and audit plane for AI-first software engineering. Multi-agent teams ship auditable software, not vibe code.

**Status: scaffolding in progress (private).** Skeleton + governance in place; Capa B reference content drafting is the next batch. Made public when Capa B.1 content is drafted, license ratified, and governance complete.

## What SliceOps is

An open methodology constituted by **12 canonical principles** (Capa A) — non-negotiable. It runs on any text-based AI agent + git + atomic-slice scoping; no specific platform or runtime is required (P8).

## Structure

| Path | Purpose |
|---|---|
| `spec/` | Versioned canonical methodology spec (principles, glossary, topics, IP boundary) |
| `reference/` | Capa B reference patterns — entity catalog, knowledge categories, R-rules, frontmatter schemas, templates, workflow exemplars |
| `decisions/` | DECs about the framework itself (recursive dogfooding) |
| `examples/` | Reference implementations + adopter onboarding |
| `governance/` | Roadmap, RFC process, maintainers, IPR policy |

Lightweight, industry-aligned structure (precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs). Grows into more folders only per explicit promotion criteria — structure emerges from need (P3 + P7), not imposed top-down.

## Layers (IP boundary)

- **Capa A — Principles**: 12 canonical principles. SliceOps IP.
- **Capa B — Reference Patterns**: B.1 Methodology Artifacts + B.2 Universal Engineering Patterns. SliceOps IP.
- **Capa C — Implementations**: C.1 Vendor Runtimes + C.2 Adopter Stack Patterns. Owned by vendors/adopters.

## Licensing

Intended: documentation under CC BY 4.0, code templates under MIT. **Final terms pending IP/Legal ratification — no `LICENSE` file yet by design.** See `governance/IPR_POLICY.md` and `DISCLOSURE.md`.

---

SliceOps™ is an open methodology authored by Andrés Ramírez Sierra. Trademark and copyright held personally.

Companion repository: [sliceops-toolkit](https://github.com/SliceOps/toolkit) — CI guardrail templates, validators, slice-forecaster, DAG builder.
