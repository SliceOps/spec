# RFC Process

How a proposed change to the SliceOps™ framework becomes canonical.

## Flow

1. **Propose** — open an RFC as a draft DecisionRecord in `decisions/rfcs/` (`DR-YYYY-MM-DD-slug.md`, `status: proposed`).
2. **Frontmatter discipline (Layer 1)** — declare `conflicts-with`, `related-decs`, `topics`, `vocabulary-changes`, and a `consistency-check` paragraph stating how the proposal relates to the existing corpus.
3. **Pre-merge consistency checklist (Layer 2)** — search topic-related DECs, read the most-related ones end-to-end, declare conflicts and resolutions, update bidirectional cross-references, update glossary/topics if vocabulary changes.
4. **Deliberate** — discussion on the RFC. Alternatives considered must be explicit (no false-binary).
5. **Ratify or reject** — on ratification the DEC moves to `decisions/accepted/` (`status: ratified`); supersession of any prior DEC is explicit and bidirectional.
6. **Propagate** — downstream docs/templates updated fix-on-touch (P12); cross-vault references handed off, not edited directly.

## Principle amendments

Amending a Layer A principle requires superseding the canonical principles DEC explicitly, with a cross-reference impact analysis, under an elevated HITL gate (P3).

## Status

Skeleton. Refined as the contributor base grows.
