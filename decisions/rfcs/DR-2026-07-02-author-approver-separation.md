---
entity: DecisionRecord
status: proposed
created: 2026-07-02
updated: 2026-07-02
owner: Andrés Ramírez Sierra
sensitivity: public
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DR-2026-07-02-evidence-v1-canonical-schema]
topics: [principles, audit-plane, layer-b-framework-artifact]
vocabulary-changes: []
consistency-check: "Formalizes the author-vs-approver separation already implicit in P3 (Human-in-the-Loop Authority). Two parts: (1) records the optional `approver` field added to the Layer B reference schemas (dec-template, entity catalog 01-decision-record, base frontmatter schema) in the same slice; (2) proposes — without amending Layer A here — a P3 implication making the separation normative, to be ratified under the elevated HITL gate P3 itself prescribes. Preserves all existing P3 gates and the DEC lifecycle; DR-2026-07-02-evidence-v1-canonical-schema is the first spec DR to record the `approver` field this RFC introduces (explicit self-ratification). No conflicts."
---

# DR-2026-07-02 — Author ≠ Approver Separation (P3)

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 Audit Plane, P1 Decision Integrity). **Status: proposed (RFC).** The Layer A portion of this proposal amends a principle and therefore requires ratification under the elevated human-in-the-loop gate that P3 itself prescribes; nothing in `spec/v1.0.0/principles.md` is edited by this RFC.

## TL;DR

P3 requires explicit human ratification of critical decisions, but the open spec never records *who* ratified — the schemas carry only `owner` (the accountable, typically authoring, party). This RFC (a) records that an optional `approver` field is added to the Layer B reference schemas in the same slice, and (b) proposes a P3 implication making author ≠ approver normative for multi-maintainer projects, with explicit — not silent — self-ratification in single-maintainer contexts.

## Context

A 2026-07 external red-team audit found that the pitch-level claim — *the human who ratifies a decision is distinct from the agent or human who authored it* — is not formalized anywhere in the open spec. P3 (Human-in-the-Loop Authority) states that "critical DECs require explicit human ratification (≠ auto-merged)", but no schema field captures the ratifying human: the audit plane records what was decided, by whom it is owned, and why — yet the *ratification actor* stays implicit. An implicit gate is not auditable (P2), and a separation that cannot be verified from the corpus cannot back the claim.

## Decision

**Part 1 — recorded (Layer B, effective this slice).** An optional `approver` field is added to the DecisionRecord frontmatter reference schemas: [`reference/templates/dec-template.md`](../../reference/templates/dec-template.md), [`reference/entity-catalog/01-decision-record.md`](../../reference/entity-catalog/01-decision-record.md), and [`reference/frontmatter-schemas/base-schema.md`](../../reference/frontmatter-schemas/base-schema.md). Semantics: `approver` is the human who ratified the DEC (the P3 human gate). Recommended on `status: ratified`. It MAY equal `owner` in single-maintainer contexts — the point is recording WHO ratified, making self-ratification explicit and auditable instead of implicit.

**Part 2 — proposed (Layer A, requires ratification).** Add the following implication to P3 in `spec/v1.0.0/principles.md`:

> When a project has more than one maintainer, the ratifying human MUST differ from the authoring human. Single-maintainer projects MUST record self-ratification explicitly (`approver` == `owner`) — a disclosed limitation, consistent with DISCLOSURE.md, not a silent one.

Per the amendment rule in the principles document and [`governance/RFC-PROCESS.md`](../../governance/RFC-PROCESS.md), this Layer A change lands only via ratification of this RFC under the elevated HITL gate, with cross-reference impact analysis.

## Alternatives considered

- **A — Leave author ≠ approver implicit in P3 (status quo)**: rejected — the audit showed the claim is made at pitch level but is unverifiable from the open corpus; an implicit gate contradicts the audit plane's own standard (P2) and leaves the framework claiming a discipline it cannot evidence (P6).
- **B — Mandate author ≠ approver unconditionally (required field, hard validator)**: rejected — it excludes single-maintainer projects (the common bootstrap case, including this repository today), forcing either fabricated attribution or non-adoption. A disclosed limitation beats a dishonest record.
- **C — Optional `approver` field now (Layer B) + conditional MUST proposed as a P3 implication (Layer A, via this RFC)**: **selected** — the schema affordance lands immediately where schemas live (Layer B), while the normative rule takes the elevated ratification path that Layer A amendments require; single-maintainer self-ratification becomes explicit and auditable rather than silent.

## Consequences

**Enables**: an auditable ratification actor on every DEC; verifiable separation of authorship and approval in multi-maintainer projects; honest, machine-readable disclosure of self-ratification in single-maintainer projects. **Constrains**: on ratification of Part 2, multi-maintainer projects can no longer have the authoring human self-approve critical DECs. **Costs**: one more frontmatter field to maintain; existing DECs may be back-filled fix-on-touch (P12) rather than in a bulk rewrite.

## References

- [`spec/v1.0.0/principles.md`](../../spec/v1.0.0/principles.md) — P3 Human-in-the-Loop Authority (the implication list Part 2 extends).
- [`reference/frontmatter-schemas/base-schema.md`](../../reference/frontmatter-schemas/base-schema.md), [`reference/entity-catalog/01-decision-record.md`](../../reference/entity-catalog/01-decision-record.md), [`reference/templates/dec-template.md`](../../reference/templates/dec-template.md) — the Layer B schemas carrying the field.
- [`DISCLOSURE.md`](../../DISCLOSURE.md) — the disclosure posture (concentration of roles disclosed openly, never left implicit) this RFC extends to ratification.
- [`governance/RFC-PROCESS.md`](../../governance/RFC-PROCESS.md) — the ratification path for this RFC.
- Origin: 2026-07 external red-team audit (finding: pitch-level author ≠ approver claim unformalized in the open spec).
