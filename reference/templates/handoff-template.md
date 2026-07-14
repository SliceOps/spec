<!--
Handoff template (ContextPack kind: handoff — DEC-0009). Naming (DEC-0008_5):
CP-NNNN-YYYYMMDD-slug.md (claim the number with claim_id.py). A handoff is born
when the session's context is exhausted, or a topic spins off to another
session. It CONTAINS context; locating context is _index.md's job (DEC-0010).
Replace all <…>.
-->
---
entity: ContextPack
kind: handoff
status: active              # active → archived (once received and absorbed)
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: internal
from_session: <SESS id or session reference>
to: <owner | domain | SESS id> | null
reason: context-exhausted   # context-exhausted | spinoff
---

# CP-NNNN — Handoff: <what continues, in one line>

## State of work
<Where things stand, in one paragraph an agent can act on cold.>

## Done
<What is finished and verified — with paths/ids, not adjectives.>

## Pending
<What remains, in execution order.>

## Open questions
<Decisions the receiver must NOT improvise — ask or escalate.>

## Next steps
<The first concrete action the receiving session should take.>

## Counter and resource state
<Claimed ids, counters touched, branches in flight, caps/budgets consumed.>
