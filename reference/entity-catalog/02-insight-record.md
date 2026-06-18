# InsightRecord — Layer B.1 Cognitive Entity

> Empirical observations captured from slices; raw material for LearningPatterns. **Mapped principle: P8 (Recursive Learning by Capture).**

## Purpose

The capture mechanism of recursive learning. Every slice may emit empirical observations — what surprised us, what drifted, what an estimate missed. InsightRecords are **append-only**: a newer insight that contradicts an older one does not delete it; both are retained with a cross-reference. When a pattern recurs ≥3 times across InsightRecords it is promoted to a LearningPattern.

## Frontmatter schema

```yaml
entity: InsightRecord
status: active | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
originating_slice: <BL-XX.SEC-XX.SL-XXX>
topics: [<canonical topic>...]
related-insights: [<INS id>...]      # prior/contradicting observations (append-only cross-ref)
promoted-to: <LP id> | null          # set when this insight contributes to a LearningPattern
```

## Lifecycle states

`active` → `archived`. **Never `superseded`** — InsightRecords are append-only by design (P8). Archival is for noise reduction only and preserves the record and cross-references.

## Usage example (generic)

```
INS-NNN-<observation-slug>.md
  entity: InsightRecord
  status: active
  originating_slice: BL-XX.SEC-XX.SL-XXX
  topics: [<canonical topic>...]
  related-insights: [INS-NNN-<prior-related-observation>]
  promoted-to: null
Body: observation · context snapshot · why it matters · candidate pattern.
```

## Cross-reference patterns

- Emitted by a slice → `originating_slice`.
- Clusters with sibling observations → `related-insights`.
- Feeds a LearningPattern → `promoted-to` (set at promotion time; the LP lists its `aggregates-insights`).

## Anti-patterns

- Retrospectives that produce no InsightRecords.
- InsightRecords that sit unused (must feed back to LearningPatterns/R-rules/DECs).
- Editing an old InsightRecord to "correct" it instead of appending a new one (violates append-only).
- Insight that names individuals instead of patterns (blameless-culture violation).
