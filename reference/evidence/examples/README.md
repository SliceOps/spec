# evidence.v1 golden examples

Golden fixtures for [`../evidence.v1.schema.json`](../evidence.v1.schema.json). Files prefixed `valid-` MUST validate; files prefixed `invalid-` MUST fail validation — use both sets to test any validator implementation. See [`../evidence-v1.md`](../evidence-v1.md) for the prose spec.

| File | Expectation | Demonstrates |
|---|---|---|
| `valid-minimal-gated-operation.evidence.v1.example.json` | valid | The smallest legal record: a gated operation (`validate`) outside a slice — required fields only, no `provenance`/`decisionRefs`. |
| `valid-full-slice-merge.evidence.v1.example.json` | valid | The flagship P6 record: `slice-merge` with all four evidence categories + the P7 security gate — functional/quality/security checks, `decisionRefs` (decision), `provenance` (slice ID, commit SHA, session ref), traces, and a namespaced vendor `extensions` block (Layer C). |
| `invalid-slice-merge-missing-security.evidence.v1.example.json` | invalid | `slice-merge` completeness is machine-enforced: no `category: security` check → schema rejection (P7 gate absent). |
| `invalid-bad-provenance-commit.evidence.v1.example.json` | invalid | `provenance.commitSha` must be a 7–40 char lowercase hex SHA; `"not-a-valid-sha"` is rejected. |
| `invalid-unknown-top-level-field.evidence.v1.example.json` | invalid | `additionalProperties: false` at the top level: non-canonical fields (`rawPayload`) are rejected — vendor/adopter data belongs under a namespaced key in `extensions`. |

All identifiers use the canonical patterns: slice IDs `BL-NN[.SEC-NN].SL-NNN[a-z]`, decision refs `DR-YYYY-MM-DD-slug` or counter ids (`DEC-021`, `INS-014`). Hashes are deliberately fake repeated-digit placeholders.
