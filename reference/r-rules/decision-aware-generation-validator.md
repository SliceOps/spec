# Decision-Aware Generation Validator - R16+ Starter

This is an adopter-instantiable validator starter for teams that want CI to enforce that technical decision analysis affects generated code, tests, and evidence.

It is not part of the canonical R1-R14 starter pack. Adopters promote it as R16+ when their slice template, PR template, and Stack Pattern Pack conventions are stable enough to validate deterministically.

## Purpose

Prevent "decision analysis theater": a slice that writes the right words but generates code that ignores accepted decisions, material forces, or stack-pack gates.

The validator checks the connection between:

- accepted decisions
- universal materiality
- routed Stack Pattern Packs
- selected implementation path
- implementation binding
- evidence produced

## Trigger

Run on non-trivial slice PR descriptions, slice markdown files, or generated slice manifests that contain `## Technical decision analysis`.

Adopters define which file paths and PR labels are in scope.

When the CI job already knows the PR is non-trivial, it should run in required-section mode: fail if no `## Technical decision analysis` section exists. The reference toolkit exposes this as `--require-technical-decision-analysis`.

## Required Fields

| Field | Rule |
|---|---|
| Relevant decisions loaded | At least one accepted decision/profile/architecture reference, or an explicit `none found` note |
| Classification | One of the accepted relationship classifications |
| Material universal dimensions | Present before Stack Pattern Packs |
| Stack Pattern Packs loaded | Empty with rationale, or entries with category/path/rationale |
| Selected path | Non-empty path tied to loaded decisions and forces |
| Implementation binding | Required when any dimension is `material` or `DEC-required` |
| Evidence required | Non-empty for each material force |
| Revisit triggers | Required for `material`, `DEC-required`, `new-decision`, `exception`, `revisit`, or `conflicts` |

## Validation Rules

1. A non-trivial code-producing slice must contain `## Technical decision analysis`.
2. `Material universal dimensions` must appear before `Stack Pattern Packs loaded`.
3. A Stack Pattern Pack entry must include category or axis, pack id/path, and rationale.
4. A Stack Pattern Pack rationale must reference a universal force, accepted decision, or touched implementation area.
5. A material or `DEC-required` dimension must have an implementation binding row or bullet.
6. Implementation binding must name both a code/design artifact and an evidence artifact.
7. `DEC-required` must be paired with one of: new DEC, superseding DEC, scoped exception/waiver, revisit item, or human review required.
8. `new-decision`, `conflicts`, `exception`, and `revisit` classifications must not be marked as "No new DEC required" without an explicit waiver/disposition.
9. `TDD/test-first` must be paired with failing-first or test-first evidence.
10. `contract-first` must be paired with schema, API, event, SDK, generated-client, or consumer/provider contract evidence.
11. `characterization-first` must be paired with characterization tests or baseline behavior evidence.
12. `integration-first` must be paired with framework/database/provider/browser/deployment integration evidence.
13. `test-after with rationale` must include a rationale and cannot be used when any dimension is `DEC-required`.
14. The completed analysis must not contain unresolved placeholders such as `<...>`, `TBD`, or `TODO` in required fields.
15. If a PR changes files in a known stack area, and no Stack Pattern Pack is loaded, the analysis must explain why no pack was needed.

## Suggested Implementation

A conservative starter can parse markdown sections and use regex checks:

- Locate `## Technical decision analysis`.
- Check section ordering.
- Extract classification, analysis depth, feedback strategy, materiality levels, stack-pack entries, implementation binding, and decision action.
- Fail on incompatible combinations.

A stronger implementation can bind changed paths to adopter routing rules:

```yaml
path_routes:
  "src/**/*.cs":
    candidate_packs:
      - languages/csharp
      - frameworks/dotnet
  "src/**/*Controller.cs":
    candidate_packs:
      - frameworks/dotnet/aspnet-core
  "src/**/*DbContext.cs":
    candidate_packs:
      - frameworks/dotnet/ef-core
  "src/**/*.tsx":
    candidate_packs:
      - frameworks/react
```

If a changed path matches a route and no related pack appears, the validator asks for either a pack entry or an explicit "not needed" rationale.

## Non-Goals

This validator does not decide whether the chosen architecture is objectively correct. It verifies that the generated implementation is traceable to the accepted decision process.

It should not force every slice into heavy analysis. Low-risk conforming slices remain valid with light analysis when the evidence and no-pack rationale are coherent.

## Allowlist

Adopters may exempt:

- typo-only documentation changes
- formatting-only changes
- generated files with no behavioral or delivery impact
- emergency hotfixes, if a retroactive decision-aware generation note is required before close

## Relationship to R15

R15 checks that the decision analysis is internally coherent.

R16 checks that the analysis is consumed by generation.

Use R15 first. Add R16 when the adopter wants stronger protection against pattern-first or documentation-only compliance.
