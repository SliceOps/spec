# SliceOps™

> The open framework and audit plane for AI-first software engineering. Multi-agent teams ship auditable software, not vibe code.

**Status: pre-launch (private).** License ratified 2026-06-15 (`DR-2026-06-15-sliceops-license-ratification`). Skeleton, governance, and Layer B.1 reference content are in place; the repository goes public on founder approval (P3 — human-in-the-loop authority).

## What SliceOps is

An open framework constituted by **12 canonical principles** (Layer A) — non-negotiable — presented in **Why → How → What** order: *why* agentic construction needs disciplined control (P1–P3), *how* you build under it (P4–P10), and *what* it makes tangible (P11–P12). It runs on any text-based AI agent, git, and atomic-slice scoping; no specific platform or runtime is required (P11 Platform-Agnostic).

[The 12 canonical principles](spec/v1.0.0/principles.md) · [Why a framework, not a methodology?](spec/v1.0.0/framework-not-methodology.md)

## Structure

| Path | Purpose |
|---|---|
| `spec/` | Versioned canonical framework spec (principles, glossary, topics, IP boundary) |
| `reference/` | Layer B reference patterns — entity catalog, knowledge categories, R-rules, frontmatter schemas, templates, workflow exemplars |
| `decisions/` | DECs about the framework itself (recursive dogfooding) |
| `examples/` | Reference implementations and adopter onboarding |
| `governance/` | Roadmap, RFC process, maintainers, IPR policy |

Lightweight, industry-aligned **publishing layout** (precedent: OpenAPI, JSON Schema, Diátaxis, Spec Kit, PEPs). It grows folders only per explicit promotion criteria — structure emerges from need (P5 Stage-as-DAG-Derived View and P8 Recursive Learning by Capture), not imposed top-down. This publishing layout is deliberately distinct from the foundations-first project structure the framework *prescribes* to adopters — see [`reference/project-structure/`](reference/project-structure/).

## Layers

SliceOps is organized in three layers — a stable top level with extensible sub-numbering:

- **Layer A — Principles**: the 12 canonical, non-negotiable principles — the *why* and the rules. SliceOps IP.
- **Layer B — Reference Patterns**: the materializations of the principles — **B.1 Framework Artifacts** (entity catalog, R-rules, frontmatter schemas, file templates, the prescribed project structure) and **B.2 Universal Engineering Patterns** (reaffirmed industry practices plus SliceOps-formalized ones). SliceOps IP.
- **Layer C — Implementations**: concrete builds — **C.1 Vendor Runtimes** (the runtimes that execute the discipline) and **C.2 Adopter Stack Patterns** (per-stack instantiations). Owned by the vendors and adopters who build them, not by SliceOps.

The IP boundary follows these layers: A and B are SliceOps IP; C belongs to the vendor or adopter. See [`spec/v1.0.0/ip-boundary.md`](spec/v1.0.0/ip-boundary.md).

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
