---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-30
updated: 2026-07-30
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # maintainer reconciliation of three divergent lines, 2026-07-30
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections, DEC-P-0019-20260730-counter-tooling-branch-and-worktree-blindness]
topics: [counter-discipline, corpus-integrity, naming]
vocabulary-changes: ["withdrawn draft (a re-authoring of an existing decision, removed as a live artifact)", "integration line"]
consistency-check: |
  Resolves a live violation of DEC-0008_5 rule 3 (one counter value = one artifact,
  shared across lifecycle prefixes): counter value 0014 addressed two different files on
  two different branches. Adds no grammar and changes no identifier rule — DEC-0008_5
  stands exactly as written; this record supplies the missing REMEDY for the case the
  rule detects but never says how to repair, and names which of the two artifacts the
  number belongs to. The normative content of DEC-0014 is untouched: both files stated
  the same four clauses, so no clause changes meaning and no corpus artifact's
  conformance moves. What is grafted into the canonical record (clause DEC-0018_2) is
  provenance and evidence only — Context and References prose, no clause text — which is
  why this record does not supersede DEC-0014. No spec version cut: no published
  document changes. DEC-0011 (container layout), DEC-0012, DEC-0013 unaffected.
---

# DEC-P-0018 — One number, one artifact: reconciling the forked DEC-0014 and naming the integration line

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1, P2).
> **Status: pending.** Constitutive: it decides which artifact a spent counter value
> addresses, so it lands only with the human ratification P3 requires.

## Summary

Counter value **0014 addressed two different DecisionRecords** on two different branches
— `DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md` (approved, on `main`)
and `DEC-P-0014-20260728-slice-coordinate-subslice-and-alphabetic-sections.md` (pending,
on `release/v2.1.0`) — violating DEC-0008_5 rule 3. Inspection shows they are not two
decisions that collided on a number: they are **two independent authorings of the same
decision**, stating the same four clauses (`DEC-0014_1` … `DEC-0014_4`) with the same
normative content. The 2026-07-15 record is **canonical** — it claimed the number first
and the entire published line is built on it. The 2026-07-28 record is **withdrawn**, not
renumbered: giving one decision a second number would be the mirror image of the defect
being repaired. Its unique material — the origin handoff and a corrected evidence figure —
is grafted into the canonical record, and `main` is named the **integration line**.

## Context

Three lines diverged from `40ea0d4` (2026-07-14, the DEC-0013 cut) and the DEC counter
forked with them.

**What happened, in order.** On **2026-07-15** the maintainer authored `DEC-0014`
(`9145e86`) and cut spec v2.1.0 from it, then spent 2026-07-16 building on it: the
validator regexes and the anti-`BL` rule, the evidence `sliceId` pattern, the living-docs
sweep, clause `DEC-0014_4` and principles P4/P5, and `DEC-0015`. On **2026-07-28**, on a
branch cut from the same `40ea0d4` and unaware of that work, the decision was authored a
**second time** as `DEC-P-0014` (`1054056`), followed by a second, independent preparation
of spec v2.1.0 (`612de10` — a 595-line glossary, a 314-line principles file, a full
version directory that already existed on `main`).

**Why the number was reissued.** The counter tooling did exactly what it was built to do
and still under-reported: `claim_id.py` re-scans the corpus for the real maximum before
claiming, but it re-scans **one working tree**. On a branch cut from `40ea0d4` the real
maximum visible on disk was 0013, so it issued 0014 — thirteen days after 0014 had been
spent on another branch. The mechanism and the repair belong to a separate record
([`DEC-P-0019`](DEC-P-0019-20260730-counter-tooling-branch-and-worktree-blindness.md));
what matters here is that the corpus is left with one number addressing two artifacts, and
DEC-0008_5 rule 3 detects that condition without saying how to repair it.

**Why this is not an ordinary collision.** The two files are the same decision. Both amend
`DEC-0008_6`; both state a one-letter lowercase sub-slice suffix, alphabetic section codes
that are pure (digits xor uppercase letters) and may not contain `BL`, a numeric `BL`, a
pin-governed dotted retirement, and the sub-slicing rate as a non-gating health signal;
both number those clauses `DEC-0014_1` through `DEC-0014_4` with the same content in each.
They differ in prose, in status, and in date — not in what they oblige. The standard
repair for a collision (renumber the loser) assumes two decisions. Applying it here would
publish the same decision under two numbers, which fails the same rule from the other
side: a reader citing `DEC-0014_2` would have two records to choose between, and the
"short citations are unambiguous within a corpus" guarantee of DEC-0008_5 rule 5 would
break for every clause in the record.

**What the second authoring has that the first does not.** Its provenance. The canonical
record attributes itself to a maintainer review; the withdrawn draft names the actual
origin — a Layer C.1 implementation handoff of 2026-07-15 (ContextPack `kind: handoff`,
DEC-0009) reporting that a third of a production corpus was not expressible under the
published grammar — and it corrects that handoff's own figure, from the reported ~40% (91
of 230) to a re-derived 75 of 229 distinct coordinates, 33%. That correction is a P6 act
(evidence, not the roundest available number) and is the kind of material that must not be
lost when a draft is withdrawn.

## Decision

### DEC-0018_1 — `DEC-0014-20260715-…` is canonical; the 2026-07-28 record is withdrawn

Counter value **0014 addresses
`DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md`**, and only that file.
Three grounds, in order of weight:

1. **First claim.** It claimed 0014 on 2026-07-15, thirteen days before the second
   authoring. A counter is a serialized shared resource (P9); the first claim holds it.
2. **Merged, immutable history depends on it.** The v2.1.0 cut, the validator regexes, the
   evidence `sliceId` pattern, `DEC-0015`, `DEC-P-0016`, `DEC-P-0017`, the CHANGELOG's
   released `[2.1.0]` section and spec v2.2.0 all cite it by its full filename.
   Renumbering it would rewrite identifiers already merged — precisely what DEC-0008_5's
   immutable-date rule and DEC-0014_1's own "renumbering rewrites identifiers already in
   branches, commits and trackers" argument forbid.
3. **It is ratified.** It carries `status: approved` with an `approver:`; the other is
   `pending`. A pending draft never displaces an approved record.

`DEC-P-0014-20260728-slice-coordinate-subslice-and-alphabetic-sections.md` is **withdrawn
as a live artifact**. It is not renumbered to a free counter value: it states no decision
that `DEC-0014` does not already state, so a new number would create a second record of
one decision — two numbers for one artifact, the same rule failing from the other side.

### DEC-0018_2 — Withdrawal absorbs, it never discards

A withdrawn draft's unique material is **grafted into the canonical record before the
draft stops being a live artifact**. Concretely, for this case:

1. The **origin** — the Layer C.1 implementation handoff of 2026-07-15 — is recorded in
   `DEC-0014`'s Context and References, replacing the thinner "maintainer review"
   attribution.
2. The **corrected evidence** — 75 of 229 distinct coordinates (33%): 65 alphabetic
   sections, 25 sub-slices, 15 hitting both gaps and counted twice by the handoff's ~40%
   (91/230) figure, with one malformed identifier that is not a coordinate — is recorded
   with the correction stated as a correction (P6).
3. The **withdrawal note** in `DEC-0014` names the withdrawn draft, its commit
   (`1054056` on `release/v2.1.0`), and this record, so the trail resolves from the
   canonical artifact without the draft being present.

Only **non-normative** material is grafted — Context and References prose. No clause text
is altered: an approved constitutive record's normative content is not editable by a
reconciliation. Where the two authorings said the same thing in different words, the
canonical wording stands.

**Not grafted, and why.** The withdrawn draft's `DEC-0014_4` carried one addition the
canonical clause does not: *"No canonical threshold is set. One corpus has reported a
measurement (≈11%, n=229). A threshold derived from a single corpus would be invention
presented as evidence — the opposite of P6. Revisit when at least three corpora have
reported."* This is **normative** — it commits the framework to a revisit condition — so it
is outside what this clause permits a reconciliation to add. It is recorded here rather
than dropped: whoever wants the sub-slicing-rate threshold governed should raise it as its
own record, on its own number, against its own evidence. Withdrawing a draft may not
smuggle a rule in through the graft, and it may not lose one through silence either.

**The general rule**: when two artifacts hold one counter value and state **one** decision,
the first claim is canonical and the other is withdrawn under this clause. When they state
**two** decisions, the first claim keeps the number and the second is **renumbered** to a
freshly claimed value, keeping its own date per DEC-0008_5 rule 2. Deletion without a
recorded rationale is not available in either case; git history is the archive, and the
canonical record carries the pointer.

### DEC-0018_3 — `main` is the integration line; `release/v2.1.0` is retired by salvage

`main` (= `origin/HEAD`) is the **integration line**. It carries the highest corpus state
(`spec/latest` → v2.2.0, decisions through 0017) and both `fix/` branches are already
merged into it:
`fix/spec-level-vocabulary-and-agents-drift` has a zero-byte content diff against `main`,
and `fix/topic-taxonomy-naming-and-back-edges` is strictly **behind** it — its residual
diff consists only of `main`'s newer DEC-P-0017 work that the branch has not received.
Neither needs merging; both are stale refs, deletable once their pull requests close.

`release/v2.1.0` is **not merged**. It is 3 commits ahead and 10 behind, and its content is
a duplicate preparation of a version `main` has already published and superseded: merging
it would regress `spec/latest` from v2.2.0 to v2.1.0, delete `spec/v2.2.0/`, and reinstate
the withdrawn draft. It is reconciled by **salvage** — one artifact travels to the
integration line, the rest is superseded:

| From `release/v2.1.0` | Disposition |
|---|---|
| `DEC-P-0014-20260728-…` | Withdrawn (DEC-0018_1); material absorbed (DEC-0018_2) |
| `612de10` — second v2.1.0 preparation | Superseded by `main`'s v2.1.0 (published) and v2.2.0 |
| `74ddb56` — re-vendored `naming_validator.py` + column-0 guard | **Salvaged** — see below |
| `16d2796` — AGENTS.md drift propagation | Already on `main` |

The salvage is not incidental. `main`'s vendored `.claude/hooks/naming_validator.py` sits
**155 lines** from the toolkit upstream it is a copy of, and still cites clause identifiers
in the dotted form (`DEC-0008.5`) that **DEC-0013 retired** in favour of the underscore —
a pre-write gate emitting the notation the corpus forbids. The `release/v2.1.0` copy is the
toolkit upstream plus an 8-line column-0 guard (top-level YAML keys only, so a vendor's
indented `*-entity-mapping:` block is not misread as a catalog signal). That guard is not
yet upstream in the toolkit; carrying it to the integration line is a **declared follow-up**
against `sliceops-toolkit` — a vendored fix that never travels home is the drift this table
exists to end.

### DEC-0018_4 — The counter reconciles to the cross-branch maximum, never the local one

`.counters/dec.txt` on the integration line is reconciled to the **real maximum across all
refs**, not the maximum visible in one working tree. At the time of this record that
maximum is **0017** (`DEC-P-0017` on `main`); `release/v2.1.0` carried `14`, which is the
fork's artifact and is retired with the branch. This record claims **0018** and its sibling
[`DEC-P-0019`](DEC-P-0019-20260730-counter-tooling-branch-and-worktree-blindness.md)
claims **0019**, both verified against every ref rather than against a single checkout;
`.counters/dec.txt` moves to `0019`.

The verification was performed by hand because the tool that should perform it cannot yet
see other branches. That is the defect, not the workaround, and it is recorded as
DEC-0019_1 rather than left as folklore in a commit message.

## Alternatives considered

- **Renumber the 2026-07-28 record to a free value (0018) and keep both**: rejected. They
  are one decision. Two numbers for one decision breaks DEC-0008_5 rule 5's guarantee that
  a short citation is unambiguous within a corpus — `DEC-0014_2` would resolve to two
  records — and leaves the corpus permanently carrying a duplicate whose only distinction
  is prose style. Renumbering is the right repair when two *decisions* collide; that is
  written into DEC-0018_2 as the general rule, and this is not that case.
- **Make the 2026-07-28 record canonical and renumber the 2026-07-15 one**: rejected. It
  would rewrite an identifier cited across merged history, a released CHANGELOG section,
  three later decisions and two published spec versions, to prefer a pending draft over an
  approved record. The richer prose does not outweigh that; the richer prose is portable,
  and DEC-0018_2 ports it.
- **Merge `release/v2.1.0` into `main` and resolve conflicts file by file**: rejected. Its
  v2.1.0 is a parallel preparation of a version already published from `main`, and the
  merge would regress `spec/latest`, delete `spec/v2.2.0/` and reinstate the withdrawn
  draft. The one artifact worth keeping is a vendored file; salvage is the proportionate
  operation, and the table in DEC-0018_3 records what was examined and dropped rather than
  leaving "superseded" to be inferred from silence.
- **Delete the duplicate quietly and reconcile the counter in a commit message**: rejected
  outright — it is the failure mode this framework exists to prevent. An audit reading the
  corpus would find a number that skipped an artifact with no explanation, and the
  corrected 33% evidence figure would be lost with the file. P2 (audit plane discipline)
  makes the rationale an artifact, not a commit message.
- **Rename the withdrawn draft to `DEC-D-0014-20260728-…`** (the deprecated lifecycle
  prefix): rejected — it does not resolve the violation. DEC-0008_5 rule 3 shares one
  counter across lifecycle prefixes precisely so that a `DEC-D-0014` colliding with a
  `DEC-0014` is a *detected error*; the rename would leave the corpus in exactly the state
  being repaired, with the collision re-labelled rather than removed.

## Consequences

**Establishes**: counter value 0014 addresses exactly one artifact; a named remedy for the
case DEC-0008_5 rule 3 detects but never resolved, split by whether the colliding artifacts
hold one decision (withdraw) or two (renumber); withdrawal as an **absorbing** operation
that may never discard unique material; `main` as the integration line with `release/v2.1.0`
retired by an itemized salvage table.

**Enables**: `DEC-0014` now carries its real provenance — a Layer C.1 handoff and a
corrected, honest evidence figure — instead of a thin self-attribution; the integration
line picks up a pre-write hook that no longer emits the clause notation DEC-0013 retired.

**Constrains**: counter reconciliation on an integration line reads **all refs**, never one
working tree (DEC-0018_4); a withdrawn draft's unique material is grafted **before**
withdrawal, and the canonical record must name the withdrawn file, its commit and this
record.

**Costs**: one non-normative edit to an approved constitutive record (bounded by
DEC-0018_2 to Context and References); `release/v2.1.0`'s independent v2.1.0 preparation is
discarded work — the true cost of the fork, and the argument for DEC-P-0019; the column-0
guard is owed upstream to `sliceops-toolkit` as a declared follow-up.

## References

- [`DEC-0008`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — clause
  DEC-0008_5, the universal grammar: rule 1 (counters as a P9 shared resource, re-scan
  before claiming), rule 2 (the immutable date), rule 3 (one counter per entity shared
  across lifecycle prefixes — the rule this reconciliation repairs), rule 5 (short
  citations unambiguous within a corpus).
- [`DEC-0014`](DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md) — the
  canonical record this reconciliation confirms and grafts into.
- [`DEC-P-0019`](DEC-P-0019-20260730-counter-tooling-branch-and-worktree-blindness.md) —
  the tooling defect that let one counter value be issued twice, and its repair.
- [`DEC-0005`](DEC-0005-20260702-author-approver-separation.md) — P3 author≠approver; why
  this record ships `pending` with `approver: null`.
- [`governance/PROPOSAL-PROCESS.md`](../governance/PROPOSAL-PROCESS.md) — the ratification
  path; step 3 (reciprocated `related-decs` edges as a Layer 2 pre-merge requirement).
- Withdrawn draft: `DEC-P-0014-20260728-slice-coordinate-subslice-and-alphabetic-sections.md`,
  commit `1054056` on `release/v2.1.0` — retrievable from git history, which is the archive.
