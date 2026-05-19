# SliceOps™ Canonical Glossary — v1.0.0

Canonical glossary of SliceOps terms. Each term here has a **canonical meaning** (per P10 Vocabulary Discipline). Terms not listed here are not canonical SliceOps; adopters may extend with domain-specific terms in their own glossaries (extend, never redefine).

**Living document**: new terms emerge via decisions with non-empty `vocabulary-changes`; updates are part of the slice that produces the decision. Major restructure → version bump.

**Per-term structure**: Definition · Origin (principle/concept that canonicalizes it) · Aliases prohibited · Cross-references.

---

## A

### Adopter
- **Definition**: An organization or product that uses the SliceOps methodology to develop software or a knowledge corpus. Distinct from a vendor: adopters consume SliceOps; vendors provide runtimes (Capa C.1).
- **Origin**: IP boundary (three-layer)
- **Aliases prohibited**: "customer" (commercial), "user" (ambiguous), "implementer" (overloaded)
- **Cross-references**: Vendor, Capa C.1, Capa C.2

### Anti-pattern
- **Definition**: A practice explicitly prohibited under SliceOps discipline. Each principle declares anti-patterns; CI gates enforce.
- **Origin**: Capa A principles
- **Cross-references**: Principle, R-rules

### Audit plane
- **Definition**: The layer above code where architectural decisions live as first-class artifacts (DECs). Empty market space pre-SliceOps; the framework's primary wedge.
- **Origin**: P2
- **Aliases prohibited**: "decision log", "ADR system" (DECs are evolved ADRs, not equivalent)
- **Cross-references**: P2, DecisionRecord, Decision Integrity

## B

### Block
- **Definition**: A logical grouping of slices with coherent scope. Closes with a Block Retrospective. Velocity calibrated post-hoc per Block.
- **Origin**: P3
- **Aliases prohibited**: "sprint" (commits velocity ahead, violates P3), "epic" (issue-tracker-flavored), "milestone" (time-based vs scope-based)
- **Cross-references**: Slice, Stage, Block Retrospective

### Block Retrospective
- **Definition**: Mandatory ritual at Block close. Includes velocity recalibration + Cross-DEC Consistency Check section + InsightRecord harvesting.
- **Origin**: P3, P7
- **Cross-references**: Block, Velocity, Consistency check

### Brain pack injection
- **Definition**: A mechanism that injects relevant context at the start of each slice (including applicable Capa C.2 stack patterns for the repo in scope).
- **Origin**: Capa C.2 stack-patterns
- **Cross-references**: Capa C.2, Stack pattern, ContextPack

## C

### Capa A — Principles
- **Definition**: Top-level taxonomy layer. The 12 canonical principles (P1–P12) that constitute the SliceOps methodology. Immutable except by superseding DEC under an elevated HITL gate.
- **Origin**: Canonical principles
- **Cross-references**: Principle, P1–P12

### Capa B — Reference Patterns
- **Definition**: Top-level taxonomy layer. Reference patterns that materialize the principles. SliceOps IP. Has sub-layers (B.1 Methodology Artifacts, B.2 Universal Engineering Patterns).
- **Origin**: IP boundary + hierarchical taxonomy
- **Aliases prohibited**: bare "Capa B" without sub-letter is ambiguous in technical context — always specify B.1 or B.2 when relevant
- **Cross-references**: Capa B.1, Capa B.2

### Capa B.1 — Methodology Artifacts
- **Definition**: Sub-layer of Capa B. SliceOps-originated patterns: entity catalog (12 cognitive entities), repo folder structure, R-rules system, counter discipline, frontmatter schemas, file templates, vocabulary discipline mechanism.
- **Origin**: Hierarchical taxonomy
- **Cross-references**: Cognitive entity, Folder structure, R-rules

### Capa B.2 — Universal Engineering Patterns
- **Definition**: Sub-layer of Capa B. Industry-canonical engineering patterns SliceOps reaffirms: SOLID, ACID, Outbox, Fail-Fast, Idempotency, Defense in Depth, CI/Pipeline Cost Economy, Determinism-over-Regeneration. Vendor-agnostic, stack-agnostic.
- **Origin**: Stack-patterns + hierarchical taxonomy
- **Cross-references**: SOLID, ACID, Outbox, Idempotency, CI/Pipeline Cost Economy, Determinism-over-Regeneration

### Capa C — Implementations
- **Definition**: Top-level taxonomy layer. Specific implementations, not canonical SliceOps. Has sub-layers (C.1 Vendor Runtimes, C.2 Adopter Stack Patterns).
- **Origin**: IP boundary + hierarchical taxonomy
- **Aliases prohibited**: bare "Capa C" without sub-letter is ambiguous — specify C.1 or C.2
- **Cross-references**: Capa C.1, Capa C.2

### Capa C.1 — Vendor Runtimes
- **Definition**: Sub-layer of Capa C. Vendor-owned runtime products implementing the SliceOps Capa B catalog — e.g., hosted knowledge-graph products, third-party tool adapters, custom homegrown brains. A reference runtime is one runtime, not the runtime (P8).
- **Origin**: IP boundary + hierarchical taxonomy
- **Cross-references**: Vendor, Adapter, P8

### Capa C.2 — Adopter Stack Patterns
- **Definition**: Sub-layer of Capa C. Adopter-defined patterns instantiable per technology stack — e.g., Repository pattern (.NET), FluentValidation, Riverpod state management (Flutter). Each adopter defines its own Capa C.2 with enforcement tooling (analyzers / lint rules / CI gates).
- **Origin**: Stack-patterns + hierarchical taxonomy
- **Cross-references**: Adopter, Stack pattern, Brain pack injection

### Capability
- **Definition**: Cognitive entity #4 in the Capa B.1 catalog. Capabilities accrued by individuals/agents/teams. **Renamed from "Skill"** ("capabilities accrued" describes Capability, not Skill; the rename improves precision and frees the term "Skill").
- **Origin**: Catalog split (entity #4) + Determinism-over-Regeneration (rename)
- **Aliases prohibited**: "Skill" (former name, now reserved for a distinct concept — do NOT use for this entity)
- **Cross-references**: Cognitive entity, Capa B.1, P7, Skill (reserved — distinct concept)

### CI/Pipeline Cost Economy
- **Definition**: A Capa B.2 Universal Engineering Pattern. Five stack-agnostic levers for pipeline economy: concurrency-cancel-in-progress + change-scoped job gating + aggregation-required-gate + draft-skip of expensive jobs + dependency-cache. Materializes P12 in the CI domain. The concrete per-CI-provider/stack instance is Capa C.2.
- **Origin**: Shared-Resource Pre-flight (P12)
- **Aliases prohibited**: "CI optimization" (generic), "pipeline tuning" (under-specified)
- **Cross-references**: P12, Capa B.2, aggregation-required-gate, Outbox (sibling B.2)

### aggregation-required-gate
- **Definition**: A CI design pattern within CI/Pipeline Cost Economy (B.2). An `if: always()` job that is THE required check, resolving the "required check skipped → PR blocked forever" trap introduced by change-scoped job gating. Mandatory when path-gating is used.
- **Origin**: Shared-Resource Pre-flight (P12)
- **Cross-references**: CI/Pipeline Cost Economy, change-scoped job gating

### Cognitive entity
- **Definition**: One of the 12 canonical entity types of SliceOps Capa B.1 (DecisionRecord, InsightRecord, OutcomeRecord, Capability, Goal, LearningPattern, CognitiveFramework, ContextPack, ActivePriority, RelationshipContext, Preference, Value). Each has a frontmatter schema + lifecycle.
- **Origin**: Catalog split
- **Aliases prohibited**: "entity type" (ambiguous with database entities), "metadata record" (under-specified)
- **Cross-references**: Capa B.1, Entity catalog, DecisionRecord, InsightRecord

### CognitiveFramework
- **Definition**: Cognitive entity. A mental model or reference structure for reasoning + decision-making (e.g., this glossary, the topic taxonomy).
- **Origin**: Catalog split
- **Cross-references**: Cognitive entity

### consistency-check (frontmatter field)
- **Definition**: Mandatory DEC frontmatter field (Layer 1). A multi-line paragraph declaring how the DEC relates to the existing corpus.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Layer 1, Frontmatter discipline, conflicts-with

### conflicts-with (frontmatter field)
- **Definition**: Mandatory DEC frontmatter field. Lists DEC IDs that could appear to contradict + a resolution paragraph in the body if non-empty.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Layer 1, consistency-check

### ContextPack
- **Definition**: Cognitive entity. A pre-computed bundle of context loaded at slice/session start. Enables P8 platform-agnosticism (bundles portable cross-tools).
- **Origin**: Catalog split
- **Cross-references**: Brain pack injection, P8

### Counter discipline
- **Definition**: Capa B.1 pattern. Atomic increment per prefix + a validate-no-duplicate CI check. Prevents counter collision in multi-coordinator parallel work. Originated as empirical practice in reference-implementation context; canonicalized in SliceOps.
- **Origin**: IP boundary (canonicalized)
- **Cross-references**: R-rules, P12, DEC numbering

## D

### DAG (Directed Acyclic Graph)
- **Definition**: The slice dependency graph. Slices have explicit `depends_on:` edges. Stage is a view derived from the DAG (P3).
- **Origin**: P3
- **Cross-references**: P3, Stage, Slice

### DEC (DecisionRecord)
- **Definition**: Cognitive entity. An architectural/strategic decision recorded with lifecycle (proposed → accepted → superseded/deprecated), supersession edges, alternatives considered, consequences. Naming: `DR-YYYY-MM-DD-slug.md` (date-based) or `DEC-NNN-slug.md` (counter-based, per repo convention).
- **Origin**: Catalog split; P2/P4
- **Aliases prohibited**: "ADR" (predecessor, DECs are evolved), "decision doc", "note"
- **Cross-references**: ADR, P2, P4

### Decision Integrity by Construction
- **Definition**: P4. Decisions emerge from slices; every DEC traces to a slice (provenance). Out-of-band decisions must be backed into a slice retroactively.
- **Origin**: P4
- **Cross-references**: P4, Slice provenance, Originating slice

### Determinism-over-Regeneration
- **Definition**: A Capa B.2 Universal Engineering Pattern. If a process repeats, materialize it once as a deterministic reusable artifact (script, function, reference file, R-rule); do NOT stochastically regenerate it with AI each time. Deterministic code (same input → same result) is cheaper, faster, repeatable, and auditable vs AI output with drift. Rule: "if you can use code instead of AI, do; have AI write the code once, then reuse it."
- **Origin**: Determinism-over-Regeneration
- **Aliases prohibited**: "DRY for AI" (imprecise), "caching" (under-specified)
- **Cross-references**: Capa B.2, P5, P7, P12, CI/Pipeline Cost Economy (sibling B.2)

### one-off-vs-permanent tuning gate
- **Definition**: A P7 granularity clarification (does not change the statement). Artifact-level: whenever an artifact underperforms, ask "one-off adjustment or permanent?"; if permanent → update the artifact immediately (don't wait for ≥3). LearningPattern-level: pattern observed ≥3 times → canonical promotion. Two complementary granularities.
- **Origin**: Determinism-over-Regeneration
- **Cross-references**: P7, LearningPattern, InsightRecord

## E

### Evidence-by-Construction
- **Definition**: P5. Each slice produces evidence in 4 categories (functional, quality, decision, provenance) + security (P6). Hard gates enforce; slices without complete evidence don't merge.
- **Origin**: P5
- **Cross-references**: P5, P6, Evidence categories

### Entity catalog
- **Definition**: The canonical set of 12 cognitive entity types of SliceOps Capa B.1. Each entity has a frontmatter schema + lifecycle + cross-reference patterns + anti-patterns. Published in `reference/entity-catalog/`.
- **Origin**: Catalog split
- **Cross-references**: Cognitive entity, Capa B.1

## F

### Finite/serialized shared resource
- **Definition**: A consumable or serialized resource, shared cross-slice/cross-coordinator, with a hard limit: CI minutes, counters, API rate limits, branch-protection serialization, DB migration locks, worktree/checkout state, connection pools. The resource class P12 mandates enumerating + capping + alerting + telemetering before scaling parallelism.
- **Origin**: Shared-Resource Pre-flight (P12)
- **Aliases prohibited**: generic "shared resource" without "finite/serialized" (loses the key property)
- **Cross-references**: P12, infra-cost-ledger

### infra-cost-ledger
- **Definition**: A Capa B.1 extension of the cost-ledger. Tracks the infra/CI cost dimension alongside token cost. The pre-Block checklist verifies infra/CI budget headroom. Closes the "infra-cost blindness" failure (a token-only ledger).
- **Origin**: Shared-Resource Pre-flight (P12)
- **Cross-references**: P12, Capa B.1, cost-ledger, token-band

### Fix-on-touch
- **Definition**: A P10 Vocabulary Discipline policy. Any slice that detects vocabulary drift in a file it touches updates it forward (no separate cleanup slice).
- **Origin**: P10
- **Cross-references**: P10, Vocabulary discipline, Glossary

### Frontmatter discipline (Layer 1)
- **Definition**: The Layer 1 mandatory frontmatter spec for all DECs. Includes consistency-check, conflicts-with, topics, vocabulary-changes fields.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Layer 1, consistency-check, conflicts-with

## G

### Glossary
- **Definition**: This document. The canonical glossary of SliceOps terms. Living document; updated by every decision with non-empty `vocabulary-changes`.
- **Origin**: P10; consistency-management mechanism
- **Cross-references**: P10, Vocabulary discipline, Layer 1

## H

### Hierarchical Layer Taxonomy
- **Definition**: The meta-decision on the naming structure of Capa A/B/C. Top-level Capa A/B/C are stable; sub-numbering (B.1, B.2, C.1, C.2) accommodates new dimensions without renaming.
- **Origin**: Hierarchical taxonomy
- **Cross-references**: Capa A/B/C, Scalability

### HITL (Human-In-The-Loop)
- **Definition**: P9. Humans retain final authority over scope, merges, architectural direction. AI agents propose; humans dispose.
- **Origin**: P9
- **Cross-references**: P9, Merge gate, CODEOWNERS

## I

### Idempotency
- **Definition**: A Capa B.2 universal engineering pattern. The same operation invoked multiple times produces the same result. Implemented via Idempotency-Key headers, deduplication tables, etc.
- **Origin**: Stack-patterns
- **Cross-references**: Capa B.2, ACID, Defense in Depth

### Infrastructure Continuity
- **Definition**: P11. Code, IaC, DB schemas, env configs form one continuum. SliceOps discipline applies uniformly.
- **Origin**: P11
- **Cross-references**: P11, Stack pattern, IaC

### InsightRecord
- **Definition**: Cognitive entity. An empirical observation captured from a slice. Append-only. Raw material for LearningPatterns. Naming: `INS-NNN-slug.md`.
- **Origin**: Catalog split; P7
- **Cross-references**: P7, LearningPattern, Recursive Learning

## L

### LearningPattern
- **Definition**: Cognitive entity. A pattern observed ≥3 times across InsightRecords; promoted as a canonical pattern. Naming: `LP-NNN-slug.md`. Triggers a DEC for R-rule amendments.
- **Origin**: Catalog split; P7
- **Cross-references**: P7, InsightRecord, R-rules

## M

### Mode S / Mode M
- **Definition**: P8 operation modes. Mode S = single-agent sequential (one slice at a time, Wedge A only); Mode M = multi-agent parallel (N simultaneous slices with a coordinator, both wedges).
- **Origin**: P8
- **Cross-references**: P8, Wedge A, Wedge B, Coordinator

## P

### Principle
- **Definition**: One of the 12 canonical SliceOps principles (P1–P12). Capa A. Immutable except by superseding DEC under an elevated HITL gate.
- **Origin**: Canonical principles
- **Cross-references**: Capa A, P1–P12

### Provenance
- **Definition**: Origin-tracking metadata. Slice ID + agent attribution + timestamps + commit SHA. An evidence category per P5.
- **Origin**: P5
- **Cross-references**: P5, Slice ID, Evidence categories

## R

### R-rules (R1–R14+)
- **Definition**: Enforced merge gates in CI that validate methodology metadata (and, per adopter, Capa C.2 stack patterns). A Capa B.1 pattern; specific Rs are adopter-instantiable (R1–R14 starter, R15+ adopter-specific).
- **Origin**: Positioning; canonicalized in IP boundary
- **Aliases prohibited**: "linter rules" (broader category), "validators" (ambiguous with runtime validation)
- **Cross-references**: Capa B.1, CI gates, Counter discipline

### Recursive Learning by Capture
- **Definition**: P7. The framework improves itself through capture. InsightRecords + LearningPatterns inform R-rule amendments via DECs. The corpus is training data.
- **Origin**: P7
- **Cross-references**: P7, InsightRecord, LearningPattern, R-rules

### Reconciliation ritual
- **Definition**: Layer 5–6 mechanisms — Block Retrospective consistency review + Quarterly Curation. Periodic drift detection + reconciliation DECs.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Block Retrospective, Quarterly Curation

## S

### Shared-Resource Pre-flight (P12)
- **Definition**: The 12th canonical principle (Capa A). Before scaling any parallelism lever beyond the baseline calibrated in the last Block Retrospective, enumerate + cap + alert + telemeter every finite/serialized shared resource that lever consumes. Operating theorem: "the success of a parallelism lever is the source of the next bottleneck."
- **Origin**: Shared-Resource Pre-flight
- **Aliases prohibited**: "resource management" (generic), "P11" (Infrastructure Continuity — distinct), "10x rule" (rejected — trigger is calibrated baseline, not a magic number)
- **Cross-references**: P11 (orthogonal — see "Why P12 ≠ P11"), Finite/serialized shared resource, CI/Pipeline Cost Economy, P3, P7

### warned degradation vs invisible hard-cut
- **Definition**: The anti-pattern framing of P12. The default for any finite shared resource must be cap+alert ("warned degradation"), never a silent hard-stop ("invisible hard-cut"). A `$0` default spending limit is the paradigmatic anti-pattern.
- **Origin**: Shared-Resource Pre-flight (P12)
- **Cross-references**: P12, Finite/serialized shared resource

### Skill (reserved)
- **Definition**: **RESERVED term** (not yet canonical). Reserved for the future **Agent-Skill** concept — a procedural pack (description + instructions + deterministic tools, composable, recursively improving, with invocation-control flags). **Formalization deferred to a future technical batch** (when the entity catalog scaffolds). Do NOT confuse with **Capability** (cognitive entity #4, formerly "Skill"). Must remain vendor-neutral (no vendor-locked naming, per P8).
- **Origin**: Determinism-over-Regeneration (term reservation)
- **Aliases prohibited**: any vendor-locked "X Skill" naming; use for the cognitive entity (that is now Capability)
- **Cross-references**: Capability (distinct entity), Determinism-over-Regeneration

### Slice
- **Definition**: An atomic, vertical, end-to-end unit of work. One AI-agent chat + one PR + one cohesive outcome. Spec + decision + code + tests + evidence + merge in one unit.
- **Origin**: P1
- **Aliases prohibited**: "story", "ticket", "task", "work item"
- **Cross-references**: P1, Slice atomicity, Token-band

### Slice ID
- **Definition**: The canonical identifier in `BL-XX.SEC-XX.SL-XXX` (Block-Section-Slice) format. A provenance carrier in branch names, commit messages, PR titles, DEC frontmatter (`originating_slice:`).
- **Origin**: P4
- **Cross-references**: P4, Provenance, Block, Slice

### Stage
- **Definition**: A computed view of the dependency DAG — which slices are mergeable now. NOT an imperative time-bound grouping (per P3).
- **Origin**: P3
- **Aliases prohibited**: "sprint" (commits velocity ahead), "phase" (linear), "milestone" (time-based)
- **Cross-references**: P3, DAG, Block

### Stack pattern
- **Definition**: A Capa C.2 pattern. An architectural pattern concrete to a technology stack, instantiable, enforced via tooling (analyzer / lint rule / CI gate), documented in the adopter's own cross-cutting architecture docs.
- **Origin**: Stack-patterns
- **Cross-references**: Capa C.2, Brain pack injection, Adopter

### Supersession
- **Definition**: An edge between DECs declaring that a new DEC replaces an earlier one. Bidirectional frontmatter: the new one has `supersedes: [old]`; the old has `superseded-by: <new>`. The graph must be acyclic.
- **Origin**: P2
- **Cross-references**: P2, Frontmatter, Bidirectional cross-reference

## T

### Token-band
- **Definition**: Slice size classification (XS/S/M/L/XL) tied to expected token consumption. Recommended defaults: XS<2M, S 2–5M, M 5–10M, L 10–20M, XL>20M (red flag).
- **Origin**: P1
- **Cross-references**: P1, Slice, Forecasting

### Topic (canonical)
- **Definition**: A tag from the canonical topic taxonomy used in DEC frontmatter `topics:`. Enables corpus indexing by theme + topic-related search.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Topic taxonomy, Layer 1

### Topic taxonomy
- **Definition**: The canonical taxonomy of SliceOps topics. Living document; new topics emerge via DEC. Documented in `topics.md`.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Topic, Layer 1, Vocabulary discipline

## V

### Vendor
- **Definition**: An organization that provides a runtime implementation (Capa C.1). Distinct from an adopter.
- **Origin**: IP boundary (three-layer)
- **Cross-references**: Adopter, Capa C.1

### Vocabulary Discipline
- **Definition**: P10. Canonical terms have canonical meanings. Synonyms drift; SliceOps does not. Fix-on-touch policy applies.
- **Origin**: P10
- **Cross-references**: P10, Glossary, Fix-on-touch

### vocabulary-changes (frontmatter field)
- **Definition**: Mandatory DEC frontmatter field. Lists canonical terms introduced or modified by the DEC. Triggers a glossary update.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Layer 1, Glossary, Vocabulary discipline

## W

### Wedge
- **Definition**: A competitive positioning differentiator. SliceOps has three: Wedge A (Audit Plane), Wedge B (DAG-driven multi-agent parallelism), Wedge C (AI-readable engineering — every artifact is training data).
- **Origin**: Positioning
- **Cross-references**: Wedge A, Wedge B, Wedge C

---

## Slot extension

Adopters may extend this glossary with domain-specific terms in their own glossaries. Canonical SliceOps terms here are reserved — do not redefine; only extend.

## Maintenance

- DEC with non-empty `vocabulary-changes` triggers an update here (same slice).
- Quarterly Curation ritual — drift detection + reconciliation.
- Fix-on-touch per P10 — slices touching stale references update forward.

Major restructure → version bump (`glossary` under a new spec version directory).
