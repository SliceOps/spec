# Intellectual Property & Contribution Policy

> **Status: ratified 2026-06-15** (decision `DR-2026-06-15-sliceops-license-ratification`). The license terms below are binding. This repository is private pre-launch; it goes public on founder approval (P3 — human-in-the-loop authority).

This is the **authoritative** policy for licensing, trademark, and contributions. [`../CONTRIBUTING.md`](../CONTRIBUTING.md) is the practical how-to and defers here for the binding terms.

## License

SliceOps is a documentation-first framework with mixed-scope content, licensed under two licenses by content type:

- **Documentation** — prose, spec, governance, decisions, examples, READMEs, R-rule narrative, entity-catalog and knowledge-category descriptions — is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. See [`../LICENSE`](../LICENSE).
- **Code** — templates, workflow YAMLs, JSON schemas, validator scripts, CI workflows, executable scripts — is licensed under the **MIT License**. See [`../LICENSE-CODE`](../LICENSE-CODE).

Code files carry an `SPDX-License-Identifier: MIT` header so per-file scope is unambiguous. When a file carries no SPDX header, scope resolves in this order: first the SPDX header, then the folder's README, then the disambiguation rule (code-shaped content, or any file under a templates, scripts, or workflows path, is MIT; prose and docs are CC BY 4.0; when in doubt, CC BY 4.0, since SliceOps is primarily a documentation framework).

**Copyright (c) 2026 Andrés Ramírez Sierra** — held personally, pre-incorporation of SliceOps LLC. When SliceOps LLC incorporates, copyright transitions via a separate IP assignment agreement.

## Attribution

Attribution is **required**, not optional, whenever you redistribute or adapt the content. CC BY 4.0 requires crediting "SliceOps" as the source, linking to the license, and indicating any changes you made; MIT requires preserving the copyright and license notice. Beyond the legal minimum, crediting SliceOps when you build on it is expected and welcomed — it is how the framework stays discoverable and correctly attributed to its author.

## Trademark — separate from copyright

"SliceOps™" is a trademark of Andrés Ramírez Sierra (EUIPO filing #019381071, pending registration). **The CC BY 4.0 / MIT licenses do not transfer trademark rights.** Copyright governs use, copying, and redistribution of the content; the trademark governs use of the name "SliceOps™" in commerce and marketing. An adopter may use and redistribute SliceOps content under CC BY 4.0 / MIT (with attribution) and publish derivatives under their own name, but may not brand a derivative "SliceOps &lt;anything&gt;" or claim "SliceOps-compliant" without honoring the spec. Trademark usage guidelines (allowable claims, attribution, anti-misuse) are published separately in [`../TRADEMARK.md`](../TRADEMARK.md). See also [`../DISCLOSURE.md`](../DISCLOSURE.md).

## Contributions — Inbound = Outbound, certified by the DCO

Contributions are accepted under the **Inbound = Outbound** principle: by opening a pull request, a contributor licenses their contribution under the same license that governs the file being changed (CC BY 4.0 for documentation, MIT for code, per the file's SPDX header or the disambiguation rule above).

Contributors additionally certify the **Developer Certificate of Origin 1.1** ([`../DCO`](../DCO)) by signing off each commit (`git commit -s`). The DCO is a lightweight attestation that the contributor has the right to submit the work; it is **not** a copyright assignment.

- **No Contributor License Agreement (CLA) is required for v1.** The Inbound = Outbound license plus DCO sign-off keeps contribution friction low while preserving provenance of every change.
- **Trademark is not included in the contribution license.** Contributing grants no rights in the "SliceOps™" mark, which remains personal IP governed by [`../TRADEMARK.md`](../TRADEMARK.md).
- Changes to a principle, reference pattern, or canonical vocabulary follow the RFC process. See [`RFC-PROCESS.md`](RFC-PROCESS.md).

A formal CLA may still be re-evaluated if the contributor base grows past roughly 50 distinct individuals, a re-licensing need arises, or enterprise adopters require it for due diligence.

## SliceOps and reference runtimes

SliceOps is an open framework. Vendor runtime implementations (including the first reference runtime) are architectural peers — none is "the official" runtime, and the framework never requires a specific runtime (P11). See [`../DISCLOSURE.md`](../DISCLOSURE.md).

## References

- Decision record: `DR-2026-06-15-sliceops-license-ratification` — the ratified SliceOps license decision: CC BY 4.0 for documentation, MIT for code, SPDX convention, Inbound = Outbound, trademark and copyright separation.
- [`../LICENSE`](../LICENSE) — Creative Commons Attribution 4.0 International (documentation).
- [`../LICENSE-CODE`](../LICENSE-CODE) — MIT License (code).
- [`../DCO`](../DCO) — Developer Certificate of Origin 1.1.
- [`../DISCLOSURE.md`](../DISCLOSURE.md) — SliceOps / reference-runtime relationship and IP transparency.
- [`../TRADEMARK.md`](../TRADEMARK.md) — trademark usage policy.
