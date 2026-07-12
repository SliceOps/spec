<!--
DecisionRecord template (Layer B.1). Naming: DEC-P-<id>-<slug>.md while pending;
renamed to DEC-<id>-<slug>.md on approval, DEC-D-<id>-<slug>.md on deprecation
(id = YYYY-MM-DD in vaults, NNN in counter-based repos — spec/v2.0.0/naming.md).
The decisions/ folder is FLAT: the prefix carries the state; a state change
renames the file and rewrites references in the same atomic change (R5).
Layer 1 consistency fields are mandatory. Replace all <…>.
-->
---
entity: DecisionRecord
status: pending             # pending → approved → deprecated (matches the prefix: DEC-P- / DEC- / DEC-D-)
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

# DEC-P-<id> — <title>

## TL;DR
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
