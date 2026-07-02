---
entity: DecisionRecord
status: ratified
created: 2026-07-02
updated: 2026-07-02
owner: Andrés Ramírez Sierra
approver: Andrés Ramírez Sierra
sensitivity: public
supersedes: []
superseded-by: null
conflicts-with: []
related-decs: [DR-2026-05-12-three-layer-ip-boundary, DR-2026-07-02-author-approver-separation, DR-2026-06-30-build-complexity-measurement-model]
topics: [evidence-categories, audit-plane, layer-b-framework-artifact, ip-boundary]
vocabulary-changes: [evidence.v1]
consistency-check: "Ratifies evidence.v1 as the canonical Layer B.1 evidence record format — the machine-readable expression of P6 (four evidence categories) and P7 (security gate). Preserves the three-layer boundary of DR-2026-05-12-three-layer-ip-boundary: the canonical schema carries no vendor internals; vendor content extends only through the namespaced extensions object (Layer C). Complements OutcomeRecord (entity catalog #3): evidence.v1 is the per-operation interchange record OutcomeRecords link to, not a new cognitive entity — the entity catalog is unchanged. First spec DR to record the approver field introduced by DR-2026-07-02-author-approver-separation (explicit self-ratification, single-maintainer context). vocabulary-changes lists evidence.v1; the glossary is versioned spec content, so its entry lands with the next spec minor version — a declared deferral (see Consequences), not an omission. No conflicts."
---

# DR-2026-07-02 — evidence.v1 Canonical Evidence Record Format (Layer B.1)

> A SliceOps DecisionRecord about SliceOps itself — recursive dogfooding (P2 Audit Plane, P1 Decision Integrity). This is the **first spec DR to carry the `approver` frontmatter field** introduced alongside [`DR-2026-07-02-author-approver-separation`](DR-2026-07-02-author-approver-separation.md) — per that RFC's single-maintainer rule, self-ratification is recorded explicitly (`approver` == `owner`) rather than left implicit (founder directive, 2026-07-02).

## TL;DR

The evidence record — the framework's flagship audit-plane artifact — now has a canonical, open, machine-validatable definition: **evidence.v1** ([`reference/evidence/evidence.v1.schema.json`](../../reference/evidence/evidence.v1.schema.json), JSON Schema draft 2020-12, plus prose spec and golden examples). It expresses P6's four evidence categories and P7's security gate as one interchange record per slice merge / gated operation. Vendors extend it only through a namespaced `extensions` object (Layer C); the canonical core carries no vendor internals.

## Context

A 2026-07 external red-team audit found (finding #1) that the evidence artifact pitched as the framework's star claim — a signed, third-party-verifiable record per slice — existed only in vendor marketing, not in the open spec. P6 mandates four evidence categories and P7 a per-slice security gate, but the spec defined no record format carrying them: adopters could not validate evidence, and third parties could not verify it, without trusting some vendor's tooling. The absence was an **omission, not an IP reservation** — the maintainer's internal decision corpus had already derived evidence/security schemas as Layer B open artifacts in 2026-06. A framework claiming Evidence-by-Construction cannot leave the evidence record itself unspecified: what the audit plane cannot verify, the framework cannot claim (P2).

## Decision

**evidence.v1 is ratified as the canonical Layer B.1 evidence record format**, published at [`reference/evidence/`](../../reference/evidence/):

1. **Format**: JSON Schema draft 2020-12, `$id` `https://sliceops.org/schemas/evidence/evidence.v1.schema.json`, `schemaVersion` const `sliceops.evidence/v1`. Prose spec: [`evidence-v1.md`](../../reference/evidence/evidence-v1.md). Golden examples (valid + invalid): [`examples/`](../../reference/evidence/examples/).
2. **Emission**: one record per **slice merge** (mandatory, P6 — un-evidenced slices do not merge) and one per **gated operation** (recommended).
3. **P6/P7 mapping**: `checks[]` entries carry `category: functional | quality | security` (functional and quality per P6, security per P7); `decisionRefs[]` carries the decision category; the `provenance` object (slice ID, commit SHA, session ref) plus `actor` and timestamps carries the provenance category. On `slice-merge` the schema machine-enforces completeness: all three check categories present, ≥1 decision ref, provenance with `sliceId` + `commitSha`.
4. **Canonical ID patterns**: `sliceId` uses `BL-NN[.SEC-NN].SL-NNN[a-z]`; decision refs use `DR-YYYY-MM-DD-slug` or counter-based ids (`DEC-NNN`, `INS-NNN`).
5. **Vendor extension mechanism (Layer C)**: the canonical schema carries **no** vendor bundle references, runtime-specific enums, or product schemas (neutrality rule, [`spec/v1.0.0/ip-boundary.md`](../../spec/v1.0.0/ip-boundary.md)). Vendors/adopters MAY add extension content under reverse-DNS-namespaced keys in the `extensions` object, under their own IP; canonical validators validate key shape and ignore extension content.
6. **Signing**: evidence.v1 records carry **no embedded signature field**. The spec defines what must be attestable — hash-anchored artifacts and traces — and recommends a detached signature (e.g. ed25519, sigstore) over the artifact bundle/manifest containing the record. Third-party verification = schema validation + hash recomputation + signature verification over the bundle.
7. **Not a cognitive entity**: evidence.v1 is an interchange **record format**; the corpus entity anchoring evidence categories remains [`OutcomeRecord`](../../reference/entity-catalog/03-outcome-record.md). The entity catalog is unchanged.
8. **Vendor realignment**: the pre-existing vendor implementation of this record format (whose existence is public fact per [`DISCLOSURE.md`](../../DISCLOSURE.md) — the relationship is named, its internals are not) has committed in its own decision corpus to realign to this upstream canonical schema, carrying its vendor-specific fields as a namespaced extension.

## Alternatives considered

- **A — Leave the evidence format vendor-defined (status quo)**: rejected — the audit showed the pitch-level artifact was unverifiable from the open corpus; per-vendor record formats fragment third-party verification and reduce P6 to marketing.
- **B — Upstream the existing vendor schema verbatim**: rejected — it carries vendor bundle references and vendor operation enums into the canonical layer, violating the IP-boundary neutrality rule (the spec includes no runtime-specific schemas) and taxing every other adopter with one vendor's semantics.
- **C — Genericized canonical core + namespaced vendor extensions**: **selected** — the canonical fields express exactly P6/P7; vendor semantics live under `extensions` as vendor IP (Layer C); every adopter gets one validatable interchange format and vendors keep full freedom inside their namespace.
- **D — Add evidence as a new cognitive entity in the catalog**: rejected — the catalog holds corpus/cognitive entities; evidence.v1 is a per-operation interchange record anchored by OutcomeRecord. Inflating the catalog would add no semantics and break entity-count coherence across the corpus.

## Consequences

**Enables**: third-party verification of the framework's flagship claim from the open spec alone (schema + hash recomputation + detached signature); a single interchange format across runtimes; machine-enforced P6 completeness at slice merge; vendor differentiation moved to where it belongs (Layer C `extensions`).
**Constrains**: conforming emitters cannot put non-canonical fields at the record's top level; vendor operation vocabularies and bundle references live only under namespaced extensions; breaking format changes require `sliceops.evidence/v2`.
**Costs**: maintaining the schema + golden examples in the spec repo; the recommended signing pattern is guidance, not yet a conformance-testable profile.

**Declared follow-ups** (not blocking this DEC):

1. **Glossary**: the `evidence.v1` term enters [`spec/v1.0.0/glossary.md`](../../spec/v1.0.0/glossary.md) with the next spec minor version — versioned spec content is not edited by a Layer B slice.
2. **`$id` hosting**: serving the schema at `https://sliceops.org/schemas/evidence/evidence.v1.schema.json` is a website follow-up; until live, the `$id` is the identifier, and the file in this repository is the canonical source.

## References

- [`spec/v1.0.0/principles.md`](../../spec/v1.0.0/principles.md) — P6 Evidence-by-Construction (the four categories), P7 Security-by-Construction (the security gate this record carries).
- [`spec/v1.0.0/ip-boundary.md`](../../spec/v1.0.0/ip-boundary.md) — Layer B.1 (framework artifacts) and Layer C (vendor extensions); the neutrality rule excluding runtime-specific schemas.
- [`reference/evidence/evidence.v1.schema.json`](../../reference/evidence/evidence.v1.schema.json), [`reference/evidence/evidence-v1.md`](../../reference/evidence/evidence-v1.md), [`reference/evidence/examples/`](../../reference/evidence/examples/) — the ratified artifacts.
- [`reference/entity-catalog/03-outcome-record.md`](../../reference/entity-catalog/03-outcome-record.md) — the cognitive entity that anchors evidence categories in the corpus.
- [`DR-2026-05-12-three-layer-ip-boundary.md`](DR-2026-05-12-three-layer-ip-boundary.md) — the layer taxonomy this DEC applies to the evidence record.
- [`DR-2026-07-02-author-approver-separation.md`](DR-2026-07-02-author-approver-separation.md) — the `approver` field this DEC is the first spec DR to dogfood.
- [`DISCLOSURE.md`](../../DISCLOSURE.md) — the posture for naming the framework↔runtime relationship without naming runtime internals.
- Origin: 2026-07 external red-team audit (finding #1: the evidence artifact existed only in vendor marketing, absent from the open spec).
