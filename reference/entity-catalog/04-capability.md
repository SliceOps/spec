# Capability — Layer B.1 Cognitive Entity

> Capabilities accrued by individuals, agents, or teams. **Mapped principle: P8 (Recursive Learning by Capture).**

> **Naming**: this entity is **Capability**. It was formerly called "Skill"; renamed because "capabilities accrued" precisely describes it. The term **"Skill"** is now **reserved** for the future *Agent-Skill* concept (a vendor-neutral procedural pack) and must NOT be used for this entity.

## Purpose

Tracks what an individual, agent, or team *can now do that it could not before* — capability accrued through slices, retrospectives, and learning. Distinct from a Goal (an objective) and from a LearningPattern (a recurring framework-level pattern): a Capability is an accrued competence held by an actor. Supports P8 by making the growth of the system's actors a first-class, auditable artifact.

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
```

## Lifecycle states

`emerging` (first demonstrated) → `established` (repeatedly demonstrated) → `deprecated` (no longer relevant or superseded by a broader capability). Level (`emerging`/`proficient`/`expert`) tracks depth independently of lifecycle.

## Usage example (generic)

```
CAP-007-multi-agent-coordination.md
  entity: Capability
  status: established
  holder: platform-team
  level: proficient
  evidence: [BL-04.SEC-01.SL-009, OUT-BL04-block-outcome]
Body: what the capability is · how it was accrued · demonstrations · gaps.
```

## Cross-reference patterns

- Demonstrated by → slices / OutcomeRecords (`evidence`).
- Accrued via → InsightRecords/LearningPatterns that drove the growth.
- Composes with → `related-capabilities`.

## Anti-patterns

- Using "Skill" for this entity (reserved term — see naming note).
- Recording a Capability with no evidence (claim without demonstration).
- Conflating Capability (accrued competence) with Goal (objective) or LearningPattern (framework pattern).
- Capability that never updates `level`/`status` despite repeated demonstration (stale record).
