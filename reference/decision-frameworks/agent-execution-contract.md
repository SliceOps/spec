# Agent Execution Contract - Decision-Aware Generation

This Layer B.1 contract defines how an AI agent turns SliceOps decision analysis into code generation behavior.

It does not prescribe a stack, language, vendor, architecture, or methodology. It prescribes the minimum operating discipline that keeps generated output aligned with the adopter's decisions, current slice forces, and evidence gates.

## Purpose

Decision Frameworks improve generation only when the agent consumes them before and during implementation. A documented framework that is not routed into the generation loop is only advisory.

This contract makes the loop explicit:

```text
model triage
  -> context routing
  -> accepted decision load
  -> universal technical triage
  -> stack pack routing
  -> implementation binding
  -> code generation
  -> evidence gate
  -> learning/revisit capture
```

## Scope

This contract applies to non-trivial slices: any slice that changes runtime behavior, API/contract shape, data, security, compliance, architecture, infrastructure, user workflow, testing strategy, dependency posture, rollout, or operational support.

Trivial slices may use a light path when they only change spelling, formatting, comments, or generated content with no behavioral, runtime, data, security, compatibility, or delivery impact.

## Authority Order

The agent must resolve technical direction in this order:

| Order | Source | Agent obligation |
|---|---|---|
| 1 | Layer A principles | Never violate decision integrity, audit, HITL, evidence, security, or context discipline |
| 2 | Explicit human instruction in the current slice | Treat as binding unless it conflicts with Layer A or accepted adopter decisions |
| 3 | Accepted adopter decisions/profile | Treat as implementation authority |
| 4 | Current codebase reality | Preserve local architecture and conventions unless a decision says to change them |
| 5 | Universal Decision Dimensions | Identify material forces before stack-specific guidance |
| 6 | Stack Pattern Packs | Apply only when routed by material forces and accepted decisions |
| 7 | Agent recommendation | Suggest, justify, and record; never silently override |

If explicit human instruction conflicts with an accepted adopter decision, the agent must surface the conflict and ask for human disposition or a superseding DEC. It must not silently choose either side.

## Required Generation Loop

### 1. Session and Model Triage

Before code generation, the session records:

- `model_used`
- `execution_mode`
- `context_orientation`
- `triage_rationale`

Model Triage chooses execution capability. It does not choose architecture or design. Technical choice still goes through Decision Frameworks.

### 2. Context Routing

The agent loads the smallest adequate context set:

- Slice scope and acceptance criteria.
- Relevant foundation/architecture/decision records.
- Adopter Technical Decision Profile, when present.
- Touched code and local conventions.
- Prior InsightRecords/LearningPatterns for similar work.

Stack Pattern Packs are not loaded yet unless they are needed to understand already accepted stack decisions. Specific packs are routed after the universal triage.

### 3. Relationship Classification

The slice is classified before implementation:

- `conforms`
- `extends`
- `new-decision`
- `conflicts`
- `exception`
- `revisit`

`new-decision`, `conflicts`, `exception`, and `revisit` require `full` analysis depth and human/DEC disposition before the conflicting or decision-changing implementation lands.

### 4. Universal Materiality Pass

The agent evaluates the Universal Decision Dimensions and marks each relevant force:

- `N/A`
- `low`
- `material`
- `DEC-required`

The pass may be compact, but it must happen before stack-specific pattern selection. This prevents pattern-first generation.

### 5. Feedback Strategy Selection

The slice selects one feedback strategy:

- `acceptance-first`
- `TDD/test-first`
- `contract-first`
- `characterization-first`
- `integration-first`
- `test-after with rationale`

The chosen strategy must match the slice risk. For example:

- Use `TDD/test-first` when domain rules, algorithms, edge cases, or refactoring confidence dominate.
- Use `contract-first` when API, event, SDK, generated client, or cross-team boundaries dominate.
- Use `characterization-first` when changing poorly understood legacy behavior.
- Use `integration-first` when framework, database, queue, browser, provider, or deployment behavior is the main risk.
- Use `test-after with rationale` only for low-risk or constrained work, and record why earlier feedback was not adequate.

### 6. Stack Pack Routing

Only after universal forces are marked does the agent load Stack Pattern Packs.

A pack is routed when:

- its category/language/framework/vendor matches the touched implementation area, and
- at least one material or low universal dimension explains why it is relevant, and
- it does not conflict with an accepted adopter decision.

A pack must not be loaded merely because it is familiar, available, or fashionable.

### 7. Implementation Binding

Before or during implementation, each material force must be bound to a concrete artifact:

| Material force | Binding examples |
|---|---|
| Domain invariant | Unit test, domain model, validation rule |
| API/contract | DTO/schema, contract test, versioning note |
| Data quality/lineage | migration, reconciliation check, audit field |
| Concurrency/coordination | idempotency key, lock/queue choice, race test |
| Security/compliance | authorization test, policy check, sensitive-field review |
| Accessibility/usability | keyboard path, labels, responsive state evidence |
| Observability/reliability | log/metric/trace, timeout/fallback test |
| Rollout/migration | flag, rollback step, compatibility test |

If a material force has no implementation or evidence binding, the slice is incomplete.

### 8. Code Generation

The agent generates code under these constraints:

- Preserve accepted decisions and existing local architecture.
- Use the smallest adequate abstraction.
- Prefer local conventions over generic best practices.
- Apply stack packs only where routed.
- Keep unrelated refactors out of the slice.
- Do not introduce distributed architecture, global state, generic repositories, CQRS, eventing, cloud services, adapters, factories, or patterns without the forces that justify them.
- When the selected path is uncertain, choose the reversible, lower-complexity path and record the revisit trigger.

### 9. Evidence Gate

Before closure, the agent runs or records the relevant evidence:

- tests
- linters/formatters
- type checks
- contract/schema checks
- migration checks
- security/dependency checks
- accessibility or UX evidence
- observability/reliability evidence
- rollout/docs/runbook evidence

Evidence must correspond to the selected feedback strategy and the material dimensions.

### 10. Learning and Revisit Capture

The slice records:

- rejected alternatives and revisit triggers for material choices
- new InsightRecords/LearningPatterns when implementation evidence changes the original assumption
- DEC updates when a repeated exception becomes a durable pattern

## Non-Negotiable Gates

The following are generation blockers for non-trivial slices:

1. No classification before implementation.
2. No materiality pass before Stack Pattern Pack selection.
3. No accepted-decision conflict implemented without HITL or superseding DEC.
4. No `DEC-required` dimension implemented as a normal conforming slice.
5. No material dimension without evidence or implementation binding.
6. No Stack Pattern Pack loaded without category/path/rationale.
7. No TDD claim without failing-first or test-first evidence.
8. No `test-after with rationale` without the rationale.
9. No pattern-first generation when the universal forces are absent.
10. No explanation substituted for runnable or reviewable evidence when such evidence is feasible.

## Light Path

For low-risk conforming slices:

```text
classification: conforms
analysis depth: light
material dimensions: none
feedback strategy: acceptance-first or test-after with rationale
stack packs: none or one directly relevant pack
evidence: normal project checks
```

The light path is still a path. It is not permission to skip decision awareness.

## Full Path

Use the full path when:

- the slice changes an accepted decision
- the slice conflicts with a decision
- a scoped exception is needed
- evidence suggests a decision should be revisited
- any dimension is `DEC-required`
- security, compliance, auditability, reliability target, compatibility guarantee, ownership, runtime/configuration model, or critical dependency posture changes

The full path produces or updates a DEC, waiver, or review item before implementation is treated as complete.

## Conformance Summary

A generated slice is decision-aware when it can answer:

1. What accepted decisions were loaded?
2. What relationship does the slice have to those decisions?
3. Which universal dimensions mattered?
4. Which stack packs were loaded because of those dimensions?
5. Which path was selected, and why is it adequate now?
6. What alternatives were rejected?
7. What evidence proves the path?
8. What would make this decision wrong later?

If those answers are absent, the output may still compile, but it is not solid SliceOps output.
