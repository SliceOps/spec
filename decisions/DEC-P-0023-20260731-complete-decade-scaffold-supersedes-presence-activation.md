---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-31
updated: 2026-07-31
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # origin: maintainer observation that an absent decade is unreadable, 2026-07-31
supersedes: [DEC-0011_2]
superseded-by: null
conflicts-with: []
related-decs: [DEC-0011-20260713-canonical-corpus-container-and-layout, DEC-0021-20260730-canonical-layout-reconciliation, DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure]
topics: [folder-structure, corpus-integrity, context-discipline, adopter, consistency-management, meta-framework]
vocabulary-changes: ["presence activation (retired)", "complete scaffold (new canonical term)", "decade README (new canonical term)"]
consistency-check: |
  Supersedes ONE clause — DEC-0011_2's presence-activation rule — and leaves the rest of
  DEC-0011 intact: the container form (_1), `50-products/` semantics (_3), `60-execution/`
  internals and the derived-only discipline (_4), the underscore family (_5), the manifest (_6),
  surfaces (_7) and application (_8) are unchanged, as are the decade NUMBERS and their reserved
  meanings. What changes is only whether an unused decade exists on disk. DEC-0021 is unaffected:
  it settled *which* locus is authoritative about layout, not whether folders are materialized,
  and its chain → decade mapping stands verbatim. DEC-0010's reserved-name family gains no
  member — the per-decade file is a `README.md`, already reserved infrastructure exempt from the
  universal grammar, not a second `_index.md`. Two terms land in the glossary at approval and
  one is retired; `presence activation` moves to the prohibited-alias list with a pointer here.
  The change is additive on disk (folders and READMEs appear; nothing is deleted or renamed), so
  no corpus valid before becomes invalid — it becomes incomplete, which the new toolkit check
  reports rather than silently tolerating.
---

# DEC-P-0023 — The complete scaffold: every canonical decade exists, always

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1, P2, P12).
> **Status: pending.** Constitutive: it supersedes a clause of DEC-0011, so it lands only with
> the human ratification P3 requires.

## Summary

DEC-0011_2 ruled that decades are **presence-activated**: a corpus materializes only what its
work needs. In practice that makes an absent decade unreadable — you cannot tell whether it is
absent *because unused* or *because forgotten*. This record replaces presence activation with a
**complete scaffold**: every canonical decade exists in every corpus, and each carries a short
`README.md` stating what belongs there. An empty decade stops being an absence and becomes a
**declared gap** — which is information, and actionable.

## Context

**The rule being superseded.** DEC-0011_2: *"presence activates (a corpus materializes only what
its work needs)"*. The reasoning was honest — scaffolding empty folders to look complete
misrepresents an empty corpus as a populated one, and empty directories are noise.

**What using it revealed.** A census of the maintainer's four operating corpora, 2026-07-31:

| Corpus | Canonical decades present |
|---|---|
| organization-zoom corpus | 9 of 9 (+1 vendor extension) |
| product A, engineering | 9 of 9 |
| product B, engineering | 9 of 9 |
| **product C, engineering** | **7 of 9** — `20-conclusions` and `40-goals` absent |

Product C is also carrying a non-canonical folder left over from an incomplete migration. So:
are its two missing decades absent because that corpus has produced no conclusions and set no
goals, or because the migration stopped early?

**The tree cannot answer that, and neither can an agent.** Under presence activation the two
states are byte-identical. The rule optimizes for the honesty of a snapshot and pays for it with
the readability of a gap — and a gap is the thing a maintainer actually needs to see.

**Why this matters more for SliceOps than for a generic layout.** P12 makes context a
first-class engineered artifact and mandates *routed* loading: an agent opens the index, then
the route. When a route's target does not exist, the agent has no way to distinguish "nothing
here yet" from "this corpus never adopted that" from "someone forgot" — and the corpus's own
`_index.md` cannot disambiguate it either, because it points at paths, not at states. The
missing information is exactly what P12 says must be authored rather than assumed.

**The empty-folder objection, answered.** Presence activation's worry — an empty folder
pretending to be a populated one — is real but is solved by *content*, not by *absence*. A
decade holding a `README.md` that says "no goals recorded yet; `GOAL-` entities live here, each
with `decided-by:`" misrepresents nothing. It reports its own emptiness, and tells the reader
what would fill it.

## Decision

**1. The scaffold is complete, always.** Every corpus materializes **all** canonical decades:
`00-context/` · `10-insights/` · `20-conclusions/` · `30-decisions/` · `40-goals/` ·
`50-products/` · `60-execution/` · `70-outcomes/` · `99-archive/`. Their numbers and reserved
semantics are unchanged (DEC-0011_2 is superseded only on materialization). Free decades 80/90
remain opt-in and are created only when declared in the manifest's `extensions`.

**2. Each decade carries a `README.md`.** One short file per decade, stating (a) what belongs
there, (b) which prefixes or artifacts it holds, and (c) any rule that is easy to get wrong
there — `30-decisions/` is flat, `62-plans/` and `63-dags/` are derived only. `README.md` is
already reserved infrastructure exempt from the universal grammar (DEC-0010_5), so no new
reserved name is introduced. **This clause is what makes the scaffold useful**: an empty folder
alone is silent, and the point of the change is to be able to read a corpus's gaps from its tree.

**3. An empty decade is a declared gap, not a defect.** No corpus is required to fill a decade.
Emptiness is a legitimate, readable state and must never be treated as a failure — the framework
reports it, it does not punish it (P9's doctrine: degradation announced, never a silent cut).

**4. Completeness is checkable.** The toolkit gains a structure check that reports a corpus
missing a canonical decade, and a decade missing its `README.md`. It reports; the maintainer
decides. A corpus predating this record is **incomplete, not invalid** — nothing it contains
becomes non-conformant.

**5. `presence activation` is retired as a canonical term.** It moves to the prohibited-alias
list with a pointer to this record, so the reasoning is not lost and the term is not reused
under its old meaning.

## Alternatives considered

- **Keep presence activation, add a manifest field listing adopted decades** — rejected. It
  moves the same information off the tree and into a file that must be maintained in parallel,
  which is a denormalization: the manifest and the filesystem would drift, and P12 names that
  exact failure. The tree is the source of truth about the tree.
- **Complete scaffold with `.gitkeep` instead of `README.md`** — rejected. `.gitkeep` makes the
  folder survive git and communicates nothing. The maintainer's stated goal — *"determinar qué
  hace falta con solo mirar un folder"* — needs the folder to say what it is for. A `.gitkeep`
  scaffold buys uniformity and forfeits readability, which is most of the value.
- **Scaffold only the decades a corpus type implies** (organization vs engineering) — rejected
  as a false economy. It reintroduces the ambiguity one level up: is `50-products/` absent
  because this is an organization corpus, or because someone forgot? Two shapes are two things
  to verify; one shape is none.
- **Leave it to adopters as a convention** — rejected. Convention is what produced a 7-of-9
  corpus that nobody noticed. If the framework's answer to "what is missing here?" depends on
  remembering to look, it has not answered.

## Consequences

**Enables**: a corpus's gaps are readable from its tree, by a human at a glance and by an agent
without a second lookup · one shape for every corpus, so routing never has to test for existence
· onboarding reads the structure as a map of what a corpus *could* hold, not only what it does.

**Constrains**: every corpus gains nine folders and nine short READMEs · new corpora scaffold in
full at adoption · the decade READMEs are documentation that must be kept true (they describe
semantics, which are reserved and stable, so the maintenance load is near zero by construction).

**Costs**: a scaffold pass over existing corpora · nine files of prose per corpus · a toolkit
check and its tests.

**Reverses a claim made in this project's own works log.** The SliceOps workspace container was
adopted on 2026-07-30 with a note stating that no decade was scaffolded because *"creating empty
decades to look complete would misrepresent an empty corpus as a populated one"* — a faithful
application of DEC-0011_2. That note is corrected on application, and this record is why. The
argument was not wrong about the risk; it was wrong about the remedy, which is a README rather
than an absence.

## References

- DEC-0011_2 — the presence-activation clause this record supersedes; every other clause of
  DEC-0011 stands
- DEC-0010_5 — the reserved-name family, which already exempts `README.md`
- DEC-0021 — the layout authority; its chain → decade mapping is unaffected
- [`spec/latest/naming.md`](../spec/latest/naming.md) §7 — the canonical container and decades
- P12 Context Discipline — context authored rather than assumed, which an unreadable absence
  violates
