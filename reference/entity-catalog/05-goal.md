# Goal — Layer B.1 Cognitive Entity

> Forward-looking objectives at various time horizons. **Mapped principle: universal.**

## Purpose

Captures intent — what an individual, team, or org is trying to achieve, at a stated horizon. Goals provide the "why" that slices and Blocks trace back to. A Goal is an objective (future-directed); distinct from a Capability (accrued competence), an ActivePriority (what is being worked now), and a Value (a guiding principle).

## Frontmatter schema

```yaml
entity: Goal
status: proposed | active | achieved | abandoned
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
decided-by: <DEC id>                     # REQUIRED — the decision that created this goal
                                          # (mirror edge of the DEC's defines-goal; clause DEC-0008.4)
horizon: now | quarter | year | multi-year
measure: <how achievement is verified>
parent-goal: <Goal id> | null            # goal hierarchy
related-priorities: [<Priority id>...]
```

A goal without an originating decision is unaccountable ambition — `decided-by:` closes the provenance chain `VAL → INS/CONC → DEC → GOAL → PRI → SESS → OUTC` end to end. **Vision** lives here too (clause DEC-0008.7): a Goal with `horizon: multi-year` and a narrative body, its `measure` qualitative.

## Lifecycle states

`proposed` → `active` → (`achieved` | `abandoned`). `abandoned` requires a rationale in the body (a Goal is not silently dropped — that is itself a decision and may warrant a DEC).

## Usage example (generic)

```
GOAL-2026-q1-publish-spec-v1.md
  entity: Goal
  status: active
  horizon: quarter
  measure: first spec version published with the full entity specs and R-rules
  parent-goal: GOAL-0001-20260315-framework-adoption
Body: objective · why now · measure of done · dependencies.
```

## Cross-reference patterns

- Decomposes from → `parent-goal` (hierarchy).
- Realized through → `related-priorities` (ActivePriority) and the slices/Blocks that serve it.
- Abandonment/major change → may produce a DecisionRecord.

## Anti-patterns

- Goal with no `measure` (unverifiable — cannot be `achieved`).
- Goal abandoned without a rationale (silent drop).
- Goal used as a task list (that is slice/ActivePriority territory).
- Perpetually `active` Goal with no review (stale intent).
