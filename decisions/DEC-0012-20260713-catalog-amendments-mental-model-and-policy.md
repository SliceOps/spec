---
entity: DecisionRecord
status: approved
kind: constitutive
created: 2026-07-13
updated: 2026-07-13
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
originating_slice: null   # back-fill: layout-design conversation, 2026-07-12/13
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0011-20260713-canonical-corpus-container-and-layout, DEC-P-0016-20260728-topic-taxonomy-naming-and-off-taxonomy-cleanup]
topics: [naming, entity-catalog, vocabulary-discipline, r-rules]
vocabulary-changes: ["MentalModel (entity — was Frame, was CognitiveFramework)", "MM- prefix", "FRAME- retired", "Policy (entity)", "POL- prefix", "policy scope", "_policies.md (derived view)"]
consistency-check: |
  Amends the single-source entity table of DEC-0008_2_1 — folded into v2.0.0 before any
  publication, so the amendment leaves no alias debt beyond the migration map. Split from
  DEC-0011 per the independence test (DEC-0008_9): the layout can be ratified without
  these catalog changes and vice versa; DEC-0011 references the folder homes these
  entities take. FRAME- joins the retired-prefix list next to CF- (one concept keeps one
  current name). Policy lands in the transversal plane, not a cycle stage: policies are
  what the machine gates of the audit plane enforce (P2, P6). Count-coherence gates cover
  every literal that states the catalog size.
---

# DEC-0012 — Catalog Amendments: MentalModel and the Policy Entity

> A SliceOps DecisionRecord about SliceOps itself. Ratified with the owner in the
> layout-design conversation (2026-07-12/13); approved 2026-07-13 (born `DEC-P-0012`,
> renamed on approval — the prefix carries the state). Clause identifiers per DEC-0008_9.

## Summary

Two amendments to the canonical entity catalog. **First**: the entity renamed by
DEC-0008 from CognitiveFramework to Frame is renamed once more — final name
**MentalModel**, prefix `MM-` — because "mental model" is self-explanatory to any
audience, while "frame" both collides with "framework" and
under-communicates. **Second**: **Policy** enters the catalog as a canonical entity
(prefix `POL-`): an operating rule with scope and enforcement — how an environment, an
agent, a corpus or a session must operate — stored one record per policy, with
the container's `_policies.md` demoted to a **derived summary**. Both amendments fold
into spec v2.0.0 before publication.

## Context

The owner reviewed the Frame rename in the layout conversation and weighed the folder
name `03-framework` (the working drafts' original) against the framework/Frame
collision; the resolution surfaced that the entity name itself was the weak point:
"mental models" is an established, transversal term — practitioners and product
surfaces read it without a glossary — while a mindset-style alternative
carries a pop-psychology register and names a global disposition rather than a chosen
instrument. Separately, the owner observed that operating policies — how an environment
or an agent operates — are deep in understanding and domain, and deserve to be
seen the way decisions are seen: one record each, with lifecycle and provenance, not
lines flattened into a single file. Both changes are cheap exactly now: v2.0.0 has never
been published.

## Decision (clauses)

### DEC-0012_1 — Frame → MentalModel (`MM-`)

The entity's final name is **MentalModel**; filename prefix **`MM-`** under the
universal grammar; container folder `00-context/03-mental-models/` (DEC-0011_2). A
MentalModel is an instrument chosen per problem — first principles, inversion, the vital
few — you hold MANY and apply them deliberately; that is exactly this entity's
semantics, and the name says so unaided. **`FRAME-` joins the retired prefixes** (never
write) alongside `CF-`; the glossary keeps Frame and CognitiveFramework as retired-name
pointers. The Why ring reads **`VAL- / PREF- / MM-`**. This clause amends the
DEC-0008_2_1 table entry; the amendment folds into v2.0.0 (nothing published — the only
trace is the migration alias map).

### DEC-0012_2 — Policy: a canonical entity (`POL-`)

A **Policy** is an **operating rule with scope and enforcement** — MUST / MUST-NOT,
verifiable, blockable. Boundary with its neighbors in the Why ring: a **Value** is a
terminal criterion (where justification stops); a **Preference** is a taste or working
choice; a **Policy** is enforceable and scoped. Prefix `POL-`, universal grammar, stored
`00-context/07-policies/` — a slot DEC-0011_2 reserves for exactly this class of
addition. Frontmatter schema:

```yaml
entity: Policy
status: active | deprecated
scope: environment | agent | corpus | session
enforced-by: [hook | validator | runtime | human]
severity: block | warn
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive
```

Cycle placement: **transversal** — policies are not a stage; they are what the machine
gates of the audit plane enforce (P2 provenance discipline, P6 evidence gates). A
runtime's session-permission grants are Policies with `scope: session` — a vendor
specialization of the canonical entity; vendors MAY extend the scope values in their
own runtimes (Layer C).

### DEC-0012_3 — `_policies.md` is a derived view

The container's `_policies.md` (DEC-0011_5) is **generated** from the active `POL-`
records: the fast summary every agent loads at session start. Truth lives in the
records; the summary is regenerable on change (Determinism-over-Regeneration — the same
discipline P5 applies to plans). Hand-editing the summary instead of its sources is the
anti-pattern.

### DEC-0012_4 — Application

The catalog grows by one entity and every dependent surface updates, folded into
v2.0.0: the catalog README and cycle table (single source, DEC-0008_2_1 as amended),
entity spec files (the frame spec renamed to mental-model; a new policy spec), the
glossary (MentalModel, Policy, policy scope; Frame as retired pointer), naming.md
(prefix table, retired list, alias table), base-schema enums, templates (mental-model
rename; new policy template), the naming validator's canonical and retired sets, and
the counter tooling. Migration maps legacy cognitive-framework artifacts to `MM-` and,
where corpus owners choose, mines operating rules scattered in foundation documents and
agent-context files into `POL-` records.

## Alternatives considered

- **Keep Frame**: cost zero, already ratified in DEC-0008 — rejected by the owner:
  meaning beats inertia while nothing is published; "frame" collides with "framework"
  in every conversation and explains nothing by itself.
- **Mindset**: rejected — pop-psychology register, and it names a person's global
  disposition (you hold one) rather than an instrument you pick per problem (you hold
  many).
- **Lens**: rejected — a second name for a concept the market already calls mental
  models; evocative but less established.
- **Policy as a Capability component (`kind: standard`)**: rejected — a standard is a
  way-of-doing, a competence; a policy is a MUST with scope and enforcement. Different
  nature, different lifecycle.
- **Policies as sections of a single `_policies.md`**: rejected by the owner — flattens
  rules that are deep in domain and understanding; kills per-record lifecycle,
  provenance and supersession.

## Consequences

**Enables**: a self-explanatory Why ring across every audience; a canonical, per-record
rule surface that machine gates can enforce and vendor permission systems can
specialize (Layer C). **Constrains**: every literal stating the catalog size updates
(count-coherence gates catch stragglers); validator and templates update. **Costs**: one
more entity to teach — mitigated because it names something every corpus already had
implicitly (operating rules existed everywhere, homeless).

## Ratification note

Both amendments ratified by the owner in the layout-design conversation (2026-07-13):
MentalModel elected over keeping Frame after an alternatives review with costs stated;
the Policy entity proposed by the owner ("each policy deserves to be seen the way
decisions are seen") and formalized here. Split from DEC-0011 per the independence test
(DEC-0008_9). **Approved by the owner on 2026-07-13**, together with DEC-0011, after the
vendor-vocabulary review (no runtime names in canonical text; scope values extensible in
Layer C).

## References

- [`DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — the amended single-source table (DEC-0008_2_1), the retired-prefix discipline, the clause rule (DEC-0008_9).
- [`DEC-0011-20260713-canonical-corpus-container-and-layout.md`](DEC-0011-20260713-canonical-corpus-container-and-layout.md) — folder homes (`03-mental-models/`, `07-policies/`), `_policies.md` in the underscore family.
- `reference/entity-catalog/` — the catalog these clauses amend.
- `spec/v2.0.0/naming.md` — prefix table, retired list and alias tables receiving the amendment.
