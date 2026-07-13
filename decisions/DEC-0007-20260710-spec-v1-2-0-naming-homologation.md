---
entity: DecisionRecord
status: approved
created: 2026-07-10
updated: 2026-07-10
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
originating_slice: null   # back-fill: cross-corpus naming ratification session, 2026-07-10
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DEC-0001-20260512-three-layer-ip-boundary, DEC-0002-20260514-spec-repo-publishing-layout, DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme]
topics: [vocabulary-discipline, entity-catalog, corpus-integrity, audit-plane]
vocabulary-changes: ["DEC-P-", "DEC-D-", "OUTC-", "SESS-", "Capability components", "Naming (canonical prefixes)", "RFC (retired term)"]
consistency-check: |
  Introduces spec v1.2.0 (SemVer minor): canonical naming (naming.md), lifecycle-in-prefix
  for DecisionRecord, flat decisions/ folders, OutcomeRecord kind:, Capability component
  model, and retirement of the "RFC" term and legacy prefixes. Entity names and catalog
  semantics from DEC-0001-20260512-three-layer-ip-boundary are preserved unchanged (the
  13-entity B.1 catalog does not grow). The v1.1.0 additions — evidence.v1
  (DEC-0006-20260702-evidence-v1-canonical-schema), the approver field
  (DEC-0005-20260702-author-approver-separation) and the measurement artifact
  (DEC-0004-20260630-build-complexity-measurement-model) — are carried forward unchanged;
  the evidence.v1 decisionRefs pattern is extended additively (DEC lifecycle ids accepted,
  legacy DR- read-tolerated). Amends one aspect of DEC-0002-20260514-spec-repo-publishing-layout:
  the decisions/ folder becomes flat (the 5-folder layout itself is untouched; amendment
  annotated there bidirectionally). v1.0.0 and v1.1.0 remain frozen; the alias tables in
  naming.md map old names to new. No other conflicts: licensing (DEC-0003) untouched
  except correcting the stale "no LICENSE published" line that predated its ratification.
---

# DEC-0007 — Spec v1.2.0: Total Naming Homologation

> **Amended by `DEC-0008-20260712-cognitive-cycle-and-universal-id-scheme`** before
> publication: the cut this record introduced was re-issued as **v2.0.0** (breaking scope
> added — catalog renames, required fields, universal identifier grammar). Its "v1.2.0"
> mentions read as that re-issued cut; v1.2.0 was never published.

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 Audit Plane, P1 Decision Integrity). This record publishes the decision; the cross-corpus ratification and inventory that motivated it (decision id `DEC-P-2026-07-10`, holding level) are maintained internally by the IP holder.

## Summary

One concept = one name = one prefix, in every layer and every store. Spec v1.2.0 makes naming **normative** (`spec/v2.0.0/naming.md`), carries the DecisionRecord lifecycle in the filename prefix (`DEC-` / `DEC-P-` / `DEC-D-`), flattens `decisions/` folders, retires the term "RFC" and the legacy prefixes (`DR-`, `IN-`, `IR-`, `OC-`, `BR-`, `SKILL-`, `RUN-`, `REF-`), and ships the enforcement so the standard **self-imposes** at the point of write.

## Context

A cross-corpus inventory (2026-07-10) of the maintainer's corpora implementing SliceOps found: four coexisting Insight schemes (`INS-`/`IN-`/`IR-`/none), `DR-` and `DEC-` simultaneously blessed by the glossary for the same entity (hundreds of artifacts affected across corpora), a `REF-` catch-all prefix hiding three distinct entities, and agent-context files missing the naming rules entirely. Root cause: the standard was **published but not enforced** — naming lived in docs one had to remember to read, with copies that drifted and no write-time gate. The framework's owner ratified total, retroactive homologation: *"I'm selling a standard — not being homologated is not an option."*

## Decision

1. **Canonical prefix per entity** (normative table in [`naming.md`](../spec/v2.0.0/naming.md)): `DEC-`(±`P`/`D`), `INS-`, `OUTC-`, `CAP-`, `GOAL-`, `LP-`, `CF-`, `CP-`, `AP-`, `REL-`, `PREF-`, `VAL-`, `SESS-`. ID schemes are local per store (`NNN` counter-based / `YYYY-MM-DD` date-based); prefix and entity name are global.
2. **DecisionRecord lifecycle in the prefix**: `DEC-P-` pending → `DEC-` approved → `DEC-D-` deprecated/superseded; `status: pending|approved|deprecated` must match; `decisions/` folders are **flat**; a state change renames the file and rewrites references atomically (R5). Legacy status values are read-tolerated, write-prohibited.
3. **The term "RFC" is retired**; a proposal is a pending DecisionRecord. The governance flow is renamed the **proposal process** (`governance/PROPOSAL-PROCESS.md`).
4. **Capability component model**: Capability is the capacity (the WHAT); `standard`/`runbook`/`playbook` are sibling **components** via `kind:` (+ `capability:` back-reference in component files). The catalog does not grow.
5. **OutcomeRecord `kind:`** is mandatory: `retrospective | postmortem | result`. Block Retrospectives are `kind: retrospective` (standalone `BR-` retired).
6. **Vendor implementation aliases** are documented (AgentContextPack→ContextPack, AgentSkill→Capability, GoalObjective→Goal, ValuePrinciple→Value, AgentPreference→Preference); the canonical name wins in portable form (P11). Runtime-proprietary entities stay outside the catalog per the existing vendor-extension mechanism.
7. **Enforcement ships with the norm** (published-not-enforced is the failure this closes): the toolkit **naming validator** runs as (a) an agent pre-write hook, (b) a CI merge gate — installed in this repo's `ci.yml` — and (c) a periodic sweeper for corpora without CI. Homologation is **retroactive** (existing artifacts renamed, references rewritten, alias maps emitted); `99-archive/` folders stay immutable, covered by alias maps.
8. **evidence.v1 compatibility**: the `decisionRefs` pattern is extended **additively** to accept the lifecycle-prefixed ids; legacy `DR-` date ids remain read-tolerated for pre-homologation archives. No breaking schema change.
9. **ip-boundary drift corrected**: the text still said no LICENSE was published; licensing was ratified 2026-06-15 and published — v1.2.0 states reality. No other licensing change.

## Alternatives considered

- **A — Forward-only homologation** (new artifacts homologated, old names grandfathered): rejected — two schemes coexisting indefinitely is the current confusion made permanent; references would mix old and new forever, and the standard's own corpora would not comply with the standard being sold.
- **B — Lifecycle in folders, prefix unchanged** (keep `accepted/`/`rfcs/`/`superseded/`): rejected — the state is invisible in references and filenames, folder moves break links silently, and folder state duplicates frontmatter state (two sources of truth for one fact, P12 violation).
- **C — Lifecycle in the prefix + flat folders + total retroactive rename with reference rewriting and alias maps**: **selected** — the state travels with every reference, one source of truth, and migration tooling makes the retroactive cost a one-time deterministic operation.

## Consequences

**Enables**: unambiguous cross-corpus references; write-time blocking of non-homologated names; adopters migrate with the published alias tables and validator. **Constrains**: no lifecycle subfolders; new spec versions must keep naming.md as the single normative source (no copies). **Costs**: one-time retroactive rename across existing corpora (executed with the migration tooling; per-corpus alias maps cover external links and archives).

## References

- [`spec/v2.0.0/naming.md`](../spec/v2.0.0/naming.md) — the normative naming standard this DEC introduces.
- [`spec/v2.0.0/glossary.md`](../spec/v2.0.0/glossary.md) — glossary v1.2.0 (aliases prohibited updated).
- [`governance/PROPOSAL-PROCESS.md`](../governance/PROPOSAL-PROCESS.md) — renamed proposal process.
- [`DEC-0001-20260512-three-layer-ip-boundary.md`](DEC-0001-20260512-three-layer-ip-boundary.md) — the B.1 catalog this homologation preserves.
- [`DEC-0002-20260514-spec-repo-publishing-layout.md`](DEC-0002-20260514-spec-repo-publishing-layout.md) — publishing layout (decisions/ flatten amendment).
- SliceOps toolkit `templates/naming-validator/` — the enforcement reference implementation.
