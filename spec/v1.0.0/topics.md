# SliceOps™ Canonical Topic Taxonomy — v1.0.0

Canonical taxonomy of SliceOps topics. Every DEC declares `topics:` in frontmatter from this list (Layer 1 frontmatter discipline). Enables:

- Corpus indexing by theme
- Pre-merge consistency check (Layer 2) — search topic-related DECs
- Conflict detection (Layer 3 R-rules) — DECs with the same topic must be cross-referenced
- Quarterly curation (Layer 6) — topic merging/splitting per drift detection

**Per-topic structure**: Scope · Parent topic · Sub-topics · Cross-references.

---

## Top-level topics

### foundational
- **Scope**: Decisions establishing Layer A principles or foundational framework concepts.
- **Parent**: (none — top-level)
- **Sub-topics**: principles, vocabulary-discipline, meta-framework
- **Cross-references**: principles, meta-framework

### principles
- **Scope**: Decisions about Layer A principles (P1–P12): amendments, deprecation, clarification.
- **Parent**: foundational
- **Sub-topics**: specific principles can become sub-topics if extensive DECs emerge (e.g., `p7-recursive-learning-operational`)
- **Cross-references**: foundational, layer-a-principles-amendment

### ip-boundary
- **Scope**: Decisions about the IP/scope axis — Layer A/B/C boundary, ownership, licensing.
- **Parent**: foundational
- **Sub-topics**: layer-a-principles, layer-b-reference-patterns, layer-c-implementations, licensing, trademark
- **Cross-references**: licensing, layer-c-vendor-runtime, layer-c-adopter-stack

### hierarchical-taxonomy
- **Scope**: Decisions about naming structure and the hierarchical layer taxonomy (Layer A/B/C top-level and sub-numbering B.1, C.2, etc.).
- **Parent**: foundational
- **Sub-topics**: layer-naming, sub-layer-numbering
- **Cross-references**: ip-boundary, scalability, vocabulary-discipline

## Patterns and practice

### layer-b-framework-artifact
- **Scope**: Layer B.1 patterns — entity catalog, folder structure, R-rules, counter discipline, frontmatter schemas, file templates.
- **Parent**: ip-boundary > layer-b-reference-patterns
- **Sub-topics**: entity-catalog, folder-structure, r-rules, counter-discipline, frontmatter-schema, file-templates
- **Cross-references**: layer-b-engineering-universal

### layer-b-engineering-universal
- **Scope**: Layer B.2 universal engineering patterns — SOLID, ACID, Outbox, Fail-Fast, Idempotency, Defense-in-Depth, CI/Pipeline Cost Economy, Determinism-over-Regeneration.
- **Parent**: ip-boundary > layer-b-reference-patterns
- **Sub-topics**: solid, acid, outbox, idempotency, fail-fast, defense-in-depth, ci-cost-economy, determinism-over-regeneration
- **Cross-references**: layer-c-adopter-stack

### layer-c-vendor-runtime
- **Scope**: Layer C.1 — vendor-owned runtime product implementations.
- **Parent**: ip-boundary > layer-c-implementations
- **Sub-topics**: adapters
- **Cross-references**: vendor, layer-c-adopter-stack

### layer-c-adopter-stack
- **Scope**: Layer C.2 — adopter-defined stack-specific instantiable patterns.
- **Parent**: ip-boundary > layer-c-implementations
- **Sub-topics**: dotnet-stack, nodejs-stack, flutter-stack, python-stack, rust-stack, go-stack (added as adopters publish)
- **Cross-references**: layer-b-engineering-universal, adopter, brain-pack-injection

### entity-catalog
- **Scope**: Decisions about the 13 canonical cognitive entity types.
- **Parent**: layer-b-framework-artifact
- **Sub-topics**: decision-record-pattern, insight-record-pattern, learning-pattern, session-management, etc.
- **Cross-references**: vocabulary-discipline, layer-b-framework-artifact, session-management

### session-management
- **Scope**: Decisions about the Session entity (#13), Session-Type taxonomy, lifecycle disposition, cross-cutting dimensions, and the slice⊂session containment.
- **Parent**: layer-b-framework-artifact
- **Sub-topics**: session-type, slice-type, lifecycle-disposition, orchestrate-session
- **Cross-references**: entity-catalog, audit-plane, development-model

### folder-structure
- **Scope**: Decisions about the canonical repo folder structure for SliceOps-compliant repos.
- **Parent**: layer-b-framework-artifact
- **Cross-references**: layer-b-framework-artifact, recursive-dogfooding

### r-rules
- **Scope**: The R-rules system — enforced CI merge gates. Adopter-instantiable (R1–R14 starter, R15+ adopter-specific).
- **Parent**: layer-b-framework-artifact
- **Sub-topics**: r1-counter-discipline, r2-frontmatter-schema, …, r-rules-amendment
- **Cross-references**: layer-b-framework-artifact, ci-gates, p7-recursive-learning-operational

### counter-discipline
- **Scope**: Counter atomicity and reconciliation strategies (renumber, accept-ours, merge).
- **Parent**: layer-b-framework-artifact
- **Cross-references**: r-rules, cross-coordinator-shared-state, finite-resource-stewardship

## Operation and workflow

### evidence-categories
- **Scope**: The evidence categories (functional, quality, security, decision, provenance) per P6 and P7.
- **Parent**: principles > p5-evidence-by-construction
- **Cross-references**: p5-evidence-by-construction, p6-security-by-construction

### slice-workflow
- **Scope**: The slice anatomy — scope declaration, branch, AI-agent chat, pre-merge checklist, PR, cleanup.
- **Parent**: principles > p1-slice-atomicity
- **Cross-references**: p1-slice-atomicity, evidence-categories, multi-agent-parallelism

### multi-agent-parallelism
- **Scope**: Mode M operation — multi-chat parallel, coordinator role, worktree discipline, adjacency conflicts.
- **Parent**: principles > p8-platform-agnostic
- **Cross-references**: p8-platform-agnostic, mode-s, mode-m, worktree-discipline

### worktree-discipline
- **Scope**: Worktree canonical path, lifecycle, cleanup, prohibitions.
- **Parent**: multi-agent-parallelism
- **Cross-references**: multi-agent-parallelism, p7-recursive-learning-operational

## Meta-framework

### meta-framework
- **Scope**: Decisions about the framework itself — taxonomy, naming, consistency management, vocabulary discipline.
- **Parent**: foundational
- **Sub-topics**: hierarchical-taxonomy, consistency-management, context-discipline, vocabulary-discipline, corpus-integrity
- **Cross-references**: foundational, scalability

### consistency-management
- **Scope**: The multi-layer mechanism preventing corpus contradictions (Layers 1–6).
- **Parent**: meta-framework
- **Sub-topics**: frontmatter-discipline, pre-merge-checklist, r-rules-validators, reconciliation-ritual
- **Cross-references**: vocabulary-discipline, p2-audit-plane, p7-recursive-learning-operational

### context-discipline
- **Scope**: The P12 principle — context as a **governed substrate** for memoryless agents: single-source-of-truth, foundations-first context architecture, selective routing (Context Router), and multi-agent coherence. The vocabulary canon is one facet. Reframed from "Vocabulary Discipline".
- **Parent**: principles + meta-framework
- **Sub-topics**: vocabulary-discipline, context-router, model-triage, consistency-management, corpus-integrity
- **Cross-references**: vocabulary-discipline, context-router, consistency-management, corpus-integrity, model-triage

### vocabulary-discipline
- **Scope**: **Facet of P12 Context Discipline** — term canonicity: glossary, fix-on-touch policy, and term-canonicity.
- **Parent**: context-discipline
- **Sub-topics**: glossary-coverage, term-canonicity, fix-on-touch
- **Cross-references**: context-discipline, glossary, consistency-management

### corpus-integrity
- **Scope**: Decisions about corpus health — bidirectional cross-references, acyclic supersession chain, no orphans, drift detection.
- **Parent**: meta-framework
- **Sub-topics**: bidirectional-cross-reference, supersession-chain, drift-detection
- **Cross-references**: consistency-management, audit-plane

### p7-recursive-learning-operational
- **Scope**: Operationalization of P8 — InsightRecord → LearningPattern → DEC flow and thresholds.
- **Parent**: principles > p7-recursive-learning
- **Cross-references**: p7-recursive-learning, insight-record-pattern, learning-pattern

### scalability
- **Scope**: Framework properties enabling scaling from N=5 to N=500 or more DECs without chaos.
- **Parent**: meta-framework
- **Cross-references**: meta-framework, consistency-management, hierarchical-taxonomy

### finite-resource-stewardship
- **Scope**: Decisions about P9 (Shared-Resource Pre-flight) — enumerate, cap, alert, and telemeter finite/serialized shared resources before scaling parallelism. Unifies resource-contention precedents (counter, worktree, CI minutes, rate limits).
- **Parent**: meta-framework
- **Sub-topics**: ci-cost-economy, infra-cost-ledger, shared-resource-preflight
- **Cross-references**: scalability, multi-agent-parallelism, p7-recursive-learning-operational, layer-b-engineering-universal

### ci-cost-economy
- **Scope**: Decisions about the Layer B.2 pattern "CI/Pipeline Cost Economy" — concurrency-cancel, change-gating, aggregation-gate, draft-skip, and dependency-cache; plus per-CI-provider/stack C.2 instances.
- **Parent**: layer-b-engineering-universal
- **Sub-topics**: aggregation-required-gate, change-scoped-job-gating, concurrency-cancel-in-progress
- **Cross-references**: finite-resource-stewardship, layer-b-engineering-universal, layer-c-adopter-stack

### determinism-over-regeneration
- **Scope**: Decisions about the Layer B.2 pattern "Determinism-over-Regeneration" — materialize repeated processes as deterministic reusable artifacts vs AI regeneration; plus the Skill→Capability naming resolution (P12) from the same analysis.
- **Parent**: layer-b-engineering-universal
- **Sub-topics**: one-off-vs-permanent-tuning-gate
- **Cross-references**: layer-b-engineering-universal, vocabulary-discipline, p7-recursive-learning-operational, ci-cost-economy

## Compliance and governance

### compliance-mapping
- **Scope**: Mappings of SliceOps Layer A/B to compliance frameworks (ISO 42001, SOC 2, EU AI Act, NIST AI RMF).
- **Parent**: foundational
- **Sub-topics**: iso-42001, soc-2, eu-ai-act, nist-ai-rmf, slsa, aibom
- **Cross-references**: ip-boundary, evidence-categories

### licensing
- **Scope**: License decisions — CC BY 4.0 (docs), MIT (code templates), vendor proprietary terms, trademark coexistence.
- **Parent**: ip-boundary
- **Cross-references**: ip-boundary, trademark

### trademark
- **Scope**: SliceOps™ trademark — registration, coexistence agreements, marketing usage guidelines.
- **Parent**: ip-boundary
- **Cross-references**: ip-boundary, licensing

## Positioning and competitive

### positioning
- **Scope**: SliceOps positioning vs competitors, wedge identification, marketing framing.
- **Parent**: (top-level)
- **Sub-topics**: wedge-a-audit-plane, wedge-b-multi-agent-parallelism, wedge-c-ai-readable-engineering, competitive-landscape
- **Cross-references**: trademark, licensing

### competitive-landscape
- **Scope**: Analysis of competitors and adjacent categories.
- **Parent**: positioning
- **Cross-references**: positioning

## Adopter-specific

### adopter
- **Scope**: Decisions about adopter-specific topics — multi-adopter ecosystem, retroactive adoption, born-on-SliceOps.
- **Parent**: ip-boundary
- **Sub-topics**: retroactive-adoption, born-on-sliceops (per-adopter sub-topics added as adopters publish)
- **Cross-references**: layer-c-adopter-stack

### brain-pack-injection
- **Scope**: The mechanism for injecting applicable Layer C.2 stack patterns at the start of each slice.
- **Parent**: layer-c-adopter-stack
- **Cross-references**: layer-c-adopter-stack, context-pack

---

## Slot extension

Adopters may extend this taxonomy with domain-specific topics in their own brain. Canonical SliceOps topics here are reserved — do not redefine semantics; only extend with sub-topics or add adopter-specific top-levels.

## Maintenance

- A DEC introducing a new topic must justify in its body why existing topics are insufficient and add the topic here (same slice).
- Quarterly Curation ritual — topic merging (over-granular consolidation), splitting (over-broad decomposition), and orphan archival.
- Fix-on-touch per P12.

Major restructure leads to a version bump.

## Likely future topics (scenarios)

| Scenario | Topic candidate |
|---|---|
| Compliance Pack maturity | `compliance-pack`, `iso-42001-mapping`, `soc-2-mapping`, `eu-ai-act-article-50-disclosure` |
| Domain vertical packs | `banking-vertical`, `healthcare-vertical`, `gov-vertical` |
| Certification program | `certification-tier`, `practitioner`, `architect` |
| Education / curriculum | `curriculum`, `onboarding-tier`, `tutorial` |
| Multi-org coordination | `cross-vault-references`, `org-boundary`, `consent-grant` |
| Conformance testing | `conformance-suite`, `compliance-test-vector` |

Hypothetical — added only when concrete DECs emerge.
