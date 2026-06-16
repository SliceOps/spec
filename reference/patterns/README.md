# Layer B.2 — Universal Engineering Patterns (v1.0)

Industry-canonical engineering patterns SliceOps **reaffirms**. Vendor-agnostic, stack-agnostic. SliceOps does not claim authorship of the long-established ones (SOLID, ACID, etc.) — it reaffirms them as non-optional and adds two patterns it formalizes from AI-first practice.

## Catalog

| Pattern | Status | Where specified |
|---|---|---|
| SOLID | Reaffirmed (industry-canonical) | Industry literature |
| ACID | Reaffirmed (industry-canonical) | Industry literature |
| Outbox | Reaffirmed (industry-canonical) | Industry literature |
| Fail-Fast | Reaffirmed (industry-canonical) | Industry literature |
| Idempotency | Reaffirmed (industry-canonical) | Industry literature |
| Defense in Depth | Reaffirmed (industry-canonical) | Industry literature |
| **CI/Pipeline Cost Economy** | SliceOps-formalized | Spec below + runnable templates in the **SliceOps toolkit** repo |
| **Determinism-over-Regeneration** | SliceOps-formalized | Spec below |
| **LLM-Inference-Cost-Economy** | SliceOps-formalized (B.2 sub-domain of CI/Pipeline Cost Economy) | [Dedicated spec](llm-inference-cost-economy.md) + runnable templates in toolkit |

The two SliceOps-formalized patterns materialize principles (P12, P5/P7) in AI-first engineering, where the failure modes are intrinsic to multi-agent parallelism and stochastic generation.

---

## Determinism-over-Regeneration

**Statement**: If a process repeats, materialize it **once** as a deterministic, reusable artifact (script, function, reference file, R-rule). Do NOT stochastically regenerate it with AI each time. Deterministic code (same input → same result) is cheaper, faster, repeatable, and auditable; AI output carries drift.

**Operating rule**: *"If you can use code instead of AI, do. Have AI write the code once, then reuse it."* Invest effort in the **tools** (deterministic layer), not only in prompts (stochastic layer).

**Principle alignment**:
- **P5 (Evidence-by-Construction)** — deterministic code produces repeatable evidence; drifting AI output is fragile evidence.
- **P7 (Recursive Learning by Capture)** — the trigger to *materialize* is the recursive-learning loop: what repeats is captured as an artifact, not re-learned each session. Operates at the artifact-level "one-off vs permanent" granularity.
- **P12 (Shared-Resource Pre-flight / cost economy)** — trading AI tokens for code execution is directly cost economy; the infra-cost-ledger benefits.

**Applies to**: validators, formatters, repeated codegen, domain checks, data transforms, document styling — any process where same-input → same-result.

**Anti-patterns**:
- Regenerating the same script/process with AI every session (token waste + drift + not repeatable).
- Elaborate prompts wrapping poor tools (undocumented functions, nonsensical parameters) — the inverse of good practice.
- Treating a determinizable process as if it required AI judgment every time.
- Monolithic non-composable mega-artifact (violates P1; hampers debugging).

---

## CI/Pipeline Cost Economy

**Statement**: Five stack-agnostic levers for pipeline economy — concurrency-cancel-in-progress, change-scoped job gating, aggregation-required-gate, draft-skip of expensive jobs, dependency-cache. Materializes P12 in the CI domain.

**Principle alignment**: P12 (Shared-Resource Pre-flight) — CI minutes are a finite, serialized, shared resource; these levers are bootstrap defaults, not post-incident retrofit. Pairs with the infra-cost-ledger.

**Specification + runnable templates**: the executable reference implementation (the five lever templates + a dual-dimension cost-ledger template) lives in the **SliceOps toolkit** repo under `templates/`. The *pattern* here is Layer B.2 (vendor-agnostic); each concrete CI-provider instance is Layer C.2 (adopter-defined).

**Anti-patterns** (summary; full list in the toolkit templates): `$0` default spending limit (invisible hard-cut), token-only cost-ledger (infra-cost blindness), scaling parallelism without enumerating shared resources, guardrails patched post-incident.

---

## Adopter rule

Layer B.2 patterns are vendor-/stack-agnostic. The concrete instantiation per stack/CI-provider is **Layer C.2** (the adopter defines and enforces it with their own tooling). Adopters reaffirm the industry-canonical patterns as non-optional and instantiate the two SliceOps-formalized ones for their stack.
