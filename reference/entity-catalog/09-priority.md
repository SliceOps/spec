# Priority — Layer B.1 Cognitive Entity

> A ranked commitment of focus toward a goal. **Mapped principle: universal.** Canonical filename prefix: `PRI-` (see `../../spec/v2.0.0/naming.md`).

> **Naming**: this entity was **ActivePriority** before v2.0.0 (renamed by clause DEC-0008.2). **An entity name must never contain a state** — "active" is a `status:` value, and an "ActivePriority" with `status: resolved` was a contradiction in the name. The `AP-` prefix is retired.

## Purpose

The Focus stage of the cognition cycle: *what is being worked now/next, and in which order*. A Priority is only meaningful relative to the goal it serves — "priority over **what**" is answerable exclusively as an ordering of focus toward Goals, which is why the pyramid edges are mandatory (clause DEC-0008.4). Distinct from a Goal (the objective), a slice (the atomic unit of work), and a ContextPack handoff (packaged context between sessions — DEC-0009): coordination documents, briefs, checklists and drafts are **not** priorities.

## Frontmatter schema

```yaml
entity: Priority
status: open | in-progress | blocked | resolved
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
serves-goal: <GOAL id>                 # REQUIRED — the goal this focus advances
rank: <int>                            # REQUIRED — unique within (owner, horizon)
horizon: now | quarter | year          # the scope the rank orders within
blocked-by: [<entity id>...]           # required when status = blocked
```

The former `priority: high | medium | low` field is **retired** — three buckets do not order work; ranks do.

## Lifecycle states

`open` → `in-progress` → (`resolved` | `blocked`). `blocked` requires `blocked-by`. A resolved Priority records its resolution (link to the decision, slice or outcome that closed it) and is retained for audit.

## Usage example (generic)

```
PRI-0001-20260401-product-mvp-first-beta-users.md
  entity: Priority
  status: in-progress
  serves-goal: GOAL-0001-20260315-product-launch
  rank: 1
  horizon: quarter
Body: what · why now · acceptance · resolution (filled on close).
```

## Cross-reference patterns

- Serves → `serves-goal` (mandatory; the Goal lists it back in `related-priorities`).
- Realized by → slices (`SLC…` coordinates); resolution links the closing decision or OutcomeRecord.
- Session-to-session continuation of the work → a ContextPack `kind: handoff` (DEC-0009), never a second Priority.

## Anti-patterns

- A Priority with no `serves-goal` (unanchored urgency — the inverted pyramid).
- `rank` collisions within the same `(owner, horizon)` scope (ranks order; buckets do not).
- Using Priority as a catch-all for briefs, handoffs, checklists or drafts (the pre-v2 failure this rename closes — those are ContextPacks, Capability components, or knowledge-layer content).
- A permanent backlog dumping ground (a Priority tracks *current* focus; the backlog lives in Goals).
- The `AP-` prefix, the name "ActivePriority", or `priority: high|medium|low` (retired — clauses DEC-0008.2 and DEC-0008.4).
