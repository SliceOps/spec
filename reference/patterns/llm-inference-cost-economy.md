# LLM-Inference-Cost-Economy — Layer B.2 (sub-domain of CI/Pipeline Cost Economy)

A **specialized sub-domain pattern** of CI/Pipeline Cost Economy. Applies when a CI/CD workflow calls a **paid LLM API** (audit, code-review, QA, codegen, summarization). Adds three genuinely-new levers and refines two parent levers for LLM-specific economics. Vendor-neutral.

SliceOps IP, CC BY 4.0 (docs) and MIT (toolkit reference impl).

**Relationship to parent**: this is a *sub-domain*, not a *standalone B.2*. CI/Pipeline Cost Economy provides the general pipeline-cost levers (concurrency, change-gating, draft-skip, dependency-cache). This sub-domain adds LLM-specific levers (caching, model-tier, diff-only context) and refines two parent levers for LLM-aware behavior. If a workflow does not call a paid LLM API, only the parent applies; if it does, both apply.

---

## Pattern statement

Any CI/CD workflow that calls a **paid LLM API** must satisfy the five disciplines below from day one. Skipping any one produces order-of-magnitude waste that the bill is the only signal to detect.

---

## The five levers — 3 new and 2 refinements

### Lever A (NEW) — Prompt-caching discipline

When a workflow sends a large stable block (system prompt, rubric, rules document, audit checklist) that is identical across runs, that block **MUST** be cached at the API level. Most LLM providers offer a short-TTL caching mechanism (minutes) ideal for PR-iteration bursts.

- Identify the stable block (typically the system / first content block, >5K tokens).
- Mark it cached via the vendor's mechanism (the per-vendor cache directive — every major provider has one).
- Skipping caching on stable blocks >5K tokens typically leaves ~40–60% of the total cost as preventable spend.

**No-cache is only acceptable if**: the block is <2K tokens, or it is a single-shot flow without repetition, or the block changes per call (rare).

### Lever B (NEW) — Model-tier discipline

Direct application of **Determinism-over-Regeneration** to model selection: use the cheapest tier that is **adequate** for the task.

- **Pattern-matching / rule-compliance / format-check** → mid-tier model suffices. Frequently substitutable with a deterministic regex / AST / static analyzer (see Determinism-over-Regeneration).
- **Code-reasoning / architectural critique / final ready-for-review gate** → top-tier model justified.
- **NO top-tier "just in case"** — typically a ~3× cost penalty with no output difference for pattern-match tasks.

**Cost-ledger row** must declare the tier chosen and the justification.

### Lever C (NEW) — Diff-only context windowing

Do NOT send full files when only the diff is needed. Send:
- The diff with limited surrounding context (small N, e.g., 3–10 lines).
- A full file fetch on-demand only when the reasoning requires it.
- NO file-wide context "for more signal" — that is unbounded cost.

Token economy LLM-specific: each KB of extra context is a recurring spend across runs.

### Lever D (REFINEMENT of parent) — Trigger-set minimalism LLM-aware

Refines the parent's `change-scoped job gating` specifically for LLM-in-CI:

- **Default**: PR-trigger on `opened, reopened, ready_for_review` only — **no `synchronize`**.
- `synchronize` fires on every push to a PR branch, leading to N audits per PR for N pushes.
- The effective merge gate is the commit at `ready_for_review`; intermediate-push audits are waste.
- Re-trigger after RFR via close and reopen or draft↔ready toggle.
- Add `synchronize` ONLY with a documented cost-DEC exception.

### Lever E (REFINEMENT of parent) — LLM-aware draft gate (green-not-skipped)

Refines the parent's `draft-skip` for LLM-in-CI: draft PRs are not mergeable, audit is waste — BUT the job must finish **green**, not skipped. Skipped contexts in branch-protection required checks block PRs permanently.

- Initial step detects `draft = true`.
- If draft: set a `skip=true` output, log "draft — audit deferred to ready-for-review", exit 0 (green).
- Subsequent step is conditional: `if: <skip != true>` runs the API call.
- Required check passes (green); no LLM bill.

This differs from the parent's general draft-skip (which is time-economy of CI minutes): here it is **cost-economy of the LLM bill and correctness** of the required-check satisfaction.

---

## Cost-ledger 3rd dimension

The cost-ledger (originally token and infra/CI) gains a **third dimension**: **LLM-API-in-CI cost** — separate because it scales with `velocity × push-frequency × prompt-size`, dynamics distinct from token-throughput and infra-minutes.

| Dimension | Scales with |
|---|---|
| Token cost | Slice throughput (LLM tokens consumed in the development session) |
| Infra/CI cost | CI minutes / compute / serialized lanes |
| **LLM-API-in-CI cost** | PR velocity × push-frequency × prompt-size of CI-time LLM calls |

The pre-Block checklist gains an item: "verify LLM-API-in-CI budget headroom".

---

## Anti-pattern catalog

| ID | Anti-pattern | Failure mode |
|---|---|---|
| AP-1 | Large system prompt without a cache directive | ~50–90% of the cost is preventable recurring spend |
| AP-2 | `synchronize` trigger on a paid-LLM workflow | Cost scales linearly with push count; velocity becomes the cost penalty |
| AP-3 | "I'll tune when I see the bill" | Paid-LLM cost compounds silently; the bill is the only signal |
| AP-4 | Audit of drafts ("real-time dev feedback") | Drafts iterate more and do not merge; audit there is systemic waste |
| AP-5 | Top-tier model "just in case" for pattern-match | A ~3× cost penalty with no quality difference; violates Lever B and Determinism-over-Regeneration |
| AP-6 | Whole-file context when only the diff is needed | Token economy unbounded; spend scales with file size across runs |
| AP-7 | No `concurrency` block | Stacked audits all bill (inherited from parent) |
| AP-8 | Draft-skip via job removal (skipped in CI) | The required-check context becomes "skipped" → the PR is permanently blocked. The gate MUST end green-not-skipped |

---

## Adopter enforcement (Layer C.2 candidate)

Adopters instantiate a Layer C.2 enforcement lint / pre-commit / CI gate that fails if a workflow YAML calls a paid-LLM endpoint without:
- A system / first stable content block with a cache directive (vendor-specific syntax).
- A `pull_request` trigger without `synchronize` (or with a documented `# synchronize-allowed: <exception ref>` comment).
- A `concurrency` block with `cancel-in-progress: true`.
- A draft gate step that ends green-not-skipped.

A canonical R-rule (`R-LLM-CI-COST`) captures the four checks — see `../r-rules/layer-3-validators.md` for the spec and the toolkit for the runnable form.

---

## Mapping to principles

- **P5 (Evidence-by-Construction)** — a cost-ledger row is mandatory per LLM-in-CI workflow at merge time (declared per-run cost estimate and monthly volume estimate; reviewable against real billing).
- **P7 (Recursive Learning by Capture)** — this pattern IS output of the P7 loop (its formalization came from a recurrence of cost-blowup observations across reference implementations).
- **P12 (Shared-Resource Pre-flight)** — LLM API budget = finite shared resource across repos / PRs / authors; the P12 pre-flight checklist includes enumerate, cap, alert, and telemeter LLM-API spend.
- **Determinism-over-Regeneration** — Lever B (model-tier) is a direct application: "cheaper deterministic alternative when adequate" extended to "cheaper model tier when adequate".
