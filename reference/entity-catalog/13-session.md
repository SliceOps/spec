# Session — Layer B.1 Cognitive Entity

> The unit of human–AI interaction (one conversation/chat with an AI agent). **Mapped principles: P2 (Audit Plane), P4 (Decision Integrity — generalized: decisions emerge from sessions), P5 (provenance evidence category).**

## Purpose

Every human–AI interaction is a **Session** — an identifiable, auditable, classifiable unit. SliceOps gives the interaction a name so the audit plane (P2) covers ALL of it, not only the development subset. The **Slice is the DEV Session-Type** (the one that produces a PR); other Session-Types (Meta, Audit, Learning, Support, Infra, Artifact, Orchestrate) are valid AI interactions that do not produce a PR. *Every slice is a session; not every session is a slice.*

P4 generalizes accordingly: **decisions emerge from sessions** (not only slices) — Meta/Audit/Learning sessions also produce decisions with provenance. The originating-session field on every DecisionRecord closes the audit-plane hole for governance decisions.

## Frontmatter schema

```yaml
entity: Session
session_id: <stable id, e.g. the platform's chat/session identifier>
session_type: Slice | Artifact | Support | Infra | Meta | Audit | Learning | Orchestrate
slice_type: Dev | Refactor | Fix | ...    # only when session_type == Slice; adopters add C.2 sub-types
workspace: <canonical cwd / project / repo root>
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: public | internal | restricted | sensitive

# Volume / cost (links P12 and cost-ledger)
turns: <int>
token_band: XS | S | M | L | XL          # billed-equivalent throughput band (see ../sizing/)
context_band: XS | S | M | L | XL         # peak context footprint band — model-viability filter
cost_estimate: <tokens or currency, optional>

# Model triage (see ../model-triage/) — what was chosen and why
model_used: <model identifier>
execution_mode: frontier-API | local-via-API | account-with-plan | local-in-IDE
triage_rationale: <one-line: which axis decided it (context-band? sensitivity? cost?)>

# Routing direction (extends model triage)
context_orientation: consuming | producing | mixed

# Orthogonal axes (NOT session_type — these cross-cut)
lifecycle: active | archive | delete
dimensions: [security, compliance, ...]   # optional cross-cutting dimensions

# Closure / provenance
outcome: <PR ref if Slice | DEC ids if Meta | INS if Learning/Audit | summary line otherwise>
provenance:
  human: <accountable party>
  agents: [<agent identifier>...]
  started: YYYY-MM-DDTHH:MM
  ended: YYYY-MM-DDTHH:MM | null
```

## Lifecycle states

`active` → (`archive` | `delete`). `archive` retains the session for audit; `delete` removes per data-retention policy. **Sessions are append-only during `active`** — a turn is added, never overwritten. Closure is recorded by setting `outcome` and `provenance.ended`. Re-opening an archived session for follow-up creates a new related session (with `related-sessions` cross-ref), not a mutation.

> `lifecycle` is the **orthogonal axis A** — NOT a Session-Type. A "Delete" disposition is not a kind of session; it is the state of one.

## Usage example (generic)

```
session-2026-XX-XX-<short-slug>.md   (or the platform's id as filename)
  entity: Session
  session_type: Meta
  workspace: <project root>
  turns: 47
  token_band: M
  context_band: L
  model_used: <frontier-class>
  execution_mode: account-with-plan
  triage_rationale: large context-band drove model choice
  context_orientation: producing
  lifecycle: active
  outcome: ratified DR-YYYY-MM-DD-<slug-1>, DR-YYYY-MM-DD-<slug-2>
Body: scope · turns summary · decisions produced · evidence references.
```

## Cross-reference patterns

- **Produces** → DecisionRecord(s) (`originating_session`), InsightRecord(s), OutcomeRecord(s), or Capability accruals (Learning sessions).
- **Sized by** → token-band and context-band (see `../sizing/`).
- **Routed by** → Model Triage (see `../model-triage/`) — `model_used`, `execution_mode`, and `triage_rationale` are auditable choices, not opaque defaults.
- **Related to** → other sessions via `related-sessions` (follow-ups, orchestration parents).
- **Coordinated by** → an `Orchestrate` Session-Type (renamed from the abbreviated "COORD"; full word per the naming convention).

## Anti-patterns

- Confusing `lifecycle` (orthogonal axis) with `session_type` (categorical) — "Delete" is not a Session-Type.
- Confusing a `dimensions` cross-cutting axis (Security/Compliance) with a Session-Type — Security is not a kind of session; it cross-cuts.
- Using **COORD** instead of **Orchestrate** (naming convention violates P10 — full words, not opaque abbreviations).
- Treating non-DEV sessions as second-class because they produce no PR (Meta/Audit/Learning are valid audit-plane sessions with provenance; P4 generalized).
- Editing a closed session instead of opening a related one (violates append-only / audit-trail integrity).
- A Session with no `provenance.human` — unaccountable AI work (violates P9).
- Forcing a Support or Infra interaction into a slice-shaped PR-required mold (the framework absorbs them natively as Session-Types — see the Session-Type taxonomy in `../sessions/`).
