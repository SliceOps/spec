# Capability — Layer B.1 Cognitive Entity

> Capabilities accrued by individuals, agents, or teams. **Mapped principle: P8 (Recursive Learning by Capture).**

> **Naming**: this entity is **Capability**. It was formerly called "Skill"; renamed because "capabilities accrued" precisely describes it. The term **"Skill"** is now **reserved** for the future *Agent-Skill* concept (a vendor-neutral procedural pack) and must NOT be used for this entity.

## Purpose

Tracks what an individual, agent, or team *can now do that it could not before* — capability accrued through slices, retrospectives, and learning. **The Capability is the capacity itself, the WHAT** (e.g., "we know how to parse financial PDFs into structured databases"). Distinct from a Goal (an objective) and from a LearningPattern (a recurring framework-level pattern): a Capability is an accrued competence held by an actor. Supports P8 by making the growth of the system's actors a first-class, auditable artifact.

## The component model (since v1.2.0)

A capability is *described* by up to three **component kinds** — siblings of each other, never nested, and NOT separate catalog entities:

| Component (`kind:`) | Answers |
|---|---|
| `standard` | how the result must look (acceptance shape) |
| `runbook` | how it is executed, step by step |
| `playbook` | what to do depending on the situation |

Implementation: a **small** capability is a single `CAP-` file with *Standard / Runbook / Playbook* sections. A **large** capability is a `CAP-` mother file plus component files that carry `capability: <mother-slug>` and `kind: standard|runbook|playbook` in frontmatter. The catalog does **not** grow — Capability remains one entity (#4).

## Frontmatter schema

```yaml
entity: Capability
status: emerging | established | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <individual | agent | team>
sensitivity: public | internal | restricted | sensitive
holder: <who holds this capability>
level: emerging | proficient | expert
evidence: [<slice id | OutcomeRecord id>...]   # what demonstrates it
related-capabilities: [<Capability id>...]

# Component files only (large capabilities — see the component model):
capability: <mother-capability-slug>           # which capability this component describes
kind: standard | runbook | playbook
```

## Lifecycle states

`emerging` (first demonstrated) → `established` (repeatedly demonstrated) → `deprecated` (no longer relevant or superseded by a broader capability). Level (`emerging`/`proficient`/`expert`) tracks depth independently of lifecycle.

## Usage example (generic)

```
CAP-007-multi-agent-coordination.md                (canonical prefix CAP- — legacy SKILL-/RUN-/REF- retired)
  entity: Capability
  status: established
  holder: platform-team
  level: proficient
  evidence: [BL-XX.SEC-XX.SL-XXX, OUTC-BLXX-block-outcome]
Body: what the capability is · how it was accrued · demonstrations · gaps.

CAP-008-financial-pdf-parsing.md                   (mother — the capacity)
CAP-009-financial-pdf-parsing-runbook.md           (component)
  entity: Capability
  capability: financial-pdf-parsing
  kind: runbook
```

## Cross-reference patterns

- Demonstrated by → slices / OutcomeRecords (`evidence`).
- Accrued via → InsightRecords/LearningPatterns that drove the growth.
- Composes with → `related-capabilities`.
- Described by → component files (`capability:` back-reference + `kind:`).

## Anti-patterns

- Using "Skill" for this entity (reserved term — see naming note).
- Recording a Capability with no evidence (claim without demonstration).
- Conflating Capability (accrued competence) with Goal (objective) or LearningPattern (framework pattern).
- Capability that never updates `level`/`status` despite repeated demonstration (stale record).
- Treating `standard`/`runbook`/`playbook` as entities or nesting them (they are sibling **components** of one Capability).
- The `SKILL-`, `RUN-` or `REF-` prefixes (retired — see `../../spec/v1.2.0/naming.md`).
