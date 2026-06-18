# LearningPattern — Layer B.1 Cognitive Entity

> A pattern observed ≥3 times across InsightRecords, promoted to a canonical pattern. **Mapped principle: P8 (Recursive Learning by Capture).**

## Purpose

The promotion target of recursive learning. When the same empirical observation recurs ≥3 times across InsightRecords, it is promoted to a LearningPattern — a canonical, named pattern that informs R-rule amendments via DECs. LearningPatterns are how the corpus stops repeating its own mistakes: InsightRecords → LearningPattern → DEC → R-rule → applied forward.

## Frontmatter schema

```yaml
entity: LearningPattern
status: candidate | canonical | retired
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
aggregates-insights: [<INS id>...]    # the ≥3 observations supporting promotion
triggered-decs: [<DEC id>...]          # DECs/R-rule amendments this pattern drove
topics: [<canonical topic>...]
```

## Lifecycle states

`candidate` (≥3 insights clustered, under review) → `canonical` (ratified, drives an R-rule/DEC) → `retired` (superseded by a broader pattern or no longer applicable; retirement is a decision → DEC).

## Usage example (generic)

```
LP-NNN-<pattern-slug>.md
  entity: LearningPattern
  status: canonical
  aggregates-insights: [INS-NNN, INS-NNN, INS-NNN]   # the ≥3 supporting observations
  triggered-decs: [DR-YYYY-MM-DD-<slug>]
  topics: [<canonical topic>...]
Body: pattern statement · evidence (the aggregated insights) · resolution.
```

## Cross-reference patterns

- Aggregates → `aggregates-insights` (the ≥3 InsightRecords; each insight's `promoted-to` points back).
- Drives → `triggered-decs` (the DEC/R-rule amendment citing this pattern as evidence).
- Retirement → a superseding DEC.

## Anti-patterns

- Promoting a pattern with fewer than 3 supporting InsightRecords (threshold violation).
- R-rule amended without a LearningPattern as cited evidence.
- LearningPattern that never triggers a DEC/R-rule (observation without action).
- Editing aggregated insights to fit the pattern (corrupts the evidence chain).
