---
entity: DecisionRecord
status: ratified
created: 2026-06-15
updated: 2026-06-22
owner: Andrés Ramírez Sierra
sensitivity: public
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DR-2026-05-12-three-layer-ip-boundary]
topics: [licensing, ip-boundary, trademark]
vocabulary-changes: []
consistency-check: "Ratifies the dual license (CC BY 4.0 for documentation + MIT for code) that operationalizes the IP boundary in DR-2026-05-12-three-layer-ip-boundary; the trademark is handled separately in TRADEMARK.md; contributions follow Inbound = Outbound with DCO sign-off. No conflicts."
---

# DR-2026-06-15 — SliceOps License

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 Audit Plane, P1 Decision Integrity). This record publishes the **decision**. The supporting work (context, market comparison, alternatives, and consequences) was carried out and is maintained internally.

## Decision

SliceOps documentation is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. SliceOps code is licensed under the **MIT License**.

**Mechanism.** A repository with mixed content carries a root `LICENSE` (CC BY 4.0, governing documentation), a `LICENSE-CODE` (MIT, governing code), a README "License" section, and an `SPDX-License-Identifier: MIT` header on each code file. A code-only repository carries a single MIT `LICENSE`, with SPDX headers retained so that individually reused files stay unambiguous.

**Per-file scope.** Where a file carries no SPDX header, scope resolves in order: the SPDX header, then the folder's README, then the rule — code-shaped content, or any file under a templates, scripts, or workflows path, is MIT; prose and documentation are CC BY 4.0; in doubt, CC BY 4.0.

SPDX header by file type:

| File type | Header |
|---|---|
| YAML / YML | `# SPDX-License-Identifier: MIT` (first line) |
| Python / Shell | `# SPDX-License-Identifier: MIT` (after the shebang) |
| JS / TS / Rust / Go | `// SPDX-License-Identifier: MIT` (first line) |
| Markdown / text | not required — CC BY 4.0 governs prose |

**Copyright.** `Copyright (c) 2026 Andrés Ramírez Sierra`, held personally, pre-incorporation of SliceOps LLC. On incorporation, copyright transitions through a separate IP assignment agreement.

**Contributions.** Contributions follow Inbound = Outbound: a contribution is licensed under the same license as the file it changes. Contributors certify the Developer Certificate of Origin 1.1 ([`DCO`](../../DCO)) by signing off each commit. No Contributor License Agreement is required for v1.

**Trademark.** The copyright licenses do not grant any right to the "SliceOps™" trademark, which is governed separately by [`TRADEMARK.md`](../../TRADEMARK.md). Receiving or contributing content conveys no trademark rights.

## Alternatives considered

- **A — A single permissive license for everything (e.g. MIT or Apache-2.0 across docs and code)**: rejected — a code license is a poor fit for prose; CC BY 4.0 is the recognized standard for documentation and makes the attribution expectation explicit.
- **B — A copyleft / share-alike documentation license (CC BY-SA) or public domain (CC0)**: rejected — BY-SA's viral terms deter commercial adoption and downstream reuse; CC0 abandons the attribution that sustains the framework's provenance and trademark story.
- **C — Dual CC BY 4.0 (docs) + MIT (code), resolved per file by SPDX/README/path**: **selected** — each artifact type gets the right instrument, reuse stays unambiguous, and the boundary aligns with DR-2026-05-12-three-layer-ip-boundary.

## References

- [`TRADEMARK.md`](../../TRADEMARK.md) — trademark usage policy.
- [`DISCLOSURE.md`](../../DISCLOSURE.md) — framework and reference-runtime relationship.
- [`governance/IPR_POLICY.md`](../../governance/IPR_POLICY.md) — intellectual-property and contribution policy.
- [`DR-2026-05-12-three-layer-ip-boundary.md`](DR-2026-05-12-three-layer-ip-boundary.md) — the IP boundary this license operationalizes.
- [`LICENSE`](../../LICENSE) — Creative Commons Attribution 4.0 International. [`LICENSE-CODE`](../../LICENSE-CODE) — MIT License. [`DCO`](../../DCO) — Developer Certificate of Origin 1.1.
