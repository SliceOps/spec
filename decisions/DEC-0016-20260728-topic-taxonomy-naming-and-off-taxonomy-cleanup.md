---
entity: DecisionRecord
status: approved
kind: constitutive
created: 2026-07-28
updated: 2026-07-30
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra   # ratified 2026-07-30 (P3)
sensitivity: public
originating_slice: null     # origin: maintainer-reported red consistency gate on main, 2026-07-28
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0011-20260713-canonical-corpus-container-and-layout, DEC-0012-20260713-catalog-amendments-mental-model-and-policy, DEC-0013-20260713-clause-identifier-separator-underscore, DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections]
topics: [naming, meta-framework, consistency-management, corpus-integrity]
vocabulary-changes: ["naming (canonical topic)"]
consistency-check: |
  Adds ONE entry to the canonical topic taxonomy — `naming` — and changes nothing else in
  it. Purely additive: no existing topic is renamed, merged, split or removed, and no
  `topics:` value that was valid under v2.1.0 becomes invalid, so this is a SemVer MINOR
  and ships as spec v2.2.0 (released versions are immutable; v2.1.0 and every earlier cut
  stay frozen and are their own alias note). The taxonomy is a Layer B.1 framework artifact,
  not a Layer A principle, so this needs a ratified DEC but not the elevated P3 gate that
  `principles.md` amendments require. No catalog entity, prefix, required field, grammar
  rule or lifecycle rule is touched, so no clause of DEC-0008 and none of DEC-0009 through
  DEC-0015 is amended — the four records this one is related to (DEC-0011, DEC-0012,
  DEC-0013, DEC-0014) keep every word of their decisions; only the taxonomy that their
  `topics:` values are validated against grows. Clause DEC-0016_2 records the three
  off-taxonomy values that were mislabels rather than gaps and were corrected fix-on-touch
  (P12) in the same slice. Clause DEC-0016_3 repoints the CI taxonomy pin, which had drifted
  two versions behind the corpus. No IP-boundary or licensing impact — public Layer B.1
  metadata only.
---

# DEC-0016 — `naming` becomes a canonical topic; three off-taxonomy values corrected

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1 — Decision
> Integrity by Construction, P2 — Audit Plane Discipline). **Status: approved**, ratified by
> the maintainer on 2026-07-30 (P3; `approver:` set — DEC-0005: self-ratification is explicit,
> never silent). Drafted by an AI agent and therefore untrusted until human-reviewed
> (`AGENTS.md`, P3); it is a constitutive record amending a Layer B.1 canonical artifact.

## Summary

The canonical topic taxonomy has no entry for **naming** — the framework's own identifier
standard — even though `naming.md` is one of the six canonical spec documents and four
approved constitutive records tag themselves `naming`. This record adds `naming` as a
top-level topic under `meta-framework`, shipping as spec **v2.2.0** (additive, backwards
compatible). It also records the disposition of the three *other* off-taxonomy values found
in the same sweep — `glossary`, `enforcement`, `adoption` — which were mislabels of concepts
the taxonomy already covers, not gaps, and were corrected in place.

## Context

The `[topic-tags]` consistency check — one of the gates this repository publishes and runs
against itself — has been red on `main` since before the v2.1.0 work: seven violations
across four approved DECs, declaring four distinct topic values absent from the canonical
taxonomy.

The check is not noise. It exists so that the Layer 2 pre-merge question — *"which prior
decisions touch this topic?"* — has a reliable answer. A `topics:` value outside the canon
is invisible to that search, so the drift it causes is exactly the drift the taxonomy exists
to prevent.

**Root cause.** `topics.md` is byte-identical from v1.1.0 through v2.1.0 (its only change in
that span was the `brain-pack-injection` → `context-pack-injection` rename in v2.0.0). It
therefore **predates DEC-0008**, the record that created the universal identifier grammar and
made `naming.md` normative in the v2 re-founding. The taxonomy never caught up with v2. Four
records reached for a `naming` topic that the v2 work should have created and did not:
DEC-0011, DEC-0012, DEC-0013 and DEC-0014.

**Why `naming` is a genuine gap and not a mislabel.** Four independent lines of evidence:

1. **The taxonomy contradicts itself.** The `meta-framework` entry defines its own scope as
   *"decisions about the framework itself — taxonomy, **naming**, consistency management,
   vocabulary discipline"* and lists five sub-topics. Four of the facets it names have a
   `###` entry of their own. `naming` is the only one that does not.
2. **A canonical artifact with no topic.** `spec/vX.Y.Z/naming.md` is normative since v2.0.0
   and one of six canonical spec documents. Every other one is covered: `principles.md` →
   `principles`, `glossary.md` → `vocabulary-discipline`, `ip-boundary.md` → `ip-boundary`,
   `topics.md` → `meta-framework`. Only `naming.md` has no home.
3. **Convergent demand.** Four approved constitutive records independently chose the same
   word. The taxonomy's own Maintenance rule treats that as the trigger to add a topic —
   subject to the justification this section supplies.
4. **No existing entry fits.** The three nearest candidates are each a different concept:
   - `hierarchical-taxonomy` — scope is the **Layer A/B/C layer taxonomy** and its
     sub-numbering (B.1, C.2). That is what the *layers* are called, not how *artifacts* are
     identified. It also has zero users anywhere in the corpus.
   - `vocabulary-discipline` — scope is **term canonicity**: what a concept is called in
     prose. DEC-0013 (clause-citation separator, `.` → `_`) introduces no term and renames no
     concept; it changes an identifier's punctuation. Different axis.
   - `meta-framework` — the parent. It is what DEC-0013 and DEC-0014 already fall back to,
     and it is too coarse to answer the Layer 2 query: `meta-framework` spans taxonomy,
     consistency management and vocabulary as well.

**The other three values are the opposite case.** `glossary`, `enforcement` and `adoption`
each name a concept the taxonomy already carries under its canonical name — the exact
one-concept-two-names drift P12 prohibits. They needed correction, not accommodation.

## Decision (clauses)

### DEC-0016_1 — `naming` is a canonical top-level topic under `meta-framework`

Added to `topics.md` in the "Meta-framework" group, in the taxonomy's per-topic structure:

- **Scope**: Decisions about the canonical identifier standard — the universal grammar
  (`PREFIX-NNNN-YYYYMMDD-slug`), one entity = one prefix, the slice coordinate, clause
  identifiers, reserved infrastructure names, retired prefixes and alias tables. The
  *identifier* axis; term canonicity in prose is `vocabulary-discipline`, and the Layer
  A/B/C layer naming is `hierarchical-taxonomy`.
- **Parent**: meta-framework
- **Sub-topics**: universal-grammar, entity-prefix, slice-coordinate, clause-identifier,
  reserved-names, alias-tables
- **Cross-references**: meta-framework, vocabulary-discipline, hierarchical-taxonomy,
  corpus-integrity

The four records already tagged `naming` — DEC-0011, DEC-0012, DEC-0013, DEC-0014 — become
conformant on approval with no edit to any of them. That is the test this clause is designed
to pass: a taxonomy addition that requires rewriting the records that motivated it would be
evidence the addition is wrong.

### DEC-0016_2 — The three mislabels are corrected to their canonical entries (fix-on-touch)

Applied in this slice as P12 fix-on-touch, recorded here so the audit plane carries the
reasoning and the approver can reverse any of the three:

| Record | Was | Now | Why |
|---|---|---|---|
| DEC-0011 | `adoption` | `adopter` | The taxonomy's entry for the adoption axis — sub-topics `retroactive-adoption`, `born-on-sliceops`; DEC-0011's `sliceops.json` adoption manifest and presence activation land squarely in it. |
| DEC-0012 | `glossary` | `vocabulary-discipline` | Whose scope *is* the glossary — `glossary-coverage` is one of its three sub-topics. `glossary` was a second name for an existing topic. |
| DEC-0012 | `enforcement` | `r-rules` | "The R-rules system — enforced CI merge gates": the count-coherence gates DEC-0012's own `consistency-check` invokes. |

The `enforcement` → `r-rules` mapping is the one judgment call; `consistency-management` was
the alternative, since the count-coherence gates are consistency validators. `r-rules` wins on
specificity — `consistency-management` already carries `r-rules-validators` as a sub-topic,
making `r-rules` the more precise node, and DEC-0012's other tags (`entity-catalog`) are
specific rather than parent-level. Reversible by the approver without touching this record's
other clauses.

No new topic is created for any of the three. Growing the taxonomy where an entry already
exists is precisely the over-granularity the Quarterly Curation ritual exists to undo.

### DEC-0016_3 — Ships as spec v2.2.0; the CI taxonomy pin moves with it

`spec/v2.2.0/` is cut from v2.1.0 with `topics.md` as the only changed document. **MINOR**,
not patch: the change adds a value adopters may legally declare, which is an addition to the
framework contract, not a clarification. Backwards-compatible — no `topics:` value valid
under v2.1.0 becomes invalid. `spec/v2.1.0/` and every earlier cut stay frozen; this record
is their forward note.

The CI gate pinned `--topic-taxonomy spec/spec/v2.0.0/topics.md` while the corpus had moved
to v2.0.1 and then v2.1.0. Harmless so far only by luck — the file happened to be
byte-identical across those cuts — but it silently decoupled the published gate from the
published spec, and it would have made this very amendment invisible to CI. The pin moves to
the current version in the same change, and moving it is hereby part of cutting any future
version.

## Alternatives considered

- **Retag the four `naming` uses to `vocabulary-discipline`** — rejected. It would make the
  taxonomy assert that DEC-0013 (a punctuation change to a citation format) is a decision
  about term canonicity. Cheapest to execute, and it silences the check, but it buys a green
  gate by recording something false in the audit plane.
- **Retag to `hierarchical-taxonomy`** — rejected. That entry already means the Layer A/B/C
  layer taxonomy. Overloading one topic name with two unrelated meanings is the P12 violation
  the taxonomy is supposed to prevent. (Its zero usage makes it *available*, not *applicable*
  — an unused topic is a candidate for the curation ritual, not a landfill.)
- **Retag to `meta-framework` alone** — rejected. Not false, merely useless: it is the parent
  of four other facets, so the Layer 2 search "which decisions govern the identifier
  grammar?" returns the vocabulary, consistency and taxonomy records as well. The taxonomy's
  Maintenance rule names over-broad topics as a decomposition trigger.
- **Add `naming` as a sub-topic line under `meta-framework` instead of a `###` entry** —
  rejected on two grounds. Sub-topics are prose, not addressable nodes; and the validator's
  canon is built from `^### ` headings, so a sub-topic would leave all four records
  non-conformant. It would look like a fix and change nothing.
- **Add all four values (`naming`, `glossary`, `enforcement`, `adoption`) as topics** —
  rejected. Three of them duplicate existing entries. It would green the gate while
  degrading the taxonomy into a tag cloud, where the same decision is findable under two
  names and reliably found under neither.
- **Add `naming` as a canonical topic; correct the other three** — **selected.** Treats the
  gap as a gap and the mislabels as mislabels, and is the only option under which every
  `topics:` value in the corpus is both valid and accurate.

## Consequences

**Enables**: the Layer 2 pre-merge search finally resolves for the identifier standard — the
most-amended area of the v2 corpus (DEC-0008, DEC-0011 through DEC-0014); `naming.md` gains
the topic every other canonical spec document already had; the `[topic-tags]` gate returns to
green with no record misdescribed.

**Constrains**: `naming` and `vocabulary-discipline` must stay distinct on the identifier /
term-canonicity line, which future DECs have to respect (the scope text above is the
tiebreaker); adopters extending the taxonomy inherit `naming` as reserved.

**Costs**: one more spec version directory to carry (six documents, one of them changed); the
CI pin and `spec/latest` move; adopters pinned to ≤2.1.0 do not see `naming` until they raise
their pin — per DEC-0014_3 they are not in violation while pinned.

**Deliberately out of scope** — around twenty living documents (`AGENTS.md`, `README.md`,
`governance/PROPOSAL-PROCESS.md`, most of `reference/entity-catalog/` and
`reference/templates/`, `reference/r-rules/layer-3-validators.md`) cite the normative source
as `spec/v2.0.1/…` or `spec/v2.0.0/…`. That drift predates this record — it was already one
version stale against v2.1.0 — and the links still resolve, since frozen versions are
retained. Sweeping them here would bury this amendment in an unrelated twenty-file diff, and
a blind sweep to `v2.2.0` only re-creates the same drift at the next cut. The real question
is whether living docs should cite a pinned version at all or route through `spec/latest`
(which exists for exactly this) — a `context-discipline` decision of its own, worth its own
record. Noted here so the audit plane shows it was seen, not missed. `_index.md` is the one
exception swept in this slice: it is the corpus entry point whose stated contract is that its
routes name current canon (DEC-0010_4).

## Ratification

Pending. On approval: rename `DEC-0016-…` → `DEC-0016-…`, set `status: approved` and
`approver:`, and rewrite the references in `CHANGELOG.md`, `spec/README.md` and
`spec/v2.2.0/topics.md` in the same atomic change (R5). The spec v2.2.0 material is
**prepared, not ratified** — it is staged in this branch so that approval is a rename and a
status flip rather than a second authoring pass.

If the approver rejects clause DEC-0016_1, the four `naming` tags must instead be retagged
(the first alternative above) and this record becomes `DEC-D-`. Clause DEC-0016_2 stands
independently of that outcome: those three corrections are valid under the v2.1.0 taxonomy
as it already exists.

## References

- [`spec/v2.2.0/topics.md`](../spec/v2.2.0/topics.md) — the amended taxonomy (prepared).
- [`spec/v2.1.0/topics.md`](../spec/v2.1.0/topics.md) — the taxonomy this record amends (frozen on cut).
- [`spec/v2.1.0/naming.md`](../spec/v2.1.0/naming.md) — the canonical artifact the new topic covers.
- [`DEC-0008`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — created the universal identifier grammar (clause DEC-0008_5) and the slice coordinate (DEC-0008_6); the taxonomy never caught up with it.
- [`DEC-0011`](DEC-0011-20260713-canonical-corpus-container-and-layout.md), [`DEC-0012`](DEC-0012-20260713-catalog-amendments-mental-model-and-policy.md), [`DEC-0013`](DEC-0013-20260713-clause-identifier-separator-underscore.md), [`DEC-0014`](DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md) — the four records tagged `naming`.
- [`governance/PROPOSAL-PROCESS.md`](../governance/PROPOSAL-PROCESS.md) — the route this record follows; step 3 is the bidirectional cross-reference requirement restored in the same slice.
- P12 — Context Discipline (one concept, one name); P9 — Shared-Resource Pre-flight (counter 0016 claimed via `claim_id.py` after a real re-scan).
