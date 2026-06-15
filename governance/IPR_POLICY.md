# Intellectual Property & Contribution Policy

> **Status: ratified 2026-06-15** (decision `DR-2026-06-15-sliceops-license-ratification`). The license terms below are binding. This repository is private pre-launch; it goes public on founder approval (P9 — human-in-the-loop authority).

## License

SliceOps is a documentation-first framework with mixed-scope content, licensed under two licenses by content type:

- **Documentation** — prose, spec, governance, decisions, examples, READMEs, R-rule narrative, entity-catalog and knowledge-category descriptions — is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. See [`../LICENSE`](../LICENSE).
- **Code** — templates, workflow YAMLs, JSON schemas, validator scripts, CI workflows, executable scripts — is licensed under the **MIT License**. See [`../LICENSE-CODE`](../LICENSE-CODE).

Code files carry an `SPDX-License-Identifier: MIT` header so per-file scope is unambiguous. When a file carries no SPDX header, scope resolves in this order: SPDX header → the folder's README → the disambiguation rule (code-shaped content, or any file under a templates/scripts/workflows path → MIT; prose/docs → CC BY 4.0; when in doubt → CC BY 4.0, since SliceOps is primarily a documentation framework).

**Copyright (c) 2026 Andrés Ramírez Sierra** — held personally, pre-incorporation of SliceOps LLC. When SliceOps LLC incorporates, copyright transitions via a separate IP assignment agreement.

## Trademark — separate from copyright

"SliceOps™" is a trademark of Andrés Ramírez Sierra (EUIPO filing #019381071, pending registration). **The CC BY 4.0 / MIT licenses do not transfer trademark rights.** Copyright governs use, copying, and redistribution of the content; the trademark governs use of the name "SliceOps™" in commerce and marketing. An adopter may use and redistribute SliceOps content under CC BY 4.0 / MIT (with attribution) and publish derivatives under their own name, but may not brand a derivative "SliceOps <anything>" or claim "SliceOps-compliant" without honoring the spec. Trademark usage guidelines (allowable claims, attribution, anti-misuse) are published separately in `TRADEMARK.md` (pending). See also [`../DISCLOSURE.md`](../DISCLOSURE.md).

## Contributions — Inbound = Outbound

Contributions are accepted under the **Inbound = Outbound** principle: by opening a pull request, a contributor licenses their contribution under the same license that governs the file being changed (CC BY 4.0 for documentation, MIT for code, per the file's SPDX header or the disambiguation rule above).

- **No Contributor License Agreement (CLA) is required for v1.** The Inbound = Outbound posture keeps contribution friction low.
- **Trademark is not included in the contribution license.** Contributing grants no rights in the "SliceOps™" mark, which remains personal IP governed by `TRADEMARK.md`.
- Changes to a principle, reference pattern, or canonical vocabulary follow the RFC process. See [`RFC-PROCESS.md`](RFC-PROCESS.md).

A CLA (DCO-style or Apache-style) may be re-evaluated if the contributor base grows past ~50 distinct individuals, a re-licensing need arises, or enterprise adopters require it for due diligence.

## SliceOps and reference runtimes

SliceOps is an open methodology. Vendor runtime implementations (including the first reference runtime) are architectural peers — none is "the official" runtime, and the methodology never requires a specific runtime (P8). See [`../DISCLOSURE.md`](../DISCLOSURE.md).

## References

- Decision record: `DR-2026-06-15-sliceops-license-ratification` — CC BY 4.0 + MIT, dual-file Option A mechanics, SPDX convention, Inbound = Outbound, TM/copyright separation.
- [`../LICENSE`](../LICENSE) — Creative Commons Attribution 4.0 International (documentation).
- [`../LICENSE-CODE`](../LICENSE-CODE) — MIT License (code).
- [`../DISCLOSURE.md`](../DISCLOSURE.md) — SliceOps / reference-runtime relationship and IP transparency.
- `TRADEMARK.md` — trademark usage policy (pending).
