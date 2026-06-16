# Value — Layer B.1 Cognitive Entity

> Core values guiding decisions — personal or org level. **Mapped principle: P9 (Human-in-the-Loop Authority).**

## Purpose

Records a guiding principle ("we value X") that shapes human judgment over scope, merges, and architectural direction. Values map to P9 indirectly: they are the substrate humans reason from when exercising the authority SliceOps reserves for them. Distinct from a Preference (a revisable default) and a Goal (an objective): a Value is durable and rarely changes; when it does, that is a significant, audited event.

## Frontmatter schema

```yaml
entity: Value
status: active | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <individual | org>
sensitivity: public | internal | restricted | sensitive
scope: personal | org
informs: [<P9 | decision-domain>...]    # where this value bears on judgment
superseded-by: <Value id> | null
related-decs: [<DEC id>...]              # decisions that invoked or changed it
```

## Lifecycle states

`active` → `superseded`. A Value change is high-significance: it requires a DecisionRecord with explicit rationale and an elevated human-in-the-loop gate (P9) — values are not silently edited.

## Usage example (generic)

```
VAL-002-blameless-culture.md
  entity: Value
  status: active
  scope: org
  informs: [P9, postmortems]
  related-decs: [DR-...-code-of-conduct]
Body: the value · what it means in practice · how it shapes decisions.
```

## Cross-reference patterns

- Bears on → `informs` (P9 / decision domains).
- Invoked/changed by → `related-decs`.
- Guides → human judgment in Block-scope decisions, merges, scope (P9).

## Anti-patterns

- Changing a Value without a DEC + elevated HITL gate (silent value drift — corrupts P9 substrate).
- Treating a Value as a revisable default (that is a Preference).
- Value so vague it informs no concrete judgment (decorative).
- Org Value asserted without the authority to set it.
