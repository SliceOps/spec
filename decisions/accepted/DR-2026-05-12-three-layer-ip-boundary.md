---
entity: DecisionRecord
status: ratified
created: 2026-05-12
updated: 2026-06-22
owner: Andrés Ramírez Sierra
sensitivity: public
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DR-2026-06-15-sliceops-license-ratification, DR-2026-05-14-spec-repo-publishing-layout]
topics: [ip-boundary, foundational, hierarchical-taxonomy]
vocabulary-changes: []
consistency-check: "Establishes the three-layer IP boundary (A principles, B reference patterns, C implementations); DR-2026-06-15-sliceops-license-ratification operationalizes it as a dual license; DR-2026-05-14-spec-repo-publishing-layout organizes the Layer B.1 artifacts. No conflicts."
---

# DR-2026-05-12 — Three-Layer IP Boundary

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 Audit Plane, P1 Decision Integrity). This record publishes the decision; the supporting analysis is maintained internally.

## Decision

SliceOps intellectual property is organized into three layers:

- **Layer A — Principles.** The canonical principles that define the framework. SliceOps IP, licensed CC BY 4.0.
- **Layer B — Reference Patterns.** The reference implementation patterns: entity catalog, knowledge-category structure, folder structure, R-rules, frontmatter schemas, file templates. SliceOps IP, licensed CC BY 4.0 for documentation and MIT for code templates. Sub-layers: B.1 Framework Artifacts, B.2 Universal Engineering Patterns.
- **Layer C — Implementations.** Vendor and adopter runtimes that implement the framework. Owned by their vendors or adopters under their own licenses, not by SliceOps. Sub-layers: C.1 Vendor Runtimes, C.2 Adopter Stack Patterns.

**Runtime neutrality.** No runtime is "the" runtime. A runtime may extend the catalog with runtime-specific entities under its own IP, but the framework's principles and reference patterns (Layers A and B) remain SliceOps IP, shared across all runtimes (P11 — Platform-Agnostic). The SliceOps spec does not include runtime-internal artifacts.

**Boundary.** Adopters may customize Layer B patterns for their context, with attribution (CC BY 4.0), provided they honor the Layer A principles. A conformance claim ("SliceOps-compliant") requires honoring the published spec.

## Alternatives considered

- **A — Two layers (methodology + implementations)**: rejected — collapsing reference patterns into "methodology" leaves no clean home for reusable-but-non-canonical artifacts (templates, schemas, R-rules) and blurs what an adopter may customize versus what defines conformance.
- **B — Keep everything proprietary to one runtime**: rejected — couples the framework to a single vendor, violates P11 (Platform-Agnostic), and removes the pull-through, ecosystem value of an open spec.
- **C — Three layers (A principles / B reference patterns / C implementations)**: **selected** — cleanly separates what is canonical and shared (A, B) from what each runtime owns (C), and makes the conformance boundary explicit.

## References

- [`DISCLOSURE.md`](../../DISCLOSURE.md) — framework and reference-runtime relationship.
- [`spec/v1.0.0/ip-boundary.md`](../../spec/v1.0.0/ip-boundary.md) — the IP boundary in the versioned spec.
- [`DR-2026-06-15-sliceops-license-ratification.md`](DR-2026-06-15-sliceops-license-ratification.md) — the license decision.
- [`DR-2026-05-14-spec-repo-publishing-layout.md`](DR-2026-05-14-spec-repo-publishing-layout.md) — Layer B.1 publishing layout.
- [`TRADEMARK.md`](../../TRADEMARK.md) — trademark usage policy.
