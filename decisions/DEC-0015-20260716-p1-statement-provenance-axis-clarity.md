---
entity: DecisionRecord
status: approved
kind: constitutive
created: 2026-07-16
updated: 2026-07-16
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
originating_slice: null   # maintainer review of P1 wording against the cognition cycle, 2026-07-16
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections, DEC-P-0017-20260730-spec-level-vocabulary-substrate-and-anchor]
topics: [meta-framework, principles]
vocabulary-changes: ["P1 statement leads with 'session' (the slice is its DEV special case)", "provenance axis vs dependency axis (named)"]
consistency-check: |
  A clarity refinement of the STATEMENT of canonical principle P1 (Decision Integrity by
  Construction), under the P3 elevated human-in-the-loop gate (approver: the framework
  owner). It changes wording, not substance: P1 already carried a clarification generalizing
  its "slice" to "session" (Session-Type taxonomy) and already framed provenance as "where a
  decision was produced". This record promotes that generalization into the statement itself
  and names the two axes the word "slice" was straddling, so a fresh reader cannot misread
  P1 as reversing the cognition cycle. No principle is added or removed; the count stays 12.
  Backwards-compatible: no corpus artifact becomes non-conformant. Ships in spec v2.1.0 with
  DEC-0014. Frozen zones (spec/v1.x, spec/v2.0.0, spec/v2.0.1, archives, git history) keep
  their published wording; this record is their forward note. No IP-boundary or licensing
  impact — public meta-framework text only.
---

# DEC-0015 — P1 statement: the provenance axis, named (clarity refinement)

## Summary

Refines the **statement** of canonical principle **P1 — Decision Integrity by Construction**
so its headline reads on the **session/provenance** axis and cannot be misread as reversing
the cognition cycle. Wording change, not a substantive amendment; the twelve-principle set is
unchanged.

## Context

P1's statement read *"Decisions emerge from slices."* Read against the cognition cycle —
insight → conclusion → decision → goal → plan → slice, where a decision *precedes* the
execution it authorizes — that headline collides: "emerge from slices" scans causally, as if
the slice (the terminal execution step) produced the decision. The collision was predictable
enough that P1 already carried a footnote generalizing "slice" to "session." The seam is that
the word **slice** was straddling two different axes:

- **Dependency axis** (the cognition cycle): *what justifies what.* Architecture, specs,
  plans, and code are consequences of decisions — never the reverse (the preamble's
  "decision-first"). On this axis a decision precedes the slices that execute it.
- **Provenance axis** (P1): *where each decision was produced.* Every decision is made inside
  a bounded unit of work and is anchored to it. "Slice" here is the general unit of work —
  the **session** — of which the DEV slice (the one that yields a PR) is the special case.
  Deciding is itself work; a governance session that ratifies decisions without a PR is still
  their anchor.

The two are orthogonal: a decision's place in the cycle and the session that produced it are
different questions. P1 governs only the second.

## Decision

### DEC-0015_1 — The statement stays a clean definition, session-first

P1's statement is refined to a plain declarative anchoring claim: every decision is anchored
to the **session** that produced it (the **slice** in the DEV case), traces to that session,
is reachable from it (back-link), and — if taken out-of-band — is backed into a session
retroactively. Only the opening *"Decisions emerge from slices"* — which scanned causally —
is replaced; traceability, back-link, and out-of-band retroactivity are preserved in
substance. The reconciliation of provenance with the cognition cycle is deliberately kept
**out** of the statement (a principle's statement defines what it *is*, not what it is not);
it lives in the clarification, DEC-0015_2.

### DEC-0015_2 — The two axes are named in P1's clarification

P1's clarification is refined from "the statement is generalized" to naming the **provenance
axis** (P1) and the **dependency axis** (the cognition cycle) explicitly, stating they are
orthogonal, so "anchored to the session that produced it" is never read as contradicting
"decisions precede plans and slices." The governance-session coverage and the Session entity
pointer (#13) are preserved.

### DEC-0015_3 — Provenance field reference updated to the SLC coordinate

P1's implication bullet no longer cites the retired dotted "Block-Section-Slice ID format";
it cites the SLC coordinate (§5, as extended by DEC-0014) for the DEV slice and a session
reference in the general case. The frontmatter field name `originating_slice:` is unchanged
(a rename is out of scope — it carries the session reference in the general case, as the
clarification states).

## Alternatives considered

- **Leave the wording and rely on the footnote**: rejected — a canonical principle's
  *statement* is the load-bearing line; a headline that a careful reader must walk back via a
  footnote is a defect in the statement, and the audit plane (P2) is weakened when the
  framework's own most-cited sentence invites the misreading it later corrects.
- **Rename the `originating_slice:` frontmatter field to `originating_session:`**: rejected
  here — it ripples across schemas, validators, and every adopter corpus; out of scope for a
  wording refinement. The field name stays historical; its meaning (session in the general
  case) is documented.
- **Record no decision, edit as editorial**: rejected — P1 itself prohibits out-of-band
  changes to the corpus, and a change to a canonical principle's text is exactly the class of
  change that must not be tribal knowledge. Recording it here is the framework applied to
  itself.

## Consequences

**Clarifies**: P1 can no longer be read as reversing the cognition cycle; the provenance and
dependency axes are named and declared orthogonal. **Preserves**: the twelve-principle set,
P1's substance (anchoring, back-link, out-of-band retroactivity), and every corpus artifact's
conformance. **Costs**: a wording edit to `principles.md` P1 (statement, rationale sentence,
one implication bullet, clarification) shipping in v2.1.0; frozen version dirs keep their
published wording.

## References

- [`../spec/v2.1.0/principles.md`](../spec/v2.1.0/principles.md) — P1, the principle whose statement this record refines.
- [`DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — the cognition cycle (the dependency axis) this record names alongside the provenance axis.
- [`DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md`](DEC-0014-20260715-slc-coordinate-subslice-and-alpha-sections.md) — the SLC coordinate P1's provenance bullet now cites; ships in the same v2.1.0 release.
