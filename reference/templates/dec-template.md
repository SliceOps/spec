<!--
DecisionRecord template (Capa B.1). Naming: DR-YYYY-MM-DD-<slug>.md
Layer 1 consistency fields are mandatory. Replace all <…>.
-->
---
entity: DecisionRecord
status: proposed            # proposed → ratified → superseded|deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: internal       # public | internal | restricted | sensitive
originating_slice: <BL-XX.SEC-XX.SL-XXX>   # P4 provenance
supersedes: []
superseded-by: null
conflicts-with: []          # non-empty → "Conflict Resolution" section below
related-decs: []
topics: []                  # ≥1 from the canonical topic taxonomy
vocabulary-changes: []      # terms introduced/modified → update glossary same slice
consistency-check: |
  How this DEC relates to the existing corpus: what is preserved,
  what changes, which conflicts (if any) are resolved and how.
---

# DR-YYYY-MM-DD — <title>

## TL;DR
<2–4 sentences: the decision + why it matters.>

## Context
<What forced this decision. Prior state. Trigger.>

## Decision
<The decision, stated normatively.>

## Alternatives considered
- **<Alt A>** — rejected/selected because <reason> (no false-binary; ≥2 real alternatives)
- **<Alt B>** — …

## Consequences
**Enables**: <…>  ·  **Constrains**: <…>  ·  **Costs**: <…>

## Conflict Resolution
<Only if conflicts-with non-empty: per conflicting DEC, how resolved.>

## References
<DECs, principles, external sources.>
