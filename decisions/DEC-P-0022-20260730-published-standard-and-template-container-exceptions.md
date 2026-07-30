---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-30
updated: 2026-07-30
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # origin: three independent DEC-0001s found in one workspace, 2026-07-30
supersedes: []
superseded-by: null
conflicts-with: [DEC-0002-20260514-spec-repo-publishing-layout]
related-decs: [DEC-0011-20260713-canonical-corpus-container-and-layout, DEC-0002-20260514-spec-repo-publishing-layout, DEC-P-0021-20260730-canonical-layout-reconciliation]
topics: [folder-structure, corpus-integrity, counter-discipline, adopter, meta-framework, ip-boundary]
vocabulary-changes: ["published-standard repository (new canonical term)", "clonable-template repository (new canonical term)", "container exemption (new canonical term)"]
consistency-check: |
  Resolves a live conflict between two approved records that never referenced each other.
  DEC-0002 (2026-05-14) gave the spec repository a publishing layout with its own root-level
  `decisions/`. DEC-0011_1 (2026-07-13) then ruled that "code repositories never carry a
  container of their own" and that one product is one corpus with one set of counters, without
  exempting anything. Both stand approved; neither cites the other; the spec repository
  satisfies one by violating the other. This record keeps DEC-0011_1 as the default and adds
  two narrow, criterion-based exemptions rather than weakening the rule — so `conflicts-with`
  names DEC-0002 and the Conflict Resolution section states how it is resolved. DEC-0011_1's
  text is amended by exception only: every repository not meeting a stated criterion remains a
  pointer, and the one-corpus-one-counter rule is unchanged for them. The organization/
  engineering zoom pair (DEC-0011_3, DEC-0011_6) is not modified — clause 1 documents the
  decision procedure that was already implicit in it, because its absence is what let three
  independent counters appear. Three new terms land in the glossary at approval, in the next
  MINOR.
---

# DEC-P-0022 — Container exemptions: published-standard and clonable-template repositories

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1, P2, P12).
> **Status: pending.** Constitutive: it amends the container rule of DEC-0011_1 by exception,
> so it lands only with the human ratification P3 requires.

## Summary

DEC-0011_1 rules that code repositories never carry a container of their own — one product, one
corpus, one set of counters. DEC-0002 had already given the spec repository its own root-level
`decisions/`. Neither record cites the other, and the spec repository cannot satisfy both. This
record keeps DEC-0011_1 as the default, documents the zoom decision procedure that was implicit,
and adds **two narrow exemptions**: a repository whose decisions are part of what it *publishes*,
and a repository that exists to be *cloned* as someone else's independent corpus.

## Context

**The symptom.** The SliceOps workspace holds three independent DEC counters — three different
`DEC-0001` files: 21 in `spec/decisions/`, 51 in the website's `10-decisions/`, one in the
quickstart. That is exactly what "one product = one corpus (one set of counters)" forbids.

**The cause is in the corpus, not the practice.** Two approved records answer the same question
differently:

| Record | Date | Says |
|---|---|---|
| DEC-0002 | 2026-05-14 | the spec repo uses a lightweight **publishing layout** — `spec/ reference/ decisions/ examples/ governance/` — precedent OpenAPI, JSON Schema, PEPs |
| DEC-0011_1 | 2026-07-13 | `_sliceops` is always the container; **code repositories never carry a container of their own**; one product = one corpus |

Cross-references between them: **zero, in both directions.** DEC-0011 was authored two months
later and never revisited DEC-0002. The spec repository has since satisfied one by violating the
other, silently.

**The zoom pair was never given a decision procedure.** DEC-0011_6 defines
`"corpus": "engineering | organization"` and DEC-0011_3 states the zoom rule — an
organization-level corpus holds the WHAT at portfolio zoom and points, never copies, at each
product corpus. What no clause states is **how to tell which one you are looking at**. Adopters
running the pattern correctly in practice could not derive it from the spec, which is how a
workspace ends up with a container at the wrong zoom and repositories filling the vacuum with
counters of their own.

**Why the naive fix is wrong.** Applying DEC-0011_1 literally would move the spec repository's
decisions into a private engineering container. Those decisions *are the standard*: third
parties cite them by URL, the website renders them, they ship under CC BY. They are the
deliverable, not construction residue. A rule that forces a standards body to hide its decision
record has misidentified what the record is for.

The same holds, differently, for the quickstart: it exists to be cloned as an **independent**
corpus. A pointer `{"ref": "../_sliceops"}` in a template resolves to nothing in the clone —
the adopter would inherit a broken reference as their first experience of the framework.

## Decision

**1. The zoom decision procedure (documentation of DEC-0011_3/_6, no change).** Before choosing a
container form, identify the zoom:

| Zoom | `corpus:` | Holds | Test |
|---|---|---|---|
| Organization | `organization` | strategy, company decisions, the product portfolio at `50-products/<product>/definition/` | does it decide *which products exist and why*? |
| Engineering | `engineering` | construction: technical decisions, architecture, specs, execution for **one** product | does it decide *how this product is built*? |

An organization corpus **points, never copies** at each product's engineering corpus. Cross-product
strategy lives at organization zoom — this is what keeps a product from becoming an island, and it
is why per-product corpora do not fragment company strategy.

**2. Default, unchanged.** Every repository inside a product workspace is a **pointer**: minimal
`sliceops.json` (`{"ref": …, "remote": …}`) plus a root agent-context file pointing at the
container. One product = one corpus = one set of counters. Clauses 3 and 4 are the only
exemptions; a repository not meeting their criteria is a pointer.

**3. Exemption A — the published-standard repository.** A repository MAY carry its own container
when **its decision record is part of what it publishes**. Criterion, verifiable and narrow:

- the decisions are a **deliverable**, cited by third parties outside the organization; and
- they ship under the repository's public licence; and
- removing them would break external references.

Such a repository declares `corpus: "engineering"` with `"extensions": {"published-standard":
"<claimant>"}` in its manifest, and its counter is its own. The counter of the workspace container
never absorbs it, so numbers are stable for external citation — which is the point of the
exemption.

**4. Exemption B — the clonable-template repository.** A repository MAY carry its own container
when **its purpose is to be cloned as an independent corpus**. Criterion:

- it is published as a template; and
- the clone is expected to operate standalone, not as a member of this workspace; and
- a pointer would resolve to nothing in the clone.

Declared as `"extensions": {"clonable-template": "<claimant>"}`. Its counter starts at the
template's own `0001` in every clone — that is the intended behaviour, not a collision.

**5. Exemptions are declared, never assumed.** An exempt repository states which exemption it
claims in `sliceops.json` `extensions`. A repository carrying a container without a declared
exemption is drift, and the completeness of the declaration is machine-checkable. **Absence of a
declaration means the default of clause 2 applies.**

**6. DEC-0002 stands.** The spec repository's publishing layout was correct and remains correct;
it is the general rule that lacked the exemption, not this repository that erred. See *Conflict
Resolution*.

## Alternatives considered

- **Amend DEC-0011_1 to drop "code repositories never carry a container of their own"** —
  rejected. The rule is load-bearing: without it every repository accretes its own counters,
  which is the exact failure being fixed. The problem was its absence of exemptions, not its
  existence.
- **Move the spec repository's decisions into the workspace container** — rejected. It would
  break external citations, contradict DEC-0002 without cause, and hide a public standards
  body's decision record inside a private engineering corpus. It also inverts the IP boundary:
  the decisions are Layer A/B public content by construction.
- **Make the spec repository its own product with its own organization corpus** — rejected as
  over-modelling. It is one product's repository; a second organization corpus for it would
  duplicate `~/companies/`-level strategy and reintroduce the copy-not-point failure DEC-0011_3
  forbids.
- **A blanket "public repositories are exempt" rule** — rejected as too wide. The website is
  public and is *not* exempt: its decisions are construction (stack, deploy, copy framing), not
  deliverable. Public is not the criterion; **published-as-deliverable** is.
- **Leave it undecided and let each workspace choose** — rejected. That is the status quo, and
  the status quo produced three `DEC-0001`s in one workspace with no rule violated on its face.

## Conflict Resolution

**vs DEC-0002 (spec repo publishing layout)** — resolved in DEC-0002's favour, scoped. DEC-0002's
layout stands unchanged and is now *authorized* rather than merely tolerated: the spec repository
meets Exemption A on all three criteria (its DECs are cited externally, ship under CC BY, and are
referenced by URL from the website and by adopters). What changes is that the exemption is
declared in `sliceops.json` instead of being implicit, so the next reader of DEC-0011_1 does not
find an unexplained violation. DEC-0011_1's default is untouched for every other repository.

## Consequences

**Enables**: a workspace can be checked for container drift mechanically — any container without
a declared exemption is a finding · external citations of spec decisions stay stable, because the
exemption exists to protect exactly that · adopters get a decision procedure for the zoom pair
instead of having to infer it.

**Constrains**: the two exemptions are exhaustive; a third requires a superseding record · every
exempt repository must declare its exemption · the website and toolkit lose the option of their
own counters and become pointers.

**Costs**: the website's 51 decisions move to the workspace engineering container (they keep
their numbers — the container holds none, so nothing renumbers) · two manifests to write ·
`sliceops.json` in the spec repository and the quickstart gains an `extensions` entry.

**Follow-on, not decided here**: the SliceOps workspace container currently exists only as a local
git repository with no remote. Once it holds the moved decisions it is a single point of failure
until it is published — a `remote` is also required by the pointer manifests of clause 2, which
cannot be completed without it.

## References

- DEC-0011 clauses _1 (container and unit-of-work), _3 (zoom rule), _6 (adoption manifest)
- DEC-0002 — the publishing layout this record authorizes rather than overrides
- DEC-P-0021 — the layout reconciliation that named DEC-0011 the single authority on where
  things live; this record answers the adjacent question of *which corpus* a thing belongs to
- [`spec/latest/naming.md`](../spec/latest/naming.md) §7 (canonical container and layout)
- P12 Context Discipline — single source of truth per fact, which one counter per corpus serves
