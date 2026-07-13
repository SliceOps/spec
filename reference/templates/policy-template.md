<!--
Policy template (Layer B.1). Naming: POL-NNNN-YYYYMMDD-<slug>.md
(universal grammar — spec/v2.0.0/naming.md; entity added by DEC-0012.2).
Home: 00-context/07-policies/ in container corpora (DEC-0011.2).
One record per policy. The corpus _policies.md is a DERIVED summary of the
active records (DEC-0012.3) — regenerate it; never hand-edit it.
A severity: block policy names at least one machine surface in enforced-by.
Replace all <…>.
-->
---
entity: Policy
status: active
scope: <environment | agent | corpus | session>
enforced-by: [<hook | validator | runtime | human>, ...]
severity: <block | warn>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
owner: <accountable party>
approver: <approving human>        # P3 — author ≠ approver for block-severity policies
sensitivity: <public | internal | restricted | sensitive>
supersedes: []
superseded-by: null
related-decs: [<DEC id>...]
topics: [<canonical topic>...]
---

# <Policy name>

## Purpose

<One paragraph: what this policy protects or guarantees, and why it exists.>

## Scope

<What the scope value covers concretely for this policy: which environment/agent/
corpus/session boundaries it applies to, and what is explicitly out of scope.>

## Rules

1. **MUST** <rule>.
2. **MUST NOT** <rule>.
3. <…numbered, each independently verifiable.>

## Enforcement

| Surface | What it does |
|---|---|
| <hook> | <blocks at write time: command / gate name> |
| <validator> | <continuous-integration / sweep check> |
| <human> | <review step, cadence> |

## Anti-patterns

- <The failure this policy exists to prevent, stated as the thing people would do without it.>
