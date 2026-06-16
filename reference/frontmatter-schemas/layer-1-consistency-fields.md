# Layer 1 Consistency Fields — Layer B.1

The **mandatory consistency-management frontmatter** for every DecisionRecord (Layer 1 of the consistency-management mechanism). These fields make corpus consistency machine-checkable and force the author to articulate consistency thinking explicitly rather than implicitly.

```yaml
# (base fields per base-schema.md, plus:)

supersedes: [<DEC id>...]          # explicit supersession edges
superseded-by: <DEC id> | null

conflicts-with: [<DEC id>...]      # DECs this could appear to contradict
related-decs: [<DEC id>...]         # topically adjacent / overlapping
topics: [<canonical topic>...]      # from the topic taxonomy (min 1, typical 2–5)
vocabulary-changes: [<term>...]     # canonical terms introduced/modified → triggers glossary update
consistency-check: |                 # mandatory multi-line paragraph
  How this DEC relates to the existing corpus: what is preserved,
  what changes, which conflicts (if any) are resolved and how.
  References specific DEC ids from related-decs.
```

## Field semantics

| Field | Meaning | If non-empty → |
|---|---|---|
| `conflicts-with` | DECs that could *appear* to contradict this one | body MUST include a "Conflict Resolution" section explaining each (supersession / sub-scoping / complementarity) |
| `related-decs` | Topically adjacent DECs | bidirectional: referenced DECs' frontmatter should reference back |
| `topics` | Canonical taxonomy tags | enables corpus indexing + topic-related conflict detection |
| `vocabulary-changes` | New/changed canonical terms | each term added to the glossary in the same slice |
| `consistency-check` | Author's explicit consistency declaration | empty `conflicts-with` (preferred) still requires a paragraph confirming coexistence intent |

## The Layer 2 pre-merge checklist (companion)

Layer 1 fields are completed alongside the Layer 2 manual pre-merge checklist (human/HITL gate, P9): searched topic-related DECs · read the top-related ones end-to-end · declared conflicts + resolutions · updated bidirectional cross-references · updated glossary/topics if vocabulary changed · self-application test (this DEC's own frontmatter satisfies this spec).

## Self-application

This spec is itself subject to it: a DEC amending these fields must carry these fields. The mechanism applies recursively from day one (reduces the meta-paradox).

## Enforcement

R3 validates presence + well-formedness. Higher layers (CI validators — see the toolkit) validate bidirectional integrity, topic-tag membership, glossary coverage, and supersession-chain acyclicity.
