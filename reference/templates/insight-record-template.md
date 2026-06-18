<!--
InsightRecord template (Layer B.1). Naming: INS-NNN-<slug>.md
Append-only (P8): never edit to "correct"; append a new record and cross-ref.
Blameless: describe patterns, never name individuals. Replace all <…>.
-->
---
entity: InsightRecord
status: active              # active → archived (never superseded — append-only)
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: internal       # public | internal | restricted | sensitive
originating_slice: <BL-XX.SEC-XX.SL-XXX>
topics: []                  # canonical topic taxonomy tags
related-insights: []        # prior/contradicting observations (cross-ref, not overwrite)
promoted-to: null           # <LP id> when this contributes to a LearningPattern
---

# INS-NNN — <observation title>

## Observation
<What was empirically observed. Factual, specific, blameless.>

## Context snapshot
<Conditions when observed: slice/block, scale, what was being done.>

## Why it matters
<Implication for the framework or the work. What it predicts/warns.>

## Candidate pattern
<If this looks like it may recur: the hypothesized pattern. When the
same observation reaches ≥3 occurrences across InsightRecords it is
promoted to a LearningPattern (set promoted-to and the LP aggregates this).>

## Cross-references
<related-insights, the DEC/Block this emerged from, any sibling observations.>
