# Agent-Skill — Layer B.1 Concept Spec (v1.0)

> **Status: formalized concept, vendor-neutral.** A distinct concept from the **Capability** cognitive entity (entity #4 in the catalog). "Skill" is the reserved term for *this* concept and must NOT be used for the cognitive entity.

## What an Agent-Skill is

An **Agent-Skill** is a portable, composable **procedural pack** an AI agent loads to perform a class of work: a curated bundle of *how to do X well*, not a one-off prompt. It sits at the application layer above the model and the agent loop — you prompt the skill, not the raw model.

This concept is **vendor-neutral** (P8 — Platform-Agnostic). Multiple AI coding platforms have an equivalent construct; SliceOps formalizes the *concept*, not any one vendor's implementation. Do not name it after a specific vendor.

## The six canonical elements

| Element | Definition | SliceOps principle alignment |
|---|---|---|
| **1. Description** | What the skill is for and when to invoke it (the selection contract) | P10 (precise, canonical naming) |
| **2. Instructions** | The procedural knowledge — how to do the work well | P2/P4 (the "how" is recorded, not tribal) |
| **3. Deterministic tools** | Bundled scripts/functions the skill calls instead of regenerating logic stochastically | **Determinism-over-Regeneration (B.2)**; P5 (repeatable evidence) |
| **4. Composability** | Small, chainable, reusable — not a monolithic custom mega-skill | **P1 (Slice Atomicity)** — same rationale at the skill level |
| **5. Recursive improvement** | Gets smarter every session; the chat/usage record is the tuning substrate | **P7 (Recursive Learning by Capture)** |
| **6. Invocation control** | Flags governing when the model may auto-invoke vs requires explicit human authorization (high-risk actions gated) | **P9 (Human-in-the-Loop Authority)** |

## Why "Skill" ≠ "Capability"

- **Capability** (cognitive entity #4): *a competence accrued by an individual/agent/team* — a record of what an actor can now do. Lives in the entity catalog. Append-tracked, evidence-backed.
- **Agent-Skill** (this concept): *a procedural pack an agent loads to do work* — an executable bundle, not a record of accrued competence.

They relate (using an Agent-Skill can accrue a Capability) but are categorically distinct. The cognitive entity was renamed from "Skill" to "Capability" precisely so "Skill" could be reserved for this concept (P10 — resolve the overload, do not let it drift).

## Relationship to the rest of the framework

- An Agent-Skill **bundles** deterministic tools — instances of Determinism-over-Regeneration (`../patterns/`).
- An Agent-Skill is **composed**, not custom-built per task — P1 at skill granularity.
- An Agent-Skill **improves** via the recursive-learning loop — its tuning is the artifact-level granularity of P7 (the "one-off vs permanent" tuning gate): when a skill underperforms, ask "one-off or permanent?"; if permanent, update the skill artifact immediately (don't wait for the ≥3 LearningPattern threshold).
- An Agent-Skill's **invocation-control** flags are a concrete P9 mechanism (high-risk actions require explicit human authorization; the model may not silently self-invoke them).

## Anti-patterns

- Using "Skill" for the cognitive entity (that is **Capability** — P10 enforced).
- Naming the concept after a specific vendor/tool (violates P8 — the concept is vendor-neutral).
- Monolithic custom mega-skills (violates P1 composability).
- A skill that regenerates its own tooling logic stochastically each run instead of bundling deterministic tools (violates Determinism-over-Regeneration / P5).
- A skill that can auto-invoke high-risk actions with no invocation-control gate (violates P9).
- A skill never tuned despite repeated underperformance (violates P7 artifact-level tuning).

## Formalization status & scope

This document **formalizes the concept** (the term, the six elements, the principle alignment, the boundary vs Capability). It is intentionally a *concept spec*, not a runtime schema: concrete on-disk skill formats are a runtime/adopter concern (Layer C). Conformance test vectors and an authoring template are future work, gated behind real adopter usage (P7 — avoid premature over-formalization).

## External corroboration (not source)

The six-element structure is consistent with how engineers at a leading AI lab publicly describe using agent skills (composable, more than prompts, deterministic tools, smarter every session, invocation control). This is **external validation** that SliceOps's P1/P7/P9 were already correct — corroboration, not the source of the framework. SliceOps formalizes as an auditable framework what is otherwise tacit practice.
