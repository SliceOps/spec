# SliceOps™ Canonical Glossary — v1.0.0

Canonical glossary of SliceOps terms. Each term here has a **canonical meaning** (per P12 Vocabulary Discipline). Terms not listed here are not canonical SliceOps; adopters may extend with domain-specific terms in their own glossaries (extend, never redefine).

**Living document**: new terms emerge via decisions with non-empty `vocabulary-changes`; updates are part of the slice that produces the decision. Major restructure leads to a version bump.

**Per-term structure**: Definition · Origin (principle/concept that canonicalizes it) · Aliases prohibited · Cross-references.

---

## A

### Adopter
- **Definition**: An organization or product that uses the SliceOps framework to develop software or a knowledge corpus. Distinct from a vendor: adopters consume SliceOps; vendors provide runtimes (Layer C.1).
- **Origin**: IP boundary (three-layer)
- **Aliases prohibited**: "customer" (commercial), "user" (ambiguous), "implementer" (overloaded)
- **Cross-references**: Vendor, Layer C.1, Layer C.2

### Acceptance-first slice
- **Definition**: SliceOps's preferred (convention, not mandate) slice-authoring style: each slice declares its **acceptance criteria upfront** — ideally as executable acceptance tests — that simultaneously serve as a **spec-anchor** (P4 scope) and **evidence-gate** (P6 closure). A single artifact bridges the start and the end of the slice. Pairs well with Determinism-over-Regeneration (acceptance tests are deterministic).
- **Origin**: SliceOps development model (Decision 3 — preferred convention)
- **Cross-references**: P4, P6, P8, Determinism-over-Regeneration, Decision-driven, spec-anchored

### Anti-pattern
- **Definition**: A practice explicitly prohibited under SliceOps discipline. Each principle declares anti-patterns; CI gates enforce.
- **Origin**: Layer A principles
- **Cross-references**: Principle, R-rules

### Audit plane
- **Definition**: The layer above code where architectural decisions live as first-class artifacts (DECs). Empty market space pre-SliceOps; the framework's primary wedge.
- **Origin**: P2
- **Aliases prohibited**: "decision log", "ADR system" (DECs are evolved ADRs, not equivalent)
- **Cross-references**: P2, DecisionRecord, Decision Integrity

## B

### Block
- **Definition**: A logical grouping of slices with coherent scope. Closes with a Block Retrospective. Velocity calibrated post-hoc per Block.
- **Origin**: P5
- **Aliases prohibited**: "sprint" (commits velocity ahead, violates P5), "epic" (issue-tracker-flavored), "milestone" (time-based vs scope-based)
- **Cross-references**: Slice, Stage, Block Retrospective

### Block Retrospective
- **Definition**: Mandatory ritual at Block close. Includes velocity recalibration, a Cross-DEC Consistency Check section, and InsightRecord harvesting.
- **Origin**: P5, P8
- **Cross-references**: Block, Velocity, Consistency check

### Brain pack injection
- **Definition**: A mechanism that injects relevant context at the start of each slice (including applicable Layer C.2 stack patterns for the repo in scope).
- **Origin**: Layer C.2 stack-patterns
- **Cross-references**: Layer C.2, Stack pattern, ContextPack

## C

### Layer A — Principles
- **Definition**: Top-level taxonomy layer. The 12 canonical principles (P1–P12) that constitute the SliceOps framework. Immutable except by superseding DEC under an elevated HITL gate.
- **Origin**: Canonical principles
- **Cross-references**: Principle, P1–P12

### Layer B — Reference Patterns
- **Definition**: Top-level taxonomy layer. Reference patterns that materialize the principles. SliceOps IP. Has sub-layers (B.1 Framework Artifacts, B.2 Universal Engineering Patterns).
- **Origin**: IP boundary and hierarchical taxonomy
- **Aliases prohibited**: bare "Layer B" without sub-letter is ambiguous in technical context — always specify B.1 or B.2 when relevant
- **Cross-references**: Layer B.1, Layer B.2

### Layer B.1 — Framework Artifacts
- **Definition**: Sub-layer of Layer B. SliceOps-originated patterns: entity catalog (13 cognitive entities), repo folder structure, R-rules system, counter discipline, frontmatter schemas, file templates, vocabulary discipline mechanism.
- **Origin**: Hierarchical taxonomy
- **Cross-references**: Cognitive entity, Folder structure, R-rules

### Layer B.2 — Universal Engineering Patterns
- **Definition**: Sub-layer of Layer B. Industry-canonical engineering patterns SliceOps reaffirms: SOLID, ACID, Outbox, Fail-Fast, Idempotency, Defense in Depth, CI/Pipeline Cost Economy, Determinism-over-Regeneration. Vendor-agnostic, stack-agnostic.
- **Origin**: Stack-patterns and hierarchical taxonomy
- **Cross-references**: SOLID, ACID, Outbox, Idempotency, CI/Pipeline Cost Economy, Determinism-over-Regeneration

### Layer C — Implementations
- **Definition**: Top-level taxonomy layer. Specific implementations, not canonical SliceOps. Has sub-layers (C.1 Vendor Runtimes, C.2 Adopter Stack Patterns).
- **Origin**: IP boundary and hierarchical taxonomy
- **Aliases prohibited**: bare "Layer C" without sub-letter is ambiguous — specify C.1 or C.2
- **Cross-references**: Layer C.1, Layer C.2

### Layer C.1 — Vendor Runtimes
- **Definition**: Sub-layer of Layer C. Vendor-owned runtime products implementing the SliceOps Layer B catalog — e.g., hosted knowledge-graph products, third-party tool adapters, custom homegrown brains. A reference runtime is one runtime, not the runtime (P11).
- **Origin**: IP boundary and hierarchical taxonomy
- **Cross-references**: Vendor, Adapter, P11

### Layer C.2 — Adopter Stack Patterns
- **Definition**: Sub-layer of Layer C. Adopter-defined patterns instantiable per technology stack — e.g., Repository pattern (.NET), FluentValidation, Riverpod state management (Flutter). Each adopter defines its own Layer C.2 with enforcement tooling (analyzers / lint rules / CI gates).
- **Origin**: Stack-patterns and hierarchical taxonomy
- **Cross-references**: Adopter, Stack pattern, Brain pack injection

### Capability
- **Definition**: Cognitive entity #4 in the Layer B.1 catalog. Capabilities accrued by individuals/agents/teams. **Renamed from "Skill"** ("capabilities accrued" describes Capability, not Skill; the rename improves precision and frees the term "Skill").
- **Origin**: Catalog split (entity #4) and Determinism-over-Regeneration (rename)
- **Aliases prohibited**: "Skill" (former name, now reserved for a distinct concept — do NOT use for this entity)
- **Cross-references**: Cognitive entity, Layer B.1, P8, Skill (reserved — distinct concept)

### CI/Pipeline Cost Economy
- **Definition**: A Layer B.2 Universal Engineering Pattern. Five stack-agnostic levers for pipeline economy: concurrency-cancel-in-progress, change-scoped job gating, aggregation-required-gate, draft-skip of expensive jobs, and dependency-cache. Materializes P9 in the CI domain. The concrete per-CI-provider/stack instance is Layer C.2.
- **Origin**: Shared-Resource Pre-flight (P9)
- **Aliases prohibited**: "CI optimization" (generic), "pipeline tuning" (under-specified)
- **Cross-references**: P9, Layer B.2, aggregation-required-gate, Outbox (sibling B.2)

### aggregation-required-gate
- **Definition**: A CI design pattern within CI/Pipeline Cost Economy (B.2). An `if: always()` job that is THE required check, resolving the "required check skipped, so PR blocked forever" trap introduced by change-scoped job gating. Mandatory when path-gating is used.
- **Origin**: Shared-Resource Pre-flight (P9)
- **Cross-references**: CI/Pipeline Cost Economy, change-scoped job gating

### Cognitive entity
- **Definition**: One of the 13 canonical entity types of SliceOps Layer B.1 (DecisionRecord, InsightRecord, OutcomeRecord, Capability, Goal, LearningPattern, CognitiveFramework, ContextPack, ActivePriority, RelationshipContext, Preference, Value, **Session**). Each has a frontmatter schema and lifecycle.
- **Origin**: Catalog split and Session as first-class unit
- **Aliases prohibited**: "entity type" (ambiguous with database entities), "metadata record" (under-specified)
- **Cross-references**: Layer B.1, Entity catalog, DecisionRecord, InsightRecord, Session

### CognitiveFramework
- **Definition**: Cognitive entity. A mental model or reference structure for reasoning and decision-making (e.g., this glossary, the topic taxonomy).
- **Origin**: Catalog split
- **Cross-references**: Cognitive entity

### consistency-check (frontmatter field)
- **Definition**: Mandatory DEC frontmatter field (Layer 1). A multi-line paragraph declaring how the DEC relates to the existing corpus.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Layer 1, Frontmatter discipline, conflicts-with

### conflicts-with (frontmatter field)
- **Definition**: Mandatory DEC frontmatter field. Lists DEC IDs that could appear to contradict, and a resolution paragraph in the body if non-empty.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Layer 1, consistency-check

### ContextPack
- **Definition**: Cognitive entity. A pre-computed bundle of context loaded at slice/session start. Enables P11 platform-agnosticism (bundles portable cross-tools). **Evolves from static to routed/dynamic** per the Context Router (selection of relevant context-experts by topic/dependency at session start, rather than loading the whole corpus).
- **Origin**: Catalog split and Context Router
- **Cross-references**: Brain pack injection, P11, Context Router, context-expert

### Calibration discipline
- **Definition**: The discipline of deriving the sizing bands (token-band, context-band) from **real data and the vigent model landscape**, NOT axiomatically. Reproducible (a versioned deterministic script parses real session corpus → percentiles → bands), quarterly cadence (hooks into the Quarterly Curation Ritual — Layer 6), and versioned (each calibration records date, script-version, dataset, model landscape, and resulting bands so band drift is auditable over time).
- **Origin**: Bidimensional sizing and Calibration discipline
- **Aliases prohibited**: "ad-hoc calibration" (anti-pattern: not reproducible, not versioned), "axiomatic bands" (rejected)
- **Cross-references**: Token-band, context-band, Model Triage, model landscape, Quarterly Curation, Determinism-over-Regeneration

### Counter discipline
- **Definition**: Layer B.1 pattern. Atomic increment per prefix and a validate-no-duplicate CI check. Prevents counter collision in multi-coordinator parallel work. Originated as empirical practice in reference-implementation context; canonicalized in SliceOps.
- **Origin**: IP boundary (canonicalized)
- **Cross-references**: R-rules, P9, DEC numbering

## D

### DAG (Directed Acyclic Graph)
- **Definition**: The slice dependency graph. Slices have explicit `depends_on:` edges. Stage is a view derived from the DAG (P5).
- **Origin**: P5
- **Cross-references**: P5, Stage, Slice

### DEC (DecisionRecord)
- **Definition**: Cognitive entity. An architectural/strategic decision recorded with lifecycle (proposed → accepted → superseded/deprecated), supersession edges, alternatives considered, consequences. Naming: `DR-YYYY-MM-DD-slug.md` (date-based) or `DEC-NNN-slug.md` (counter-based, per repo convention).
- **Origin**: Catalog split; P2/P1
- **Aliases prohibited**: "ADR" (predecessor, DECs are evolved), "decision doc", "note"
- **Cross-references**: ADR, P2, P1

### Decision Integrity by Construction
- **Definition**: P1. Decisions emerge from slices; every DEC traces to a slice (provenance). Out-of-band decisions must be backed into a slice retroactively.
- **Origin**: P1
- **Cross-references**: P1, Slice provenance, Originating slice

### Decision-driven (development model)
- **Definition**: SliceOps's canonical development model: **decision-driven and evidence-gated**, with **spec-anchoring** per slice. The driver and wedge is the audit/decision plane (P2), NOT the spec. Distinct from spec-driven-first (where the spec is the source of truth, immutable, and divergence is a bug): in SliceOps the source of truth is the corpus of decisions and merged code with evidence; the spec evolves and the decision-of-why-it-changed is itself the valuable artifact (P8).
- **Origin**: SliceOps development model
- **Aliases prohibited**: "spec-driven" (incorrect characterization), "specless" (also incorrect — specs are anchors)
- **Cross-references**: P2, P1, P6, P8, spec-anchored, development-style-agnostic, Acceptance-first slice

### development-style-agnostic
- **Definition**: A characterization of SliceOps (analog to P11 Platform-Agnostic, applied to input/authoring style): SliceOps is a discipline plane that wraps any development input style — spec-first (e.g., Spec Kit), test-first, contract-first, sketch-first. Spec-driven adopters compose SliceOps on top; they don't compete with it. The 12 principles do not prescribe the input style — they prescribe the discipline plane.
- **Origin**: SliceOps development model
- **Cross-references**: P11 (analog), Decision-driven, spec-anchored

### Determinism-over-Regeneration
- **Definition**: A Layer B.2 Universal Engineering Pattern. If a process repeats, materialize it once as a deterministic reusable artifact (script, function, reference file, R-rule); do NOT stochastically regenerate it with AI each time. Deterministic code (same input → same result) is cheaper, faster, repeatable, and auditable vs AI output with drift. Rule: "if you can use code instead of AI, do; have AI write the code once, then reuse it."
- **Origin**: Determinism-over-Regeneration
- **Aliases prohibited**: "DRY for AI" (imprecise), "caching" (under-specified)
- **Cross-references**: Layer B.2, P6, P8, P9, CI/Pipeline Cost Economy (sibling B.2)

### one-off-vs-permanent tuning gate
- **Definition**: A P8 granularity clarification (does not change the statement). Artifact-level: whenever an artifact underperforms, ask "one-off adjustment or permanent?"; if permanent, update the artifact immediately (don't wait for ≥3). LearningPattern-level: a pattern observed ≥3 times leads to canonical promotion. Two complementary granularities.
- **Origin**: Determinism-over-Regeneration
- **Cross-references**: P8, LearningPattern, InsightRecord

## E

### Evidence-by-Construction
- **Definition**: P6. Each slice produces evidence in 4 categories (functional, quality, decision, provenance) plus security (P7). Hard gates enforce; slices without complete evidence don't merge.
- **Origin**: P6
- **Cross-references**: P6, P7, Evidence categories

### Entity catalog
- **Definition**: The canonical set of 13 cognitive entity types of SliceOps Layer B.1. Each entity has a frontmatter schema, lifecycle, cross-reference patterns, and anti-patterns. Published in `reference/entity-catalog/`.
- **Origin**: Catalog split and Session as first-class unit
- **Cross-references**: Cognitive entity, Layer B.1, Session

## F

### Finite/serialized shared resource
- **Definition**: A consumable or serialized resource, shared cross-slice/cross-coordinator, with a hard limit: CI minutes, counters, API rate limits, branch-protection serialization, DB migration locks, worktree/checkout state, connection pools. The resource class P9 mandates enumerating, capping, alerting, and telemetering before scaling parallelism.
- **Origin**: Shared-Resource Pre-flight (P9)
- **Aliases prohibited**: generic "shared resource" without "finite/serialized" (loses the key property)
- **Cross-references**: P9, infra-cost-ledger

### infra-cost-ledger
- **Definition**: A Layer B.1 extension of the cost-ledger. Tracks the infra/CI cost dimension alongside token cost. The pre-Block checklist verifies infra/CI budget headroom. Closes the "infra-cost blindness" failure (a token-only ledger).
- **Origin**: Shared-Resource Pre-flight (P9)
- **Cross-references**: P9, Layer B.1, cost-ledger, token-band

### Fix-on-touch
- **Definition**: A P12 Vocabulary Discipline policy. Any slice that detects vocabulary drift in a file it touches updates it forward (no separate cleanup slice).
- **Origin**: P12
- **Cross-references**: P12, Vocabulary discipline, Glossary

### Frontmatter discipline (Layer 1)
- **Definition**: The Layer 1 mandatory frontmatter spec for all DECs. Includes consistency-check, conflicts-with, topics, vocabulary-changes fields.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Layer 1, consistency-check, conflicts-with

## G

### Glossary
- **Definition**: This document. The canonical glossary of SliceOps terms. Living document; updated by every decision with non-empty `vocabulary-changes`.
- **Origin**: P12; consistency-management mechanism
- **Cross-references**: P12, Vocabulary discipline, Layer 1

## H

### Hierarchical Layer Taxonomy
- **Definition**: The meta-decision on the naming structure of Layer A/B/C. Top-level Layer A/B/C are stable; sub-numbering (B.1, B.2, C.1, C.2) accommodates new dimensions without renaming.
- **Origin**: Hierarchical taxonomy
- **Cross-references**: Layer A/B/C, Scalability

### HITL (Human-In-The-Loop)
- **Definition**: P3. Humans retain final authority over scope, merges, architectural direction. AI agents propose; humans dispose.
- **Origin**: P3
- **Cross-references**: P3, Merge gate, CODEOWNERS

## I

### Idempotency
- **Definition**: A Layer B.2 universal engineering pattern. The same operation invoked multiple times produces the same result. Implemented via Idempotency-Key headers, deduplication tables, etc.
- **Origin**: Stack-patterns
- **Cross-references**: Layer B.2, ACID, Defense in Depth

### Infrastructure Continuity
- **Definition**: P10. Code, IaC, DB schemas, env configs form one continuum. SliceOps discipline applies uniformly.
- **Origin**: P10
- **Cross-references**: P10, Stack pattern, IaC

### InsightRecord
- **Definition**: Cognitive entity. An empirical observation captured from a slice. Append-only. Raw material for LearningPatterns. Naming: `INS-NNN-slug.md`.
- **Origin**: Catalog split; P8
- **Cross-references**: P8, LearningPattern, Recursive Learning

## L

### LLM-Inference-Cost-Economy
- **Definition**: A Layer B.2 **sub-domain pattern** specialized within CI/Pipeline Cost Economy. Applies when a CI/CD workflow calls a paid LLM API (audit, code-review, QA, codegen). Adds three genuinely-new levers (prompt-caching discipline, model-tier discipline, diff-only context windowing) and refines two parent levers (trigger-set minimalism LLM-aware, LLM-aware draft gate green-not-skipped). Extends the cost-ledger to a third dimension: LLM-API-in-CI cost (independent of token and infra dimensions).
- **Origin**: LLM-Inference-Cost-Economy
- **Aliases prohibited**: "LLM cost optimization" (generic), "CI LLM tuning" (under-specified)
- **Cross-references**: P9, Layer B.2, CI/Pipeline Cost Economy (parent), Determinism-over-Regeneration, model-tier discipline, prompt-caching discipline

### LearningPattern
- **Definition**: Cognitive entity. A pattern observed ≥3 times across InsightRecords; promoted as a canonical pattern. Naming: `LP-NNN-slug.md`. Triggers a DEC for R-rule amendments.
- **Origin**: Catalog split; P8
- **Cross-references**: P8, InsightRecord, R-rules

## M

### Mode S / Mode M
- **Definition**: P11 operation modes. Mode S = single-agent sequential (one slice at a time, Wedge A only); Mode M = multi-agent parallel (N simultaneous slices with a coordinator, both wedges).
- **Origin**: P11
- **Cross-references**: P11, Wedge A, Wedge B, Coordinator

### Model Triage
- **Definition**: A Layer B.1 artifact. Routes each slice/session to a **(model and execution-mode)** recommendation according to five axes, in filter order: (1) **context-band** as primary filter — which models have a window ≥ footprint? (2) **sensitivity → locality** — can it leave to an external API or must it be local? (3) **complexity** — token-band and slice-type → reasoning tier. (4) **latency** — speed need. (5) **cost** — economic tier. Plus a **synthesis efficiency** axis with the consuming/producing distinction. Recommends; the human disposes (P3). The choice (`model_used`, `execution_mode`, `triage_rationale`) is recorded in Session provenance (P2 audit plane).
- **Origin**: Bidimensional sizing and Model Triage
- **Aliases prohibited**: "model selection" (under-specified), "routing" (ambiguous — distinct from Context Router)
- **Cross-references**: context-band, Token-band, Session, synthesis efficiency, P3, P9, execution-mode, model landscape

### model landscape
- **Definition**: A snapshot of the model classes / context windows available at the time of a calibration. Recalibration is triggered when the landscape changes materially (e.g., local models reaching mainstream 128K, frontier crossing 2M). Versioned as part of the Calibration discipline.
- **Origin**: Bidimensional sizing and Calibration discipline
- **Cross-references**: Model Triage, Calibration discipline, Quarterly Curation

### execution-mode
- **Definition**: How a slice/session is executed against a model: `frontier-API`, `local-via-API`, `account-with-plan` (fixed-cost subscription already paid), or `local-in-IDE`. A Model Triage axis tied to sensitivity → locality (P7) and cost (P9).
- **Origin**: Model Triage
- **Cross-references**: Model Triage, P7, P9

## O

### Orchestrate
- **Definition**: A canonical Session-Type. A session that coordinates other sessions (does not produce direct work output). **Renamed from the abbreviated "COORD"** — the convention is full words, not opaque abbreviations (P12). Examples: a coordinator session managing parallel slice execution, a meta-session orchestrating a multi-session research program.
- **Origin**: Session as first-class unit
- **Aliases prohibited**: "COORD" (deprecated abbreviation), "coordinator" (role, not Session-Type)
- **Cross-references**: Session-Type, Session, P12

## P

### Principle
- **Definition**: One of the 12 canonical SliceOps principles (P1–P12). Layer A. Immutable except by superseding DEC under an elevated HITL gate.
- **Origin**: Canonical principles
- **Cross-references**: Layer A, P1–P12

### Provenance
- **Definition**: Origin-tracking metadata. Slice ID, agent attribution, timestamps, and commit SHA. An evidence category per P6.
- **Origin**: P6
- **Cross-references**: P6, Slice ID, Evidence categories

## R

### R-rules (R1–R14+)
- **Definition**: Enforced merge gates in CI that validate framework metadata (and, per adopter, Layer C.2 stack patterns). A Layer B.1 pattern; specific Rs are adopter-instantiable (R1–R14 starter, R15+ adopter-specific).
- **Origin**: Positioning; canonicalized in IP boundary
- **Aliases prohibited**: "linter rules" (broader category), "validators" (ambiguous with runtime validation)
- **Cross-references**: Layer B.1, CI gates, Counter discipline

### Recursive Learning by Capture
- **Definition**: P8. The framework improves itself through capture. InsightRecords and LearningPatterns inform R-rule amendments via DECs. The corpus is training data.
- **Origin**: P8
- **Cross-references**: P8, InsightRecord, LearningPattern, R-rules

### Reconciliation ritual
- **Definition**: Layer 5–6 mechanisms — Block Retrospective consistency review and Quarterly Curation. Periodic drift detection and reconciliation DECs.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Block Retrospective, Quarterly Curation

## S

### Shared-Resource Pre-flight (P9)
- **Definition**: The 12th canonical principle (Layer A). Before scaling any parallelism lever beyond the baseline calibrated in the last Block Retrospective, enumerate, cap, alert, and telemeter every finite/serialized shared resource that lever consumes. Operating theorem: "the success of a parallelism lever is the source of the next bottleneck."
- **Origin**: Shared-Resource Pre-flight
- **Aliases prohibited**: "resource management" (generic), "P10" (Infrastructure Continuity — distinct), "10x rule" (rejected — trigger is calibrated baseline, not a magic number)
- **Cross-references**: P10 (orthogonal — see "Why P9 ≠ P10"), Finite/serialized shared resource, CI/Pipeline Cost Economy, P5, P8

### warned degradation vs invisible hard-cut
- **Definition**: The anti-pattern framing of P9. The default for any finite shared resource must be cap and alert ("warned degradation"), never a silent hard-stop ("invisible hard-cut"). A `$0` default spending limit is the paradigmatic anti-pattern.
- **Origin**: Shared-Resource Pre-flight (P9)
- **Cross-references**: P9, Finite/serialized shared resource

### Session
- **Definition**: Cognitive entity #13 in the Layer B.1 catalog. The unit of human–AI interaction (one conversation/chat with an AI agent). Every AI interaction is a Session, identifiable and auditable. **The Slice is the DEV Session-Type** — every slice is a session; not every session is a slice (Meta, Audit, Learning, Support, Infra, Artifact, Orchestrate are valid Session-Types that do not produce a PR). Decisions emerge from sessions (P1 generalized).
- **Origin**: Session as first-class unit
- **Aliases prohibited**: "chat" (under-specified), "conversation" (informal), "interaction" (ambiguous)
- **Cross-references**: Slice, Session-Type, P2, P1, P6, Cognitive entity

### Session-Type
- **Definition**: A canonical classification of a Session (level 1). Eight universal types: **Slice** (development → PR), **Artifact** (bounded output), **Support** (incidents/care), **Infra** (infra/deploy/ops), **Meta** (governance), **Audit** (verification/control), **Learning** (exploration/research), **Orchestrate** (coordinates other sessions). Vendor-neutral; adopter-specific sub-variants are Layer C.2.
- **Origin**: Session as first-class unit
- **Aliases prohibited**: "category" (too broad), "kind" (informal)
- **Cross-references**: Session, Slice-Type, Orchestrate

### Slice-Type
- **Definition**: A level-2 classification, only when Session-Type=Slice. Three canonical: **Dev** (feature, typically SemVer minor), **Refactor** (no functional change, SemVer patch), **Fix** (bugfix, SemVer patch). Adopters may add stack-specific Slice-Types (Layer C.2).
- **Origin**: Session as first-class unit
- **Cross-references**: Session-Type, Slice

### Slice
- **Definition**: An atomic, vertical, end-to-end unit of work. One AI-agent chat, one PR, one cohesive outcome. Spec, decision, code, tests, evidence, and merge in one unit. **Clarification (slice ⊂ session)**: the Slice is the DEV Session-Type — there are other valid Session-Types (Meta, Audit, Learning, etc.) that do not produce a PR; P4 governs the atomicity of DEV slices specifically.
- **Origin**: P4; clarified by Session as first-class unit
- **Aliases prohibited**: "story", "ticket", "task", "work item"
- **Cross-references**: P4, Session, Session-Type, Slice-Type, Token-band

### synthesis efficiency
- **Definition**: A calibrable model attribute = the **semantic density** with which a model creates context (information preserved per output token). "Says the same thing without losing the idea." Varies across models (a language skill, like code-golf for code: 1 line vs 70). An **axis of Model Triage** (priority for context-producing slices). Proxy measurement: output-tokens to pass fixed acceptance criteria. Caveat: density ≠ terseness; optimum is maximum density that still passes the acceptance gate (P6) and remains auditable (P2).
- **Origin**: Context Router and synthesis efficiency
- **Cross-references**: Model Triage, context-consuming vs context-producing slice, P6, Determinism-over-Regeneration

### Slice ID
- **Definition**: The canonical identifier in `BL-XX.SEC-XX.SL-XXX` (Block-Section-Slice) format. A provenance carrier in branch names, commit messages, PR titles, DEC frontmatter (`originating_slice:`).
- **Origin**: P1
- **Cross-references**: P1, Provenance, Block, Slice

### Stage
- **Definition**: A computed view of the dependency DAG — which slices are mergeable now. NOT an imperative time-bound grouping (per P5).
- **Origin**: P5
- **Aliases prohibited**: "sprint" (commits velocity ahead), "phase" (linear), "milestone" (time-based)
- **Cross-references**: P5, DAG, Block

### Stack pattern
- **Definition**: A Layer C.2 pattern. An architectural pattern concrete to a technology stack, instantiable, enforced via tooling (analyzer / lint rule / CI gate), documented in the adopter's own cross-cutting architecture docs.
- **Origin**: Stack-patterns
- **Cross-references**: Layer C.2, Brain pack injection, Adopter

### spec-anchored
- **Definition**: How SliceOps uses specs: the spec **anchors** the slice scope (prevents drift, declares the outcome upfront) but is **co-equal** with decision and evidence, NOT sovereign. Distinct from "spec-driven" (where the spec is the driver and source of truth). The framework itself has a versioned spec (this document and siblings) — but that is the spec of the framework, not spec-driven-development per project.
- **Origin**: SliceOps development model
- **Aliases prohibited**: "spec-driven" (different concept), "specless" (incorrect)
- **Cross-references**: Decision-driven, Acceptance-first slice, P4

### Supersession
- **Definition**: An edge between DECs declaring that a new DEC replaces an earlier one. Bidirectional frontmatter: the new one has `supersedes: [old]`; the old has `superseded-by: <new>`. The graph must be acyclic.
- **Origin**: P2
- **Cross-references**: P2, Frontmatter, Bidirectional cross-reference

## T

### Token-band
- **Definition**: Slice/session size classification (XS/S/M/L/XL) for **throughput** — measured in **billed-equivalent** tokens (input + cache_creation×1.25 + cache_read×0.1 + output), NOT total-with-cache (which inflates ~5×). Calibrated bands (baseline 2026-06-15): XS<2M · S 2–5M · M 5–10M · L 10–20M · XL>20M. Governs cost (P9) and forecast.
- **Origin**: P4 and Bidimensional sizing
- **Aliases prohibited**: "total-with-cache" as the band unit (inflates the measurement; not the canonical unit)
- **Cross-references**: P4, P9, Slice, Session, context-band, Sizing, Calibration discipline

### context-band
- **Definition**: Slice/session size classification (XS/S/M/L/XL) for **peak context footprint** — the maximum `input + cache_creation + cache_read` loaded in a single turn. Orthogonal to token-band. Calibrated bands (baseline 2026-06-15): XS<32K · S 32–128K · M 128–200K · L 200–512K · XL>512K. Governs **model viability** (the primary filter in Model Triage — a model whose window is smaller than the footprint cannot run the slice).
- **Origin**: Bidimensional sizing
- **Cross-references**: P4, Sizing, Model Triage, Calibration discipline, Context Router

### Context Router
- **Definition**: A Layer B.1 artifact. Routes context selectively to each slice/session — instead of loading the whole corpus, activates only the relevant **context-experts** (DECs/entities/code-modules grouped by topic/dependency). Three mechanisms: (1) routing, (2) compression (coordinator summaries, handoff contracts), (3) sparse working set. Reduces the context-band footprint that Model Triage filters on. MoE-inspired (gating-network analog at the orchestration level, NOT a claim about the transformer's internal architecture).
- **Origin**: Context Router and synthesis efficiency
- **Cross-references**: ContextPack, context-band, context-expert, Model Triage

### context-expert
- **Definition**: A specialized context module (a cluster of DECs / entities / code modules grouped by topic or dependency) that can be activated selectively by the Context Router. The "expert" analog from MoE applied to context selection, not to model weights.
- **Origin**: Context Router
- **Cross-references**: Context Router, ContextPack

### context-consuming vs context-producing slice
- **Definition**: A triage distinction. A **context-consuming** slice reads a lot (analysis over existing code/corpus), so Model Triage prioritizes a large window. A **context-producing** slice writes a lot (specs/docs/code/refactor), so Model Triage prioritizes synthesis efficiency (density). A model optimal for consuming is not necessarily optimal for producing.
- **Origin**: Context Router and synthesis efficiency
- **Cross-references**: Model Triage, synthesis efficiency, Context Router

### Topic (canonical)
- **Definition**: A tag from the canonical topic taxonomy used in DEC frontmatter `topics:`. Enables corpus indexing by theme and topic-related search.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Topic taxonomy, Layer 1

### Topic taxonomy
- **Definition**: The canonical taxonomy of SliceOps topics. Living document; new topics emerge via DEC. Documented in `topics.md`.
- **Origin**: Consistency-management mechanism
- **Cross-references**: Topic, Layer 1, Vocabulary discipline

## V

### Vendor
- **Definition**: An organization that provides a runtime implementation (Layer C.1). Distinct from an adopter.
- **Origin**: IP boundary (three-layer)
- **Cross-references**: Adopter, Layer C.1

### Vocabulary Discipline
- **Definition**: P12. Canonical terms have canonical meanings. Synonyms drift; SliceOps does not. Fix-on-touch policy applies.
- **Origin**: P12
- **Cross-references**: P12, Glossary, Fix-on-touch

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
- Quarterly Curation ritual — drift detection and reconciliation.
- Fix-on-touch per P12 — slices touching stale references update forward.

Major restructure leads to a version bump (`glossary` under a new spec version directory).
