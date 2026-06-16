# Preference — Layer B.1 Cognitive Entity

> Stated preferences (style, tooling, approach) — personal or team/org level. **Mapped principle: universal.**

## Purpose

Records a stated "we/I prefer X over Y" so that recurring choices are explicit and auditable rather than re-litigated each slice. A Preference carries meaning standalone in markdown (which is why it is Layer B, runtime-independent). Distinct from a Value (a deeper guiding principle) and a DecisionRecord (a binding architectural decision): a Preference is a softer, revisable default.

## Frontmatter schema

```yaml
entity: Preference
status: active | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <individual | team | org>
sensitivity: public | internal | restricted | sensitive
scope: personal | team | org
domain: <style | tooling | approach | process>
strength: default | strong            # "strong" → deviation needs a DEC
superseded-by: <Preference id> | null
```

## Lifecycle states

`active` → `superseded` (a newer Preference replaces it; bidirectional). A `strong` Preference contradicted by a slice escalates to a DecisionRecord (the contradiction is itself a decision).

## Usage example (generic)

```
PREF-006-prefer-deterministic-scripts.md
  entity: Preference
  status: active
  scope: org
  domain: approach
  strength: strong
Body: the preference · rationale · when deviation is acceptable.
```

## Cross-reference patterns

- Escalates to → a DecisionRecord when a `strong` preference is contradicted.
- Informs → slice scoping and tooling choices.
- Superseded by → a newer Preference (bidirectional).

## Anti-patterns

- Encoding a binding architectural decision as a Preference to dodge the audit plane (that is a DEC — P2).
- `strong` preference with no rationale (unjustifiable default).
- Contradicting a `strong` preference in a slice without escalating to a DEC.
- Personal preference asserted as org scope without authority.
