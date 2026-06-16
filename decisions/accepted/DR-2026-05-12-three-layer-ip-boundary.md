# DR-2026-05-12 — Three-Layer IP Boundary

- **Status**: ratified
- **Date**: 2026-05-12
- **Topics**: ip-boundary, foundational, governance

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 Audit Plane, P4 Decision Integrity). This record publishes the decision; the supporting analysis is maintained internally.

## Decision

SliceOps intellectual property is organized into three layers:

- **Layer A — Principles.** The canonical principles that define the framework. SliceOps IP, licensed CC BY 4.0.
- **Layer B — Reference Patterns.** The reference implementation patterns: entity catalog, knowledge-category structure, folder structure, R-rules, frontmatter schemas, file templates. SliceOps IP, licensed CC BY 4.0 for documentation and MIT for code templates. Sub-layers: B.1 Framework Artifacts, B.2 Universal Engineering Patterns.
- **Layer C — Implementations.** Vendor and adopter runtimes that implement the framework. Owned by their vendors or adopters under their own licenses, not by SliceOps. Sub-layers: C.1 Vendor Runtimes, C.2 Adopter Stack Patterns.

**Runtime neutrality.** No runtime is "the" runtime. A runtime may extend the catalog with runtime-specific entities under its own IP, but the framework's principles and reference patterns (Layers A and B) remain SliceOps IP, shared across all runtimes (P8 — Platform-Agnostic). The SliceOps spec does not include runtime-internal artifacts.

**Boundary.** Adopters may customize Layer B patterns for their context, with attribution (CC BY 4.0), provided they honor the Layer A principles. A conformance claim ("SliceOps-compliant") requires honoring the published spec.

## References

- [`DISCLOSURE.md`](../../DISCLOSURE.md) — framework and reference-runtime relationship.
- [`spec/v1.0.0/ip-boundary.md`](../../spec/v1.0.0/ip-boundary.md) — the IP boundary in the versioned spec.
- [`DR-2026-06-15-sliceops-license-ratification.md`](DR-2026-06-15-sliceops-license-ratification.md) — the license decision.
- [`TRADEMARK.md`](../../TRADEMARK.md) — trademark usage policy.
