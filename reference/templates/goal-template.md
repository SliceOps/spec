<!--
Goal template (Layer B.1). Naming (DEC-0008_5): GOAL-NNNN-YYYYMMDD-slug.md
(claim the number with claim_id.py). decided-by is REQUIRED (DEC-0008_4):
a goal without an originating decision is unaccountable ambition.
Vision = a Goal with horizon: multi-year and a narrative body (DEC-0008_7).
Replace all <…>.
-->
---
entity: Goal
status: proposed            # proposed → active → achieved | abandoned
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: internal
decided-by: <DEC id>        # REQUIRED — the decision that created this goal
horizon: quarter            # now | quarter | year | multi-year
measure: <how achievement is verified>
parent-goal: null
related-priorities: []
---

# GOAL-NNNN — <the objective, stated as an outcome>

## Why this goal
<The decision context it operationalizes — link decided-by, do not repeat it.>

## Measure
<What true looks like, verifiable. Qualitative allowed at multi-year horizon.>

## Abandonment note
<Only if abandoned: the rationale (a goal is never silently dropped).>
