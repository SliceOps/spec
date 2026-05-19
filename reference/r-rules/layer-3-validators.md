# Layer 3 — Consistency CI Validators (Capa B.1)

The consistency-management mechanism has six layers. Layers 1–2 are immediate manual discipline (frontmatter fields + pre-merge checklist + HITL gate). **Layer 3** automates consistency as CI validators so corpus health does not depend 100% on human discipline — it does not scale past ~20 DECs by hand. This document is the **specification** of the Layer 3 validators; runnable workflow templates live in the **SliceOps toolkit** repo (`templates/consistency-validators/`).

## Phase 2 — basic validators (low complexity)

| Validator | Rule | Check |
|---|---|---|
| `validate-cross-references-bidirectional` | If DEC A lists DEC B in `related-decs`, DEC B's frontmatter should reference DEC A | frontmatter parse + graph traversal; flag asymmetric edges |
| `validate-no-orphan-decs` | A DEC with empty `related-decs` AND empty `topics` must justify isolation in its body | frontmatter check + body grep for a justification marker |
| `validate-frontmatter-schema` | Layer 1 fields present + well-formed (`conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, `consistency-check`) | YAML schema validation |
| `validate-topic-tags` | Every value in `topics:` exists in the canonical topic taxonomy | set membership against `spec/v1.0.0/topics.md` |

## Phase 3 — advanced validators (medium complexity, later)

| Validator | Rule |
|---|---|
| `validate-glossary-coverage` | Canonical terms used in DEC bodies exist in the glossary |
| `validate-supersession-chain` | The supersession graph (`supersedes`/`superseded-by`) is acyclic |
| `validate-vocabulary-changes-glossary-sync` | Non-empty `vocabulary-changes` ⇒ the glossary contains those terms |

A future `detect-semantic-overlap` (embeddings-based near-duplicate DEC detection) is out of scope for CI starters (high complexity; runtime/MCP capability).

## Counter-discipline validator (P12-driven, ships with Phase 2)

`validate-counter-atomicity` — enforces the counter-discipline pattern that prevents cross-coordinator numbering collisions (a finite/serialized shared resource per P12). Root cause: parallel agents independently claiming the same `INS-NNN`/`HANDOFF-NNN`/`LP-NNN`.

**Pattern (Capa B.1, vendor-neutral)**:
- A counter store per numeric prefix (date-based artifacts like `DR-YYYY-MM-DD-slug` need none — date+slug carries uniqueness).
- Pre-flight: re-scan the **real max** before claiming; never trust a stale "counter currently at" cache (it drifts under parallel work).
- Claim = increment the counter store **and** create the artifact in the same logical step.
- Collision rule: the resolved/closed artifact keeps its number; the open/new one renumbers; the human is flagged (P9 HITL).
- Check: no two artifacts share a `<PREFIX>-NNN`; the counter store ≥ real max.

This validator traces to **P12** (Shared-Resource Pre-flight — counters are a finite/serialized shared resource) and **P2/P4** (audit-plane integrity — duplicate IDs corrupt traceability). It is the automated backstop for the manual P12 pre-flight discipline.

## Mapping to principles

Every Layer 3 validator traces to a principle: bidirectional/orphan/supersession → P2 + P4 (audit-plane reachability + decision integrity); frontmatter-schema/topic-tags/glossary → P10 (vocabulary discipline) + the consistency mechanism; counter-atomicity → P12. A validator with no principle backing is a retirement candidate (P7).

## Adopter instantiation

These specs are vendor-neutral (Capa B.1). The runnable form (CI workflow + parser scripts) is Capa C.2 — the adopter binds the abstract checks to their stack and CI provider. The SliceOps toolkit provides reference starters; adopters extend (R15+).
