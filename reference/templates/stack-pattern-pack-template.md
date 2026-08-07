<!--
Stack Pattern Pack template.
The pack contents are adopter-owned Layer C.2. The shape is standardized by
SliceOps Decision Frameworks so agents can route, apply, validate, and revisit
stack guidance consistently.
-->

---
entity: CognitiveFramework
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <team/person accountable>
sensitivity: internal
---

# Stack Pattern Pack - <stack/domain name>

## Classification

| Axis | Value |
|---|---|
| Category | <architecture | language | framework | runtime | data | frontend | testing | design-patterns | vendor-service | domain> |
| Language | <C# | TypeScript | SQL | none | mixed> |
| Framework/library | <ASP.NET Core | EF Core | React | none | mixed> |
| Runtime/platform | <.NET | browser | Node.js | SQL Server | Azure | none | mixed> |
| Vendor/fabricante | <Microsoft | Meta | OpenJS | vendor-neutral | adopter-owned> |
| Layer | <C.2 adopter stack pattern> |

## Scope

Applies to:

- <slice types, modules, repos, languages, frameworks>

Does not apply to:

- <explicit exclusions>

## Authority

This pack complements accepted adopter decisions. If this pack conflicts with an accepted DEC/ARC/profile, the accepted decision wins until a human-approved superseding DEC changes it.

## Pattern entries

### <namespace.pattern-id> - <Pattern name>

```yaml
id: <namespace.pattern-id>
name: <Pattern name>
default: true | false
addresses_dimensions:
  - <Universal Decision Dimension this pattern answers>
applies_when:
  - <slice/file/runtime condition>
use_when:
  - <force that justifies the pattern>
avoid_when:
  - <condition where the pattern is over-engineering or risky>
requires_decision_for:
  - <exception or escalation that requires DEC/HITL>
required_evidence:
  - <test, metric, artifact, log, validator, review item>
cross_cutting_checks:
  data_quality_lineage: <required | not-applicable + rationale>
  compatibility: <required | not-applicable + rationale>
  accessibility: <required | not-applicable + rationale>
  compliance: <required | not-applicable + rationale>
  auditability_traceability: <required | not-applicable + rationale>
  reliability_availability: <required | not-applicable + rationale>
  configuration_environment: <required | not-applicable + rationale>
  dependency_vendor_risk: <required | not-applicable + rationale>
  rollout_adoption: <required | not-applicable + rationale>
  documentation_dx: <required | not-applicable + rationale>
review_gate: validator | checklist | DEC | HITL
evolution_triggers:
  - <condition that reopens this pattern or decision>
anti_patterns:
  - <misuse to avoid>
```

#### Rationale

<Why this pattern exists and what failure mode it prevents.>

#### Example acceptance criteria

- [ ] <criterion>
- [ ] <criterion>

#### Example validator/checklist hook

- <static analyzer / grep / AST / test / manual review item>

## Pack-level evidence baseline

| Slice type | Evidence |
|---|---|
| <type> | <required evidence> |

## Exceptions

Every exception must record:

- Which pattern is bypassed.
- Why the exception is appropriate now.
- Scope and expiry.
- Compensating evidence.
- Revisit trigger.

## Changelog

| Date | Change | Decision/Insight |
|---|---|---|
| YYYY-MM-DD | <change> | <DEC/INS/LP> |
