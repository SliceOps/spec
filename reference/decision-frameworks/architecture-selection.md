# Architecture Selection Decision Framework - Layer B.1

This framework helps an adopter choose an architecture path without defaulting to the most complex option.

The decision is always scoped to the adopter's accepted technical decisions and business constraints. This document supplies the analysis structure; it does not override the owning team's decisions.

## Inputs

Load these before recommending architecture:

- Product foundations and constraints.
- Accepted architecture DECs.
- Current module/service boundaries.
- Team size and ownership model.
- Deployment and release pain.
- Compatibility, versioning, and migration constraints.
- Data ownership and consistency needs.
- Data quality, lineage, and auditability needs.
- Concurrency, coordination, and idempotency needs.
- Maintainability and cognitive-load constraints.
- Observability, reliability, and operational maturity.
- Configuration, environment, and portability constraints.
- Security, compliance, and sensitivity requirements.
- Dependency/vendor risk and hosting lock-in tolerance.
- Rollout, rollback, and adoption constraints.
- Evidence from incidents, retrospectives, and repeated exceptions.

## Default posture

Prefer the simplest architecture that satisfies current forces and keeps a clear evolution path.

The default is not "microservices." The default is adequate modularity with explicit revisit triggers.

## Option matrix

| Option | Use when | Avoid when | Evidence required |
|---|---|---|---|
| Simple monolith | Product is small, domain is simple, team is small, deployment unit is not a bottleneck | Domain already has strong internal boundaries or release coordination is painful | Tests around core flows, basic observability/reliability, clear module naming, migration path if boundaries emerge |
| Modular monolith | Domain is evolving but has emerging capabilities; team wants boundaries without distributed-system cost | Independent deployment or scale pressure is already real and recurring | Module boundaries, dependency rules, integration tests, decision record for boundaries, compatibility rules |
| Microservices | Bounded contexts are stable, teams own services independently, independent deploy/scale is necessary, distributed observability/reliability exists | Domain is unclear, team is small, transactional consistency dominates, ops maturity is low | Service boundary DEC, data ownership plan, contract tests, observability, reliability target, rollout/rollback plan, failure-mode analysis |
| Event-driven workflow | Work is long-running, side effects are decoupled, multiple consumers exist, availability coupling should be reduced | Caller needs immediate committed result or idempotency/observability cannot be implemented | Event contract, idempotency tests, retry/DLQ policy, correlation propagation |
| CQRS | Read and write models have materially different shape/performance needs | CRUD is simple or split adds only ceremony | Query model rationale, consistency expectation, tests for read/write behavior |
| Outbox | Local state is persisted and an integration event/message must be published reliably | No external event/message is published, or a DEC accepts loss/compensation risk | Transaction test, publisher worker evidence, duplicate-consumer idempotency evidence |
| Saga | A business process spans multiple services/resources and requires compensating actions | A single local transaction is enough | Step map, compensation plan, idempotent handlers, retry/DLQ evidence, observability |

## Decision flow

1. Start from the accepted adopter default.
2. Identify whether the slice changes a boundary, persistence model, deployment unit, consistency model, data-quality/auditability model, concurrency/coordination model, reliability target, configuration/environment model, compatibility guarantee, dependency posture, or rollout model.
3. If no material boundary changes, implement inside the accepted architecture.
4. If new forces appear, classify the slice as `extends`, `new-decision`, `conflicts`, or `revisit`.
5. For `new-decision`, `conflicts`, or `revisit`, create or propose a DEC before implementing the new architecture path.
6. Attach evidence and revisit triggers.

## Microservice extraction triggers

A module may be a candidate for extraction only when evidence accumulates. Typical triggers:

- It changes independently for three or more blocks.
- Release coordination with other modules repeatedly blocks delivery.
- It has distinct latency, scale, availability, or compliance requirements.
- It has distinct auditability, data-quality, configuration, or reliability requirements.
- A separate team owns it end-to-end.
- Its data ownership boundary is stable and explicit.
- Contract testing and distributed observability are ready.
- Rollout, rollback, compatibility, and support ownership are ready.

If these are not true, prefer a module boundary inside the current deployment unit.

## Example classification

Scenario: adding a new `Billing` capability to a product whose accepted decision is modular monolith.

Decision-aware result:

- Classification: `conforms` or `extends`.
- Selected path: new module inside the modular monolith.
- Rejected path: new Billing microservice.
- Reason: boundary may be emerging, but independent team ownership and deploy pressure are not yet evidenced.
- Revisit triggers: Billing changes independently for three blocks, billing release coordination blocks other work, or billing requires a separate compliance/scale profile.

## Anti-patterns

- Extracting a service because the concept has a noun.
- Choosing distributed architecture before the team can observe and operate it.
- Using CQRS/eventing to compensate for unclear domain modeling.
- Treating a temporary workaround as a permanent architecture.
- Treating migration, compatibility, rollout, or support cost as details to solve after the architecture is chosen.
- Treating auditability, reliability, data quality, or configuration drift as details to solve after the architecture is chosen.
- Ignoring accepted adopter decisions in favor of generic best-practice advice.
