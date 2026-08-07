<!--
Adopter Technical Decision Profile template (Layer B.1 envelope, Layer C.2 content).
Use this in an adopter corpus to bind SliceOps to the team's accepted architecture,
stack defaults, evidence expectations, exceptions, and revisit triggers.
-->

---
entity: CognitiveFramework
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <human/team accountable for architecture>
sensitivity: internal
---

# Adopter Technical Decision Profile - <product/repo/team>

## Authority

Accepted technical decisions by the owning team are the primary implementation authority after SliceOps Layer A principles. Stack Pattern Packs guide and validate work; they do not silently override accepted decisions.

## Current defaults

| Area | Default | Decision | Notes |
|---|---|---|---|
| Backend architecture | <monolith | modular-monolith | microservices | other> | <DEC/ARC id> | <why this is the default> |
| API style | <REST | GraphQL | RPC | event-first> | <DEC/ARC id> | <rules> |
| Data access | <EF Core | Dapper | SQL | other> | <DEC/ARC id> | <rules> |
| Frontend state | <local/context/react-query/redux/zustand/etc> | <DEC/ARC id> | <rules> |
| Cloud hosting | <provider/service> | <DEC/ARC id> | <rules> |
| Messaging | <none/service bus/kafka/etc> | <DEC/ARC id> | <rules> |
| Testing baseline | <unit/integration/contract/e2e mix> | <DEC/ARC id> | <rules> |

## Accepted technical decisions

| Decision | Scope | Selected path | Rejected paths | Revisit triggers |
|---|---|---|---|---|
| <DEC-...> | <capability/module/system> | <selected> | <rejected> | <trigger list> |

## Choices requiring a DEC

- New service or separate deployable unit.
- New database ownership boundary.
- New data lineage, reconciliation, or auditability requirement.
- New concurrency, idempotency, locking, or coordination model for a critical path.
- New reliability/availability target or degraded-mode behavior for a critical path.
- New configuration, environment, or portability model that changes runtime behavior.
- New external dependency with business-critical, regulated, or hard-to-exit role.
- Material change to public compatibility guarantees: API/event/schema versions, supported clients/browsers, or migration policy.
- Material change to compliance, privacy, accessibility, or data-retention posture.
- Exception to security, evidence, observability, accessibility, or compatibility baseline.
- Moving from synchronous to asynchronous/event-driven workflow for a critical path.
- Introducing a framework/pattern that materially changes code organization or developer workflow.

## Stack Pattern Packs

| Pack | Applies to | Source | Enforcement |
|---|---|---|---|
| <dotnet-api> | <api slices> | <path/link> | <validator/checklist/DEC/HITL> |
| <react-frontend> | <frontend slices> | <path/link> | <validator/checklist/DEC/HITL> |

## Evidence baseline

| Slice type | Required evidence |
|---|---|
| API endpoint | <integration test, ProblemDetails/error path, auth/validation evidence, compatibility evidence, auditability/logs/correlation> |
| Data migration | <migration review, data-quality/lineage check, backward-compatibility/expand-contract plan, rollback, backup/deploy evidence> |
| Async message flow | <idempotency test, DLQ/retry policy, outbox/exception DEC, observability> |
| Frontend feature | <visible behavior test, loading/error/empty states, accessibility evidence, API contract typing> |
| Infrastructure | <plan/diff, config validation, reliability/health evidence, rollout/rollback, security/compliance scan, secrets handling, smoke test> |

## Exception policy

Every exception records:

- The rule or decision being bypassed.
- The scope and expiry.
- Why the exception is safer or cheaper now.
- Required compensating evidence.
- The trigger that removes or revisits the exception.

## Review cadence

Review this profile at Block Retrospective and when any revisit trigger fires.

## Changelog

| Date | Change | Decision/Insight |
|---|---|---|
| YYYY-MM-DD | <change> | <DEC/INS/LP> |
