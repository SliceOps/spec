# Proposal Process

How a proposed change to the SliceOps™ framework becomes canonical.

> Formerly the "RFC process". The term **"RFC" is retired** from the SliceOps vocabulary (v1.2.0 naming homologation): a proposal IS a **pending DecisionRecord** (`DEC-P-`, `status: pending`) — the lifecycle lives in the prefix, not in a folder or a separate artifact type. See `../spec/v2.0.0/naming.md`.

## Flow

1. **Propose** — open a pending DecisionRecord in the flat `decisions/` folder: `DEC-P-YYYY-MM-DD-slug.md`, `status: pending`.
2. **Frontmatter discipline (Layer 1)** — declare `conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, and a `consistency-check` paragraph stating how the proposal relates to the existing corpus.
3. **Pre-merge consistency checklist (Layer 2)** — search topic-related DECs, read the most-related ones end-to-end, declare conflicts and resolutions, update bidirectional cross-references, update glossary/topics if vocabulary changes.
4. **Deliberate** — discussion on the pending record. Alternatives considered must be explicit (no false-binary).
5. **Approve or reject** — on approval the record is **renamed** `DEC-P-…` → `DEC-…`, `status: approved`, and the `approver:` field records the approving human (P3); all references to the old id are rewritten in the same atomic change (R5); supersession of any prior DEC is explicit and bidirectional (the superseded record becomes `DEC-D-…`, `status: deprecated`, `superseded-by:` set).
6. **Propagate** — downstream docs/templates updated fix-on-touch (P12); cross-vault references handed off, not edited directly.

## Principle amendments

Amending a Layer A principle requires superseding the canonical principles DEC explicitly, with a cross-reference impact analysis, under an elevated HITL gate (P3).

## Status

Skeleton. Refined as the contributor base grows.
