# SliceOps™

> The open framework and audit plane for AI-first software engineering. Multi-agent teams ship auditable software, not vibe code.

**Status: pre-launch (private).** License ratified 2026-06-15 (`DR-2026-06-15-sliceops-license-ratification`). Skeleton, governance, and Layer B.1 reference content are in place; the repository goes public on founder approval (P9 — human-in-the-loop authority).

## What SliceOps is

An open framework constituted by **12 canonical principles** (Layer A) — non-negotiable. It runs on any text-based AI agent, git, and atomic-slice scoping; no specific platform or runtime is required (P8).

[Why a framework, not a methodology?](spec/v1.0.0/framework-not-methodology.md)

## Structure

| Path | Purpose |
|---|---|
| `spec/` | Versioned canonical framework spec (principles, glossary, topics, IP boundary) |
| `reference/` | Layer B reference patterns — entity catalog, knowledge categories, R-rules, frontmatter schemas, templates, workflow exemplars |
| `decisions/` | DECs about the framework itself (recursive dogfooding) |
| `examples/` | Reference implementations and adopter onboarding |
| `governance/` | Roadmap, RFC process, maintainers, IPR policy |

Lightweight, industry-aligned structure (precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs). Grows into more folders only per explicit promotion criteria — structure emerges from need (P3 and P7), not imposed top-down.

## Layers (IP boundary)

- **Layer A — Principles**: 12 canonical principles. SliceOps IP.
- **Layer B — Reference Patterns**: B.1 Framework Artifacts and B.2 Universal Engineering Patterns. SliceOps IP.
- **Layer C — Implementations**: C.1 Vendor Runtimes and C.2 Adopter Stack Patterns. Owned by vendors and adopters.

## License

This repository contains mixed-scope content under two licenses:

- **Documentation** (prose, spec, governance, decisions, examples, READMEs) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
- **Code** (templates, workflows, schemas, validators) is licensed under the [MIT License](LICENSE-CODE).

Code files carry an `SPDX-License-Identifier: MIT` header making per-file scope unambiguous. Full terms and the contribution posture (Inbound = Outbound, certified by the DCO; no CLA for v1) are in [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md).

Copyright (c) 2026 Andrés Ramírez Sierra.

SliceOps™ is a trademark of Andrés Ramírez Sierra (EUIPO filing #019381071, pending registration). Trademark usage is governed separately by [`TRADEMARK.md`](TRADEMARK.md) — the CC BY 4.0 / MIT licenses **do not** transfer trademark rights. See [`DISCLOSURE.md`](DISCLOSURE.md).

---

SliceOps™ is an open framework authored by Andrés Ramírez Sierra. Trademark and copyright held personally.

Companion repository: [sliceops-toolkit](https://github.com/SliceOps/toolkit) — CI guardrail templates, validators, slice-forecaster, DAG builder.
