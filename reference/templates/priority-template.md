<!--
Priority template (Layer B.1). Naming (DEC-0008.5): PRI-NNNN-YYYYMMDD-slug.md
(claim the number with claim_id.py). serves-goal and rank are REQUIRED
(DEC-0008.4): "priority over what" is only answerable as an ordering of focus
toward goals. Briefs/handoffs/checklists/drafts are NOT priorities.
Replace all <…>.
-->
---
entity: Priority
status: open                # open → in-progress → blocked | resolved
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: internal
serves-goal: <GOAL id>      # REQUIRED
rank: 1                     # REQUIRED — integer, unique within (owner, horizon)
horizon: now                # now | quarter | year
blocked-by: []              # required when status = blocked
---

# PRI-NNNN — <the focus, in one line>

## What and why now
<The work this focus commits to, and why it outranks its siblings.>

## Acceptance
<What resolved looks like.>

## Resolution
<Filled on close: link to the decision, slice (SLC…) or outcome that closed it.>
