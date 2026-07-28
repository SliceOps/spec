---
entity: DecisionRecord
status: approved
kind: constitutive
created: 2026-07-15
updated: 2026-07-15
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
originating_slice: null   # maintainer review of the SLC coordinate against real corpora, 2026-07-15
supersedes: [DEC-0008_6]
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0013-20260713-clause-identifier-separator-underscore, DEC-0015-20260716-p1-statement-provenance-axis-clarity]
topics: [naming, meta-framework]
vocabulary-changes: ["slice coordinate sub-slice suffix (SLC…[a-z])", "alphabetic section code (SEC…[A-Z])"]
consistency-check: |
  Amends the slice-coordinate grammar of DEC-0008_6 additively — every coordinate valid
  under DEC-0008_6 stays valid, so this is a backwards-compatible extension, not a break.
  Three clauses: (1) restores the OPTIONAL one-letter sub-slice suffix that the legacy
  dotted form BL-NN[.SEC-NN].SL-NNN[a-z] already carried (see reference/evidence/evidence-v1.md,
  whose sliceId pattern kept the [a-z] suffix on the dotted side) — its absence from the
  SLC coordinate was a regression against that precedent; (2) admits ALPHABETIC section
  codes alongside numeric ones, each PURE (a section code is all digits OR all uppercase
  letters, never mixed), with the single normative constraint that an alphabetic code
  MUST NOT contain the substring BL (the one parse-ambiguity source against the BL block
  qualifier — the validator rejects it at write time); (3) states that retirement of the
  legacy dotted recognizer binds a corpus only once it adopts a spec version ≥2.0.1, so
  corpora still pinned to 2.0.0 are not in violation and migrate when they raise their pin
  (the sliceops.json pin governs). BL stays numeric. Preserves DEC-0008_6's letters-as-
  separators philosophy (no dots, no inner hyphens) and DEC-0013's separator philosophy.
  The immutable-history rule of DEC-0008_6 is unchanged. Ships as spec v2.1.0 — a MINOR
  version (additive, backwards-compatible: no previously valid id becomes invalid), the
  first minor of the v2 line. Frozen zones (spec/v1.x, spec/v2.0.0, spec/v2.0.1,
  99-archive folders, git history) keep the grammar they were published with; this record
  is their forward note. No conflict with licensing or the IP boundary.
---

# DEC-0014 — Slice Coordinate: Sub-Slice Suffix and Alphabetic Section Codes

> A SliceOps DecisionRecord about SliceOps itself. Raised and ratified by the maintainer on
> 2026-07-15 after using the SLC coordinate against real corpora.

## Summary

The slice coordinate gains two expressive powers it lost in the move off the dotted form,
plus a rule that keeps the grammar unambiguous. A coordinate may carry an **optional
one-letter sub-slice suffix** (`SLC0010b`) — restoring the `[a-z]` tail the legacy dotted
`BL-NN[.SEC-NN].SL-NNN[a-z]` already had. A **section code may be alphabetic** as well as
numeric (`SLC0034SECDOC` next to `SLC0012SEC03BL02`), because real corpora label sections
by meaning, not only by number. To keep parsing single-valued, a section code is **pure**
— all digits or all uppercase letters, never mixed — and an alphabetic code **must not
contain the substring `BL`**, the one string that could be read as the block qualifier.
`BL` stays numeric. Every coordinate valid before this record stays valid: it ships as a
backwards-compatible **minor**, spec v2.1.0.

## Context

Two gaps surfaced once the SLC coordinate met corpora that had been running the pattern in
its earlier, dotted shape:

- **Sub-slices lost their suffix.** A slice frequently subdivides mid-implementation — one
  planned unit of work splits into an `a` and a `b` part that must stay addressable
  without renumbering everything around them. The legacy dotted coordinate carried this as
  a trailing lowercase letter (`…SL-NNN[a-z]`); the SLC coordinate of DEC-0008_6 dropped
  it. That was a **regression**, not a deliberate simplification — the expressive need
  predates the SLC cut and is documented in the evidence record's `sliceId` pattern, which
  retained the `[a-z]` suffix on its dotted alternative (see
  [`../reference/evidence/evidence-v1.md`](../reference/evidence/evidence-v1.md)).
- **Section codes are often semantic, not numeric.** Corpora label the sections of a body
  of work by what they *are* — a documentation section, an operations section, an
  interface section — and a purely numeric section code forces an opaque lookup table onto
  what the author already has a name for. The dotted form technically allowed only numeric
  sections too, but the friction became visible only at SLC scale.

Neither gap justifies a new identifier; both are amendments to one existing coordinate. The
question DEC-0008_6 answered (letters as separators, no dots, no inner hyphens, regex-clean
in git refs and `.md` filenames) is untouched. What changes is the *alphabet* two of its
components may draw from — and one guard rail that keeps the whole thing unambiguous.

## Decision

Amends clause DEC-0008_6. The coordinate grammar becomes:

```
SLC0012SEC03BL02        full numeric coordinate (unchanged)
SLC0034                 simple form (unchanged)
SLC0010b                sub-slice suffix — one optional lowercase letter
SLC0010bSECAPIBL02      sub-slice + alphabetic section + block
SLC0001bSEC21BL06       sub-slice + numeric section + block
SLC0034SECDOC           alphabetic section, no block
```

Formally: `^SLC\d{4,}[a-z]?(SEC(\d{2,}|[A-Z]{2,}))?(BL\d{2,})?$`.

### DEC-0014_1 — The sub-slice suffix (regression fix)

A coordinate MAY carry exactly **one optional lowercase letter** immediately after the
slice number (`SLC0010b`), denoting a sub-slice — a unit that split off an existing slice
mid-implementation without renumbering its neighbours. This restores the expressiveness of
the legacy dotted `…SL-NNN[a-z]` tail (the precedent). **Exactly one** letter: `SLC0010ab`
(two letters) is invalid, and an uppercase suffix (`SLC0010B`) is invalid — suffixes are
lowercase, keeping the sub-slice letter visually distinct from the uppercase section
alphabet introduced next.

### DEC-0014_2 — Alphabetic section codes, pure, and the anti-`BL` constraint

A section code (`SEC…`) MAY be **alphabetic** (uppercase letters, `[A-Z]{2,}`) as well as
**numeric** (`\d{2,}`). Two constraints keep it unambiguous:

1. **Purity** — a section code is *all digits* or *all uppercase letters*, never mixed.
   `SECAPI` and `SEC03` are valid; a mixed code such as `SECA1B2` is not. Purity is what
   lets a reader (and the validator) tell a numeric code from an alphabetic one without a
   lookahead.
2. **No `BL` substring in an alphabetic code** — an alphabetic section code MUST NOT
   contain the two-letter sequence `BL`, because `BL` opens the block qualifier and is the
   single source of parse ambiguity between "section letters" and "start of the block
   field". A code like `SECTABLE` (the alphabetic run `TABLE` contains `BL`) is therefore
   rejected **at the point of write** by the naming validator, which names the constraint
   in its message. The rule is simply that the chosen letters must not spell `BL`
   anywhere; codes such as `SECDOC`, `SECAPI`, `SECOPS` are fine. The block qualifier `BL`
   itself **remains numeric** (`BL\d{2,}`), unchanged.

### DEC-0014_3 — Applicability of the dotted-recognizer retirement (pin-governed)

DEC-0008_6 retired the dotted coordinate. This clause states *when* that retirement binds
a given corpus: **only upon adopting a spec version ≥2.0.1**. A corpus whose adoption
manifest (`sliceops.json`) still pins **2.0.0** is **not in violation** for carrying the
dotted form; it migrates to the SLC coordinate when it raises its pin. The version pin
governs which era's rules apply — retirement is a property of the adopted version, not a
retroactive obligation. (The legacy dotted *recognizer* is simultaneously widened, in this
same release, so migration tooling can SEE the sub-slice and alphabetic-section forms in
old dotted coordinates that were previously invisible to it:
`^BL-?\d+\.SEC-?(\d+|[A-Z]+)\.SL-?\d+[a-z]?$`.)

### DEC-0014_4 — The sub-slice as instrument: rate is a health signal

The sub-slice suffix (DEC-0014_1) is not merely permitted syntax; it carries a meaning the
framework reads. A sub-slice is **the plan correcting itself against reality** — a unit of
granularity that emerged *in execution* after its parent's coordinate was already claimed
(coordinates are monotonic and merged history is immutable, so the child takes a suffix, not
an inserted number). A plan is a hypothesis stated at one altitude; the true granularity of
the work is discovered only by doing it, which is why a slice sometimes subdivides after the
fact rather than being enumerated up front. Two consequences bind:

1. **Emergent, not batch.** The suffix is for work that *emerged* bound to a parent slice —
   a necessary adjacent fix, a discovered reconciliation. Foreseeable fan-out (a batch whose
   leaves are enumerable before work begins) is planned as numbered **sibling** slices, not
   sub-sliced after the fact. Using the suffix to enumerate a known batch is misuse that
   inflates the signal below.
2. **Rate is observable and read as health.** The proportion of a corpus's slices carrying a
   sub-slice suffix is a signal about its planning altitude: low and concentrated in
   inherently-emergent work (tooling, cleanup, meta) is healthy; rising, or spreading into
   the plannable core of the build, means slices are being cut too coarse. Corpora keep this
   rate **observable** — a sweeper metric, not a hard gate (announced, not cut, per P9).

The principle-level statement of this lives in [`../spec/v2.1.0/principles.md`](../spec/v2.1.0/principles.md)
P4 (atomicity under emergence) and P5 (the plan is a hypothesis; leaves are discovered in
execution). This clause is the decision that binds the concept to the coordinate.

## Alternatives considered

- **Leave the SLC coordinate as-is and tell authors to renumber sub-slices**: rejected —
  it discards an expressiveness the legacy form had, forces churn on stable neighbours, and
  ignores the documented precedent. A grammar that loses a capability its predecessor
  carried is a regression to fix, not a simplification to defend.
- **Allow mixed alphanumeric section codes** (`SECA1`): rejected — mixing destroys the
  "digits xor letters" purity that lets numeric and alphabetic codes be told apart without
  a lookahead, and re-introduces exactly the parse fragility the letters-as-separators
  design exists to avoid.
- **Allow `BL` inside alphabetic section codes and disambiguate by longest-match**:
  rejected — relying on backtracking/longest-match to resolve `…BL…` is precisely the kind
  of tooling-dependent fragility DEC-0008_6 and DEC-0013 removed elsewhere; a flat write-
  time prohibition is deterministic and explainable in one line.
- **Multi-letter sub-slice suffixes** (`SLC0010ab`): rejected — one letter matches the
  precedent and covers the real need (a slice splitting into a handful of parts); more than
  one letter invites collision with the uppercase section alphabet and buys no expressiveness
  a fresh slice number would not.

## Consequences

**Establishes**: the sub-slice as a first-class concept the framework reads, not just
tolerated syntax — emergent-granularity notation (a leaf discovered in execution after the
parent's coordinate was spent) whose *rate* is a health signal for planning altitude, with
the emergent-vs-batch rule that keeps the signal honest (clause DEC-0014_4; principle
statement in principles.md P4/P5). **Enables**: sub-slices addressable without renumbering
(the regression is closed); section codes that read as what they mean; migration tooling
that can finally see the sub-slice and alphabetic-section shapes inside legacy dotted
coordinates. **Constrains**:
section codes stay pure (digits xor uppercase letters) and alphabetic ones may not spell
`BL`; sub-slice suffixes are a single lowercase letter; `BL` stays numeric — the validator
enforces all of this at write time. **Costs**: a one-time validator + evidence-schema
update on both grammar sides (SLC and the dotted recognizer), and a v2.1.0 cut; corpora
pinned to 2.0.0 are unaffected until they raise their pin (DEC-0014_3).

## References

- [`DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — clause DEC-0008_6 (the SLC coordinate) is the clause this record amends.
- [`DEC-0013-20260713-clause-identifier-separator-underscore.md`](DEC-0013-20260713-clause-identifier-separator-underscore.md) — the separator-philosophy precedent (letters/underscores over dots) this record stays consistent with.
- [`../reference/evidence/evidence-v1.md`](../reference/evidence/evidence-v1.md) — the evidence record whose `sliceId` pattern kept the `[a-z]` sub-slice suffix on its dotted alternative: the documented precedent for clause DEC-0014_1.
- [`../spec/v2.1.0/naming.md`](../spec/v2.1.0/naming.md) — §5 (slice coordinate) and the grammar table, amended by this record; ships in spec v2.1.0.
- [`../spec/README.md`](../spec/README.md) — the versioning policy whose "backwards-compatible addition → minor" rule this record applies (v2.1.0).
