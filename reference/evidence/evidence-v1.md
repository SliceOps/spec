# evidence.v1 — Canonical Evidence Record Format (Layer B.1)

> **P6 Evidence-by-Construction, made machine-readable.** The record every slice merge emits — and every gated operation may emit — so that "auditable" is a property a third party can verify from the record itself, not a claim. Ratified in [`DR-2026-07-02-evidence-v1-canonical-schema`](../../decisions/accepted/DR-2026-07-02-evidence-v1-canonical-schema.md).

Canonical schema: [`evidence.v1.schema.json`](evidence.v1.schema.json) (JSON Schema draft 2020-12, `$id` `https://sliceops.org/schemas/evidence/evidence.v1.schema.json`). Golden examples: [`examples/`](examples/).

## Purpose

P6 states that every slice produces evidence in four mandatory categories — functional, quality, decision, provenance — and P7 adds the per-slice security gate. Until this format existed in the open spec, that evidence had no canonical machine-readable shape: every runtime would emit its own record, and third-party verification degraded into trusting each vendor's tooling. **evidence.v1** is the vendor-neutral interchange record: one validatable JSON document per gated operation, hash-anchored to the artifacts it covers, categorized against P6/P7, and extensible by vendors only through a namespaced extension point.

## Position in the framework — evidence.v1 is a record format, NOT a cognitive entity

The cognitive entity catalog (Layer B.1, `reference/entity-catalog/`) is unchanged by this format. The corpus entity that anchors evidence at slice/Block scope is **[OutcomeRecord](../entity-catalog/03-outcome-record.md)** (entity #3, mapped to P6): its `evidence:` frontmatter field declares which categories are satisfied, and its body links the evidence produced in scope. evidence.v1 is what those links point to — the **per-operation interchange record** that carries the actual gate results. OutcomeRecord lives in the corpus and narrates *what happened*; evidence.v1 records live with the artifacts and prove *that the gates ran and what they found*. Neither replaces the other, and evidence.v1 does not extend the entity catalog.

## When records are emitted

| Trigger | Cardinality | Requirement |
|---|---|---|
| **Slice merge** (`operationType: slice-merge`) | one record per merged slice | **Mandatory** (P6: un-evidenced slices do not merge). The schema machine-enforces completeness: checks in all three check categories, ≥1 `decisionRefs` entry, and `provenance` with `sliceId` + `commitSha`. |
| **Gated operation** (validate, test-run, release, publish, infra-plan, infra-apply, cicd-run, …) | one record per operation run | Recommended. Emitted whenever an operation passes through a gate whose outcome should be auditable. `provenance` MAY be omitted when the operation runs outside a slice. |

Checks that did not execute are recorded with status `skipped` — enumerated, never silently absent. A record with `status: failed` (or `redaction.status: failed`) must fail the gate that consumes it.

## Field-by-field

| Field | Required | Type | Meaning |
|---|---|---|---|
| `schemaVersion` | yes | const `sliceops.evidence/v1` | Format identity and version pin. Breaking changes bump to `sliceops.evidence/v2`. |
| `evidenceId` | yes | slug string | Stable unique id of the record within the emitting corpus. |
| `operationType` | yes | lowercase token | The gated operation that produced the record. `slice-merge` is canonical and triggers the P6 completeness constraints; other tokens are open (vendor operation vocabularies are Layer C). |
| `status` | yes | enum `passed\|failed\|inconclusive\|skipped\|stale\|blocked` | Overall outcome. P6 hard gate: merge requires `passed`. |
| `actor` | yes | `{type: human\|agent\|tool\|system, id}` | Who/what executed the operation — provenance category (agent attribution). |
| `startedAt` / `finishedAt` | yes | RFC 3339 date-time | Execution window — provenance category (timestamps). |
| `artifacts[]` | yes | `{kind, id, path?, hash}` | Hash-anchored artifacts the evidence covers (hex digest: SHA-256 recommended; SHA-384 and SHA-512 accepted). What makes the record third-party recomputable. |
| `checks[]` | yes | `{id, category, status, severity, message?}` | Categorized gate results. `category` is `functional` or `quality` (P6) or `security` (P7). |
| `traceRefs[]` | no | `{executionId, traceHash}` | Hash-anchored execution traces — drift tests, eval suites, agentic runs. |
| `provenance` | conditional | `{sliceId, commitSha, sessionRef?}` | P6 provenance category. Required (with `sliceId` + `commitSha`) on `slice-merge`. `sliceId` uses the canonical pattern `BL-NN[.SEC-NN].SL-NNN[a-z]`. |
| `decisionRefs[]` | conditional | canonical decision ids | P6 decision category: the DECs / InsightRecords this evidence supports or was produced alongside (`DR-YYYY-MM-DD-slug` or counter ids like `DEC-021`, `INS-014`). Required (min 1) on `slice-merge`. |
| `redaction` | yes | `{status: applied\|not-needed\|failed, rules[]}` | Secrets-redaction attestation (P7 secrets policy: secrets never enter evidence, logs, or the audit plane). |
| `extensions` | no | namespaced object | Vendor/adopter extension point — see below. |

Unknown top-level fields are rejected (`additionalProperties: false`): anything non-canonical goes under `extensions`, or it is not a valid evidence.v1 record.

## Category mapping to P6 / P7

| P6/P7 category | Where it lives in the record | Slice-merge gate |
|---|---|---|
| **Functional** (P6) | `checks[]` with `category: functional` | ≥1 entry required (schema-enforced) |
| **Quality** (P6) | `checks[]` with `category: quality` | ≥1 entry required (schema-enforced) |
| **Security** (P7) | `checks[]` with `category: security` (SAST, secrets scan, dependency vulnerabilities, hallucinated-dependency check, …) plus the `redaction` attestation | ≥1 entry required (schema-enforced) |
| **Decision** (P6) | `decisionRefs[]` | ≥1 entry required (schema-enforced) |
| **Provenance** (P6) | `provenance` (`sliceId`, `commitSha`, `sessionRef`) + `actor` + `startedAt`/`finishedAt` + `artifacts[].hash` | `provenance.sliceId` + `provenance.commitSha` required (schema-enforced) |

The schema enforces the *shape* of completeness (categories present). Whether specific checks are sufficient (coverage thresholds, which SAST rules, which eval suites) is process policy — adopter R-rules and CI gates decide that, per stack (P6 implication: each tech stack defines its test taxonomy).

## Vendor extensions (Layer C)

The canonical schema deliberately carries **no vendor internals** — no vendor bundle references, no runtime-specific enums, no product schemas (per the neutrality rule in [`spec/v1.0.0/ip-boundary.md`](../../spec/v1.0.0/ip-boundary.md): the spec includes no runtime-specific schemas). Vendors and adopters extend the record through the `extensions` object:

- Keys MUST be reverse-DNS-style namespaces (at least one dot, e.g. `dev.example.runtime`), so extension ownership is explicit and collisions are impossible.
- Extension content is the extension owner's IP (Layer C per the three-layer IP boundary) and is **ignored by canonical validators** — they validate key shape only.
- Extensions MUST NOT override or re-define canonical field semantics. A record that needs different semantics for a canonical field is not an evidence.v1 record.
- A vendor runtime that binds evidence to its own versioned rule bundles, trace stores, or product entities carries those references inside its namespace under `extensions`.

## Signing and verification — what v1 does and does not define

Scrupulous honesty about the "signed, third-party-verifiable" claim:

- **evidence.v1 records carry no embedded signature field in v1.** There is no `signature` property, deliberately: embedding a signature inside the signed document forces canonicalization machinery (e.g. JCS) into every emitter and verifier, and locks the format to one crypto mechanism.
- **The spec defines what must be attestable, not one crypto mechanism.** The record is designed to be *hash-anchored*: every artifact and trace it covers is referenced by content digest, so the record's claims are recomputable from the artifacts alone.
- **Recommended pattern — detached signature over the bundle.** Pack the evidence record together with (or alongside) the artifacts/manifest it covers, and produce a detached signature over that bundle or its manifest — e.g. an ed25519 signature, or a sigstore/cosign attestation with transparency-log inclusion. The evidence record is hash-anchored *to* the signed bundle, not self-signed.
- **Third-party verification** is then three independent, tool-agnostic steps:
  1. **Schema validation** — the record validates against `evidence.v1.schema.json` (including the slice-merge completeness constraints).
  2. **Hash recomputation** — recompute the digests of the covered artifacts/traces and compare against `artifacts[].hash` / `traceRefs[].traceHash`.
  3. **Signature verification** — verify the detached signature/attestation over the bundle containing the record, against the emitter's published key or certificate identity.

A future `sliceops.evidence/v2` MAY standardize a signature envelope once one mechanism earns canonical status; v1 keeps the crypto pluggable and the record honest about it.

## Versioning

`schemaVersion` is a const: `sliceops.evidence/v1`. Additive, backward-compatible schema revisions (new optional fields) land via DEC without changing the const; anything breaking (renames, new required fields, semantic changes) is `sliceops.evidence/v2` with a new `$id`. Emitters MUST NOT emit fields outside the schema (they will fail validation); consumers MUST NOT rely on extension content of namespaces they do not own.

## Anti-patterns

- **Slice-merge record without all categories** — a `slice-merge` record missing functional/quality/security checks, `decisionRefs`, or `provenance` fails schema validation by design; do not downgrade the operation type to dodge the gate (that is P6 theater).
- **Raw payloads in evidence** — logs, request bodies, or secrets pasted into the record. Rejected structurally (`additionalProperties: false`) and by policy (`redaction`, P7).
- **Vendor fields at the top level** — vendor data outside `extensions` makes the record invalid; namespace it.
- **Self-signed-inside claims** — asserting third-party verifiability from the record alone, without a detached signature over the bundle. The record proves gate results; the signature proves who attests them.
- **Evidence emitted but never anchored** — records that no OutcomeRecord links and no gate consumes ("write-only evidence") — evidence exists to be selected, filtered, and verified (P6: audit = select date range, filter, evidence present by construction).
