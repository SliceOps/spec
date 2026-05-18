# Disclosure — SliceOps and reference runtimes

SliceOps™ is an open methodology authored by Andrés Ramírez Sierra. Trademark and copyright are held personally (pre-incorporation). The framework is intended for release under permissive open-source terms — documentation under CC BY 4.0, code templates under MIT (final terms pending an IP/Legal ratification; see `governance/IPR_POLICY.md`).

A reference runtime implementation of the SliceOps reference patterns exists, authored by the same IP holder. It is **one** reference implementation — the first, but not exclusive and not "official."

To preserve framework neutrality:

- The SliceOps spec does **not** include any runtime-internal artifacts (internal decision IDs, slice IDs, internal paths, runtime-specific schemas).
- Any conforming runtime must honor the SliceOps principles (per P8 — Platform-Agnostic).
- Other runtime implementations (adapters over third-party tools, custom homegrown brains) are architectural peers, not subordinates.
- SliceOps trademark licensing and any runtime's product licensing operate independently.

The methodology runs on any text-based AI agent + git + atomic-slice scoping + file-producing capability. No specific platform or runtime is a gate of entry.

For runtime selection guidance, see `examples/reference-implementations.md` (pending).
