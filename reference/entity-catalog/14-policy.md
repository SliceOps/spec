# Policy — Layer B.1 Cognitive Entity

> An operating rule with scope and enforcement. **Mapped principles: P2 (Audit Plane Discipline), P6 (Evidence-by-Construction).** Canonical filename prefix: `POL-` (see `../../spec/v2.0.1/naming.md`). Entity added by clause DEC-0012_2.

## Purpose

Holds the rules an environment, an agent, a corpus or a session MUST or MUST NOT follow — verifiable, blockable, one record per policy. Boundary with its Why-ring neighbors: a **Value** is a terminal criterion (where justification stops); a **Preference** is a taste or working choice; a **Policy is enforceable** — it has scope and an enforcement surface. Policies are **transversal**, not a cycle stage: they are what the machine gates of the audit plane enforce. The container's `_policies.md` is a **derived summary** generated from the active Policy records (clause DEC-0012_3) — truth lives in the records; the summary is regenerable.

## Frontmatter schema

```yaml
entity: Policy
status: active | deprecated
scope: environment | agent | corpus | session   # canonical set; vendors MAY extend (Layer C)
enforced-by: [hook | validator | runtime | human]
severity: block | warn
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
approver: <name>                 # P3 — author ≠ approver for block-severity policies
sensitivity: public | internal | restricted | sensitive
supersedes: [<POL id>...]
superseded-by: <POL id> | null
related-decs: [<DEC id>...]
topics: [<canonical topic>...]
```

## Lifecycle states

`active` → `deprecated` (with `superseded-by` when a newer policy replaces it). A deprecated policy is retained for audit; its enforcement is withdrawn from the derived summary on regeneration.

## Usage example (generic)

```
POL-0001-20260713-public-boundary.md
  entity: Policy
  status: active
  scope: corpus
  enforced-by: [hook, validator, human]
  severity: block
Body: purpose · scope statement · the numbered rules (MUST / MUST NOT) ·
enforcement surfaces (which gate runs where) · anti-patterns.
```

## Cross-reference patterns

- Ratified/amended by → `related-decs`.
- Enforced by → the gates named in `enforced-by` (a block-severity policy names at least one machine surface).
- Summarized into → the corpus `_policies.md` (derived, regenerated — never hand-edited).
- A runtime's session-permission grants are a vendor specialization (`scope: session`, Layer C).

## Anti-patterns

- Flattening many policies into one file (kills per-record lifecycle, provenance and supersession — the reason this entity exists).
- Hand-editing `_policies.md` instead of regenerating it from the records (DEC-0012_3).
- A `severity: block` policy with no machine surface in `enforced-by` (unenforceable MUST — either wire a gate or set `warn`).
- Restating a Value or Preference as a Policy (if it has no enforcement, it is not a policy).
