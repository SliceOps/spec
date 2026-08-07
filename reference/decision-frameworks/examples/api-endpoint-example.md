# Example - API Endpoint Technical Decision Analysis

Scenario: add `POST /exports` to request an evidence export for a project.

## Technical decision analysis

### Relevant decisions loaded

- `ARC-current-api-style` - API uses resource-oriented HTTP endpoints and typed DTOs.
- `SEC-authz-baseline` - project-scoped actions require authenticated user and project permission.
- `TEST-api-baseline` - API behavior changes require integration evidence.

### Relationship to existing decisions

Classification: `conforms`

Rationale:

The endpoint follows the accepted API style and security baseline. No new runtime, service boundary, database owner, or public compatibility guarantee changes.

### Analysis depth and materiality

Analysis depth: `focused`

| Dimension | Level | Rationale | Evidence or decision action |
|---|---|---|---|
| Business capability | material | New user-visible export request capability | Acceptance/integration test |
| Boundary and contract | material | New HTTP request/response contract | DTO/schema and contract evidence |
| Security and privacy | material | Export may expose project evidence | Authz test and sensitive-field review |
| Concurrency and coordination | material | Repeated requests must not create duplicate export jobs | Idempotency test |
| Reliability and availability | low | Export job is asynchronous; request path only enqueues work | Error-path integration test |
| Compatibility and versioning | low | Additive endpoint; no existing contract changes | Normal API review |
| Dependency and vendor risk | N/A | No new external dependency | N/A |
| DEC-required | N/A | No accepted decision changes | No DEC |

### Forces and constraints

- Business capability: evidence export request.
- User interaction: API consumer and operator support workflow.
- State ownership: server state plus export job state.
- Boundary/contract: `POST /exports`, request DTO, response DTO, ProblemDetails errors.
- Concurrency/coordination: idempotency key or deterministic request dedupe.
- Security/sensitivity: user must have project export permission.
- Feedback strategy: acceptance/integration-first; TDD optional for pure idempotency rule.
- Observability/testability: correlation ID and export request log.
- Rollout/migration/adoption: additive endpoint; no migration.

### Universal-to-specific routing

Material universal dimensions:

- Boundary and contract -> load API contract pack.
- Security and privacy -> load auth/security pack.
- Concurrency and coordination -> load idempotency/testing pack.

Stack Pattern Packs loaded after generic analysis:

- `<api-pack>` -> endpoint, DTO, error shape, auth evidence.
- `<testing-pack>` -> integration and idempotency evidence.

### Selected path

Selected pattern/approach:

- Add a resource-oriented HTTP endpoint with explicit request/response DTOs.
- Validate input before enqueueing.
- Return `202 Accepted` with a request identifier.
- Use idempotency/deduplication for repeated requests.
- Return ProblemDetails for validation/auth errors.

Why this is adequate now:

The request starts a long-running export but does not justify a new service boundary. The existing API and async job model are enough.

### Rejected alternatives

| Alternative | Why rejected now | Revisit trigger |
|---|---|---|
| New export microservice | No independent ownership, deploy, or scale evidence | Export volume develops distinct scale/availability profile |
| Synchronous export generation | Request can exceed latency budget | Export becomes consistently small and bounded |
| Global unauthenticated export URL | Violates sensitivity baseline | Human-approved security DEC |

### Evidence required

- [ ] Feedback loop: API integration test for success, auth failure, validation failure, and duplicate request.
- [ ] Functional: export request is created and observable.
- [ ] Security: project permission enforced.
- [ ] Observability: correlation/request ID logged.
- [ ] Decision: no DEC required; conforms to accepted decisions.

### Revisit triggers

- Export requests need independent scaling or ownership.
- Duplicate exports occur in production.
- Export data sensitivity changes.

### HITL disposition

- [x] No new human decision required; conforms to accepted decisions.

