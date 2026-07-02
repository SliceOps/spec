# examples/ — Reference implementations and adopter onboarding

Concrete, copy-pasteable starting points for adopters.

## Day 1 SliceOps — the quickstart repository

**[github.com/SliceOps/quickstart](https://github.com/SliceOps/quickstart)** — a
minimal, clonable **template repository** that already runs on the framework
(spec v1.1.0): a ratified DEC with recorded `approver`, a slice tracker, a valid
`evidence.v1` record hash-anchored to its work commit, and CI running the
toolkit consistency validators (including schema validation of every evidence
record), the test suite, and a secrets scan. The README walks an engineer
through shipping their first slice — decision → code → evidence → merge — in
about 30 minutes, with the real gates failing the build on drift.

## Planned contents

| Document | Purpose |
|---|---|
| `reference-implementations.md` | Catalog of known SliceOps runtime implementations (vendor runtimes and adapters), their Layer B compliance level, and selection guidance. Implementations are architectural peers — none is "the official" runtime. |
| `adopter-customization-guide.md` | What adopters may customize (rename folders, extend the entity catalog, add vertical packs) while staying SliceOps-compliant, and what they may not (remove canonical entities, conflict canonical semantics). |

## Status

The Day-1 onramp is live (the quickstart repository above — it supersedes the
`onboarding-day-1.md` document planned here). The two catalog documents remain
planned. For corpus-only adoption (no new repo), the toolkit README's
["Use it"](https://github.com/SliceOps/toolkit#use-it) section is the shortest
path.

## Note

Examples must be vendor-neutral and platform-agnostic (P11). Tutorial content that assumes a specific platform's features does not belong here.
