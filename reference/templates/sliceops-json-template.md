# `sliceops.json` — adoption manifest templates (DEC-0011_6)

Written by scaffolding and migrations; read by validators and runtimes. Never a
hand-maintained document surface. The local `_sliceops` name is what detects
(DEC-0011_1); this manifest pins the spec version and declares extensions.

## Container form (at the `_sliceops` root)

```json
{
  "spec": "2.0.0",
  "corpus": "engineering | organization",
  "vendor": "none",
  "extensions": {}
}
```

- `spec` — the spec version the corpus claims conformance with (validators validate against it).
- `corpus` — the corpus type. Vendors MAY define additional types for their runtime products (Layer C — declared here, specified in their own corpora).
- `vendor` — the runtime vendor operating this corpus, or `none`.
- `extensions` — which free decades (80, 90) and vendor layers exist, and who claims them: `{"<free slot or layer>": "<claimant>"}`. A verifiable conformance claim: canonical decades are never declared (they are the framework's).

## Pointer form (at a code repository root inside a workspace)

```json
{
  "ref": "../_sliceops",
  "remote": "<git url of the container repository>"
}
```

- `ref` — the local path to the workspace container (sibling checkout).
- `remote` — where continuous integration can fetch the container when the sibling is absent (DEC-0011's container checkout step).
