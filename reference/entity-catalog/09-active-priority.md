# ActivePriority — Capa B.1 Cognitive Entity

> Current priorities tracked with status + ownership. **Mapped principle: universal.**

## Purpose

The live "what is being worked now / next" record. Distinct from a Goal (an objective) and a slice (an atomic unit of work): an ActivePriority is the tracked, owned, status-bearing bridge between intent (Goals) and execution (slices). Cross-domain handoffs are commonly tracked as ActivePriorities.

## Frontmatter schema

```yaml
entity: ActivePriority
status: open | in-progress | blocked | resolved
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
priority: high | medium | low
serves-goal: <Goal id> | null
blocked-by: [<entity id>...]            # dependencies if status=blocked
handoff: { from: <domain>, to: <domain> } | null   # cross-domain handoffs
```

## Lifecycle states

`open` → `in-progress` → (`resolved` | `blocked`). `blocked` requires `blocked-by`. A resolved ActivePriority records its resolution (link to the DEC/slice/outcome that closed it) and is retained for audit.

## Usage example (generic)

```
AP-014-port-entity-catalog.md
  entity: ActivePriority
  status: in-progress
  priority: high
  serves-goal: GOAL-2026-q1-publish-spec-v1
  handoff: null
Body: what · why now · acceptance · resolution (filled on close).
```

## Cross-reference patterns

- Serves → `serves-goal` (Goal).
- Realized by → slices; resolution links the DEC/OutcomeRecord that closed it.
- Cross-domain → `handoff` (from/to domain); a handoff log is a collection of these.

## Anti-patterns

- ActivePriority with no owner (unaccountable work).
- `blocked` with no `blocked-by` (untraceable block).
- Resolved without recording how (no resolution link).
- Using ActivePriority as a permanent backlog dumping ground (it tracks *active* priorities).
