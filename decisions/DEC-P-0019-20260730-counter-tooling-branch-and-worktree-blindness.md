---
entity: DecisionRecord
status: pending
kind: constitutive
created: 2026-07-30
updated: 2026-07-30
owner: Andrés Ramírez Sierra
approver: null              # P3 — recorded on approval (DEC-0005: self-ratification is explicit, never silent)
sensitivity: public
originating_slice: null     # diagnosis of the forked DEC counter, 2026-07-30
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme, DEC-P-0018-20260730-duplicate-decision-number-reconciliation]
topics: [counter-discipline, worktree-discipline, corpus-integrity, finite-resource-stewardship]
vocabulary-changes: ["claimed-id set (the union of ids across all refs, not one working tree)", "corpus boundary (a checkout nested inside a corpus is not part of it)"]
consistency-check: |
  Does not change the universal grammar: DEC-0008_5 rule 1 already REQUIRES re-scanning
  the real maximum before claiming, and rule 3 already REQUIRES that one counter value
  address one artifact. This record fixes the two reference implementations that fail to
  deliver what those rules already oblige — it makes the obligation reachable, it does not
  widen it. No identifier, prefix, lifecycle rule or entity definition moves, so no corpus
  artifact's conformance changes and no spec version is cut; `naming.md` §5 item 5 and the
  `counter discipline` glossary entry gain precision about what "the corpus" means when a
  repository has branches and nested checkouts. Directly enables the repair DEC-P-0018
  performs by hand. P9 (Shared-Resource Pre-flight) is the governing principle: a counter
  is the canonical finite serialized shared resource, and a pre-flight that cannot see the
  whole resource is not a pre-flight. The toolkit changes are a declared follow-up against
  `sliceops-toolkit` (same pattern as DEC-0014's validator-engine follow-up).
---

# DEC-P-0019 — The claimed-id set spans refs, and the corpus boundary stops at nested checkouts

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P1, P2).
> **Status: pending.** Constitutive: it fixes what the counter-discipline pattern must
> read, so it lands only with the human ratification P3 requires.

## Summary

The two tools that enforce counter discipline both mistake **one working tree** for **the
corpus**, and they fail in opposite directions. `claim_id.py` **under-reports**: it re-scans
the filesystem, cannot see other branches, and therefore hands out a number that is already
spent exactly when parallel branches exist — the condition it was built to defend against.
`validators.py`'s counter-atomicity check **over-reports**: it descends into
`.claude/worktrees/`, finds every record twice, and reports **17 collisions, all false and
none real**, in the worktree layout SliceOps itself prescribes. One tool cannot see far
enough; the other cannot see where to stop. Both are the same missing idea — the corpus is
the set of artifacts across all **refs**, and a checkout nested inside it is not part of it.

## Context

This record exists because the defect it describes produced a live corpus violation, and
that violation is not hypothetical: it is
[`DEC-P-0018`](DEC-P-0018-20260730-duplicate-decision-number-reconciliation.md), where
counter value 0014 came to address two different DecisionRecords thirteen days apart.

### The claim path under-reports

`templates/counter-discipline/claim_id.py` opens by naming exactly this failure: it was
root-caused by the **INS-006 collision incident** (parallel sessions independently claiming
the same ids), and its header commits to never trusting the counter file in isolation,
listing "a merge from another branch" among the drift sources it reconciles. It then
implements `scan_real_max()` as an `os.walk()` of `--root`.

An `os.walk()` sees one checked-out tree. It cannot see a branch. The reconciliation
`base = max(real_max, file_max)` is real but does not rescue it, because `.counters/dec.txt`
is a **tracked file that forks with the branch**: on a branch cut before a claim, the
filesystem scan and the counter file are stale *together*, and the maximum of two stale
numbers is stale. What the tool defends against is the state *after* a merge has landed;
what produces collisions is the interval *before* it. So on a branch cut at the DEC-0013
commit, the real maximum on disk was 0013, the counter file said 0013, and the tool issued
**0014** — a number spent on another branch nearly two weeks earlier. The defence and the
attack never met.

The exclusion list is not the problem here: `claim_id.py` already excludes `.claude` and
`.worktrees` correctly. Its horizon is the problem.

### The validation path over-reports

`templates/consistency-validators/validators.py` `check_counter_atomicity()` walks from the
root skipping only `.git`. SliceOps corpora keep agent worktrees at `.claude/worktrees/`
— a second checkout of the same repository, inside the repository — so the walk finds every
record twice and reports each as colliding with itself. Measured on this repository today:

```
counter collision DEC-14: ['./.claude/worktrees/<wt>/decisions/DEC-0014-…md',
                           './decisions/DEC-0014-…md']
```

**17 issues, 17 false positives, 0 true positives** — one per DecisionRecord in the corpus.
(The count was 15 when the defect was first diagnosed; DEC-0016 and DEC-P-0017 landing
since then raised it, which is the tell: the false-positive count tracks corpus size, so it
only ever grows.) The check is not merely noisy — a gate whose every finding is false is a
gate no one reads, which is the precondition for the one true finding to be missed.

And it *was* missed. The real DEC-0014 collision lived on another branch, so a filesystem
walk could not have found it at any exclusion setting. The check reported seventeen
collisions that were not real and stayed silent on the one that was.

### Why this stayed invisible

Continuous integration checks out a clean tree with no nested worktrees, so **all nine
checks pass in CI**. The same command in a maintainer's worktree fails with 17 issues. The
gate CI runs and the gate a maintainer runs are different gates, and the divergence is
silent in the direction that matters: the local run is the *pre-flight* — the one that
happens before the write, when a collision is still cheap. The published gate was green
throughout the thirteen days the corpus carried a duplicate number.

The framework had the concept and did not apply it to itself. P9 (Shared-Resource
Pre-flight) names counters and **worktree/checkout state** in the same breath, as the
resource class to enumerate before scaling parallelism; `naming.md` §48 calls counters
"finite, serialized, shared resources … every claim re-scans the real maximum". Both tools
implement "re-scan" against a definition of *corpus* that predates the parallel-worktree,
multi-branch topology the framework prescribes.

## Decision

### DEC-0019_1 — The claimed-id set is the union across all refs

For counter discipline, the set of claimed ids for an entity is the union of the ids
appearing in **every ref of the repository** — local branches, remote-tracking branches, and
the working tree — not the ids visible in one checkout. A claim re-scans that union before
issuing.

`claim_id.py` gains a git-aware scan: enumerate refs and read artifact names from each tree
(`git for-each-ref` + `git ls-tree`), unioned with the existing filesystem walk, which is
retained so that uncommitted and untracked artifacts still count. Where git is unavailable
or the root is not a repository, the tool **falls back to the filesystem walk and says so on
stderr** — a silent narrowing of the horizon is what produced this defect, so a narrowed
horizon must be announced (P9: announce, do not fail silently). Remote refs are read as
already-fetched; the tool does not fetch, and it names the staleness of an un-fetched remote
in the same notice rather than implying a freshness it cannot guarantee.

The reconciliation rule is otherwise unchanged: claim `max(scanned, counter-file) + 1`,
atomically, under the existing lock.

### DEC-0019_2 — The corpus boundary stops at a nested checkout

A checkout nested inside a corpus — `.claude/worktrees/*`, and any nested `.git` — is **not
part of that corpus**. It is a second view of the same artifacts, and counting it duplicates
every record in it.

Every filesystem walk in the consistency validators applies this boundary.
`check_counter_atomicity()` currently skips `.git` alone; the module's shared `_SKIP_DIRS`
also lacks the worktree path, so the boundary is applied **once, at module level**, and used
by every walk rather than re-specified per check — the per-check inline skip list is how the
two walks drifted apart in the first place.

A corpus that genuinely vendors a second corpus inside itself validates it as its own root.
One walk, one corpus, one boundary.

### DEC-0019_3 — A gate that behaves differently in CI and locally is not a gate

Where the same check runs both in continuous integration and as a local pre-flight, the two
must return the **same verdict on the same corpus state**. A divergence is a defect in the
check, not a property of the environment, and it is repaired in the check — never worked
around by narrowing what runs locally.

This clause is what makes the other two enforceable. The counter-atomicity defect survived
thirteen days precisely because the published gate was green while the local gate was
unusable, and nothing in the framework said that combination was itself a failure. The
validators' own test corpus therefore includes a nested-checkout fixture, so the boundary of
DEC-0019_2 is asserted rather than assumed.

**Declared follow-up.** The clauses above bind
[`sliceops-toolkit`](https://github.com/SliceOps/toolkit), which carries both engines; this
repository consumes them fetched, not vendored. A rule published without the mechanism that
enforces it is the *published-not-enforced* anti-pattern the framework rejects (the same
declaration DEC-0014 made for its validator engine), so this record is not complete until
the toolkit ships: the git-aware scan, the shared boundary, the nested-checkout fixture,
and — separately owed — the column-0 guard now vendored into this repository's pre-write
hook but not yet upstream (DEC-0018_3).

## Alternatives considered

- **Fix the exclusion list only** (add `.claude`/`worktrees` to the validator's skip set):
  rejected as a complete answer, though it is half of DEC-0019_2. It silences 17 false
  positives and leaves the check unable to detect the only collision that has ever actually
  occurred here — a cross-branch one. Fixing the noise and leaving the blindness would
  convert a visibly broken gate into an invisibly useless one, which is worse: the noise is
  at least a signal that something is wrong.
- **Make the claim path branch-aware only** and leave the validator noisy: rejected. The
  claim is the pre-flight and the validator is the audit; P9 wants both, and a corpus whose
  audit gate is ignored has no defence when a claim is made out-of-band by a human editing
  a filename — the drift source `claim_id.py`'s own header names.
- **Serialize claims through a remote service** (a counter API, or a lock in a shared
  store): rejected. It contradicts the toolkit's stdlib-only, offline-capable design, adds
  an availability dependency to the act of creating a file, and is unnecessary — git already
  *is* the multi-host merge point, as `claim_id.py`'s lock docstring says. The defect is not
  that git is missing; it is that the tool never asks git.
- **Drop the counter and identify records by date+slug alone**: rejected. It would repeal
  DEC-0008_5 rather than implement it, discard ordinal readability across the corpus, and
  trade a detectable collision for a silent one — two records with the same date and a
  near-identical slug (exactly the DEC-0014 case) would then differ only in prose.
- **Accept the false positives and document them as known noise**: rejected — this is the
  status quo, and DEC-0019_3 exists to name why it is not acceptable. A documented broken
  gate is still a broken gate, and it trained a reader to skip the one output that would
  have surfaced the fork.

## Consequences

**Establishes**: the *claimed-id set* as a union across refs rather than a property of a
checkout; the *corpus boundary* as a module-level invariant that stops at nested checkouts;
and the CI/local parity rule that makes a silently-divergent gate a defect in its own right.

**Enables**: the P9 pre-flight DEC-0008_5 rule 1 already requires actually becomes
reachable in the parallel-branch, parallel-worktree topology SliceOps prescribes — the
collision class INS-006 identified is defended against in the interval where it occurs,
before a merge rather than after; and the counter-atomicity gate becomes usable locally, so
its findings can be read.

**Constrains**: claims and validation walks read git refs, and a narrowed horizon (no git,
un-fetched remotes) must be announced on stderr, never assumed away; new consistency checks
use the shared boundary rather than an inline skip list; a check that diverges between CI
and local is repaired, not documented.

**Costs**: `claim_id.py` gains a git dependency on its fast path — mitigated by the
announced filesystem fallback, keeping the stdlib-only guarantee intact for the degraded
case; the ref scan costs one `ls-tree` per ref, which is milliseconds at corpus scale and
happens once per claim; and the toolkit owes a release before either clause is enforced
anywhere, which is the declared follow-up above.

## References

- [`DEC-0008`](DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) — clause
  DEC-0008_5 rule 1 (every corpus REQUIRES the `.counters/` discipline: re-scan the real max
  before claiming) and rule 3 (one counter per entity, shared across lifecycle prefixes) —
  the obligations these tools fail to deliver.
- [`DEC-P-0018`](DEC-P-0018-20260730-duplicate-decision-number-reconciliation.md) — the
  corpus violation this defect produced, and the hand-performed reconciliation that stood in
  for the tooling.
- [`spec/v2.2.0/principles.md`](../spec/v2.2.0/principles.md) — **P9 Shared-Resource
  Pre-flight**, which names counters and worktree/checkout state as the same resource class,
  and whose "telemeter, announce, do not moralize" rule governs the fallback notice.
- [`spec/v2.2.0/naming.md`](../spec/v2.2.0/naming.md) — §5 item 5 (counter discipline;
  `claim_id.py` as the one-command pre-flight, the counter-atomicity check as the detector)
  and the counters paragraph these clauses give precision to.
- `sliceops-toolkit` — `templates/counter-discipline/claim_id.py` (`scan_real_max`) and
  `templates/consistency-validators/validators.py` (`check_counter_atomicity`, `_SKIP_DIRS`):
  the two reference implementations bound by the declared follow-up.
- INS-006 — the collision incident that root-caused `claim_id.py`, cited by identifier;
  the record itself is maintained internally (DISCLOSURE.md).
