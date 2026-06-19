# SliceOps™ IP Boundary & Layer Taxonomy — v1.0.0

SliceOps is articulated in **three IP layers** with a stable top level and extensible sub-numbering. This document is the canonical statement of what is SliceOps IP, what is reference pattern, and what belongs to vendors/adopters.

---

## The three layers

| Layer | Definition | Ownership | License |
|---|---|---|---|
| **Layer A — Principles** | The 12 canonical framework principles (P1–P12). The set without which it is not SliceOps. | SliceOps IP | CC BY 4.0 |
| **Layer B — Reference Patterns** | Patterns that materialize the principles and reaffirmed universal engineering practices. | SliceOps IP | CC BY 4.0 (docs) and MIT (code templates) |
| **Layer C — Implementations** | Specific implementations — vendor runtimes and adopter stack patterns. | Per vendor / adopter | Vendor / adopter choice |

> **Licensing status**: the intended licensing above is pending an IP/Legal ratification. No `LICENSE` file is published in this repository yet by design. See `../../governance/IPR_POLICY.md` and `../../DISCLOSURE.md`.

### Layer A — Principles (Framework)

The 12 canonical principles (see `principles.md`). The set is **non-negotiable**: an implementation that violates any one is not SliceOps-compliant. Amendment requires a superseding DEC under an elevated human-in-the-loop gate (P3).

### Layer B — Reference Patterns

Operational materializations of the principles. Adopters may customize Layer B patterns (rename, extend, adapt) for their context while honoring Layer A principles; customizations require attribution per the documentation license.

### Layer C — Implementations

Vendor-specific runtimes and adopter-specific stack patterns. **Runtime-specific entity types** — entities whose meaning depends on a runtime to operate — are NOT SliceOps Layer B, because they do not operate without that specific runtime. Vendors may extend the canonical catalog with runtime-specific entities under their own IP.

---

## Sub-numbering (extensible)

Top-level Layer A/B/C describe the **IP/scope boundary axis** and are **immutable** except by a major superseding DEC (elevated HITL gate). Sub-layers describe categories within each top level. Naming convention: `<Top>.<N>` (e.g., B.1, B.2, C.1, C.2). Sub-numbers are incremental and are not recycled.

### Layer A — sub-layers
Currently none; P1–P12 are monolithic. Future principle dimensions (e.g., compliance principles, ethics principles) could be added as A.1, A.2 via DEC.

### Layer B — sub-layers

| Sub-layer | Content |
|---|---|
| **B.1 — Framework Artifacts** | The 13-entity cognitive catalog, repo folder structure, R-rules system, counter discipline, frontmatter schemas, file templates, vocabulary discipline mechanism, sizing artifacts, model triage. SliceOps-originated. |
| **B.2 — Universal Engineering Patterns** | SOLID, ACID, Outbox, Fail-Fast, Idempotency, Defense in Depth, CI/Pipeline Cost Economy, Determinism-over-Regeneration. Industry-canonical, reaffirmed; vendor-agnostic, stack-agnostic. |

Future potential: **B.3 — Compliance Pattern Mappings**; **B.4 — Domain Pattern Libraries**.

### Layer C — sub-layers

| Sub-layer | Content | Ownership |
|---|---|---|
| **C.1 — Vendor Runtimes** | Runtime products implementing the SliceOps catalog (hosted knowledge-graph products, third-party tool adapters, custom homegrown brains). | Per vendor |
| **C.2 — Adopter Stack Patterns** | Adopter-defined patterns instantiable per technology stack, enforced via tooling (analyzers / lint rules / CI gates). | Per adopter |

Future potential: **C.3 — Adopter Compliance Mappings**; **C.4 — Adopter Domain Specializations**.

### Evolution rules

1. Top-level Layer A/B/C are immutable except by a major superseding DEC under an elevated HITL gate.
2. Sub-layers are added via DEC without touching parents (additive evolution).
3. Sub-layer naming `<Parent>.<N>`, incremental, never recycled on deprecation.
4. A sub-layer that grows substantial and qualitatively distinct may be **promoted to a top level** via DEC (e.g., compliance mappings becoming "Layer D").
5. New top-level Layers (D, E, …) are reserved for dimensions truly orthogonal to the IP/scope axis; require a DEC with strong justification ("why not a sub-layer?").
6. Default convention: bare "Layer B" = the full layer (all sub-layers); for a specific sub-layer use "B.1" or "B.2".
7. Cross-references in DECs must use precise sub-numbering when relevant (P12).

---

## The 13-entity catalog (Layer B.1)

The canonical cognitive entity catalog is **SliceOps IP, shared across vendors** (CC BY 4.0): DecisionRecord, InsightRecord, OutcomeRecord, Capability, Goal, LearningPattern, CognitiveFramework, ContextPack, ActivePriority, RelationshipContext, Preference, Value, **Session**. Each entity has a frontmatter schema, lifecycle, cross-reference patterns, and anti-patterns (see `../../reference/entity-catalog/`).

### Why the catalog is shared SliceOps IP, not vendor-proprietary

- **Schemas are weakly protectable by copyright** — naming entities "Account/Contact/Opportunity" or "blocks" has never been enforceable IP. Catalog-as-moat is weak protection regardless.
- **Real runtime differentiation is runtime quality** — hosted operation, AI integration, sync, enterprise features, compliance certifications — not schema ownership.
- **Mainstream adoption requires a catalog default** — purely abstract frameworks stay niche; a shared default catalog is what makes an ecosystem (precedent: SQL standard and vendor runtimes, container concepts and orchestrators).

Operating analogy: a public production methodology (Lean / Toyota Production System) vs the private blueprints of a specific product. The methodology is public; specific product internals are private.

### Adopter customization rules

Adopters **may**: use the catalog as-is (recommended — preserves cross-adopter interop); add adopter-specific entities (extends the catalog; lives in the adopter's own brain, NOT in the SliceOps spec); fork with renames/extensions (requires attribution and documenting the customization in adopter DECs).

Adopters **may not**: remove canonical entities and still claim SliceOps-compliance (breaks interop); conflict canonical entity semantics (e.g., redefine DecisionRecord to mean "user preferences").

---

## Framework neutrality & disclosure

SliceOps is an open framework authored by [Andrés Ramírez Sierra](https://andres.co); trademark and copyright held personally. A reference runtime implementation of the SliceOps reference patterns exists, authored by the same IP holder — it is **one** reference implementation: the first, but not exclusive and not "official."

To preserve ecosystem neutrality (a bright line maintained even though one party holds IP across both the framework and a runtime):

- The SliceOps spec does **not** include any runtime-internal artifacts (internal decision IDs, slice IDs, internal filesystem paths, runtime-specific schemas, vendor product internals).
- Any conforming runtime must honor the SliceOps principles (P11 — Platform-Agnostic). A runtime may extend the catalog with runtime-specific entities under its own IP, but may not capture catalog ownership as a product feature, claim "SliceOps is X-only," or position other implementations as "unofficial/non-compliant" without evidence.
- Other runtime implementations are architectural peers, not subordinates.
- SliceOps trademark licensing and any runtime's product licensing operate independently.

For runtime selection guidance, see `../../examples/reference-implementations.md` (drafting).

---

## Future-proofing (taxonomy scales without breaking)

| Scenario | Resolution via taxonomy |
|---|---|
| Compliance mappings mature | New sub-layer **B.3** (reference patterns) — or top-level **Layer D — Compliance** if it spans A, B, and C |
| Domain vertical packs (banking/healthcare/gov) | **B.4 — Domain Pattern Libraries** and **C.3 — Adopter Domain Specializations** |
| Certification / curriculum | **Layer E — Education Layer** (truly distinct dimension from IP/scope) |

In every scenario the taxonomy scales **without breaking changes** — no top-level renaming. Precedent: the periodic table (stable groups, new elements added without renaming) and Linnaean taxonomy (hierarchy extends without renaming top ranks).
