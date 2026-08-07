# Universal Decision Dimensions - Layer B.1

Universal Decision Dimensions are the generic analysis axes every non-trivial slice considers before applying stack-specific patterns.

They exist to keep SliceOps ordered from general to specific:

1. Universal software/product forces.
2. Accepted adopter decisions.
3. Domain and slice-specific constraints.
4. Stack Pattern Packs.
5. Concrete implementation.

The dimensions are vendor-neutral and language-neutral. Backend, frontend, data, infrastructure, UX, security, compliance, testing, operations, reliability, maintainability, and delivery all map to them.

## Operating rule

Do not start from a technology or pattern. Start from the forces.

For example:

- Do not start with "microservice"; start with ownership, deployment, consistency, scale, and operational maturity.
- Do not start with "Redux"; start with state ownership, data freshness, sharing scope, mutation flow, and UI complexity.
- Do not start with "cache"; start with latency, freshness, invalidation, consistency risk, and cost.
- Do not start with "AKS"; start with deploy/runtime constraints, operating maturity, scaling model, and failure modes.
- Do not start with "new UI library"; start with usability, accessibility, design-system ownership, state boundaries, bundle/runtime cost, and migration.
- Do not start with "major dependency upgrade"; start with compatibility, vendor risk, security need, rollout, and rollback.
- Do not start with "retry"; start with reliability target, idempotency, failure mode, timeout budget, and user recovery.
- Do not start with "config file"; start with environment differences, secret/config ownership, validation, portability, and rollback.
- Do not start with "just format the date"; start with timezone, locale, currency, calendar, sorting, and storage semantics.

## Materiality rule

Universal dimensions are mandatory to consider, not mandatory to expand in full.

Every non-trivial slice classifies each relevant dimension with the smallest adequate level:

| Level | Meaning | Expected treatment |
|---|---|---|
| `N/A` | The dimension does not affect this slice | Mark it and move on |
| `low` | Local concern handled by accepted defaults | Brief note or normal evidence is enough |
| `material` | The dimension affects design, evidence, rollout, or review | Record rationale, selected path, rejected alternative when useful, and evidence |
| `DEC-required` | The dimension changes an accepted decision, ownership boundary, runtime, security/compliance/auditability posture, reliability target, compatibility guarantee, or critical dependency | Stop for human disposition or create/update a DEC |

Use a light analysis for small conforming slices, a focused analysis for slices with one or more material dimensions, and a full analysis for slices with `DEC-required`, `conflicts`, `exception`, or `revisit` classification.

## The dimensions

| Dimension | Core question | Backend examples | Frontend examples | Evidence examples |
|---|---|---|---|---|
| Business capability | What business outcome or capability is touched? | Order creation, billing, identity, evidence export | Stage board, DEC viewer, checkout flow | Capability reference, acceptance criteria |
| Domain model and invariants | What business rules, terms, and state transitions must stay true? | aggregate invariants, validation rules, workflow states | form rules, wizard state, user-visible domain language | TDD tests, acceptance criteria, glossary/DEC reference |
| Ownership boundary | Who owns this behavior and data? | Module/service/team boundary | Feature area, route, design system ownership | DEC/ARC reference, owner in profile |
| User interaction | How does a human or external actor experience this? | API consumer contract, support workflow | UX states, forms, navigation, accessibility | User-visible tests, UX acceptance criteria |
| Usability and accessibility | Can the intended user complete the flow reliably and inclusively? | support/operator flow, API ergonomics, documentation clarity | keyboard flow, screen reader semantics, responsive layout, form UX | accessibility checks, UX acceptance criteria, usability notes |
| Localization and temporal correctness | Do language, locale, time, currency, and regional rules affect correctness? | timezone storage, currency precision, collation, regional rules | date/number formatting, translated copy, RTL/layout, locale-aware validation | locale tests, timezone tests, content review |
| State ownership | Where does mutable state live and who may change it? | DB aggregate, cache, queue, session | local state, server state, global client state | State model, tests for transitions |
| Data ownership | Who owns persisted data and its lifecycle? | schema, aggregate, service database | API DTOs, cached server data | migration plan, contract tests |
| Data quality and lineage | How trustworthy, complete, and traceable is the data being used or produced? | source of truth, validation, dedupe, import/export lineage | stale display risk, client-side validation, source labels | data-quality tests, lineage note, reconciliation evidence |
| Consistency and freshness | How fresh/consistent must the result be? | transaction, eventual consistency, read model | stale data tolerance, refetch/invalidation | consistency rationale, idempotency tests |
| Concurrency and coordination | What can happen simultaneously, and what must be serialized or deduplicated? | locks, idempotency keys, optimistic concurrency, queue workers | double-submit, request cancellation, optimistic UI, stale responses | race-condition tests, idempotency tests, concurrency rationale |
| Boundary and contract | What contract crosses a boundary? | REST endpoint, event, SDK adapter | component props, API response, route params | schema, DTO, contract test |
| Compatibility and versioning | What existing consumers, data, clients, or contracts must keep working? | API versioning, event schema evolution, DB migrations | browser support, route compatibility, typed API changes | compatibility tests, migration plan, deprecation note |
| Error and recovery | What can fail and how is it recovered? | retry, DLQ, compensation, ProblemDetails | loading/error/empty states, retry UI | error-path tests, runbook |
| Security and privacy | What must be protected? | auth, authorization, secrets, PII | permission states, sensitive UI data | security scan, auth tests |
| Compliance and policy | Which external or internal rules constrain the implementation? | audit logging, retention, data residency, regulatory controls | consent, accessibility policy, privacy notices | compliance checklist, audit trail, waiver |
| Auditability and traceability | Can the important action be reconstructed later? | audit log, actor/action/resource, provenance chain | user action attribution, support-visible history | audit-log tests, provenance evidence, trace sample |
| Observability | How will we understand behavior in production? | logs, metrics, traces, correlation IDs | client telemetry, user-impact metrics | dashboard/alert/log evidence |
| Reliability and availability | What service level or degraded behavior is required? | SLO, timeout budget, circuit breaker, health model | offline/degraded UI, retry affordance, cached fallback | SLO/error-budget note, failure test, health/smoke evidence |
| Performance and scale | What load, latency, or footprint matters? | SQL plan, queue depth, p95/p99, memory | render cost, list size, bundle size | benchmark, profile, plan evidence |
| Feedback strategy | What feedback should exist before or during implementation? | TDD for domain rules, contract-first for APIs/events, characterization tests for refactors | behavior-first component tests, contract-first API types, acceptance-first user flows | failing-first test, acceptance test, contract test, characterization test |
| Testability | What proof gives confidence? | unit/integration/contract/e2e mix | RTL/MSW/E2E visible behavior tests | CI results, coverage rationale |
| Maintainability and complexity | How much change cost or cognitive load does this add? | coupling, cohesion, abstraction depth, module boundaries | component boundaries, hook complexity, design-system fit | review notes, complexity rationale, refactor plan |
| Configuration and environment | Which runtime/build/config assumptions must hold across environments? | env vars, options validation, secrets, container/runtime differences | build-time env, CSP, browser/device constraints | config validation, environment matrix, startup/smoke evidence |
| Operability | How is this deployed, rolled back, and supported? | health checks, migration order, smoke tests | feature flags, rollout, browser support | deploy plan, rollback, smoke test |
| Rollout and adoption | How will the change reach users safely? | migration order, feature flag, canary, rollback | progressive release, browser matrix, user-facing migration | rollout plan, smoke test, adoption metric |
| Cost and shared resources | What finite resources are consumed? | CI minutes, API quotas, DB locks, cloud spend | bundle/runtime cost, API call volume | cost-ledger, caps, alerts |
| Dependency and vendor risk | What third-party or platform dependency becomes more important? | library/runtime/cloud service lock-in, SLA | UI library, auth SDK, analytics SDK | dependency review, license/security check, exit plan |
| Documentation and developer experience | What must future maintainers know to use or change this? | runbook, API doc, local setup, codegen workflow | Storybook/example, component docs, typed contract usage | docs diff, onboarding test, examples |
| Evolution | What would make today's decision wrong later? | service extraction trigger, outbox backlog | state management trigger, design-system split | revisit triggers, InsightRecords |

## Generic triage order

For every non-trivial slice:

1. Name the business capability.
2. Load accepted decisions and the adopter technical profile.
3. Walk the universal dimensions that are relevant to the slice, starting with domain rules and invariants when behavior is being changed.
4. Classify dimensions as `N/A`, `low`, `material`, or `DEC-required`.
5. Choose the feedback strategy: acceptance-first, TDD/test-first, contract-first, characterization-first, integration-first, or justified test-after.
6. Only then load Stack Pattern Packs that map to those material dimensions.
7. Select the adequate path and rejected alternatives.
8. Define evidence, rollout/adoption needs, documentation needs, and revisit triggers.

## Backend mapping

Backend decisions commonly emphasize:

- Ownership boundary.
- Domain model and invariants.
- Data ownership.
- Data quality and lineage.
- Consistency and freshness.
- Concurrency and coordination.
- Boundary and contract.
- Compatibility and versioning.
- Error and recovery.
- Security and privacy.
- Compliance and policy.
- Auditability and traceability.
- Observability.
- Reliability and availability.
- Operability.
- Performance and scale.
- Feedback strategy.
- Maintainability and complexity.
- Dependency and vendor risk.
- Rollout and adoption.

These dimensions map to choices such as monolith vs modular monolith vs microservices, sync vs async, Outbox, Saga, CQRS, EF Core vs SQL, API design, cloud hosting, and resilience.

## Frontend mapping

Frontend decisions commonly emphasize:

- User interaction.
- Usability and accessibility.
- Localization and temporal correctness.
- State ownership.
- Domain model and invariants.
- Boundary and contract.
- Compatibility and versioning.
- Consistency and freshness.
- Concurrency and coordination.
- Reliability and availability.
- Error and recovery.
- Security and privacy.
- Performance and scale.
- Feedback strategy.
- Testability.
- Maintainability and complexity.
- Configuration and environment.
- Dependency and vendor risk.
- Rollout and adoption.
- Evolution.

These dimensions map to choices such as local state vs context vs client store vs server-state library, form strategy, API typing, loading/error/empty states, accessibility evidence, route design, component composition, and rendering optimization.

## Data mapping

Data decisions commonly emphasize:

- Data ownership.
- Domain model and invariants.
- Data quality and lineage.
- Localization and temporal correctness.
- Consistency and freshness.
- Concurrency and coordination.
- Compatibility and versioning.
- Performance and scale.
- Security and privacy.
- Compliance and policy.
- Auditability and traceability.
- Operability.
- Rollout and adoption.
- Evolution.

These dimensions map to choices such as schema design, migration strategy, indexing, transaction boundaries, retention, auditability, data export, and cache invalidation.

## Infrastructure mapping

Infrastructure decisions commonly emphasize:

- Operability.
- Security and privacy.
- Compliance and policy.
- Auditability and traceability.
- Observability.
- Reliability and availability.
- Cost and shared resources.
- Concurrency and coordination.
- Dependency and vendor risk.
- Error and recovery.
- Rollout and adoption.
- Documentation and developer experience.
- Configuration and environment.
- Evolution.

These dimensions map to choices such as hosting runtime, deployment strategy, secret management, identity, scaling policy, smoke tests, rollback, monitoring, and budget caps.

## Review levels

Not every dimension needs a DEC. Use the smallest adequate review level:

| Review level | Use when |
|---|---|
| Slice rationale | The choice conforms to accepted decisions and has local impact |
| Checklist | The choice follows a stack pack and needs reviewer confirmation |
| Validator | The rule is deterministic enough to automate |
| DEC | The choice changes architecture, data ownership, runtime/configuration model, reliability target, auditability requirement, security posture, compatibility guarantees, compliance posture, vendor dependency, or accepted team decisions |
| Superseding DEC | The choice replaces or contradicts a prior accepted decision |
| HITL block | The agent cannot safely choose without owner authority |

## Feedback strategy

For feedback-style selection, use [`testing-feedback-selection.md`](testing-feedback-selection.md). TDD is first-class but not mandatory for every slice: choose it when rule-level or state-transition feedback is the earliest useful proof. Prefer acceptance-first when the slice outcome is externally visible and a single executable acceptance criterion can anchor scope and close evidence.

## Anti-patterns

- Loading a stack pack before understanding the universal forces.
- Treating backend architecture as the only architecture.
- Treating frontend as "just UI" with no state, contract, security, testability, or evolution decisions.
- Treating cloud/runtime choice as an implementation detail without operability and cost analysis.
- Treating accessibility, compatibility, compliance, rollout, or dependency risk as implementation details outside the decision.
- Treating reliability, auditability, data quality, or environment/configuration assumptions as afterthoughts.
- Adding abstraction for "maintainability" without naming the concrete change pressure it reduces.
- Letting a best-practice pack override the owning team's accepted decision.
