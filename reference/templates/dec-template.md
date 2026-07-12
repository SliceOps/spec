<!--
DecisionRecord template (Layer B.1). Universal grammar (DEC-0008.5):
DEC-P-NNNN-YYYYMMDD-slug.md while pending; renamed DEC-NNNN-… on approval,
DEC-D-NNNN-… on deprecation — number and date never change. Claim the number
with the toolkit's claim_id.py (P9 pre-flight). The decisions/ folder is FLAT.
Clauses inside this record are cited DEC-NNNN.n (DEC-0008.9).
Layer 1 consistency fields are mandatory. Replace all <…>.
-->
---
entity: DecisionRecord
status: pending             # pending → approved → deprecated (matches the prefix: DEC-P- / DEC- / DEC-D-)
kind: tactical              # constitutive | strategic | tactical (DEC-0008.3)
defines-goal: []            # REQUIRED when strategic — the goal(s) this decision creates
serves-goal: null           # REQUIRED when tactical — the goal this decision advances
serves-value: null          # strategic decisions with no goal above terminate in a value
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
approver: <approving human> # OPTIONAL — the human who approved (P3 human gate); recommended on
                            # status: approved. MAY equal owner in single-maintainer contexts:
                            # the point is recording WHO approved, making self-approval
                            # explicit and auditable instead of implicit.
sensitivity: internal       # public | internal | restricted | sensitive
originating_slice: <BL-XX.SEC-XX.SL-XXX>   # P1 provenance
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

# DEC-P-NNNN — <title>

## Summary
<2–4 sentences: the decision and why it matters.>

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
