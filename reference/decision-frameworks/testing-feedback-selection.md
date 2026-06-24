# Testing Feedback Selection - Layer B.1

This framework decides how a slice gets fast, deterministic feedback before implementation details dominate.

It is generic: it applies to backend, frontend, data, infrastructure, CLI, generated code, and documentation/tooling slices. Stack-specific test tools live in Layer C.2 Stack Pattern Packs.

## Relationship to TDD and acceptance-first

SliceOps is development-style-agnostic: adopters may use TDD, acceptance-first, contract-first, spec-first, characterization-first, or a mixed style.

SliceOps's preferred default is **acceptance-first slices** because one executable acceptance artifact can anchor scope at the start and close evidence at the end. TDD remains a first-class option, especially for business rules, algorithms, state transitions, and refactors where the feedback loop should be unit-level and very fast.

The rule:

> Choose the feedback style that proves the slice's risk earliest, with the smallest deterministic evidence that still protects the behavior.

## Feedback styles

| Style | Use when | Avoid when | Typical evidence |
|---|---|---|---|
| Acceptance-first | The slice has user/API/operator-visible behavior and a clear done condition | The change is a tiny internal refactor with no external behavior | Executable acceptance/integration test, E2E for critical flow |
| TDD / test-first | The slice changes business rules, algorithms, validation, state transitions, or domain behavior | The code is mostly glue/config and unit seams would be artificial | Failing unit test first, implementation, passing test, refactor |
| Contract-first | A boundary is the primary risk: API, event, schema, component props, SDK adapter | The contract is not yet known and exploration is the slice | Contract/schema test, generated types, compatibility evidence |
| Characterization-first | Existing behavior is unclear but must be preserved during refactor | Greenfield behavior is being invented | Tests that capture current behavior before change |
| Integration-first | The risk is wiring: DI, middleware, DB, auth, serialization, queue, cloud resource | Pure business logic can be isolated cheaper | Integration test, container/fake/sandbox evidence |
| Test-after with rationale | Spike/prototype, documentation-only change, or deterministic validator covers the risk | Behavior or risk is known before coding | Written rationale plus follow-up evidence before merge |

## TDD loop

When TDD is selected, the slice records:

1. The behavior/rule being protected.
2. The first failing test or expected failure.
3. The minimal implementation that makes it pass.
4. The refactor step, if any.
5. The evidence command/output in CI or local verification.

TDD is not "write tests sometime before merge." It is a feedback loop: red -> green -> refactor.

## Selection questions

Before coding, answer:

- What is the main risk of this slice?
- Is the risk business behavior, domain invariant, state transition, data quality, concurrency, boundary contract, integration wiring, UI behavior, accessibility, localization/time/region, compatibility, auditability, reliability, performance, security, compliance, configuration, dependency risk, rollout, documentation, or migration safety?
- Can the risk be expressed as an executable test before implementation?
- Is unit-level feedback enough, or must the real pipeline/boundary be exercised?
- Is current behavior unknown and therefore needs characterization?
- What evidence will close the slice?

## Generic mapping

| Slice risk | Preferred feedback |
|---|---|
| Business invariant or state transition | TDD/unit test-first |
| Data quality, lineage, or reconciliation | Characterization-first for existing behavior; integration/contract-first for external sources |
| Concurrency, idempotency, or race condition | TDD/unit test-first when isolated; integration/concurrency test when boundary-dependent |
| API behavior and error shape | Acceptance/integration-first |
| Event/message/schema compatibility | Contract-first |
| Refactor of legacy/unclear behavior | Characterization-first |
| Middleware, DI, auth, EF query, queue, cloud wiring | Integration-first |
| Critical user journey | Acceptance-first plus small E2E |
| Visual/component behavior | Frontend behavior test first when practical |
| Accessibility requirement | Accessibility check plus visible behavior test |
| Localization, timezone, currency, or regional correctness | Locale/timezone test plus visible behavior or domain test |
| Audit trail or provenance requirement | Contract/integration test plus audit-log/provenance evidence |
| Reliability, fallback, timeout, or degraded mode | Integration/failure-path test plus smoke/health evidence |
| Backward compatibility or deprecation | Contract-first plus compatibility/migration test |
| Compliance or policy requirement | Policy checklist plus targeted test/scan evidence |
| Configuration or environment behavior | Startup/config validation plus environment-matrix smoke evidence |
| New third-party dependency | Dependency review plus integration/smoke evidence |
| Migration or deploy safety | Dry-run/rollback/smoke evidence |
| Documentation/tooling behavior | Runnable example, validator, or documented command evidence |

## Evidence rules

- A slice may choose any style, but it must declare the style and evidence.
- If test-after is chosen for a behavior-changing slice, the slice must justify why earlier executable feedback was not practical.
- Evidence must be deterministic enough to re-run.
- Tests should protect behavior and contracts, not private implementation details.
- Mock external boundaries when the boundary is not the risk; exercise real-ish boundaries when the boundary is the risk.
- Non-test evidence is valid when it directly proves the risk: accessibility scan, migration dry-run, audit-log sample, SLO/health evidence, config validation, dependency audit, policy checklist, runbook, or executable docs example.

## Revisit triggers

Reopen the feedback strategy when:

- Regressions escape tests.
- Tests are flaky or block merges without signal.
- Tests pass but integration fails.
- Accessibility, compatibility, compliance, or rollout defects escape the selected evidence.
- Data quality, auditability, reliability, or configuration defects escape the selected evidence.
- A pattern of test-after justifications repeats.
- TDD tests become coupled to private implementation and slow refactoring.
- Acceptance tests become too broad or expensive for normal slice flow.

## Anti-patterns

- Claiming TDD while writing tests after implementation.
- Requiring TDD for every slice regardless of risk.
- Using only unit tests when the risk is the HTTP/DB/auth/message boundary.
- Using only E2E tests for business rules that can be tested cheaply.
- Mocking every internal class and proving interactions instead of behavior.
- Treating coverage percentage as evidence by itself.
