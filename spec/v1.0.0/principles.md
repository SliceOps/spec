# SliceOps™ Canonical Principles (Capa A) — v1.0.0

SliceOps™ as a framework is constituted by **12 canonical principles (Capa A)**. Without any one of them, the result **is not SliceOps**. Each principle is defined with a statement, rationale, implication, and anti-pattern.

These principles are **non-negotiable**: an implementation that violates any one is not SliceOps-compliant. Amendments to this set require a superseding decision under an elevated human-in-the-loop gate (P9).

Gamification (slice-count badges, streaks, leaderboards, motivation mechanics) is explicitly **out of scope** — the asymmetric risk via Goodhart's law + cobra effect + quality erosion outweighs the benefit. SliceOps takes no position on gamification at any layer.

---

## P1 — Slice Atomicity

**Statement**: One chat = one PR = one atomic vertical slice. A slice carries one outcome end-to-end: spec, decision, code, tests, evidence, merge.

**Rationale**: Atomic units of work are a prerequisite for parallelization, audit, and recursive learning (P7). Without atomicity, scope drifts, decisions smear across multiple PRs, evidence fragments, post-hoc reconstruction is impossible. AI agents specifically benefit from bounded scope: a chat session has finite context window, finite attention budget, finite reasoning depth. Atomicity matches the capability envelope of the agent.

**Implication**:
- Slices declare scope upfront (spec block in PR description or DEC)
- Token-band sizing recommended (XS/S/M/L/XL Tk) tied to the capability envelope
- DAG dependencies explicit (`depends_on`)
- Branch naming aligned with slice ID
- Slice ID is the provenance carrier in every artifact produced
- A slice does NOT span multiple architectural concerns; if it must → split

**Anti-pattern**:
- Catch-all PRs ("misc fixes")
- Slices that grow >2× forecast without a retrospective
- Slices touching unrelated concerns (DI + business logic + DB migration + UI)
- Slices without explicit scope declaration

---

## P2 — Audit Plane Discipline

**Statement**: Every architectural decision is recorded, traceable, and cross-slice consistent. The audit plane is the layer above code where decisions live as first-class artifacts.

**Rationale**: Code-quality tools audit code. Runtime tools audit behavior. Compliance tools audit post-hoc. **No existing tool audits the decision plane** — what was decided, by whom (human/agent), why, when, with which alternatives considered, with what supersession chain. This layer **is** the SliceOps wedge. Without P2, SliceOps is just another collection of CI rules.

**Implication**:
- DecisionRecord schema mandatory (Capa B catalog)
- DECs date-based or counter-based, with a uniqueness check enforced in CI
- DEC content: context, alternatives considered, rationale, consequences, supersession chain
- Cross-slice DEC consistency check enforced in CI
- Counter discipline pattern (atomic increment per prefix, validate-no-duplicate)
- DECs append-only; supersession explicit, never silent

**Anti-pattern**:
- Decisions in chat/email/meetings without a subsequent DEC
- DECs created post-hoc to justify already-merged code
- DECs contradicting prior DECs without explicit supersession
- DECs without alternatives considered (false-binary thinking)

---

## P3 — Stage as DAG-Derived View

**Statement**: A Stage is a computed view of the slice dependency graph, **not** an imperative time-bound grouping. Slices belong to Blocks (logical scope) and depend on each other; Stage = "what is mergeable now given dependencies."

**Rationale**: Sprint-based models assume fixed cadence + predicted velocity + commitment per sprint. AI-first SDLC has variable velocity per slice (size unknown until decomposed), opportunistic parallelism (depends on DAG topology), and emerging dependencies (discovered during slice execution). Stage-as-DAG-view aligns the planning model to reality: Stage N includes whatever slices are unblocked at time N. This is the most novel SliceOps concept relative to existing SDLC frameworks.

**Implication**:
- DAG explicit in slice metadata (`depends_on`)
- Stage computed by graph traversal, not assigned imperatively
- Forecasting at Block level (which Block costs M tokens), not Stage level
- Retrospectives close a Block, not a Sprint
- Velocity calibrated post-hoc per Block, applied forward as an adjustment

**Anti-pattern**:
- Sprint-based commitment with fixed scope
- Slices assigned to "Sprint 1" / "Sprint 2" without DAG analysis
- Burndown charts (Sprint artifact, not Block artifact)
- "We committed to N slices this stage" — Stage is derived, not committed

---

## P4 — Decision Integrity by Construction

**Statement**: Decisions emerge from slices. Every DEC traces to a slice (where it was produced) and is reachable from that slice (back-link). Decisions made out-of-band must be backed into a slice retroactively.

**Rationale**: Out-of-band decisions accumulate as tribal knowledge — chat DMs, the founder's head. Six months later nobody knows why X. SliceOps eliminates tribal knowledge by requiring every decision to live in the corpus tied to the slice that produced it. The slice is the unit of work AND the unit of provenance. Without P4 → tribal knowledge re-emerges → the audit plane is theater.

**Implication**:
- DEC frontmatter includes slice provenance (`originating_slice:` in the canonical Block-Section-Slice ID format)
- Slice PRs include the DEC list produced
- Retroactive DECs allowed but require a "back-fill slice" with an explicit retro-decision flag
- Architecture-spanning decisions get their own slice (no decision is "free" of slice provenance)

**Anti-pattern**:
- DECs created without slice context
- "We decided this in a meeting" — re-record as a slice
- Decisions in a chat backlog never committed to the corpus
- DECs that supersede priors without explaining what changed in context

---

## P5 — Evidence-by-Construction

**Statement**: Every slice produces evidence in **4 mandatory categories**: functional (tests pass), quality (linters/metrics), decision (DECs + InsightRecords), provenance (slice ID, agent, timestamps, commit SHA). Evidence is non-negotiable; un-evidenced slices do not merge.

**Rationale**: Compliance frameworks (ISO 42001, SOC 2, EU AI Act) treat evidence as a periodic burden — collect quarterly, audit annually. SliceOps treats evidence as a per-slice byproduct: if you finished the slice, you have the evidence. Audit becomes trivial: select a date range, filter slices, evidence is present by construction. AI-generated code specifically requires robust evidence because its failure modes are subtle (hallucinated APIs, invalid schemas, drift between runs).

**Implication**:
- Each tech stack defines its test taxonomy (unit/integration/regression/e2e as relevant)
- Hard CI gates: test pass, coverage threshold, lint pass, format check
- AI-specific evidence: hallucination tests (outputs don't invent APIs/imports/types), drift tests (same input → same output), eval suites for agentic outputs
- Provenance metadata mandatory: slice ID, originating chat, agent attribution, commit SHA, timestamps
- Coverage threshold per slice (not just project-wide average)

**Anti-pattern**:
- Tests added in a "follow-up slice" → block merge or fix retroactively
- Coverage skipped for a "small slice" — all slices evidenced regardless of size
- Manual QA only → not evidenced; testing must be CI-enforced
- "We'll add tests later" — never happens; merge with tests or don't merge

---

## P6 — Security-by-Construction

**Statement**: Security is a per-slice gate, not a periodic audit. Every slice passes security validation before merge: SAST, secrets scan, dependency vulnerability check, SBOM update, supply-chain provenance attestation.

**Rationale**: AI-generated code introduces specific vectors that traditional security gates miss: (a) hallucinated dependencies → typosquat attacks via packages the model invents; (b) prompt injection in outputs surfaced to other agents; (c) secrets leakage in agent-generated logs/DECs; (d) supply chain via inflated context windows. Compliance requires a security baseline. Without P6, the compliance wedge is theater and adopters face real attack vectors invisible to status-quo gates.

**Implication**:
- Hard CI gates per slice: SAST, secrets scan, dependency vulnerabilities
- SBOM generated per slice, accumulated at Block level
- Supply-chain provenance attestation for every merged artifact
- AI-specific gates: hallucinated-dependency check (imports vs known-good registry), prompt-injection regression suite, output schema validation
- Secrets policy: never in DECs, InsightRecords, slices, branches, commit messages — enforced by scanning

**Anti-pattern**:
- Quarterly security review without per-slice gates
- Security as "the security team's job" — security is a per-slice concern
- Trusting AI-generated dependency manifests without validation
- Secrets in committed env files (any LLM "helpfully" attempts this)

---

## P7 — Recursive Learning by Capture

**Statement**: The framework improves itself through capture. Every slice produces InsightRecords (empirical observations); patterns appearing ≥3 times become LearningPatterns; LearningPatterns inform R-rule amendments via DECs; R-rule amendments apply forward to subsequent slices. **The corpus is the training data.**

**Rationale**: ADRs are static — decided once, recorded, archived. Static methodologies have no first-class learning loop. Black-box trajectory replay learns for the vendor, not the adopter. SliceOps is recursive: adopters' own corpora improve their own frameworks. InsightRecords → LearningPatterns → R-rules → DECs → updated corpus. This is probably the principle **most differentiated** from existing approaches.

**Granularity clarification** (does not change the statement): the ≥3 threshold applies to **LearningPattern promotion** (framework-level, deliberate). A complementary finer granularity exists — **artifact-level tuning**: whenever an artifact (reference file / script / template / skill) does not behave as expected, ask "one-off adjustment or permanent?"; if permanent → update the artifact immediately (do not wait for ≥3).

**Implication**:
- InsightRecord schema (Capa B catalog) captures cross-slice empirical observations
- LearningPattern schema captures recurring patterns (threshold ≥3 observations)
- R-rule amendments require DECs referencing LearningPatterns as evidence
- Block Retrospective mandatory sections: "forward forecast adjustments" + "captured insights"
- Postmortem schema for negative outcomes (blameless)
- Public corpora compound: adopters publishing InsightRecords contribute to ecosystem-wide learning

**Anti-pattern**:
- Retrospectives that produce no InsightRecords
- InsightRecords that sit unused (must feed back to R-rules or DECs)
- R-rules amended without LearningPattern evidence
- Postmortems that name names instead of patterns (blameless-culture violation)

---

## P8 — Platform-Agnostic

**Statement**: SliceOps runs on any text-based AI agent + git + atomic-slice scoping + file-producing capability. Specific platforms add velocity and UX but are NOT a gate of entry. SliceOps is not locked to any vendor.

**Rationale**: Vendor lock-in kills adoption. Frameworks tied to a single tool limit ecosystem growth. The SliceOps wedge **is** the methodology, which must run anywhere. Specific platforms unlock additional capability (multi-chat unlocks the parallelism wedge, knowledge-graph integration unlocks substrate features) but adopters get base value (Audit Plane, Decision Integrity) with no specific tool.

**Implication**:
- **Mode S** (single-agent, sequential) and **Mode M** (multi-agent, parallel) — both produce full audit-plane evidence
- Mode M unlocks Wedge B (parallelism); Mode S unlocks Wedge A (audit) without Wedge B
- Minimum declared prerequisites: text-based AI agent, git, file system, atomic-slice scoping capability
- Capability matrix per platform (Capa B pattern): which platforms unlock which features
- **A reference runtime is one runtime, not the runtime.** Substrate options (third-party tool adapters, custom homegrown brains) are valid and are architectural peers

**Anti-pattern**:
- Claiming SliceOps requires a specific AI coding tool
- Documentation assuming specific platform features (e.g., "open a chat" assuming multi-chat exists)
- Tooling that only works with specific platforms
- License terms requiring a specific runtime

---

## P9 — Human-in-the-Loop Authority

**Statement**: Humans retain final authority over scope, merges, and architectural direction. AI agents propose; humans dispose. Critical decisions (Block-scope DECs, R-rule amendments, repo-level changes) require a human approval gate. Routine slices may auto-approve based on policy + evidence, but an escape hatch to a human always exists.

**Rationale**: AI agents make confident-sounding wrong decisions. Without HITL, errors compound into the corpus → poisoned training data → future agents inherit the poison (P7 backfires without HITL). Regulatory: EU AI Act Article 14 mandates human oversight for high-risk systems. Reputational: AI-only orgs lose trust fast. SliceOps explicitly preserves human authority while maximizing AI leverage.

**Implication**:
- Merge gate is human approval (CODEOWNERS or equivalent)
- Critical DECs require explicit human ratification (≠ auto-merged)
- Block-scope decisions (what enters/exits) are human authority
- R-rule amendments require human DEC ratification
- AI-generated content disclosed (EU AI Act Art. 50): content, code, decisions
- Provenance metadata distinguishes human-authored vs agent-authored

**Anti-pattern**:
- Auto-merge on green CI without human review in critical scope
- AI agents amending R-rules without a human DEC
- AI agents closing Blocks without a retrospective
- Hidden AI-generated content (no provenance, no disclosure)
- "Agentic auto-merge" for L or XL slices (size disproportionate to human-review risk)

---

## P10 — Vocabulary Discipline

**Statement**: Canonical terms have canonical meanings. Synonyms drift; SliceOps does not. **Vocabulary is canon, not preference.** Drift detected on touch is fixed forward.

**Rationale**: Without vocabulary discipline, the corpus becomes junk. Adopters with N words for "slice" cannot interoperate. A cross-org ecosystem becomes impossible. SliceOps adopters speaking the same language **is** the ecosystem-compounding effect. Vocabulary drift is silent corruption of the audit plane (P2) — auditing decisions requires consistent term semantics.

**Implication**:
- Canonical glossary at `spec/v1.0.0/glossary.md`
- DEC required to add/rename/retire a canonical term
- "Fix on touch" — any slice that detects drift updates content forward
- Adopters may extend with domain-specific vocabulary, but SliceOps core terms are reserved
- Linters enforce vocabulary (Capa B pattern: term-linter)

**Anti-pattern**:
- "Slice" + "story" + "ticket" used interchangeably
- "DEC" + "ADR" + "decision doc" treated as synonyms
- New terms invented without a DEC
- Marketing content using non-canonical terms (drift entry vector)

---

## P11 — Infrastructure Continuity

**Statement**: Code, infrastructure-as-code, database schemas, and environment configuration form one continuum. SliceOps discipline applies uniformly across them: atomic slice, DEC trail, evidence-by-construction, security gates, HITL authority. Infrastructure is not a separate domain.

**Rationale**: Many SDLC frameworks bifurcate code vs infrastructure (a separate ops workflow, separate review, separate tooling). AI-first SDLC **cannot bifurcate** — AI agents can and will modify Terraform, Pulumi, CloudFormation, k8s manifests, DB migrations, env configs. Without P11, infrastructure becomes a "shadow domain" where AI changes happen without slice discipline → audit-plane gaps → security gaps → compliance gaps. SOC 2 + ISO 27001 + banking-grade compliance require infrastructure change tracking equivalent to code. DB migrations are particularly risky (complex rollback, data-loss potential) — AI generating them without a DEC trail + rollback plan + evidence is a critical failure vector for regulated ventures.

**Implication**:
- IaC changes are slices with the same atomicity and DEC trail
- DB migrations are slices with a mandatory rollback plan in the spec
- Environment-specific configs versioned; differences declared in a DEC
- Infrastructure DECs (cloud provider, DB type, region, runtime topology) follow P2/P4 like any other DEC
- Multi-environment testing for deploy slices (dev → staging → prod evidence chain)
- Secrets/credentials handled per environment with P6 discipline
- AI-generated IaC requires a human review gate per P9

**Anti-pattern**:
- "Ops team handles infra" — separate workflow from slice discipline
- DB migrations without a DEC + without a rollback plan
- Production hotfixes without slice provenance
- Cross-environment config drift unreviewed
- AI-generated IaC merged without human review (also violates P9)
- Database schema changes that are not slices
- Infrastructure as a "shadow domain" outside the audit plane

---

## P12 — Shared-Resource Pre-flight

**Statement**: Before scaling any parallelism lever beyond the baseline calibrated in the last Block Retrospective, enumerate + cap + alert + telemeter every finite/serialized shared resource that lever consumes. SliceOps's parallel throughput stresses shared resources the methodology must protect **proactively** — protection is bootstrap, not reaction.

**Rationale**: Multi-agent parallelism is **constitutive** of SliceOps (Wedge B) — no other SDLC runs 5–13 simultaneous agents as its normal mode. So this failure mode (parallelism stresses an un-enumerated finite/serialized shared resource) is **more intrinsic to SliceOps than to any existing framework**. Operating theorem: *"the success of a parallelism lever is the source of the next bottleneck."* Observed in reference-implementation practice ≥3 times (serialized-counter contention, shared worktree/checkout state, CI-minute exhaustion — same family as API rate limits, branch-protection serialization, DB migration locks). Without systematic pre-flight, the primary wedge silently self-destructs (invisible hard-stop).

**Implication**:
- Pre-Block checklist: enumerate finite/serialized shared resources the Block consumes (CI minutes, counters, API rate limits, branch-protection serialization, DB migration locks, worktree/checkout state, connection pools)
- Each resource: **cap** (hard limit) + **alert** (warns BEFORE the limit, not at it) + **telemetry** (continuous visibility)
- Trigger: crossing the baseline calibrated in the last Block Retrospective (tied to P3 + velocity recalibration — NOT a fixed magic number)
- Default for any shared resource = cap+alert, **never silent hard-stop** ("warned degradation" > "invisible hard-cut")
- Cost-ledger extended to an infra/CI dimension (not just tokens) — Capa B.1
- Guardrails as repo-scaffold bootstrap defaults, NOT post-incident retrofit

**Anti-pattern**:
- A `$0` spending limit / default quota that turns "exhaust resource" into "invisible hard-cut"
- A cost-ledger that tracks only tokens (infra-cost blindness)
- Scaling parallelism without enumerating the shared resources it consumes
- Guardrails patched post-incident instead of bootstrap defaults
- Treating CI minutes / counters / rate limits / locks as infinite
- Docs/orchestration PRs burning the same finite budget as heavy code PRs without change-gating

**Why P12 ≠ P11**: P11 (Infrastructure Continuity) = "infra changes are slices (atomicity applied to infra)." P12 = "before scaling parallelism, protect the finite shared resources it consumes." An adopter can honor P11 perfectly (migrations as slices) and still exhaust CI minutes by never enumerating that resource. Orthogonal.

---

## Amendment policy

This set evolves only via a superseding DEC under an elevated HITL gate (P9), with explicit cross-reference impact analysis. The derivation history of these principles is itself corpus produced by the framework operating on itself (P4 + P7) — a recursive demonstration, at a cadence of roughly one principle per intensive operating period, which is a maturity signal, not instability.
