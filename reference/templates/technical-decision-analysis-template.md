<!--
Technical Decision Analysis template.
Use inside a slice PR description or as the "decision analysis" section of a DEC.
-->

## Technical decision analysis

### Relevant decisions loaded

- <DEC/ARC/FND id> - <one-line relevance>

### Relationship to existing decisions

Classification: `<conforms | extends | new-decision | conflicts | exception | revisit>`

Rationale:

<Explain whether this slice follows, extends, conflicts with, or requires a decision.>

### Analysis depth and materiality

Analysis depth: `<light | focused | full>`

Materiality levels:

- `N/A` - not relevant to this slice.
- `low` - handled by accepted defaults; brief note or normal evidence is enough.
- `material` - affects design, evidence, rollout, or review.
- `DEC-required` - changes accepted decisions, ownership, runtime/config, security/compliance/auditability posture, reliability target, compatibility guarantee, or critical dependency.

Use `light` when the slice conforms and all dimensions are `N/A` or `low`.
Use `focused` when one or more dimensions are `material`.
Use `full` when classification is `new-decision`, `conflicts`, `exception`, `revisit`, or any dimension is `DEC-required`.

Materiality pass:

| Dimension | Level | Rationale | Evidence or decision action |
|---|---|---|---|
| <dimension> | <N/A \| low \| material \| DEC-required> | <why> | <evidence/DEC/waiver/revisit> |

### Forces and constraints

For `light` analysis, keep only the force lines that are `material` or need clarification.
For `focused` or `full` analysis, fill the relevant lines and mark non-relevant items as `N/A`.

- Business capability: <capability/module>
- Domain model/invariants: <business rules, validation, workflow states, ubiquitous language, state transitions>
- User interaction: <none | human UI | API consumer | operator | external system>
- Usability/accessibility: <keyboard/screen reader/responsive/interaction quality/API ergonomics or N/A>
- Localization/time/region: <timezone, locale, language, currency, calendar, sorting/collation, regional rules or N/A>
- Ownership boundary: <team/module/service/component owner>
- Domain clarity: <stable | evolving | unknown>
- State ownership: <local UI | server state | DB aggregate | cache | queue | stateless | mixed>
- Data ownership/lifecycle: <owner, retention, migration/export needs>
- Data quality/lineage: <source of truth, validation, dedupe, lineage, reconciliation needs>
- Boundary/contract: <API | event | component props | route | SDK adapter | DB schema | none>
- Compatibility/versioning: <existing consumers, supported clients/browsers, schema/API versions, deprecation needs>
- Consistency requirement: <strong | eventual | mixed>
- Concurrency/coordination: <parallel work, double-submit, idempotency, locks, cancellation, stale responses, serialization needs>
- Error/recovery model: <validation | retry | compensation | rollback | user retry | none>
- Security/sensitivity: <notes>
- Compliance/policy: <regulatory/internal policy/audit/data residency/accessibility policy or N/A>
- Auditability/traceability: <actor/action/resource/provenance/audit log/correlation needs>
- Observability/testability: <logs/metrics/traces/tests/fixtures/evidence>
- Reliability/availability: <SLO, timeout budget, degraded mode, retry budget, health model>
- Feedback strategy: <acceptance-first | TDD/test-first | contract-first | characterization-first | integration-first | test-after with rationale>
- Maintainability/complexity: <coupling, cohesion, abstraction level, cognitive load, design debt>
- Configuration/environment: <env vars, options validation, secrets, build/runtime assumptions, portability constraints>
- Operability/deployment: <deploy, rollback, health/smoke, support>
- Rollout/migration/adoption: <feature flags, migration order, rollout metric, rollback, communication>
- Latency/performance/scale profile: <notes>
- Cost/shared-resource impact: <notes>
- Dependency/vendor risk: <third-party/platform/SLA/license/security/exit-plan notes>
- Documentation/DX: <docs, runbook, examples, local setup, discoverability>
- Evolution trigger: <what would make this choice wrong later>

### Universal-to-specific routing

Material universal dimensions:

- <dimension> -> <why it matters>

Stack Pattern Packs loaded after generic analysis:

- <category/language/framework/vendor> - <pack id/path> -> <why loaded>

Testing/feedback framework loaded:

- <testing-feedback-selection | adopter testing pack> -> <why loaded>

### Selected path

Selected pattern/approach:

- <pattern or implementation path>

Why this is adequate now:

<Short justification tied to the loaded decisions and forces.>

### Implementation binding

Bind each material or `DEC-required` force to the implementation artifact and evidence that will prove it.

| Force or pattern | Code/design artifact | Evidence artifact | Status |
|---|---|---|---|
| <material dimension or stack pattern> | <file/module/component/schema/test target> | <test/check/log/review/doc> | <planned | implemented | verified | blocked> |

### Rejected alternatives

| Alternative | Why rejected now | Revisit trigger |
|---|---|---|
| <alternative> | <reason> | <trigger> |

### Evidence required

- [ ] Feedback loop: <failing-first test | acceptance test | contract test | characterization test | integration test | rationale>
- [ ] Functional: <tests/acceptance>
- [ ] Quality: <lint/coverage/performance>
- [ ] Data quality/auditability/reliability: <lineage/reconciliation/audit/SLO/failure evidence, if applicable>
- [ ] Compatibility/accessibility/compliance: <version/migration/a11y/policy evidence, if applicable>
- [ ] Security: <security evidence>
- [ ] Observability: <logs/metrics/traces/correlation, if applicable>
- [ ] Rollout/docs: <flag/canary/migration/rollback/runbook/docs evidence, if applicable>
- [ ] Decision: <DEC/waiver/review item, if applicable>

### Revisit triggers

- <condition that should reopen this decision>

### HITL disposition

- [ ] No new human decision required; conforms to accepted decisions.
- [ ] Human review required before implementation.
- [ ] Superseding DEC required.
- [ ] Scoped exception/waiver required.
