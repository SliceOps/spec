# Decision Frameworks - Layer B.1

Decision Frameworks are the SliceOps mechanism for turning universal software/product forces, principles, adopter decisions, and stack-specific engineering knowledge into context-aware technical choices.

They are not a pattern catalog to apply mechanically. They are a governed decision process: load the relevant decisions, analyze the forces, select the adequate pattern for the current slice, record the rationale, produce evidence, and define when the decision must be revisited.

## Purpose

AI agents tend to over-apply familiar patterns: microservices, CQRS, eventing, abstractions, generic repositories, global state, or cloud services "just in case." SliceOps prevents that by making the agent operate from the adopter's decision corpus first.

The operating rule:

> SliceOps does not prescribe the technical answer. It prescribes an auditable way to choose, justify, validate, and evolve the technical answer that fits the adopter's context.

## Authority order

When a slice requires a technical choice, the agent evaluates inputs in this order:

| Priority | Source | Role |
|---|---|---|
| 1 | Layer A principles | Non-negotiable SliceOps compliance: decision integrity, audit plane, HITL, evidence, security, context discipline |
| 2 | Adopter technical decisions | The application/team owner's accepted architecture and stack decisions |
| 3 | Business and operating constraints | Compliance, cost, team size, roadmap, latency, scale, sensitivity, deployment model |
| 4 | Decision Frameworks and Stack Pattern Packs | Vendor-neutral decision criteria plus adopter-owned stack guidance |
| 5 | Agent recommendation | Suggestion only; never a silent override of accepted decisions |

If an agent recommendation conflicts with an accepted adopter decision, the agent must surface the conflict and require human disposition. It may propose a superseding DEC, but it must not silently implement the conflicting path.

## General-to-specific flow

SliceOps decision analysis always moves from general to specific:

```text
Universal Decision Dimensions
  -> accepted adopter decisions
  -> business/domain/slice constraints
  -> feedback strategy (acceptance-first, TDD/test-first, contract-first, characterization-first, integration-first)
  -> Stack Pattern Packs
  -> concrete implementation
```

The generic layer is not backend-only. It covers backend, frontend, data, infrastructure, UX, accessibility, localization, temporal correctness, security, compliance, auditability, reliability, testing, operations, maintainability, compatibility, configuration, dependencies, rollout, cost, and evolution through the same dimensions. See [`universal-decision-dimensions.md`](universal-decision-dimensions.md).

For the agent-level operating contract that turns this analysis into generation behavior, see [`agent-execution-contract.md`](agent-execution-contract.md). A framework that is not routed into the generation loop is only advisory; SliceOps requires the analysis to bind to implementation and evidence for non-trivial slices.

## Decision-aware technical triage

Every non-trivial slice performs a short technical triage before implementation.

The triage is a generation gate, not only documentation. For non-trivial slices, code generation starts after relationship classification, universal materiality, feedback strategy, and stack-pack routing are known. The agent may inspect code before the gate to understand context, but it should not commit to an implementation path before the gate.

### 1. Load relevant context

Use the Context Router to load:

- Foundation documents and accepted DECs relevant to the touched capability.
- Current architecture docs and module boundaries.
- The slice scope and declared dependencies.
- Applicable Stack Pattern Packs.
- Prior InsightRecords and LearningPatterns related to similar work.

### 2. Classify the relationship to existing decisions

The slice must be classified as one of:

| Classification | Meaning | Required action |
|---|---|---|
| `conforms` | Implements within accepted decisions | Reference the decisions; no new DEC required |
| `extends` | Adds detail inside an accepted direction | Reference the parent decision; add rationale in the slice or DEC if material |
| `new-decision` | Introduces a new architectural/stack choice | Create or update a DEC before/with implementation |
| `conflicts` | Contradicts an accepted decision | Stop for HITL or create a superseding DEC |
| `exception` | Temporarily violates a rule/pattern for scoped reasons | Record waiver/DEC, scope, expiry, and evidence |
| `revisit` | Evidence suggests an accepted decision may be aging | Open a review item or superseding DEC proposal |

### 3. Analyze forces

The triage first walks the Universal Decision Dimensions and records the forces that matter for this slice:

- Business capability and ownership boundary.
- Domain model, invariants, and state transitions.
- User interaction, usability, accessibility, localization, and state ownership.
- Data ownership, lifecycle, quality, and lineage.
- Boundary contracts and integration points.
- Compatibility and versioning constraints.
- Consistency and freshness.
- Concurrency, coordination, and deduplication needs.
- Failure modes, error handling, and recovery.
- Security, privacy, and sensitivity constraints.
- Compliance, policy, and accessibility constraints.
- Auditability, traceability, and provenance needs.
- Feedback strategy: acceptance-first, TDD/test-first, contract-first, characterization-first, integration-first, or justified test-after.
- Observability, reliability, testability, maintainability, configuration, and operability.
- Performance, scale, rollout, cost, dependency, and shared-resource impact.
- Evolution triggers.

Only after these generic dimensions are clear should the agent route to stack-specific packs.

### 3.1. Classify materiality

The agent does not expand every dimension mechanically. It classifies dimensions with the smallest adequate level:

| Level | Meaning | Required treatment |
|---|---|---|
| `N/A` | Not relevant to the slice | Mark and skip |
| `low` | Handled by accepted defaults | Brief note or normal evidence |
| `material` | Affects design, evidence, rollout, or review | Record rationale, selected path, evidence, and rejected alternative when useful |
| `DEC-required` | Changes accepted decisions, ownership, runtime/configuration model, security/compliance/auditability posture, reliability target, compatibility guarantee, or critical dependency | Stop for human disposition or create/update a DEC |

Analysis depth follows materiality:

- `light` - conforming slice; all dimensions are `N/A` or `low`.
- `focused` - one or more dimensions are `material`.
- `full` - classification is `new-decision`, `conflicts`, `exception`, `revisit`, or any dimension is `DEC-required`.

### 4. Select the adequate pattern

Patterns are selected only when their forces are present. For example:

- Microservices are not the default; they require stable bounded contexts, independent deployment pressure, team ownership, and operational maturity.
- A modular monolith is often the better default when the domain is still evolving and the team is small.
- Outbox is required when the same workflow persists local state and publishes an integration event, unless an accepted exception explains why not.
- CQRS is useful when read/write needs diverge; it is not a synonym for microservices, event sourcing, or two databases.
- React global state is not the default; local UI state, server state, and complex client state have different homes.

### 5. Record rejected alternatives

For material choices, the slice or DEC names the options rejected and why. This prevents pattern drift and lets future agents understand that an option was considered, not forgotten.

### 6. Attach evidence

The selected path must be validated by evidence appropriate to the choice:

- Tests for business rules, edge cases, idempotency, and error paths.
- Integration/contract tests for API, database, queue, and external boundaries.
- Data quality, lineage, and reconciliation evidence when correctness depends on sourced or transformed data.
- Compatibility and migration evidence when existing consumers or data must keep working.
- Accessibility or usability evidence when a human-facing flow changes.
- Localization, timezone, currency, or regional-rule evidence when those affect correctness.
- Auditability/provenance evidence when actions must be reconstructed later.
- Observability evidence for distributed or async flows.
- Reliability evidence when the decision claims a service level, fallback, timeout, retry, or degraded mode.
- Security evidence for auth, secrets, sensitivity, and dependency boundaries.
- Performance evidence when the decision claims scale or efficiency.
- Configuration validation, rollout, documentation, or runbook evidence when delivery/support risk is material.

### 7. Define revisit triggers

Accepted technical decisions are not permanent by default. They carry revisit triggers, such as:

- A module changes independently for three or more blocks.
- Deployment coordination repeatedly blocks a team.
- A capability develops a distinct scale, latency, or availability profile.
- A bounded context becomes stable enough to extract.
- A workaround or exception repeats enough to become a LearningPattern.
- Operational evidence contradicts the original assumption.

When a trigger fires, the agent proposes review. The human/team decides whether to keep, amend, or supersede the decision.

## Adopter Technical Decision Profile

An Adopter Technical Decision Profile is the adapter between SliceOps and a team's real architecture.

It declares the team's accepted defaults, stack choices, exceptions, and review triggers in a machine-readable and human-reviewable form. The profile is adopter-owned Layer C.2 content; the profile envelope and triage discipline are Layer B.1.

The profile answers:

- What architecture is the current default?
- Which decisions are already accepted?
- Which choices require a DEC?
- Which exceptions are allowed and for how long?
- Which stack packs apply to which slice types?
- What evidence is required for each class of work?
- What conditions trigger re-evaluation?

See [`../templates/adopter-technical-decision-profile-template.md`](../templates/adopter-technical-decision-profile-template.md).

## Stack Pattern Packs

Stack Pattern Packs are adopter-owned Layer C.2 pattern libraries. SliceOps standardizes their shape, not their contents.

Adopters may also define a path routing map that binds changed files to candidate packs and required decision analysis. The routing map is Layer C.2: SliceOps standardizes the shape, while the adopter owns the concrete paths and pack ids. See [`../templates/path-routing-template.json`](../templates/path-routing-template.json).

Packs should be organized by the most specific stable axis first:

| Axis | Use for | Example folder |
|---|---|---|
| Architecture/domain | Vendor-neutral architecture or adopter-domain rules | `architecture/`, `domain/<capability>/` |
| Language | Language semantics and runtime behavior | `languages/csharp/`, `languages/typescript/`, `languages/sql/` |
| Framework/library | Framework-specific implementation patterns | `frameworks/dotnet/aspnet-core/`, `frameworks/react/` |
| Data | Persistence/query/schema patterns when not framework-specific | `data/sql-server/`, `data/postgres/` |
| Design patterns | SOLID and pattern criteria applied to a stack | `patterns/dotnet/`, `patterns/typescript/` |
| Testing | Feedback strategy and test tooling | `testing/` |
| Vendor/fabricante | Cloud/SaaS/vendor services | `vendors/microsoft/azure/`, `vendors/aws/` |

When a pack belongs to multiple axes, store it in the axis that drives implementation, and link it from secondary indexes. For example, an Azure pack lives under `vendors/microsoft/azure/`; ASP.NET Core lives under `frameworks/dotnet/aspnet-core/` and may also be linked from a Microsoft vendor index.

Examples:

- `.NET API`
- `ASP.NET Core`
- `EF Core`
- `SQL Server`
- `Azure`
- `React`
- `TypeScript`
- `Testing`
- `Compliance export`

A pattern pack entry should include:

```yaml
classification:
  category: <architecture | language | framework | runtime | data | frontend | testing | design-patterns | vendor-service | domain>
  language: <C# | TypeScript | SQL | none | mixed>
  framework: <ASP.NET Core | EF Core | React | none | mixed>
  runtime: <.NET | browser | Node.js | SQL Server | Azure | none | mixed>
  vendor: <Microsoft | Meta | OpenJS | vendor-neutral | adopter-owned>
id: <namespace.pattern-id>
name: <short name>
default: true | false
applies_when:
  - <slice condition>
use_when:
  - <force or criterion>
avoid_when:
  - <counter-force or anti-pattern>
requires_decision_for:
  - <material exception or escalation>
required_evidence:
  - <test, metric, log, artifact, review item>
review_gate: validator | checklist | DEC | HITL
evolution_triggers:
  - <condition that reopens the decision>
```

The pack is guidance plus gates. It must not override accepted adopter decisions without a DEC.

## Universal before specific

Stack Pattern Packs are the last mile. They should be loaded only after the slice analysis identifies which universal dimensions are material.

Examples:

| Universal dimension | Possible backend pack | Possible frontend pack |
|---|---|---|
| Domain model and invariants | domain rules / validation / aggregates | form rules / workflow state / domain language |
| State ownership | EF Core / SQL / cache | React state / React Query |
| Data quality and lineage | import/export validation / reconciliation | source labels / stale-data warnings |
| Concurrency and coordination | idempotency / locks / queue workers | double-submit / cancellation / stale response handling |
| Boundary and contract | API / events / SDK adapters | DTO typing / component props / routes |
| Compatibility and versioning | API versioning / schema migration | browser support / typed contract changes |
| Error and recovery | ProblemDetails / retries / DLQ | loading/error/empty states / retry UI |
| Usability and accessibility | API ergonomics / support workflow | keyboard flow / screen reader semantics / responsive layout |
| Localization and temporal correctness | timezone/currency/collation handling | translated copy / locale-aware formatting |
| Auditability and traceability | actor/action/resource audit trail | user action attribution / support-visible history |
| Observability | logs / metrics / traces | client telemetry / user-impact metrics |
| Reliability and availability | SLO / timeout / fallback / health | degraded UI / retry affordance / cached fallback |
| Feedback strategy | TDD / contract / integration / characterization tests | behavior tests / contract types / acceptance flows |
| Performance and scale | query plans / queues / memory | virtualization / pagination / bundle size |
| Configuration and environment | options validation / env matrix | build-time env / browser-device constraints |
| Rollout and adoption | migration / flags / canary | progressive release / browser matrix |

## Example: architecture selection

| Context | Preferred starting point | Why |
|---|---|---|
| Small team, unclear domain, transactional consistency | Monolith or modular monolith | Lower operational complexity while learning the domain |
| Medium/large domain, boundaries emerging | Modular monolith | Keeps deploy simple while enforcing internal boundaries |
| Stable bounded contexts, independent teams, distinct scale/deploy needs | Microservices | Distribution cost is justified by autonomy and scaling pressure |
| Long-running side effects or multiple consumers | Event-driven flow | Decouples availability and latency, requires idempotency and observability |

This table is not a universal prescription. The adopter's accepted decisions and constraints decide the result.

For the full architecture decision framework, see [`architecture-selection.md`](architecture-selection.md).

For feedback style selection, including TDD, see [`testing-feedback-selection.md`](testing-feedback-selection.md).

For concrete usage shapes, see [`examples/`](examples/): API endpoint, React feature, and data migration analyses.

## Mapping to principles

- **P1/P2** - technical choices are decision-backed and auditable.
- **P3** - accepted adopter decisions and conflicts require human authority.
- **P4** - triage is scoped to the slice.
- **P6/P7** - selected paths require functional, quality, security, and provenance evidence.
- **P8** - repeated evidence promotes patterns and triggers superseding DECs.
- **P11** - the mechanism is platform-agnostic; stack packs are adopter-owned.
- **P12** - the decision corpus is the source of truth; stack guidance is selectively routed.

## Anti-patterns

- Applying microservices, CQRS, event sourcing, repository, MediatR, Redux, AKS, or any pattern by default.
- Applying TDD to every slice mechanically, or claiming TDD when tests are written only after implementation.
- Ignoring an accepted adopter decision because a generic best practice suggests another path.
- Letting an agent silently implement a conflicting architecture.
- Treating compatibility, accessibility, compliance, auditability, reliability, configuration, dependency, documentation, or rollout concerns as "just implementation."
- Keeping obsolete technical decisions without revisit triggers.
- Turning stack packs into unbounded context loaded into every session.
- Replacing evidence with explanation.
