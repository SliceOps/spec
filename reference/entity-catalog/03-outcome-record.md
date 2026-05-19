# OutcomeRecord — Capa B.1 Cognitive Entity

> Tracked outcomes of slices/blocks — what shipped, what worked, what the result was. **Mapped principle: P5 (Evidence-by-Construction).**

## Purpose

The factual record of what a slice or Block actually produced and how it performed against forecast. Where a DecisionRecord captures *what we decided* and an InsightRecord captures *what we observed*, an OutcomeRecord captures *what happened* — shipped scope, forecast vs actual, evidence references. It is the provenance/evidence anchor that makes audits "select date range, filter, evidence present by construction."

## Frontmatter schema

```yaml
entity: OutcomeRecord
status: open | closed
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
scope: slice | block
ref: <BL-XX.SEC-XX.SL-XXX | BL-XX>     # the slice or block this records
forecast: { token_band: <XS|S|M|L|XL>, estimate: <value> }
actual: { value: <value>, drift_pct: <number> }
evidence: [functional, quality, security, decision, provenance]   # categories satisfied
related-decs: [<DEC id>...]
```

## Lifecycle states

`open` (slice/block in flight) → `closed` (merged + evidence complete). A `closed` OutcomeRecord is immutable; corrections append a new record citing the original.

## Usage example (generic)

```
OUT-BL05-block-outcome.md
  entity: OutcomeRecord
  status: closed
  scope: block
  ref: BL-05
  forecast: { token_band: L, estimate: 14M }
  actual: { value: 17M, drift_pct: 21 }
  evidence: [functional, quality, security, decision, provenance]
Body: shipped scope · forecast vs actual narrative · evidence links · carry-forward.
```

## Cross-reference patterns

- Anchors a slice/block → `ref`.
- Drift feeds velocity recalibration in the Block Retrospective (P3).
- Links the DECs and evidence produced in scope.
- Negative outcomes pair with a blameless Postmortem and emit InsightRecords (P7).

## Anti-patterns

- Closing an OutcomeRecord without all required evidence categories present (violates P5).
- "We'll record the outcome later" — outcome is a per-slice/Block byproduct, not deferred.
- Editing a closed OutcomeRecord instead of appending a correction.
- Forecast/actual omitted (breaks velocity recalibration input).
