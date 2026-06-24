# Decision Analysis Materiality Validator - R15+ Starter

This is an adopter-instantiable validator starter for teams that want CI to enforce Decision Framework usage in slice PRs.

It is not part of the canonical R1-R14 starter pack. Adopters promote it as R15+ when their slice/PR template is stable enough to validate deterministically.

## Purpose

Prevent decision-aware triage from becoming optional prose.

The validator checks that a non-trivial slice records:

- Relationship classification.
- Analysis depth.
- Materiality levels.
- Feedback strategy.
- Evidence for material dimensions.
- Human/DEC disposition when required.
- Stack Pattern Pack routing after the universal materiality pass.
- Implementation binding for material dimensions, when the slice generates code.

## Trigger

Run on slice PR descriptions, slice markdown files, or DEC sections that contain `## Technical decision analysis`.

Adopters define which files are in scope.

When the CI job already knows the PR is non-trivial, it should run in required-section mode: fail if no `## Technical decision analysis` section exists. The reference toolkit exposes this as `--require-technical-decision-analysis`.

## Required fields

| Field | Accepted values or rule |
|---|---|
| `Classification` | `conforms`, `extends`, `new-decision`, `conflicts`, `exception`, `revisit` |
| `Analysis depth` | `light`, `focused`, `full` |
| Materiality level | `N/A`, `low`, `material`, `DEC-required` |
| `Feedback strategy` | `acceptance-first`, `TDD/test-first`, `contract-first`, `characterization-first`, `integration-first`, or `test-after with rationale` |

## Validation rules

1. A technical decision analysis must declare `Classification`.
2. A technical decision analysis must declare `Analysis depth`.
3. At least one materiality level must be present.
4. If any dimension is `material`, the evidence section must name non-empty evidence.
5. If any dimension is `DEC-required`, the decision action must require human review, a new/superseding DEC, a scoped exception, or a revisit item.
6. If classification is `new-decision`, `conflicts`, `exception`, or `revisit`, `Analysis depth` must be `full`.
7. If classification is `conforms` and all dimensions are `N/A` or `low`, `Analysis depth` may be `light`.
8. Stack Pattern Packs must be listed after material universal dimensions, not before them.
9. If the section declares Stack Pattern Packs, each pack entry must include category/path and a rationale tied to a material or low dimension.
10. If a material or `DEC-required` dimension exists in a code-producing slice, `Implementation binding` must map it to a code/design artifact and an evidence artifact.
11. If feedback strategy is `TDD/test-first`, evidence must include failing-first or test-first evidence.
12. If feedback strategy is `test-after with rationale`, the rationale must be non-empty.
13. Template placeholders such as `<...>` must not remain in a completed slice analysis.

## Non-goals

This validator does not judge whether the selected technical path is correct. It only checks that the decision process is present and internally coherent.

## Allowlist

Adopters may exempt:

- Typo-only documentation changes.
- Generated files with no behavioral, runtime, data, security, compatibility, or delivery impact.
- Emergency hotfixes, if a retroactive Decision Analysis is required before close.

## Implementation sketch

A starter implementation can use markdown parsing or conservative regex checks:

- Detect `## Technical decision analysis`.
- Read the section until the next `##`.
- Search for required labels and accepted values.
- Fail if required fields are missing or incompatible.

For stronger enforcement, bind the validator to the adopter's PR template schema or slice file schema.
