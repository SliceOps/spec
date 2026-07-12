<!--
Capability template (Layer B.1). Naming: CAP-<id>-<slug>.md
(id = NNN counter-based repos, YYYY-MM-DD vaults — spec/v2.0.0/naming.md).
The Capability is the CAPACITY (the WHAT). Small capability: one file with the
Standard / Runbook / Playbook sections below. Large capability: this file is the
mother; components split into their own CAP- files carrying `capability:` and
`kind:` (see the component-files variant at the bottom). Replace all <…>.
-->
---
entity: Capability
status: emerging            # emerging | established | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <individual | agent | team>
sensitivity: internal       # public | internal | restricted | sensitive
holder: <who holds this capability>
level: emerging             # emerging | proficient | expert
evidence: []                # [<slice id | OUTC id>...] — what demonstrates it
related-capabilities: []
---

# CAP-<id> — <the capacity, stated as a capability>

## What we can do
<The capacity in one paragraph: "we know how to <X>". The WHAT, not the how.>

## Standard (how the result must look)
<Acceptance shape of the output. What "done right" looks like. Or link the component file.>

## Runbook (how it is executed)
<Step-by-step execution. Or link the component file.>

## Playbook (what to do depending on the situation)
<Situational branches: if <situation> then <play>. Or link the component file.>

## Evidence
<Demonstrations: slices, OutcomeRecords. A capability without evidence is a claim.>

<!--
Component-file variant (large capabilities): each component is its own CAP- file
with this frontmatter addition — components are SIBLINGS, never nested:

  entity: Capability
  capability: <mother-capability-slug>
  kind: standard | runbook | playbook
-->
