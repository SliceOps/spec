# Conclusion — Layer B.1 Cognitive Entity

> What we now believe: a generalization promoted from repeated insights, or reached by explicit reasoning. **Mapped principle: P8 (Recursive Learning by Capture).** Canonical filename prefix: `CONC-` (see `../../spec/v2.0.0/naming.md`).

> **Naming**: this entity was **LearningPattern** before v2.0.0 (renamed by clause DEC-0008.2 — the framework must be understandable in plain words, and what this entity holds are conclusions). The `LP-` prefix is retired.

## Purpose

The promotion target of recursive learning. A Conclusion changes what the corpus *believes*; a DecisionRecord changes what it *does* — the epistemic act and the volitional act stay separate entities. Conclusions are how the corpus stops repeating its own mistakes: InsightRecords → Conclusion → DecisionRecord → enforced rule → applied forward.

## Frontmatter schema

```yaml
entity: Conclusion
status: candidate | canonical | retired
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
aggregates-insights: [<INS id>...]    # the supporting observations (≥3 to reach canonical)
triggered-decs: [<DEC id>...]          # decisions / rule amendments this conclusion drove
topics: [<canonical topic>...]
```

## Lifecycle states

`candidate` → `canonical` → `retired`. **Three or more supporting insights remain the promotion rule to `canonical`** (empirical conclusions); a conclusion reached by a single reasoning chain may exist as `candidate` until evidence accumulates. Retirement is a decision (a superseding DecisionRecord) — conclusions are falsifiable by design.

## Usage example (generic)

```
CONC-0012-20260710-the-decision-creates-the-goal.md
  entity: Conclusion
  status: canonical
  aggregates-insights: [INS-0004-…, INS-0007-…, INS-0011-…]
  triggered-decs: [DEC-0008-…]
  topics: [<canonical topic>...]
Body: conclusion statement · evidence (the aggregated insights) · resolution.
```

## Cross-reference patterns

- Aggregates → `aggregates-insights` (each insight's `promoted-to` points back).
- Drives → `triggered-decs` (the decision or rule amendment citing this conclusion as evidence).
- Retirement → a superseding DecisionRecord.

## Anti-patterns

- Promoting to `canonical` with fewer than three supporting InsightRecords (threshold violation).
- A rule amended without a Conclusion as cited evidence.
- A Conclusion that never triggers a decision or rule (belief without consequence).
- Editing aggregated insights to fit the conclusion (corrupts the evidence chain).
- The `LP-` prefix or the name "LearningPattern" (retired — clause DEC-0008.2).
