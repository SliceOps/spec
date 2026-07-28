---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-28
updated: 2026-07-28
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # origin: a Layer C.1 implementation handoff, 2026-07-15
supersedes: [DEC-0008_6]
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme]
topics: [slice-workflow, vocabulary-discipline, corpus-integrity, meta-framework]
vocabulary-changes: ["sub-slice (one-letter suffix on the slice coordinate)", "alphabetic section code", "sub-slicing rate", "pinned conformance (sliceops.json spec pin)"]
consistency-check: |
  Widens the SLC coordinate grammar of DEC-0008_6 — additively. Every coordinate valid
  under v2.0.0/v2.0.1 stays valid: the sub-slice suffix and the alphabetic section code are
  OPTIONAL forms, so the change is a SemVer MINOR and ships as spec v2.1.0 (released
  versions are immutable; v2.0.1 and v2.0.0 stay frozen and are their own alias note).
  Everything else in DEC-0008_6 stands unchanged — letters as separators, no dots, no inner
  hyphens, the SLC → SEC → BL order, git history immutable. No catalog entity, prefix,
  required field or lifecycle rule is touched, so no other clause of DEC-0008 and none of
  DEC-0009 / DEC-0010 / DEC-0011 / DEC-0012 / DEC-0013 is affected. Vocabulary additions
  (sub-slice, alphabetic section code, sub-slicing rate) land in the v2.1.0 glossary in the
  same change, together with the fix of the glossary's `Slice ID` entry, which still carried
  the dotted pre-v2 definition that DEC-0008_6 had already replaced (fix-on-touch, P12).
  The dotted-form recognizer is widened in the same pass so migration tooling can SEE the
  forms this record legalizes — previously they did not even register as legacy coordinates.
---

# DEC-P-0014 — Slice coordinate: sub-slice suffix and alphabetic section codes

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1 — Decision
> Integrity by Construction, P2 — Audit Plane Discipline). **Status: pending.** It is a
> constitutive record: it amends the canonical identifier grammar, so it lands only with the
> human ratification P3 requires (`approver:` set on approval — see *Ratification*, below).

## Summary

The slice coordinate `SLC[n]SEC[n]BL[n]` (clause DEC-0008_6) gains two optional forms: a
**one-letter sub-slice suffix** (`SLC0042b`) and an **alphabetic section code**
(`SEC` followed by uppercase letters instead of digits). Both are additive — every
coordinate valid under v2.0.1 remains valid — so this ships as spec **v2.1.0**. The record
also states when a spec rule starts binding an adopting corpus (its manifest pin), and
introduces the **sub-slicing rate** as a non-blocking health signal of planning altitude.

## Context

The v2 coordinate was designed from the shape the framework's own documents used
(`BL-XX.SEC-XX.SL-XXX`), not from a survey of real corpora. Two gaps surfaced the first
time a full corpus was migrated onto it.

**Origin.** A Layer C.1 runtime implementation reported, in a 2026-07-15 handoff
(ContextPack `kind: handoff` — DEC-0009), that migrating its slice identifiers from the
retired dotted form to the SLC coordinate stalled: a large share of its real coordinates
was **not expressible** under the published grammar. Two causes: an **alphabetic section
code** for named (rather than numbered) program sections, and a **sub-slice suffix** — a
single lowercase letter marking a slice split off from another mid-implementation. Its
migration was paused pending this decision, and the runtime asked the standard to choose:
widen the grammar, or require the corpus to be remodelled.

The handoff reported ~40% (91 of 230). Re-derived from the implementation's own migration
map while preparing this record, the honest figure is **75 of 229 distinct coordinates —
33%** (65 alphabetic sections, 25 sub-slices, 15 coordinates hitting both gaps, which the
handoff counted twice; the 230th identifier was malformed and is not a coordinate at all).
The corrected number is the one this record stands on (P6 — evidence, not the roundest
available number). A third of a production corpus is the same finding either way.

Two facts decided it.

1. **The suffix is a regression, not a new request.** The pre-v2 pattern published by this
   repository — including the evidence.v1 reference pattern — carried the optional
   `[a-z]` sub-slice suffix. The SLC coordinate silently dropped it. v2.0.0 lost
   expressivity the retired form had, and nothing in DEC-0008_6 argues for the loss; the
   clause argues about *separators* (dots, hyphens), never about sub-slices.
2. **The section field was never surveyed.** `SEC\d{2,}` assumes every section is numbered.
   Real programs name some of them, because the name *is* the meaning; a number would have
   to be decoded through a mapping table maintained by hand — a second source of truth for
   one fact, which P12 exists to prevent.

A third of the coordinates of the first corpus to attempt the migration is evidence about
the **grammar**, not about the corpus. That is the Layer B ↔ Layer C feedback path
working as designed: implementations are where a reference pattern meets reality, and what
they cannot express is the standard's finding to act on.

## Decision

The SLC coordinate grammar becomes:

```
SLC<digits≥4>[a-z]?(SEC(<digits≥2>|<A-Z≥2>))?(BL<digits≥2>)?
```

### DEC-0014_1 — Sub-slice suffix (restores the pre-v2 capability)

**Exactly one optional lowercase letter** (`a`–`z`) directly after the slice number:
`SLC0042b`, `SLC0042bSEC03BL02`. It marks a **sub-slice**: emergent granularity discovered
in execution, when an in-flight slice splits and renumbering its siblings would rewrite
identifiers already in branches, commits and trackers.

- **One letter, never more.** A sub-slice is a leaf of an existing slice, not a second
  numbering axis. Needing more than 26 says the parent was sized wrong — a planning signal
  (clause DEC-0014_4), not a grammar requirement.
- **Emergent work only.** Foreseeable work is planned as **numbered siblings**
  (`SLC0011`, `SLC0012`, …). The suffix is for what execution discovers, consistent with
  P5 (the plan is a derived hypothesis, not a commitment to leaves).
- The suffix binds to the slice number and travels with it everywhere the coordinate is
  used: branches, commits, pull-request titles, `originating_slice:`, filenames.

### DEC-0014_2 — Alphabetic section codes

`SEC` accepts **either** ≥2 digits **or** ≥2 uppercase letters. Two constraints keep one
grammar and one parse:

- **Pure, never mixed** — a section code is digits *xor* uppercase letters (`SEC03`,
  `SECQA`; not `SEC3A`). Mixed codes invite per-corpus dialects and ambiguous scanning.
- **An alphabetic code must not contain the substring `BL`** — `BL` opens the block
  qualifier and is the sole source of parse ambiguity in the coordinate. Excluding it lets
  a plain left-to-right scanner parse the coordinate; without it, correctness would depend
  on regex backtracking, which is not a property a published identifier grammar should
  require of its readers.

**`BL` stays numeric.** Blocks are the framework's coarse ordinal container; no
implementation has reported a need to name them, and the numeric block is what keeps the
anti-ambiguity rule above small.

### DEC-0014_3 — Conformance is pinned to the adopted version

A corpus is bound by the spec version its adoption manifest declares (`sliceops.json`
`spec:` — DEC-0011_8). Rules introduced in later versions do not bind it until it **raises
the pin**; raising the pin is the migration trigger, and `--transition` mode covers the
interval while a corpus migrates.

Applied to the retirement of the dotted Slice ID (DEC-0008_6, v2.0.0): a corpus whose real
coordinates were **not expressible** under the version it pinned is not in violation for
keeping the dotted form — the standard cannot retire a notation while its replacement
cannot carry the same information. For sub-sliced and alphabetically-sectioned corpora the
retirement therefore takes effect on adoption of **v2.1.0**, the first version that can
express them.

### DEC-0014_4 — The sub-slicing rate is a health signal, never a gate

The **sub-slicing rate** of a corpus — sub-sliced coordinates ÷ total coordinates — is a
signal of **planning altitude**: a high rate means the plan committed at too coarse a grain
and execution kept splitting it (P4 slice atomicity under emergence; P5 the plan as derived
view). Corpora SHOULD report it; it is emitted as a **notice** and **never fails a gate**
(P9 — telemeter the shared resource; do not moralize it).

**No canonical threshold is set.** One corpus has reported a measurement (≈11%, n=229). A
threshold derived from a single corpus would be invention presented as evidence — the
opposite of P6. Revisit when at least three corpora have reported.

### The handoff's open questions, answered

| Question | Answer |
|---|---|
| Restore the sub-slice suffix? | Yes — DEC-0014_1 (regression fix). |
| Allow alphabetic section codes, or require runtimes to map names to numbers? | Allow — DEC-0014_2. Mapping tables are a second source of truth (P12). |
| Multi-letter sub-slices? | No — one letter (DEC-0014_1). |
| Does the dotted retirement bind a corpus pinned to an older version? | It binds at the pin — DEC-0014_3. |

## Alternatives considered

- **A — Require the implementation to remodel** (renumber alphabetic sections, flatten
  sub-slices into siblings): rejected. It deletes meaning (a named section carries its
  semantics in the name) and retroactively renumbers atomic units already recorded in
  merged history, to satisfy a format constraint with no stated rationale behind it. A
  third of a corpus failing to fit is evidence the grammar was too narrow; treating it as a
  corpus defect would make the Layer B ↔ Layer C feedback path one-way, which the IP
  boundary never claimed.
- **B — Restore the sub-slice suffix only**, keep sections numeric and require runtimes to
  map names → numbers: rejected. The mapping table is an unmaintained second source of
  truth (P12), and the spec would owe a migration recipe it does not have — publishing an
  obligation without the mechanism is the *published-not-enforced* failure mode in reverse.
- **C — Free-form section codes** (`SEC[A-Z0-9]{2,}`, as the handoff proposed): rejected.
  Mixed codes (`SEC1A`) make the coordinate ambiguous to a single-pass parser and let each
  corpus invent a dialect. Purity (digits xor letters) plus the anti-`BL` rule keeps one
  grammar with one parse.
- **D — Extend the coordinate additively** (DEC-0014_1 + _2), with conformance pinned
  (_3) and the rate as a signal (_4): **selected**. All prior coordinates stay valid, the
  regression is repaired, and the emergent granularity implementations actually produce
  becomes expressible in the canonical identifier.
- **Ship as a major version (v3.0.0)**: rejected — nothing breaks. Every v2.0.1 coordinate
  parses unchanged under v2.1.0; capability is added, none removed. SemVer minor.

## Consequences

**Enables**: corpora with named program sections and mid-implementation splits can express
their real work coordinates canonically, instead of keeping a retired notation alive; the
dotted-form recognizer is widened in the same pass, so migration tooling **sees** the
coordinates it previously skipped (`BL-09.SEC-ABC.SL-010b`-shaped ids matched no pattern at
all and were invisible to sweeps); the sub-slicing rate gives planning altitude a
measurable, non-punitive instrument.

**Constrains**: section codes must be pure and must not spell `BL`; sub-slice suffixes are
single-letter; blocks stay numeric. A corpus that raises its pin to 2.1.0 owes the dotted →
SLC migration (DEC-0014_3).

**Costs**: a v2.1.0 cut (naming.md §5 and the glossary rewritten); the naming validator,
the evidence.v1 `sliceId` pattern and the validator documentation updated in the same
change; the toolkit release that carries the validator engine is a **declared follow-up**
— a published-but-unenforced rule is an anti-pattern this framework rejects, so the cut is
not complete until the toolkit ships the widened grammar and the sub-slicing-rate reporter
(DEC-0014_4).

## Ratification

Pending. Per `governance/PROPOSAL-PROCESS.md` step 5 and P3 (AI agents propose; humans
dispose), approval is a human act and cannot be self-applied by the authoring agent. On
approval:

1. Rename `DEC-P-0014-20260728-…` → `DEC-0014-20260728-…` (number and date stable — rule 3
   of DEC-0008_5); set `status: approved` and `approver:` (DEC-0005 — explicit
   self-ratification in a single-maintainer project, never silent).
2. Rewrite the `DEC-P-0014` references in the same atomic change (R5): this file,
   `decisions/DEC-0008-20260712-…` (`related-decs` + the DEC-0008_6 clause annotation),
   `CHANGELOG.md`, `spec/v2.1.0/naming.md` (governance line), `spec/v2.1.0/README.md`.
3. Flip the `[2.1.0]` CHANGELOG heading from *pending ratification* to the release date.
4. Tag `v2.1.0` after merge, and release the toolkit carrying the widened validator.

## References

- [`DEC-0008`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — clause
  DEC-0008_6 (the coordinate this record extends), DEC-0008_5 (the universal grammar and
  the lifecycle-stable identity), DEC-0008_9 (clause identifiers).
- [`DEC-0011`](DEC-0011-20260713-canonical-corpus-container-and-layout.md) — clause
  DEC-0011_8, the adoption manifest whose `spec:` field clause DEC-0014_3 reads as the pin.
- [`DEC-0013`](DEC-0013-20260713-clause-identifier-separator-underscore.md) — the
  immediately prior version cut; same pattern (a frozen version keeps what it published,
  the new record is its alias note).
- [`spec/v2.1.0/naming.md`](../spec/v2.1.0/naming.md) §5 — the normative grammar text this
  record governs; [`spec/v2.1.0/glossary.md`](../spec/v2.1.0/glossary.md) — *Slice ID*,
  *Sub-slice*, *Sub-slicing rate*.
- [`governance/PROPOSAL-PROCESS.md`](../governance/PROPOSAL-PROCESS.md) — the ratification
  path; [`DISCLOSURE.md`](../DISCLOSURE.md) — why implementation feedback is recorded openly
  and why no runtime-internal identifier appears in this record.
- Origin: Layer C.1 implementation handoff, 2026-07-15 (ContextPack `kind: handoff`,
  DEC-0009) — quantified non-expressibility of the v2.0.x coordinate in a production corpus.
