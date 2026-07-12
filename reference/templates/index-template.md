<!--
Corpus index template (_index.md — reserved-name infrastructure, DEC-0010).
NOT an entity: no entity frontmatter, no counter, always this exact filename
at the corpus root. It POINTS, never copies; the validator enforces that it
exists and that every route resolves. Loading chain: agent-context file →
_index.md → exact files or ContextPacks. Replace all <…>.
-->

# _index — <corpus name>

> Load this first. Routes say WHERE to look — open only what the route names.

## Routes

| If you need… | Open |
|---|---|
| <decisions about X> | `<path/DEC-…>` |
| <the current goals / priorities> | `<path/goals/>` · `<path/priorities/>` |
| <how we do Y (capability)> | `<path/CAP-…>` |
| <session handoffs in flight> | `<path/CP-…>` |
| <operating rules for agents> | `CLAUDE.md` / `AGENTS.md` |

## Sub-indexes (large corpora)

| Area | Index |
|---|---|
| <brain/> | `<brain/_index.md>` |
| <knowledge/> | `<knowledge/_index.md>` |

## Maintenance

Structural changes update this file in the same change (a broken route is a
build failure, not a suggestion). Point, never copy.
