# Disclosure — SliceOps and reference runtimes

SliceOps™ is an open framework authored by Andrés Ramírez Sierra. Trademark and copyright are held personally, pre-incorporation of SliceOps LLC. The framework is openly licensed: documentation under **Creative Commons Attribution 4.0 International (CC BY 4.0)** and code under the **MIT License**. These terms are ratified in decision record `DR-2026-06-15-sliceops-license-ratification`; see [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md) for the full intellectual-property and contribution policy and [`TRADEMARK.md`](TRADEMARK.md) for trademark usage.

## Author's dual role — disclosed deliberately

The person who authors and maintains SliceOps also authors one or more **runtime implementations** of it — software that puts the framework's reference patterns into practice. Each such runtime is **one** implementation among possible others — not exclusive, and not "official."

This concentration of authorship — the same hand on the open framework and on a runtime that implements it — is disclosed openly rather than left implicit. The framework's neutrality does not rest on assuming the author is disinterested; it is protected by the rules below.

## How framework neutrality is protected

- The SliceOps spec does **not** include any runtime-internal artifacts — internal decision IDs, slice IDs, internal paths, or runtime-specific schemas. The published spec is the framework, never a particular product's implementation of it.
- Any conforming runtime must honor the SliceOps principles (per **P8 — Platform-Agnostic**). The framework never requires a specific runtime.
- All runtime implementations — those authored by the framework's own author, adapters over third-party tools, and custom homegrown systems alike — are **architectural peers**, not subordinates. None is "the official" SliceOps runtime.
- A runtime's **product license is its own**, chosen by that runtime's vendor and independent of the framework's CC BY 4.0 / MIT terms. Likewise, the SliceOps trademark is licensed separately from the content — see [`TRADEMARK.md`](TRADEMARK.md).

The framework runs on any text-based AI agent, git, atomic-slice scoping, and file-producing capability. No specific platform or runtime is a gate of entry.

## References

- [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md) — intellectual-property and contribution policy (license terms, Inbound = Outbound, trademark separation).
- [`TRADEMARK.md`](TRADEMARK.md) — SliceOps™ trademark usage policy.
- [`LICENSE`](LICENSE) — Creative Commons Attribution 4.0 International (documentation).
- [`LICENSE-CODE`](LICENSE-CODE) — MIT License (code).
- Decision record `DR-2026-06-15-sliceops-license-ratification` — ratifies the CC BY 4.0 and MIT licensing and the trademark / copyright separation.
