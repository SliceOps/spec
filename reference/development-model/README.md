# Development Model — SliceOps™ (Layer B.1)

The canonical answer to "what kind of development model is SliceOps?" — and how it relates to spec-first / test-first / contract-first authoring styles. SliceOps IP, CC BY 4.0.

Three characterizations, all derived from the canonical principles — none of them adds a new Layer A principle (anti-over-promotion discipline applies):

1. **Decision-driven and evidence-gated** (not spec-driven-first).
2. **Development-style-agnostic** (analog to P8 Platform-Agnostic, applied to input/authoring style).
3. **Acceptance-first slices** as the **preferred convention** (Rails-style: opinionated default, override permitted).

---

## 1. Decision-driven and evidence-gated, NOT spec-driven-first

The **driver** of SliceOps is the slice (atomic unit), and the **canonical differentiating artifact** is the decision (DEC, audit plane). The spec is **a component** of the slice (P1: "spec, decision, code, tests, evidence, and merge") — co-equal, not sovereign.

| Dimension | Spec-driven-first | SliceOps |
|---|---|---|
| Source of truth | The spec (canonical, immutable) | The corpus of decisions and merged code with evidence |
| Primary artifact | Spec document | DecisionRecord (audit plane) |
| What is audited | Conformance code ↔ spec | Integrity of the decisions (what / why / who) |
| Flow | spec → plan → code → conformance | slice scope (spec-anchor) → execution → decisions captured → evidence-gated → merge → learning |
| When spec and reality diverge | A bug (code must conform) | A recorded decision (why it changed — the change IS valuable) |
| Relationship with learning | Spec assumes correctness upfront | P7: you learn during execution; the spec evolves |

### Why NOT spec-driven-first (tension with P7)

Spec-driven-first assumes the **spec is correct upfront**, code conforms, divergence = bug. This is in **direct tension with P7 (Recursive Learning)**: SliceOps assumes you learn during execution, the spec can evolve, and **the decision of why it changed IS the valuable artifact**. A rigid immutable spec contradicts the audit plane (which captures evolution of decisions, not static conformance) and P7. Forcing SliceOps to be spec-driven-rigid would break it conceptually.

### Where it DOES use specs ("spec-anchored", ≠ spec-driven)

- **P1**: every slice carries a spec as its first element (anchors scope, prevents drift) — co-equal with decision/evidence, not sovereign.
- **Scope declaration** in the slice template = a mini-spec per slice.
- **The framework itself** has a versioned spec (this very document tree) — but that is the spec of the framework, not spec-driven-development per project.

**"Spec-anchored"** = the spec anchors the slice. **"Spec-driven"** = the spec is the driver and source of truth. SliceOps is the first, not the second.

---

## 2. Development-style-agnostic (analog to P8)

Spec-driven is an **input/authoring style**; SliceOps is a **discipline plane** that wraps any style. Analog to P8 (Platform-Agnostic) but for development-style instead of tools:

- An adopter can be **spec-first AND SliceOps-compliant**: a spec-first toolchain handles spec to code; SliceOps adds audit plane, slice atomicity, evidence, and recursive learning **on top**.
- Or **test-first AND SliceOps**, or **contract-first AND SliceOps**, or **sketch-first AND SliceOps**.
- The 12 principles **do not prescribe an input style** — they prescribe the discipline plane (auditable decisions, atomic slices, gated evidence, captured learning).

### Competitive implication (positioning)

SliceOps **does not compete** with spec-first / contract-first toolchains — it **wraps** them. Messaging: *"Use your preferred authoring flow to go from intent to code; use SliceOps to make the whole process auditable, atomic, and self-improving."* Consistent with the pattern established elsewhere (SliceOps operates on top of code-quality, runtime governance, compliance, and CI tools — now also on top of authoring-flow tools on the input axis).

**Documentation status**: development-style-agnostic is documented as a **characterization** (it derives from the spirit of P8 and the framework's composable nature), NOT as a new Layer A principle. Re-evaluable if the need to elevate it recurs.

---

## 3. Acceptance-first slices — preferred convention

Convention-over-configuration (Rails-style): SliceOps is style-agnostic in capability but declares an **opinionated default**.

### The preferred default

**Acceptance-first slices**: each slice declares its **acceptance criteria upfront** — ideally as **executable acceptance tests** — that serve simultaneously as:
- **Spec-anchor** (P1 scope): the acceptance test defines the expected outcome of the slice.
- **Evidence-gate** (P5 closure): the acceptance test pass IS the evidence that closes the slice.

**A single artifact bridges the start and end of the slice.** This is exactly "complete the back end of the slice": the criterion defined upfront closes the slice at the end when it passes.

### Why acceptance-first as the default

| Style | Spec-anchor (start) | Evidence-gate (end) | Bridges start ↔ end |
|---|---|---|---|
| Spec-first (prose) | ✅ strong | ✗ requires separate spec→test mapping | No — leaves a gap |
| Test-first / TDD (unit) | partial | ✅ but unit granularity, not slice | Partial — sub-slice |
| **Acceptance-first** | ✅ test defines expected | ✅ test pass = evidence | **Yes — one artifact** |
| Type/contract-first | ✅ for API surface | partial | API only |

It also reinforces:
- **Determinism-over-Regeneration** (B.2): acceptance tests are deterministic (same input gives same result).
- **P2 Audit Plane**: the acceptance test is part of the audit trail.
- **P7 Recursive Learning**: acceptance criteria can evolve; the change is captured as a decision (not as spec-rigidity).

### Convention, NOT mandate

It is a **recommended default with override permitted**. An adopter may use prose-first, TDD-pure, or any other style and remain SliceOps-compliant if they honor the 12 principles. SliceOps recommends acceptance-first because it best materializes P1, P5, and P7 — but does not require it (development-style-agnostic is preserved, characterization 2).

---

## How this plays back into the slice template

The canonical slice template (`../templates/slice-template.md`) makes acceptance criteria a first-class section, declared upfront — defaulting toward the recommended convention while leaving room to express any style.
