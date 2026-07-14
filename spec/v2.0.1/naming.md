# SliceOps™ Canonical Naming — v2.0.0

The canonical naming standard for SliceOps artifacts: **one concept = one name = one prefix = one grammar, across every layer and every store**. This document is the **single normative source** for artifact naming; every other document points here and never copies the tables (copies drift — principle P12, Context Discipline).

Governed by [`DEC-0008`](../../decisions/DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme.md) (the cognition cycle and the universal identifier scheme), with [`DEC-0009`](../../decisions/DEC-0009-20260712-handoffs-as-a-contextpack-kind.md) (handoffs), [`DEC-0010`](../../decisions/DEC-0010-20260712-corpus-index-as-reserved-name-infrastructure.md) (the corpus index), [`DEC-0011`](../../decisions/DEC-0011-20260713-canonical-corpus-container-and-layout.md) (the canonical container and layout, §7) and [`DEC-0012`](../../decisions/DEC-0012-20260713-catalog-amendments-mental-model-and-policy.md) (MentalModel + Policy catalog amendments). The complete catalog table with definitions is clause DEC-0008_2_1 as amended by DEC-0012 — the entity catalog (`../../reference/entity-catalog/`) is rewritten from it.

---

## 1. Canonical prefix per entity

Every catalog entity has exactly **one** canonical filename prefix, identical in every store — code repositories, knowledge corpora, runtime exports.

| # | Entity | Prefix | Retired aliases (prohibited) |
|---|---|---|---|
| 01 | DecisionRecord | `DEC-` · `DEC-P-` · `DEC-D-` (lifecycle, §3) | `DR-`, the term "RFC" |
| 02 | InsightRecord | `INS-` | `IN-`, `IR-` |
| 03 | OutcomeRecord | `OUTC-` (`kind:` mandatory) | `OC-`, `BR-` |
| 04 | Capability | `CAP-` (components via `kind:`) | `SKILL-`, `RUN-`, `REF-` |
| 05 | Goal | `GOAL-` (`decided-by:` mandatory) | — |
| 06 | Conclusion | `CONC-` | `LP-` (former LearningPattern) |
| 07 | MentalModel | `MM-` | `CF-` (former CognitiveFramework), `FRAME-` (interim v2 design name — DEC-0012_1) |
| 08 | ContextPack | `CP-` (`kind: pack / brief / handoff`) | `HANDOFF-` (folk counter, migrates into `CP-`) |
| 09 | Priority | `PRI-` (`serves-goal:` + `rank:` mandatory) | `AP-` (former ActivePriority — names never carry states) |
| 10 | RelationshipContext | `REL-` | — |
| 11 | Preference | `PREF-` | — |
| 12 | Value | `VAL-` | — |
| 13 | Session | `SESS-` | — |
| 14 | Policy | `POL-` (`scope:` mandatory; `enforced-by:` + `severity:`) — DEC-0012_2 | — |
| — | *slice coordinate* (not an entity) | `SLC[n]SEC[n]BL[n]` (§5) | `BL-XX.SEC-XX.SL-XXX` (dotted form) |

`REF-` remains retired as a catch-all (coding standards → `CAP-`, patterns → `CONC-`, third-party integrations → vendor connector entities). A prefix that maps to more than one entity is the anti-pattern this standard exists to prevent.

## 2. The universal identifier grammar

One grammar for every entity artifact, in every store type (clause DEC-0008_5):

```
PREFIX-NNNN-YYYYMMDD-slug-in-kebab-case.md
```

| Part | Rule |
|---|---|
| `NNNN` | Per-corpus, per-entity counter. **Minimum 4 digits, zero-padded, unbounded** (`0001 … 9999 → 10000 → …`). One counter per entity, shared across lifecycle prefixes (`DEC-P-0007` and `DEC-0007` are the same record; a *new* `DEC-0007` colliding with an existing `DEC-D-0007` is an error). |
| `YYYYMMDD` | The creation date, compact, **immutable** — taken from frontmatter `created:` (migrations fall back to the first git commit date). The compact form also keeps v2 names visually distinct from legacy date-based names. |
| slug | Kebab-case, lowercase only — case-insensitive-filesystem safety, web-address convention, shell and pattern-matching safety. |

- **Number and date are stable across the lifecycle**: on approval `DEC-P-0008-…` renames to `DEC-0008-…` — the prefix carries the state, the identity never changes.
- **Counters are finite, serialized, shared resources** (principle P9, Shared-Resource Pre-flight): every corpus carries `.counters/`, and every claim re-scans the real maximum before writing. The toolkit ships `templates/counter-discipline/claim_id.py` to make the discipline one command.
- **Short citations** (`DEC-0008`) are unambiguous *within* a corpus; cross-corpus citations carry corpus context or the full filename.

## 3. DecisionRecord: lifecycle in the prefix, kind in the frontmatter, clauses by sub-number

**Lifecycle** (unchanged from the naming homologation): `DEC-P-` pending → `DEC-` approved → `DEC-D-` deprecated/superseded, with `status: pending | approved | deprecated` matching the prefix, **flat `decisions/` folders** (lifecycle subfolders `rfcs/`, `accepted/`, `superseded/`, `deprecated/` are retired), and every state change renaming the file plus rewriting references in the same atomic change (rule R5). Legacy status values (`proposed`, `ratified`, `superseded`, adopter variants `active`/`accepted`) are read-tolerated, write-prohibited. The optional `approver:` field (P3 — Human-in-the-Loop Authority) records the approving human.

**Kind** (clause DEC-0008_3): `kind: constitutive | strategic | tactical`, with the truth carried by goal edges — `strategic` requires `defines-goal:`, `tactical` requires `serves-goal:`, `constitutive` requires `approver:`. Mandatory for records created on or after 2026-07-13; earlier records are back-filled fix-on-touch.

**Clauses** (clause DEC-0008_9): resolutions inside a record are cited **`DEC-NNNN_n`** (e.g. `DEC-0008_5`), never "Decision n" bare. Clause identifiers are valid supersession targets: a future record may declare `supersedes: [DEC-0008_3]` without touching sibling clauses. The independence test decides clause versus standalone record: *could you reject this part and approve the rest without breaking the design?* No → clause; yes → its own record, immediately.

## 4. The pyramid edges (naming-visible fields)

The provenance chain is machine-checkable end to end (clause DEC-0008_4): every **Goal** carries `decided-by: <DEC id>` (the decision that created it — mirror of `defines-goal`); every **Priority** carries `serves-goal: <GOAL id>` and an integer `rank` unique within its `(owner, horizon)` scope — the three-bucket `priority: high|medium|low` field is retired.

## 5. The slice coordinate

Work coordinates (clause DEC-0008_6) replace the dotted Slice ID. **Letters are the separators** — no dots (fragile in git references and `.md` filenames), no inner hyphens (the hyphen is the grammar's field separator):

```
SLC0012SEC03BL02        full coordinate (slice ∈ section ∈ block)
SLC0034                 simple form — SEC and BL are optional qualifiers
```

Minimum widths: `SLC` 4 digits, `SEC`/`BL` 2 — all unbounded per §2. In frontmatter: `originating_slice: SLC0012SEC03BL02`. In branches, commits and pull-request titles: the bare coordinate. As a materialized file it joins the universal grammar: `SLC0012SEC03BL02-20260712-slug.md`. Slice coordinates inside **merged git history are immutable** (same standing as archives) — alias maps cover them; trackers, ledgers, frontmatter and living documents are rewritten.

## 6. Reserved infrastructure names

The universal grammar governs *entity artifacts*. Infrastructure files are exempt and their names are **reserved** (DEC-0010_5, extended by DEC-0011_5): `README.md`, `CLAUDE.md`/`AGENTS.md` (thin pointers at the repo root), `MEMORY.md`, `_organization.md`, **`_index.md`**, **`_agents.md`** (the corpus behavior contract), **`_policies.md`** (DERIVED summary of the active Policy records — DEC-0012_3, never hand-edited), `*-ledger.md`, the **`_metrics/`** and **`_meta/`** directories, the `.counters/` directory (inside `_metrics/` in container corpora), and the adoption manifest **`sliceops.json`** (§7). Anything else must be an entity artifact under the grammar. Numbers are cognition; underscores are infrastructure.

**`_index.md` is mandatory at every corpus root** (DEC-0010): the map of where to look for what — the loading chain is *agent-context file → `_index.md` → exact files or ContextPacks*. It points, never copies; the validator enforces that it exists and that every route resolves. Large corpora may add per-folder `_index.md` files; the root index routes to them.

## 7. The canonical container and layout (`_sliceops/`)

Folder names are names too (DEC-0011). **`_sliceops` is always the container at the root
of the unit of work**: a *directory* in a single repository; a *git repository named
`_sliceops`* in a multi-repo product workspace (replacing the former "-engineering"
repo); a *pointer* `sliceops.json` (`{"ref": …, "remote": …}`) in code repositories. The
LOCAL name detects; the remote name is free. One product = one corpus = one set of
counters.

Inside, the decades are numbered in cognition-cycle order and their semantics are
**reserved forever** — presence activates (a corpus materializes only what its work
needs):

```
_sliceops/
  sliceops.json · _index.md · _agents.md · _policies.md (derived) · _metrics/ · _meta/
  00-context/    01-values 02-preferences 03-mental-models 04-context-packs
                 05-relations 06-capabilities 07-policies 10-custom-context
                 (08–09 reserved to the framework)
  10-insights/   20-conclusions/   30-decisions/ (flat)   40-goals/
  50-products/   the complete WHAT: definition + architecture + specs + reference
  60-execution/  61-priorities 62-plans 63-dags (derived only, P5)
                 64-fleet-agents 65-in-flight
  70-outcomes/   99-archive/ (immutable, R10)
```

Decades **80 and 90 are free** adopter/vendor space, declared in the manifest's
`extensions`. Normative source for every rule above: DEC-0011 (clauses .1–.8).

## 8. Immutable zones

`99-archive/` folders (rule R10) are **never renamed**; merged git history is never rewritten. Historical names in both are covered by each corpus's **alias map**, emitted by the migration tooling. Everything else is renamed retroactively — homologation is total, not forward-only.

## 9. Alias tables

### Migration to v2.0.0 (scheme level; per-file maps are emitted per corpus)

| Pre-v2 form | v2.0.0 canonical | Rule |
|---|---|---|
| `PREFIX-YYYY-MM-DD-slug.md` (date-based) | `PREFIX-NNNN-YYYYMMDD-slug.md` | universal grammar: number assigned chronologically by `created:` |
| `PREFIX-NNN-slug.md` (3-digit counter) | `PREFIX-NNNN-YYYYMMDD-slug.md` | renumber to 4-digit minimum + date inserted |
| `LP-<id>` | `CONC-<id>` | Conclusion rename |
| `CF-<id>` | `MM-<id>` | MentalModel rename (DEC-0012_1) |
| `FRAME-<id>` (interim v2 design name) | `MM-<id>` | MentalModel rename (DEC-0012_1) |
| `AP-<id>` | `PRI-<id>` | Priority rename (or reclassification where the file was never a priority) |
| `HANDOFF-NNN` (folk counter) | `CP-NNNN-…` with `kind: handoff` | DEC-0009 |
| `BL-XX.SEC-XX.SL-XXX` | `SLC…SEC…BL…` | slice coordinate (§5) |
| `priority: high\|medium\|low` | `rank: <int>` within `(owner, horizon)` | pyramid (§4) |
| `DR-`, `IN-`, `IR-`, `OC-`, `BR-`, `SKILL-`, `RUN-`, `REF-`, lifecycle subfolders, `status: proposed/ratified/superseded`, term "RFC" | as in §1/§3 | carried over from the earlier naming homologation |

### Implementation aliases (vendor runtimes — the canonical name always wins in portable form, principle P11)

| Runtime name | Canonical entity |
|---|---|
| AgentContextPack | ContextPack |
| AgentSkill | Capability |
| GoalObjective | Goal |
| ValuePrinciple | Value |
| AgentPreference | Preference |
| LearningPattern *(pre-v2 canonical name)* | Conclusion |
| CognitiveFramework *(pre-v2 canonical name)* | MentalModel |
| Frame *(interim v2 design name)* | MentalModel |
| ActivePriority *(pre-v2 canonical name)* | Priority |

Runtime-**proprietary** entities are NOT in the canonical catalog and are not renamed by this standard — they follow the vendor-extension mechanism in [`ip-boundary.md`](ip-boundary.md).

## 10. Enforcement

The standard self-imposes at the point of write (published-not-enforced is the failure mode this closes):

1. **Norm without copies** — naming lives only here; other documents link.
2. **Agent context** — each corpus's `AGENTS.md`/`CLAUDE.md` carries a short NAMING block pointing here, and points to the corpus `_index.md`.
3. **Write hook** — the toolkit naming validator blocks non-homologated names at write time, indicating the correct form.
4. **Continuous-integration gate + sweeper** — the same validator as a merge gate in repositories and as a periodic sweep over document corpora; it also verifies `_index.md` presence and route resolution, and — in container corpora — the adoption manifest's presence and coherence (DEC-0011_8).
5. **Counter discipline** — `claim_id.py` makes the pre-flight one command; the counter-atomicity check detects collisions.

Reference implementation: `sliceops-toolkit/templates/naming-validator/` and `sliceops-toolkit/templates/counter-discipline/`.
