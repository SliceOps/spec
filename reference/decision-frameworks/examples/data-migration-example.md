# Example - Data Migration Technical Decision Analysis

Scenario: rename a persisted status value from `Queued` to `Pending` while existing consumers still read status.

## Technical decision analysis

### Relevant decisions loaded

- `ARC-data-migration-baseline` - production data changes use expand-and-contract unless a DEC accepts downtime.
- `ARC-api-compatibility-baseline` - public consumers get additive/deprecation-compatible changes.
- `TEST-data-baseline` - migrations require rollback or recovery evidence.

### Relationship to existing decisions

Classification: `extends`

Rationale:

The slice applies the accepted migration baseline to a concrete status rename. It does not change database ownership, but it materially affects compatibility, data quality, and rollout sequencing.

### Analysis depth and materiality

Analysis depth: `full`

| Dimension | Level | Rationale | Evidence or decision action |
|---|---|---|---|
| Domain model and invariants | material | Status language changes user-visible/domain meaning | Domain tests and glossary/DEC note |
| Data ownership/lifecycle | material | Existing persisted rows must be migrated safely | Migration review |
| Data quality and lineage | material | Old and new values must reconcile | Backfill/reconciliation evidence |
| Compatibility and versioning | material | Existing consumers may still send/read `Queued` | Compatibility test/deprecation note |
| Rollout and adoption | material | Requires ordered deploy and backfill | Rollout/rollback plan |
| Auditability and traceability | low | Migration should be traceable | Migration log/evidence |
| DEC-required | N/A | No database ownership or accepted policy changes | No new DEC unless downtime requested |

### Forces and constraints

- Business capability: status semantics cleanup.
- Domain model/invariants: `Pending` is the canonical term; `Queued` remains accepted input during transition.
- Data ownership/lifecycle: existing rows and future writes must converge.
- Data quality/lineage: report counts before/after migration.
- Boundary/contract: API response and request values.
- Compatibility/versioning: support old value during deprecation window.
- Consistency requirement: mixed during rollout, canonical after contract phase.
- Error/recovery model: rollback code deploy first; data migration must be recoverable.
- Feedback strategy: characterization-first for current behavior plus migration/integration evidence.
- Configuration/environment: run migration in environment with backup/restore path.
- Rollout/migration/adoption: expand -> dual-read/write -> backfill -> contract.

### Universal-to-specific routing

Material universal dimensions:

- Data ownership/lifecycle -> load migration pack.
- Compatibility/versioning -> load API contract pack.
- Data quality/lineage -> load reconciliation evidence guidance.
- Rollout/adoption -> load deploy/rollback guidance.

Stack Pattern Packs loaded after generic analysis:

- `<data-pack>` -> expand-and-contract, migration review, rollback.
- `<api-pack>` -> compatibility/deprecation behavior.
- `<testing-pack>` -> characterization and integration evidence.

### Selected path

Selected pattern/approach:

- Introduce `Pending` as canonical status.
- Temporarily accept/read both `Queued` and `Pending`.
- Backfill existing rows with reconciliation counts.
- Keep compatibility behavior until consumers are migrated.
- Remove old value in a later contract slice.

Why this is adequate now:

It preserves compatibility and gives production data a recoverable path. A direct rename is too risky because consumers and persisted rows may not update atomically.

### Rejected alternatives

| Alternative | Why rejected now | Revisit trigger |
|---|---|---|
| Direct in-place rename and deploy | Breaks old consumers and rollback | All consumers are internal and deployed atomically |
| Keep both values forever | Creates domain ambiguity and data-quality drift | External consumers require permanent legacy contract |
| New status table/service | Over-engineering for a value rename | Status rules become independently owned and complex |

### Evidence required

- [ ] Feedback loop: characterization test for current status behavior before change.
- [ ] Functional: migration/backfill test and API compatibility test.
- [ ] Data quality/auditability/reliability: before/after counts and migration log.
- [ ] Compatibility/accessibility/compliance: deprecation note or compatibility window.
- [ ] Rollout/docs: expand-contract rollout and rollback steps.
- [ ] Decision: no DEC required unless downtime or direct breaking change is requested.

### Revisit triggers

- Consumers keep using `Queued` past the deprecation window.
- Reconciliation finds mismatched or unknown status values.
- Status semantics expand into a workflow requiring a stronger domain model.

### HITL disposition

- [x] No new human decision required for expand-and-contract path.
- [ ] Human review required if a direct breaking migration is requested.

