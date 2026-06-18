# R-rules — Layer B.1 (v1.0)

The **R-rules system**: enforced merge gates in CI that validate framework metadata. SliceOps IP (Layer B.1); documentation under CC BY 4.0, code templates under MIT (final terms pending IP/Legal — see `../../governance/IPR_POLICY.md`).

Each R-rule is a **hard gate**: a PR violating any rule does not merge. R1–R14 are the **canonical starter pack** — vendor-neutral, stack-agnostic, adopter-instantiable. Adopters add R15+ for their own stack/domain (Layer C.2). The starter rules trace to canonical principles; an R-rule with no principle backing is a retirement candidate.

## Files

- [`r1-r14-starter.md`](r1-r14-starter.md) — the 14 canonical starter rules (statement · rationale · principle · check pattern · allowlist · instantiation note)
- [`layer-3-validators.md`](layer-3-validators.md) — consistency-management Layer 3 CI validator specs (Phase 2 and 3) and the counter-discipline / counter-atomicity pattern (P9)

## How adopters instantiate

1. Copy the starter pack into the adopter repo's CI.
2. Bind each rule's abstract check to the adopter's stack (grep patterns, schema validators, language linters).
3. Add adopter-specific R15+ rules (Layer C.2) for stack patterns.
4. R-rule amendments require a DEC citing a LearningPattern as evidence (P8).

## Companion tooling

CI workflow reference implementations (the executable form of these gates) live in the **SliceOps toolkit** repo (`templates/`). The R-rules here are the *specification*; the toolkit provides *runnable starters*.
