# SliceOps™

> The open methodology and audit plane for AI-first software engineering. Multi-agent teams ship auditable software, not vibe code.

**Status: pre-launch (private).** License ratified 2026-06-15 (`DR-2026-06-15-sliceops-license-ratification`). Skeleton, governance, and Capa B.1 reference content are in place; the repository goes public on founder approval (P9 — human-in-the-loop authority).

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

## License

This repository contains mixed-scope content under two licenses:

- **Documentation** (prose, spec, governance, decisions, examples, READMEs) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
- **Code** (templates, workflows, schemas, validators) is licensed under the [MIT License](LICENSE-CODE).

Code files carry an `SPDX-License-Identifier: MIT` header making per-file scope unambiguous. Full terms and the contribution posture (Inbound = Outbound; no CLA for v1) are in [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md).

Copyright (c) 2026 Andrés Ramírez Sierra.

SliceOps™ is a trademark of Andrés Ramírez Sierra (EUIPO filing #019381071, pending registration). Trademark usage is governed separately by [`TRADEMARK.md`](TRADEMARK.md) — the CC BY 4.0 / MIT licenses **do not** transfer trademark rights. See [`DISCLOSURE.md`](DISCLOSURE.md).

---

SliceOps™ is an open methodology authored by Andrés Ramírez Sierra. Trademark and copyright held personally.

Companion repository: [sliceops-toolkit](https://github.com/SliceOps/toolkit) — CI guardrail templates, validators, slice-forecaster, DAG builder.
